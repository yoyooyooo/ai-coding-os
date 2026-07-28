# Default Effect Module Conventions

Use this portable default when an Effect project has no coherent adopted file grammar. It restores deterministic semantics without requiring one Service or Layer per file.

## Default mapping

```text
<capability>.port.ts                    ordinary application-owned contract
<capability>.service.ts                 Effect Service key/contract, only when useful
<capability>.<provider>.live.ts         live Layer or adapter
<capability>.memory.fake.ts             deterministic Effect implementation
<subject>.<operation>.use-case.ts       application operation
<subject>.model.ts                      pure data and decisions
<host>.composition.ts                   Layer graph selection and host assembly
<host>.runtime.ts                       owned Runtime facade when a non-Effect host needs it
```

Examples:

```text
payment-gateway.port.ts
payment-gateway.service.ts
payment-gateway.stripe.live.ts
payment-gateway.memory.fake.ts
payment.authorize.use-case.ts
api.composition.ts
api.runtime.ts
```

Use kebab-case inside semantic segments and dots between dimensions.
Keep these files in the owning capability module by default. Do not create `services/`, `layers/`, `runtimes/`, or `adapters/` subtrees solely for structural symmetry.

## Required invariants

- a Service is admitted for a real capability, not one file per helper;
- a Layer graph does not decide product fact authority or package boundaries;
- each host constructs and closes its own live graph;
- internal Service keys, Layers, and Runtime construction stay private unless the public API is intentionally Effect-native;
- installed package version and declarations decide concrete API syntax.

## Conditional roles

```text
<subject>.stream.ts             when a Stream is a stable capability surface
<subject>.queue.ts              when a Queue is deliberately exposed inside the module
<subject>.actor.ts              when a real long-lived state owner exists
<subject>.config.ts             when typed config is local to one host/capability
<subject>.layer.ts              only when Layer itself is the stable named responsibility
```

Do not introduce these for visual symmetry.

## Project override

Preserve a coherent project grammar. Record significant differences in a Standard or `AGENTS.md`. Keep the semantic roles and host lifetime visible.

## Example

See the [Effect capability tree](effect-capability-tree-example.md).

## Related knowledge

- Use [Service, Layer, and Runtime](service-layer-runtime.md) for responsibility.
- Use [Mechanism selection](mechanism-selection.md) before admitting a Service or Actor.
- Use `$evolvable-application-architecture` for the application-wide source grammar.
- Return to the [Effect map](../SKILL.md).
