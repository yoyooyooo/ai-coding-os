# Rust Projection

Rust should preserve the same semantic owners while using idiomatic modules, visibility, traits, crates, binaries, ownership, and lifetimes. Do not imitate TypeScript dot filenames.

## Semantic mapping

```text
product model/policy    private modules and domain types
use case                application function/struct/module with explicit input/output
capability Port         trait owned by the application side
live adapter            provider/storage module implementing the trait
public surface          facade module and deliberate re-exports
composition root        binary crate or host module constructing implementations
resource ownership      RAII, owned guards, cancellation tokens, structured task scopes
boundary guard          pub/pub(crate), module privacy, crate dependency direction, clippy/custom checks
```

## Default crate pressure

Start with private modules in one crate. Create a crate when one or more are durable:

```text
several binaries need a stable public API
independent compilation or feature policy
external distribution
trust or unsafe boundary
independent ownership
stable reuse with meaningful dependency direction
```

Do not create a crate per directory or domain noun.

## Suggested workspace shape

Conditional multi-host example:

```text
crates/
  domain/                  # only if a real shared stable core is earned
  application/             # use cases and application-owned traits
  adapters-postgres/       # provider-specific implementation when separation is useful
  host-api/
  host-worker/
```

A smaller application may keep:

```text
src/
  domain/
  application/
  adapters/
  host/
  main.rs
```

Use Rust conventions (`mod.rs` only when the edition/tooling style prefers it, otherwise named module files). Avoid one universal folder profile across existing Rust projects.

## Traits

Place the trait with the side that owns the capability semantics, not automatically with the adapter. Keep traits small and use-case-relevant. Avoid exposing provider types or forcing async traits where the application does not need them.

## Ownership and resources

Use ownership and RAII to keep acquisition and release local. Long-lived tasks still need a supervisor, cancellation, join, error, and shutdown policy; spawning a task does not define its lifetime.

## Error semantics

Distinguish expected application errors, infrastructure errors, cancellation, timeout, and unknown external outcome. `anyhow` may be appropriate at a host boundary, while public application surfaces often benefit from typed errors.

## Unsafe and FFI

Treat `unsafe`, FFI, and OS handles as explicit trust and lifecycle boundaries. Wrap them behind the smallest safe API and test invariants at the boundary.

## Concurrency

Prefer ownership transfer, message passing, immutable data, or single-state owners before shared `Arc<Mutex<_>>`. When shared locking is necessary, keep the invariant and lock order local to the owning API.

## Related knowledge

- Use [Source topology and semantic naming](source-topology-and-semantic-naming.md) for cross-ecosystem invariants.
- Use [Changeability, modularity, and repository shape](changeability-modularity-and-repository-shape.md) before creating crates.
- Use [Composition roots and lifetimes](composition-roots-and-lifetimes.md) for binary/host ownership.
- Use [Consistency, events, and shared state](consistency-events-and-shared-state.md) for concurrency semantics.
- Return to the [EAA map](../SKILL.md).
