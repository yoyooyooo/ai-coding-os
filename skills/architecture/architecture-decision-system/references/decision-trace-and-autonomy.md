# Decision Trace and Autonomy

A Decision Trace records the reviewable result, not private chain of thought.

```text
question and normalized scope
project facts and source observations used
applicable owner rules and binding constraints
material options considered
selected option and concise rationale
rejected options and concise reasons
unresolved boundary and decision owner
verification path and invalidation trigger
```

## Bounded Assumption

A durable assumption requires:

```text
owner
scope
reason it is safe enough for current work
commitments it cannot cross
expiry or invalidates_when
replacement decision or probe
```

## Optional Autonomy Envelope

Use only when long-running, cross-Agent, high-risk, or migration work benefits:

```yaml
settled: []
residual_material_unknowns: []
decision_rights:
  agent_may_decide: []
  bounded_assumptions: []
  owner_decision_required: []
stop_lines: []
proof_obligations: []
safe_to_proceed: exploration | reversible-implementation | commitment | claim
```

The envelope is a local projection. It does not create a new project Authority.
