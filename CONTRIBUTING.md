# Contributing

Use Bun and the locked Python audit dependencies:

```bash
bun install
python3 -m pip install -r requirements-dev.txt
bun run check
```

## Core Suite Changes

- Keep core Skill source under the owning `skills/**` group.
- Preserve independent installation and Skill-local relative links.
- Treat Pass sections as owner-local coverage unless the owner has a real state machine, transaction, migration, safety protocol, or external protocol.
- Update source, references, templates, evals, golden fixtures, public docs, and audits for the same semantic change.
- Run `bun run check:core` and `bun run bundle:skills` when distribution boundaries change.

## Goal Proof Experiment Changes

- Keep the user-invoked Skill and schemas under `experiments/goal-proof/skill/**`.
- Keep CLI source and tests under `packages/cli/**`.
- Do not add Goal Proof back to the core Router, core contract enums, core Skill roster, or core ZIP.
- Preserve historical `experiments/goal-proof/dogfood/**/evidence.jsonl`; corrections append evidence or update current experiment docs rather than rewriting history.
- Run `bun run check:goal-proof-experiment`.

## Documentation Changes

- Use semantic Authority layers and multi-entry Routes rather than workflow or `Read First` sequences.
- Keep one Current Home per meaning and retain useful source/Evidence backlinks.
- Run the Docs audit through `bun run check:core`.

PRs should state the bounded claim, Core/Experiment impact, user-visible contract or command changes, and actual verification commands.
