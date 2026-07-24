# Realtime Capability

Realtime is a delivery and continuity mechanism for projections. It is not an
alternate business authority.

## Pipeline

```text
committed fact
  -> projection event/envelope
  -> client decode and continuity check
  -> feature reducer/patch/invalidation
  -> query cache or local resource state
  -> view model
```

## Contract

A useful subscription contract exposes:

```text
identity or stream key
cursor/version/sequence when available
event id for dedupe
typed envelope or decode error
close/unsubscribe
connection/retry diagnostics
gap/requires-backfill signal
```

Transport, auth, backoff, timeout, cancellation, and raw decoding belong in the
client/host capability. Feature realtime code consumes typed envelopes and owns
only projection reduction.

## Reduction Rules

```text
duplicate id -> ignore
known contiguous event -> small deterministic patch or invalidate
unknown event/shape -> diagnostic + invalidate/backfill
cursor gap or stale version -> backfill
permission/visibility change -> discard unsafe local data and refetch
connection state -> local resource status, not business status
```

Patching is worthwhile only when it is simpler and equally safe as refetching.
Prefer invalidation/backfill when an event lacks enough context.

## Lifecycle

Choose and document lifetime: component, route, feature, tab, app, worker, or
process. The host/client owns transport resources; React hooks may attach and
release subscriptions through an injected capability.

Handle reconnect with cursor/version handoff. A successful socket reconnect does
not prove projection continuity until gap/backfill rules pass.

## Testing

Minimum contract cases:

```text
happy event updates or invalidates projection
duplicate does not duplicate visible state
gap triggers backfill
unknown/decode failure does not invent facts
close/unmount releases resource
reconnect resumes or explicitly refetches
permission change removes stale visibility
```

Add browser and real transport tests only for claims that require them.

## Effect Mapping

When Effect is selected, the live client may use Service/Layer/Scope/Stream/Queue
for resources, retry, cancellation, and fakes. Expose a runtime-bound
subscription facade to ordinary feature code unless the feature is explicitly
Effect-native. Load `$effect-best-practices` for version-specific APIs.
