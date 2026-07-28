# Scenario Examples

These examples show conditional Effect use. They are not a stack maturity path.

## HTTP use case with typed failure

```text
HttpApi handler
  -> decode request
  -> run order.create.use-case.ts
  -> use OrderRepository and Transaction capabilities
  -> map typed outcome to HTTP
```

The API host owns the live Layer graph and Runtime.

## Provider timeout with unknown outcome

```text
PaymentGateway.authorize(operationId)
  -> local timeout fires
  -> return UnknownOutcome(operationId)
  -> reconciliation query runs before retry
```

Do not map the timeout to `PaymentFailed`.

## Bounded worker pool

```text
Stream of jobs
  -> mapEffect with bounded concurrency
  -> provider/database capability
  -> retry only transient idempotent failures
  -> parent Scope owns all Fibers
  -> Queue/Stream lag is observed
```

## Browser subscription

The browser host constructs one Runtime and one socket/Stream. Features consume typed realtime values and update projections through frontend-owned continuity logic.

## Deterministic state machine

A pure transition kernel handles order lifecycle. An Effect Actor interpreter owns mailbox, persistence, provider calls, and restart. This pattern is earned by replay and long-lived state pressure.

## Plain TypeScript alternative

A pure tax calculation or one local mapping remains an ordinary function. Effect is not introduced merely because the surrounding project uses it.

## Related knowledge

- Use [Mechanism selection](mechanism-selection.md) for choosing each shape.
- Use [Default Effect module conventions](default-effect-module-conventions.md) for files.
- Use [Testing Effect](testing-effect.md) for evidence.
- Use the [Effect capability tree example](effect-capability-tree-example.md).
- Return to the [Effect map](../SKILL.md).
