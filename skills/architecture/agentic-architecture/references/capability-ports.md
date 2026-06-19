# Capability Ports

A capability port is a narrow contract defined by the application side for a
replaceable power outside product authority.

## Port Qualification Test

Create a port when the dependency crosses a vendor, process, machine, trust,
storage technology, deployment profile, or realistic fake/replay boundary.

Do not create a capability port for an internal business module merely because
it may be refactored later. Internal modules expose use-case APIs; adapters
implement outer capabilities.

## Port Shape

A useful port names:

```text
capability, not vendor
input contract
candidate / observation / handle output
stable error taxonomy
idempotency and retry semantics
deadline / cancellation behavior
privacy and redaction boundary
capability or manifest snapshot
diagnostics and claim ceiling
adapter-private data that must not escape
```

Avoid exposing a provider SDK's full object graph. Normalize at the adapter
edge.

## Adapter Output

Adapters may return:

- normalized candidates;
- diagnostics and usage samples;
- opaque external handles;
- capability/manifest snapshots;
- bounded retrieval or projection inputs;
- delivery acknowledgements.

They normally may not:

- create accepted domain facts;
- grant permissions;
- write the event spine or outbox;
- own object lifecycle or completion;
- define product routing, memory, or visibility truth.

## Common Port Families

Keep these conceptually separate even when one vendor implements several:

```text
StructuredInferencePort
RuntimeExecutionPort
MemoryRetrievalPort
ExternalIngressPort
Blob/ObjectStoragePort
NotificationDeliveryPort
Search/IndexPort
ExternalParticipantPort
```

## Extension Classes, Not a Universal Plugin Runtime

Define a finite list of extension classes before building a generic plugin
platform. For each class state:

```text
which port it implements
which candidate types it may return
which commands it may request
which permissions/policies apply
which private state is opaque
which conformance suite it must pass
which product claims it cannot make
```

A plugin is packaging and distribution. It is not authority.

## Replaceability Test

A capability is genuinely replaceable when:

- domain language contains no adapter-private terms;
- two adapters can pass the same contract/conformance suite;
- unknown capabilities fail explicitly rather than silently changing meaning;
- error and retry semantics are stable;
- fallback or migration behavior is deliberate;
- diagnostics support side-by-side comparison;
- removal does not require changing product truth.

An interface alone proves none of these.

## Strict Placement and Fallback

For capabilities whose semantics differ, prefer explicit selection and explicit
failure. A default adapter may be acceptable for an optional capability, but a
requested runtime, provider, storage class, or security profile should not
silently fall back to a semantically different implementation.
