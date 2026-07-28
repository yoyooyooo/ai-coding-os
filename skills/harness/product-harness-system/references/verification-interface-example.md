# Verification Interface Example

A TypeScript monorepo may expose the portable command slots through package scripts:

```json
{
  "scripts": {
    "format:check": "prettier --check .",
    "lint": "eslint .",
    "typecheck": "tsc -b --pretty false",
    "test": "vitest run",
    "architecture:check": "python tooling/architecture_check.py",
    "verify:affected": "turbo run lint typecheck test --affected",
    "verify": "pnpm format:check && pnpm lint && pnpm typecheck && pnpm test && pnpm architecture:check"
  }
}
```

`AGENTS.md` maps the roles:

```text
Install: pnpm install --frozen-lockfile
Format/lint: pnpm format:check && pnpm lint
Static/type check: pnpm typecheck
Unit/integration tests: pnpm test
Architecture/boundary check: pnpm architecture:check
Affected verification: pnpm verify:affected
Full verification: pnpm verify
```

## Defaults used

- command roles are stable across projects;
- actual spellings remain project-owned;
- commands are non-interactive and return stable exit codes;
- full verification is not described as proof of product success.

## Conditional elements

- `architecture:check` exists because import/public-boundary pressure is real;
- affected verification depends on a trustworthy project graph;
- a destructive migration command would require `--dry-run` and explicit apply.

## Intentionally omitted

- a universal JSON evidence envelope;
- one fixed package manager;
- a release command or deployment workflow;
- a claim that all tests prove external provider behavior.

## Related Skills

- `$product-harness-system`
- `$docs-governance`
