# Contributing

Use Bun and the locked Python audit dependencies:

```bash
bun install
python3 -m pip install -r requirements-dev.txt
bun run check
```

## Package Mirror and Ownership

- The mapped Skill bodies and attachments under `skills/**` are outbound projections of Agent Kit's admitted snapshot, not editable source in this repository.
- The shared core roster is `ai-coding-os`, `ai-coding-os-evolution`, `product-definition`, `docs-governance`, `evolvable-application-architecture`, `frontend-architecture`, `effect-best-practices`, and `product-harness-system`; Synpraxis and SMIP are its declared candidate contributors.
- `effect-server-module-design` is a model-visible supporting Skill with a separate strict SMIP source group. It does not become a ninth semantic Owner or widen the shared target set.
- Route body, reference, template, and example changes to the owning declared project source. Agent Kit admission is required before an export may be treated as current package content.
- Agent Kit collect must skip all mapped Suite content from this outbound mirror. Export writes only to a clean mirror; a dirty mirror is safely skipped rather than overwritten.
- `experiments/goal-proof/skill/**` is outside the Suite outbound mapping. Goal Proof remains experiment-owned and uses a separate bidirectional Agent Kit mapping; do not treat it as part of the core roster, supporting Server Module Skill, core Router, or Suite ZIP.
- Package-owned surfaces are `README.md`, `README.zh-CN.md`, `skills/README.md`, `CONTRIBUTING.md`, `docs/**`, `VERSION`, `CHANGELOG.md`, and `release/**`.
- Config, a PR, or a staged export alone does not prove admission, package publication, or npm release; cite exact accepted and mirror commits.
- Preserve `release/**` and its [`README.md`](release/README.md) as historical pre-import evidence unless the release workflow explicitly regenerates it.

## Core Suite Changes

- Keep semantic ownership with the declared upstream source; do not treat this repository's `skills/**` projection as the Skill source.
- Preserve independent installation and Skill-local relative links.
- Treat Pass sections as owner-local coverage unless the owner has a real state machine, transaction, migration, safety protocol, or external protocol.
- Update source, references, templates, evals, golden fixtures, public docs, and audits for the same semantic change at the owning source before admission.
- Run `bun run check:core` for the core and Docs audit; run `bun run check` and `bun run pack:dry` for package changes.

## Goal Proof Experiment Changes

- Keep the user-invoked Skill and schemas under `experiments/goal-proof/skill/**`.
- Keep CLI source and tests under `packages/cli/**`.
- Do not add Goal Proof to the core Router, shared core roster, supporting Server Module mapping, or Suite ZIP.
- Preserve historical `experiments/goal-proof/dogfood/**/evidence.jsonl`; corrections append evidence or update current experiment docs rather than rewriting history.
- Run `bun run check:goal-proof-experiment`.

## Documentation Changes

- Use semantic Authority layers and multi-entry Routes rather than workflow or `Read First` sequences.
- Keep one Current Home per meaning and retain useful source/Evidence backlinks.
- Run the Docs audit through `bun run check:core`.

PRs should state the bounded claim, Core/Experiment impact, user-visible contract or command changes, and actual verification commands.
