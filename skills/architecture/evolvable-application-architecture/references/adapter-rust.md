# Rust Projection

Load this after the generic doctrine when Rust is the implementation ecosystem.
Rust can enforce useful boundaries, but its language ownership model is not the
same as product fact Authority.

## Non-Equivalences

```text
memory ownership          != product fact authority
exclusive borrow          != durable single-writer proof
pub/private visibility    != product authorization
crate ownership           != transaction ownership
Send + Sync               != lifecycle correctness
RAII                      != async graceful shutdown
successful compilation    != behavioral evidence
shared crate              != permission for every host to write facts
```

Another process, database connection, retrying worker, old deployment, or
external callback can violate business Authority even when Rust aliasing is
perfectly safe.

## Module and Crate Boundaries

Use module privacy first:

```text
private module
  -> pub(super) / pub(crate) controlled collaboration
  -> explicit facade and re-exports
  -> workspace crate when compilation, reuse, ownership, or release pressure is real
  -> binary/deployable when lifecycle, trust, fault, scaling, or deployment pressure is real
```

Audit accidental `pub` expansion. Fix the semantic boundary instead of making
items public merely to silence the compiler.

Cargo workspace and crate boundaries enforce compilation dependency and public
API shape. They do not determine consistency domains or fact writers.

## Capability Contracts and Dispatch

An application-owned trait is appropriate for a genuine outer capability,
replaceable provider, trust/lifecycle boundary, or realistic fake/replay seam.
Do not create a trait for every domain service.

```text
implementation fixed by build/profile
  -> concrete composition or generic parameter

runtime registration / plugin / dynamic selection required
  -> dyn-compatible trait and explicit erased boundary
```

Avoid defaulting every dependency to `Arc<dyn Service + Send + Sync>`. The
selection time, object-safety/dyn-compatibility, ownership, and lifecycle should
justify dynamic dispatch.

For async capability methods, choose the contract shape deliberately. If a
runtime-selected trait cannot remain dyn-compatible, use an explicit boxed
future or adapter boundary and record the cost; do not leak that erasure into
domain semantics.

## Authority and Use Cases

A private authority module should expose Commands/Queries or use-case functions,
not mutable state containers.

```rust
pub struct RequestRefund {
    pub refund_id: RefundId,
    pub amount: Money,
}

pub enum RefundAttemptOutcome {
    Accepted(ExternalReceipt),
    Rejected(ProviderRejection),
    OutcomeUnknown(ProviderOperationId),
}

pub trait PaymentRefundPort {
    fn request_refund(
        &self,
        request: RefundRequest,
    ) -> impl Future<Output = Result<RefundAttemptOutcome, PaymentError>> + Send;
}
```

The provider adapter returns a receipt, rejection, or unknown outcome. The
application use case decides and commits local accepted facts.

## Async Task and Resource Lifecycle

RAII covers lexical resource cleanup; detached tasks and external effects still
need structured ownership.

Name:

```text
task owner and child tracking
cancellation propagation and deadline
shutdown trigger and notification
wait-for-exit policy
resource finalization order
in-flight external effect / outcome-unknown reconciliation
panic and join-error policy
```

Keep `tokio::spawn`, channels, `Arc`, `Mutex`, task trackers, and shutdown tokens
in host/application infrastructure unless they are truly part of the product
model. A successful `Drop` does not prove a spawned task completed safely.

## Type Boundaries

Keep representation responsibilities separate:

```text
Serde/wire DTO              != domain fact
SQLx/Diesel/ORM row         != authority model
Axum extractor              != CommandContext
Tonic/protobuf generated    != internal collaboration type
provider SDK error          != stable capability error
storage enum                != public product contract
```

Do not derive every wire and persistence trait on the same domain type merely
for convenience. Map at explicit boundaries where compatibility or trust differs.

## Public API and Forward Evolution

Review:

```text
public struct field construction
public enum exhaustiveness
#[non_exhaustive] where ecosystem compatibility requires it
constructors/builders and invariant preservation
SemVer and crate release boundary
MSRV and edition policy
Cargo feature compatibility and feature unification
wire contract versus Rust API versus persisted-data compatibility
```

Rust API compatibility tools do not replace data migration, authority-epoch
fencing, or protocol negotiation.

## Composition Root

A binary/profile/bootstrap layer owns:

```text
validated config and credentials
concrete adapters
connection pools and runtimes
static or dynamic implementation selection
task supervision and graceful shutdown
transport/router construction
```

It does not own product transitions. Avoid one public `App` or
`Arc<Mutex<AppState>>` that combines every authority, cache, registry, adapter,
and proof hook.

## Verification

Choose proof surfaces according to the claim:

```text
cargo check / compile-fail / visibility tests
Cargo dependency and feature graph checks
public API / semver / MSRV checks
forbidden import and dependency-boundary tests
adapter conformance with deterministic fake
transaction, idempotency, duplicate delivery, and restart tests
async cancellation and graceful-shutdown tests
migration, bridge fencing, and old-writer deletion tests
real-adapter sandbox or integration evidence
```

`cargo test` alone does not prove process shutdown, network reachability,
migration correctness, production configuration, or real-provider behavior.

## Common Audit Findings

- public global `App`/state container owns unrelated facts and runtime resources;
- whole-state Store trait snapshots the entire graph;
- every service is a trait and every dependency is `Arc<dyn ...>`;
- provider, ORM, or transport types enter authority logic;
- API and Worker share one crate and both write the same fact directly;
- spawned tasks have no owner, cancellation, or shutdown wait;
- public enums/structs block forward-compatible evolution;
- tests mutate maps or DB tables instead of invoking governed use cases;
- compile success is reported as behavioral or deployment proof.
