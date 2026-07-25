#!/usr/bin/env python3
"""Optional multi-entry discovery heuristics for repositories with documentation."""
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path

MD_LINK_RE = re.compile(r"!?\[[^\]]*\]\((?:<([^>]+)>|([^\s)]+))")
ROUTE_HEADINGS = (
    "Discovery Surfaces",
    "Discovery Routes",
    "Authority Routes",
    "Routes",
    "Entry Points",
    "Homes",
    "入口",
    "路由",
    # Reader compatibility for existing repositories; new writers prefer Routes.
    "Read Next",
    "下一步阅读",
    "Read First",
    "最短阅读路径",
)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.is_file() else ""


def contains_route_heading(text: str) -> bool:
    lowered = text.lower()
    return any(f"## {heading}".lower() in lowered for heading in ROUTE_HEADINGS)


def markdown_files(root: Path) -> list[Path]:
    return sorted(path for path in root.rglob("*.md") if path.is_file()) if root.is_dir() else []


def resolve_targets(path: Path) -> set[Path]:
    targets: set[Path] = set()
    for first, second in MD_LINK_RE.findall(read(path)):
        raw = first or second
        target = raw.split("#", 1)[0]
        if not target or "://" in target or target.startswith("#"):
            continue
        candidate = (path.parent / target).resolve()
        if candidate.is_dir():
            for name in ("README.md", "readme.md"):
                if (candidate / name).is_file():
                    candidate = (candidate / name).resolve()
                    break
        if candidate.exists():
            targets.add(candidate)
    return targets


def finding(rule_id: str, severity: str, path: Path, summary: str, evidence: list[str], fix: str) -> dict:
    return {
        "id": f"{rule_id}::{path.as_posix()}",
        "severity": severity,
        "ruleId": rule_id,
        "path": str(path),
        "summary": summary,
        "evidence": evidence,
        "fixHint": fix,
    }


def scan(repo: Path) -> dict:
    root = repo.resolve()
    docs = root / "docs"
    findings: list[dict] = []
    if not docs.is_dir():
        return {
            "version": "v3",
            "scannedAt": datetime.now(timezone.utc).isoformat(),
            "repoRoot": str(root),
            "findings": [],
            "skipped": True,
            "reason": "docs/ does not exist",
        }

    router = docs / "README.md"
    if router.is_file() and not contains_route_heading(read(router)):
        findings.append(finding(
            "DOCS_DISCOVERY_SURFACES_MISSING", "info", router,
            "docs router exposes no explicit discovery surfaces or routes",
            ["docs/README.md"],
            "add concise links by question, authority, code area, or artifact without prescribing a reading order",
        ))

    if router.is_file():
        linked = resolve_targets(router)
        for child in sorted(path for path in docs.iterdir() if path.is_dir() and not path.name.startswith(".")):
            child_router = next((child / name for name in ("README.md", "readme.md") if (child / name).is_file()), None)
            if child_router and child_router.resolve() not in linked:
                findings.append(finding(
                    "DOCS_ROUTER_LAYER_LINK_MISSING", "info", router,
                    f"docs router does not link an existing layer router: {child.name}",
                    [str(child_router.relative_to(root))],
                    "link the layer when it is an intended discovery surface; no ordering is required",
                ))

    for path in markdown_files(docs):
        if path.name.lower() != "readme.md" or path == router:
            continue
        if not contains_route_heading(read(path)):
            findings.append(finding(
                "DOCS_LOCAL_ROUTES_MISSING", "info", path,
                "local docs router exposes no explicit neighboring routes",
                [str(path.relative_to(root))],
                "add only relevant Authority, Evidence, source, or neighboring links without copying parent prose",
            ))

    return {
        "version": "v3",
        "scannedAt": datetime.now(timezone.utc).isoformat(),
        "repoRoot": str(root),
        "findings": findings,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Scan optional docs discovery-route heuristics")
    parser.add_argument("--repo", default=".", help="Repository root")
    args = parser.parse_args()
    print(json.dumps(scan(Path(args.repo)), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
