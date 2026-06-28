#!/usr/bin/env python3
"""Audit relative Markdown links under docs/."""

from __future__ import annotations

import argparse
import json
import re
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path

LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")


def scan(repo: Path) -> dict:
    repo = repo.resolve()
    docs = repo / "docs"
    findings: list[dict] = []
    checked = 0
    if docs.exists():
        for path in sorted(docs.rglob("*.md")):
            text = path.read_text(encoding="utf-8", errors="ignore")
            for match in LINK_RE.finditer(text):
                raw = match.group(1).strip()
                # Ignore optional title and angle brackets.
                target = raw.split()[0].strip("<>") if raw else ""
                if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                target = urllib.parse.unquote(target.split("#", 1)[0])
                if not target:
                    continue
                checked += 1
                resolved = (path.parent / target).resolve()
                if not resolved.exists():
                    rel = path.relative_to(repo).as_posix()
                    findings.append({
                        "id": f"DOCS_LINK_MISSING::{rel}::{target}",
                        "severity": "warn",
                        "ruleId": "DOCS_RELATIVE_LINK_MISSING",
                        "path": str(path),
                        "summary": f"relative Markdown link target does not exist: {target}",
                        "evidence": [raw, str(resolved)],
                        "fixHint": "repair the link, restore the intended retained artifact, or remove the stale reference",
                    })
    counts = {"blocker": 0, "warn": 0, "info": 0}
    for item in findings:
        counts[item["severity"]] = counts.get(item["severity"], 0) + 1
    counts["total"] = len(findings)
    return {
        "version": "v1",
        "scannedAt": datetime.now(timezone.utc).isoformat(),
        "repoRoot": str(repo),
        "checkedRelativeLinks": checked,
        "summary": counts,
        "findings": findings,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit relative Markdown links under docs/")
    parser.add_argument("--repo", default=".", help="Repository root")
    args = parser.parse_args()
    report = scan(Path(args.repo))
    print(json.dumps(report, ensure_ascii=True, indent=2))
    if report["summary"].get("blocker", 0):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
