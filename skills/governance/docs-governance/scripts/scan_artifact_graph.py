#!/usr/bin/env python3
"""Audit explicitly opted-in artifact graph metadata."""

from __future__ import annotations

import argparse
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

from common import as_list, json_print, parse_frontmatter, relative_path

GRAPH_CONFIG_NAMES = (
    ".docs-graph.yml",
    ".docs-graph.yaml",
    "docs/.artifact-graph.yml",
    "docs/.artifact-graph.yaml",
)
RELATION_KEYS = ("related_to", "supersedes", "source_material", "evidence")
# This is an optional navigation inventory, not an execution graph. Projects may
# declare a local vocabulary, but these values keep lifecycle semantics generic.
KNOWN_STATUS = {"candidate", "current", "future", "historical", "superseded", "retired"}


def _finding(rule: str, severity: str, path: Path, summary: str, evidence: list[str], fix: str) -> dict:
    return {
        "id": f"{rule}::{path.as_posix()}",
        "severity": severity,
        "ruleId": rule,
        "path": str(path),
        "summary": summary,
        "evidence": evidence,
        "fixHint": fix,
    }


def has_opt_in_metadata(repo: Path) -> bool:
    root = repo.resolve()
    if any((root / rel).is_file() for rel in GRAPH_CONFIG_NAMES):
        return True
    for base_name in ("docs", "specs"):
        base = root / base_name
        if not base.is_dir():
            continue
        for path in base.rglob("*.md"):
            metadata = parse_frontmatter(path.read_text(encoding="utf-8", errors="ignore"))
            if metadata and "node_id" in metadata:
                return True
    return False


def scan(repo: Path) -> dict:
    root = repo.resolve()
    nodes: dict[str, Path] = {}
    relations: dict[str, dict[str, list[str]]] = defaultdict(dict)
    findings: list[dict] = []
    scanned_files = 0

    for base_name in ("docs", "specs"):
        base = root / base_name
        if not base.is_dir():
            continue
        for path in sorted(base.rglob("*.md")):
            metadata = parse_frontmatter(path.read_text(encoding="utf-8", errors="ignore"))
            if not metadata or "node_id" not in metadata:
                continue
            scanned_files += 1
            node_id = str(metadata.get("node_id") or "").strip()
            if not node_id:
                findings.append(_finding(
                    "GRAPH_NODE_ID_EMPTY", "blocker", path,
                    "graph metadata declares an empty node_id",
                    [relative_path(path, root)],
                    "assign a unique graph identity or remove the opt-in graph metadata",
                ))
                continue
            if node_id in nodes:
                findings.append(_finding(
                    "GRAPH_NODE_ID_DUPLICATE", "blocker", path,
                    f"duplicate node_id: {node_id}",
                    [str(nodes[node_id]), str(path)],
                    "assign a unique graph identity or remove unnecessary graph metadata",
                ))
            else:
                nodes[node_id] = path
            status = str(metadata.get("status") or "").strip()
            if status and status not in KNOWN_STATUS:
                findings.append(_finding(
                    "GRAPH_STATUS_UNKNOWN", "info", path,
                    f"graph status is outside the generic vocabulary: {status}",
                    [status],
                    "declare the project-local extension or use the generic status vocabulary",
                ))
            for key in RELATION_KEYS:
                values = as_list(metadata.get(key))
                if values:
                    relations[node_id][key] = values

    for source, fields in relations.items():
        for key, values in fields.items():
            if key in {"source_material", "evidence"}:
                continue
            for target in values:
                if target not in nodes:
                    path = nodes.get(source, root)
                    findings.append(_finding(
                        "GRAPH_TARGET_MISSING", "warn", path,
                        f"graph relation points to unknown node_id: {target}",
                        [source, key, target],
                        "repair the relation, add the intended graph node, or use a direct file reference instead",
                    ))

    counts = {"blocker": 0, "warn": 0, "info": 0}
    for item in findings:
        counts[item["severity"]] = counts.get(item["severity"], 0) + 1
    counts["total"] = len(findings)
    return {
        "version": "v3",
        "scannedAt": datetime.now(timezone.utc).isoformat(),
        "repoRoot": str(root),
        "summary": counts,
        "nodeCount": len(nodes),
        "metadataFiles": scanned_files,
        "optIn": True,
        "findings": findings,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit explicitly opted-in artifact graph metadata")
    parser.add_argument("--repo", default=".", help="Repository root")
    args = parser.parse_args()
    report = scan(Path(args.repo))
    json_print(report)
    if report["summary"].get("blocker", 0):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
