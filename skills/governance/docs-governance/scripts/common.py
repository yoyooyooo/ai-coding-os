#!/usr/bin/env python3
"""Small shared parsing/output helpers for the docs-governance scanners."""

from __future__ import annotations

import ast
import json
import re
from pathlib import Path
from typing import Any

FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|$)", re.DOTALL)
KEY_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):(?:[ \t]*(.*))?$")


def frontmatter_text(text: str) -> str | None:
    match = FRONTMATTER_RE.match(text)
    return match.group(1) if match else None


def _scalar(value: str) -> Any:
    value = value.strip()
    if value in {"", "~", "null", "Null", "NULL"}:
        return None if value else ""
    if value.lower() in {"true", "false"}:
        return value.lower() == "true"
    if (value.startswith("'") and value.endswith("'")) or (value.startswith('"') and value.endswith('"')):
        try:
            return ast.literal_eval(value)
        except (SyntaxError, ValueError):
            return value[1:-1]
    if value.startswith("[") and value.endswith("]"):
        try:
            decoded = json.loads(value)
            return decoded
        except json.JSONDecodeError:
            return value
    return value


def _fallback_frontmatter(body: str) -> dict[str, Any]:
    """Parse common scalar/list/block-string YAML when PyYAML is unavailable."""
    fields: dict[str, Any] = {}
    lines = body.splitlines()
    index = 0
    while index < len(lines):
        line = lines[index].rstrip()
        index += 1
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        match = KEY_RE.match(line)
        if not match:
            continue
        key, rest = match.group(1), match.group(2) or ""
        rest = rest.strip()
        if rest in {"|", "|-", "|+", ">", ">-", ">+"}:
            block: list[str] = []
            while index < len(lines):
                candidate = lines[index]
                if candidate.strip() and not candidate.startswith((" ", "\t")):
                    break
                block.append(candidate[2:] if candidate.startswith("  ") else candidate.lstrip() if candidate.strip() else "")
                index += 1
            value = "\n".join(block)
            if rest.startswith(">"):
                value = " ".join(part.strip() for part in block).strip()
            if not rest.endswith("+"):
                value = value.rstrip("\n")
            fields[key] = value
            continue
        if rest:
            fields[key] = _scalar(rest)
            continue
        values: list[Any] = []
        while index < len(lines):
            item = re.match(r"^\s*-\s*(.*?)\s*$", lines[index])
            if not item:
                break
            values.append(_scalar(item.group(1)))
            index += 1
        fields[key] = values
    return fields


def parse_frontmatter(text: str) -> dict[str, Any] | None:
    body = frontmatter_text(text)
    if body is None:
        return None
    try:
        import yaml  # type: ignore
    except ImportError:
        return _fallback_frontmatter(body)
    try:
        value = yaml.safe_load(body)
    except Exception:
        return _fallback_frontmatter(body)
    return value if isinstance(value, dict) else {}


def as_list(value: Any) -> list[str]:
    if value is None or value == "":
        return []
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    return [str(value).strip()]


def json_print(value: Any) -> None:
    print(json.dumps(value, ensure_ascii=False, indent=2))


def relative_path(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return path.as_posix()
