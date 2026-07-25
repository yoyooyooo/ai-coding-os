# Goal Pack Artifact Routing

Goal Proof owns its execution-state artifacts. They are method-local and do
not become project documentation Authority merely because they are current in a
Goal Pack.

## Home

A repository-declared home wins. The portable fallback is:

```text
.goal-proof/
  README.md                    optional method index
  inbox/                       weak input not yet a Goal Pack
  sources/                     consumed provenance
  goals/<goal-id>/
    goal.yaml                  protected objective and completion contract
    progress.yaml              proof step, work state, next action
    evidence.jsonl             append-only transition evidence
    plans/<work_id>.md         selected high-risk slice only
    interface-capabilities.yaml optional candidate trace
    product-harness.yaml       optional candidate proof contract
    notes/                     long local context
```

`goal_pack_root` is the concrete `goals/<goal-id>/` directory. It is resolved
once at activation and inherited by all method branches. Bare CLI IDs use
`.goal-proof/goals/<goal-id>/`; legacy `docs/goal-proof/goals/<goal-id>/` packs
remain reader-compatible during the migration but are not the writer default.

## Artifact Boundaries

| Artifact | Method role | Must not become |
| --- | --- | --- |
| `goal.yaml` | authorization and protected completion contract | Product requirement authority |
| `progress.yaml` | current proof step and local work state | tracker, roadmap, or release state |
| `evidence.jsonl` | append-only bounded observations/reduction inputs | product acceptance or docs lifecycle verdict |
| `plans/<work_id>.md` | pre-reviewed structure for one `needs_plan` slice | second planning system or durable spec owner |
| `inbox/` | retained weak signal | backlog/queue |
| `sources/` | consumed provenance | current decision home |
| interface companion | candidate interface trace | full InterfaceCapability Authority |
| harness companion | candidate proof trace | product truth or raw run artifact store |

A Harness pass never implies Goal completion. Goal completion never implies
Product acceptance, documentation promotion, release, or external tracker
completion.

## Routing Decisions

```text
current product / terminology / rule / architecture meaning
  -> the project Authority selected by that question

implementation behavior or observation
  -> source, test, runtime, Harness, CI, or report Evidence surface

Goal-local objective, proof step, work state, or completion review
  -> goal_pack_root

weak retained input
  -> .goal-proof/inbox/ or source material

consumed external input
  -> .goal-proof/sources/ or pack notes with provenance

high-risk selected slice
  -> goal_pack_root/plans/<work_id>.md
```

Do not copy project glossaries, ADRs, requirements, Harness schemas, or tracker
state into the pack. Reference Authority IDs and paths instead.

## Companion Promotion

Local `interface-capabilities.yaml` and `product-harness.yaml` may help one
Goal Pack reason about traceability. They must be thin and reference durable
IDs where those already exist.

When their meaning survives the execution method, the project explicitly
chooses one of:

```text
promote to the semantic project owner
keep method-local as historical evidence
split durable meaning from local execution detail
retire under the host retention policy
block pending authority decision
```

Promotion retains source and Evidence links but removes workflow-specific status
from the durable artifact. The local companion no longer acts as a second
Current Home.

## Inbox And Retention

Inbox labels may describe `weak_signal`, `open_candidate`, `decision_needed`,
`bridge_needed`, `source_ready`, or `retired`. They are method-local labels, not
core vocabulary or a scheduler.

Retain a Goal artifact only while it preserves current method continuity,
Evidence provenance, or an explicitly selected future handoff. Reduce duplicate
or obsolete prose to source links, retire it according to the repository policy,
and preserve append-only evidence. Do not silently rewrite historical records.

## Project Adapter

A project may add a thin local adapter that states its declared Goal Pack home,
language policy, commands, retention policy, and destination Authorities. It
must not restate generic Goal Proof doctrine or create a parallel docs layer.
