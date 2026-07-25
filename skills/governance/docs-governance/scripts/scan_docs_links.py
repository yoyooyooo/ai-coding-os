#!/usr/bin/env python3
"""Audit Markdown links, images, anchors, directories, and repository boundaries."""

from __future__ import annotations

import argparse
import re
import unicodedata
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path

from common import json_print, relative_path

LINK_START_RE = re.compile(r"!?\[[^\]]*\]\(")
HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$", re.MULTILINE)
HTML_ANCHOR_RE = re.compile(r"<(?:a|span)\b[^>]*\bid=[\"']([^\"']+)[\"']", re.IGNORECASE)
EXPLICIT_ANCHOR_RE = re.compile(r"\{#([^}]+)\}")
IGNORED_SCHEMES = {"http", "https", "mailto", "tel", "data", "ftp"}
README_NAMES = ("README.md", "readme.md")


def _extract_links(text: str) -> list[tuple[str, bool]]:
    """Extract destinations without treating parentheses in a path as the end."""
    links: list[tuple[str, bool]] = []
    for match in LINK_START_RE.finditer(text):
        index = match.end()
        while index < len(text) and text[index].isspace():
            index += 1
        is_image = text[match.start()] == "!"
        if index >= len(text):
            continue
        if text[index] == "<":
            end = text.find(">", index + 1)
            if end < 0:
                continue
            links.append((text[index + 1 : end], is_image))
            continue
        start = index
        depth = 0
        while index < len(text):
            char = text[index]
            if char == "(":
                depth += 1
            elif char == ")":
                if depth == 0:
                    break
                depth -= 1
            elif char.isspace() and depth == 0:
                break
            index += 1
        if start < index:
            links.append((text[start:index], is_image))
    return links


def _slug(value: str) -> str:
    value = re.sub(r"<[^>]+>", "", value)
    value = re.sub(r"`([^`]*)`", r"\1", value)
    value = re.sub(r"\s*\{#([^}]+)\}\s*$", "", value)
    value = value.strip().lower()
    value = "".join(char for char in value if unicodedata.category(char)[0] != "P" or char in "-_ ")
    return re.sub(r"\s+", "-", value)


def _anchors(path: Path) -> set[str]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    values = set(HTML_ANCHOR_RE.findall(text))
    values.update(EXPLICIT_ANCHOR_RE.findall(text))
    values.update(_slug(heading) for heading in HEADING_RE.findall(text))
    return {value for value in values if value}


def _link_destination(raw: str) -> tuple[str, str]:
    raw = raw.strip()
    if raw.startswith("<") and ">" in raw:
        raw = raw[1 : raw.index(">")]
    path, separator, fragment = raw.partition("#")
    return urllib.parse.unquote(path), urllib.parse.unquote(fragment) if separator else ""


def _inside(path: Path, root: Path) -> bool:
    try:
        path.resolve().relative_to(root.resolve())
        return True
    except ValueError:
        return False


def _finding(rule: str, severity: str, source: Path, root: Path, summary: str, evidence: list[str], fix: str) -> dict:
    return {
        "id": f"{rule}::{relative_path(source, root)}::{summary}",
        "severity": severity,
        "ruleId": rule,
        "path": str(source),
        "summary": summary,
        "evidence": evidence,
        "fixHint": fix,
    }


def scan(repo: Path) -> dict:
    root = repo.resolve()
    docs = root / "docs"
    findings: list[dict] = []
    checked = 0
    if docs.is_dir():
        for source in sorted(docs.rglob("*.md")):
            for raw, is_image in _extract_links(source.read_text(encoding="utf-8", errors="ignore")):
                destination, fragment = _link_destination(raw)
                if not destination and not fragment:
                    continue
                parsed = urllib.parse.urlsplit(destination)
                if parsed.scheme.lower() in IGNORED_SCHEMES or destination.startswith("//"):
                    continue
                if not destination:
                    resolved = source.resolve()
                elif destination.startswith("/"):
                    resolved = (root / destination.lstrip("/")).resolve()
                else:
                    resolved = (source.parent / destination).resolve()
                checked += 1
                if not _inside(resolved, root):
                    findings.append(_finding(
                        "DOCS_LINK_ROOT_ESCAPE", "blocker", source, root,
                        f"relative link resolves outside repository: {destination or '#'+fragment}",
                        [raw, str(resolved)],
                        "use an in-repository target or an explicit external URL",
                    ))
                    continue
                target = resolved
                if target.is_dir():
                    readme = next((target / name for name in README_NAMES if (target / name).is_file()), None)
                    if readme is None:
                        findings.append(_finding(
                            "DOCS_DIRECTORY_LINK_README_MISSING", "warn", source, root,
                            f"directory link has no README target: {destination}",
                            [raw, str(target)],
                            "link to the intended document or add a README only when the directory is a durable route",
                        ))
                        continue
                    target = readme.resolve()
                if not target.exists():
                    findings.append(_finding(
                        "DOCS_RELATIVE_LINK_MISSING", "warn", source, root,
                        f"relative {'image ' if is_image else ''}link target does not exist: {destination}",
                        [raw, str(target)],
                        "repair the link, restore the retained artifact, or remove the stale route",
                    ))
                    continue
                anchor_values = _anchors(target) if fragment and target.is_file() else set()
                if fragment and target.is_file() and fragment not in anchor_values and fragment.lower() not in anchor_values and _slug(fragment) not in anchor_values:
                    findings.append(_finding(
                        "DOCS_LINK_ANCHOR_MISSING", "warn", source, root,
                        f"link anchor does not exist: #{fragment}",
                        [raw, str(target)],
                        "repair the anchor or remove the stale fragment",
                    ))

    counts = {"blocker": 0, "warn": 0, "info": 0}
    for item in findings:
        counts[item["severity"]] += 1
    counts["total"] = len(findings)
    return {
        "version": "v3",
        "scannedAt": datetime.now(timezone.utc).isoformat(),
        "repoRoot": str(root),
        "checkedRelativeLinks": checked,
        "summary": counts,
        "findings": findings,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit Markdown links under docs/")
    parser.add_argument("--repo", default=".", help="Repository root")
    args = parser.parse_args()
    report = scan(Path(args.repo))
    json_print(report)
    if report["summary"].get("blocker", 0):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
