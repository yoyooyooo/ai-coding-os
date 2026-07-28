# Topology, Composition, and Hosts

A frontend may execute in several hosts. Each host owns live implementations and resources; feature code consumes capabilities.

## Common hosts

```text
browser SPA
SSR/server render process
React Server Components host
web worker or service worker
browser extension
Electron/Tauri desktop shell
mobile host
test or Harness host
```

## Composition rule

```text
host/bootstrap
  decodes configuration
  constructs product clients and resources
  constructs router/query/store/runtime providers
  injects capabilities
  owns shutdown/disposal

route/feature
  consumes injected capabilities
  does not construct live providers or process-global resources
```

## Resource ownership

Assign owner and lifetime for:

```text
HTTP client/session
auth refresh
WebSocket/EventSource
worker
Effect Runtime
query cache
external store
background polling
analytics or telemetry client
```

State whether lifetime is per request, route, tab, app, worker, or process.

## Feature boundaries

A feature normally owns the behavior needed for one user-facing capability:

```text
client contract usage
query/mutation factories or hooks
local interaction transitions
realtime projection reduction
mappers and view models
page/surface composition
fixtures and focused tests
```

Feature A consumes Feature B through an explicit public surface when the product relationship is stable. Loose coordination belongs in the host or route composition.

## Package boundaries

Packages do not import app internals. Host-specific implementations remain selected by hosts. Generated wire contracts remain separate from view models. Consumers do not deep-import private feature files.

A source-only package versus a built/published package is a build decision, not an architecture invariant.

## SSR and hydration

Define the handoff between server and browser:

```text
what data is serialized
which cache owns it after hydration
what is revalidated
which resources are client-only
how identity and secrets remain server-only
```

## Related knowledge

- Use [Default frontend source conventions](default-frontend-source-conventions.md) for directories and suffixes.
- Use [Naming and feature boundaries](naming-and-feature-boundaries.md) for public surfaces.
- Use [React integration](react-integration.md) for providers and hooks.
- Use `$evolvable-application-architecture` for repository and capability boundaries.
- Use `$effect-best-practices` for Runtime/Scope ownership.
- Return to the [Frontend Architecture map](../SKILL.md).
