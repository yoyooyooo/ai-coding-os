# Harness Lifecycle and Placement

## Lifecycle

```text
candidate
  useful discovery surface; semantics or stability may still evolve

accepted
  stable enough for normal Agent reuse

regression
  expected CI or release coverage

retired
  replaced by equivalent coverage or intentionally removed
```

Promotion depends on stable capability semantics, stable entrypoint, honest
environment labels, useful failure localization, and acceptable flake risk. It
does not imply the entire product capability is complete.

## Code placement

Business-specific harnesses stay near the authority or feature they exercise:

```text
apps/api/src/modules/orders/
  order.checkout.retry.harness.ts
  order.repository.postgres.contract.test.ts

apps/web/src/features/orders/
  order.checkout.surface.tsx
  order.checkout.browser.test.ts
```

Generic runner/discovery tooling may live under:

```text
tooling/verification/
```

A package such as `packages/testkit` is admitted only for business-neutral,
truly reused primitives. Do not centralize all business harnesses in a generic
`testing`, `mocks`, or `harness` package.

Create a separate `apps/harness-*` host only when it has a real independent
runtime/resource lifecycle.

## Docs placement

`$docs-governance` owns the final decision. Typical project homes:

```text
docs/standards/verification-policy.md
  command conventions, environment labels, CI/opt-in rules

docs/product-harness/**
  stable scenario/descriptor references, coverage, lifecycle, gaps

docs/interface-capabilities/**
  user-facing interface semantics, not harness steps

docs/reports/**
  retained evidence summary when audit/navigation requires it
```

Raw run artifacts belong in the test/artifact system, not copied into durable
docs by default.

If a project explicitly uses Goal Proof, its Goal Pack may reference Harness IDs
or results. Harness doctrine does not depend on Goal Proof and does not duplicate
Goal Pack lifecycle.
