---
name: write-work-plans
description: >-
  High-risk work-plan authoring for $goal-proof. Use when a selected Goal Pack
  work item needs plans/<work_id>.md because execution changes a public
  API/schema/protocol, irreversible data, security or permissions, a broad
  transition, strict multi-agent sequencing, or an expensive rollback path.
---

# Plan Required Phase

Write one reviewable implementation plan for a selected high-risk work item:

```text
docs/goal-proof/goals/<goal-id>/plans/<work_id>.md
```

Use this phase through `$goal-proof`. The plan returns to the current proof step;
it is neither a second Goal Pack nor a product or roadmap authority.

## Admission

Use a work plan when at least one condition materially changes execution:

- transition or deletion has broad blast radius;
- public API, schema, protocol, persisted contract, or command language changes;
- data, credentials, permissions, security, or an external effect is hard to
  reverse;
- multiple agents require strict ordering or disjoint write scopes;
- a wrong first implementation is expensive to unwind.

Ordinary rolling work stays in `progress.yaml.proof_step`.

## Required Inputs

```text
goal_pack
goal.claim_limit
progress.proof_step
work_item.objective
work_item.allowed_scope
work_item.checks
work_item.stop_if
authority_refs
```

Protected fields stay unchanged; any required change routes to `$goal-contracts`
or the human decision named by the contract.

## Planning Pass

| Step | Completion criterion |
| --- | --- |
| Admit | A concrete high-risk condition justifies a separate plan. |
| Ground | Every required input and affected authority/public surface is identified. |
| Sequence | Transitions, write scopes, compatibility bridges, rollback limits, and ownership handoffs are ordered without creating a second work tree. |
| Verify | Each stage has a falsifiable check, expected evidence record, and first failure-inspection point. |
| Cover | Schema/terminology changes include all active skills, references, templates, evals, docs, CLI, tests, fixtures, and active artifacts in scope. |
| Handoff | `ready_for_run: true` only when `progress.yaml.proof_step` names the runnable next movement and all required plan review findings are resolved. |

For renamed public fields, record one decision per surface: rename now, retain a
documented compatibility alias, or leave an explicit remaining gap.

Use [Reference](REFERENCE.md) for the full template and [Examples](EXAMPLES.md)
for a worked plan. `plan-reviewer-prompt.md` is optional when the repository has
selected an independent plan review.

## Output

```text
implementation_plan
path
goal_pack
work_item
ready_for_run: true | false
blocked_by
next_phase: run | blocked
```
