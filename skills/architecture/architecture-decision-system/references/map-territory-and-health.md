# Map–Territory Reconciliation

Architecture claims are maps. Source, schema, runtime composition, migration state, and executed evidence are parts of the territory. Reconcile them without granting any one representation universal precedence.

## Compare by Claim

For each material claim, distinguish:

```text
normative basis       accepted Product / Standard / ADR / architecture decision
observed basis        source / schema / migration / lockfile / runtime observation
knowledge basis       accepted | observed | source-derived | inferred | assumed | unknown
temporal plane        current | accepted-target | future
evidence state        not-proven | partial | verified
```

## Findings

Use specific findings rather than a generic mismatch:

```text
scope difference
representation difference
current / target confusion
stale claim
wrong semantic owner
source drift
implementation gap
unaccepted implementation
evidence gap
bridge or migration debt
```

A `False Known` becomes a concrete finding; it is not retained as a trusted input.

## Diff

An Architecture Diff compares the decision-bearing meaning of two scopes or times:

```text
claim added / removed / changed
authority or writer changed
commitment boundary changed
current -> target transition
bridge / fence / deletion gate changed
proof obligation or claim ceiling changed
```

Do not treat file movement or formatting alone as an architecture change.

Health derivation is owned by [Architecture Health](architecture-health.md).
