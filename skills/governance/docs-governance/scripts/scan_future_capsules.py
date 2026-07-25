#!/usr/bin/env python3
"""Audit future routes and capability capsules without requiring a fixed shape."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

from common import json_print, parse_frontmatter, relative_path

SHADOW_LAYERS = {"ssot", "standards", "adr", "architecture", "product", "protocols", "design", "security", "api", "data"}
CURRENT_SCOPES = {"current", "current-authority", "current-fact", "current-binding", "active-authority"}
CURRENT_STATUSES = {"current", "current-fact", "current-binding", "active-authority"}


def _finding(rule: str, severity: str, path: Path, summary: str, fix: str, evidence: list[str] | None = None) -> dict:
    return {
        "id": f"{rule}::{path.as_posix()}",
        "severity": severity,
        "ruleId": rule,
        "path": str(path),
        "summary": summary,
        "evidence": evidence or [path.as_posix()],
        "fixHint": fix,
    }


def _authority_finding(path: Path, metadata: dict, root: Path) -> dict | None:
    scope = str(metadata.get("authority_scope") or "").strip().lower()
    status = str(metadata.get("status") or "").strip().lower()
    if scope in CURRENT_SCOPES or status in CURRENT_STATUSES:
        value = f"authority_scope={scope!r}" if scope in CURRENT_SCOPES else f"status={status!r}"
        return _finding(
            "FUTURE_ROUTE_CLAIMS_CURRENT_AUTHORITY", "blocker", path,
            f"future route declares current authority ({value})",
            "keep the route as future-candidate or accepted-target and promote current meaning into its owning layer",
            [relative_path(path, root), value],
        )
    return None


def scan(repo: Path) -> dict:
    root = repo.resolve()
    roadmap = root / "docs" / "roadmap"
    future = roadmap / "future"
    findings: list[dict] = []
    routes: list[dict] = []
    capsules: list[dict] = []

    if not roadmap.is_dir():
        return {
            "version": "v3",
            "scannedAt": datetime.now(timezone.utc).isoformat(),
            "repoRoot": str(root),
            "summary": {"blocker": 0, "warn": 0, "info": 0, "total": 0},
            "findings": [],
            "routes": [],
            "capsules": [],
            "skipped": True,
            "reason": "docs/roadmap does not exist; future routes are not required",
        }

    for path in sorted(p for p in roadmap.glob("*.md") if p.name.lower() not in {"readme.md", "_template.md", "template.md"}):
        metadata = parse_frontmatter(path.read_text(encoding="utf-8", errors="ignore")) or {}
        issue = _authority_finding(path, metadata, root)
        if issue:
            findings.append(issue)
        routes.append({
            "path": relative_path(path, root),
            "kind": "flat-route",
            "authorityScope": metadata.get("authority_scope"),
        })

    if not future.is_dir():
        counts = {"blocker": 0, "warn": 0, "info": 0}
        for item in findings:
            counts[item["severity"]] += 1
        counts["total"] = len(findings)
        return {
            "version": "v3",
            "scannedAt": datetime.now(timezone.utc).isoformat(),
            "repoRoot": str(root),
            "summary": counts,
            "findings": findings,
            "routes": routes,
            "capsules": capsules,
            "skipped": True,
            "reason": "docs/roadmap/future does not exist; flat Roadmap routes are sufficient",
        }

    index = future / "README.md"
    index_text = index.read_text(encoding="utf-8", errors="ignore") if index.is_file() else ""
    for child in sorted(p for p in future.iterdir() if p.is_dir() and not p.name.startswith(".")):
        if child.name.lower() in SHADOW_LAYERS:
            findings.append(_finding(
                "FUTURE_SHADOW_AUTHORITY_LAYER", "blocker", child,
                f"future route duplicates authority layer name: {child.name}",
                "replace the shadow layer with a capability-oriented route or capsule",
            ))
            continue

        markdown_files = sorted(p for p in child.rglob("*.md") if p.is_file())
        readme = child / "README.md"
        if not readme.is_file():
            if len(markdown_files) <= 1:
                findings.append(_finding(
                    "FUTURE_SINGLE_FILE_PARTITION", "info", child,
                    "future capability directory contains one file and no README route",
                    "flatten to docs/roadmap/<capability>.md unless a durable local boundary already exists",
                ))
            else:
                findings.append(_finding(
                    "FUTURE_CAPSULE_README_MISSING", "warn", child,
                    "future capability directory has multiple files but no README entry route",
                    "add a concise capsule README or flatten the route when the directory has not earned a boundary",
                ))
            continue

        metadata = parse_frontmatter(readme.read_text(encoding="utf-8", errors="ignore")) or {}
        issue = _authority_finding(readme, metadata, root)
        if issue:
            findings.append(issue)
        if index.is_file() and f"{child.name}/README.md" not in index_text:
            findings.append(_finding(
                "FUTURE_CAPSULE_NOT_INDEXED", "info", child,
                "future capability is not linked from the local future index",
                "link it when the index is the declared entry route; otherwise document the alternate route",
            ))
        capsules.append({
            "path": relative_path(readme, root),
            "authorityScope": metadata.get("authority_scope"),
            "nodeId": metadata.get("node_id"),
            "markdownFiles": len(markdown_files),
        })

    counts = {"blocker": 0, "warn": 0, "info": 0}
    for item in findings:
        counts[item["severity"]] += 1
    counts["total"] = len(findings)
    return {
        "version": "v3",
        "scannedAt": datetime.now(timezone.utc).isoformat(),
        "repoRoot": str(root),
        "summary": counts,
        "findings": findings,
        "routes": routes,
        "capsules": capsules,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit future routes and capability capsules")
    parser.add_argument("--repo", default=".", help="Repository root")
    args = parser.parse_args()
    report = scan(Path(args.repo))
    json_print(report)
    if report["summary"].get("blocker", 0):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
