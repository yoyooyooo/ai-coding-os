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
import time
import warnings
import zipfile
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
DEFAULT_SUBPROCESS_TIMEOUT_SECONDS = 120
MAX_CAPTURE_CHARS = 4000
SEMVER_RE = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")


def bounded_output(value: str | bytes | None) -> str:
    if value is None:
        return ""
    text = value.decode("utf-8", errors="replace") if isinstance(value, bytes) else value
    return text[-MAX_CAPTURE_CHARS:]


class Audit:
    def __init__(self, root: Path) -> None:
        self.root = root.resolve()
        self.findings: list[dict[str, Any]] = []
        self.checks: list[dict[str, Any]] = []
        self.active_check = "suite-audit"
        self.effect_template_typecheck = "not-run"

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

    def run(
        self,
        cmd: list[str],
        cwd: Path | None = None,
        *,
        timeout_seconds: float = DEFAULT_SUBPROCESS_TIMEOUT_SECONDS,
    ) -> subprocess.CompletedProcess[str]:
        env = os.environ.copy()
        env["PYTHONDONTWRITEBYTECODE"] = "1"
        try:
            return subprocess.run(
                cmd,
                cwd=cwd or self.root,
                text=True,
                capture_output=True,
                env=env,
                timeout=timeout_seconds,
            )
        except subprocess.TimeoutExpired as exc:
            stdout = bounded_output(exc.stdout)
            stderr = bounded_output(exc.stderr)
            self.add(
                "error",
                "subprocess-timeout",
                f"{self.active_check} subprocess exceeded {timeout_seconds:g}s",
                evidence={"command": cmd[:8], "stdout": stdout, "stderr": stderr},
            )
            return subprocess.CompletedProcess(cmd, 124, stdout=stdout, stderr=stderr or "subprocess timed out")

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

    def validate_schema_instance(self, schema_rel: str, instance: Any) -> None:
        schema_path = self.root / schema_rel
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        jsonschema.Draft202012Validator.check_schema(schema)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            resolver = jsonschema.RefResolver(base_uri=schema_path.resolve().as_uri(), referrer=schema)
        jsonschema.Draft202012Validator(schema, resolver=resolver).validate(instance)

    def check_schema_instances(self) -> None:
        cases = [
            ("contracts/ai-coding-os-suite-contracts/references/semantic-vocabulary.schema.json", "contracts/ai-coding-os-suite-contracts/references/semantic-vocabulary.yaml"),
            ("contracts/ai-coding-os-suite-contracts/references/harness/harness-descriptor.schema.json", "contracts/ai-coding-os-suite-contracts/references/harness/examples/order-checkout-retry.descriptor.yaml"),
            ("contracts/ai-coding-os-suite-contracts/references/harness/harness-result.schema.json", "contracts/ai-coding-os-suite-contracts/references/harness/examples/order-checkout-retry.result.yaml"),
            ("contracts/ai-coding-os-suite-contracts/references/evidence/evidence-envelope.schema.json", "contracts/ai-coding-os-suite-contracts/references/evidence/examples/harness-retry-observation.yaml"),
            ("contracts/ai-coding-os-suite-contracts/references/evidence/evidence-envelope.schema.json", "contracts/ai-coding-os-suite-contracts/references/evidence/examples/product-decision-evidence.yaml"),
            ("contracts/ai-coding-os-suite-contracts/references/evidence/evidence-envelope.schema.json", "contracts/ai-coding-os-suite-contracts/references/evidence/examples/execution-completion-evidence.yaml"),
            ("preset/evolvable-application-preset/schemas/preset-input.schema.json", "preset/evolvable-application-preset/examples/commerce-platform/preset-input.yaml"),
            ("preset/evolvable-application-preset/schemas/project-overlay.schema.json", "preset/evolvable-application-preset/examples/commerce-platform/project-overlay.yaml"),
            ("preset/evolvable-application-preset/schemas/architecture-profile.schema.json", "preset/evolvable-application-preset/examples/commerce-platform/expected/docs/standards/architecture-profile.yaml"),
            ("preset/evolvable-application-preset/schemas/naming-vocabulary.schema.json", "preset/evolvable-application-preset/examples/commerce-platform/expected/docs/standards/naming-vocabulary.yaml"),
            ("tooling/effect-api-app-kit/schemas/change-spec.schema.json", "tooling/effect-api-app-kit/examples/add-order-create.yaml"),
        ]
        for schema_rel, instance_rel in cases:
            try:
                instance_path = self.root / instance_rel
                if instance_path.suffix == ".json":
                    instance = json.loads(instance_path.read_text(encoding="utf-8"))
                else:
                    instance = yaml.safe_load(instance_path.read_text(encoding="utf-8"))
                self.validate_schema_instance(schema_rel, instance)
            except Exception as exc:
                self.add("error", "schema-validation", f"schema instance validation failed: {exc}", instance_rel, {"schema": schema_rel})
        legacy_cases = [
            (
                "contracts/ai-coding-os-suite-contracts/references/harness/harness-descriptor.schema.json",
                {"schema_version": 1, "id": "legacy", "capability": "legacy", "surface": "headless", "command": "verify", "can_observe": [], "does_not_cover": []},
            ),
            (
                "contracts/ai-coding-os-suite-contracts/references/harness/harness-result.schema.json",
                {"schema_version": 1, "harness": "legacy", "status": "pass", "observed": {}, "supports": [], "not_proven": []},
            ),
            (
                "contracts/ai-coding-os-suite-contracts/references/evidence/evidence-envelope.schema.json",
                {
                    "schema_version": 1,
                    "translation": "harness_to_execution",
                    "source_ref": {"kind": "harness_result", "ref": "legacy:result"},
                    "claim_ceiling": "legacy bounded claim",
                    "observed": {},
                    "supports": [],
                    "not_proven": [],
                    "evidence_refs": ["legacy:result"],
                    "verification_level": "legacy",
                },
            ),
        ]
        for schema_rel, instance in legacy_cases:
            try:
                self.validate_schema_instance(schema_rel, instance)
            except Exception as exc:
                self.add("error", "schema-validation", f"documented v1 compatibility failed: {exc}", schema_rel)

        static_proof = {"surface_kind": "headless", "dependency_reality": ["none"], "proof_focus": ["typecheck"]}
        try:
            self.validate_schema_instance("contracts/ai-coding-os-suite-contracts/references/proof/proof-surface.schema.json", static_proof)
        except Exception as exc:
            self.add("error", "schema-validation", f"pure static Proof Surface failed: {exc}", "contracts/ai-coding-os-suite-contracts/references/proof/proof-surface.schema.json")

        negative_cases = [
            (
                "evidence-v2-directional-field",
                "contracts/ai-coding-os-suite-contracts/references/evidence/evidence-envelope.schema.json",
                {
                    "schema_version": 2,
                    "translation": "harness_to_execution",
                    "source_ref": "hr:1",
                    "claim_ceiling": "invalid v2 direction",
                    "observed": {},
                    "supports": [],
                    "not_proven": [],
                    "evidence_refs": ["hr:1"],
                },
            ),
            (
                "evidence-direction-kind-mismatch",
                "contracts/ai-coding-os-suite-contracts/references/evidence/evidence-envelope.schema.json",
                {
                    "schema_version": 1,
                    "translation": "harness_to_execution",
                    "source_ref": {"kind": "product_decision", "ref": "PDR-1"},
                    "claim_ceiling": "invalid legacy pair",
                    "observed": {},
                    "supports": [],
                    "not_proven": [],
                    "evidence_refs": ["PDR-1"],
                    "verification_level": "legacy",
                },
            ),
            (
                "proof-none-mixed-with-runtime",
                "contracts/ai-coding-os-suite-contracts/references/proof/proof-surface.schema.json",
                {"surface_kind": "headless", "dependency_reality": ["none", "fake"], "proof_focus": ["typecheck"]},
            ),
            (
                "descriptor-v2-legacy-surface",
                "contracts/ai-coding-os-suite-contracts/references/harness/harness-descriptor.schema.json",
                {
                    "schema_version": 2,
                    "id": "invalid",
                    "capability": "invalid",
                    "surface": "browser",
                    "proof_surface": {"surface_kind": "headless", "dependency_reality": ["none"]},
                    "command": "typecheck",
                    "can_observe": [],
                    "does_not_cover": [],
                    "claim_ceiling": "static",
                },
            ),
            (
                "result-v2-legacy-environment",
                "contracts/ai-coding-os-suite-contracts/references/harness/harness-result.schema.json",
                {
                    "schema_version": 2,
                    "harness": "invalid",
                    "status": "pass",
                    "proof_surface": {"surface_kind": "headless", "dependency_reality": ["none"]},
                    "claim_ceiling": "static",
                    "observed": {},
                    "supports": [],
                    "not_proven": [],
                    "environment": "local",
                },
            ),
            (
                "descriptor-v2-legacy-does-not-cover-alias",
                "contracts/ai-coding-os-suite-contracts/references/harness/harness-descriptor.schema.json",
                {
                    "schema_version": 2,
                    "id": "invalid-alias",
                    "capability": "invalid-alias",
                    "proof_surface": {"surface_kind": "headless", "dependency_reality": ["none"]},
                    "command": "typecheck",
                    "can_observe": [],
                    "does_not_cover": [],
                    "doesNotCover": ["duplicate fact"],
                    "claim_ceiling": "static",
                },
            ),
            (
                "descriptor-v2-legacy-exercises",
                "contracts/ai-coding-os-suite-contracts/references/harness/harness-descriptor.schema.json",
                {
                    "schema_version": 2,
                    "id": "invalid-exercises",
                    "capability": "invalid-exercises",
                    "proof_surface": {"surface_kind": "headless", "dependency_reality": ["none"]},
                    "command": "typecheck",
                    "can_observe": [],
                    "does_not_cover": [],
                    "exercises": ["legacy proof claim"],
                    "claim_ceiling": "static",
                },
            ),
            (
                "result-v2-legacy-not-proven-alias",
                "contracts/ai-coding-os-suite-contracts/references/harness/harness-result.schema.json",
                {
                    "schema_version": 2,
                    "harness": "invalid-alias",
                    "status": "pass",
                    "proof_surface": {"surface_kind": "headless", "dependency_reality": ["none"]},
                    "claim_ceiling": "static",
                    "observed": {},
                    "supports": [],
                    "not_proven": [],
                    "notProven": ["duplicate fact"],
                },
            ),
            (
                "kit-p3-harness-binding-required",
                "tooling/effect-api-app-kit/schemas/change-spec.schema.json",
                {
                    "schema_version": 1,
                    "change": {"id": "p3-without-command", "operation": "add-slice"},
                    "host": {"path": "apps/api", "name": "api"},
                    "slice": {"module": "orders", "subject": "order", "operation": "recover", "pressure": "P3", "persistence": "postgres", "effect_profile": "installed"},
                    "external_capability": {"name": "provider", "provider": "example"},
                    "verification": {"commands": ["pnpm test"]},
                },
            ),
        ]
        for case_id, schema_rel, instance in negative_cases:
            try:
                self.validate_schema_instance(schema_rel, instance)
            except Exception:
                continue
            self.add("error", "schema-negative", f"invalid schema case was accepted: {case_id}", schema_rel)

        forbidden_path = self.root / "contracts/ai-coding-os-suite-contracts/references/evidence/examples/forbidden-promotions.yaml"
        forbidden = yaml.safe_load(forbidden_path.read_text(encoding="utf-8")) or {}
        expected_forbidden = {
            "harness-pass-is-not-execution-complete",
            "harness-not-proven-is-not-execution-exclusion",
            "accepted-target-is-not-verified-implementation",
            "observed-behavior-is-not-future-intent",
            "execution-status-is-not-product-or-doc-acceptance",
            "docs-evidence-is-not-document-acceptance",
        }
        actual_forbidden = {item.get("id") for item in forbidden.get("cases", []) if isinstance(item, dict)}
        if actual_forbidden != expected_forbidden:
            self.add("error", "evidence-promotion-cases", "forbidden evidence promotions are incomplete or drifted", self.rel(forbidden_path), {"expected": sorted(expected_forbidden), "actual": sorted(item for item in actual_forbidden if item)})
        total_cases = len(cases) + len(legacy_cases) + 1
        failed = any(f["rule"] in {"schema-validation", "schema-negative", "evidence-promotion-cases"} for f in self.findings)
        self.check("schema-validation", "fail" if failed else "pass", {"positive_cases": total_cases, "negative_cases": len(negative_cases), "evidence_examples": 3, "forbidden_promotions": len(actual_forbidden)})

    def check_evals(self, skills: dict[str, dict[str, Any]]) -> None:
        schema_rel = "contracts/ai-coding-os-suite-contracts/references/evals/skill-evals.schema.json"
        files = 0
        cases = 0
        composition_cases = 0
        for name, skill in sorted(skills.items()):
            eval_dir = self.root / skill["path"] / "evals"
            eval_paths = sorted(eval_dir.glob("*.json")) if eval_dir.is_dir() else []
            if not eval_paths:
                self.add("error", "eval-missing", f"Skill {name} has no eval file", skill["file"])
                continue
            ids: set[str] = set()
            for path in eval_paths:
                files += 1
                try:
                    data = json.loads(path.read_text(encoding="utf-8"))
                    self.validate_schema_instance(schema_rel, data)
                except Exception as exc:
                    self.add("error", "eval-schema", f"eval file failed schema validation: {exc}", self.rel(path))
                    continue
                if data.get("skill_name") != name:
                    self.add("error", "eval-skill-name", f"eval skill_name must match {name}", self.rel(path), data.get("skill_name"))
                for case in data.get("evals", []):
                    cases += 1
                    case_id = str(case.get("id"))
                    if case_id in ids:
                        self.add("error", "eval-id-duplicate", f"duplicate eval case id for {name}: {case_id}", self.rel(path))
                    ids.add(case_id)
                    expectations = case.get("expectations")
                    if not isinstance(expectations, list) or len(expectations) < 2:
                        self.add(
                            "error",
                            "eval-expectations",
                            "each core eval needs at least a positive artifact/observation expectation and an ownership/claim-boundary expectation",
                            self.rel(path),
                            {"case_id": case_id},
                        )
                    if path.name == "composition.evals.json":
                        composition_cases += 1
        failed_rules = {"eval-missing", "eval-schema", "eval-skill-name", "eval-id-duplicate", "eval-expectations"}
        failed = any(f["rule"] in failed_rules for f in self.findings)
        self.check("skill-evals", "fail" if failed else "pass", {"files": files, "cases": cases, "composition_cases": composition_cases})

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
                try:
                    candidate.relative_to(self.root)
                except ValueError:
                    self.add("error", "bundle-external-markdown-link", f"Core Markdown link escapes skills/** and would break in the Core ZIP: {raw}", self.rel(path), str(candidate))
                    continue
                if not candidate.exists():
                    self.add("error", "markdown-link", f"broken relative Markdown link: {raw}", self.rel(path), self.rel(candidate))
        failed_rules = {"markdown-link", "bundle-external-markdown-link"}
        self.check("markdown-links", "fail" if any(f["rule"] in failed_rules for f in self.findings) else "pass", {"links": checked})

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
        self.active_check = "preset-golden"
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
                profile = yaml.safe_load((out / "docs/standards/architecture-profile.yaml").read_text(encoding="utf-8")) or {}
                agents_text = (out / "AGENTS.md").read_text(encoding="utf-8")
                adoption_adr = (out / "docs/adr/0001-adopt-evolvable-application-preset.md").read_text(encoding="utf-8")
                source_standard = (out / "docs/standards/source-topology-and-naming.md").read_text(encoding="utf-8")
                profile_resolution = profile.get("profile_resolution") or {}
                if (
                    (profile.get("preset") or {}).get("mode") != "candidate-snapshot"
                    or profile_resolution.get("requested") != (yaml.safe_load((example / "preset-input.yaml").read_text(encoding="utf-8")) or {}).get("profiles")
                    or profile_resolution.get("defaults_added") != []
                    or profile_resolution.get("dependency_added") != ["application-core"]
                    or profile_resolution.get("resolved") != profile.get("profiles")
                    or "- Status: proposed" not in adoption_adr
                    or "candidate" not in agents_text.lower()
                    or ("candidate" not in source_standard.lower() and "候选" not in source_standard)
                    or (out / "docs/ssot/authority-map.md").exists()
                    or not (out / "docs/architecture/fact-authority-map.md").is_file()
                ):
                    self.add("error", "preset-candidate-truth", "Preset render claimed adoption/current authority or misplaced the fact-writer map", self.rel(script))
                rendered_vocabulary = yaml.safe_load((out / "docs/standards/naming-vocabulary.yaml").read_text(encoding="utf-8")) or {}
                project_terms = rendered_vocabulary.get("project_terms") or {}
                duplicated_meanings = sorted(token for token, spec in project_terms.items() if isinstance(spec, dict) and ("meaning" in spec or "not_the_same_as" in spec))
                missing_meaning_refs = sorted(token for token, spec in project_terms.items() if not isinstance(spec, dict) or spec.get("meaning_ref") != "../ssot/product-language.md")
                if duplicated_meanings or missing_meaning_refs:
                    self.add("error", "preset-product-language-shadow", "source naming output duplicated product meaning or omitted its SSoT reference", self.rel(out / "docs/standards/naming-vocabulary.yaml"), {"duplicated": duplicated_meanings, "missing_refs": missing_meaning_refs})
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
                english_adr = (english_out / "docs/adr/0001-adopt-evolvable-application-preset.md").read_text(encoding="utf-8") if english.returncode == 0 else ""
                english_profile = yaml.safe_load((english_out / "docs/standards/architecture-profile.yaml").read_text(encoding="utf-8")) if english.returncode == 0 else {}
                if english.returncode != 0 or "## TypeScript / Node Projection" not in english_source or "<subject>.<operation>.use-case.ts" not in english_source or "candidate" not in english_source.lower() or "- Status: proposed" not in english_adr or "Date: 2026-07-23" not in english_adr or (english_profile.get("preset") or {}).get("mode") != "candidate-snapshot" or not (english_out / "docs/architecture/fact-authority-map.md").is_file():
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
                snapshot = inspected.get("preset_snapshot") or {}
                if inspect.returncode != 0 or not inspected.get("managed_agents_section") or "docs/standards/architecture-profile.yaml" not in (inspected.get("existing_surfaces") or []) or snapshot.get("mode") != "candidate-snapshot" or not snapshot.get("profiles") or inspected.get("adopted_preset") is not None:
                    self.add("error", "preset-inspect", "Preset inspect did not expose candidate facts without claiming adoption", self.rel(script), {"returncode": inspect.returncode, "output": inspected, "stderr": inspect.stderr[-1000:]})
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
            def render_profile_case(label: str, profile_ids: list[str]) -> tuple[subprocess.CompletedProcess[str], Path, dict[str, Any], dict[str, Any]]:
                input_path = base_path / f"{label}-input.yaml"
                input_path.write_text(yaml.safe_dump({"schema_version": 1, "profiles": profile_ids}, sort_keys=False), encoding="utf-8")
                output = base_path / f"{label}-out"
                process = self.run([sys.executable, str(script), "render", "--input", str(input_path), "--overlay", str(example / "project-overlay.yaml"), "--out", str(output)])
                try:
                    profile = yaml.safe_load((output / "docs/standards/architecture-profile.yaml").read_text(encoding="utf-8")) if process.returncode == 0 else {}
                    vocabulary = yaml.safe_load((output / "docs/standards/naming-vocabulary.yaml").read_text(encoding="utf-8")) if process.returncode == 0 else {}
                except (OSError, yaml.YAMLError):
                    profile, vocabulary = {}, {}
                return process, output, profile, vocabulary

            minimal, minimal_out, minimal_profile, minimal_vocabulary = render_profile_case("minimal", ["monorepo-core"])
            minimal_owners = set((minimal_vocabulary.get("contract_selection") or {}).get("term_owners") or [])
            minimal_terms = set((minimal_vocabulary.get("canonical_terms") or {}).keys())
            expected_minimal_terms = {"command", "command-context", "query", "use-case", "policy", "projection", "observation", "candidate", "receipt", "port", "repository", "transaction", "idempotency", "contract", "schema", "mapper", "composition", "migration"}
            minimal_patterns = minimal_vocabulary.get("filename_patterns") or []
            minimal_resolution = minimal_profile.get("profile_resolution") or {}
            minimal_source_standard = (minimal_out / "docs/standards/source-topology-and-naming.md").read_text(encoding="utf-8") if minimal.returncode == 0 else ""
            if (
                minimal.returncode != 0
                or minimal_owners != {"evolvable-application-architecture"}
                or not expected_minimal_terms.issubset(minimal_terms)
                or minimal_patterns
                or ".ts" in minimal_source_standard
                or minimal_resolution.get("requested") != ["monorepo-core"]
                or minimal_resolution.get("defaults_added") != ["agent-entry"]
                or minimal_resolution.get("dependency_added") != ["application-core"]
                or minimal_resolution.get("resolved") != ["agent-entry", "application-core", "monorepo-core"]
                or minimal_terms.intersection({"layer", "runtime", "client", "store", "harness", "scenario"})
                or (minimal_out / "docs/standards/verification-policy.md").exists()
                or (minimal_out / "tooling/architecture_check.py").exists()
            ):
                self.add("error", "preset-profile-minimality", "minimal language-neutral profile leaked filename patterns, lost provenance, or omitted selected terms", self.rel(script), {"returncode": minimal.returncode, "owners": sorted(minimal_owners), "terms": sorted(minimal_terms), "patterns": minimal_patterns, "resolution": minimal_resolution, "expected_terms": sorted(expected_minimal_terms)})

            composed, composed_out, composed_profile, composed_vocabulary = render_profile_case("composed", ["react", "verification-core"])
            composed_owners = set((composed_vocabulary.get("contract_selection") or {}).get("term_owners") or [])
            composed_pattern_owners = {item.get("owner") for item in composed_vocabulary.get("filename_patterns", []) if isinstance(item, dict)}
            composed_resolution = composed_profile.get("profile_resolution") or {}
            composed_added = set(composed_resolution.get("dependency_added") or [])
            if (
                composed.returncode != 0
                or composed_owners != {"evolvable-application-architecture", "frontend-architecture", "product-harness-system"}
                or composed_pattern_owners != {"evolvable-application-architecture", "frontend-architecture"}
                or not {"application-core", "typescript-node"}.issubset(composed_added)
                or "monorepo-core" in composed_added
                or composed_resolution.get("defaults_added") != ["agent-entry"]
                or "effect-best-practices" in composed_owners
                or not (composed_out / "docs/standards/verification-policy.md").is_file()
                or not (composed_out / "tooling/architecture_check.py").is_file()
            ):
                self.add("error", "preset-profile-composition", "composed profile did not preserve language/profile boundaries or provenance", self.rel(script), {"returncode": composed.returncode, "owners": sorted(composed_owners), "pattern_owners": sorted(owner for owner in composed_pattern_owners if owner), "resolution": composed_resolution})

            closure, closure_out, closure_profile, closure_vocabulary = render_profile_case("closure", ["effect-httpapi-v4"])
            closure_profiles = set(closure_profile.get("profiles") or [])
            closure_added = set((closure_profile.get("profile_resolution") or {}).get("dependency_added") or [])
            closure_owners = set((closure_vocabulary.get("contract_selection") or {}).get("term_owners") or [])
            if (
                closure.returncode != 0
                or not {"application-core", "effect", "typescript-node"}.issubset(closure_profiles)
                or not {"application-core", "effect", "typescript-node"}.issubset(closure_added)
                or "monorepo-core" in closure_profiles
                or closure_owners != {"evolvable-application-architecture", "effect-best-practices"}
                or not (closure_out / "tooling/architecture_check.py").is_file()
                or (closure_out / "docs/standards/verification-policy.md").exists()
            ):
                self.add("error", "preset-profile-closure", "Preset dependency closure or adopted vocabulary drifted", self.rel(script), {"returncode": closure.returncode, "profiles": sorted(closure_profiles), "dependency_added": sorted(closure_added), "owners": sorted(closure_owners)})

            rust_case, rust_out, rust_profile, rust_vocabulary = render_profile_case("rust", ["rust"])
            rust_profiles = rust_profile.get("profiles") or []
            rust_patterns = rust_vocabulary.get("filename_patterns") or []
            rust_source = (rust_out / "docs/standards/source-topology-and-naming.md").read_text(encoding="utf-8") if rust_case.returncode == 0 else ""
            if (
                rust_case.returncode != 0
                or rust_profiles != ["agent-entry", "application-core", "rust"]
                or rust_patterns
                or ".ts" in rust_source
                or "Rust" not in rust_source
                or "monorepo-core" in rust_profiles
                or (rust_out / "tooling/architecture_check.py").exists()
            ):
                self.add("error", "preset-rust-profile", "Rust profile inherited TypeScript or Monorepo assumptions, or lost its Rust projection", self.rel(script), {"returncode": rust_case.returncode, "profiles": rust_profiles, "patterns": rust_patterns})
            bad_overlay = yaml.safe_load((example / "project-overlay.yaml").read_text(encoding="utf-8"))
            bad_overlay["authorities"] = ["not-an-object"]
            bad_overlay_path = base_path / "invalid-overlay.yaml"
            bad_overlay_path.write_text(yaml.safe_dump(bad_overlay, sort_keys=False), encoding="utf-8")
            invalid = self.run([sys.executable, str(script), "render", "--input", str(example / "preset-input.yaml"), "--overlay", str(bad_overlay_path), "--out", str(base_path / "invalid-out")])
            if invalid.returncode == 0 or "Traceback" in invalid.stderr or "authorities[0]" not in invalid.stderr:
                self.add("error", "preset-overlay-validation", "invalid overlay did not produce a structured validation error", self.rel(script), {"returncode": invalid.returncode, "stderr": invalid.stderr[-1000:]})
            lean_overlay = yaml.safe_load((example / "project-overlay.yaml").read_text(encoding="utf-8"))
            for key in ("deployables", "packages", "modules", "workflows", "topology_notes", "domain_terms", "authorities", "harness_coverage", "exceptions"):
                lean_overlay.pop(key, None)
            lean_overlay_path = base_path / "lean-overlay.yaml"
            lean_overlay_path.write_text(yaml.safe_dump(lean_overlay, sort_keys=False), encoding="utf-8")
            lean_input_path = base_path / "lean-input.yaml"
            lean_input_path.write_text(yaml.safe_dump({"schema_version": 1, "profiles": ["monorepo-core"]}, sort_keys=False), encoding="utf-8")
            lean_out = base_path / "lean-out"
            lean = self.run([sys.executable, str(script), "render", "--input", str(lean_input_path), "--overlay", str(lean_overlay_path), "--out", str(lean_out)])
            unearned_layers = [rel for rel in ("docs/product", "docs/ssot", "docs/architecture", "docs/product-harness") if (lean_out / rel).exists()]
            if lean.returncode != 0 or unearned_layers:
                self.add("error", "preset-incremental-shape", "minimal technical render created unearned project knowledge layers", self.rel(script), {"returncode": lean.returncode, "unearned_layers": unearned_layers, "stderr": lean.stderr[-1000:]})

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
        self.active_check = "effect-api-app-kit"
        kit = self.root / "tooling/effect-api-app-kit/scripts/kit.py"
        with tempfile.TemporaryDirectory(prefix="effect-kit-audit-") as td:
            base = Path(td)
            repo = base / "repo"
            (repo / "apps/api").mkdir(parents=True)
            (repo / "package.json").write_text(json.dumps({"name": "kit-audit", "private": True, "dependencies": {"effect": "3.21.4"}}) + "\n", encoding="utf-8")
            harness_entry = repo / "tests/order-create-recovery.py"
            harness_entry.parent.mkdir(parents=True)
            harness_entry.write_text('print("recovery-harness-entry")\n', encoding="utf-8")
            harness_command = f'{sys.executable} tests/order-create-recovery.py'
            spec = {
                "schema_version": 1,
                "change": {"id": "add-order-create", "operation": "add-slice"},
                "host": {"path": "apps/api", "name": "api"},
                "slice": {"module": "orders", "subject": "order", "operation": "create", "pressure": "P3", "persistence": "postgres", "effect_profile": "installed"},
                "http": {"enabled": True, "route": "/orders"},
                "external_capability": {"name": "risk-score", "provider": "example-provider"},
                "verification": {
                    "commands": [harness_command],
                    "harness": {
                        "entry": "tests/order-create-recovery.py",
                        "command": harness_command,
                        "can_observe": ["project recovery Harness entry outcome"],
                        "does_not_cover": ["production external-provider behavior"],
                        "claim_ceiling": "project-declared local recovery Harness entry outcome",
                    },
                },
            }
            try:
                self.validate_schema_instance("tooling/effect-api-app-kit/schemas/change-spec.schema.json", spec)
            except Exception as exc:
                self.add("error", "effect-kit-p3-change-spec", f"project-bound P3 Change Spec failed schema validation: {exc}", self.rel(kit))
            spec_path = base / "change.yaml"
            spec_path.write_text(yaml.safe_dump(spec, sort_keys=False), encoding="utf-8")
            apply = self.run([sys.executable, str(kit), "apply", "--repo", str(repo), "--change", str(spec_path)])
            if apply.returncode != 0:
                self.add("error", "effect-kit-apply", "Kit apply failed", self.rel(kit), {"stdout": apply.stdout[-2000:], "stderr": apply.stderr[-2000:]})
            descriptor_path = repo / "apps/api/src/modules/orders/order.create.recovery.harness.yaml"
            try:
                descriptor = yaml.safe_load(descriptor_path.read_text(encoding="utf-8"))
                self.validate_schema_instance("contracts/ai-coding-os-suite-contracts/references/harness/harness-descriptor.schema.json", descriptor)
                uses = descriptor.get("uses") or {}
                if descriptor.get("command") != harness_command or descriptor.get("can_observe") != ["project recovery Harness entry outcome"] or uses.get("harness_entry") != "tests/order-create-recovery.py" or uses.get("binding") != "project-provided":
                    raise ValueError("Descriptor did not preserve the explicit project Harness binding")
            except Exception as exc:
                self.add("error", "effect-kit-p3-descriptor", f"P3 output is not a schema-valid, project-bound Harness Descriptor v2: {exc}", self.rel(kit))
            verify = self.run([sys.executable, str(kit), "verify", "--repo", str(repo), "--run"])
            if verify.returncode != 0:
                self.add("error", "effect-kit-verify", "Kit structural/project-command verification failed", self.rel(kit), {"stdout": verify.stdout[-2000:], "stderr": verify.stderr[-2000:]})

            manifest_path = repo / ".evo-kit/manifest.yaml"
            manifest_before_timeout = manifest_path.read_text(encoding="utf-8")
            timeout_manifest = yaml.safe_load(manifest_before_timeout)
            timeout_manifest["verification_commands"] = [harness_command, f'{sys.executable} -c "import time; time.sleep(10)"']
            manifest_path.write_text(yaml.safe_dump(timeout_manifest, sort_keys=False), encoding="utf-8")
            timeout_started = time.monotonic()
            timed_out = self.run([sys.executable, str(kit), "verify", "--repo", str(repo), "--run", "--timeout-seconds", "1"], timeout_seconds=10)
            timeout_elapsed = time.monotonic() - timeout_started
            try:
                timeout_data = json.loads(timed_out.stdout)
            except json.JSONDecodeError:
                timeout_data = {}
            timeout_rules = {item.get("rule") for item in timeout_data.get("findings", []) if isinstance(item, dict)}
            timeout_commands = timeout_data.get("commands") or []
            if timed_out.returncode == 0 or timeout_elapsed >= 5 or "verification-command-timeout" not in timeout_rules or len(timeout_commands) != 2 or timeout_commands[-1].get("status") != "timeout" or "Traceback" in timed_out.stderr:
                self.add("error", "effect-kit-command-timeout", "Kit verify did not terminate a hanging command with bounded structured output", self.rel(kit), {"returncode": timed_out.returncode, "elapsed": timeout_elapsed, "rules": sorted(rule for rule in timeout_rules if rule), "stdout": bounded_output(timed_out.stdout), "stderr": bounded_output(timed_out.stderr)})
            manifest_path.write_text(manifest_before_timeout, encoding="utf-8")
            effect_stub = repo / "node_modules/effect"
            effect_stub.mkdir(parents=True, exist_ok=True)
            (effect_stub / "package.json").write_text('{"name":"effect","version":"0.0.0","type":"module","exports":{".":"./index.d.ts"}}\n', encoding="utf-8")
            (effect_stub / "index.d.ts").write_text('export namespace Effect { export interface Effect<A, E = never, R = never> { readonly _A?: A; readonly _E?: E; readonly _R?: R } }\n', encoding="utf-8")
            (repo / "package.json").write_text('{"name":"kit-audit","private":true,"type":"module"}\n', encoding="utf-8")
            (repo / "tsconfig.json").write_text(json.dumps({"compilerOptions":{"target":"ES2022","module":"NodeNext","moduleResolution":"NodeNext","strict":True,"noEmit":True,"skipLibCheck":True},"include":["apps/api/src/**/*.ts"]}, indent=2) + "\n", encoding="utf-8")
            local_tsc = self.root.parent / "node_modules/.bin/tsc"
            tsc_bin = str(local_tsc) if local_tsc.is_file() else shutil.which("tsc")
            if not tsc_bin:
                self.effect_template_typecheck = "not-run-compiler-unavailable"
            else:
                tsc = self.run([tsc_bin, "-p", "tsconfig.json"], cwd=repo)
                self.effect_template_typecheck = "pass" if tsc.returncode == 0 else "fail"
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
            try:
                rollback_error = json.loads(rollback.stderr)
            except json.JSONDecodeError:
                rollback_error = {}
            if rollback.returncode == 0 or (repo3 / ".evo-kit/manifest.yaml").exists() or (repo3 / ".evo-kit/lock").exists() or not blocking_registry.is_dir() or rollback_error.get("error_code") != "commit-failed" or rollback_error.get("rolled_back") is not True or "Traceback" in rollback.stderr:
                self.add("error", "effect-kit-rollback", "commit-time failure did not restore the repository and release its lock with structured machine output", self.rel(kit), {"returncode": rollback.returncode, "manifest_exists": (repo3 / ".evo-kit/manifest.yaml").exists(), "lock_exists": (repo3 / ".evo-kit/lock").exists(), "blocking_registry_preserved": blocking_registry.is_dir(), "error": rollback_error, "stderr": bounded_output(rollback.stderr)})
        failed = any(f["rule"].startswith("effect-kit-") and f["severity"] == "error" for f in self.findings)
        self.check("effect-api-app-kit", "fail" if failed else "pass", {"p3_harness_binding": "project-provided", "verification_command_timeout": "pass", "structured_rollback": "pass", "template_typecheck": self.effect_template_typecheck})

    def check_bundle_builder(self, skills: dict[str, dict[str, Any]]) -> None:
        self.active_check = "core-bundle-builder"
        with tempfile.TemporaryDirectory(prefix="suite-bundle-audit-") as td:
            base = Path(td)
            bundle_root = base / "bundle-root"
            isolated_suite = bundle_root / "skills"
            shutil.copytree(self.root, isolated_suite)
            isolated_audit_path = base / "isolated-audit.json"
            isolated_source_hash = self.tree_hash(isolated_suite)
            isolated_audit_path.write_text(
                json.dumps({
                    "suite_root": str(isolated_suite),
                    "source_tree_sha256": isolated_source_hash,
                    "summary": {"error": 0, "warn": 0, "info": 0, "total": 0},
                    "checks": [{"name": "effect-api-app-kit", "status": "pass", "detail": {"template_typecheck": "pass"}}],
                    "findings": [],
                    "claim_ceiling": "machine-a diagnostic claim",
                }),
                encoding="utf-8",
            )
            out_dir = base / "out"
            builder = isolated_suite / "tooling/build_suite_release.py"
            result = self.run(
                [
                    sys.executable,
                    str(builder),
                    "--repo",
                    str(bundle_root),
                    "--audit",
                    str(isolated_audit_path),
                    "--out-dir",
                    str(out_dir),
                ]
            )
            if result.returncode != 0:
                self.add("error", "bundle-builder", "Core-only bundle builder failed", self.rel(self.root / "tooling/build_suite_release.py"), {"stdout": bounded_output(result.stdout), "stderr": bounded_output(result.stderr)})
            else:
                try:
                    payload = json.loads(result.stdout)
                    archive = Path(payload["archive"])
                    manifest_path = Path(payload["manifest"])
                    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
                    release_audit_path = Path(payload["audit"])
                    release_audit = json.loads(release_audit_path.read_text(encoding="utf-8"))
                    reports = manifest.get("reports") or {}
                    with zipfile.ZipFile(archive) as zipped:
                        names = zipped.namelist()
                    non_skill_entries = [name for name in names if "/skills/" not in name or not name.split("/", 1)[1].startswith("skills/")]
                    expected_names = set(skills)
                    actual_names = {item.get("name") for item in manifest.get("skills", []) if isinstance(item, dict)}
                    source_hash = self.tree_hash(isolated_suite)
                    if (
                        non_skill_entries
                        or manifest.get("archive_scope", {}).get("includes") != ["skills/**"]
                        or actual_names != expected_names
                        or set(reports) != {"change_report", "composition_eval_review"}
                        or manifest.get("source_tree_sha256") != source_hash
                        or (manifest.get("audit") or {}).get("source_tree_sha256") != source_hash
                        or (manifest.get("audit") or {}).get("report") != release_audit_path.name
                        or (manifest.get("audit") or {}).get("sha256") != hashlib.sha256(release_audit_path.read_bytes()).hexdigest()
                        or release_audit.get("suite_root") != "skills"
                        or (release_audit.get("release_canonicalization") or {}).get("version") != 1
                    ):
                        self.add(
                            "error",
                            "bundle-boundary",
                            "Core bundle scope, roster, source provenance, or sidecar reports drifted",
                            self.rel(self.root / "tooling/build_suite_release.py"),
                            {
                                "non_skill_entries": non_skill_entries[:10],
                                "manifest_scope": manifest.get("archive_scope"),
                                "expected_skills": sorted(expected_names),
                                "actual_skills": sorted(name for name in actual_names if name),
                                "reports": sorted(reports),
                                "source_hash": source_hash,
                                "manifest_source_hash": manifest.get("source_tree_sha256"),
                            },
                        )

                    bundle_root_b = base / "different-absolute-root" / "bundle-root"
                    isolated_suite_b = bundle_root_b / "skills"
                    shutil.copytree(self.root, isolated_suite_b)
                    audit_b_path = base / "machine-b-audit.json"
                    audit_b_path.write_text(
                        json.dumps({
                            "suite_root": str(isolated_suite_b),
                            "source_tree_sha256": self.tree_hash(isolated_suite_b),
                            "summary": {"error": 0, "warn": 0, "info": 0, "total": 0},
                            "checks": [{"name": "effect-api-app-kit", "status": "pass", "detail": {"template_typecheck": "not-run-compiler-unavailable"}}],
                            "findings": [],
                            "claim_ceiling": "machine-b diagnostic claim",
                        }),
                        encoding="utf-8",
                    )
                    result_b = self.run([
                        sys.executable,
                        str(isolated_suite_b / "tooling/build_suite_release.py"),
                        "--repo",
                        str(bundle_root_b),
                        "--audit",
                        str(audit_b_path),
                        "--out-dir",
                        str(base / "out-b"),
                    ])
                    if result_b.returncode != 0:
                        self.add("error", "bundle-cross-machine-determinism", "second-path deterministic build failed", self.rel(self.root / "tooling/build_suite_release.py"), bounded_output(result_b.stderr))
                    else:
                        payload_b = json.loads(result_b.stdout)
                        artifact_keys = ("archive", "audit", "manifest", "change_report", "composition_eval_review")
                        mismatches = [key for key in artifact_keys if Path(payload[key]).read_bytes() != Path(payload_b[key]).read_bytes()]
                        if mismatches:
                            self.add("error", "bundle-cross-machine-determinism", "release artifacts vary by absolute source path or compiler availability", self.rel(self.root / "tooling/build_suite_release.py"), mismatches)
                except Exception as exc:
                    self.add("error", "bundle-builder", f"could not inspect Core-only bundle output: {exc}", self.rel(self.root / "tooling/build_suite_release.py"))

            stale_audit_path = base / "stale-audit.json"
            stale_audit_path.write_text(json.dumps({"source_tree_sha256": "0" * 64, "summary": {"error": 0, "warn": 0, "info": 0, "total": 0}}), encoding="utf-8")
            stale = self.run([
                sys.executable,
                str(builder),
                "--repo",
                str(bundle_root),
                "--audit",
                str(stale_audit_path),
                "--out-dir",
                str(base / "stale-out"),
            ])
            if stale.returncode == 0 or "source_tree_sha256" not in stale.stderr:
                self.add("error", "bundle-audit-provenance", "builder accepted an audit for a different source tree", self.rel(self.root / "tooling/build_suite_release.py"), {"returncode": stale.returncode, "stderr": bounded_output(stale.stderr)})
        failed_rules = {"bundle-builder", "bundle-boundary", "bundle-audit-provenance", "bundle-cross-machine-determinism"}
        failed = any(f["rule"] in failed_rules for f in self.findings)
        self.check("core-bundle-builder", "fail" if failed else "pass", {"skills": len(skills), "isolated": True, "source_bound": True, "canonical_audit_sidecar": True, "cross_machine_deterministic": True})

    def check_subprocess_timeout(self) -> None:
        probe = Audit(self.root)
        probe.active_check = "timeout-contract-probe"
        result = probe.run([sys.executable, "-c", "import time; time.sleep(1)"], timeout_seconds=0.02)
        timeout_findings = [item for item in probe.findings if item.get("rule") == "subprocess-timeout"]
        if result.returncode != 124 or len(timeout_findings) != 1 or "timeout-contract-probe" not in timeout_findings[0].get("message", ""):
            self.add("error", "subprocess-timeout-contract", "audit subprocess timeout did not produce one structured bounded failure")
        self.check("subprocess-timeout", "fail" if any(f["rule"] == "subprocess-timeout-contract" for f in self.findings) else "pass", {"default_seconds": DEFAULT_SUBPROCESS_TIMEOUT_SECONDS})

    def check_suite_version(self) -> None:
        version_path = self.root / "VERSION"
        version = version_path.read_text(encoding="utf-8").strip() if version_path.is_file() else ""
        if not SEMVER_RE.fullmatch(version):
            self.add("error", "suite-version", "skills/VERSION must contain one semantic version", self.rel(version_path), version)
        package_path = self.root.parent / "package.json"
        if package_path.is_file():
            try:
                package_version = str(json.loads(package_path.read_text(encoding="utf-8"))["version"])
            except Exception as exc:
                self.add("error", "suite-version", f"cannot read repository package version: {exc}", self.rel(package_path))
            else:
                if package_version != version:
                    self.add("error", "suite-version", "root package version and skills/VERSION differ", self.rel(version_path), {"package": package_version, "suite": version})
        self.check("suite-version", "fail" if any(f["rule"] == "suite-version" for f in self.findings) else "pass", {"version": version})

    def check_source_hygiene(self) -> None:
        required = [
            "README.md",
            "VERSION",
            "requirements-audit.txt",
            "contracts/ai-coding-os-suite-contracts/SKILL.md",
            "contracts/ai-coding-os-suite-contracts/references/semantic-vocabulary.yaml",
            "contracts/ai-coding-os-suite-contracts/references/proof/proof-surface.schema.json",
            "contracts/ai-coding-os-suite-contracts/references/evidence/evidence-envelope.schema.json",
            "contracts/ai-coding-os-suite-contracts/references/evals/skill-evals.schema.json",
            "router/ai-coding-os/SKILL.md",
            "architecture/evolvable-application-architecture/SKILL.md",
            "architecture/architecture-decision-system/SKILL.md",
            "meta/skill-evaluation-system/SKILL.md",
            "meta/ai-coding-os-evolution/SKILL.md",
            "preset/evolvable-application-preset/SKILL.md",
            "preset/evolvable-application-preset/profiles/application-core/profile.yaml",
            "preset/evolvable-application-preset/profiles/rust/profile.yaml",
            "tooling/effect-api-app-kit/SKILL.md",
        ]
        for rel in required:
            if not (self.root / rel).is_file():
                self.add("error", "source-hygiene", f"required grouped source file missing: {rel}", rel)
        audit_requirements = self.root / "requirements-audit.txt"
        if audit_requirements.is_file():
            requirement_lines = [line.strip() for line in audit_requirements.read_text(encoding="utf-8").splitlines() if line.strip() and not line.lstrip().startswith("#")]
            if not requirement_lines or any("==" not in line or line.startswith(("-", "http:", "https:")) for line in requirement_lines):
                self.add("error", "source-pin", "bundle-local audit dependencies must use exact package pins", self.rel(audit_requirements), requirement_lines)
        if (self.root / "architecture/effect-best-practices/package.json").is_file():
            pkg = json.loads((self.root / "architecture/effect-best-practices/package.json").read_text(encoding="utf-8"))
            ts = ((pkg.get("devDependencies") or {}).get("typescript"))
            if ts and any(ts.startswith(prefix) for prefix in ("^", "~", ">", "<", "*")):
                self.add("error", "source-pin", "fixture TypeScript dependency is not exact", "architecture/effect-best-practices/package.json", ts)
        late_caches = [p for p in self.root.rglob("*") if p.name == "__pycache__" or p.suffix in {".pyc", ".pyo"}]
        for path in late_caches:
            self.add("error", "generated-cache", "audit subprocess created a release cache file", self.rel(path))
        for path in sorted(self.root.rglob("*")):
            if not path.is_file():
                continue
            if "__MACOSX" in path.parts or path.name.startswith("._") or path.name == ".DS_Store":
                self.add("error", "source-hygiene", "platform archive metadata must not enter canonical source", self.rel(path))
            if path.suffix.lower() in {".zip", ".tar", ".gz", ".tgz"}:
                self.add("error", "source-hygiene", "nested delivery archive must not enter canonical source", self.rel(path))
        failed = {"source-hygiene", "source-pin", "generated-cache"}
        self.check("source-hygiene", "pass" if not any(f["rule"] in failed for f in self.findings) else "fail")

    def execute(self) -> dict[str, Any]:
        skills = self.parse_skill_frontmatter()
        self.check_contract_owners(skills)
        self.check_data_files()
        self.check_schema_instances()
        self.check_evals(skills)
        self.check_markdown_links()
        self.check_skill_portability(skills)
        self.check_contract_snapshot()
        self.check_source_conventions(skills)
        self.check_python()
        self.check_preset()
        self.check_effect_kit()
        self.check_bundle_builder(skills)
        self.check_subprocess_timeout()
        self.check_suite_version()
        self.check_source_hygiene()
        summary = {
            "error": sum(f["severity"] == "error" for f in self.findings),
            "warn": sum(f["severity"] == "warn" for f in self.findings),
            "info": sum(f["severity"] == "info" for f in self.findings),
            "total": len(self.findings),
        }
        template_claim = (
            "generated-template typecheck against a minimal internal Effect type surface"
            if self.effect_template_typecheck == "pass"
            else "generated-template structure only; TypeScript template typecheck not run because no compiler was available"
        )
        return {
            "suite_root": str(self.root),
            "source_tree_sha256": self.tree_hash(self.root),
            "summary": summary,
            "checks": self.checks,
            "findings": self.findings,
            "claim_ceiling": f"offline grouped-source structure, portable Skill-local links, frontmatter/cross-Skill reference closure, Proof/Evidence/Harness/eval positive and targeted-negative schema cases, eval ID uniqueness and declared composition cases, source conventions, Preset candidate provenance/language-profile closure/golden/merge/upgrade integration, Docs audit, architecture checker, bounded subprocess handling, experimental Kit project-bound P3 Descriptor/command-timeout/atomicity/structured-rollback smoke tests, {template_claim}, and self-contained source-bound cross-path-deterministic Core ZIP/canonical-audit/manifest/review sidecars; no external execution-method state, model-run eval result, external network, exact installed Effect API, Descriptor semantic coverage, production runtime, or production behavior claimed",
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
