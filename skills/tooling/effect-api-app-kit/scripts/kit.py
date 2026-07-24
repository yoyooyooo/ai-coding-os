#!/usr/bin/env python3
"""Experimental atomic Effect-oriented capability-slice scaffolder."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
import uuid
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover
    raise SystemExit("PyYAML is required") from exc

KIT_VERSION = "0.2.0-experimental.1"
MANIFEST_REL = Path(".evo-kit/manifest.yaml")
LOCK_REL = Path(".evo-kit/lock")


def sha256_text(text: str) -> str:
    return "sha256:" + hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_file(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def load_yaml(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"expected YAML object: {path}")
    return data


def dump_yaml(data: Any) -> str:
    return yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=1000)


def validate_token(name: str, value: Any) -> str:
    if not isinstance(value, str) or not value or any(c not in "abcdefghijklmnopqrstuvwxyz0123456789-" for c in value) or not value[0].isalnum():
        raise ValueError(f"{name} must be kebab-case: {value!r}")
    return value


def validate_spec(spec: dict[str, Any]) -> None:
    if spec.get("schema_version") != 1:
        raise ValueError("schema_version must be 1")
    change = spec.get("change") or {}
    host = spec.get("host") or {}
    slice_ = spec.get("slice") or {}
    validate_token("change.id", change.get("id"))
    if change.get("operation") != "add-slice":
        raise ValueError("only change.operation=add-slice is implemented")
    validate_token("host.name", host.get("name"))
    host_path = host.get("path")
    if not isinstance(host_path, str) or not host_path or Path(host_path).is_absolute() or ".." in Path(host_path).parts:
        raise ValueError("host.path must be a safe relative path")
    for key in ("module", "subject", "operation"):
        validate_token(f"slice.{key}", slice_.get(key))
    if slice_.get("pressure") not in {"P0", "P1", "P2", "P3"}:
        raise ValueError("slice.pressure must be P0-P3")
    if slice_.get("persistence") not in {"none", "memory", "postgres"}:
        raise ValueError("slice.persistence must be none|memory|postgres")
    if slice_.get("effect_profile") not in {"installed", "v3", "v4"}:
        raise ValueError("slice.effect_profile must be installed|v3|v4")
    if slice_["pressure"] in {"P1", "P2", "P3"} and slice_["persistence"] == "none":
        raise ValueError(f"{slice_['pressure']} requires an explicit persistence seam (memory or postgres)")
    if slice_["pressure"] in {"P2", "P3"}:
        cap = spec.get("external_capability")
        if not isinstance(cap, dict):
            raise ValueError(f"{slice_['pressure']} requires external_capability")
        validate_token("external_capability.name", cap.get("name"))
        validate_token("external_capability.provider", cap.get("provider"))
    http = spec.get("http")
    if http is not None and not isinstance(http, dict):
        raise ValueError("http must be object or null")
    commands = ((spec.get("verification") or {}).get("commands") or [])
    if not isinstance(commands, list) or not all(isinstance(c, str) and c.strip() for c in commands):
        raise ValueError("verification.commands must be an array of non-empty strings")


def pascal(token: str) -> str:
    return "".join(part.capitalize() for part in token.split("-"))


def camel(token: str) -> str:
    p = pascal(token)
    return p[:1].lower() + p[1:]


def header(change_id: str) -> str:
    return f"// Scaffolded by effect-api-app-kit {KIT_VERSION}; change={change_id}.\n// This file is project-owned after creation.\n\n"


def generate_slice_files(spec: dict[str, Any]) -> dict[str, str]:
    change_id = spec["change"]["id"]
    host = Path(spec["host"]["path"])
    s = spec["slice"]
    module, subject, op, pressure, persistence = s["module"], s["subject"], s["operation"], s["pressure"], s["persistence"]
    base = host / "src" / "modules" / module
    S, O = pascal(subject), pascal(op)
    files: dict[str, str] = {}

    files[str(base / f"{subject}.model.ts")] = header(change_id) + f'''export type {S}Id = string & {{ readonly __brand: "{S}Id" }}\n\nexport type {S} = Readonly<{{\n  id: {S}Id\n  version: number\n}}>\n'''

    if pressure == "P0":
        files[str(base / f"{subject}.{op}.use-case.ts")] = header(change_id) + f'''import type {{ {S} }} from "./{subject}.model.js"\n\nexport type {O}{S}Input = Readonly<Record<string, unknown>>\nexport type {O}{S}Outcome = Readonly<{{ value: {S} }}>\n\nexport const {camel(op)}{S} = async (_input: {O}{S}Input): Promise<{O}{S}Outcome> => {{\n  throw new Error("Implement {subject}.{op} using the repository's current authority")\n}}\n'''
    else:
        files[str(base / f"{subject}.{op}.command.ts")] = header(change_id) + f'''export type {O}{S}Command = Readonly<{{
  commandId: string
  idempotencyKey: string
  expectedVersion?: number
  payload: Readonly<Record<string, unknown>>
}}>
'''
        files[str(base / f"{subject}.command-context.ts")] = header(change_id) + f'''export type {S}CommandContext = Readonly<{{
  actorId: string
  correlationId: string
  requestedAt: string
  deadlineAt?: string
}}>
'''
        files[str(base / f"{subject}.{op}.receipt.ts")] = header(change_id) + f'''import type {{ {S}Id }} from "./{subject}.model.js"

export type {O}{S}Receipt = Readonly<{{
  subjectId: {S}Id
  committedVersion: number
  idempotencyKey: string
}}>
'''
        files[str(base / f"{subject}.repository.port.ts")] = header(change_id) + f'''import type {{ Effect }} from "effect"
import type {{ {S}, {S}Id }} from "./{subject}.model.js"

export type {S}RepositoryError = Readonly<{{ _tag: "{S}RepositoryError"; message: string }}>

export interface {S}Repository {{
  readonly get: (id: {S}Id) => Effect.Effect<{S} | null, {S}RepositoryError>
  readonly commit: (value: {S}, expectedVersion?: number) => Effect.Effect<{S}, {S}RepositoryError>
}}
'''
        files[str(base / f"{subject}.transaction.port.ts")] = header(change_id) + f'''import type {{ Effect }} from "effect"

export interface {S}Transaction {{
  readonly run: <A, E, R>(effect: Effect.Effect<A, E, R>) => Effect.Effect<A, E, R>
}}
'''
        files[str(base / f"{subject}.idempotency.port.ts")] = header(change_id) + f'''import type {{ Effect }} from "effect"
import type {{ {O}{S}Receipt }} from "./{subject}.{op}.receipt.js"

export interface {S}Idempotency {{
  readonly lookup: (key: string) => Effect.Effect<{O}{S}Receipt | null>
  readonly record: (key: string, receipt: {O}{S}Receipt) => Effect.Effect<void>
}}
'''
        adapter_suffix = "memory.fake" if persistence == "memory" else "postgres.live"
        adapter_name = f"{S}Repository{pascal('memory' if persistence == 'memory' else 'postgres')}{'Fake' if persistence == 'memory' else 'Live'}"
        files[str(base / f"{subject}.repository.{adapter_suffix}.ts")] = header(change_id) + f'''import type {{ {S}Repository }} from "./{subject}.repository.port.js"

export const make{adapter_name} = (_dependency: unknown): {S}Repository => ({{
  get: (_id) => {{ throw new Error("Implement {adapter_suffix} get") }},
  commit: (_value, _expectedVersion) => {{ throw new Error("Implement {adapter_suffix} commit") }}
}})
'''
        files[str(base / f"{subject}.{op}.use-case.ts")] = header(change_id) + f'''import type {{ Effect }} from "effect"
import type {{ {O}{S}Command }} from "./{subject}.{op}.command.js"
import type {{ {S}CommandContext }} from "./{subject}.command-context.js"
import type {{ {O}{S}Receipt }} from "./{subject}.{op}.receipt.js"
import type {{ {S}Repository }} from "./{subject}.repository.port.js"
import type {{ {S}Transaction }} from "./{subject}.transaction.port.js"
import type {{ {S}Idempotency }} from "./{subject}.idempotency.port.js"

export type {O}{S}Error = Readonly<{{ _tag: "{O}{S}Error"; message: string }}>

export type {O}{S}Dependencies = Readonly<{{
  repository: {S}Repository
  transaction: {S}Transaction
  idempotency: {S}Idempotency
}}>

export const {camel(op)}{S} = (
  _dependencies: {O}{S}Dependencies,
  _context: {S}CommandContext,
  _command: {O}{S}Command
): Effect.Effect<{O}{S}Receipt, {O}{S}Error> => {{
  throw new Error("Implement authorization, invariants, durable idempotency, transaction, and receipt")
}}
'''

    if pressure in {"P2", "P3"}:
        cap = spec["external_capability"]
        cap_name, provider = cap["name"], cap["provider"]
        C = pascal(cap_name)
        files[str(base / f"{subject}.{cap_name}.candidate.ts")] = header(change_id) + f'''export type {S}{C}Candidate = Readonly<{{\n  candidateId: string\n  sourceRef: string\n  observedAt: string\n  payload: Readonly<Record<string, unknown>>\n}}>\n'''
        files[str(base / f"{subject}.{cap_name}.port.ts")] = header(change_id) + f'''import type {{ Effect }} from "effect"\nimport type {{ {S}{C}Candidate }} from "./{subject}.{cap_name}.candidate.js"\n\nexport type {C}Error = Readonly<{{ _tag: "{C}Error"; message: string; unknownOutcome?: boolean }}>\n\nexport interface {S}{C}Port {{\n  readonly observe: (request: Readonly<Record<string, unknown>>) => Effect.Effect<{S}{C}Candidate, {C}Error>\n}}\n'''
        files[str(base / f"{subject}.{cap_name}.{provider}.live.ts")] = header(change_id) + f'''import type {{ {S}{C}Port }} from "./{subject}.{cap_name}.port.js"\n\nexport const make{S}{C}{pascal(provider)}Live = (_client: unknown): {S}{C}Port => ({{\n  observe: (_request) => {{ throw new Error("Normalize provider output into a Candidate") }}\n}})\n'''
        files[str(base / f"{subject}.{cap_name}.materialize.use-case.ts")] = header(change_id) + f'''import type {{ Effect }} from "effect"\nimport type {{ {S}{C}Candidate }} from "./{subject}.{cap_name}.candidate.js"\n\nexport const materialize{S}{C}Candidate = (\n  _candidate: {S}{C}Candidate\n): Effect.Effect<Readonly<{{ committedVersion: number }}>, Readonly<{{ _tag: "MaterializationError"; message: string }}>> => {{\n  throw new Error("Implement governed decision/materialization through the authority transaction")\n}}\n'''
        files[str(base / f"{subject}.{cap_name}.contract.test.ts")] = header(change_id) + f'''// Connect this conformance contract to the repository's test runner.\nexport const {camel(subject)}{C}Contract = {{\n  verifies: ["normalized candidate", "error taxonomy", "deadline/cancellation", "unknown outcome"]\n}} as const\n'''

    if pressure == "P3":
        files[str(base / f"{subject}.outbox.ts")] = header(change_id) + '''export type OutboxRecord = Readonly<{ id: string; topic: string; payload: unknown; committedAt: string }>\n'''
        files[str(base / f"{subject}.inbox.ts")] = header(change_id) + '''export type InboxReceipt = Readonly<{ messageId: string; receivedAt: string; duplicate: boolean }>\n'''
        files[str(base / f"{subject}.{op}.recovery.harness.ts")] = header(change_id) + f'''export const {camel(subject)}{O}RecoveryHarnessDescriptor = {{\n  id: "{subject}.{op}.recovery",\n  surface: "headless",\n  exercises: ["restart", "replay", "duplicate", "unknown outcome"],\n  doesNotCover: ["production external provider"]\n}} as const\n'''

    http = spec.get("http") or {}
    if http.get("enabled"):
        route = http.get("route") or f"/{module}"
        files[str(base / f"{subject}.http.contract.ts")] = header(change_id) + f'''export const {S}HttpContract = {{\n  profile: "{s['effect_profile']}",\n  route: "{route}",\n  operation: "{op}",\n  note: "Map this transport-neutral contract through the target project's installed HttpApi profile"\n}} as const\n'''
        files[str(base / f"{subject}.http.handlers.ts")] = header(change_id) + f'''import {{ {camel(op)}{S} }} from "./{subject}.{op}.use-case.js"\n\nexport const make{S}HttpHandlers = (dependencies: Parameters<typeof {camel(op)}{S}>[0]) => ({{\n  {op}: (input: unknown) => {{\n    // Decode at the edge, call the use case, and map stable errors to transport responses.\n    return {{ dependencies, input }}\n  }}\n}})\n'''

    public_exports = [f'export * from "./{subject}.model.js"', f'export * from "./{subject}.{op}.use-case.js"']
    if pressure != "P0":
        public_exports += [f'export * from "./{subject}.{op}.command.js"', f'export * from "./{subject}.command-context.js"', f'export * from "./{subject}.{op}.receipt.js"']
    files[str(base / f"{subject}.public.ts")] = header(change_id) + "\n".join(public_exports) + "\n"

    wiring_lines = [f'export * from "./{subject}.public.js"']
    if pressure != "P0":
        suffix = "memory.fake" if persistence == "memory" else "postgres.live"
        wiring_lines.append(f'export * from "./{subject}.repository.{suffix}.js"')
    if pressure in {"P2", "P3"}:
        cap = spec["external_capability"]
        wiring_lines.append(f'export * from "./{subject}.{cap["name"]}.{cap["provider"]}.live.js"')
    if (spec.get("http") or {}).get("enabled"):
        wiring_lines.append(f'export * from "./{subject}.http.handlers.js"')
    files[str(base / f"{subject}.wiring.ts")] = header(change_id) + "\n".join(wiring_lines) + "\n"

    files[str(base / f"{subject}.{op}.use-case.test.ts")] = header(change_id) + f'''// Connect to the repository's test runner. Keep the test near the authority slice.\nexport const {camel(subject)}{O}UseCaseExpectations = [\n  "formal command path",\n  "typed outcome",\n  {json.dumps("idempotency and expected-version behavior" if pressure != "P0" else "bounded operation behavior")}\n] as const\n'''
    return files


def empty_manifest() -> dict[str, Any]:
    return {"schema_version": 1, "kit_version": KIT_VERSION, "slices": {}, "managed": {}, "verification_commands": []}


def load_manifest(repo: Path) -> dict[str, Any]:
    path = repo / MANIFEST_REL
    if not path.is_file():
        return empty_manifest()
    data = load_yaml(path)
    if data.get("schema_version") != 1 or not isinstance(data.get("slices"), dict):
        raise ValueError("unsupported or invalid .evo-kit/manifest.yaml")
    return data


def registry_path(spec_or_manifest_host: str) -> Path:
    return Path(spec_or_manifest_host) / "src" / "host" / "generated.modules.ts"


def build_registry(slices: dict[str, Any]) -> tuple[Path | None, str | None]:
    hosts = {entry["host_path"] for entry in slices.values()}
    if not hosts:
        return None, None
    if len(hosts) != 1:
        raise ValueError("current experimental kit supports one managed host registry per repository")
    host = next(iter(hosts))
    entries=[]
    for change_id, entry in sorted(slices.items()):
        module, subject = entry["module"], entry["subject"]
        entries.append(f'  {{ id: "{change_id}", load: () => import("../modules/{module}/{subject}.wiring.js") }}')
    text = f'''// @generated by effect-api-app-kit {KIT_VERSION}. Do not edit manually.\n\nexport const generatedModuleWiring = [\n{",\n".join(entries)}\n] as const\n'''
    return registry_path(host), text


def inspect_repo(repo: Path) -> dict[str, Any]:
    root=repo.resolve(); package=root/"package.json"; pkg={}
    if package.is_file():
        try: pkg=json.loads(package.read_text(encoding="utf-8"))
        except Exception: pkg={"parse_error":True}
    deps={**(pkg.get("dependencies") or {}), **(pkg.get("devDependencies") or {})}
    effect=deps.get("effect") or deps.get("effect-v3") or deps.get("effect-v4")
    return {
        "repo":str(root),
        "manifest":str(MANIFEST_REL) if (root/MANIFEST_REL).is_file() else None,
        "package_manager":[n for n in ("pnpm-lock.yaml","package-lock.json","yarn.lock","bun.lock","bun.lockb") if (root/n).exists()],
        "effect_dependency":effect,
        "apps":sorted(p.name for p in (root/"apps").iterdir() if p.is_dir()) if (root/"apps").is_dir() else [],
        "claim_ceiling":"repository/profile discovery only",
    }


def plan(repo: Path, spec: dict[str, Any]) -> dict[str, Any]:
    validate_spec(spec)
    manifest=load_manifest(repo)
    change_id=spec["change"]["id"]
    if change_id in manifest["slices"]:
        raise ValueError(f"change id already exists in manifest: {change_id}")
    files=generate_slice_files(spec)
    conflicts=[rel for rel in files if (repo/rel).exists()]
    if conflicts:
        raise FileExistsError("source files already exist: " + ", ".join(conflicts[:12]))
    previous_registry=(manifest.get("managed") or {}).get("registry")
    if previous_registry:
        rp=repo/previous_registry["path"]
        if not rp.is_file() or sha256_file(rp)!=previous_registry.get("sha256"):
            raise ValueError("managed registry drift detected; run verify/repair before apply")
    slice_entry={
        "host_path":spec["host"]["path"],"host_name":spec["host"]["name"],
        "module":spec["slice"]["module"],"subject":spec["slice"]["subject"],"operation":spec["slice"]["operation"],
        "pressure":spec["slice"]["pressure"],"persistence":spec["slice"]["persistence"],"effect_profile":spec["slice"]["effect_profile"],
        "files":sorted(files),"created_by":change_id,
    }
    next_manifest=json.loads(json.dumps(manifest))
    next_manifest["kit_version"]=KIT_VERSION
    next_manifest["slices"][change_id]=slice_entry
    commands=((spec.get("verification") or {}).get("commands") or [])
    next_manifest["verification_commands"]=list(dict.fromkeys([*(next_manifest.get("verification_commands") or []), *commands]))
    reg_path, reg_text=build_registry(next_manifest["slices"])
    assert reg_path and reg_text
    next_manifest["managed"]["registry"]={"path":reg_path.as_posix(),"sha256":sha256_text(reg_text)}
    patch=dict(files)
    patch[reg_path.as_posix()]=reg_text
    patch[MANIFEST_REL.as_posix()]=dump_yaml(next_manifest)
    return {
        "change_id":change_id,
        "pressure":spec["slice"]["pressure"],
        "patch":patch,
        "source_files":sorted(files),
        "managed_files":[reg_path.as_posix(),MANIFEST_REL.as_posix()],
        "verification_commands":commands,
        "claim_ceiling":"planned file set and preflight conflicts; no source written, no compile/HTTP behavior claimed",
    }


def validate_staged(patch: dict[str, str]) -> None:
    for rel, content in patch.items():
        p=Path(rel)
        if p.is_absolute() or ".." in p.parts:
            raise ValueError(f"unsafe target path: {rel}")
        if not content.strip():
            raise ValueError(f"empty staged file: {rel}")
        if p.suffix in {".ts", ".tsx"} and p.name.count(".") > 8:
            raise ValueError(f"unexpectedly long semantic filename: {rel}")
    manifest=yaml.safe_load(patch[MANIFEST_REL.as_posix()])
    if manifest.get("schema_version")!=1:
        raise ValueError("staged manifest invalid")


def acquire_lock(repo: Path) -> int:
    path=repo/LOCK_REL; path.parent.mkdir(parents=True, exist_ok=True)
    try:
        return os.open(path, os.O_CREAT|os.O_EXCL|os.O_WRONLY, 0o600)
    except FileExistsError:
        raise RuntimeError(f"kit lock exists: {path}")


def release_lock(repo: Path, fd: int) -> None:
    try: os.close(fd)
    finally:
        try: (repo/LOCK_REL).unlink()
        except FileNotFoundError: pass


def apply_plan(repo: Path, p: dict[str, Any]) -> dict[str, Any]:
    repo=repo.resolve(); patch=p["patch"]; validate_staged(patch)
    txid=f"{int(time.time())}-{uuid.uuid4().hex[:8]}"
    evo=repo/".evo-kit"; stage=evo/"staging"/txid; tx=evo/"transactions"/txid; backups=tx/"backups"
    stage.mkdir(parents=True, exist_ok=False); backups.mkdir(parents=True, exist_ok=False)
    for rel, content in patch.items():
        sp=stage/rel; sp.parent.mkdir(parents=True, exist_ok=True); sp.write_text(content, encoding="utf-8")
    validate_staged({rel:(stage/rel).read_text(encoding="utf-8") for rel in patch})
    fd=acquire_lock(repo)
    journal={"txid":txid,"change_id":p["change_id"],"status":"committing","targets":sorted(patch),"new_files":[],"backups":[]}
    (tx/"journal.json").write_text(json.dumps(journal,indent=2)+"\n",encoding="utf-8")
    committed=[]
    try:
        # Re-check create-only source conflicts under lock.
        for rel in p["source_files"]:
            if (repo/rel).exists(): raise FileExistsError(f"source appeared during apply: {rel}")
        for rel in sorted(patch):
            dest=repo/rel; dest.parent.mkdir(parents=True, exist_ok=True)
            if dest.exists():
                bp=backups/rel; bp.parent.mkdir(parents=True, exist_ok=True); shutil.copy2(dest,bp); journal["backups"].append(rel)
            else:
                journal["new_files"].append(rel)
            tmp=dest.parent/(dest.name+f".evo-tmp-{txid}")
            shutil.copy2(stage/rel,tmp)
            os.replace(tmp,dest)
            committed.append(rel)
        journal["status"]="applied"; journal["completed_at"]=time.time()
        (tx/"journal.json").write_text(json.dumps(journal,indent=2)+"\n",encoding="utf-8")
    except Exception as exc:
        for rel in reversed(committed):
            dest=repo/rel; bp=backups/rel
            if bp.exists():
                dest.parent.mkdir(parents=True, exist_ok=True); shutil.copy2(bp,dest)
            else:
                try: dest.unlink()
                except FileNotFoundError: pass
        journal["status"]="rolled-back"; journal["error"]=repr(exc); journal["completed_at"]=time.time()
        (tx/"journal.json").write_text(json.dumps(journal,indent=2)+"\n",encoding="utf-8")
        raise
    finally:
        release_lock(repo,fd)
        shutil.rmtree(stage,ignore_errors=True)
    return {"status":"applied","transaction":txid,"change_id":p["change_id"],"files":sorted(patch),"claim_ceiling":"files atomically applied; compile/test/HTTP only if separately executed"}


def verify(repo: Path, run_commands: bool) -> dict[str, Any]:
    repo=repo.resolve(); findings=[]; results=[]
    manifest=load_manifest(repo)
    for cid, entry in manifest.get("slices",{}).items():
        for rel in entry.get("files",[]):
            if not (repo/rel).is_file(): findings.append({"severity":"error","rule":"missing-source","slice":cid,"path":rel})
    reg=(manifest.get("managed") or {}).get("registry")
    if reg:
        p=repo/reg["path"]
        if not p.is_file(): findings.append({"severity":"error","rule":"missing-registry","path":reg["path"]})
        elif sha256_file(p)!=reg.get("sha256"): findings.append({"severity":"error","rule":"registry-drift","path":reg["path"]})
        else:
            expected_path, expected_text=build_registry(manifest["slices"])
            if expected_path.as_posix()!=reg["path"] or p.read_text(encoding="utf-8")!=expected_text:
                findings.append({"severity":"error","rule":"registry-manifest-mismatch","path":reg["path"]})
    txroot=repo/".evo-kit"/"transactions"
    if txroot.is_dir():
        for journal in txroot.glob("*/journal.json"):
            try: data=json.loads(journal.read_text())
            except Exception: findings.append({"severity":"error","rule":"invalid-journal","path":str(journal.relative_to(repo))}); continue
            if data.get("status")=="committing": findings.append({"severity":"error","rule":"incomplete-transaction","path":str(journal.relative_to(repo))})
    if run_commands and not findings:
        for command in manifest.get("verification_commands",[]) or []:
            proc=subprocess.run(command,shell=True,cwd=repo,text=True,capture_output=True)
            results.append({"command":command,"exit_code":proc.returncode,"stdout":proc.stdout[-4000:],"stderr":proc.stderr[-4000:]})
            if proc.returncode!=0: findings.append({"severity":"error","rule":"verification-command-failed","command":command,"exit_code":proc.returncode})
    summary={"error":sum(x["severity"]=="error" for x in findings),"warn":sum(x["severity"]=="warn" for x in findings),"total":len(findings)}
    return {"summary":summary,"findings":findings,"commands":results,"claim_ceiling":"structural integrity" + (" plus recorded project commands" if run_commands else "; project commands not run")}


def repair(repo: Path) -> dict[str, Any]:
    repo=repo.resolve(); manifest=load_manifest(repo)
    missing=[]
    for cid, entry in manifest.get("slices",{}).items():
        for rel in entry.get("files",[]):
            if not (repo/rel).is_file(): missing.append({"slice":cid,"path":rel})
    if missing:
        return {"status":"blocked","reason":"project-owned source files are missing; repair will not recreate them silently","missing":missing}
    reg_path, reg_text=build_registry(manifest.get("slices",{}))
    if reg_path is None: return {"status":"noop","reason":"no registered slices"}
    manifest["managed"]["registry"]={"path":reg_path.as_posix(),"sha256":sha256_text(reg_text)}
    patch={reg_path.as_posix():reg_text, MANIFEST_REL.as_posix():dump_yaml(manifest)}
    pseudo={"change_id":"repair-managed-state","patch":patch,"source_files":[],"managed_files":list(patch)}
    return apply_plan(repo,pseudo)


def main() -> None:
    ap=argparse.ArgumentParser(description="Effect API App Kit")
    sub=ap.add_subparsers(dest="cmd",required=True)
    p=sub.add_parser("inspect"); p.add_argument("--repo",default=".")
    for name in ("plan","apply"):
        p=sub.add_parser(name); p.add_argument("--repo",default="."); p.add_argument("--change",required=True)
    p=sub.add_parser("verify"); p.add_argument("--repo",default="."); p.add_argument("--run",action="store_true")
    p=sub.add_parser("repair"); p.add_argument("--repo",default=".")
    args=ap.parse_args(); repo=Path(args.repo)
    try:
        if args.cmd=="inspect": result=inspect_repo(repo)
        elif args.cmd=="plan":
            p=plan(repo,load_yaml(Path(args.change))); result={k:v for k,v in p.items() if k!="patch"}; result["patch_preview"]=[{"path":rel,"sha256":sha256_text(content),"bytes":len(content.encode())} for rel,content in sorted(p["patch"].items())]
        elif args.cmd=="apply": result=apply_plan(repo,plan(repo,load_yaml(Path(args.change))))
        elif args.cmd=="verify":
            result=verify(repo,args.run); print(json.dumps(result,ensure_ascii=False,indent=2));
            if result["summary"]["error"]: raise SystemExit(1)
            return
        elif args.cmd=="repair": result=repair(repo)
        print(json.dumps(result,ensure_ascii=False,indent=2))
    except (ValueError,FileExistsError,RuntimeError) as exc:
        print(json.dumps({"status":"error","error":str(exc)},ensure_ascii=False,indent=2),file=sys.stderr)
        raise SystemExit(2)

if __name__=="__main__": main()
