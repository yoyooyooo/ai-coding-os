# docs-governance

A project-agnostic Skill for converging documentation Authority, Earned Shape, and Evidence. It is for competing current homes, current/accepted-target/future classification, docs layer/partition/identity admission, thin repository entry and docs routers, migration/cleanup, and source alignment.

`SKILL.md` is the entry point. Load only the reference named by the current task.

## Self-check

```bash
python3 scripts/self_check.py
```

The self-check uses only the Python standard library and compiles every scanner without leaving `__pycache__` or `.pyc` files in the Skill tree.

## Repository Audit

From the installed Skill directory:

```bash
python3 scripts/run_docs_audit.py --repo /path/to/repository
```

The default audit is a read-only mechanical coverage pass for explicit identity conflicts, structural authority-route violations, declared routes and links, entry markers, Future route honesty, repository boundaries, and declared source anchors. Semantic Authority conflicts remain Agent-reviewed. It does not require `docs/`, a fixed layer tree, Artifact Graph metadata, a particular execution method, or a tracker. Run it when documentation changed, convergence is being claimed, or repository-wide coverage matters; advisory-only work may state that no repository audit was required.

Opt into branch extensions only when the repository uses them:

```bash
python3 scripts/run_docs_audit.py --repo /path/to/repository --artifact-graph
python3 scripts/run_docs_audit.py --repo /path/to/repository --readability
```

JSON output uses `ensure_ascii=False`. Severity remains narrow:

```text
blocker  explicit identity/Authority contradiction, dishonest Future route,
         repository-root escape, or broken adopted machine contract
warning  broken declared link/route, invalid entry marker, declared entry/layer
         gap, or declared source-anchor failure
info     Earned Shape review signal that still exits successfully
```

Only blockers return exit status 1. Warnings and review signals remain visible without turning contextual judgment into an automatic migration order.

## Dependencies

The scanners have a standard-library fallback for frontmatter parsing. Repository Preset profile validation may use the locked `requirements-dev.txt` dependency set when PyYAML is available.
