# Contributing

Use Bun for all local development.

```bash
bun install
bun run check
```

Before opening a change:

- keep CLI source in `packages/cli/src/`;
- keep Skill material in the owning grouped source under `skills/**`; `$goal-proof` lives at `skills/goal/goal-proof-system/`;
- update README or skill references when command names, paths, or Goal Pack
  fields change;
- add or update tests for CLI behavior changes;
- run `bun run check`;
- for Skill or docs changes, also run `python3 skills/tooling/suite_audit.py --suite skills` and the Docs audit documented in `AGENTS.md`.

Do not rewrite historical `evidence.jsonl` entries in real Goal Packs. Append a
new evidence record when evidence or interpretation changes.
