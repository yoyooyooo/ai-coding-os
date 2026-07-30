# Use Cases, Transactions, and Idempotency

A use case is the governed application operation that accepts intent, enforces product rules, coordinates capabilities, and commits an authoritative result.

## Command, use case, Outcome, and Receipt

```text
Command     immutable intent and stable operation identity
Use case    authorization, validation, policy, coordination, and materialization
Outcome     complete discriminated result of this invocation
Receipt     smallest stable operation evidence when replay/reconciliation needs it
```

A Command is not proof that the change happened. An Outcome is not necessarily durable evidence. A Receipt is not the name for every success and failure branch.

Example semantic shape:

```text
SubmitOutcome
  Accepted { receipt: SubmitReceipt }
  Incomplete { gaps }
  InvalidState { current }
  NotAccessible
  VersionConflict { currentVersion }
  PendingExternalConfirmation { operationId }
```

Keep these types beside the use case while they are local. Extract independent files only after reuse, public-contract, navigation, or machine-consumer pressure.

## Use-case boundary

A use case may:

- load authoritative state;
- validate command and permission;
- apply domain policy and invariants;
- coordinate application-owned Ports;
- define and enter the required consistency scope;
- commit business rows and event/audit/outbox data;
- return a use-case-specific Outcome.

It should not depend on HTTP request objects, provider SDK response shapes, UI state, or live adapter selection.

## Transaction scope

> **A transaction capability belongs to the consistency scope, not automatically to the module name.**

The transaction boundary should match the product invariant, not repository method count. A process-global ORM client is not a transaction model.

When one operation touches several repositories or capabilities, use a coherent mechanism controlled by the use case or consistency owner:

```text
explicit transaction context
transaction-scoped repositories
application Unit of Work
store-native transaction program behind an application capability
```

Do not create `<module>.transaction.port.ts` for symmetry. Extract a transaction capability when its contract, participants, implementation, reuse, or test surface is independently meaningful. A future cross-capability operation must be able to join the same consistency scope without depending on one module's private adapter.

Database constraints and migrations should protect invariants that remain true under concurrency. Application checks alone do not prove uniqueness, compare-and-set, or exactly-one-attempt properties.

## External effects

A local database transaction cannot atomically include an external provider that offers no compatible transaction. Use patterns such as:

```text
outbox and asynchronous dispatch
idempotent provider operation identity
state machine with pending/confirmed/failed/unknown
compensation when the domain allows it
reconciliation and audit
```

Do not label a compensating workflow a rollback when the external world has already changed.

## Idempotency

Idempotency is an operation semantic before it is a Port or file. Define:

```text
operation scope and command type
actor/tenant/resource scope when relevant
stable key for the same intent
request fingerprint or equivalent payload identity
where the accepted result is remembered
how long the identity remains valid
what happens when payload differs under the same key
whether the external provider also deduplicates
how pending or unknown outcome is reconciled
```

A successful replay of the same accepted intent normally returns the prior accepted Outcome or equivalent Receipt, optionally marked `replayed: true`. It is not automatically a product rejection. Reusing the same key for a different fingerprint is a distinct conflict.

Extract an idempotency capability when storage, provider integration, cross-operation reuse, or independently changing retention/replay policy earns it. Do not generate one module-local idempotency Port by default.

"Retry-safe" is not a property of a function name.

## Receipt design

Persist only evidence needed for stable replay or reconciliation, for example:

```text
operation identity
accepted fact identifier
resulting version or causal frontier
commit/provider reference
timestamp
minimal response fields that remain contractually stable
```

Do not persist a full mutable aggregate snapshot by default. Large receipts leak sensitive data, couple replay to schema evolution, and may present stale state as current truth.

## Unknown outcome

A timeout or interruption means local waiting ended. The external effect or transaction commit may have succeeded. Preserve operation identity, expose the uncertain state, and reconcile before retrying a non-idempotent effect.

## Outcome types

Prefer discriminated Outcomes that reflect the use case:

```text
accepted
rejected by product rule
not authorized or not accessible
conflict / stale version
already completed
pending external confirmation
unknown outcome requiring reconciliation
```

Keep infrastructure failure distinct from a product Outcome when callers or operators need different handling. Avoid one giant DTO with optional fields for every operation.

## Related knowledge

- Use [Fact authority and candidate boundaries](fact-authority-and-candidate-boundaries.md) for the final writer.
- Use [Source topology and semantic naming](source-topology-and-semantic-naming.md) for role-to-file pressure.
- Use [Capability boundaries and adapters](capability-boundaries-and-adapters.md) for external effects.
- Use [Consistency, events, and shared state](consistency-events-and-shared-state.md) for outbox and Saga choices.
- Use `$effect-best-practices` for interruption, retry, and resource mechanisms.
- Use `$product-harness-system` for duplicate, timeout, restart, replay, and migration observations.
- Return to the [EAA map](../SKILL.md).
