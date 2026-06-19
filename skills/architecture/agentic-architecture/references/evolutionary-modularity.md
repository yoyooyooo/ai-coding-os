# Evolutionary Modularity

Use this reference when the system has a god application service, global mutable
state, giant client, universal result type, or modules that cannot evolve
without repository-wide edits.

## Target Shape

Prefer a modular monolith with a thin application facade:

```text
ApplicationFacade
  -> ConversationUseCases
  -> GovernanceUseCases
  -> WorkUseCases
  -> ResultUseCases
  -> BillingUseCases
  -> ...

Shared Application Kernel
  -> CommandContext
  -> authorization / policy
  -> UnitOfWork factory
  -> capability ports
  -> event/outbox/audit support
```

The facade offers a coherent product API but does not own every map, cache,
registry, adapter, or invariant.

## Thin Facade Test

A facade is thin when it primarily:

- exposes use-case-oriented entry points;
- creates or receives command context;
- delegates to one owning module;
- coordinates an explicit cross-module use case;
- returns a typed outcome and commit receipt.

It is too thick when it stores all domain state, holds per-command caches,
contains every projection, selects vendors, or lets callers access internals.

## Module Boundary Rules

1. Keep module state private.
2. Expose commands and queries, not internal collections.
3. Use references rather than shared mutable objects across cells.
4. Put cross-cell orchestration in an application use case, not in an adapter.
5. Keep invariants close to the state they protect.
6. Separate test fixture construction from public production APIs.
7. Enforce dependency direction mechanically where the language permits.

## Specific Outcomes, Shared Receipt

Avoid a universal outcome with optional fields for every operation. Prefer:

```text
UseCaseResult<SpecificOutcome> {
  value: SpecificOutcome
  receipt: CommitReceipt
}

CommitReceipt {
  accepted_fact_refs
  event_refs
  outbox_refs
  idempotency_disposition
  causal_or_version_frontier
  inspect_or_trace_ref
}
```

This lets new product concepts evolve without widening every existing command.

## Stable Versus Evolvable Contracts

Usually stabilize:

- identity and source references;
- command context and authorization inputs;
- idempotency semantics;
- candidate/decision/materialization stages;
- commit receipt and evidence references;
- adapter capability and diagnostic contracts.

Allow active evolution of:

- domain classifications and workflows;
- relationships between product objects;
- projection and UI vocabulary;
- routing, memory, and interaction policies;
- adapter selection and deployment profiles.

## When to Split Further

Promote a module to a separate package/crate when compile-time dependency
control, ownership, or build isolation is useful. Promote to a separate process
only when deployment, scaling, failure isolation, trust, or data residency
requires it.

Do not use network boundaries to compensate for public mutable state or unclear
fact authority. Fix the semantic boundary first.
