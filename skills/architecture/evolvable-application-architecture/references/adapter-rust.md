# Rust Adapter

Load this after the generic doctrine when the implementation uses Rust.

## Idiom Mapping

```text
Authority cell       -> private module/types with controlled public API
Capability port      -> trait owned by application/core crate
Adapter              -> outer crate/module implementing the trait
Composition root     -> bin/main/profile/bootstrap module
Typed ChangeSet      -> enum/struct specific to a use case
CommitReceipt        -> explicit result struct
Dependency guard     -> Cargo graph + visibility + boundary tests
Test fixture support -> cfg(test), dev-dependency, or test-support crate
```

Do not create traits for every domain service. Use traits when an outer
capability, replacement, trust boundary, or fake/replay seam is real.

## Dynamic Versus Static Dispatch

Use generics when an implementation is fixed for a build/profile and monomorphy
is useful. Use `dyn Trait` when adapters are selected or registered at runtime.
Keep `Arc`, `Mutex`, channels, tasks, and supervision in application/runtime
infrastructure; do not expose concurrency containers as domain semantics.

## Repository Audit Checks

Inspect:

- `Cargo.toml` dependency direction and accidental feature coupling;
- `pub` fields exposing authority state or bootstrap internals;
- a central app struct holding every map, cache, registry, and adapter;
- store traits that load/persist an entire state graph;
- giant result structs filled with `Option` and empty vectors;
- vendor/provider enums in reusable core libraries;
- environment/time/ID access inside authority logic;
- transport crates importing storage or adapter implementation crates;
- smoke/proof builders exported as production application methods;
- tests mutating internal maps rather than supported commands/fixtures.

## Recommended Shape

```rust
pub struct ApplicationFacade {
    orders: OrdersUseCases,
    reviews: ReviewUseCases,
    queries: ProductQueries,
}

pub trait IdentityVerificationPort: Send + Sync {
    fn verify(
        &self,
        request: VerificationRequest,
    ) -> Result<VerificationCandidate, VerificationPortError>;
}

pub struct UseCaseResult<T> {
    pub value: T,
    pub receipt: CommitReceipt,
}
```

Keep traits and normalized contracts in the inward-facing crate. Keep SDK types
and adapter-private errors in the adapter crate; map them to a stable port error
at the boundary.

## Composition

Prefer concrete adapter construction in binaries or profile modules. A reusable
server/worker/daemon library should consume registrations, factories, or
endpoints rather than import every adapter crate and match on vendor names.

Use crate splits for dependency enforcement, not as a substitute for module
privacy. Start with private modules if a new crate adds ceremony without real
pressure.

## Persistence

Avoid a trait whose central method is `load_state() -> EntireDomainState`.
Define use-case or cell-owned transaction/repository capabilities and contract
tests against in-memory and database adapters.

External async calls should not hold database transactions. Materialize returned
observations/candidates in a later transaction with epoch, expected-version,
and idempotency checks.

## Mechanical Proof

Use compile tests, public API tests, dependency graph checks, forbidden-import
checks, adapter conformance suites, restart tests, migration tests, and database
transaction proofs. `cargo test` alone does not prove process, transport,
privacy, or real-adapter behavior.
