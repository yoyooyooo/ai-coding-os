#!/usr/bin/env python3
"""Audit the repository operational entry and opt-in Preset adoption links."""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from common import json_print, relative_path

HOST_EQUIVALENTS = (
    "CLAUDE.md",
    ".github/copilot-instructions.md",
    ".cursorrules",
)
MANAGED_BEGIN_RE = re.compile(r"<!--\s*[^>]+:begin\s*-->")
MANAGED_END_RE = re.compile(r"<!--\s*[^>]+:end\s*-->")
PROJECT_MANIFESTS = ("package.json", "pyproject.toml", "Cargo.toml", "go.mod", "mix.exs", "pom.xml")


def _finding(rule_id: str, severity: str, path: Path, summary: str, evidence: list[str], fix: str) -> dict:
    return {
        "id": f"{rule_id}::{path.as_posix()}",
        "severity": severity,
        "ruleId": rule_id,
        "path": str(path),
        "summary": summary,
        "evidence": evidence,
        "fixHint": fix,
    }


def _manifest_paths(root: Path) -> list[Path]:
    paths: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file() or path.name not in PROJECT_MANIFESTS:
            continue
        if any(part in {".git", "node_modules", "dist", "build", ".next", ".venv", "venv", "__pycache__"} for part in path.parts):
            continue
        if len(path.relative_to(root).parts) <= 3:
            paths.append(path)
    return sorted(paths)


def _detect_topology(root: Path) -> dict[str, Any]:
    manifests = _manifest_paths(root)
    evidence: list[str] = []
    workspace = False
    package = root / "package.json"
    if package.is_file():
        try:
            data = json.loads(package.read_text(encoding="utf-8"))
            if data.get("workspaces"):
                workspace = True
                evidence.append("package.json:workspaces")
        except (OSError, json.JSONDecodeError):
            evidence.append("package.json:unreadable")
    for candidate, marker in (
        (root / "pnpm-workspace.yaml", "pnpm-workspace.yaml"),
        (root / "go.work", "go.work"),
    ):
        if candidate.is_file():
            workspace = True
            evidence.append(marker)
    cargo = root / "Cargo.toml"
    if cargo.is_file() and re.search(r"^\[workspace(?:\.|\])", cargo.read_text(encoding="utf-8", errors="ignore"), re.MULTILINE):
        workspace = True
        evidence.append("Cargo.toml:[workspace]")

    nested_projects = [path for path in manifests if path.parent != root]
    nested_agents = [path for path in root.rglob("AGENTS.md") if path != root / "AGENTS.md" and ".git" not in path.parts]
    for path in nested_agents:
        evidence.append(relative_path(path, root))

    if workspace:
        mode, confidence = "workspace-monorepo", "high"
    elif (root / "AGENTS.md").is_file() and len(nested_projects) >= 2:
        mode, confidence = "aggregate-root", "medium"
        evidence.append("root AGENTS.md with multiple nested project manifests")
    elif len(nested_projects) >= 2:
        mode, confidence = "nested-independent-project", "medium"
        evidence.append("multiple nested project manifests without workspace declaration")
    elif (root / "AGENTS.md").is_file() or any(path.parent == root for path in manifests):
        mode, confidence = "single-project", "medium"
        if any(path.parent == root for path in manifests):
            evidence.append("root project manifest")
    else:
        mode, confidence = "unknown", "low"

    return {
        "mode": mode,
        "confidence": confidence,
        "evidence": sorted(set(evidence)),
        "nestedAgentCount": len(nested_agents),
    }


def _resolved_standard_paths(profile: Path, data: dict[str, Any]) -> list[tuple[str, Path]]:
    standards = data.get("resolved_standards") if isinstance(data, dict) else None
    if not isinstance(standards, dict):
        return []
    result: list[tuple[str, Path]] = []
    for name, value in standards.items():
        if not isinstance(value, str) or not value or "://" in value:
            continue
        result.append((str(name), (profile.parent / value).resolve()))
    return result


def scan(repo: Path) -> dict:
    root = repo.resolve()
    findings: list[dict] = []
    agents = root / "AGENTS.md"
    host_files = [root / rel for rel in HOST_EQUIVALENTS if (root / rel).is_file()]
    docs = root / "docs"
    profile = root / "docs/standards/architecture-profile.yaml"

    if not agents.is_file() and not host_files:
        has_docs_content = docs.is_dir() and any(path.is_file() for path in docs.rglob("*"))
        has_root_manifest = any((root / name).is_file() for name in PROJECT_MANIFESTS)
        severity = "warn" if has_docs_content or has_root_manifest else "info"
        findings.append(_finding(
            "AGENT_ENTRY_MISSING", severity, agents,
            "repository has no tool-neutral AGENTS.md or detected host-equivalent entry",
            ["an operational entry is optional until the repository needs one"],
            "create a small repository entry when agent routing, local commands, or restrictions need a durable home",
        ))

    if agents.is_file():
        text = agents.read_text(encoding="utf-8", errors="ignore")
        required_links = ["docs/README.md"] if docs.is_dir() and any(path.is_file() for path in docs.rglob("*")) else []
        for rel in required_links:
            if rel not in text:
                findings.append(_finding(
                    "AGENT_ENTRY_LINK_MISSING", "warn", agents,
                    f"AGENTS.md does not point to the repository docs router: {rel}",
                    [rel],
                    "add a knowledge-network route to the docs index; keep the target document as authority",
                ))
        line_count = len(text.splitlines())
        if line_count > 220:
            findings.append(_finding(
                "AGENT_ENTRY_TOO_LARGE", "warn", agents,
                f"AGENTS.md has {line_count} lines and may be becoming a shadow standards corpus",
                ["operational entry should stay thin while project-specific commands remain local"],
                "move durable detail to the owning docs layer and keep links in AGENTS.md",
            ))
        begin_count = len(MANAGED_BEGIN_RE.findall(text))
        end_count = len(MANAGED_END_RE.findall(text))
        if begin_count != end_count or begin_count > 1:
            findings.append(_finding(
                "AGENT_MANAGED_SECTION_MARKER_INVALID", "warn", agents,
                "managed AGENTS.md section markers are missing, unbalanced, or repeated",
                [f"begin={begin_count}", f"end={end_count}"],
                "use one stable begin/end marker pair and report drift before replacing the marked section",
            ))

    if profile.is_file():
        profile_text = profile.read_text(encoding="utf-8", errors="ignore")
        mode_match = re.search(r"^\s*mode:\s*([^\s#]+)", profile_text, re.MULTILINE)
        mode = mode_match.group(1).strip("'\"") if mode_match else None
        if mode and mode not in {"candidate-snapshot", "resolved-snapshot"}:
            findings.append(_finding(
                "PRESET_MODE_UNSAFE", "blocker", profile,
                f"Preset mode is {mode!r}; only an explicit candidate or finite-compatible resolved snapshot is supported",
                ["dynamic inheritance can change project rules without a decision"],
                "use candidate-snapshot for generated proposals and explicit project adoption for Current Homes",
            ))
        try:
            import yaml  # type: ignore
            data = yaml.safe_load(profile_text) or {}
        except ImportError:
            data = {}
        except Exception as exc:
            findings.append(_finding(
                "ARCH_PROFILE_PARSE", "blocker", profile,
                f"cannot parse architecture profile: {exc}",
                [], "repair the YAML before treating the profile as current authority",
            ))
            data = {}
        for name, target in _resolved_standard_paths(profile, data):
            if not target.is_file():
                findings.append(_finding(
                    "PRESET_RESOLVED_STANDARD_MISSING", "blocker", target,
                    f"resolved Preset standard is missing: {name}",
                    [str(profile.relative_to(root)), str(target)],
                    "restore the project-owned resolved standard or repair the profile reference",
                ))

    counts = {"blocker": 0, "warn": 0, "info": 0}
    for item in findings:
        counts[item["severity"]] = counts.get(item["severity"], 0) + 1
    counts["total"] = len(findings)
    return {
        "version": "v2",
        "scannedAt": datetime.now(timezone.utc).isoformat(),
        "repoRoot": str(root),
        "agentEntry": "AGENTS.md" if agents.is_file() else None,
        "hostEquivalents": [str(p.relative_to(root)) for p in host_files],
        "presetProfile": str(profile.relative_to(root)) if profile.is_file() else None,
        "repoTopology": _detect_topology(root),
        "summary": counts,
        "findings": findings,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit repository Agent entry and optional Preset adoption")
    parser.add_argument("--repo", default=".", help="Repository root")
    args = parser.parse_args()
    report = scan(Path(args.repo))
    json_print(report)
    if report["summary"]["blocker"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
