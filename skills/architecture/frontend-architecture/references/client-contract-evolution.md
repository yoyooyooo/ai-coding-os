# Client Contract Evolution

A frontend product client is a typed capability facade, not a dumping ground for React hooks, Query policy, stores, or view models.

## Client responsibilities

A client may own:

```text
transport/protocol invocation
runtime decoding
authentication and headers
timeout, cancellation, and transport retry
provider/transport error translation
subscription entry points
host-specific live implementations
```

It should return normalized product/application representations or typed outcomes, not raw HTTP, SDK, or generated-wire types.

## Contract layers

```text
wire/generated contract     external representation
client capability contract  frontend-owned typed operation surface
projection model            remote state used by features
view model                  surface-specific composition
```

Do not collapse all four into one generated type.

## Version evolution

When the backend contract changes:

```text
expand decode support when compatibility is required
normalize old/new wire forms inside the client/mapper boundary
migrate feature consumers to one stable client contract
remove old decode paths after no live producer remains
```

Avoid leaking version branches through every component.

## Error and outcome mapping

Keep meaningful distinctions such as validation, authorization, conflict, pending, timeout, and unknown outcome. Do not map every failure to `Error` with a message string.

## Splitting clients

Split a large client by cohesive product capability when ownership, replacement, permission, lifetime, or test pressure is real. Do not create one interface per endpoint.

## Fakes

A `.client.fake.ts` is explicit deterministic behavior for tests or demos. It should not silently activate in production when configuration is missing.

## Related knowledge

- Use [Default frontend source conventions](default-frontend-source-conventions.md) for filenames.
- Use [Intent, acknowledgement, and reconciliation](intent-acknowledgement-and-reconciliation.md) for typed outcomes.
- Use [Topology, composition, and hosts](topology-composition-and-hosts.md) for live client construction.
- Use `$evolvable-application-architecture` for backend Port and protocol evolution.
- Return to the [Frontend Architecture map](../SKILL.md).
