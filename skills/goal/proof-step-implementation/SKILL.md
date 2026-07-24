---
name: proof-step-implementation
description: >-
  Proof-step execution for $goal-proof. Use when an active Goal Pack has a
  runnable proof_step and needs implementation, checks, an append-only evidence
  record, deterministic progress reduction, and continued execution inside the
  protected goal contract.
---

# Run Phase

Execute the largest safe useful slice inside the current smallest falsifiable
path. Use this phase through `$goal-proof`.

## Readiness Gate

`progress.yaml.proof_step` is runnable when it contains concrete values for:

```text
from
target_delta
proof_path
checks
failure_inspection
```

A future command name, repeated objective, or work-item list returns to
`$finding-proof-step` before production edits.

## Run Pass

| Step | Completion criterion |
| --- | --- |
| Refresh | Current Goal Pack state, append-only evidence, relation checks, and relevant authority are read immediately before work starts. |
| Select slice | The slice moves an owner outcome and stays inside allowed scope, claim limit, and stop rules. |
| Implement | Source, migration, harness, docs, or review work reaches the current target delta without changing protected goal fields. |
| Check | Every declared check runs or is inspected; `pass` means its assertion passed, not exit code alone. |
| Record | One evidence JSON object captures completed, blocked, or reviewed work, commands/observations, claims, `not_claimed`, and next action. |
| Reduce | Progress fields are derived from the new evidence and the next falsifiable movement is written when known. |
| Continue | Execution continues while the contract remains valid and another honest path exists; otherwise it transitions to review, needs-plan, blocked, done, or needs-human. |

Use `goal-proof evidence add --apply --check` when append, reduction, and
validation need no intermediate inspection.

## Slice and State Rules

Useful slices include a working screen, API/data path, bug fix, migration seam,
review milestone, or harness that proves the current movement. Helper churn and
notes without claim movement stay inside a larger useful slice.

```text
same proof_step has useful work -> continue
next movement clear -> update proof_step and continue
selected high-risk movement needs reviewed structure -> $write-work-plans
required evidence satisfied -> completion review
no honest next movement -> blocked
protected field must change -> $goal-contracts or needs_human
```

Separate evidence records across distinct proof surfaces. A lower-level result
may support a later run but does not become that later claim.

## Evidence Discipline

Append one JSON object per completed, blocked, or reviewed work item. Historical
records remain unchanged; reinterpretation appends a new record.

- `checks[].status: pass` means the assertion passed.
- Absence claims use an inverted check or explicit allowlist.
- Public schema/terminology migrations inspect skills, references, templates,
  evals, docs, CLI help, tests, fixtures, and active artifacts in scope.
- Broad claim slices retain command/check evidence, proof surface,
  `not_claimed`, and remaining gaps.
- Completion review maps evidence to every `completion.required_evidence` item
  and sets `completion_satisfied: true`.

See [Reference](REFERENCE.md) for evidence-record and state-update shapes.

## Output

```text
goal_pack
work_item
evidence_record
checks
state_update
next_action: proof_step | continue | needs_plan | blocked | review | done | needs_human
```
