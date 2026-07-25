#!/usr/bin/env python3
"""Self-check the product-definition Skill package using the standard library only."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = {
    "SKILL.md",
    "README.md",
    "CHANGELOG.md",
    "VERSION",
    "agents/openai.yaml",
    "evals/evals.json",
    "references/artifact-selection-and-readiness.md",
    "references/source-to-product-truth.md",
    "references/scope-and-version-baselines.md",
    "references/product-modeling.md",
    "references/workflow-and-exception-modeling.md",
    "references/rules-permissions-metrics-quality.md",
    "references/challenge-and-decide.md",
    "references/alignment-and-facilitation.md",
    "references/prd-and-acceptance.md",
    "references/traceability-and-change-impact.md",
    "references/product-technical-boundary.md",
    "templates/README.md",
    "templates/product-brief.md",
    "templates/source-synthesis.md",
    "templates/scope-baseline.md",
    "templates/clarification-register.md",
    "templates/decision-packet.md",
    "templates/product-decision-record.md",
    "templates/product-model.md",
    "templates/workflow-specification.md",
    "templates/state-machine.md",
    "templates/business-rule-catalog.md",
    "templates/raci-permission-matrix.md",
    "templates/metric-dictionary.md",
    "templates/quality-attribute-requirements.md",
    "templates/module-prd.md",
    "templates/design-handoff.md",
    "templates/acceptance-criteria.md",
    "templates/uat-scenario.md",
    "templates/requirements-traceability-matrix.md",
    "templates/change-impact-assessment.md",
    "templates/alignment-meeting-pack.md",
    "scripts/scan_product_artifacts.py",
}

MARKDOWN_LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def check_required_files(errors: list[str]) -> None:
    for relative in sorted(REQUIRED_FILES):
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    lines = text.splitlines()
    result: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip()
    return result


def check_skill_metadata(errors: list[str]) -> None:
    text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    metadata = parse_frontmatter(text)
    if metadata.get("name") != "product-definition":
        errors.append("SKILL.md frontmatter name must be product-definition")
    if not metadata.get("description"):
        errors.append("SKILL.md frontmatter description is missing")

    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    if not re.fullmatch(r"\d+\.\d+\.\d+(?:[-+][A-Za-z0-9.-]+)?", version):
        errors.append(f"VERSION is not semantic-version-like: {version!r}")

    agent = (ROOT / "agents/openai.yaml").read_text(encoding="utf-8")
    for token in ("display_name:", "short_description:", "default_prompt:"):
        if token not in agent:
            errors.append(f"agents/openai.yaml missing {token}")


def check_evals(errors: list[str]) -> None:
    try:
        data = json.loads((ROOT / "evals/evals.json").read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"evals/evals.json is invalid JSON: {exc}")
        return
    if not isinstance(data, dict) or data.get("schema_version") != 1 or data.get("skill_name") != "product-definition":
        errors.append("evals/evals.json must use schema_version 1 and skill_name product-definition")
        return
    evals = data.get("evals")
    if not isinstance(evals, list) or not evals:
        errors.append("evals/evals.json must contain a non-empty evals list")
        return
    seen: set[str] = set()
    for index, item in enumerate(evals):
        if not isinstance(item, dict):
            errors.append(f"eval item {index} is not an object")
            continue
        identifier = item.get("id")
        if not identifier:
            errors.append(f"eval item {index} has no id")
        elif identifier in seen:
            errors.append(f"duplicate eval id: {identifier}")
        else:
            seen.add(identifier)
        if not item.get("prompt") or not item.get("expected_output"):
            errors.append(f"eval {identifier or index} must have prompt and expected_output")


def resolve_link(source: Path, target: str) -> Path | None:
    value = target.strip()
    if value.startswith("<") and value.endswith(">"):
        value = value[1:-1].strip()
    lower = value.lower()
    if not value or value.startswith("#") or lower.startswith(
        ("http://", "https://", "mailto:", "tel:", "data:", "sandbox:", "file:")
    ):
        return None
    value = value.split("#", 1)[0].split("?", 1)[0]
    if not value:
        return None
    return (source.parent / unquote(value)).resolve()


def check_markdown_links(errors: list[str]) -> None:
    for path in sorted(ROOT.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        for line_number, line in enumerate(text.splitlines(), start=1):
            for match in MARKDOWN_LINK_PATTERN.finditer(line):
                target = resolve_link(path, match.group(1))
                if target is None:
                    continue
                try:
                    target.relative_to(ROOT)
                except ValueError:
                    errors.append(
                        f"local Markdown link escapes package: {path.relative_to(ROOT)}:{line_number} -> {match.group(1)}"
                    )
                    continue
                if not target.exists():
                    errors.append(
                        f"missing local Markdown link: {path.relative_to(ROOT)}:{line_number} -> {match.group(1)}"
                    )


def check_python_compilation(errors: list[str]) -> None:
    for path in sorted((ROOT / "scripts").glob("*.py")):
        try:
            compile(path.read_text(encoding="utf-8"), str(path), "exec")
        except SyntaxError as exc:
            errors.append(f"Python syntax error in {path.relative_to(ROOT)}: {exc}")
    for path in sorted((ROOT / "tests").glob("*.py")):
        try:
            compile(path.read_text(encoding="utf-8"), str(path), "exec")
        except SyntaxError as exc:
            errors.append(f"Python syntax error in {path.relative_to(ROOT)}: {exc}")


def main() -> int:
    errors: list[str] = []
    check_required_files(errors)
    if not errors:
        check_skill_metadata(errors)
        check_evals(errors)
        check_markdown_links(errors)
        check_python_compilation(errors)

    if errors:
        print("product-definition self-check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("product-definition self-check passed")
    print(f"root: {ROOT}")
    print(f"version: {(ROOT / 'VERSION').read_text(encoding='utf-8').strip()}")
    print(f"required files: {len(REQUIRED_FILES)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
