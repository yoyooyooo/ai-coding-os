# Scenario Examples

These examples show how semantic roles and portable defaults combine. They are not mandatory blueprints.

## Order creation in a TypeScript API

```text
POST /orders
  -> order.http.handlers.ts
  -> order.create.use-case.ts
  -> order.repository.port.ts
  -> order.repository.postgres.live.ts
  -> committed order + outbox
  -> order.created event
```

`api.composition.ts` selects the live repository and transaction capability. The handler decodes and maps; it does not write the database directly.

## Payment with unknown outcome

```text
payment.authorize.command.ts
  -> payment.authorize.use-case.ts
  -> payment-gateway.port.ts
  -> payment-gateway.stripe.live.ts
```

The command carries an operation ID. A timeout returns `pendingExternalConfirmation` rather than "failed". Reconciliation queries by operation ID before retry.

## Frontend optimistic update

```text
user intent
  -> operation ID + optimistic proposal
  -> mutation through injected client
  -> acknowledgement/rejection
  -> server projection refresh or realtime reduction
  -> proposal removed or reconciled
```

The local store does not become the accepted fact owner.

## AI-generated MVP takeover

```text
polished UI + local JSON + direct SDK calls
  -> identify accepted user obligations
  -> classify fake/prototype/real paths
  -> establish one governed use case and fact writer
  -> isolate provider capability
  -> add host composition and stable verification command
  -> migrate one Tracer slice
  -> fence and delete legacy writes
```

## Database replacement

```text
current repository Port
  -> new adapter passes conformance tests
  -> schema/data backfill
  -> shadow read or dual-read comparison
  -> promote new source of truth
  -> fence old writer
  -> remove bridge after no remaining use
```

## Worker extraction

A long-running operation moves from API host to worker only after independent lifetime, retry, throughput, or failure pressure exists. The use case and fact authority remain explicit; creating a queue does not automatically create a new semantic owner.

## Related knowledge

- Use [TypeScript backend projection](typescript-backend-projection.md) for source details.
- Use [Forward evolution and migration](forward-evolution-and-migration.md) for replacement.
- Use [Agentic systems projection](agentic-systems-projection.md) for Agent runtime.
- Use the [TypeScript capability tree example](typescript-capability-tree-example.md).
- Return to the [EAA map](../SKILL.md).
