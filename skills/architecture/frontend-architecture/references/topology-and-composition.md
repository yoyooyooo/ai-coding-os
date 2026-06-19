# Topology and Composition

## Host Roots

A frontend may run in several hosts:

```text
browser SPA
SSR/server render process
React Server Components host
web worker/service worker
browser extension
Electron/Tauri desktop shell
mobile host
test/harness host
```

Each host needs an explicit composition root that normalizes configuration,
credentials, transport implementations, runtime resources, query/cache policy,
and shutdown/disposal.

Feature code consumes capability contracts. It does not read environment
variables, create live SDKs, or choose vendor implementations.

## Composition Rule

```text
host/bootstrap
  builds config and platform adapters
  builds product clients / runtimes
  builds router/query/store providers
  injects capabilities

route/feature
  consumes injected capabilities
  does not construct live implementations
```

SSR and hydration require a declared ownership handoff: what is prefetched,
serialized, dehydrated, revalidated, and client-only. Never create two live
resource owners during hydration by accident.

## Package Boundaries

Universal rules:

- packages do not import app internals;
- public APIs hide private transport/runtime details;
- generated wire contracts remain distinct from feature view models;
- package consumers do not deep-import private files;
- host-specific implementations are selected at composition roots.

“Source-only package” versus built/published package is a build profile, not a
universal architecture law. Choose based on tooling, versioning, runtime format,
and distribution; preserve the same public dependency direction either way.

## Client Capability

A product client is a typed gateway, not a dumping ground. It may own decode,
auth/header injection, timeout/retry/cancel, transport errors, subscriptions, and
host-specific implementations. It should not own React hooks, Query cache policy,
feature stores, view models, or surfaces.

Split a giant client by cohesive capability when there is real independent
ownership, replacement, permission, lifecycle, or test pressure. Avoid one
interface per endpoint.

## Feature Boundaries

A feature capability usually owns:

```text
commands and query option factories
local interaction transitions
projection/realtime reduction
mapping and view model
page/surface composition
fixtures and feature tests
```

Feature A may consume Feature B only through an explicit public contract when
the product relationship is stable. Prefer composition in routes/app for loose
coordination. Promote shared product concepts to a named shared capability or
package rather than a generic bucket.

## Resource Lifetimes

Assign owners for:

```text
HTTP client/session
auth refresh
WebSocket/EventSource
worker
Effect runtime
query cache
external store
background polling
```

State whether lifetime is per request, route, tab, app, worker, or process.
Resource creation hidden in a hook or module singleton makes test isolation,
StrictMode behavior, SSR, and disposal unpredictable.
