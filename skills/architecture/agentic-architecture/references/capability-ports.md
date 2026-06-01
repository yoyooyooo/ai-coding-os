# Capability Ports

A capability port is a typed boundary defined by the core or application layer.
It describes what capability the system needs, not which vendor, SDK, plugin,
runtime, or framework currently implements it.

## Port Shape

Good ports are narrow:

```text
capability name
input contract
output contract
error model
idempotency / retry behavior
permission / policy inputs
diagnostic shape
redaction boundary
claim ceiling
adapter-private data boundary
```

Avoid ports that expose a provider's full object model. That makes the provider
the real architecture.

## Adapter Output

Adapters may return:

- candidate facts;
- diagnostics;
- opaque external handles;
- manifest or capability snapshots;
- bounded projection inputs;
- usage/cost/latency samples.

Adapters should not return accepted business facts, grant permissions, write the
event spine, own memory entries, or define lifecycle state.

## Provider vs Runtime vs Memory Ports

Keep these boundaries separate unless the project has a deliberate reason to
merge them:

```text
ModelProvider
  ordinary model calls, structured generation, extraction, rerank, query planning

RuntimeExecutionPort
  agentic runtime start/resume/steer/interrupt, continuation handles, runtime events

MemoryRetrievalPort
  accepted-memory search, candidate ranking, retrieval evidence, fallback behavior

ExternalIngressPort
  external human/system ingress verification, dedupe, mapping, diagnostics
```

One vendor may implement multiple ports, but the core should not see one vendor
object as the common abstraction for all of them.

## Plugin Boundary

Plugin is a packaging and distribution mechanism. It is not authority.

For a plugin system, state:

```text
which ports can plugins implement
which facts plugins may only propose
which commands plugins may request
which policies can reject plugin output
which diagnostics are persisted
which plugin-private state is opaque
which claims plugin tests can prove
```

Do not allow plugin-owned domain facts, event writes, permission grants, object
lifecycle, scheduler authority, route authority, or memory authority unless the
system explicitly makes the plugin the product authority.

## Replaceability Test

A port is replaceable when:

- adapter-private terms do not leak into domain objects;
- output is narrow and normalized;
- error semantics are stable;
- fallback or migration behavior is defined;
- diagnostics are enough to compare adapters;
- tests or harnesses prove at least one fake and one real or replay adapter path;
- removing the adapter does not require changing product truth.

If replacing an adapter requires changing domain language, the port is too
wide or in the wrong layer.
