#!/usr/bin/env python3
"""Audit the repository Agent entry and optional Preset adoption links."""
from __future__ import annotations
import argparse, json
from datetime import datetime, timezone
from pathlib import Path

HOST_EQUIVALENTS = (
    "CLAUDE.md",
    ".github/copilot-instructions.md",
    ".cursorrules",
)


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


def scan(repo: Path) -> dict:
    root = repo.resolve()
    findings: list[dict] = []
    agents = root / "AGENTS.md"
    host_files = [root / rel for rel in HOST_EQUIVALENTS if (root / rel).is_file()]
    profile = root / "docs/standards/architecture-profile.yaml"
    source_standard = root / "docs/standards/source-topology-and-naming.md"
    vocabulary = root / "docs/standards/naming-vocabulary.yaml"

    if not agents.is_file() and not host_files:
        findings.append(_finding(
            "AGENT_ENTRY_MISSING", "warn", agents,
            "repository has no tool-neutral AGENTS.md or detected host-equivalent entry",
            ["expected a thin operational entry, not a full standards corpus"],
            "create a small AGENTS.md or document the canonical host equivalent",
        ))

    if agents.is_file():
        text = agents.read_text(encoding="utf-8", errors="ignore")
        required_links = ["docs/README.md"]
        if profile.is_file():
            required_links.extend([
                "docs/standards/architecture-profile.yaml",
                "docs/standards/source-topology-and-naming.md",
                "docs/standards/naming-vocabulary.yaml",
            ])
        for rel in required_links:
            if rel not in text:
                findings.append(_finding(
                    "AGENT_ENTRY_LINK_MISSING", "warn", agents,
                    f"AGENTS.md does not point to current project authority: {rel}",
                    [rel],
                    "add a Read First link; do not copy the target document into AGENTS.md",
                ))
        line_count = len(text.splitlines())
        if line_count > 220:
            findings.append(_finding(
                "AGENT_ENTRY_TOO_LARGE", "warn", agents,
                f"AGENTS.md has {line_count} lines and may be becoming a shadow standards corpus",
                ["recommended entry is normally one to two screens plus project-specific commands"],
                "move durable detail to the owning docs layer and keep links in AGENTS.md",
            ))

    if profile.is_file():
        for required in (source_standard, vocabulary):
            if not required.is_file():
                findings.append(_finding(
                    "PRESET_RESOLVED_STANDARD_MISSING", "blocker", required,
                    "architecture profile exists but a resolved standard it should reference is missing",
                    [str(profile.relative_to(root))],
                    "restore the project-owned resolved standard or repair the profile references",
                ))
        try:
            import yaml
            data = yaml.safe_load(profile.read_text(encoding="utf-8")) or {}
            mode = ((data.get("preset") or {}).get("mode"))
            if mode and mode != "resolved-snapshot":
                findings.append(_finding(
                    "PRESET_MODE_UNSAFE", "blocker", profile,
                    f"Preset mode is {mode!r}; projects must use a resolved snapshot",
                    ["dynamic inheritance can change project rules without a decision"],
                    "set preset.mode to resolved-snapshot and perform explicit upgrades",
                ))
        except Exception as exc:
            findings.append(_finding(
                "ARCH_PROFILE_PARSE", "blocker", profile,
                f"cannot parse architecture profile: {exc}",
                [], "repair the YAML before treating the profile as current authority",
            ))

    counts = {"blocker": 0, "warn": 0, "info": 0}
    for item in findings:
        counts[item["severity"]] = counts.get(item["severity"], 0) + 1
    counts["total"] = len(findings)
    return {
        "version": "v1",
        "scannedAt": datetime.now(timezone.utc).isoformat(),
        "repoRoot": str(root),
        "agentEntry": "AGENTS.md" if agents.is_file() else None,
        "hostEquivalents": [str(p.relative_to(root)) for p in host_files],
        "presetProfile": str(profile.relative_to(root)) if profile.is_file() else None,
        "summary": counts,
        "findings": findings,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    args = parser.parse_args()
    report = scan(Path(args.repo))
    print(json.dumps(report, ensure_ascii=True, indent=2))
    if report["summary"]["blocker"]:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
