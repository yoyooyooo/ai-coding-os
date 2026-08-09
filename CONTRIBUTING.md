# Contributing

Use Bun and the locked Python audit dependencies:

```bash
bun install
python3 -m pip install -r requirements-dev.txt
bun run check
```

## Package Mirror and Ownership

- The eight tracked core Skill bodies and attachments under `skills/**` are outbound projections of Agent Kit's admitted snapshot, not editable source in this repository. Their candidate source is Synpraxis; the route is Synpraxis -> AK upstream admission -> accepted snapshot -> this package mirror.
- The tracked core roster is `ai-coding-os`, `ai-coding-os-evolution`, `product-definition`, `docs-governance`, `evolvable-application-architecture`, `frontend-architecture`, `effect-best-practices`, and `product-harness-system`.
- Route body, reference, template, and example changes for that roster to Synpraxis. Agent Kit admission is required before `ak export` updates this mirror.
- Agent Kit collect must skip mapped core Skill content from this outbound mirror. Export writes only to a clean mirror; a dirty mirror is safely skipped rather than overwritten.
- `experiments/goal-proof/skill/**` is outside the core outbound mapping. Goal Proof remains experiment-owned and uses a separate bidirectional Agent Kit mapping; do not treat it as part of the core roster, core Router, or core ZIP.
- Package-owned surfaces are `README.md`, `README.zh-CN.md`, `skills/README.md`, `CONTRIBUTING.md`, `docs/**`, `VERSION`, `CHANGELOG.md`, and `release/**`.
- This Ticket defines a routing/config contract only. Current docs/config do not prove Synpraxis source merge, AK admission, export, package commit/push, or npm release; Ticket 04 supplies live evidence.
- Preserve `release/**` and its [`README.md`](release/README.md) as historical pre-import evidence. Do not regenerate release artifacts in this Ticket.

## Core Suite Changes

- Keep semantic ownership with the declared upstream source; do not treat this repository's `skills/**` projection as the Skill source.
- Preserve independent installation and Skill-local relative links.
- Treat Pass sections as owner-local coverage unless the owner has a real state machine, transaction, migration, safety protocol, or external protocol.
- Update source, references, templates, evals, golden fixtures, public docs, and audits for the same semantic change at the owning source before admission.
- Run `bun run check:core` for the core and Docs audit; run `bun run check` and `bun run pack:dry` for package changes.

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
