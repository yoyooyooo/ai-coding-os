---
name: finding-proof-step
description: >-
  Proof-step discovery for $goal-proof. Use when a selected Goal Pack needs its
  first or next falsifiable runnable movement written to
  progress.yaml.proof_step, or when the current path must become honestly
  blocked.
---

# Proof Step Phase

A proof step connects the current goal state to a sharper state through an
inspectable result:

```text
source state -> proof_path -> checks -> evidence -> sharper state
```

Use this phase through `$goal-proof`. Find one path; avoid precomputing the
whole work graph.

## Owned Fields

```text
proof_step.from
proof_step.target_delta
proof_step.proof_path
proof_step.checks
proof_step.failure_inspection
```

## Calibration Pass

| Step | Completion criterion |
| --- | --- |
| Ground | `goal.yaml`, current progress/evidence, relevant relation evidence, and source authority for the next movement are read. |
| State | `from` names a concrete current state rather than a slogan or roadmap row. |
| Candidates | When route choice matters, two or three plausible proof paths are compared by falsifiability, cost, authority, and claim fit. |
| Select | `target_delta` is the smallest useful claim slice and the chosen path can produce or falsify it. |
| Specify | Input/fixture/action, positive observations, `not_claimed`, checks, and first failure-inspection location are explicit. |
| Bind | The path can produce or inspect a scoped part of `completion.required_evidence` inside `claim_limit`. |
| Write | `progress.yaml.proof_step` contains all five owned fields; the first work item is activated only when execution is clear. |

## Proof-Surface Menu

```text
static or boundary check
offline fixture
replay
adapter or projection
real database and restart
real runtime or manual acceptance
interface-headless
render wiring
browser-visible
production-near
```

Select the surface required by the current claim. Lower surfaces support only
their own observations; higher surfaces are justified when the claim depends on
their runtime behavior.

A future command name becomes a proof path only after its input, execution
contract, expected observations, failure status, and inspection location are
specified. If command creation is itself the target, those conditions define
its proof.

## Rolling Boundary

After evidence succeeds, select the next smallest falsifiable movement without
changing objective, completion, claim limit, stop rules, or authority refs.
When evidence shows the protected contract is no longer suitable, return to
`$goal-contracts` or request the protected decision.

For mixed or broad claims, place the current slice and proof surface in
`target_delta`, preserve adjacent exclusions in `proof_path`, and carry relevant
open surfaces into completion gaps.

## No Honest Path

Record the missing bridge rather than inventing work:

```text
missing_authority
missing_harness
blocked_by
smallest_bridge_needed
human_decision_needed
```

Then set `next_action: blocked` or return to `$goal-contracts`.

## Output

```text
goal_pack
proof_step:
  from:
  target_delta:
  proof_path:
  checks:
  failure_inspection:
next_phase: run | needs_plan | blocked
```

Read [Workflow Details](references/workflow-details.md) when candidate comparison
or state encoding needs more detail, [Route Archetypes](references/route-archetypes.md)
for common path shapes, and [Implementation Brief Template](references/implementation-brief-template.md)
when the selected movement needs a compact execution brief.
