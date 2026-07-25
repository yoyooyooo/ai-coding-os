# Goal Proof System CLI

## Compatibility

The current templates and owner-local schemas use Goal Pack `schema_version: 2`
and require `goal-proof` CLI `>=0.2.0 <0.3.0` for list-shaped
`completion.required_evidence`. CLI 0.2.x also reads a legacy scalar and emits a
migration warning; historical packs need not be rewritten only for that reason.
The experiment Skill, templates, and CLI package version must advance together when
a machine field changes.

Install and inspect:

```bash
npm install -g goal-proof@^0.2.0
goal-proof --help
goal-proof <command> --help
```

Read commands:

```bash
goal-proof inspect <goal-pack> [--json]
goal-proof summary [project-root|goals-dir] [--completion all|todo|done] [--status <status>] [--depth repo|groups|items] [--limit N] [--include fields] [--show-empty] [--json]
goal-proof list [project-root|goals-dir] [--completion all|todo|done] [--status <status>] [--limit N] [--include fields] [--show-empty] [--json]
goal-proof work list <goal-pack> [--completion all|todo|done] [--status queued|active|blocked|done] [--limit N] [--include fields] [--show-empty] [--json]
goal-proof work brief <goal-pack> [--work <id>] [--json]
goal-proof evidence list <goal-pack> [--limit N] [--work <id>] [--type discovery|decision|implementation|coordination|review|planning] [--result done|blocked] [--decision <value>] [--next-action proof_step|continue|needs_plan|blocked|review|done|needs_human] [--completion-satisfied true|false] [--changed-file <glob>] [--command-status pass|fail] [--contains <text>] [--include fields] [--show-empty] [--json]
goal-proof evidence show <goal-pack> --index N [--json]
```

For repo-wide progress questions, prefer `summary`, `list`, `work list`, and
`evidence list` over hand-written roadmap prose. Use `relations *` for
thread-scoped continuity, predecessor evidence, and graph checks. A roadmap can
constrain product strategy and launch gates, but Goal Pack files and CLI output
remain the source for ready / running / done and active-work claims.

State commands:

```bash
goal-proof work activate <goal-pack> --work <id> [--dry-run]
goal-proof evidence add <goal-pack> (--file evidence-record.json | --json '<json>' | --stdin) [--apply] [--check]
goal-proof apply <goal-pack> [--dry-run]
goal-proof check <goal-pack>
```

Relation commands:

```bash
goal-proof relations list [project-root|goals-dir] [--thread <id>] [--limit N] [--include fields] [--show-empty] [--json]
goal-proof relations goals [project-root|goals-dir] [--thread <id>] [--completion all|todo|done] [--status forming|ready|running|blocked|done|retired] [--next-action proof_step|continue|needs_plan|blocked|review|done|needs_human] [--limit N] [--include fields] [--show-empty] [--json]
goal-proof relations work [project-root|goals-dir] [--thread <id>] [--completion all|todo|done] [--status queued|active|blocked|done] [--goal-completion all|todo|done] [--goal-status forming|ready|running|blocked|done|retired] [--goal <goal-id>] [--limit N] [--include fields] [--show-empty] [--json]
goal-proof relations check [project-root|goals-dir] [--thread <id>] [--json]
goal-proof relations graph [project-root|goals-dir] [--thread <id>] [--json]
```

`<goal-pack>` should be the resolved `goal_pack_root`. A bare goal ID first
uses `.goal-proof/goals/`; projects with another artifact home pass the
directory explicitly. CLI 0.2.x also reads the former `docs/goal-proof/goals/`
location for finite migration compatibility. `summary` and `list` accept a
project root or goals directory.

For `summary` and `list`, `--completion todo` means Goal Pack status is neither
`done` nor `retired`, and `--status` filters raw Goal Pack status. For
`work list`, `--completion todo` means work item status is not `done`, and
`--status` filters raw work item status.

For `evidence list`, filters compose with AND semantics and output compact
evidence record summaries by default. Use `evidence show --index N` to expand
one full evidence record.

Read JSON commands share output controls: `--limit` bounds collections,
`--include path,objective,links` restores omitted detail, and `--show-empty`
restores empty/default fields. `summary` defaults to `--depth groups` and
`--limit 20`; `--depth repo` returns only repo totals plus thread/unthreaded
counts, while `--depth items` nests threaded goal items under `threads` and
leaves only unthreaded goals in top-level `items`.

For `evidence add`, choose exactly one input source. Use `--stdin` for heredoc
JSON. Use `--apply --check` for the common append, deterministic apply, and
validation path. `work activate` and `apply` are state-transition commands, not
payload input commands.

## CLI-unavailable fallback

The method remains executable without the CLI:

1. read `goal.yaml`, `progress.yaml`, and every non-empty JSON line in
   `evidence.jsonl`;
2. validate required fields against the local schemas and checker rules;
3. append exactly one JSON object without rewriting prior lines;
4. reduce progress from that record while preserving protected Goal contract
   fields;
5. rerun available project checks and manually verify the completion-review
   contract before setting `done`.

The CLI owns deterministic parsing, append, reduction, read views, and mechanical
checks. The Skill owns method semantics, claim judgment, and manual fallback.

Local development:

```bash
bun install
bun run check
```
