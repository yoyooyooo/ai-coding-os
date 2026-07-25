# Work Plan Reference

Use this only for a selected Goal Pack work item that needs pre-reviewed
execution structure.

## Path

```text
<goal_pack_root>/plans/<work_id>.md
```

`$goal-proof` resolves `goal_pack_root`; the writer fallback is
`.goal-proof/goals/<goal-id>/`. CLI 0.2.x also reads the former
`docs/goal-proof/goals/<goal-id>/` location. The plan lives inside the Goal Pack,
is referenced from the selected work item when useful, and `allowed_scope`
includes the plan file when the work item writes or updates it.

## Plan Template

```markdown
# <Goal ID> Work Plan

## Goal Pack

- goal: `<goal_pack_root>/goal.yaml`
- progress: `<goal_pack_root>/progress.yaml`
- work item: `<W###>`
- plan: `<goal_pack_root>/plans/<work_id>.md`

## Protected Boundary

- objective:
- authority:
- engineering_guidance:
- claim_limit:
- stop_if:

## Allowed Scope

- Create:
- Modify:
- Test:

## Verification

- command/manual:
- expected:
- failure inspection:
- no-match or allowlist checks for retired terms when absence is claimed
- public-surface rename/alias checks when schema fields are renamed

## Plan Optimality Review

- review gate:
- review object:
- reviewer contract:
- adopted correction plan:
- unresolved findings:
- ledger/evidence refs:

## Execution Chunks

### Chunk 1: <name>

- [ ] Write or update focused evidence.
- [ ] Implement inside allowed scope.
- [ ] Run checks.
- [ ] Append evidence record.
- [ ] Apply progress.

## Evidence Record Requirements

```json
{
  "schema_version": 2,
  "evidence_id": "E001",
  "work_id": "<W###>",
  "type": "planning",
  "result": "done",
  "recorded_at": "<ISO-8601-UTC>",
  "changed_files": ["<goal_pack_root>/plans/<work_id>.md"],
  "checks": [{ "kind": "command", "cmd": "<review command or manual gate>", "status": "pass" }],
  "evidence": ["<plan review evidence>"],
  "claims": ["<claim limited to plan readiness>"],
  "not_claimed": [],
  "summary": "",
  "next_action": "continue"
}
```

## Handoff

- ready_for_run:
- blocked_by:
- next_action:
```

## Review Gate

The plan is valid only if it preserves the Goal Pack goal contract and can
return to implementation without changing fields listed in
`agent_authority.requires_human_decision`.

For high-risk wave boundaries, an independent plan-review method is optional.
When the user, repository, or active work plan explicitly selects one, the plan
must pass that gate before `ready_for_run: true`. Passing means reviewers have
no unresolved findings, or residual risks are explicitly moved to
`not_claimed`, `remaining_gaps`, `blockers`, or a human decision; accepted
corrections are applied to the plan and any bound proof-step text; and review or
planning evidence cites the reviewer output.

`ready_for_run: true` also requires `progress.yaml.proof_step` to remain
falsifiable after the plan. If the plan changes the evidence path, update the
proof step before returning to implementation.

For schema, terminology, or command-language migrations, the plan should include
an active-surface pass: skill bodies, references, templates, agents, evals,
README/package docs, CLI help/flags, tests/fixtures, and active Goal Pack
artifacts. It should also state whether public names are renamed, kept as
documented aliases, or recorded as `remaining_gaps`.
