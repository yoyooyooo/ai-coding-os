# Product Capability Example: Exception Resolution

This example uses the default capability shape selectively.

## Outcome and user context

Regional operations leads need to receive high-risk exceptions, accept responsibility, resolve them with evidence, and escalate unresolved work before the SLA is breached.

## Actors and responsibilities

| Actor | Responsibility | Authority |
| --- | --- | --- |
| Operations lead | owns and resolves assigned exceptions | may accept assignment and submit resolution |
| Regional manager | reallocates and escalates work | may reassign and accept residual operational risk |
| Auditor | reviews history and evidence | read-only; cannot change resolution facts |

## Objects, states, and invariants

```text
ExceptionCase
  identity
  severity
  assignment
  resolution state
  evidence references
  deadline
```

Invariant: one active case has at most one accountable assignee. Reassignment preserves history.

## Actions, rules, permissions, and policy

- An operations lead may accept only a case visible to their region.
- A manager may reassign an unresolved case.
- High-severity cases require at least one evidence reference before resolution.
- Escalation threshold is policy, not a semantic invariant.

## Workflow, exceptions, and recovery

```text
created -> assigned -> accepted -> resolved
                    \-> escalated
```

If submission times out, the interface must preserve the operation ID and reconcile before allowing a duplicate resolution.

## Scope and non-goals

In scope: assignment, acceptance, resolution, evidence link, escalation, history.

Not in scope: authoring the upstream anomaly rule or replacing the external case source.

## Quality and acceptance boundary

- no accepted resolution is lost;
- duplicate submission does not create two resolution facts;
- keyboard users can complete the flow;
- unauthorized regions cannot discover case details;
- reload restores authoritative state and pending-operation status.

## Interface obligations

The surface must show ownership, deadline, evidence requirement, pending/accepted/conflict state, and a recovery path after timeout.

## Related Skills

- `$product-definition`
- `$frontend-architecture`
- `$evolvable-application-architecture`
