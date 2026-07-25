#!/usr/bin/env python3
"""Self-check the independent Goal Proof experiment Skill."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

try:
    import jsonschema
    import yaml
except ImportError as exc:  # pragma: no cover
    raise SystemExit("PyYAML and jsonschema are required") from exc

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skill"
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def load_instance(path: Path) -> Any:
    text = path.read_text(encoding="utf-8")
    return json.loads(text) if path.suffix == ".json" else yaml.safe_load(text)


def validate(schema_name: str, instance_path: Path) -> None:
    schema_path = SKILL / "schemas" / schema_name
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    jsonschema.Draft202012Validator.check_schema(schema)
    jsonschema.Draft202012Validator(schema).validate(load_instance(instance_path))


def check_evals(errors: list[str]) -> int:
    path = SKILL / "evals/evals.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"eval parse failed: {exc}")
        return 0
    if data.get("schema_version") != 1 or data.get("skill_name") != "goal-proof":
        errors.append("eval root must use schema_version 1 and skill_name goal-proof")
    cases = data.get("evals")
    if not isinstance(cases, list) or not cases:
        errors.append("evals must be a non-empty list")
        return 0
    ids: set[str] = set()
    for index, case in enumerate(cases, start=1):
        if not isinstance(case, dict):
            errors.append(f"eval {index} is not an object")
            continue
        case_id = str(case.get("id", ""))
        if not case_id or case_id in ids:
            errors.append(f"eval id is missing or duplicated: {case_id!r}")
        ids.add(case_id)
        for field in ("prompt", "expected_output"):
            if not isinstance(case.get(field), str) or not case[field].strip():
                errors.append(f"eval {case_id} has no {field}")
        expectations = case.get("expectations", [])
        if not isinstance(expectations, list) or len(expectations) < 2 or any(not isinstance(item, str) or not item for item in expectations):
            errors.append(f"eval {case_id} needs at least two valid expectations")
    return len(cases)


def check_links(errors: list[str]) -> int:
    checked = 0
    for path in sorted(SKILL.rglob("*.md")):
        for raw in LINK_RE.findall(path.read_text(encoding="utf-8", errors="replace")):
            target = raw.strip().split(" ", 1)[0].strip("<>").split("#", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            checked += 1
            candidate = (path.parent / target).resolve()
            if not candidate.exists():
                errors.append(f"broken Skill-local link: {path.relative_to(SKILL)} -> {raw}")
                continue
            try:
                candidate.relative_to(SKILL.resolve())
            except ValueError:
                errors.append(f"link escapes independent Skill root: {path.relative_to(SKILL)} -> {raw}")
    return checked


def main() -> None:
    errors: list[str] = []
    text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        errors.append("SKILL.md frontmatter is missing")
    else:
        data = yaml.safe_load(match.group(1)) or {}
        if data.get("name") != "goal-proof":
            errors.append("Skill name must remain goal-proof")
        if data.get("disable-model-invocation") is not True:
            errors.append("experimental Goal Proof must be user-invoked")
        if not isinstance(data.get("description"), str) or not data["description"].strip():
            errors.append("human-facing description is missing")
        extra = sorted(set(data) - {"name", "description", "disable-model-invocation"})
        if extra:
            errors.append(f"nonessential frontmatter fields: {extra}")

    for schema_name, instance in (
        ("goal.schema.json", SKILL / "templates/goal.yaml"),
        ("progress.schema.json", SKILL / "templates/progress.yaml"),
    ):
        try:
            validate(schema_name, instance)
        except Exception as exc:
            errors.append(f"{instance.name} failed {schema_name}: {exc}")

    evidence_schema = json.loads((SKILL / "schemas/evidence-record.schema.json").read_text(encoding="utf-8"))
    evidence_lines = [line for line in (SKILL / "templates/evidence.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
    for index, line in enumerate(evidence_lines, start=1):
        try:
            jsonschema.Draft202012Validator(evidence_schema).validate(json.loads(line))
        except Exception as exc:
            errors.append(f"evidence template line {index} failed schema: {exc}")

    eval_count = check_evals(errors)
    link_count = check_links(errors)
    retired = {"goal-contracts", "finding-proof-step", "proof-step-implementation", "write-work-plans"}
    public_skill_refs = set(re.findall(r"\$([a-z][a-z0-9-]+)", text))
    leaked = sorted(public_skill_refs & retired)
    if leaked:
        errors.append(f"retired public phase Skill references remain: {leaked}")

    report = {
        "experiment": str(ROOT),
        "summary": {"error": len(errors), "total": len(errors)},
        "checks": {
            "skill": "pass" if not errors else "fail",
            "eval_cases": eval_count,
            "skill_local_links": link_count,
            "schema_instances": 2 + len(evidence_lines),
        },
        "errors": errors,
        "claim_ceiling": "Skill-local structure, user invocation, eval shape, links, and Goal/Progress/Evidence template schema compatibility; no model-run quality or production behavior claimed",
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    raise SystemExit(1 if errors else 0)


if __name__ == "__main__":
    main()
