# Plan Required Examples

## High-Risk Slice

```markdown
# public-relay-deployment-readiness Implementation Plan

## Goal Pack

- goal: `<goal_pack_root>/goal.yaml`
- progress: `<goal_pack_root>/progress.yaml`
- work item: `W002`
- plan: `<goal_pack_root>/plans/<work_id>.md`

## Protected Boundary

- objective: prove a deployment-readiness path for the public relay
- claim_limit: claim only readiness evidence inside this Goal Pack
- stop_if: needs public API, security, or deployment authority change

## Allowed Scope

- Modify: `<goal_pack_root>/**`

## Verification

- `bun run check`
- `goal-proof check <goal_pack_root>`

## Execution Chunks

1. Confirm authority and claim_limit.
2. Define a runnable readiness harness.
3. Execute the smallest readiness proof.
4. Append evidence record and apply state.
```
