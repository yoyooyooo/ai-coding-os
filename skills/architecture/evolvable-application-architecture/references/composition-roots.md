# Composition Roots

A composition root assembles one deployment profile. It selects concrete
adapters, resource lifetimes, credentials, configuration, observability, and
profile-specific operational policy.

## Responsibilities

Composition roots may:

- instantiate adapters and clients;
- register capabilities and manifests;
- construct application modules and facades;
- bind clocks, IDs, transaction factories, and publishers;
- load configuration and secrets;
- start servers, workers, daemons, CLIs, or frontend runtimes;
- select fake, replay, local, hosted, or real-external profiles.

They must not own product transitions, permission decisions, settlement,
workflow completion, or direct canonical event-spine writes.

## One Core, Multiple Profiles

```text
core application and authority cells
  -> local standalone
  -> server / worker
  -> desktop / daemon
  -> hosted / cloud
  -> test fake
  -> deterministic replay
  -> real external capability opt-in
```

Profile changes alter assembly and evidence, not product fact authority.

## Keep Vendor Enumeration Out of Core Libraries

A reusable server, worker, daemon, or application library should not need an
enum and match statement for every provider. Prefer registrations, factories,
manifests, or profile-specific constructors in executable/bootstrap code.

Adding an adapter should ideally require:

```text
new adapter implementation
+ profile registration
+ conformance evidence
```

It should not require unrelated authority-cell edits.

## Registries

A registry is appropriate when implementations are selected dynamically. Keep
selection policy explicit and separate from the adapter collection.

State:

- whether unknown IDs reject or fall back;
- whether aliases are explicit;
- how capability snapshots are validated;
- who owns adapter lifecycle, concurrency, and shutdown;
- whether registrations are static, configured, or discovered;
- which profile and authority epoch used the registration.

## Lifecycle

The root owns construction and shutdown order for external resources. It should
propagate cancellation and deadlines without leaking resource handles into
authority semantics.

For long-running workers, define supervision, lease renewal, backpressure, and
graceful drain. Those operational mechanisms do not decide business outcomes.

## Signs of a Thick Root

- business branching in `main`, server setup, or frontend bootstrap;
- vendor errors directly choose product transitions;
- tests duplicate production wiring by hand;
- local and hosted profiles implement different product semantics;
- a profile imports adapters it cannot use;
- configuration or environment reads appear inside authority logic.

Use reusable profile builders for tests and production, but keep fixture-only
fact creation outside the public product API.
