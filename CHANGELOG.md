# Changelog

## Unreleased

- Expanded the grouped Skill source with `architecture/`, `contracts/`, `preset/`, `tooling/`, and owner-local examples; no Flat source is generated.
- Added independently installable `$ai-coding-os-suite-contracts`; cross-Skill relationships now use canonical Skill names and never depend on grouped sibling paths.
- Removed the installable contract's static Skill manifest and duplicate role/invocation/routing taxonomy; runtime discovery supplies the installed set, while owner IDs preserve only actionable handoffs.
- Pruned repeated vocabulary `status`, duplicate per-term filename patterns, and unused pattern/descriptor fields from the portable contract data.
- Made `$evolvable-application-architecture` the sole application-architecture doctrine and removed the retired compatibility entry.
- Added `$evolvable-application-preset` with Agent-guided discovery, incremental surface adoption, project-owned resolved docs/AGENTS snapshots, optional deterministic renderer primitives, and a golden commerce example.
- Scoped Preset diff/upgrade output to candidate-managed files so unrelated project files are never represented as deletions.
- Expanded Preset `inspect` into a decision-free discovery surface for existing managed files, adopted profiles, dependency versions, apps/packages, and commands.
- Added the atomic, Change-Spec-driven `$effect-api-app-kit` and grouped source audit.
- Aligned cross-Skill prose on `$skill-name`, removed capability-tier narratives, and reduced Skill frontmatter to invocation-relevant fields.
- Removed the unused Preset content fingerprint; upgrades now rely on Preset version, selected profiles, and semantic candidate diffs.
- Renamed the formal long-running goal method to Goal Proof System, with `goal-proof` CLI, v2 Goal Pack artifacts, and `work` / `evidence` command groups.
- Added shared read-output controls (`--limit`, `--include`, `--show-empty`, and `summary --depth`) with bounded, thread-aware repo summary output.
- Added `goal-proof evidence add --stdin` for heredoc evidence record JSON input.
- Added `goal-proof work list` for listing work items inside one Goal Pack, with work item completion/status filters and JSON output.
- Added `goal-proof evidence list/show` for compact, filterable evidence history inspection and explicit full evidence record expansion.

## 0.1.0

- Rebuilt Goal Proof System as a Bun monorepo.
- Added the `goal-proof` npm CLI package in TypeScript.
- Moved the agent skill into the public OS skill suite.
- Added Bun build, typecheck, test, pack, and local install workflows.
- Added bilingual README documentation.
