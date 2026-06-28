#!/usr/bin/env python3
"""Audit explicit repository-path anchors written in Markdown code spans."""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path

PREFIXES = ("crates/", "apps/", "packages/", "bins/", "xtask/", "scripts/", "migrations/", "fixtures/", "schemas/", "proto/", "tests/")
CODE_RE = re.compile(r"`([^`\n]+)`")


def scan(repo: Path) -> dict:
    repo = repo.resolve()
    docs = repo / "docs"
    has_source = any((repo / prefix.rstrip("/")).exists() for prefix in PREFIXES)
    if not has_source:
        return {
            "version": "v1",
            "scannedAt": datetime.now(timezone.utc).isoformat(),
            "repoRoot": str(repo),
            "summary": {"blocker": 0, "warn": 0, "info": 0, "total": 0},
            "findings": [],
            "checkedAnchors": 0,
            "skipped": True,
            "reason": "no recognized source roots in the scanned repository",
        }
    findings: list[dict] = []
    checked = 0
    if docs.exists():
        for path in sorted(docs.rglob("*.md")):
            text = path.read_text(encoding="utf-8", errors="ignore")
            for raw in CODE_RE.findall(text):
                value = raw.strip().rstrip(".,;:")
                if not value.startswith(PREFIXES):
                    continue
                prefix = re.split(r"[\*\?\[]", value, maxsplit=1)[0].rstrip("/")
                if not prefix:
                    continue
                checked += 1
                target = repo / prefix
                if not target.exists():
                    rel = path.relative_to(repo).as_posix()
                    findings.append({
                        "id": f"DOCS_SOURCE_ANCHOR::{rel}::{value}",
                        "severity": "warn",
                        "ruleId": "DOCS_SOURCE_ANCHOR_MISSING",
                        "path": str(path),
                        "summary": f"documented repository path does not exist: {value}",
                        "evidence": [str(target)],
                        "fixHint": "repair the code anchor, label it as a future/example path, or remove the stale current claim",
                    })
    counts = {"blocker": 0, "warn": 0, "info": 0}
    for item in findings:
        counts[item["severity"]] = counts.get(item["severity"], 0) + 1
    counts["total"] = len(findings)
    return {
        "version": "v1",
        "scannedAt": datetime.now(timezone.utc).isoformat(),
        "repoRoot": str(repo),
        "checkedAnchors": checked,
        "summary": counts,
        "findings": findings,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit repository-path anchors in docs")
    parser.add_argument("--repo", default=".", help="Repository root")
    args = parser.parse_args()
    report = scan(Path(args.repo))
    print(json.dumps(report, ensure_ascii=True, indent=2))
    if report["summary"].get("blocker", 0):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
