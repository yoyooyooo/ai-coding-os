# Interface Obligations

An interface is where a product obligation becomes operable and perceivable. Product Definition owns the obligation; frontend and architecture owners decide the implementation mechanisms.

## Start from obligation, not component

Describe:

```text
which actor is trying to do what
what information they need before acting
what action or choice must be possible
what state or confirmation they need afterward
how waiting, failure, rejection, partial success, conflict, and recovery appear
what permission and accessibility conditions apply
```

Do not begin with "use a modal", "add a Zustand store", or "put a button in the top right" unless that form is itself an accepted constraint.

## Interface capability

A durable interface obligation can be expressed as:

```text
product obligation
  -> surface or region where it is available
  -> information and action affordances
  -> interaction states
  -> implementation owner
  -> observation surface
```

This relation may live in ordinary product prose. A separate InterfaceCapability schema is unnecessary without a real consumer.

## Complete interaction states

Consider only states relevant to the capability:

```text
normal
empty
loading or processing
validation failure
system failure
partial success
read-only or locked
no permission
expired or stale
optimistic/pending
concurrent conflict
recovery or retry
```

## Cross-surface obligations

When the same capability exists in web, mobile, API, CLI, or agent interfaces, preserve the product rule and outcome while allowing each surface to use appropriate interaction mechanics.

## Handoff to implementation owners

- `$frontend-architecture` owns Query/store/realtime, view model, route, and host responsibilities.
- `$evolvable-application-architecture` owns authoritative Commands, fact transitions, and external capability boundaries.
- `$product-harness-system` owns the observation surface.

Product Definition should not pre-select those mechanisms, but it should make the obligation concrete enough that they can be chosen honestly.

## Related knowledge

- Use [Workflow, state, and exceptions](workflow-state-and-exceptions.md) for lifecycle and recovery.
- Use [Rules, permissions, quality, and metrics](rules-permissions-quality-and-metrics.md) for permissions and quality.
- Use [Default product knowledge shape](default-product-knowledge-shape.md) for a capability document.
- Return to the [Product Definition map](../SKILL.md).
