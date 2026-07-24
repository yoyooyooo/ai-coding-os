# Human-Agent SOP

This SOP keeps long-running AI coding from becoming a pile of plans, stale
prompts, and unverified claims.

## Operating Loop

```text
human input
  -> inspect current repository authority and state
  -> classify the information or change
  -> route durable content to the right owner
  -> implement and verify through repository-selected surfaces
  -> report observations, supported conclusions, and unresolved uncertainty
  -> update durable authority only when current truth actually changed
```

This is a semantic map rather than a mandatory reasoning sequence. Planning,
implementation, inspection, and verification may follow the order best suited
to the work while preserving repository authority and evidence boundaries.

## Human Escalation Rule

Escalate to a human only as a last resort. Missing implementation detail is not
itself a blocker when the current authority, allowed write scope, and
falsifiable verification intent are clear. The Agent should create the thinnest
missing harness, bridge, command wrapper, local test, report, index, or queue
plumbing that the work genuinely requires.

Mark work blocked and ask for a human / higher-authority decision only when one
of these is true:

- no honest falsifiable evidence path can be named;
- continuing would change product truth, SSoT / standards / ADR authority,
  public protocol/API/schema posture, security policy, or claim standard;
- continuation requires unsafe raw/private data handling or retention;
- two authority layers plausibly conflict and the agent cannot resolve by the
  project's conflict order;
- legal, security, release-history, compliance, or irreversible data risk is
  present.

In short:

```text
missing harness -> agent fills within scope
missing bridge -> agent creates bridge within scope
missing authority / changed claim -> stop and escalate
```

## 1. Classify The Input

Treat user input as one of:

- `governance-convergence`: initialize, migrate, or periodically clean planning
  and docs governance so material lands in the right layer.
- `workflow-supplement`: add or repair a repo's human-agent workflow baseline
  after a docs foundation already exists. This is a narrow convergence pass,
  not a second bootstrap doctrine.
- `signal-placement`: decide which layer or method should hold a weak signal,
  open candidate, source note, Goal Pack, report, or implementation artifact.
- `proposal`: shaped candidate with tradeoffs or open questions when the repo
  is not routing that candidate through `$goal-proof`.
- `authority change`: SSoT, standard, ADR, protocol, or governance update.
- `execution-method-artifact`: tracker, spec, Goal Pack, or another explicitly adopted method artifact.
- `implementation`: chosen change with files, verification surfaces, and an honest conclusion boundary.
- `audit`: compare current repo against declared rules.
- `cleanup`: delete, migrate, or retire old artifacts.

Do not turn every idea into a goal. Do not turn every goal into a work item list.
Do not split initialization and cleanup into separate doctrines: they are the
same convergence loop with different amounts of existing material.

## 1.5 Governance Convergence

Use governance convergence when a repo is new, lightly documented, previously
documented under another scheme, or already mature but due for cleanup.

The convergence loop is:

```text
inspect current material
  -> classify docs-layer state
  -> keep / create only thin routing structure
  -> promote authority
  -> demote candidates
  -> bridge gaps
  -> archive converted source
  -> delete obsolete material
  -> update nearest indexes
  -> run audit
```

New repositories are not a special workflow. They usually have fewer artifacts
to classify, so convergence mostly creates thin layer README files and a small
project-local `AGENTS.md` / docs router. Existing repositories follow the same
loop but first assign docs-layer retention verdicts to current docs. For artifacts belonging to an explicitly adopted execution method, use that
method for its internal lifecycle and this Skill for layer placement, indexing,
retained-evidence risk, and conflict behavior.

When baseline docs are missing, create only the minimum host-appropriate
structure needed for future agents to route work:

```text
AGENTS.md or host equivalent
docs/README.md
docs/product/README.md, when the repo has a product or operator surface
docs/ssot/README.md
docs/standards/README.md
docs/adr/README.md and docs/adr/_template.md
```

Add optional layers such as `docs/goal-proof/**`, `docs/roadmap/**`,
`docs/protocols/**`, `docs/design/**`, or root `specs/**` only when the project
actually needs that artifact type or is explicitly adopting that workflow.

### Workflow Supplement

Use workflow supplement when the repo already has some docs foundation, but the
agent operating loop is missing, scattered, or too implicit. It usually touches
the project entry instructions, the standards layer, nearby README indexes, and
the docs router. It should not duplicate the full docs bootstrap or create a
project-local replacement for this governance skill.

The supplement loop is:

```text
inspect current workflow surface
  -> identify the missing collaboration contract
  -> update the thinnest authority files
  -> add index links
  -> verify private/local tooling did not leak into public doctrine
  -> report proven changes and not_claimed
```

Good workflow supplements define how agents read, route, implement, verify, and
report in that repo. They do not encode one user's private runtime, local skill
distribution, or a specific retrieval provider as generic project doctrine.

## 2. Read Before Writing

Default read path:

```text
AGENTS.md
docs/README.md
docs/ssot/README.md
docs/standards/README.md
```

Then read the relevant layer README and the artifact being changed. If the repo
does not have these files, run governance convergence: use the host's documented
equivalent if it exists, otherwise create the thinnest docs model needed to
route future work.

Before writing or rewriting durable docs, also extract the host narrative
language rule from `AGENTS.md` / docs policy. Apply it to body prose in
planning, roadmap, governance, report, proposal, goal and spec artifacts. Keep
frontmatter keys, schema fields, commands, paths, code symbols, prompt blocks
and reusable template labels stable when English improves copyability or
machine matching.

Wrong pattern:

```text
Host requires Chinese planning prose -> agent copies an English goal-plan
template verbatim into docs/goal-proof/**.
```

Correct pattern:

```text
Host requires Chinese planning prose -> frontmatter and command blocks stay
stable; narrative sections explain objective, scope, constraints, stop rules
and evidence in Chinese.
```

## 3. Place The Artifact

Ask:

- Is this current truth?
- Is it an executable rule?
- Is it an adopted decision record?
- Is it sequence/status?
- Is it an open candidate?
- Is it a wire contract?
- Is it an implementation work item system artifact?
- Is it evidence?

Place by answer, not by convenience.

## 3.5 Planning Convergence Protocol

Use this protocol when planning arrives across time, people, agents, branches,
or worktrees and begins to conflict, duplicate, drift, or leave placement gaps.

The goal is to route planning material to the right docs layer or method without
pretending every idea is implementation-ready.

### Method Handoff

Do not reimplement Goal Proof System artifact lifecycle here. When a project uses
`$goal-proof`, that skill owns:

```text
inbox/source/Goal Pack routing
promotion gate
retention and demotion marker
Goal Relations
evidence-backed completion
completion review
ready / running / blocked / done progress state
```

This governance skill owns:

```text
docs-layer placement
authority-layer conflict
host language policy
index coverage
retained evidence risk
project-local governance simplification
```

When a weak signal or candidate arrives:

```text
uses Goal Proof System -> route to $goal-proof inbox/source/Goal Pack rules
does not use Goal Proof System -> route to docs/proposals, docs/research, or nearest implementation artifact
already authority -> promote to SSoT / standard / ADR / protocol / roadmap
already implemented/evidenced -> retain as report/source/backlink or delete duplicate text
```

### Decision Queue

When planning inputs conflict or need a human / higher-authority decision, do
not bury the decision inside prose. Record a decision item in the closest open
proposal, planning index, host project decision queue, or Goal Proof System artifact
selected by `$goal-proof`.

Use this shape:

```text
id:
source_artifacts:
conflict:
options:
decision_level: product | ssot | standard | adr | roadmap | goal | implementation
owner:
needed_by:
status: open | decided | obsolete
resolution_target:
```

After decision:

```text
decided
  -> promote semantic authority to SSoT / standard / ADR / roadmap
  -> route chosen work to the owning tracker/spec/execution artifact
  -> backlink from the source material
  -> convert stale candidate material to source or delete it
```

### Convergence Sweep

Periodically run a convergence sweep over candidate docs, Goal Proof System
indexes, roadmaps, reports, sources, specs, and authority docs. This is a
docs-layer cleanup pass, not a replacement for `$goal-proof` lifecycle:

```text
promote    rule / truth / decision becomes authority
demote     useful context is not authority
split      one artifact contains multiple docs-layer concerns
merge      duplicates describe the same candidate or source
bridge     docs route or authority relation needs a thin bridge
archive    converted material becomes source
delete     obsolete material has no evidence or routing value
block      human / higher-authority decision is required
```

Sweep output:

```text
promoted:
demoted:
split:
merged:
bridges_needed:
archived_as_source:
deleted:
decision_queue:
open_questions:
```

### Queue Boundaries

Keep queues distinct:

- Goal Proof System inbox, relations, launch prompts, and completion state: governed
  by `$goal-proof` and related Goal Proof System phase / prompt skills.
- Proposal pool: shaped candidates only when the repo is not using
  `$goal-proof` for that candidate stream.
- Decision queue: conflicts, missing authority, and human decisions.
- Roadmap: sequence, gates, coverage, status, and evidence links.
- Reports: evidence only.

In a Goal Proof System project, roadmap status is a route/index/evidence signal.
Do not use it as a second source of Goal Pack progress truth.

Do not use a roadmap, proposal directory, Goal Proof System inbox, or
method-specific queue as a generic planning backlog.

## 4. Make Work Legible Without Controlling The Agent

Before durable implementation, the Agent should be able to discover enough
repository context to act honestly:

```text
objective or requested change
relevant authority refs
chosen product slice
allowed write/security boundaries
available verification surfaces
public or durable compatibility constraints
```

These are discovery needs rather than a mandatory form or fixed execution state
machine. Infer and refine them from repository authority while working. Ask
only when unresolved ambiguity changes product meaning, fact authority, public
compatibility, permissions, privacy, or irreversible behavior.

If a project uses a tracker, Goal Pack, spec, or another execution method, that
method may impose its own durable fields. Docs Governance does not make one
method universal.

## 5. Preserve Agent Freedom And Durable Boundaries

The Agent may adapt exact steps, verification depth, and implementation shape as
new evidence appears. Governance should not prescribe fixed attempt counts,
model roles, diff-size budgets, or one mandatory planning sequence.

The Agent still must not:

- silently change current product authority or public contracts;
- hide a new long-lived rule only in code when project standards/SSoT must change;
- report evidence stronger than the exercised surface;
- move active progress into Roadmap or Reports as a second truth;
- retain duplicate current documentation homes.

Small missing bridges, harnesses, indexes, or checks can be created directly when
their meaning follows from current authority. Preserve a future candidate only
when it has durable navigation value.

## 6. Report Evidence

A useful report includes:

```text
claim:
evidence:
commands_or_checks:
changed_artifacts:
remaining_gaps:
next_action:
```

Reports are optional unless needed for cross-session navigation, auditability,
handoff, or user request. When written, they must be evidence-bearing and
bounded; they are not diaries.

## Skill Handoffs

Use this governance skill for:

- docs layer design;
- artifact placement;
- repo-level SOP;
- cleanup and migration of old docs structures;
- deciding how project-local skills should be replaced or simplified.

Use the repository's configured planning, tracker, spec and execution skills
for:

- candidate shaping and first proof paths;
- objective and acceptance contracts;
- exact file-level work_items and blocking edges;
- test commands, local checklists and handoff-ready sequencing;
- rolling progress, evidence and completion review.

When a repository explicitly adopts Goal Proof System for a candidate stream,
use `$goal-proof` for its method-internal Goal Pack, progress, evidence and
completion lifecycle. That choice is optional and must not be inferred merely
because `$docs-governance` is in use.

The handoff boundary is artifact-based. Do not rely on conversation memory as
the only carrier of scope.
## Current/Future Classification Pass

Before restructuring mature docs, classify each claim as current-fact, current-binding, future-candidate, active-proof, or historical-evidence. Current layers must stay aligned with source/accepted contracts; future complete models go to capability capsules. Preserve Product Evolution Sequence and promotion gates even when their implementation has not started. See [Current vs Future](current-vs-future.md), [Roadmap and Future Capsules](roadmap-and-future-capsules.md), and [Source-Code Alignment](source-code-alignment.md).

When a future capability becomes active work, create or link its owning
tracker/spec/execution artifact rather than copying progress into Roadmap. When
proof/adoption succeeds, move authority into formal layers and shrink the
capsule in the same change.
