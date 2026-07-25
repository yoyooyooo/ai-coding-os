#!/usr/bin/env python3
"""Validate the packaged skill without third-party dependencies."""

from __future__ import annotations

import json
import os
import py_compile
import subprocess
import sys
import tempfile
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    required = [
        root / "SKILL.md",
        root / "agents" / "openai.yaml",
        root / "references" / "docs-layer-model.md",
        root / "references" / "elastic-shape-and-identity.md",
        root / "scripts" / "common.py",
        root / "evals" / "evals.json",
    ]
    missing = [str(path.relative_to(root)) for path in required if not path.is_file()]
    if missing:
        raise SystemExit("missing required files: " + ", ".join(missing))

    with tempfile.TemporaryDirectory(prefix="docs-governance-pyc-") as tmp:
        for index, path in enumerate(sorted((root / "scripts").glob("*.py"))):
            py_compile.compile(str(path), cfile=str(Path(tmp) / f"{index}.pyc"), doraise=True)

    data = json.loads((root / "evals" / "evals.json").read_text(encoding="utf-8"))
    if data.get("skill_name") != "docs-governance":
        raise SystemExit("evals skill_name mismatch")
    ids = [item.get("id") for item in data.get("evals", [])]
    if len(ids) != len(set(ids)):
        raise SystemExit("duplicate eval ids")

    skill = (root / "SKILL.md").read_text(encoding="utf-8")
    for pointer in (
        "references/docs-layer-model.md",
        "references/elastic-shape-and-identity.md",
        "references/current-vs-future.md",
        "references/roadmap-and-future-capsules.md",
        "scripts/run_docs_audit.py",
    ):
        if pointer not in skill:
            raise SystemExit(f"SKILL.md missing pointer: {pointer}")

    tests = root / "tests"
    test_result = None
    if tests.is_dir():
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
        completed = subprocess.run(
            [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-t", str(root)],
            cwd=root,
            env=env,
            check=False,
        )
        test_result = completed.returncode
        if completed.returncode:
            raise SystemExit("docs-governance fixture tests failed")

    print(json.dumps({"ok": True, "compiledScripts": len(list((root / 'scripts').glob('*.py'))), "evalCount": len(ids), "fixtureTests": "pass" if test_result == 0 else "not-run"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
