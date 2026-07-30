# TypeScript Capability Tree Example

This example shows how a capability grows from a small base through explicit pressure. The combined result is not the default shape for every capability.

## Minimum API slice

```text
apps/
  api/
    src/
      host/
        api.main.ts
        api.composition.ts
      modules/
        payments/
          payment.authorize.use-case.ts       # Command + Outcome + local policy may be co-located
          payment-gateway.port.ts
          payment-gateway.stripe.live.ts
          payment.http.handlers.ts
```

Defaults used:

- dots separate subject, operation/facet, responsibility, and provider qualifier;
- the application-owned Port carries payment capability meaning;
- Stripe types remain inside the live implementation;
- host composition selects the implementation and owns its resources;
- no public surface, fake, transaction Port, Service, or worker is created without pressure.

## Delta: shared product model and policy

Add only after several operations share the concepts or the policy changes independently:

```text
payment.model.ts
payment.risk.policy.ts
payment.authorize.command.ts          # only if several entries/adopters need it
payment.authorize.outcome.ts          # only if several consumers need it
```

## Delta: verification substitute

Add after a real test needs provider substitution and the fake can honor the intended contract:

```text
payment-gateway.memory.fake.ts
```

A fake is explicit and never a silent production fallback. It does not prove Stripe behavior.

## Delta: cross-module or cross-host surface

Add after another module or host needs a deliberate stable API:

```text
payment.public.ts
```

Do not create a broad barrel before that consumer exists.

## Delta: consistency mechanism

If authorization must atomically commit several authoritative records, name the mechanism after the actual consistency scope rather than the `payments` directory by reflex:

```text
payment-authorization.transaction.port.ts
```

Use an explicit transaction context, transaction-scoped repositories, Unit of Work, or equivalent project mechanism. Omit this file when the store-native transaction remains local and no independent contract is needed.

## Delta: unknown-outcome reconciliation host

Add an independent host only when provider outcomes require durable reconciliation with their own lifetime:

```text
apps/
  worker/
    src/
      host/
        worker.main.ts
        worker.composition.ts
      modules/
        payment-reconciliation/
          payment.reconcile.use-case.ts
```

API and worker may share a package or public surface later if stable compile/reuse pressure appears. Sharing a database or repository does not make both hosts final writers.

## Effect projection

When the project uses Effect, choose one canonical capability contract:

```text
payment-gateway.port.ts        ordinary TypeScript Port
or
payment-gateway.service.ts     Effect Service as the application Port
```

Do not keep both by default. The existing `payment-gateway.stripe.live.ts` may export a Layer, and `api.composition.ts` may assemble it.

## Intentionally omitted

- an event-sourced ledger when authoritative rows plus audit/outbox are sufficient;
- one Service interface per file;
- a package boundary before stable sharing or public compatibility pressure;
- a complete command/outcome/receipt/schema/mapper suffix family.

## Related Skills

- `$evolvable-application-architecture`
- `$effect-best-practices`
