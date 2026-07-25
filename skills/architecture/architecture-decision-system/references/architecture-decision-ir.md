# Architecture Decision IR

Architecture Decision IR (ADIR) is a partial, reference-oriented graph for one
architecture question or durable slice. It is not a complete model of the
repository.

## Minimal Envelope

```text
scope
  object / capability / vertical slice
  version / market / tenant / environment / host when relevant

claims
  meaning
  semantic_owner
  authority_ref
  temporal_plane
  knowledge_basis
  evidence_state
  invalidates_when

relations
  owns / writes / reads / materializes / invokes / depends-on
  selected-by / projects-to / constrained-by / evidenced-by
  supersedes / migrates-to / violates

issues
  affected claims, impact, treatment, owner, blocking scope

decisions
  selected option, concise rationale, rejected options, verification path
```

## Independent Axes

Do not compress these into one `status` field:

```text
authority_state   accepted | recommended | none
knowledge_basis   observed | source-derived | inferred | assumed | unknown
temporal_plane    current | accepted-target | future
evidence_state    not-proven | partial | verified
lifecycle         draft | in-review | accepted | superseded | archived
```

## Owner-Qualified Node Kinds

Examples:

```text
eaa.fact-authority
eaa.consistency-domain
eaa.use-case
eaa.capability-port
eaa.composition-profile
eaa.migration-bridge

frontend.state-owner
frontend.intent
frontend.projection
frontend.reconciliation-path

effect.service
effect.layer-binding
effect.runtime-owner
effect.scope
```

The owner prefix preserves semantic ownership. The Architecture Decision System
may connect nodes but does not redefine them.

## Reference, Do Not Clone

Prefer:

```yaml
claim:
  meaning: Orders is the final writer of Order.status
  authority_ref: docs/architecture/order-boundaries.md#order-status
  source_observation_refs:
    - src/orders/complete.rs
  evidence_refs:
    - reports/order-restart-result.json
```

over copying the full ADR, source excerpt, and test report into the IR.

## Partial Information

Allowed values include `unknown`, `not_applicable`, `contested`, and
`not_proven`. A missing answer is not permission to invent a writer, transaction,
port, migration, or proof surface.
