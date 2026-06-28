#!/usr/bin/env python3
"""Audit docs/roadmap/future capability capsules."""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path

SHADOW_LAYERS = {
    "ssot", "standards", "adr", "architecture", "product", "protocols",
    "design", "reports", "goal-proof", "api", "runbook", "security",
}
REQUIRED_FRONTMATTER = {
    "node_id", "artifact_type", "status", "authority_scope", "objective",
    "claim_limit", "evidence_contract", "next_action",
}
SECTION_GROUPS = {
    "Product Hypothesis": ("## Product Hypothesis", "## 产品假设"),
    "Candidate Capability Boundary": ("## Candidate Capability Boundary", "## 候选能力边界"),
    "Reusable Current Foundations": ("## Reusable Current Foundations", "## Current Foundations", "## 当前可复用基础"),
    "Current Non-authority": ("## Current Non-authority", "## Current Non-Authority", "## 当前非权威"),
    "Candidate Authority Model": ("## Candidate Authority Model", "## 候选权威模型"),
    "Candidate Architecture": ("## Candidate Architecture", "## 候选架构"),
    "Prerequisites": ("## Prerequisites", "## 前置条件"),
    "Promotion Gates": ("## Promotion Gates", "## 晋升门槛"),
    "First Falsifiable Proof": ("## First Falsifiable Proof", "## 首个可证伪证明"),
    "Forbidden Early Implementations": ("## Forbidden Early Implementations", "## 禁止提前实现"),
    "Promotion Targets": ("## Promotion Targets", "## 晋升目标"),
    "Sources And Evidence": ("## Sources And Evidence", "## Sources And Related Current Docs", "## 来源与证据"),
}


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}
    result: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line or line.startswith((" ", "\t", "#", "-")) or ":" not in line:
            continue
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip('"\'')
    return result


def finding(rule: str, severity: str, path: Path, summary: str, fix: str) -> dict:
    return {
        "id": f"{rule}::{path.as_posix()}",
        "severity": severity,
        "ruleId": rule,
        "path": str(path),
        "summary": summary,
        "evidence": [path.as_posix()],
        "fixHint": fix,
    }


def scan(repo: Path) -> dict:
    repo = repo.resolve()
    root = repo / "docs" / "roadmap" / "future"
    findings: list[dict] = []
    capsules: list[dict] = []
    if not root.exists():
        return {
            "version": "v1",
            "scannedAt": datetime.now(timezone.utc).isoformat(),
            "root": str(root),
            "summary": {"blocker": 0, "warn": 0, "info": 0, "total": 0},
            "findings": [],
            "capsules": [],
            "skipped": True,
            "reason": "docs/roadmap/future does not exist",
        }

    for required in (root / "README.md", root / "_template.md"):
        if not required.is_file():
            findings.append(finding(
                "FUTURE_CAPSULE_BASELINE_MISSING", "warn", required,
                f"missing future capsule baseline file: {required.name}",
                "add an index and reusable capsule template",
            ))

    children = sorted(p for p in root.iterdir() if p.is_dir() and not p.name.startswith("."))
    index_text = (root / "README.md").read_text(encoding="utf-8", errors="ignore") if (root / "README.md").is_file() else ""
    indexed_dirs = set(re.findall(r"\(([^)/#]+?)/README\.md(?:#[^)]+)?\)", index_text))
    node_ids: dict[str, Path] = {}
    for child in children:
        if child.name not in indexed_dirs:
            findings.append(finding(
                "FUTURE_CAPSULE_NOT_INDEXED", "warn", child,
                f"future capability capsule is not linked from roadmap/future/README.md: {child.name}",
                "add the capsule to the Future index or merge/delete the unreferenced duplicate",
            ))
        if child.name in SHADOW_LAYERS:
            findings.append(finding(
                "FUTURE_SHADOW_AUTHORITY_LAYER", "blocker", child,
                f"future capsule tree contains forbidden shadow layer: {child.name}",
                "replace the layer with capability-oriented future/<capability>/README.md capsules",
            ))
        readme = child / "README.md"
        if not readme.is_file():
            findings.append(finding(
                "FUTURE_CAPSULE_README_MISSING", "blocker", readme,
                f"future capability directory has no README: {child.name}",
                "add a README using templates/future-capability-capsule.md or delete the empty directory",
            ))
            continue
        text = readme.read_text(encoding="utf-8", errors="ignore")
        fm = parse_frontmatter(text)
        missing_fm = sorted(REQUIRED_FRONTMATTER - set(fm))
        if missing_fm:
            findings.append(finding(
                "FUTURE_CAPSULE_FRONTMATTER_MISSING", "warn", readme,
                "missing future capsule frontmatter: " + ", ".join(missing_fm),
                "add future-candidate frontmatter fields",
            ))
        if fm.get("authority_scope") not in {None, "future-candidate"}:
            findings.append(finding(
                "FUTURE_CAPSULE_AUTHORITY_SCOPE_INVALID", "blocker", readme,
                f"future capsule authority_scope is {fm.get('authority_scope')!r}",
                "set authority_scope: future-candidate; future capsules cannot be current authority",
            ))
        node_id = fm.get("node_id")
        if node_id:
            if node_id in node_ids:
                findings.append(finding(
                    "FUTURE_CAPSULE_NODE_ID_DUPLICATE", "blocker", readme,
                    f"duplicate future capsule node_id: {node_id}",
                    f"choose a unique node_id; first seen at {node_ids[node_id]}",
                ))
            else:
                node_ids[node_id] = readme
        missing_sections = [
            label for label, aliases in SECTION_GROUPS.items()
            if not any(alias.lower() in text.lower() for alias in aliases)
        ]
        if missing_sections:
            findings.append(finding(
                "FUTURE_CAPSULE_SECTIONS_MISSING", "warn", readme,
                "missing future capsule sections: " + ", ".join(missing_sections),
                "answer every governance question or explicitly merge equivalent sections",
            ))
        capsules.append({
            "path": str(readme.relative_to(repo)),
            "nodeId": node_id,
            "authorityScope": fm.get("authority_scope"),
            "missingFrontmatter": missing_fm,
            "missingSections": missing_sections,
        })

    counts = {"blocker": 0, "warn": 0, "info": 0}
    for item in findings:
        counts[item["severity"]] = counts.get(item["severity"], 0) + 1
    counts["total"] = len(findings)
    return {
        "version": "v1",
        "scannedAt": datetime.now(timezone.utc).isoformat(),
        "root": str(root),
        "summary": counts,
        "findings": findings,
        "capsules": capsules,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit docs/roadmap/future capability capsules")
    parser.add_argument("--repo", default=".", help="Repository root")
    args = parser.parse_args()
    report = scan(Path(args.repo))
    print(json.dumps(report, ensure_ascii=True, indent=2))
    if report["summary"].get("blocker", 0):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
