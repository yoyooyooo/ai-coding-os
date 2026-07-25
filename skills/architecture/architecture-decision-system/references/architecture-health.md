# Architecture Health

Architecture Health is a time-bounded derivation:

```text
accepted architecture claims
+ observed source/schema/runtime territory
+ owner-scoped rules
+ evidence
+ assumptions and invalidation conditions
= current health findings
```

It is not a permanent field in ADIR and is not reduced to one score by default.

## Dimensions

```text
Authority Integrity       final writers, consistency domains, epochs, forbidden writers
Decision Closure          material decisions and commitment boundaries
Map–Territory Alignment   accepted map versus source/runtime observations
Assumption Hygiene        owner, scope, expiry, invalidation, reversibility
Boundary Integrity        dependency, visibility, adapter, host, trust boundaries
Temporal Integrity        transaction, idempotency, retry, cancellation, shutdown
Evolution Integrity       bridge, fencing, migration, deletion gate
Evidence Adequacy         proof surface versus claim ceiling
Agent Legibility          discoverability of owner, entry, composition, proof, unknowns
Knowledge Freshness       basis age and re-grounding triggers
```

## Finding Shape

```text
status: healthy | watch | degraded | critical | unknown | not_applicable
severity
basis_refs
applicable_rule
affected_scope
decision_needed
smallest_repair
smallest_verification
not_proven
invalidates_when
evaluated_at
```

`unknown` is not automatically unhealthy; `not_proven` is not failure; the
absence of Outbox, Port, service, or package is not a defect unless pressure
requires it.

## Reporting

Lead with critical and decision-bearing findings. State the observation basis
instead of an unsupported confidence percentage. A report may be persisted in a
project report Home, while a current architecture view only links to it and
retains its claim ceiling.
