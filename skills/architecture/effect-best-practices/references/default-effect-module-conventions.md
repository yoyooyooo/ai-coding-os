# Default Effect Module Conventions

Use this portable overlay when a project has a coherent application source grammar but no coherent convention for Effect-specific Service, Layer, Runtime, Queue, Stream, or Actor roles. It does not replace the source grammar owned by the project or `$evolvable-application-architecture`.

## Projection invariant

> **Effect projects the execution mechanism; it does not duplicate the application role.**

An application-owned capability contract may be represented as either:

```text
an ordinary TypeScript Port
or
an Effect Service contract
```

Choose one canonical contract by default. Do not maintain matching `<capability>.port.ts` and `<capability>.service.ts` files merely because the project uses Effect.

## Default projection

| Application role | Effect projection |
| --- | --- |
| use case | the existing `*.use-case.ts` may return an Effect program |
| application Port | an ordinary contract may remain ordinary, or an Effect Service may represent it directly |
| live adapter | the existing `.<provider>.live.ts` may construct/export the implementing Layer |
| fake | an earned `.memory.fake.ts` may provide the same Port/Service contract through a test Layer |
| host composition | the existing `<host>.composition.ts` may assemble the Layer graph and own resources |
| host execution boundary | add `<host>.runtime.ts` only when a non-Effect host needs a stable prepared-Runtime facade |

Examples using an Effect Service as the application Port:

```text
payment-gateway.service.ts
payment-gateway.stripe.live.ts
payment.authorize.use-case.ts
api.composition.ts
```

Alternative using an ordinary Port:

```text
payment-gateway.port.ts
payment-gateway.stripe.live.ts
payment.authorize.use-case.ts
api.composition.ts
```

Do not combine both alternatives by default.

Use kebab-case inside semantic segments and dots between dimensions. Keep files in the owning capability module. Do not create `services/`, `layers/`, `runtimes/`, or `adapters/` subtrees solely for structural symmetry.

## Required invariants

- a Service is admitted for a real capability, not one file per helper;
- one capability has one canonical contract unless a distinct public/internal or compatibility boundary earns translation;
- a Layer graph does not decide product fact authority, application module boundaries, or package boundaries;
- each host constructs and closes its own live graph;
- internal Service keys, Layers, and Runtime construction stay private unless the public API is intentionally Effect-native;
- installed package version and declarations decide concrete API syntax.

## Conditional Effect-specific roles

```text
<capability>.service.ts        when an Effect Service is the chosen canonical capability contract
<subject>.stream.ts            when a Stream is a stable capability surface
<subject>.queue.ts             when a Queue is deliberately exposed inside the module
<subject>.actor.ts             when a real long-lived state owner exists
<subject>.config.ts            when typed config is local to one host/capability
<subject>.layer.ts             only when Layer itself is the stable named responsibility
<host>.runtime.ts              when a non-Effect host needs a prepared execution facade
```

Do not introduce these for visual symmetry. A live adapter file can export its Layer without a separate `.layer.ts` file.

## Parallel contracts are exceptional

If an ordinary Port and an Effect Service both exist, state the independent reason, for example:

```text
ordinary public package API -> internal Effect-native execution contract
legacy compatibility Port   -> new Service with an explicit translation bridge
separate trust boundary     -> normalized public capability and private privileged capability
```

Keep the translation visible and remove a compatibility contract when no consumer remains.

## Project override

Preserve a coherent project grammar. Record significant differences in a Standard or `AGENTS.md`. Keep the semantic role, chosen canonical contract, and host lifetime visible.

## Example

See the [Effect capability tree](effect-capability-tree-example.md).

## Related knowledge

- Use [Service, Layer, and Runtime](service-layer-runtime.md) for responsibility.
- Use [Mechanism selection](mechanism-selection.md) before admitting a Service or Actor.
- Use [Version grounding](version-grounding.md) before writing concrete APIs.
- Use `$evolvable-application-architecture` for application roles, source grammar, transactions, and composition roots.
- Return to the [Effect map](../SKILL.md).
