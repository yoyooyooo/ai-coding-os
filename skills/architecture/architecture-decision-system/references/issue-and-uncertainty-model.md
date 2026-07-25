# Issue and Uncertainty Model

Persist the discovered issue, not the pre-discovery label `unknown-unknown`.

| Kind | Meaning | Typical treatment |
| --- | --- | --- |
| Conflict | Two claims cannot both hold in the same normalized scope | resolve by semantic owner |
| Ambiguity | More than one materially different interpretation remains | elicit or decide |
| Gap | A required decision or fact is absent | investigate, decide, or isolate |
| Assumption | A temporary belief permits bounded progress | owner, scope, expiry, invalidation |
| Hypothesis | An empirical proposition can be tested | probe or Harness |
| Drift | Current source or runtime differs from accepted/current documentation | reconcile or lower claim |
| Violation | Current implementation contradicts a binding Standard or decision | repair or accept exception |
| Evidence Gap | A claim exceeds its proof surface | add proof or lower claim |
| Risk | A possible failure affects commitment or claim boundaries | mitigate, probe, or stop |
| External Dependency | Resolution belongs to a policy, security, legal, vendor, or operational owner | route and localize blocker |
| Migration Debt | A temporary bridge lacks fencing, owner, or deletion gate | repair migration contract |
| Over-abstraction | Mechanism exceeds demonstrated pressure | simplify or retain with evidence |

## Scope Normalization

Before reporting a conflict, compare:

```text
product object and capability
version and temporal plane
market, tenant, and permission scope
host and deployable
consistency domain and authority epoch
wire, persistence, domain, and UI representations
```

Different scopes may coexist.

## Materiality

Escalate an unknown when different answers would materially change product
semantics, accepted facts, permissions, durable data, public compatibility,
irreversible migration, or external effects. Naming and private implementation
choices usually remain Agent decisions.

## False Known

Treat these as high-priority findings:

```text
stale document presented as current
accepted target presented as implemented fact
source behavior presented as product intent
fake/local test presented as real dependency proof
shared crate/package presented as fact-writing authority
a historic ADR presented as active without lifecycle evidence
```

A False Known should become a scoped Drift, Wrong Authority, Stale Claim,
Evidence Gap, or Current/Target confusion finding.
