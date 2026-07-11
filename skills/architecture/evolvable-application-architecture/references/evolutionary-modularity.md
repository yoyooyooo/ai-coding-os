# Evolutionary Modularity

Use this reference when the system has a god application service, global mutable
state, giant client, universal result type, or modules that cannot evolve
without repository-wide edits.

## Target Shape

Prefer an authority-first modular monolith with one system hexagon and multiple
private authority cells:

```text
ApplicationFacade
  -> OrdersUseCases
  -> AccountsUseCases
  -> ReviewUseCases
  -> BillingUseCases
  -> CollaborationUseCases
  -> ...

Authority cells
  -> private state and invariants
  -> typed commands / queries
  -> specific decisions and changes

Shared application kernel
  -> CommandContext
  -> identity / authorization / policy
  -> transaction or UnitOfWork factory
  -> capability ports
  -> event/outbox/audit support
```

The facade offers a coherent product API but does not own every map, cache,
registry, adapter, projection, or invariant.

## Thin Facade Test

A facade is thin when it primarily:

- exposes use-case-oriented entry points;
- creates or receives command context;
- delegates to one owning cell;
- coordinates an explicit cross-cell use case;
- returns a typed outcome and commit receipt.

It is too thick when it stores all domain state, holds per-command caches,
contains every projection, selects vendors, or gives callers internal objects.

## Internal Cells Are Not Ports

Do not wrap every authority cell in a capability interface for diagram symmetry.
Internal cell-to-cell collaboration is an application protocol:

```text
typed command or query
stable FactRef / SourceRef
explicit orchestration
immutable internal obligation + typed receipt when asynchronous
```

Use a capability port only when the boundary is genuinely outer or replaceable.
Avoid a universal JSON command bus that erases transaction ownership, schema,
authorization, and error semantics.

## Module Boundary Rules

1. Keep module state private.
2. Expose commands and queries, not internal collections.
3. Use references rather than shared mutable objects across cells.
4. Put cross-cell orchestration in an application use case, not an adapter.
5. Keep invariants close to the state they protect.
6. Separate test fixture construction from public production APIs.
7. Enforce dependency direction mechanically where the language permits.
8. Give asynchronous internal obligations stable identity, target authority,
   ordering policy, and receipt semantics.

## Specific Outcomes, Shared Receipt

Avoid a universal outcome with optional fields for every operation. Prefer:

```text
UseCaseResult<SpecificOutcome> {
  value
  CommitReceipt {
    accepted_fact_refs
    event_refs
    outbox_refs
    idempotency_disposition
    causal_or_version_frontier
    inspect_or_trace_ref
  }
}
```

This lets new product concepts evolve without widening every existing command.

## Stable Versus Evolvable Contracts

Usually stabilize:

- identity, source, and authority-epoch references;
- command context and authorization inputs;
- idempotency semantics;
- command/candidate/decision/materialization stages;
- commit receipt and evidence references;
- adapter capability and diagnostic contracts.

Allow active evolution of:

- domain classifications and workflows;
- relationships between product objects;
- projection and UI vocabulary;
- routing, review, collaboration, and interaction policy;
- adapter selection and deployment profiles.

## When to Split Further

Promote a module to a package/crate when compile-time dependency control,
ownership, or build isolation is useful. Promote to a separate process only when
deployment, scaling, failure isolation, trust, lifecycle, or data residency
requires it.

Do not use network boundaries to compensate for public mutable state or unclear
fact authority. Fix the semantic boundary first.
