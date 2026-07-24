#!/usr/bin/env python3
"""Deterministic source audit for the grouped AI Coding OS Skill Suite.

The audit is intentionally offline. It validates frontmatter, portable Suite
contracts, links, schemas-as-data, source conventions, Preset golden output,
Docs Governance compatibility, and the experimental Effect API kit's atomic
behavior.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import py_compile
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

try:
    import yaml
    import jsonschema
except ImportError as exc:  # pragma: no cover
    raise SystemExit("PyYAML and jsonschema are required") from exc

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)
MD_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
MANAGED_BEGIN = "<!-- evolvable-application-preset:begin -->"
MANAGED_END = "<!-- evolvable-application-preset:end -->"


class Audit:
    def __init__(self, root: Path) -> None:
        self.root = root.resolve()
        self.findings: list[dict[str, Any]] = []
        self.checks: list[dict[str, Any]] = []

    def add(self, severity: str, rule: str, message: str, path: str | None = None, evidence: Any = None) -> None:
        item: dict[str, Any] = {"severity": severity, "rule": rule, "message": message}
        if path is not None:
            item["path"] = path
        if evidence is not None:
            item["evidence"] = evidence
        self.findings.append(item)

    def check(self, name: str, status: str, detail: Any = None) -> None:
        item: dict[str, Any] = {"name": name, "status": status}
        if detail is not None:
            item["detail"] = detail
        self.checks.append(item)

    def rel(self, path: Path) -> str:
        try:
            return path.resolve().relative_to(self.root).as_posix()
        except ValueError:
            return str(path)

    def run(self, cmd: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
        env = os.environ.copy()
        env["PYTHONDONTWRITEBYTECODE"] = "1"
        return subprocess.run(cmd, cwd=cwd or self.root, text=True, capture_output=True, env=env)

    def parse_skill_frontmatter(self) -> dict[str, dict[str, Any]]:
        skills: dict[str, dict[str, Any]] = {}
        for path in sorted(self.root.rglob("SKILL.md")):
            text = path.read_text(encoding="utf-8")
            match = FRONTMATTER_RE.match(text)
            if not match:
                self.add("error", "skill-frontmatter", "SKILL.md is missing YAML frontmatter", self.rel(path))
                continue
            try:
                data = yaml.safe_load(match.group(1)) or {}
            except Exception as exc:
                self.add("error", "skill-frontmatter", f"invalid YAML frontmatter: {exc}", self.rel(path))
                continue
            name = data.get("name")
            if not isinstance(name, str) or not name:
                self.add("error", "skill-name", "Skill name is missing", self.rel(path))
                continue
            if name in skills:
                self.add("error", "skill-name-duplicate", f"duplicate Skill name {name}", self.rel(path), [skills[name]["path"]])
                continue
            description = data.get("description")
            if not isinstance(description, str) or not description.strip():
                self.add("error", "skill-description", "Skill description is missing", self.rel(path))
            extra = sorted(set(data) - {"name", "description", "disable-model-invocation"})
            if extra:
                self.add("error", "skill-frontmatter-extra", "Skill frontmatter contains nonessential fields", self.rel(path), extra)
            invocation = "user" if data.get("disable-model-invocation") is True else "model"
            skills[name] = {
                "path": self.rel(path.parent),
                "file": self.rel(path),
                "frontmatter": data,
                "invocation": invocation,
            }
        self.check("skill-frontmatter", "pass" if not any(f["rule"].startswith("skill-") and f["severity"] == "error" for f in self.findings) else "fail", {"count": len(skills)})
        return skills

    def check_contract_owners(self, skills: dict[str, dict[str, Any]]) -> None:
        root = self.root / "contracts/ai-coding-os-suite-contracts/references"
        vocabulary = yaml.safe_load((root / "semantic-vocabulary.yaml").read_text(encoding="utf-8")) or {}
        patterns = yaml.safe_load((root / "filename-patterns.yaml").read_text(encoding="utf-8")) or {}
        guarded = yaml.safe_load((root / "guarded-terms.yaml").read_text(encoding="utf-8")) or {}
        known = set(skills)
        owners: set[str] = set()
        for term, spec in (vocabulary.get("terms") or {}).items():
            owner = (spec or {}).get("owner")
            if isinstance(owner, str):
                owners.add(owner)
            if "status" in (spec or {}) or "filename_patterns" in (spec or {}):
                self.add("error", "contract-redundant-field", f"semantic term carries a redundant field: {term}", self.rel(root / "semantic-vocabulary.yaml"))
        for item in patterns.get("patterns") or []:
            owner = (item or {}).get("owner")
            if isinstance(owner, str):
                owners.add(owner)
        for term, spec in (guarded.get("terms") or {}).items():
            if "status" in (spec or {}):
                self.add("error", "contract-redundant-field", f"guarded-term membership already implies status: {term}", self.rel(root / "guarded-terms.yaml"))
        for owner in sorted(owners - known):
            self.add("error", "contract-owner-unknown", f"contract owner does not resolve to an installed Suite Skill: {owner}", self.rel(root))
        stale_rosters = sorted(root.glob("*manifest*"))
        for path in stale_rosters:
            self.add("error", "contract-static-roster", "installable contracts must not ship a static Suite roster", self.rel(path))
        failed_rules = {"contract-redundant-field", "contract-owner-unknown", "contract-static-roster"}
        self.check(
            "suite-contracts",
            "fail" if any(f["rule"] in failed_rules for f in self.findings) else "pass",
            {"owners": sorted(owners), "skills": len(skills)},
        )

    def check_data_files(self) -> None:
        parsed = 0
        for path in sorted(self.root.rglob("*")):
            if not path.is_file() or any(part in {"node_modules", ".git"} for part in path.parts):
                continue
            try:
                if path.suffix == ".json":
                    json.loads(path.read_text(encoding="utf-8"))
                    parsed += 1
                elif path.suffix in {".yaml", ".yml"}:
                    yaml.safe_load(path.read_text(encoding="utf-8"))
                    parsed += 1
            except Exception as exc:
                self.add("error", "data-parse", f"cannot parse {path.suffix}: {exc}", self.rel(path))
        self.check("json-yaml-parse", "pass" if not any(f["rule"] == "data-parse" for f in self.findings) else "fail", {"files": parsed})

    def check_schema_instances(self) -> None:
        cases = [
            ("contracts/ai-coding-os-suite-contracts/references/semantic-vocabulary.schema.json", "contracts/ai-coding-os-suite-contracts/references/semantic-vocabulary.yaml"),
            ("contracts/ai-coding-os-suite-contracts/references/harness/harness-descriptor.schema.json", "contracts/ai-coding-os-suite-contracts/references/harness/examples/order-checkout-retry.descriptor.yaml"),
            ("contracts/ai-coding-os-suite-contracts/references/harness/harness-result.schema.json", "contracts/ai-coding-os-suite-contracts/references/harness/examples/order-checkout-retry.result.yaml"),
            ("preset/evolvable-application-preset/schemas/preset-input.schema.json", "preset/evolvable-application-preset/examples/commerce-platform/preset-input.yaml"),
            ("preset/evolvable-application-preset/schemas/project-overlay.schema.json", "preset/evolvable-application-preset/examples/commerce-platform/project-overlay.yaml"),
            ("preset/evolvable-application-preset/schemas/architecture-profile.schema.json", "preset/evolvable-application-preset/examples/commerce-platform/expected/docs/standards/architecture-profile.yaml"),
            ("preset/evolvable-application-preset/schemas/naming-vocabulary.schema.json", "preset/evolvable-application-preset/examples/commerce-platform/expected/docs/standards/naming-vocabulary.yaml"),
            ("tooling/effect-api-app-kit/schemas/change-spec.schema.json", "tooling/effect-api-app-kit/examples/add-order-create.yaml"),
        ]
        for schema_rel, instance_rel in cases:
            try:
                schema = json.loads((self.root / schema_rel).read_text(encoding="utf-8"))
                instance_path = self.root / instance_rel
                if instance_path.suffix == ".json":
                    instance = json.loads(instance_path.read_text(encoding="utf-8"))
                else:
                    instance = yaml.safe_load(instance_path.read_text(encoding="utf-8"))
                jsonschema.Draft202012Validator.check_schema(schema)
                jsonschema.validate(instance=instance, schema=schema)
            except Exception as exc:
                self.add("error", "schema-validation", f"schema instance validation failed: {exc}", instance_rel, {"schema": schema_rel})
        self.check("schema-validation", "pass" if not any(f["rule"] == "schema-validation" for f in self.findings) else "fail", {"cases": len(cases)})

    def check_markdown_links(self) -> None:
        checked = 0
        for path in sorted(self.root.rglob("*.md")):
            text = path.read_text(encoding="utf-8", errors="replace")
            for raw in MD_LINK_RE.findall(text):
                target = raw.strip().split(" ", 1)[0].strip("<>")
                if not target or target.startswith(("#", "http://", "https://", "mailto:", "sandbox:", "data:")):
                    continue
                target = target.split("#", 1)[0].split("?", 1)[0]
                if not target or any(token in target for token in ("<", ">", "${", "{{")):
                    continue
                if target.startswith("/"):
                    # Project-root examples in doctrine are not Suite file links.
                    continue
                checked += 1
                candidate = (path.parent / target).resolve()
                if not candidate.exists():
                    self.add("error", "markdown-link", f"broken relative Markdown link: {raw}", self.rel(path), self.rel(candidate))
        self.check("markdown-links", "pass" if not any(f["rule"] == "markdown-link" for f in self.findings) else "fail", {"links": checked})

    def check_skill_portability(self, skills: dict[str, dict[str, Any]]) -> None:
        checked = 0
        for name, skill in skills.items():
            skill_root = (self.root / skill["path"]).resolve()
            for path in sorted(skill_root.rglob("*.md")):
                text = path.read_text(encoding="utf-8", errors="replace")
                for raw in MD_LINK_RE.findall(text):
                    target = raw.strip().split(" ", 1)[0].strip("<>")
                    if not target or target.startswith(("#", "http://", "https://", "mailto:", "sandbox:", "data:", "/")):
                        continue
                    target = target.split("#", 1)[0].split("?", 1)[0]
                    if not target or any(token in target for token in ("<", ">", "${", "{{")):
                        continue
                    checked += 1
                    candidate = (path.parent / target).resolve()
                    try:
                        candidate.relative_to(skill_root)
                    except ValueError:
                        self.add(
                            "error",
                            "cross-skill-relative-link",
                            f"Skill {name} links outside its installable directory; use `$skill-name` for cross-Skill relationships",
                            self.rel(path),
                            self.rel(candidate),
                        )
        self.check(
            "skill-portability",
            "pass" if not any(f["rule"] == "cross-skill-relative-link" for f in self.findings) else "fail",
            {"relative_links": checked, "skills": len(skills)},
        )

    def check_contract_snapshot(self) -> None:
        contract = self.root / "contracts/ai-coding-os-suite-contracts/references"
        snapshot = self.root / "preset/evolvable-application-preset/references/suite-contract-snapshot"
        files = ["semantic-vocabulary.yaml", "filename-patterns.yaml", "guarded-terms.yaml"]
        for name in files:
            source = contract / name
            local = snapshot / name
            if not source.is_file() or not local.is_file() or source.read_bytes() != local.read_bytes():
                self.add(
                    "error",
                    "suite-contract-snapshot",
                    "Preset-local Suite contract snapshot differs from the canonical contract Skill",
                    self.rel(local),
                    {"source": self.rel(source)},
                )
        self.check(
            "suite-contract-snapshot",
            "pass" if not any(f["rule"] == "suite-contract-snapshot" for f in self.findings) else "fail",
            {"files": files},
        )

    def check_source_conventions(self, skills: dict[str, dict[str, Any]]) -> None:
        level_re = re.compile(
            r"high[- ]?(?:capability|intelligence|smart)|highly capable|high-capacity|"
            r"capable agent|weak (?:agent|model)|strong (?:agent|model)|"
            r"agent intelligence|model intelligence|高智能|高能力|弱模型|强模型|"
            r"智能等级|能力等级",
            re.I,
        )
        for path in sorted(self.root.rglob("*")):
            if not path.is_file() or any(part in {"node_modules", ".git"} for part in path.parts):
                continue
            if path.resolve() == Path(__file__).resolve():
                continue
            if path.suffix not in {".md", ".json", ".yaml", ".yml", ".toml", ".py"}:
                continue
            text = path.read_text(encoding="utf-8", errors="replace")
            match = level_re.search(text)
            if match:
                self.add("error", "agent-level-narrative", "explicit agent/model intelligence-level narrative remains", self.rel(path), match.group(0))
        for path in sorted(self.root.rglob("SKILL.md")):
            text = path.read_text(encoding="utf-8")
            own = next((name for name, item in skills.items() if item["file"] == self.rel(path)), None)
            body = text.split("---", 2)[2]
            for name in skills:
                if name == own:
                    continue
                if re.search(rf"`{re.escape(name)}`", body):
                    self.add("error", "skill-reference-syntax", f"cross-Skill reference must use `${name}`", self.rel(path))
            for referenced in sorted(set(re.findall(r"\$([a-z][a-z0-9-]+)", body)) - {"skill-name"}):
                if referenced not in skills:
                    self.add("error", "skill-reference-unknown", f"cross-Skill reference does not resolve: ${referenced}", self.rel(path))
        flat_dirs = [p for p in self.root.rglob("*") if p.is_dir() and p.name.lower() in {"flat", "flattened"}]
        for path in flat_dirs:
            self.add("error", "flat-source", "Flat Skill source is not part of this repository", self.rel(path))
        failed = any(
            f["rule"] in {"agent-level-narrative", "skill-reference-syntax", "skill-reference-unknown", "flat-source"}
            and f["severity"] == "error"
            for f in self.findings
        )
        self.check("source-conventions", "fail" if failed else "pass", {"skills": len(skills)})

    def check_python(self) -> None:
        py_files = [p for p in sorted(self.root.rglob("*.py")) if "__pycache__" not in p.parts]
        with tempfile.TemporaryDirectory(prefix="suite-pyc-") as td:
            for index, path in enumerate(py_files):
                try:
                    py_compile.compile(str(path), cfile=str(Path(td) / f"{index}.pyc"), doraise=True)
                except Exception as exc:
                    self.add("error", "python-compile", f"Python compile failed: {exc}", self.rel(path))
        cache_paths = [p for p in self.root.rglob("*") if p.name == "__pycache__" or p.suffix in {".pyc", ".pyo"}]
        for path in cache_paths:
            self.add("error", "generated-cache", "generated Python cache must not be released", self.rel(path))
        self.check("python-compile", "pass" if not any(f["rule"] in {"python-compile", "generated-cache"} for f in self.findings) else "fail", {"files": len(py_files)})

    @staticmethod
    def tree_hash(root: Path) -> str:
        h = hashlib.sha256()
        for path in sorted(p for p in root.rglob("*") if p.is_file()):
            h.update(path.relative_to(root).as_posix().encode())
            h.update(b"\0")
            h.update(path.read_bytes())
            h.update(b"\0")
        return h.hexdigest()

    @staticmethod
    def compare_trees(a: Path, b: Path) -> list[str]:
        paths = {p.relative_to(a).as_posix() for p in a.rglob("*") if p.is_file()} | {p.relative_to(b).as_posix() for p in b.rglob("*") if p.is_file()}
        diffs: list[str] = []
        for rel in sorted(paths):
            pa, pb = a / rel, b / rel
            if not pa.is_file() or not pb.is_file() or pa.read_bytes() != pb.read_bytes():
                diffs.append(rel)
        return diffs

    def check_preset(self) -> None:
        base = self.root / "preset/evolvable-application-preset"
        script = base / "scripts/preset.py"
        example = base / "examples/commerce-platform"
        expected = example / "expected"
        with tempfile.TemporaryDirectory(prefix="preset-golden-") as td:
            out = Path(td) / "rendered"
            proc = self.run([sys.executable, str(script), "render", "--input", str(example / "preset-input.yaml"), "--overlay", str(example / "project-overlay.yaml"), "--out", str(out)])
            if proc.returncode != 0:
                self.add("error", "preset-render", "Preset golden render failed", self.rel(script), {"stdout": proc.stdout[-2000:], "stderr": proc.stderr[-2000:]})
            else:
                diffs = self.compare_trees(expected, out)
                if diffs:
                    self.add("error", "preset-golden", "rendered Preset differs from golden fixture", self.rel(expected), diffs[:30])
                validate = self.run([sys.executable, str(script), "validate", "--repo", str(out)])
                if validate.returncode != 0:
                    self.add("error", "preset-validate", "rendered Preset failed validation", self.rel(script), {"stdout": validate.stdout[-2000:], "stderr": validate.stderr[-2000:]})
                docs = self.run([sys.executable, str(self.root / "governance/docs-governance/scripts/run_docs_audit.py"), "--repo", str(out)])
                try:
                    docs_data = json.loads(docs.stdout)
                    summary = docs_data.get("summary") or {}
                except Exception:
                    summary = {"parse_error": True}
                if docs.returncode != 0 or summary.get("blocker") or summary.get("warn"):
                    self.add("error", "preset-docs-audit", "Preset example is not clean under Docs Governance", self.rel(expected), {"returncode": docs.returncode, "summary": summary, "stderr": docs.stderr[-1000:]})
                arch = self.run([sys.executable, str(out / "tooling/architecture_check.py"), "--repo", str(out)])
                if arch.returncode != 0:
                    self.add("error", "preset-architecture-check", "Preset architecture checker failed on golden output", self.rel(expected), {"stdout": arch.stdout[-2000:], "stderr": arch.stderr[-2000:]})
                bad_root = Path(td) / "build" / "project"
                bad_file = bad_root / "apps/api/src/modules/orders/order.create.use-case.ts"
                bad_file.parent.mkdir(parents=True)
                bad_file.write_text('import value from "./order.live.ts";\nvoid value;\n', encoding="utf-8")
                bad_arch = self.run([sys.executable, str(out / "tooling/architecture_check.py"), "--repo", str(bad_root)])
                try:
                    bad_data = json.loads(bad_arch.stdout)
                except json.JSONDecodeError:
                    bad_data = {}
                bad_rules = {item.get("rule") for item in bad_data.get("findings", []) if isinstance(item, dict)}
                if bad_arch.returncode == 0 or "use-case-imports-live" not in bad_rules:
                    self.add("error", "preset-architecture-check-scan", "generated checker did not detect a violation under a parent directory named build", self.rel(out / "tooling/architecture_check.py"), {"returncode": bad_arch.returncode, "rules": sorted(rule for rule in bad_rules if rule)})
                english_overlay = yaml.safe_load((example / "project-overlay.yaml").read_text(encoding="utf-8"))
                english_overlay["project"]["narrative_language"] = "en-US"
                english_overlay_path = Path(td) / "english-overlay.yaml"
                english_overlay_path.write_text(yaml.safe_dump(english_overlay, sort_keys=False), encoding="utf-8")
                english_out = Path(td) / "english-rendered"
                english = self.run([sys.executable, str(script), "render", "--input", str(example / "preset-input.yaml"), "--overlay", str(english_overlay_path), "--out", str(english_out)])
                english_source = (english_out / "docs/standards/source-topology-and-naming.md").read_text(encoding="utf-8") if english.returncode == 0 else ""
                english_ssot = (english_out / "docs/ssot/README.md").read_text(encoding="utf-8") if english.returncode == 0 else ""
                if english.returncode != 0 or "## Canonical Patterns" not in english_source or "order.create.use-case.ts" not in english_source or "## Authority Resolution" not in english_ssot or "Date: 2026-07-23" not in (english_out / "docs/adr/0001-adopt-evolvable-application-preset.md").read_text(encoding="utf-8"):
                    self.add("error", "preset-bilingual-parity", "English Preset render is missing semantic sections present in the canonical render", self.rel(script), {"returncode": english.returncode, "stderr": english.stderr[-1000:]})
        with tempfile.TemporaryDirectory(prefix="preset-merge-") as td:
            repo = Path(td) / "existing"
            repo.mkdir(parents=True)
            local_agents = "# Existing Agent Entry\n\n## Local Rules\n\n- Preserve this project-owned instruction.\n"
            (repo / "AGENTS.md").write_text(local_agents, encoding="utf-8")
            first = self.run([sys.executable, str(script), "render", "--input", str(example / "preset-input.yaml"), "--overlay", str(example / "project-overlay.yaml"), "--out", str(repo)])
            if first.returncode != 0:
                self.add("error", "preset-merge", "Preset failed to merge into an existing AGENTS.md", self.rel(script), first.stderr[-2000:])
            else:
                merged = (repo / "AGENTS.md").read_text(encoding="utf-8")
                if "Preserve this project-owned instruction" not in merged or merged.count(MANAGED_BEGIN) != 1 or merged.count(MANAGED_END) != 1:
                    self.add("error", "preset-merge", "existing AGENTS.md content/managed markers were not preserved correctly", self.rel(script))
                inspect = self.run([sys.executable, str(script), "inspect", "--repo", str(repo)])
                try:
                    inspected = json.loads(inspect.stdout)
                except Exception:
                    inspected = {}
                adopted = inspected.get("adopted_preset") or {}
                if inspect.returncode != 0 or not inspected.get("managed_agents_section") or "docs/standards/architecture-profile.yaml" not in (inspected.get("existing_surfaces") or []) or not adopted.get("profiles"):
                    self.add("error", "preset-inspect", "Preset inspect did not expose adoption facts for Agent discovery", self.rel(script), {"returncode": inspect.returncode, "output": inspected, "stderr": inspect.stderr[-1000:]})
                second = self.run([sys.executable, str(script), "render", "--input", str(example / "preset-input.yaml"), "--overlay", str(example / "project-overlay.yaml"), "--out", str(repo), "--force"])
                merged2 = (repo / "AGENTS.md").read_text(encoding="utf-8")
                if second.returncode != 0 or merged2.count(MANAGED_BEGIN) != 1 or "Preserve this project-owned instruction" not in merged2:
                    self.add("error", "preset-merge", "Preset managed-section update was not idempotent", self.rel(script), second.stderr[-1000:])
                sentinel = repo / "package.json"
                sentinel.write_text('{"name":"project-owned-sentinel","private":true}\n', encoding="utf-8")
                authoritative_before = hashlib.sha256(((repo / "AGENTS.md").read_bytes()) + ((repo / "docs/standards/architecture-profile.yaml").read_bytes()) + sentinel.read_bytes()).hexdigest()
                upgrade = self.run([sys.executable, str(script), "upgrade", "--repo", str(repo), "--input", str(example / "preset-input.yaml"), "--overlay", str(example / "project-overlay.yaml")])
                authoritative_after = hashlib.sha256(((repo / "AGENTS.md").read_bytes()) + ((repo / "docs/standards/architecture-profile.yaml").read_bytes()) + sentinel.read_bytes()).hexdigest()
                patches = list((repo / ".evolvable-preset/upgrade-candidate").glob("*/PRESET-DIFF.patch"))
                patch_text = patches[-1].read_text(encoding="utf-8") if patches else ""
                if upgrade.returncode != 0 or authoritative_before != authoritative_after or not patches or "project/package.json" in patch_text:
                    self.add("error", "preset-upgrade", "Preset upgrade did not stage a scoped non-destructive candidate", self.rel(script), {"returncode": upgrade.returncode, "authoritative_changed": authoritative_before != authoritative_after, "unrelated_file_in_diff": "project/package.json" in patch_text, "stderr": upgrade.stderr[-1000:]})
        with tempfile.TemporaryDirectory(prefix="preset-negative-") as td:
            base_path = Path(td)
            conflict_input = {"schema_version": 1, "profiles": ["effect-httpapi-v3", "effect-httpapi-v4"]}
            conflict_path = base_path / "conflict-input.yaml"
            conflict_path.write_text(yaml.safe_dump(conflict_input, sort_keys=False), encoding="utf-8")
            conflict = self.run([sys.executable, str(script), "render", "--input", str(conflict_path), "--overlay", str(example / "project-overlay.yaml"), "--out", str(base_path / "conflict-out")])
            if conflict.returncode == 0 or "conflicting profiles" not in conflict.stderr:
                self.add("error", "preset-profile-conflict", "Preset accepted mutually conflicting profile versions", self.rel(script), {"returncode": conflict.returncode, "stderr": conflict.stderr[-1000:]})
            minimal_input = {"schema_version": 1, "profiles": ["effect-httpapi-v4"]}
            minimal_path = base_path / "minimal-input.yaml"
            minimal_path.write_text(yaml.safe_dump(minimal_input, sort_keys=False), encoding="utf-8")
            minimal_out = base_path / "minimal-out"
            minimal = self.run([sys.executable, str(script), "render", "--input", str(minimal_path), "--overlay", str(example / "project-overlay.yaml"), "--out", str(minimal_out)])
            try:
                minimal_profile = yaml.safe_load((minimal_out / "docs/standards/architecture-profile.yaml").read_text(encoding="utf-8")) if minimal.returncode == 0 else {}
            except (OSError, yaml.YAMLError):
                minimal_profile = {}
            if minimal.returncode != 0 or "effect" not in (minimal_profile.get("profiles") or []) or "typescript-node" not in (minimal_profile.get("profiles") or []):
                self.add("error", "preset-profile-closure", "Preset did not resolve required profile dependencies", self.rel(script), {"returncode": minimal.returncode, "profiles": minimal_profile.get("profiles")})
            bad_overlay = yaml.safe_load((example / "project-overlay.yaml").read_text(encoding="utf-8"))
            bad_overlay["authorities"] = ["not-an-object"]
            bad_overlay_path = base_path / "invalid-overlay.yaml"
            bad_overlay_path.write_text(yaml.safe_dump(bad_overlay, sort_keys=False), encoding="utf-8")
            invalid = self.run([sys.executable, str(script), "render", "--input", str(example / "preset-input.yaml"), "--overlay", str(bad_overlay_path), "--out", str(base_path / "invalid-out")])
            if invalid.returncode == 0 or "Traceback" in invalid.stderr or "authorities[0]" not in invalid.stderr:
                self.add("error", "preset-overlay-validation", "invalid overlay did not produce a structured validation error", self.rel(script), {"returncode": invalid.returncode, "stderr": invalid.stderr[-1000:]})
            partial = base_path / "partial"
            (partial / "docs/standards").mkdir(parents=True)
            (partial / "docs/standards/naming-vocabulary.yaml").write_text("schema_version: 1\n", encoding="utf-8")
            partial_validation = self.run([sys.executable, str(script), "validate", "--repo", str(partial)])
            try:
                partial_data = json.loads(partial_validation.stdout)
            except json.JSONDecodeError:
                partial_data = {}
            if partial_validation.returncode != 0 or partial_data.get("scope") != "partial":
                self.add("error", "preset-partial-validation", "partial Preset adoption was treated as a broken full snapshot", self.rel(script), {"returncode": partial_validation.returncode, "stdout": partial_validation.stdout[-1000:], "stderr": partial_validation.stderr[-1000:]})
        with tempfile.TemporaryDirectory(prefix="preset-isolated-") as td:
            isolated = Path(td) / "evolvable-application-preset"
            shutil.copytree(base, isolated)
            isolated_script = isolated / "scripts/preset.py"
            isolated_example = isolated / "examples/commerce-platform"
            isolated_out = Path(td) / "rendered"
            proc = self.run(
                [
                    sys.executable,
                    str(isolated_script),
                    "render",
                    "--input",
                    str(isolated_example / "preset-input.yaml"),
                    "--overlay",
                    str(isolated_example / "project-overlay.yaml"),
                    "--out",
                    str(isolated_out),
                ]
            )
            diffs = self.compare_trees(isolated_example / "expected", isolated_out) if proc.returncode == 0 else []
            if proc.returncode != 0 or diffs:
                self.add(
                    "error",
                    "preset-isolated-install",
                    "Preset failed when copied without sibling Skill directories",
                    self.rel(script),
                    {"returncode": proc.returncode, "diffs": diffs[:30], "stderr": proc.stderr[-1000:]},
                )
        failed = any(f["rule"].startswith("preset-") and f["severity"] == "error" for f in self.findings)
        self.check("preset-golden", "fail" if failed else "pass", {"example": self.rel(expected)})

    def check_effect_kit(self) -> None:
        kit = self.root / "tooling/effect-api-app-kit/scripts/kit.py"
        with tempfile.TemporaryDirectory(prefix="effect-kit-audit-") as td:
            base = Path(td)
            repo = base / "repo"
            (repo / "apps/api").mkdir(parents=True)
            (repo / "package.json").write_text(json.dumps({"name": "kit-audit", "private": True, "dependencies": {"effect": "3.21.4"}}) + "\n", encoding="utf-8")
            spec = {
                "schema_version": 1,
                "change": {"id": "add-order-create", "operation": "add-slice"},
                "host": {"path": "apps/api", "name": "api"},
                "slice": {"module": "orders", "subject": "order", "operation": "create", "pressure": "P2", "persistence": "postgres", "effect_profile": "installed"},
                "http": {"enabled": True, "route": "/orders"},
                "external_capability": {"name": "risk-score", "provider": "example-provider"},
                "verification": {"commands": [f'{sys.executable} -c "print(123)"']},
            }
            spec_path = base / "change.yaml"
            spec_path.write_text(yaml.safe_dump(spec, sort_keys=False), encoding="utf-8")
            apply = self.run([sys.executable, str(kit), "apply", "--repo", str(repo), "--change", str(spec_path)])
            if apply.returncode != 0:
                self.add("error", "effect-kit-apply", "Kit apply failed", self.rel(kit), {"stdout": apply.stdout[-2000:], "stderr": apply.stderr[-2000:]})
            verify = self.run([sys.executable, str(kit), "verify", "--repo", str(repo), "--run"])
            if verify.returncode != 0:
                self.add("error", "effect-kit-verify", "Kit structural/project-command verification failed", self.rel(kit), {"stdout": verify.stdout[-2000:], "stderr": verify.stderr[-2000:]})
            effect_stub = repo / "node_modules/effect"
            effect_stub.mkdir(parents=True, exist_ok=True)
            (effect_stub / "package.json").write_text('{"name":"effect","version":"0.0.0","type":"module","exports":{".":"./index.d.ts"}}\n', encoding="utf-8")
            (effect_stub / "index.d.ts").write_text('export namespace Effect { export interface Effect<A, E = never, R = never> { readonly _A?: A; readonly _E?: E; readonly _R?: R } }\n', encoding="utf-8")
            (repo / "package.json").write_text('{"name":"kit-audit","private":true,"type":"module"}\n', encoding="utf-8")
            (repo / "tsconfig.json").write_text(json.dumps({"compilerOptions":{"target":"ES2022","module":"NodeNext","moduleResolution":"NodeNext","strict":True,"noEmit":True,"skipLibCheck":True},"include":["apps/api/src/**/*.ts"]}, indent=2) + "\n", encoding="utf-8")
            local_tsc = self.root.parent / "node_modules/.bin/tsc"
            tsc_bin = str(local_tsc) if local_tsc.is_file() else shutil.which("tsc")
            if not tsc_bin:
                self.add("error", "effect-kit-template-typecheck", "TypeScript compiler is unavailable for generated-template verification", self.rel(kit))
            else:
                tsc = self.run([tsc_bin, "-p", "tsconfig.json"], cwd=repo)
                if tsc.returncode != 0:
                    self.add("error", "effect-kit-template-typecheck", "generated template failed the internal minimal Effect type-surface check", self.rel(kit), {"stdout": tsc.stdout[-2000:], "stderr": tsc.stderr[-2000:]})
            before = self.tree_hash(repo)
            duplicate = self.run([sys.executable, str(kit), "apply", "--repo", str(repo), "--change", str(spec_path)])
            after = self.tree_hash(repo)
            if duplicate.returncode == 0:
                self.add("error", "effect-kit-duplicate", "duplicate change unexpectedly succeeded", self.rel(kit))
            if before != after:
                self.add("error", "effect-kit-atomicity", "failed duplicate apply changed repository state", self.rel(kit))
            registry = repo / "apps/api/src/host/generated.modules.ts"
            registry.write_text(registry.read_text(encoding="utf-8") + "// drift\n", encoding="utf-8")
            drift = self.run([sys.executable, str(kit), "verify", "--repo", str(repo)])
            if drift.returncode == 0:
                self.add("error", "effect-kit-drift", "managed registry drift was not detected", self.rel(kit))
            repair = self.run([sys.executable, str(kit), "repair", "--repo", str(repo)])
            repaired = self.run([sys.executable, str(kit), "verify", "--repo", str(repo)])
            if repair.returncode != 0 or repaired.returncode != 0:
                self.add("error", "effect-kit-repair", "managed drift repair failed", self.rel(kit), {"repair": repair.stderr[-1000:] + repair.stdout[-1000:], "verify": repaired.stderr[-1000:] + repaired.stdout[-1000:]})

            # A pre-existing project-owned source file must block without side effects.
            repo2 = base / "conflict-repo"
            target = repo2 / "apps/api/src/modules/todos/todo.model.ts"
            target.parent.mkdir(parents=True)
            target.write_text("// project file\n", encoding="utf-8")
            spec2 = {
                "schema_version": 1,
                "change": {"id": "add-todo-create", "operation": "add-slice"},
                "host": {"path": "apps/api", "name": "api"},
                "slice": {"module": "todos", "subject": "todo", "operation": "create", "pressure": "P0", "persistence": "none", "effect_profile": "installed"},
                "verification": {"commands": []},
            }
            spec2_path = base / "conflict.yaml"
            spec2_path.write_text(yaml.safe_dump(spec2, sort_keys=False), encoding="utf-8")
            before2 = self.tree_hash(repo2)
            conflict = self.run([sys.executable, str(kit), "apply", "--repo", str(repo2), "--change", str(spec2_path)])
            after2 = self.tree_hash(repo2)
            if conflict.returncode == 0 or before2 != after2:
                self.add("error", "effect-kit-preflight", "source conflict did not fail atomically", self.rel(kit), {"returncode": conflict.returncode, "changed": before2 != after2})

            # Force a commit-time failure after the manifest replacement and verify rollback.
            repo3 = base / "rollback-repo"
            blocking_registry = repo3 / "apps/api/src/host/generated.modules.ts"
            blocking_registry.mkdir(parents=True)
            spec3_path = base / "rollback.yaml"
            spec3_path.write_text(yaml.safe_dump(spec2, sort_keys=False), encoding="utf-8")
            rollback = self.run([sys.executable, str(kit), "apply", "--repo", str(repo3), "--change", str(spec3_path)])
            if rollback.returncode == 0 or (repo3 / ".evo-kit/manifest.yaml").exists() or not blocking_registry.is_dir():
                self.add("error", "effect-kit-rollback", "commit-time failure did not restore the repository", self.rel(kit), {"returncode": rollback.returncode, "manifest_exists": (repo3 / ".evo-kit/manifest.yaml").exists(), "blocking_registry_preserved": blocking_registry.is_dir()})
        failed = any(f["rule"].startswith("effect-kit-") and f["severity"] == "error" for f in self.findings)
        self.check("effect-api-app-kit", "fail" if failed else "pass")

    def check_source_hygiene(self) -> None:
        required = [
            "README.md",
            "contracts/ai-coding-os-suite-contracts/SKILL.md",
            "contracts/ai-coding-os-suite-contracts/references/semantic-vocabulary.yaml",
            "router/ai-coding-os/SKILL.md",
            "architecture/evolvable-application-architecture/SKILL.md",
            "preset/evolvable-application-preset/SKILL.md",
            "tooling/effect-api-app-kit/SKILL.md",
        ]
        for rel in required:
            if not (self.root / rel).is_file():
                self.add("error", "source-hygiene", f"required grouped source file missing: {rel}", rel)
        if (self.root / "architecture/effect-best-practices/package.json").is_file():
            pkg = json.loads((self.root / "architecture/effect-best-practices/package.json").read_text(encoding="utf-8"))
            ts = ((pkg.get("devDependencies") or {}).get("typescript"))
            if ts and any(ts.startswith(prefix) for prefix in ("^", "~", ">", "<", "*")):
                self.add("error", "source-pin", "fixture TypeScript dependency is not exact", "architecture/effect-best-practices/package.json", ts)
        late_caches = [p for p in self.root.rglob("*") if p.name == "__pycache__" or p.suffix in {".pyc", ".pyo"}]
        for path in late_caches:
            self.add("error", "generated-cache", "audit subprocess created a release cache file", self.rel(path))
        self.check("source-hygiene", "pass" if not any(f["rule"] in {"source-hygiene", "source-pin", "generated-cache"} for f in self.findings) else "fail")

    def execute(self) -> dict[str, Any]:
        skills = self.parse_skill_frontmatter()
        self.check_contract_owners(skills)
        self.check_data_files()
        self.check_schema_instances()
        self.check_markdown_links()
        self.check_skill_portability(skills)
        self.check_contract_snapshot()
        self.check_source_conventions(skills)
        self.check_python()
        self.check_preset()
        self.check_effect_kit()
        self.check_source_hygiene()
        summary = {
            "error": sum(f["severity"] == "error" for f in self.findings),
            "warn": sum(f["severity"] == "warn" for f in self.findings),
            "info": sum(f["severity"] == "info" for f in self.findings),
            "total": len(self.findings),
        }
        return {
            "suite_root": str(self.root),
            "summary": summary,
            "checks": self.checks,
            "findings": self.findings,
            "claim_ceiling": "offline grouped-source structure, portable Skill-local links, frontmatter/cross-Skill reference closure, schema/link/data parsing, source conventions, Preset contract-snapshot/golden/merge/upgrade integration, Docs audit, architecture checker, experimental Kit atomicity/rollback smoke tests, and generated-template typecheck against a minimal internal Effect type surface; no external network, exact installed Effect API, production runtime, or production behavior claimed",
        }


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit the AI Coding OS Skill Suite")
    parser.add_argument("--suite", default=str(Path(__file__).resolve().parents[1]))
    parser.add_argument("--out")
    args = parser.parse_args()
    result = Audit(Path(args.suite)).execute()
    text = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
    print(text, end="")
    raise SystemExit(1 if result["summary"]["error"] else 0)


if __name__ == "__main__":
    main()
