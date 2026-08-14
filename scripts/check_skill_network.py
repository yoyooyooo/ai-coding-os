#!/usr/bin/env python3
"""Integrity checks for the AI Coding OS Skill network and project routes."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

SHARED_CORE_SKILLS = {
    "ai-coding-os",
    "product-definition",
    "docs-governance",
    "evolvable-application-architecture",
    "frontend-architecture",
    "effect-best-practices",
    "product-harness-system",
    "ai-coding-os-evolution",
}
SUPPORTING_SKILLS = {"effect-server-module-design"}
EXPECTED_SKILLS = SHARED_CORE_SKILLS | SUPPORTING_SKILLS
EXPECTED_VISIBLE = (
    SHARED_CORE_SKILLS - {"ai-coding-os", "ai-coding-os-evolution"}
) | SUPPORTING_SKILLS
SUPPORTED_FRONTMATTER_FIELDS = {"name", "description", "disable-model-invocation"}
EXPECTED_NETWORK_ANCHORS = (
    "Project Authority First.",
    "Source Is Not Decision.",
    "Evidence Bounds Claims.",
    "Route Is an Edge, Not a Sequence.",
    "Local Agency, Bounded Authority.",
    "No Silent Material Assumption.",
    "Strong Invariants, Weak Choreography.",
    "Minimal Context, Maximal Legibility.",
    "Shape Must Be Earned.",
    "Portable Defaults Standardize the Boring Choices.",
    "The Project Should Explain Itself.",
    "Feedback Horizon Sets the Safe Step Size.",
    "Preserve Semantics; Re-earn Scaffolding and Conventions.",
)
JUNK_NAMES = {".DS_Store", "Thumbs.db"}
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
SKILL_REF_RE = re.compile(r"\$([a-z][a-z0-9-]+)")
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
FRONTMATTER_KEY_RE = re.compile(r"(?m)^([a-z][a-z0-9-]*):")
CJK_RE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]")
AGENT_ROUTE_RE = re.compile(r"`((?:docs|skills)/[^`]+)`")


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def frontmatter_value(frontmatter: str, key: str) -> str | None:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*(.+?)\s*$", frontmatter)
    return match.group(1).strip().strip('"\'') if match else None


def relative_link_target(raw: str) -> str | None:
    target = raw.strip().split(" ", 1)[0].strip("<>").split("#", 1)[0].split("?", 1)[0]
    if not target or target.startswith(("http://", "https://", "mailto:", "data:", "/")):
        return None
    if any(marker in target for marker in ("<", ">", "${", "{{")):
        return None
    return target


def check(root: Path) -> list[str]:
    errors: list[str] = []
    root = root.resolve()
    repo_root = root.parent

    for path in root.rglob("*"):
        if path.is_symlink():
            fail(errors, f"symlink is not allowed: {path.relative_to(root)}")
        if path.name in JUNK_NAMES or path.name.startswith("._"):
            fail(errors, f"junk file: {path.relative_to(root)}")
        if path.is_dir() and path.name == "__pycache__":
            fail(errors, f"cache directory: {path.relative_to(root)}")
        if path.is_file() and path.suffix in {".pyc", ".pyo"}:
            fail(errors, f"cache file: {path.relative_to(root)}")

    skills: dict[str, Path] = {}
    visible: set[str] = set()
    for skill_file in sorted(root.rglob("SKILL.md")):
        text = skill_file.read_text(encoding="utf-8")
        match = FRONTMATTER_RE.match(text)
        if not match:
            fail(errors, f"missing frontmatter: {skill_file.relative_to(root)}")
            continue
        frontmatter = match.group(1)
        unsupported = set(FRONTMATTER_KEY_RE.findall(frontmatter)) - SUPPORTED_FRONTMATTER_FIELDS
        if unsupported:
            fail(errors, f"unsupported frontmatter fields {sorted(unsupported)}: {skill_file.relative_to(root)}")
        name = frontmatter_value(frontmatter, "name")
        description = frontmatter_value(frontmatter, "description")
        disabled = frontmatter_value(frontmatter, "disable-model-invocation")
        if not name:
            fail(errors, f"missing name: {skill_file.relative_to(root)}")
            continue
        if not description:
            fail(errors, f"missing description: {skill_file.relative_to(root)}")
        if name in SHARED_CORE_SKILLS and "## Semantic anchors" not in text:
            fail(errors, f"missing Semantic anchors: {skill_file.relative_to(root)}")
        if name in SUPPORTING_SKILLS:
            for required_heading in ("## Authority", "## Run"):
                if required_heading not in text:
                    fail(
                        errors,
                        f"missing supporting Skill heading {required_heading}: {skill_file.relative_to(root)}",
                    )
        if CJK_RE.search(text):
            fail(errors, f"non-English canonical Skill prose: {skill_file.relative_to(root)}")
        if name in skills:
            fail(errors, f"duplicate Skill name {name}: {skill_file} and {skills[name]}")
        skills[name] = skill_file
        if skill_file.parent.name != name:
            fail(errors, f"Skill name/path mismatch: {name} at {skill_file.relative_to(root)}")
        if disabled not in {None, "true"}:
            fail(errors, f"invalid disable-model-invocation for {name}: {disabled}")
        if disabled != "true":
            visible.add(name)

    names = set(skills)
    if names != EXPECTED_SKILLS:
        fail(errors, f"Skill roster mismatch: expected={sorted(EXPECTED_SKILLS)} actual={sorted(names)}")
    if visible != EXPECTED_VISIBLE:
        fail(errors, f"visible Skill mismatch: expected={sorted(EXPECTED_VISIBLE)} actual={sorted(visible)}")

    incoming: dict[Path, set[Path]] = {}
    for markdown in sorted(root.rglob("*.md")):
        text = markdown.read_text(encoding="utf-8")
        if CJK_RE.search(text):
            fail(errors, f"non-English canonical Skill prose: {markdown.relative_to(root)}")
        skill_root = next((parent for parent in [markdown.parent, *markdown.parents] if (parent / "SKILL.md").is_file()), None)
        for raw in LINK_RE.findall(text):
            target = relative_link_target(raw)
            if target is None:
                continue
            resolved = (markdown.parent / target).resolve()
            if not resolved.exists():
                fail(errors, f"broken link: {markdown.relative_to(root)} -> {raw}")
                continue
            incoming.setdefault(resolved, set()).add(markdown)
            if skill_root is not None and not resolved.is_relative_to(skill_root.resolve()):
                fail(errors, f"relative link escapes Skill root: {markdown.relative_to(root)} -> {raw}")
        for referenced in SKILL_REF_RE.findall(text):
            if referenced not in names:
                fail(errors, f"unknown Skill reference ${referenced}: {markdown.relative_to(root)}")

    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(root)
        if ("references" in relative.parts or "templates" in relative.parts) and path.resolve() not in incoming:
            fail(errors, f"unrouted reference or template: {relative}")

    network_readme = root / "README.md"
    if not network_readme.is_file():
        fail(errors, "missing Skill network README.md")
    else:
        network_text = network_readme.read_text(encoding="utf-8")
        for anchor in EXPECTED_NETWORK_ANCHORS:
            if f"**{anchor}**" not in network_text:
                fail(errors, f"missing canonical network anchor in skills/README.md: {anchor}")

    docs_root = repo_root / "docs"
    if docs_root.is_dir():
        project_markdown = sorted(repo_root.glob("*.md")) + sorted(docs_root.rglob("*.md"))
        for markdown in project_markdown:
            text = markdown.read_text(encoding="utf-8")
            for raw in LINK_RE.findall(text):
                target = relative_link_target(raw)
                if target is None:
                    continue
                resolved = (markdown.parent / target).resolve()
                if not resolved.exists():
                    fail(errors, f"broken project link: {markdown.relative_to(repo_root)} -> {raw}")

        agents_file = repo_root / "AGENTS.md"
        if agents_file.is_file():
            for route in AGENT_ROUTE_RE.findall(agents_file.read_text(encoding="utf-8")):
                matches = list(repo_root.glob(route)) if "*" in route else [repo_root / route]
                if not any(path.exists() for path in matches):
                    fail(errors, f"broken AGENTS.md route: {route}")

        for path in docs_root.rglob("*"):
            if path.name in JUNK_NAMES or path.name.startswith("._"):
                fail(errors, f"junk project doc: {path.relative_to(repo_root)}")

    print(f"skills={len(skills)} visible={len(visible)} markdown={len(list(root.rglob('*.md')))} errors={len(errors)}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("skills"))
    args = parser.parse_args()
    errors = check(args.root)
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
