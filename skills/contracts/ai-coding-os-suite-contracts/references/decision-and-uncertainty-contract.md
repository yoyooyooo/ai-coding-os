# Decision and Uncertainty Contract

This is a minimal cross-Skill vocabulary. Domain meaning remains with the
question-scoped semantic owner.

```text
scope
  the object, capability, version, market, host, environment, and claim boundary

claim
  a statement whose Authority, basis, temporal plane, and evidence can be named

basis
  accepted | observed | source-derived | inferred | assumed | unknown

temporal plane
  current | accepted-target | future | historical

issue
  conflict | ambiguity | gap | assumption | hypothesis | drift | violation
  | evidence-gap | risk | external-dependency

decision owner
  the accountable owner allowed to select or accept the answer

decision right
  agent-may-decide | bounded-assumption | owner-decision-required | stop

blocking scope
  only the commitments affected by the unresolved issue

invalidates_when
  source, version, decision, migration, environment, evidence, or time condition
  that makes the claim or assumption stale
```

## Guardrails

```text
unknown to whom, about which claim, and in which scope?
assumption must not silently cross its commitment boundary
not_proven is an evidence state, not product ambiguity
source observation is not accepted intent
a binding constraint is not automatically semantic ownership
an issue is not a global workflow state
```

Use domain-qualified terms such as `fact authority`, `documentation Authority`,
`product decision owner`, `resource owner`, and `execution owner` rather than one
unqualified global owner field.
