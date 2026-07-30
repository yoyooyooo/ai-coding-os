# Service, Layer, and Runtime

> **Layer Wires Capabilities; It Does Not Own Product Meaning.** Service contracts, Layers, and Runtimes assemble execution dependencies without becoming semantic or fact authority.

Service, Layer, and Runtime solve different problems. Keeping them distinct prevents dependency injection from becoming a global architecture identity.

## Service

A Service describes an Effect-native capability contract. It is useful when:

```text
several callers need the capability
tests need substitution
failure/resource semantics belong to the capability
implementations vary by host or environment
```

An Effect Service may be the concrete representation of an application-owned Port. In that case, the Service contract is the Port; do not add a parallel `.port.ts` contract with the same methods and meaning.

Do not create a Service for every pure function, value object, mapper, or one-use helper.

## One canonical contract

Choose the smallest stable capability surface:

```text
ordinary TypeScript Port
  -> useful when the capability should remain framework-neutral

Effect Service contract
  -> useful when Effect failure/environment semantics are intentionally part of the capability surface
```

Both may coexist only when they serve independent consumers or a real compatibility/trust boundary. Make the translation explicit; duplicated contracts that drift independently are not separation.

## Layer

A Layer constructs one or more Services and owns any resources required for that construction. It may decode configuration, acquire clients, and register finalizers. A provider-qualified live adapter file may export the Layer directly.

Layer should not:

```text
decide product fact authority
expose provider details through the capability contract
be constructed deep inside business logic
be rebuilt for every small operation unless lifetime requires it
create application module or package boundaries by itself
```

## Runtime

A Runtime executes Effect values against a prepared environment. The host owns it when ordinary framework callbacks, React, CLI, or transport adapters need to enter Effect.

Default:

```text
one owned live graph per real host lifetime
narrow runtime-bound facade at integration boundaries
explicit shutdown
```

An all-Effect host may execute the program directly and omit a separate `<host>.runtime.ts` file.

## Public API

Keep internal Service keys, Layer construction, and Runtime details private unless the package intentionally exposes an Effect-native public API. External consumers may receive ordinary typed functions backed by an internal Runtime.

## Composition

Effect mechanics project onto the application's existing roles:

```text
application capability contract
  -> ordinary Port OR Effect Service
  <- provider-qualified live implementation / Layer
  <- host composition
  <- host Runtime or direct Effect program
```

Preserve the semantic owner of the capability. Host composition chooses implementations and lifetime; it does not choose which module owns an accepted fact.

## Testing

Substitute at the canonical capability boundary. Avoid mocking internal Effects or exact call sequences unless the interaction itself is the contract. A fake proves only the behavior and dependency reality it exercised; it does not prove the live provider or resource graph.

## Common smells

- a global Runtime imported everywhere;
- live Layer construction inside request handlers or React hooks;
- Service keys exported only to satisfy a DI style;
- parallel Port and Service definitions with identical methods;
- Layer composition determines which module owns product facts;
- test Layers diverge semantically from live capability contracts.

## Related knowledge

- Use [Default Effect module conventions](default-effect-module-conventions.md) for the Effect overlay on source filenames.
- Use [Scope, resources, and finalization](scope-resources-and-finalization.md) for Layer lifetime.
- Use [Frontend integration](frontend-integration.md) for React/host boundaries.
- Use `$evolvable-application-architecture` for application Ports, source grammar, and composition roots.
- Return to the [Effect map](../SKILL.md).
