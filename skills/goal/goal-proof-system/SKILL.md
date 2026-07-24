---
name: goal-proof
description: >-
  Goal Pack method for durable objectives tracked through goal.yaml,
  progress.yaml, evidence.jsonl, proof_step, and completion review. Use only
  when the user explicitly selects Goal Proof or Goal Pack, or the repository
  declares $goal-proof as the active execution method for the workstream.
---

# Goal Proof System

Goal Proof turns an explicitly selected durable objective into evidence-backed
state transitions:

```text
human intent -> goal contract -> proof_step -> evidence -> next_action
```

> **Roll past the current plan, not past the goal contract.**

Task size alone does not activate this method. Work with one same-turn evidence
path stays inline unless the user or repository selects a Goal Pack.

## Ownership

```text
Owns:
  Goal Pack lifecycle
  goal contract and protected authority
  current proof_step and work-item state
  append-only evidence records
  Goal relations metadata
  completion review

Adjacent owners:
  goal contract authoring -> $goal-contracts
  runnable proof-step discovery -> $finding-proof-step
  implementation and evidence reduction -> $proof-step-implementation
  selected high-risk work plan -> $write-work-plans
  docs placement -> $docs-governance
  interface trace -> $interface-capability-planning
  shared harness architecture -> $product-harness-system
  command proof -> $headless-product-harness
  browser-visible proof -> $ui-product-harness
```

Product truth, docs-layer doctrine, interface semantics, and harness
implementation remain with their owners.

## Goal Pack

```text
docs/goal-proof/
  README.md
  inbox/
  sources/
  goals/<goal-id>/
    goal.yaml
    progress.yaml
    evidence.jsonl
    plans/<work_id>.md             # only when needs_plan
    interface-capabilities.yaml    # optional reference companion
    product-harness.yaml           # optional reference companion
    notes/
```

```text
goal.yaml       protected objective, authority, completion, claim_limit, stops
progress.yaml   current proof_step, work items, blockers, last check, next_action
evidence.jsonl  append-only transition evidence
plans/**        pre-reviewed structure for selected high-risk work only
notes/**        long context that does not own current state
```

A “Goal Plan” request compiles to this Goal Pack rather than a parallel prose
plan.

## Ready Gate

```text
stable goal contract
+ authorized proof_step can produce or inspect completion.required_evidence
  within claim_limit
= ready Goal Pack
```

A roadmap paragraph, work-item list, future command name, or planning preface is
not a ready proof path.

## Operating Loop

| Step | Completion criterion |
| --- | --- |
| Activate | Explicit user selection or repository adoption is confirmed; inline work is not inflated into a Goal Pack. |
| Contract | `goal.yaml` has stable objective, authority refs, constraints, completion evidence, claim limit, stop rules, and agent authority. |
| Calibrate | `progress.yaml.proof_step` names `from`, `target_delta`, runnable/inspectable `proof_path`, checks, and first failure inspection. |
| Execute | The largest safe useful slice inside the proof step runs and its checks produce observations. |
| Record | One append-only evidence record maps the completed or blocked slice to checks, claims, `not_claimed`, and `next_action`. |
| Reduce | Evidence updates progress deterministically; the next falsifiable movement is selected while protected fields remain stable. |
| Complete | A review evidence record maps the evidence chain to every `completion.required_evidence` item and sets `completion_satisfied: true`. |

Canonical CLI loop:

```text
check -> inspect -> work brief -> work -> evidence add -> apply -> check
```

Use `goal-proof evidence add --apply --check` when append, state reduction, and
validation can occur atomically.

## Rolling Rule

One proof step is the current falsifiable movement, not the goal horizon. After
evidence succeeds:

```text
same movement still has useful work -> continue
next movement is clear -> write next proof_step and continue
selected high-risk movement needs reviewed structure -> needs_plan
required evidence is satisfied -> completion review
no honest path -> blocked
protected goal field must change -> needs_human or contract repair
```

Separate evidence records when claims move across distinct proof surfaces such
as interface-headless, render, browser, headless product, real database, or
production-near execution.

## Claim Coverage

For public surfaces, schema/protocol/CLI/template/skill changes, authority
changes, security/destructive boundaries, mixed proof surfaces, or broad
completion, use existing v2 fields to keep claim slices explicit:

```text
completion.required_evidence  scoped required slices
claim_limit / non_goals       excluded adjacent claims
proof_step                    current slice and proof surface
evidence claims/not_claimed   proven slice and exclusions
completion review             claim-to-evidence mapping and remaining gaps
```

A successful command supports only the assertion it actually checked.
`not_proven` and changed surfaces remain narrative unless the schema, templates,
and checker explicitly add them.

## Stop Boundary

Continue inside the protected contract. Stop or repair the contract when the
work requires changing objective, completion, claim limit, authority refs, stop
rules, or another field listed in `agent_authority.requires_human_decision`; or
when no honest path exists; or when permission, private data, security,
destructive action, compliance, or public compatibility needs a new decision.

Historical `evidence.jsonl` records remain append-only.

## Read When Needed

- Placing inbox, source, Goal Pack, companions, or successor relations: [Artifact Routing](references/artifact-routing.md)
- Initializing Goal Proof in a repository: [Bootstrap](references/bootstrap.md)
- Running CLI commands: [CLI](references/cli.md)
- Inspecting cross-pack relations: [Goal Relations](references/goal-relations.md)
- Understanding checker behavior: [Checker Rules](references/checker-rules.md)
- Migrating schema terminology: [Schema Terminology Migration](references/schema-terminology-migration.md)
- Seeing complete examples: [Examples](EXAMPLES.md)
