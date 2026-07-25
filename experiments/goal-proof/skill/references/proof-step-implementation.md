# Proof Step Implementation Reference

## Horizons

```text
guiding_principle     far target that must not be lost
goal contract         current human-owned objective and boundaries
proof_step            proof path to sharper clarity
active_work_item      largest safe useful slice inside the proof step
```

Agents may see far, but execute the current proof step.

## Largest Safe Useful Slice

Safe means bounded, explicit, verified, and reversible enough for the current
goal contract. Safe does not mean tiny.

Prefer slices that produce one of:

- working screen;
- working API path;
- working data path;
- real bug fix;
- transition slice;
- milestone review;
- harness that proves the current proof step.

After two helper-sized slices in a row, reorient the proof step or work item. If
the next slice cannot move completion, stop and update progress instead of
pretending progress.

## Run Loop

```text
choose useful slice
  -> capture baseline if needed
  -> implement inside allowed scope
  -> check
  -> add evidence record
  -> apply progress
  -> proof_step / continue / needs_plan / blocked / review / done
```

`goal-proof evidence add --apply --check` is the compact path when evidence
record append, progress update, and validation should happen together.

## Rolling Review Boundary

When a completed proof step creates a new wave that needs a structured contract,
high-risk work plan, or broad proof-step rationale, use the normal Goal Proof
checks unless the user or repository has selected an independent plan-review
method for that boundary.

When an independent review is selected, use `next_action: review` or
`needs_plan`, apply its accepted corrections to the plan and bound proof-step
text, and cite the review evidence. Unresolved findings stay in `blockers`,
`not_claimed`, `remaining_gaps`, or require a human decision.

## Allowed Revisions

Inside the current goal contract, the agent may revise:

- next slice;
- work item order;
- local implementation shape;
- harness strength;
- failure inspection path;
- `progress.yaml.next_action`.

The agent may not silently revise:

- objective;
- authority refs;
- engineering guidance;
- completion;
- claim_limit;
- public API/schema/protocol posture;
- security or private-data handling;
- destructive or irreversible data behavior.

## Evidence Record Rules

Append one JSON object per completed, blocked, or reviewed work item to
`evidence.jsonl`. Do not rewrite history.

Done implementation evidence records need:

```text
schema_version
evidence_id
work_id
type
result
recorded_at
changed_files
checks
evidence
claims
not_claimed
summary
next_action
```

Blocked evidence records need:

```text
schema_version
evidence_id
work_id
type
result: blocked
recorded_at
blocked_by
evidence
summary
next_action: blocked
```

Completion review evidence records need:

```text
schema_version: 2
evidence_id: E999
work_id: W999
type: review
result: done
decision: complete
completion_satisfied: true
claim_evidence
not_claimed
remaining_gaps
summary
next_action: done
```

Implementation evidence record shape:

```json
{
  "schema_version": 2,
  "evidence_id": "E001",
  "work_id": "W001",
  "type": "implementation",
  "result": "done",
  "recorded_at": "2026-05-28T00:00:00Z",
  "changed_files": ["<file-in-allowed-scope>"],
  "checks": [{ "kind": "command", "cmd": "<command>", "status": "pass" }],
  "evidence": ["<evidence>"],
  "claims": ["<claim>"],
  "not_claimed": [],
  "summary": "",
  "next_action": "continue"
}
```

When a real cross-owner handoff consumes a version-2 Evidence Envelope, preserve
its available `source_ref`, `proof_surface`, `claim_ceiling`, `observed`,
`supports`, `not_proven`, and `evidence_refs` before adding Goal-local
`claims` or `not_claimed`. Ordinary implementation evidence does not need empty
copies of those optional fields.

`checks[].status: "pass"` means the check's assertion passed. For absence
claims, use an inverted no-match command such as `! rg ...` or record an
explicit allowlist of intentional matches.

For schema or terminology migrations, include active surfaces in evidence:
templates, references, agents, evals, CLI help/flags, README examples,
tests/fixtures, and active Goal Pack artifacts.

## Recovery

If verification fails:

1. inspect the failure path named in `progress.yaml.proof_step`;
2. make a bounded fix inside allowed scope if obvious;
3. append a blocked evidence record if recovery would cross a protected boundary;
4. update `progress.yaml.next_action`.
