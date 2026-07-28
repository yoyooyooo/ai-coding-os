# Frontend Integration

Effect can provide typed execution, dependencies, resources, and concurrency in a frontend host. It should not take over React rendering, Query ownership, navigation, or local interaction state.

## Host-owned Runtime

The browser/desktop host may construct one Runtime or live Layer graph for the intended lifetime. Expose a narrow runtime-bound facade or adapter to features.

Do not construct a Runtime in every component, hook, query callback, or event handler.

## Client capability

An Effect-based client may own:

```text
transport invocation
runtime decoding
authentication/session integration
timeout, retry, cancellation
subscription resources
typed failures
```

React hooks and Query policy remain separate.

## React boundary

Convert Effect results to the frontend's chosen state mechanism at an explicit boundary. Preserve interruption and unknown outcome rather than flattening every failure to a string.

## Query

Query functions may execute a runtime-bound Effect client. Query still owns remote projection and mutation lifecycle. Effect does not automatically replace the Query cache.

## Local store

Use ordinary local state or an external store for interaction state. A Ref inside a global Runtime is not automatically a better frontend state owner.

## Realtime

The host owns the socket or Stream resource. A feature-level realtime reducer consumes typed values and manages projection continuity; it does not create the transport.

## SSR and hydration

Separate server-only Runtime/resources from browser-owned resources. Do not serialize Service instances or secrets. Define which data is dehydrated and revalidated.

## Testing

Provide test client implementations or Layers at the capability boundary. Use browser/host Harnesses to observe resource duplication, cancellation, reload, and reconnect.

## Related knowledge

- Use [Service, Layer, and Runtime](service-layer-runtime.md) for Runtime ownership.
- Use [Scope, resources, and finalization](scope-resources-and-finalization.md) for socket and subscription lifetime.
- Use `$frontend-architecture` for Query/store/realtime/React ownership.
- Use `$product-harness-system` for browser and reload observation.
- Return to the [Effect map](../SKILL.md).
