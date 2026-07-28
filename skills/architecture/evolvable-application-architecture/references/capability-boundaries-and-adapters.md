# Capability Boundaries and Adapters

> **Ports Describe Capabilities, Not Providers.** Name the product-relevant power the application needs; contain provider protocol, credentials, failures, and lifetime details behind it.

A capability boundary lets application code depend on a product-relevant ability instead of a provider, transport, database, or framework implementation.

## When a boundary is earned

Create an application-owned Port when one or more are material:

```text
provider protocol or SDK should not leak to callers
credentials, trust, or permission need a boundary
failure and unknown-outcome semantics need normalization
resource lifetime or host construction differs from use-case logic
several implementations or test realities are valuable
replacement risk is plausible and costly
public compatibility requires an owned contract
```

Do not wrap every library or pure helper.

## Name the capability, not the provider

Prefer:

```text
PaymentAuthorization
DocumentStorage
CaseSearch
Clock
IdentityDirectory
```

over:

```text
StripeService
S3Manager
ElasticHelper
```

The live implementation may carry the provider qualifier.

## Contract shape

The Port should expose application meaning:

```text
normalized input and output
modeled failures meaningful to the caller
operation identity when duplicate/unknown outcomes matter
cancellation/deadline contract when relevant
no provider SDK, ORM, HTTP, or raw JSON types
```

Do not erase real provider differences behind a fictional universal interface. Keep provider-specific capabilities visible when they change product or operational decisions.

## Adapter responsibilities

A live adapter may own:

```text
protocol and SDK calls
credential and endpoint mapping
runtime decoding
provider error translation
timeout/retry policy that belongs at the provider boundary
resource acquisition and finalization
provider-specific observability
```

It must not decide product acceptance or write facts outside the governed use case.

## Fakes and replays

A fake is a behavioral substitute, not a silent production fallback. A replay reproduces recorded interaction and cannot prove live-provider behavior. Use contract/conformance tests to compare implementations where the contract is intended to be shared.

## Database boundaries

A repository Port is useful when the application needs a stable persistence capability and should not expose ORM records. Do not create one repository per table by reflex; shape it around use-case and aggregate needs.

## Related knowledge

- Use [Source topology and semantic naming](source-topology-and-semantic-naming.md) for filenames.
- Use [Use cases, transactions, and idempotency](use-cases-transactions-and-idempotency.md) for coordination.
- Use [Composition roots and lifetimes](composition-roots-and-lifetimes.md) for live selection.
- Use `$product-harness-system` for dependency reality and conformance evidence.
- Return to the [EAA map](../SKILL.md).
