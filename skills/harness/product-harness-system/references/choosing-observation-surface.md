# Choosing an Observation Surface

Choose the smallest surface that can honestly answer the current property. A slower or more realistic surface is not automatically better.

## Property first

State the property before selecting the test:

```text
pure rule or invariant
public contract
adapter/provider translation
transaction and persistence
resource lifetime or shutdown
browser interaction and accessibility
restart/reconnect/reload behavior
real provider or production-like behavior
```

## Observation surfaces

### Static

Types, schema validation, import rules, configuration checks, and source inspection. Useful for structural properties; cannot prove runtime reachability.

### Unit or property test

Fast, local, and precise for pure decisions, state transitions, mappers, invariants, and generated input spaces.

### Contract or conformance test

Compares implementations against an application-owned Port or public protocol. It cannot prove the real provider behaves identically outside the exercised cases.

### Headless integration

Runs real application composition without a browser. Useful for use cases, database, event, resource, and restart behavior.

### Browser/UI

Observes rendering, navigation, focus, accessibility, hydration, reload, and real browser integration.

### Restart/recovery

Kills or restarts the relevant host/resource and observes persistence, replay, idempotency, continuity, and cleanup.

### Local-real

Uses the real dependency type in a controlled local environment, such as PostgreSQL or a local object store.

### External-real

Uses an actual provider or production-like external system. Stronger for provider behavior, still bounded by account, configuration, region, timing, and path.

### Focused probe

A small falsifiable experiment for one empirical unknown. The result may be observation, not a permanent test.

## Selection questions

```text
what claim would change because of this result?
which dependency reality is required?
what failure should the surface expose?
can a smaller surface answer the same question?
what will remain unproven?
```

## Avoid ladders

Do not require every property to pass unit -> integration -> browser -> external. Different properties need different surfaces.

## Related knowledge

- Use [Dependency realities](dependency-realities.md) to label what actually ran.
- Use [Observation limits](observation-limits.md) before promoting the claim.
- Use [Default project verification interface](default-project-verification-interface.md) for command discovery.
- Use [Feedback horizon](feedback-horizon.md) to choose safe implementation step size.
- Return to the [Harness map](../SKILL.md).
