# Bootstrap

Use this only after `$goal-proof` is explicitly selected and a persistent Goal
Pack home is justified. Do not initialize a method tree for a read-only
question, a one-turn change, or a workstream already owned by another execution
ledger.

## Discovery

Inspect only relevant project conventions:

```text
AGENTS.md / repository instructions
project execution-method declaration
existing Goal Pack home
Product / SSoT / Standards / ADR / Architecture routes
source, tests, Harness, and release Evidence surfaces
```

A project-declared Goal Pack home wins. Map it to the method roles below rather
than creating a second state tree.

## Admission

Bootstrap when explicit adoption needs durable state across evidence records,
sessions, agents, or a repository-selected downstream consumer. Otherwise keep
the work in its existing owner.

## Portable Fallback

When no host convention exists, use a method-owned hidden root rather than a
project documentation layer:

```text
.goal-proof/
  README.md              optional local method index
  inbox/                 weak signals only; not a backlog
  sources/               consumed context with provenance
  goals/
    <goal-id>/
      goal.yaml
      progress.yaml
      evidence.jsonl
      plans/<work_id>.md             only when needs_plan
      interface-capabilities.yaml    optional candidate companion
      product-harness.yaml           optional candidate companion
      notes/
```

Resolve the concrete pack as `goal_pack_root`. A bare CLI goal ID searches
`.goal-proof/goals/<goal-id>/` first. CLI 0.2.x also reads the former
`docs/goal-proof/goals/<goal-id>/` location for finite migration compatibility;
new writes and documentation use the hidden-root path.

## Minimal Local Index

```markdown
# Goal Proof

This directory is the repository-selected Goal Proof execution state. It is not
Product, SSoT, ADR, Architecture, Roadmap, or documentation Authority.

## Homes

| Role | Path |
| --- | --- |
| inbox | `.goal-proof/inbox/` |
| sources | `.goal-proof/sources/` |
| goal packs | `.goal-proof/goals/<goal-id>/` |
| work plans | `.goal-proof/goals/<goal-id>/plans/<work_id>.md` |

## Active Goal Packs

## Sources
```

## Guardrails

- Goal Pack state consumes project Authority; it does not replace it.
- Inbox is not a backlog, queue, tracker, or requirement registry.
- Sources preserve provenance, not live scope.
- Evidence records are bounded observations and reductions, not diaries.
- `plans/<work_id>.md` is exceptional and only exists for a selected
  `needs_plan` slice.
- Method-local interface/harness companions are candidates; durable semantics
  move to the project authority selected by their meaning.
- Retire obsolete local material under the host retention policy after checking
  source and Evidence links. Never silently destroy historical evidence.
- Stop for a higher-authority decision when Product, SSoT, Standard, ADR,
  public protocol, security, data handling, completion contract, or claim limit
  must change.
