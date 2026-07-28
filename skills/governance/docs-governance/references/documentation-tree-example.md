# Documentation Tree Example

This example shows the portable documentation default for a product with durable product, semantic, engineering, and architecture knowledge.

```text
docs/
  README.md
  product/
    README.md
    product-brief.md
    case-review.md
  ssot/
    README.md
    product-language.md
  standards/
    README.md
    source-topology-and-naming.md
    architecture-profile.yaml
    naming-vocabulary.yaml
    verification-policy.md
  architecture/
    README.md
    fact-authority-map.md
    repository-topology.md
  adr/                         # conditional: durable accepted technical decisions exist
    README.md
    0001-use-postgres.md
  runbook/                     # conditional: operational recovery knowledge is durable
    README.md
    provider-timeout-reconciliation.md
```

## Defaults used

- `docs/README.md` is the project documentation router.
- `product`, `ssot`, `standards`, and `architecture` use the portable first-level names.
- ordinary files use kebab-case;
- top-level homes have local `README.md` routers;
- ADR files use numeric prefixes because order and stable citation are meaningful.

## Conditional elements

- `adr/` appears because the project has accepted technical decisions worth retaining.
- `runbook/` appears because provider timeout and reconciliation are operational responsibilities.

## Intentionally omitted

```text
roadmap/
reports/
features/
design/
product-harness/
protocols/
security/
data/
research/
evals/
```

The project has no durable pressure for those homes yet.

## Next structural pressure

A `product/case-review/` partition would become useful only if the capability accumulates several independently linked documents or a distinct owner/update cadence.

## Related Skills

- `$docs-governance`
- `$product-definition`
