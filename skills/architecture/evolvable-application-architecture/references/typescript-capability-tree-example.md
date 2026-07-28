# TypeScript Capability Tree Example

This example shows a richer capability without implying that every capability needs every role.

```text
apps/
  api/
    src/
      host/
        api.main.ts
        api.config.ts
        api.composition.ts
        api.shutdown.ts
      modules/
        payments/
          payment.model.ts
          payment.authorize.command.ts
          payment.authorize.use-case.ts
          payment.risk.policy.ts
          payment-gateway.port.ts
          payment-gateway.stripe.live.ts
          payment-gateway.memory.fake.ts
          payment.transaction.port.ts
          payment.http.contract.ts
          payment.http.handlers.ts
          payment.public.ts
  worker/
    src/
      host/
        worker.main.ts
        worker.composition.ts
        worker.shutdown.ts
      modules/
        payment-reconciliation/
          payment.reconcile.use-case.ts
          payment-reconciliation.public.ts
```

## Defaults used

- dots separate subject, operation/facet, responsibility, and provider qualifier;
- live provider types remain outside the use case and Port;
- API and worker have independent composition/lifetime;
- sharing a package or database does not make both hosts fact writers;
- `memory.fake.ts` is explicit and never a silent production fallback.

## Conditional elements

The worker exists because unknown provider outcomes require durable reconciliation with an independent lifetime.

## Intentionally omitted

- a package boundary between API and worker: shared compile/public API pressure has not yet been demonstrated;
- an event-sourced ledger: ordinary authoritative rows plus audit/outbox are sufficient;
- one Service interface per file.

## Related Skills

- `$evolvable-application-architecture`
- `$effect-best-practices`
