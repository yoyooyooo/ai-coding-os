#!/usr/bin/env python3
"""Conservative mechanical audit for product-definition artifacts.

The scanner is intentionally structure-neutral. It does not infer semantic authority,
approval, implementation, or delivery status. It checks only explicit identifiers,
explicit @ID references, obvious accepted-document placeholders, and local Markdown links.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, Sequence
from urllib.parse import unquote

TEXT_EXTENSIONS = {
    ".md",
    ".markdown",
    ".txt",
    ".csv",
    ".tsv",
    ".yaml",
    ".yml",
    ".json",
}

DEFAULT_EXCLUDED_DIRS = {
    ".git",
    ".hg",
    ".svn",
    ".idea",
    ".vscode",
    ".venv",
    "venv",
    "node_modules",
    "vendor",
    "dist",
    "build",
    "coverage",
    "__pycache__",
}

PREFIXES = (
    "SRC",
    "CLM",
    "ISSUE",
    "Q",
    "DEC",
    "PDR",
    "OBJ",
    "ACTOR",
    "WF",
    "STATE",
    "RULE",
    "REQ",
    "BR",
    "FR",
    "NFR",
    "METRIC",
    "AC",
    "UAT",
    "CHG",
)

ID_CORE = rf"(?:{'|'.join(PREFIXES)})(?:-[A-Z0-9][A-Z0-9_.]*)*-[0-9][A-Z0-9_.-]*"
ID_PATTERN = re.compile(rf"\b({ID_CORE})\b")
EXPLICIT_REFERENCE_PATTERN = re.compile(rf"@({ID_CORE})\b")

HEADING_DEFINITION = re.compile(rf"^\s{{0,3}}#{{1,6}}\s+({ID_CORE})(?:\s|:|—|–|-|$)")
TABLE_DEFINITION = re.compile(rf"^\s*\|\s*({ID_CORE})\s*\|")
BOLD_DEFINITION = re.compile(rf"^\s*(?:[-*+]\s+)?\*\*({ID_CORE})\*\*(?:\s|:|—|–|-|$)")
KEY_DEFINITION = re.compile(
    rf"^\s*(?:id|source_id|claim_id|issue_id|question_id|decision_id|object_id|"
    rf"workflow_id|state_id|rule_id|requirement_id|metric_id|scenario_id|change_id)"
    rf"\s*:\s*[\"']?({ID_CORE})[\"']?\s*,?\s*$",
    re.IGNORECASE,
)
JSON_KEY_DEFINITION = re.compile(
    rf"[\"'](?:id|source_id|claim_id|issue_id|question_id|decision_id|object_id|"
    rf"workflow_id|state_id|rule_id|requirement_id|metric_id|scenario_id|change_id)[\"']"
    rf"\s*:\s*[\"']({ID_CORE})[\"']",
    re.IGNORECASE,
)

MARKDOWN_LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
FRONTMATTER_STATUS_PATTERN = re.compile(r"^status\s*:\s*[\"']?([^\"'\n]+)", re.IGNORECASE | re.MULTILINE)
ACCEPTED_STATUS_TOKENS = {
    "accepted",
    "approved",
    "baselined",
    "baseline",
    "final",
    "current-binding",
    "current_binding",
}
PLACEHOLDER_PATTERNS = (
    re.compile(r"\bTBD\b", re.IGNORECASE),
    re.compile(r"\bTODO\b", re.IGNORECASE),
    re.compile(r"\bFIXME\b", re.IGNORECASE),
    re.compile(r"\?\?\?"),
    re.compile(r"\{\{[^{}]+\}\}"),
    re.compile(r"<\s*(?:replace[-_ ]?me|fill[-_ ]?me|owner|version|date|title|name)\s*>", re.IGNORECASE),
)


@dataclass(frozen=True)
class Location:
    path: str
    line: int


@dataclass(frozen=True)
class Finding:
    code: str
    severity: str
    message: str
    path: str | None = None
    line: int | None = None
    identifier: str | None = None


@dataclass
class ScanResult:
    root: str
    files_scanned: int
    definitions: dict[str, list[Location]]
    references: dict[str, list[Location]]
    findings: list[Finding]

    def to_jsonable(self) -> dict[str, object]:
        return {
            "root": self.root,
            "files_scanned": self.files_scanned,
            "definitions": {
                key: [asdict(location) for location in value]
                for key, value in sorted(self.definitions.items())
            },
            "references": {
                key: [asdict(location) for location in value]
                for key, value in sorted(self.references.items())
            },
            "findings": [asdict(finding) for finding in self.findings],
            "summary": summarize(self.findings),
        }


def summarize(findings: Sequence[Finding]) -> dict[str, int]:
    summary = {"blocker": 0, "warning": 0, "info": 0}
    for finding in findings:
        summary[finding.severity] = summary.get(finding.severity, 0) + 1
    return summary


def read_text(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        try:
            return path.read_text(encoding="utf-8-sig")
        except UnicodeDecodeError:
            return None
    except OSError:
        return None


def iter_text_files(root: Path, excluded_dirs: set[str]) -> Iterable[Path]:
    for current_root, dirs, files in os.walk(root):
        dirs[:] = sorted(directory for directory in dirs if directory not in excluded_dirs)
        current_path = Path(current_root)
        for file_name in sorted(files):
            path = current_path / file_name
            if path.suffix.lower() in TEXT_EXTENSIONS:
                yield path


def parse_frontmatter(text: str) -> str:
    if not text.startswith("---\n") and not text.startswith("---\r\n"):
        return ""
    lines = text.splitlines()
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            return "\n".join(lines[1:index])
    return ""


def accepted_status(text: str) -> bool:
    frontmatter = parse_frontmatter(text)
    if not frontmatter:
        return False
    match = FRONTMATTER_STATUS_PATTERN.search(frontmatter)
    if not match:
        return False
    raw = match.group(1).strip().lower()
    normalized = re.split(r"\s*[|,/]\s*", raw)[0].strip()
    return normalized in ACCEPTED_STATUS_TOKENS


def definition_ids_for_line(line: str) -> set[str]:
    definitions: set[str] = set()
    for pattern in (HEADING_DEFINITION, TABLE_DEFINITION, BOLD_DEFINITION, KEY_DEFINITION):
        match = pattern.search(line)
        if match:
            definitions.add(match.group(1))
    for match in JSON_KEY_DEFINITION.finditer(line):
        definitions.add(match.group(1))
    return definitions


def resolve_local_link(source: Path, raw_target: str, root: Path) -> tuple[Path | None, str | None]:
    target = raw_target.strip()
    if not target:
        return None, None
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1].strip()
    lower = target.lower()
    if lower.startswith(("http://", "https://", "mailto:", "tel:", "data:", "sandbox:", "file:")):
        return None, None
    if target.startswith("#"):
        return None, None

    target_without_fragment = target.split("#", 1)[0].split("?", 1)[0]
    if not target_without_fragment:
        return None, None

    decoded = unquote(target_without_fragment)
    candidate = (source.parent / decoded).resolve()
    try:
        candidate.relative_to(root.resolve())
    except ValueError:
        return candidate, "escapes scan root"
    return candidate, None


def scan(root: Path, excluded_dirs: set[str] | None = None) -> ScanResult:
    root = root.resolve()
    excluded = set(DEFAULT_EXCLUDED_DIRS)
    if excluded_dirs:
        excluded.update(excluded_dirs)

    definitions: dict[str, list[Location]] = {}
    references: dict[str, list[Location]] = {}
    findings: list[Finding] = []
    files_scanned = 0

    for path in iter_text_files(root, excluded):
        text = read_text(path)
        if text is None:
            continue
        files_scanned += 1
        relative = str(path.relative_to(root))
        lines = text.splitlines()

        # De-duplicate frontmatter + heading definitions inside the same artifact.
        artifact_definitions: dict[str, int] = {}
        for line_number, line in enumerate(lines, start=1):
            for identifier in definition_ids_for_line(line):
                artifact_definitions.setdefault(identifier, line_number)
            for match in EXPLICIT_REFERENCE_PATTERN.finditer(line):
                identifier = match.group(1)
                references.setdefault(identifier, []).append(Location(relative, line_number))

            if path.suffix.lower() in {".md", ".markdown"}:
                for match in MARKDOWN_LINK_PATTERN.finditer(line):
                    raw_target = match.group(1)
                    candidate, problem = resolve_local_link(path, raw_target, root)
                    if candidate is None:
                        continue
                    if problem:
                        findings.append(
                            Finding(
                                code="PD-LINK-ESCAPE",
                                severity="warning",
                                message=f"Local link {raw_target!r} {problem}.",
                                path=relative,
                                line=line_number,
                            )
                        )
                    elif not candidate.exists():
                        findings.append(
                            Finding(
                                code="PD-LINK-MISSING",
                                severity="blocker",
                                message=f"Local Markdown link target does not exist: {raw_target}",
                                path=relative,
                                line=line_number,
                            )
                        )

        for identifier, line_number in artifact_definitions.items():
            definitions.setdefault(identifier, []).append(Location(relative, line_number))

        if path.suffix.lower() in {".md", ".markdown"} and accepted_status(text):
            body_start = 0
            frontmatter = parse_frontmatter(text)
            if frontmatter:
                closing_marker = text.find("\n---", 4)
                if closing_marker >= 0:
                    body_start = closing_marker + 4
            body = text[body_start:]
            for pattern in PLACEHOLDER_PATTERNS:
                match = pattern.search(body)
                if match:
                    line_number = body[: match.start()].count("\n") + 1
                    if body_start:
                        line_number += text[:body_start].count("\n")
                    findings.append(
                        Finding(
                            code="PD-ACCEPTED-PLACEHOLDER",
                            severity="warning",
                            message=f"Accepted artifact contains an obvious placeholder: {match.group(0)!r}",
                            path=relative,
                            line=line_number,
                        )
                    )
                    break

    for identifier, locations in sorted(definitions.items()):
        distinct_paths = {location.path for location in locations}
        if len(distinct_paths) > 1:
            paths = ", ".join(sorted(distinct_paths))
            findings.append(
                Finding(
                    code="PD-ID-DUPLICATE",
                    severity="blocker",
                    message=f"Identifier is explicitly defined in multiple artifacts: {paths}",
                    identifier=identifier,
                )
            )

    for identifier, locations in sorted(references.items()):
        if identifier not in definitions:
            first = locations[0]
            findings.append(
                Finding(
                    code="PD-REF-UNRESOLVED",
                    severity="blocker",
                    message=f"Explicit reference @{identifier} has no scanned definition.",
                    path=first.path,
                    line=first.line,
                    identifier=identifier,
                )
            )

    findings.sort(key=lambda item: (item.severity != "blocker", item.code, item.path or "", item.line or 0))
    return ScanResult(
        root=str(root),
        files_scanned=files_scanned,
        definitions=definitions,
        references=references,
        findings=findings,
    )


def render_text(result: ScanResult) -> str:
    lines = [
        f"Product artifact audit: {result.root}",
        f"Files scanned: {result.files_scanned}",
    ]
    summary = summarize(result.findings)
    lines.append(
        "Findings: "
        + ", ".join(f"{name}={count}" for name, count in summary.items())
    )
    if not result.findings:
        lines.append("No mechanical findings.")
        return "\n".join(lines)

    for finding in result.findings:
        location = ""
        if finding.path:
            location = f" {finding.path}"
            if finding.line:
                location += f":{finding.line}"
        identifier = f" [{finding.identifier}]" if finding.identifier else ""
        lines.append(
            f"- {finding.severity.upper()} {finding.code}{identifier}{location}: {finding.message}"
        )
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True, type=Path, help="Repository or artifact root to scan")
    parser.add_argument(
        "--exclude",
        action="append",
        default=[],
        help="Additional directory name to exclude; may be repeated",
    )
    parser.add_argument("--json", action="store_true", dest="json_output", help="Emit JSON")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Return exit code 1 when blocker findings exist",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if not args.root.exists() or not args.root.is_dir():
        print(f"error: scan root is not a directory: {args.root}", file=sys.stderr)
        return 2

    result = scan(args.root, set(args.exclude))
    if args.json_output:
        print(json.dumps(result.to_jsonable(), ensure_ascii=False, indent=2))
    else:
        print(render_text(result))

    if args.strict and any(finding.severity == "blocker" for finding in result.findings):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
