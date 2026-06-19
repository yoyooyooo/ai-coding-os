# Rust Adapter

Load this after the generic doctrine when the implementation uses Rust.

## Idiom Mapping

```text
Authority cell       -> private module/types with controlled public API
Capability port      -> trait owned by application/core crate
Adapter              -> outer crate implementing the trait
Composition root     -> bin/main/profile/bootstrap module
Typed ChangeSet      -> enum/struct specific to a use case
CommitReceipt        -> explicit result struct
Dependency guard     -> Cargo graph + visibility + boundary tests
Test fixture support -> cfg(test), dev-dependency, or dedicated test-support crate
```

Do not create traits for every domain service. Use traits when dynamic/static
replacement or an outer capability boundary is real.

## Dynamic Versus Static Dispatch

Use generics when the implementation is fixed for a build/profile and monomorphy
is useful. Use `dyn Trait` when adapters are registered or selected at runtime.
Keep `Arc`, `Mutex`, channels, and task supervision in application/runtime
infrastructure; do not expose concurrency containers as domain semantics.

## Repository Audit Checks

Inspect:

- `Cargo.toml` dependency direction and accidental feature coupling;
- `pub` fields exposing domain state or bootstrap internals;
- a central application struct holding every map, cache, registry, and adapter;
- store traits that load/persist an entire state graph;
- giant result structs filled with `Option` and empty vectors;
- provider enums/matches in reusable daemon/server libraries;
- environment/time/ID access inside domain methods;
- transport crates importing storage or runtime implementation crates;
- smoke/proof builders exported as production application methods;
- tests that mutate internal maps rather than use commands/fixtures.

## Recommended Shape

```rust
pub struct ApplicationFacade {
    orders: OrdersUseCases,
    results: ResultUseCases,
    queries: ProductQueries,
}

pub trait RuntimeExecutionPort: Send + Sync {
    fn execute(&self, request: RuntimeRequest)
        -> Result<RuntimeCandidateBatch, RuntimePortError>;
}

pub struct UseCaseResult<T> {
    pub value: T,
    pub receipt: CommitReceipt,
}
```

Keep trait and normalized contracts in the inward-facing crate. Keep SDK types
and adapter-private errors in the adapter crate; map them to a stable port error
at the boundary.

## Composition

Prefer concrete adapter construction in binaries or profile modules. A library
such as `daemon` should consume registrations/factories/endpoints rather than
import every runtime crate and match on every vendor mode.

Use crate splits for dependency enforcement, not as a substitute for module
privacy. Start with private modules if a new crate would add ceremony without a
real dependency or ownership benefit.

## Persistence

Avoid a trait whose core method is `load_state() -> EntireDomainState`. Define
use-case or module-owned transaction/repository ports and use contract tests
against in-memory and database adapters.

External async calls should not hold database transactions. Materialize returned
candidates in a second transaction with expected-version/idempotency checks.

## Mechanical Proof

Use compile tests, public API tests, dependency graph checks, forbidden-import
checks, adapter conformance suites, restart tests, and database transaction
proofs. A successful `cargo test` alone does not prove process, transport, or
real-adapter behavior.
