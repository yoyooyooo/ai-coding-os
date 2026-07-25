---
name: goal-proof
description: Experimental Goal Pack method for durable objectives, proof steps, append-only evidence, and completion review.
disable-model-invocation: true
---

# Goal Proof

Goal Proof is a co-located early experiment, not an AI Coding OS default. Use it
only when the user explicitly chooses `$goal-proof` or a repository already
names a Goal Pack as the current execution method.

> **Roll past the current plan, not past the goal contract.**

A Goal Pack turns one durable objective into evidence-backed state transitions:

```text
goal contract -> proof step -> evidence -> next action -> completion review
```

Task size does not activate this method. A workstream already owned by a tracker,
ticket system, or another execution method keeps that owner rather than gaining
a parallel Goal ledger.

## Ownership

```text
Owns:
  goal.yaml protected intent and completion contract
  progress.yaml current proof step and work state
  evidence.jsonl append-only transition evidence
  optional high-risk work plans
  Goal relations metadata
  completion review

Does not own:
  product meaning, documentation placement, architecture, proof implementation,
  release state, tracker state, or another execution method's dependency graph
```

Project authorities decide product, policy, architecture, security, and public
contract questions. Harnesses and tests supply bounded observations; the Goal
contract alone decides whether they satisfy Goal completion.

## Goal Pack

Resolve one concrete `goal_pack_root` from an explicit path or repository
convention. Use this fallback only when no project Home exists:

```text
.goal-proof/goals/<goal-id>/
```

```text
goal.yaml       objective, authority refs, completion, claim limit, stop rules
progress.yaml   proof step, work items, blockers, last check, next action
evidence.jsonl  append-only implementation, blocked, planning, and review records
plans/**        reviewed structure for selected high-risk work only
notes/**        long context that does not own current state
```

A request for a “Goal Plan” creates or updates this pack instead of a second
prose planning system.

## Stateful Method

The ordering below is part of this experiment's state protocol.

| State transition | Completion criterion |
| --- | --- |
| Activate | User or repository selection is explicit, one `goal_pack_root` is resolved, and no competing execution ledger owns the same workstream. |
| Contract | `goal.yaml` protects an observable objective, current authority refs, constraints, completion evidence, claim limit, stop rules, and human decision fields. |
| Calibrate | `progress.yaml.proof_step` names the current state, target delta, runnable or inspectable proof path, checks, and first failure inspection. |
| Execute | The largest safe useful slice inside the proof step runs without changing protected fields. |
| Record | One evidence object records checks, observations, bounded claims, exclusions, gaps, and next action without rewriting history. |
| Reduce | Progress is derived from fresh evidence and either continues, selects the next falsifiable movement, requests a high-risk plan, blocks, or enters review. |
| Complete | A review record maps every `completion.required_evidence` item to evidence and sets `completion_satisfied: true`. |

Ready means both the protected contract and an authorized falsifiable proof step
exist. A work-item list, roadmap paragraph, future command name, or planning
preface is not readiness evidence.

## Rolling Boundary

```text
same proof step still has useful work -> continue
next movement is clear             -> replace proof_step and continue
high-risk movement needs structure -> needs_plan
required evidence is satisfied     -> completion review
no honest path                     -> blocked
protected field must change        -> needs_human or contract repair
```

Protected fields include objective, completion, claim limit, authority refs,
stop rules, and any project-declared human decision. Historical evidence remains
append-only.

When imported evidence has a source reference, proof surface, dependency reality,
claim ceiling, observations, supported conclusions, or unproven neighbors,
preserve those distinctions. A passing Harness path never implies Goal completion.

## Conditional References

- Creating or repairing `goal.yaml`: [Goal Contract](references/goal-contracts.md)
- Choosing the first or next falsifiable movement: [Proof Step Details](references/proof-step-details.md) and [Route Archetypes](references/proof-step-archetypes.md)
- Executing, recording evidence, and reducing progress: [Proof Step Implementation](references/proof-step-implementation.md)
- Planning one selected high-risk work item: [Work Plan](references/work-plan.md) and [Plan Review](references/work-plan-review.md)
- Placing packs, sources, companions, or successors: [Artifact Routing](references/artifact-routing.md)
- Initial repository adoption: [Bootstrap](references/bootstrap.md)
- CLI commands and offline fallback: [CLI](references/cli.md)
- Relation metadata: [Goal Relations](references/goal-relations.md)
- Checker and schema compatibility: [Checker Rules](references/checker-rules.md)
- Changing schema, terms, CLI language, or Goal Pack home: [Schema And Terminology Migration](references/schema-terminology-migration.md)
- Complete examples: [Examples](references/examples.md)

## Stop Boundary

Stop or repair the contract when no honest path exists, a protected field must
change, or permission, private data, security, destructive action, compliance,
public compatibility, or irreversible external effects need a new decision.

## Output

```text
goal_pack_root
goal_contract_state
current_proof_step
latest_evidence_and_claim_ceiling
next_action
not_claimed
remaining_gaps
```
