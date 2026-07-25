#!/usr/bin/env python3
"""Build a deterministic grouped-source AI Coding OS Suite bundle and sidecar manifest."""
from __future__ import annotations

import argparse
import hashlib
import json
import stat
import zipfile
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover
    raise SystemExit("PyYAML is required") from exc

FIXED_ZIP_TIME = (2020, 1, 1, 0, 0, 0)
CANONICAL_AUDIT_CLAIM_CEILING = (
    "Deterministic grouped-source structure, portable links, schema/eval assets, "
    "Preset/Kit fixtures, bounded subprocess handling, and source-bound bundle checks. "
    "Machine-local paths and compiler-dependent template typecheck status are excluded "
    "from release provenance; no model-run, runtime installation, or production behavior is claimed."
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def tree_hash(root: Path) -> str:
    digest = hashlib.sha256()
    for path in sorted(item for item in root.rglob("*") if item.is_file()):
        relative = path.relative_to(root).as_posix()
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def canonicalize_release_audit(audit: dict[str, Any]) -> dict[str, Any]:
    canonical = json.loads(json.dumps(audit))
    canonical["suite_root"] = "skills"
    for check in canonical.get("checks") or []:
        if not isinstance(check, dict) or check.get("name") != "effect-api-app-kit":
            continue
        detail = check.setdefault("detail", {})
        if isinstance(detail, dict) and "template_typecheck" in detail:
            detail["template_typecheck"] = "excluded-environment-dependent"
    canonical["claim_ceiling"] = CANONICAL_AUDIT_CLAIM_CEILING
    canonical["release_canonicalization"] = {
        "version": 1,
        "suite_root": "relative",
        "excluded": ["machine-absolute-suite-root", "compiler-dependent-template-typecheck-status"],
    }
    return canonical


def skill_frontmatter(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"missing frontmatter: {path}")
    _, frontmatter, _ = text.split("---", 2)
    data = yaml.safe_load(frontmatter) or {}
    if not isinstance(data, dict) or not data.get("name"):
        raise ValueError(f"invalid frontmatter: {path}")
    return data


def source_version(skill_root: Path) -> str | None:
    version_file = skill_root / "VERSION"
    return version_file.read_text(encoding="utf-8").strip() if version_file.is_file() else None


def archive_sources(suite_root: Path) -> list[tuple[str, bytes, int]]:
    """Return the core Suite source and nothing from the repository shell.

    The audit report and provenance manifest are sidecars. Including README,
    repository-root README/docs, CLI code, experiments, package metadata, or repository release support
    would make this archive claim a broader distribution surface than the core
    Skill Suite.
    """
    entries: list[tuple[str, bytes, int]] = []
    for path in sorted(item for item in suite_root.rglob("*") if item.is_file()):
        relative_parts = path.relative_to(suite_root).parts
        if (
            path.name == ".DS_Store"
            or path.name.startswith("._")
            or any(part in {"node_modules", "dist", "__pycache__"} for part in relative_parts)
            or path.suffix in {".pyc", ".pyo"}
        ):
            continue
        mode = 0o755 if path.suffix == ".py" or path.name.endswith(".sh") else 0o644
        entries.append((f"skills/{path.relative_to(suite_root).as_posix()}", path.read_bytes(), mode))
    return entries


def write_zip(path: Path, bundle_root: str, entries: list[tuple[str, bytes, int]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for relative, content, mode in entries:
            info = zipfile.ZipInfo(f"{bundle_root}/{relative}", FIXED_ZIP_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = (stat.S_IFREG | mode) << 16
            archive.writestr(info, content)


def write_sidecar_reports(
    *,
    suite_root: Path,
    out_dir: Path,
    bundle_name: str,
    suite_version: str,
    skills: list[dict[str, Any]],
    audit_path: Path,
    audit: dict[str, Any],
    archive_path: Path,
    archive_hash: str,
    audit_hash: str,
) -> tuple[Path, Path]:
    """Write deterministic release-review sidecars without placing them in ZIP.

    The composition file validates the declared eval contract only. It explicitly
    does not claim an independent model run or a production behavior result.
    """
    change_path = out_dir / f"{bundle_name}-change-report.md"
    composition_path = out_dir / f"{bundle_name}-composition-eval-review.json"
    composition_source = suite_root / "router/ai-coding-os/evals/composition.evals.json"
    composition_data = json.loads(composition_source.read_text(encoding="utf-8"))
    composition_cases = composition_data.get("evals") or []

    change_lines = [
        f"# AI Coding OS Core Suite {suite_version} Change Report",
        "",
        "## Scope",
        "",
        "This sidecar describes the current core-Suite boundary. It is not a claim about downstream installation, model-run quality, external execution-method state, or production behavior.",
        "",
        "- Core source: `skills/**` only.",
        "- Excluded: `experiments/**`, `packages/**`, `docs/**`, repository shell, release support, and generated distribution artifacts.",
        "- Goal Proof is a co-located user-invoked experiment, not a core Skill, Router branch, contract lifecycle, or ZIP member.",
        "- Routes are discovery edges; owner-local Passes are coverage unless an owner has a real state machine or protocol.",
        "",
        "## Minimal Knowledge Kernel",
        "",
        "- Project Authority First.",
        "- Question-scoped Ownership.",
        "- One Scoped Meaning, One Current Home.",
        "- Binding Constraint Is Not Semantic Ownership.",
        "- Evidence Bounds Claims.",
        "- Route Is an Edge; Change Creates an Impact Obligation.",
        "",
        "## Core Skills",
        "",
        *[f"- `${item['name']}`" for item in skills],
        "",
        "## Evidence",
        "",
        f"- Source tree: `skills/**` — SHA-256 `{tree_hash(suite_root)}`.",
        f"- Core audit: `{audit_path.name}` — SHA-256 `{audit_hash}` — errors `{(audit.get('summary') or {}).get('error', 'unknown')}`.",
        f"- Archive: `{archive_path.name}` — SHA-256 `{archive_hash}`.",
        f"- Composition contract cases: `{len(composition_cases)}` in `skills/router/ai-coding-os/evals/composition.evals.json`; independent model run: `not_run`.",
        "",
        "## Claim Ceiling",
        "",
        "The bundle proves deterministic grouped-source packaging, source-tree/audit identity, and the attached mechanical audit. It does not prove runtime installation, user adoption, stochastic model quality, or behavior outside the covered source/test contracts.",
        "",
    ]
    change_path.write_text("\n".join(change_lines), encoding="utf-8")
    composition_path.write_text(
        json.dumps(
            {
                "schema_version": 1,
                "review_kind": "composition-contract-validation",
                "suite_version": suite_version,
                "source": "skills/router/ai-coding-os/evals/composition.evals.json",
                "source_sha256": sha256_file(composition_source),
                "independent_model_run": "not_run",
                "case_count": len(composition_cases),
                "cases": [
                    {
                        "id": item.get("id"),
                        "prompt": item.get("prompt"),
                        "expected_output": item.get("expected_output"),
                        "expectations": item.get("expectations"),
                    }
                    for item in composition_cases
                ],
                "claim_ceiling": "Declared composition-eval structure and expected owner/claim boundaries only; no independent model-run quality, runtime installation, or production behavior claimed.",
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    return change_path, composition_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the AI Coding OS grouped-source Suite ZIP and provenance manifest")
    parser.add_argument("--repo", default=str(Path(__file__).resolve().parents[2]))
    parser.add_argument("--audit", required=True)
    parser.add_argument("--out-dir", default="dist")
    args = parser.parse_args()

    requested_root = Path(args.repo).resolve()
    suite_root = requested_root / "skills" if (requested_root / "skills").is_dir() else requested_root
    distribution_root = requested_root if suite_root != requested_root else requested_root.parent
    if not (suite_root / "README.md").is_file() or not (suite_root / "tooling/build_suite_release.py").is_file():
        raise SystemExit(f"cannot locate a grouped Suite at {requested_root}")

    audit_path = Path(args.audit).resolve()
    audit = json.loads(audit_path.read_text(encoding="utf-8"))
    audit_summary = audit.get("summary") or {}
    if audit_summary.get("error") != 0:
        raise SystemExit("refusing to bundle a Suite audit with errors")
    if audit_summary.get("total") != 0:
        raise SystemExit("refusing to publish canonical release provenance from an audit with findings")
    source_tree_sha256 = tree_hash(suite_root)
    audited_source_tree_sha256 = audit.get("source_tree_sha256")
    if audited_source_tree_sha256 != source_tree_sha256:
        raise SystemExit(
            "refusing to bundle: audit source_tree_sha256 does not match the current skills/** tree "
            f"(audit={audited_source_tree_sha256!r}, current={source_tree_sha256})"
        )

    version_path = suite_root / "VERSION"
    if not version_path.is_file():
        raise SystemExit("skills/VERSION is required for a self-contained Core bundle")
    suite_version = version_path.read_text(encoding="utf-8").strip()
    if not suite_version:
        raise SystemExit("skills/VERSION must not be empty")
    bundle_name = f"ai-coding-os-skill-suite-{suite_version}"
    out_arg = Path(args.out_dir)
    out_dir = out_arg.resolve() if out_arg.is_absolute() else (distribution_root / out_arg).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    archive_path = out_dir / f"{bundle_name}.zip"
    manifest_path = out_dir / f"{bundle_name}.manifest.json"
    release_audit_path = out_dir / f"{bundle_name}.audit.json"
    release_audit = canonicalize_release_audit(audit)
    release_audit_path.write_text(json.dumps(release_audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    skills = []
    for skill_file in sorted(suite_root.rglob("SKILL.md")):
        metadata = skill_frontmatter(skill_file)
        skill_root = skill_file.parent
        skills.append({
            "name": metadata["name"],
            "version": source_version(skill_root),
            "sha256": tree_hash(skill_root),
        })

    write_zip(archive_path, bundle_name, archive_sources(suite_root))
    archive_hash = sha256_file(archive_path)
    audit_hash = sha256_file(release_audit_path)
    contracts_version = (suite_root / "contracts/ai-coding-os-suite-contracts/VERSION").read_text(encoding="utf-8").strip()
    preset_version = (suite_root / "preset/evolvable-application-preset/VERSION").read_text(encoding="utf-8").strip()
    change_path, composition_path = write_sidecar_reports(
        suite_root=suite_root,
        out_dir=out_dir,
        bundle_name=bundle_name,
        suite_version=suite_version,
        skills=skills,
        audit_path=release_audit_path,
        audit=release_audit,
        archive_path=archive_path,
        archive_hash=archive_hash,
        audit_hash=audit_hash,
    )
    manifest = {
        "manifest_version": 2,
        "suite_version": suite_version,
        "source_layout": "grouped",
        "source_tree_sha256": source_tree_sha256,
        "archive_scope": {
            "includes": ["skills/**"],
            "excludes": ["experiments/**", "packages/**", "docs/**", "AGENTS.md", "package.json", "scripts/**", "dist/**"],
        },
        "skills": skills,
        "contracts_version": contracts_version,
        "preset_version": preset_version,
        "audit": {
            "status": "pass",
            "report": release_audit_path.name,
            "sha256": audit_hash,
            "summary": release_audit.get("summary"),
            "source_tree_sha256": audited_source_tree_sha256,
        },
        "archive": {
            "filename": archive_path.name,
            "sha256": archive_hash,
            "size_bytes": archive_path.stat().st_size,
        },
        "reports": {
            "change_report": {"filename": change_path.name, "sha256": sha256_file(change_path)},
            "composition_eval_review": {"filename": composition_path.name, "sha256": sha256_file(composition_path)},
        },
        "archive_sha256": archive_hash,
        "notes": [
            "Per-Skill version is null when that Skill is not independently versioned; sha256 is the source identity.",
            "The sidecar is authoritative for archive_sha256 because a ZIP cannot contain its own final hash without a circular definition.",
            "The ZIP contains only skills/**; the canonical audit report, manifest, project docs, CLI packages, experiments, and repository release support are sidecars or external surfaces.",
            "The canonical audit sidecar normalizes machine-local path and compiler-dependent diagnostics before hashing.",
            "The audit and archive are bound to the same canonical skills/** source_tree_sha256.",
        ],
    }
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "archive": str(archive_path),
        "archive_sha256": archive_hash,
        "manifest": str(manifest_path),
        "audit": str(release_audit_path),
        "change_report": str(change_path),
        "composition_eval_review": str(composition_path),
        "skills": len(skills),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
