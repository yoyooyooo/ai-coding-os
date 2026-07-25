# AI Coding OS Harness Contracts

These portable contracts keep Harness discovery and results interoperable
without creating a central verification workflow.

- **Proof Surface** separates observation surface, dependency reality,
  environment class, and owner-local proof focus.
- **Harness Descriptor** names a runnable entry, observable properties,
  exclusions, dependencies, and claim ceiling.
- **Harness Result** records the exact Proof Surface, observations, bounded
  support, and adjacent `not_proven`.

Writers emit Descriptor/Result `schema_version: 2`. The schemas retain v1 reader
compatibility but reject legacy `surface` / `environment`, known camelCase
aliases, and the former Descriptor `exercises` field on v2 artifacts. Unknown
extension data may still use explicit non-conflicting names. Pure static proof uses `dependency_reality: [none]`; `none` cannot be
combined with runtime dependency values. Use the [migration note](../migrations/v2-proof-evidence.md)
for legacy `surface`, `production_near`, `db_backed`, and `render_wiring` labels.

## Examples

- `examples/order-checkout-retry.descriptor.yaml`
- `examples/order-checkout-retry.result.yaml`

Suite audit validates both examples and the shared Proof Surface object. Durable
provenance remains optional unless CI, release, audit, or cross-artifact reuse
requires it.

## Empirical Unknowns

A Descriptor may be used as a bounded Probe Request. A Result separates `observed`, `supports`, `does_not_decide`, and `not_proven`. The probe can close an empirical unknown but cannot decide product, architecture, documentation, execution, or release authority.
