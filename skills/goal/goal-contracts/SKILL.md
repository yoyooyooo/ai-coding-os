---
name: goal-contracts
description: >-
  Goal contract authoring for $goal-proof. Use when a selected Goal Pack needs
  goal.yaml created or repaired, or when a discussed solution must become a
  Goal Plan with protected objective, authority, completion, claim limit, and
  stop rules.
---

# Goal Contract Phase

This phase writes the protected human-intent contract at:

```text
docs/goal-proof/goals/<goal-id>/goal.yaml
```

Use it through `$goal-proof`.

## Owned Fields

```text
id
status
intent
objective
guiding_principle
relations
authority_refs
engineering_guidance
constraints
non_goals
completion
claim_limit
stop_rules
agent_authority
evidence_mode
conditional
strict
```

The contract authorizes the goal. `progress.yaml.proof_step` owns the current
executable movement; `evidence.jsonl` owns observed transitions.

## Contract Pass

| Step | Completion criterion |
| --- | --- |
| Ground | Host instructions, docs router, SSoT, Standards, ADRs, Architecture, Roadmap, source, tests, and existing evidence relevant to the objective are identified. |
| Horizon | `objective` is wider than the first proof step and narrow enough for completion evidence, claim limit, and stop rules to close. |
| Authority | Current authority refs and protected human decisions are linked rather than copied. |
| Completion | `completion.signal` and scoped `completion.required_evidence` cover every claim-bearing axis included in the objective. |
| Exclusions | Adjacent surfaces excluded from the goal are explicit in `claim_limit`, `non_goals`, or constraints. |
| Permission | `agent_authority` states revisable fields and fields requiring a human decision. |
| Handoff | `$finding-proof-step` can name an authorized falsifiable path; otherwise status remains `forming` or blocked. |

For public API/schema/protocol/CLI/template/skill changes, authority changes,
security or destructive boundaries, mixed proof surfaces, or multi-evidence
completion, scope completion evidence by claim-bearing slice. Existing v2 fields
carry this coverage; no parallel coverage schema is needed.

## Ready Contract

```text
goal.yaml protects intent and boundaries
progress.yaml.proof_step proves the next movement can be tested
evidence.jsonl stays empty until work runs
```

`status: ready` requires stable protected fields plus an authorized proof step
that can produce or inspect required evidence inside the claim limit. A docs-only
proof step is valid when the target itself is a claim-bearing documentation or
review authority surface with inspectable diffs, links, conflicts, or scans.

## Rules

- Keep `goal.yaml` as a goal contract rather than a work-item tree.
- Link authority and retained source material; store consumed source under
  `docs/goal-proof/sources/` or `notes/`.
- Use relation metadata as lineage, not as a second scheduler or nested state
  system.
- A successor Goal Pack cites predecessor evidence without reopening history.
- Public naming migrations state whether each surface is renamed, retained as a
  documented alias, or excluded from the claim.
- When objective or authority cannot be settled, keep the pack unready and name
  the required decision.

## Output

```text
goal_pack
goal_contract
status: forming | ready | running | blocked | done | retired
completion
claim_limit
next_phase: proof_step | blocked
```

Read [Reference](REFERENCE.md) when authoring field details or using the current
template.
