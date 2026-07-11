# Capability Ports

A capability port is a narrow contract defined by the application side for a
power outside product authority.

## Port Qualification Test

Create a port when a dependency crosses a vendor, process, machine, trust,
storage technology, deployment profile, external lifecycle, or realistic
fake/replay boundary.

Do not create a capability port for an internal business module merely because
it may be refactored later. Internal authority cells expose typed use-case APIs;
adapters implement outer capabilities.

## Port Shape

A useful port names:

```text
capability, not vendor
input contract
Observation / Candidate / Receipt / opaque-handle output
stable error taxonomy
idempotency and retry semantics
deadline / cancellation behavior
privacy, residency, and redaction boundary
capability or manifest snapshot
diagnostics and claim ceiling
adapter-private data that must not escape
```

Avoid exposing a provider SDK's object graph, ORM record, protocol frame, or
vendor error type. Normalize at the adapter edge.

## Adapter Output

Adapters may return:

- normalized observations or candidates;
- diagnostics, metering, and usage samples;
- opaque external handles;
- capability/manifest snapshots;
- bounded retrieval or projection inputs;
- delivery acknowledgements and external receipts.

They normally may not:

- create accepted application facts;
- grant product permissions;
- write the canonical event spine or outbox;
- own local object lifecycle or completion;
- define product routing, visibility, settlement, or workflow truth.

An external system may be authoritative for its *own* source record. The adapter
still cannot decide the local application's interpretation of that record.

## Common Port Families

Keep semantically distinct capabilities separate even when one vendor implements
several:

```text
PaymentOrSettlementPort
IdentityOrRiskVerificationPort
ExternalExecutionPort
StructuredInferencePort
DeviceOrSensorGatewayPort
ExternalIngressPort
BlobOrObjectStoragePort
NotificationDeliveryPort
SearchOrIndexPort
ExternalParticipantPort
```

Choose names from the application's need, not this illustrative list.

## Extension Classes, Not a Universal Plugin Runtime

Define a finite list of extension classes before building a generic plugin
platform. For each class state:

```text
which port it implements
which observations/candidates it may return
which commands it may request
which permissions and policy versions apply
which private state remains opaque
which conformance suite it must pass
which product claims it cannot make
```

A plugin is packaging and distribution. It is not authority.

## Replaceability Test

A capability is genuinely replaceable when:

- domain language contains no adapter-private terms;
- two adapters or fake/replay implementations pass the same contract suite;
- unknown capabilities fail explicitly rather than silently changing meaning;
- error, deadline, retry, and cancellation semantics are stable;
- fallback or migration behavior is deliberate;
- diagnostics support comparison;
- removal does not require redefining product truth.

An interface alone proves none of these.

## Strict Placement and Fallback

For capabilities whose semantics differ, prefer explicit selection and explicit
failure. A default adapter may be acceptable for an optional capability, but a
requested payment rail, runtime, storage class, residency region, safety
profile, or security mode must not silently fall back to a semantically
different implementation.

## Side-Effect Safety

Ports that cause external effects need:

```text
stable intent identity
attempt identity
idempotency or dedupe contract
send-started / acknowledged / unknown distinction
receipt normalization
reconciliation and compensation limits
redacted diagnostics
```

Do not hold the local database transaction open across the external call.
