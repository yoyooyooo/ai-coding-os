# Use Cases, Transactions, and Idempotency

A use case is the governed application operation that accepts intent, enforces product rules, coordinates capabilities, and commits an authoritative result.

## Command, use case, and result

```text
Command     immutable intent and operation identity
Use case    authorization, validation, policy, coordination, and materialization
Outcome     explicit accepted result or modeled failure
Receipt     durable operation identity or evidence when reconciliation is needed
```

A Command is not proof that the change happened.

## Use-case boundary

A use case may:

- load authoritative state;
- validate command and permission;
- apply domain policy and invariants;
- coordinate application-owned Ports;
- commit business rows and event/audit/outbox data;
- return a use-case-specific outcome.

It should not depend on HTTP request objects, provider SDK response shapes, UI state, or live adapter selection.

## Transaction scope

The transaction boundary should match the product invariant, not repository method count. A process-global ORM client is not a transaction model.

When one operation touches several repositories, pass an explicit transaction context or unit of work controlled by the use case or transaction capability.

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

Idempotency requires a stable operation identity and a defined scope. Ask:

```text
what key identifies the same intent
where the result is remembered
how long the key remains valid
what happens when payload differs under the same key
whether the external provider also deduplicates
how an unknown outcome is reconciled
```

"Retry-safe" is not a property of a function name.

## Unknown outcome

A timeout or interruption means local waiting ended. The external effect may have succeeded. Preserve operation identity and reconcile before retrying a non-idempotent effect.

## Outcome types

Prefer discriminated outcomes that reflect the use case:

```text
accepted
rejected by product rule
not authorized
conflict / stale version
already completed
pending external confirmation
unknown outcome requiring reconciliation
```

Avoid one giant DTO with optional fields for every operation.

## Related knowledge

- Use [Fact authority and candidate boundaries](fact-authority-and-candidate-boundaries.md) for the final writer.
- Use [Capability boundaries and adapters](capability-boundaries-and-adapters.md) for external effects.
- Use [Consistency, events, and shared state](consistency-events-and-shared-state.md) for outbox and Saga choices.
- Use `$effect-best-practices` for interruption, retry, and resource mechanisms.
- Use `$product-harness-system` for duplicate, timeout, restart, and replay scenarios.
- Return to the [EAA map](../SKILL.md).
