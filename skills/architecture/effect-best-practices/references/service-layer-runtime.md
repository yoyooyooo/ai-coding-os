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

Do not create a Service for every pure function, value object, mapper, or one-use helper.

## Layer

A Layer constructs one or more Services and owns any resources required for that construction. It may decode configuration, acquire clients, and register finalizers.

Layer should not:

```text
decide product fact authority
expose provider details through the Service contract
be constructed deep inside business logic
be rebuilt for every small operation unless lifetime requires it
```

## Runtime

A Runtime executes Effect values against a prepared environment. The host owns it when ordinary framework callbacks, React, CLI, or transport adapters need to enter Effect.

Default:

```text
one owned live graph per real host lifetime
narrow runtime-bound facade at integration boundaries
explicit shutdown
```

## Public API

Keep internal Service keys, Layer construction, and Runtime details private unless the package intentionally exposes an Effect-native public API. External consumers may receive ordinary typed functions backed by an internal Runtime.

## Composition

```text
application-owned Port or Service contract
  <- live implementation Layer
  <- host composition
  <- host Runtime or direct Effect program
```

A host may combine pure application Ports with Effect Services. Preserve the semantic owner of the capability.

## Testing

Substitute at the capability boundary. Avoid mocking internal Effects or exact call sequences unless the interaction itself is the contract.

## Common smells

- a global Runtime imported everywhere;
- live Layer construction inside request handlers or React hooks;
- Service keys exported only to satisfy a DI style;
- Layer composition determines which module owns product facts;
- test Layers diverge semantically from live capability contracts.

## Related knowledge

- Use [Default Effect module conventions](default-effect-module-conventions.md) for filenames.
- Use [Scope, resources, and finalization](scope-resources-and-finalization.md) for Layer lifetime.
- Use [Frontend integration](frontend-integration.md) for React/host boundaries.
- Use `$evolvable-application-architecture` for application Ports and composition roots.
- Return to the [Effect map](../SKILL.md).
