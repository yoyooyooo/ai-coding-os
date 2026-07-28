# Default Project Standard Surfaces

Portable conventions become most useful when a project can discover the adopted local projection without rereading the Skill package. This reference defines reserved project-owned standard surfaces. Create only the files whose rules are durable and actually used.

## Required router when `docs/standards/` exists

```text
docs/standards/README.md
```

The router names current standards, their scope, their enforcement or review surface, and deliberate project overrides. It does not duplicate every rule.

## Reserved default filenames

| Path | Role | Create when |
| --- | --- | --- |
| `docs/standards/source-topology-and-naming.md` | adopted directory, module, filename, public-surface, and dependency-direction conventions | contributors or Agents repeatedly need a stable source grammar |
| `docs/standards/architecture-profile.yaml` | compact project-readable summary of selected architecture defaults and deliberate exceptions | several tools, hosts, or contributors need the same structured profile |
| `docs/standards/naming-vocabulary.yaml` | project-owned canonical terms, implementation qualifiers, aliases, and deprecated names | terminology drift or machine lookup is a recurring problem |
| `docs/standards/verification-policy.md` | stable verification command roles, dependency realities, and claim boundaries | the project has repeatable verification surfaces worth routing consistently |

These filenames are portable defaults. A coherent existing project may use different names; map them once in `docs/standards/README.md` or `AGENTS.md` rather than creating duplicates.

## What belongs in a Standard

A Standard should state a rule that currently binds work, its scope, and how readers know whether it is satisfied. Good content includes:

```text
adopted source and filename grammar
public/private dependency direction
host and resource ownership rules
project-wide terminology that must stay stable
verification command roles and evidence limits
security or data-handling constraints that apply across capabilities
```

A proposal, aspiration, one-off report, tutorial, or copied industry practice is not a Standard merely because it is useful.

## Human-readable first

Prefer Markdown for rules and explanation. Add YAML or another structured representation when a real consumer benefits from stable fields. A structured profile summarizes adopted choices; it does not replace the owning narrative or create architecture authority by itself.

## Ownership

- `$docs-governance` owns Current Home, routing, freshness, and file admission.
- `$evolvable-application-architecture` owns source topology, semantic naming, architecture profile meaning, and dependency direction.
- `$frontend-architecture` and `$effect-best-practices` own their local extensions.
- `$product-harness-system` owns verification surface and claim semantics.
- The project owns the adopted copies.

## Templates

- [Standards router](../templates/standards-README.md)
- Use `$evolvable-application-architecture` for source-topology, architecture-profile, and naming-vocabulary templates.
- Use `$product-harness-system` for the verification-policy template.
- See the [Project Standards baseline example](project-standards-baseline-example.md) for the smallest conditional set.

## Related knowledge

- Use [Default documentation topology](default-documentation-topology.md) for first-level Home admission.
- Use [Document naming and local routing](document-naming-and-local-routing.md) for path grammar.
- Use `$evolvable-application-architecture` before changing source or architecture conventions.
- Return to the [Docs Governance map](../SKILL.md).
