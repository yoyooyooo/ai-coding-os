# Project Standards Baseline Example

A project that has adopted durable source, naming, and verification conventions may use this small Standards set:

```text
docs/
  standards/
    README.md
    source-topology-and-naming.md
    architecture-profile.yaml
    naming-vocabulary.yaml
    verification-policy.md
```

## Defaults used

- `README.md` routes the binding Standards and explains their scope.
- `source-topology-and-naming.md` is the narrative authority for directories, filenames, public surfaces, and dependency direction.
- `architecture-profile.yaml` is a compact structured summary for repeated lookup; it does not replace architecture meaning.
- `naming-vocabulary.yaml` exists because stable project terms and provider qualifiers are repeatedly reused.
- `verification-policy.md` maps stable command roles and claim limits.

## Conditional elements

Only `source-topology-and-naming.md` may be needed in a small project. Add the structured profile or vocabulary only when contributors or tools actually consume them. Do not create empty Standards for symmetry.

## Project override

An established repository may keep `engineering/`, `conventions.md`, or another coherent structure. Map it in `docs/README.md` or `AGENTS.md`; do not duplicate the same rules under portable filenames.

## Related Skills

- `$docs-governance`
- `$evolvable-application-architecture`
- `$product-harness-system`
