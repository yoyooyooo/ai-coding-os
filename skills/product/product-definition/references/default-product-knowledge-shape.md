# Default Product Knowledge Shape

Use this portable default when the project has no coherent adopted product-document convention. It provides stable cross-project homes and headings without requiring a complete PRD family.

## Default homes

```text
docs/product/README.md              product map, outcomes, scope, and current capability routes
docs/product/product-brief.md       product-wide outcome and Quality Boundary when durable
docs/ssot/product-language.md       shared terms, objects, states, and invariants
docs/product/<capability>.md        accepted capability definition
```

Create only the files that carry durable meaning. A small project may keep the brief and capability map together in `docs/product/README.md`.

## Capability definition headings

Use selectively:

```text
Outcome and user context
Actors and responsibilities
Objects, states, and invariants
Actions, rules, permissions, and policy
Workflow, time, exceptions, and recovery
Scope and explicit non-goals
Quality and acceptance boundary
Interface obligations
Open decisions and invalidating feedback
```

The headings create familiarity. They do not define a required authoring order, and an Agent should delete empty or irrelevant sections.

## Default file names

```text
product-brief.md
product-language.md
<capability>.md
<capability>-decision.md only when a durable product decision needs a separate record
```

Use kebab-case. Do not add numeric prefixes to ordinary capability documents.

## Product router

`docs/product/README.md` should link current capabilities, the product brief when present, shared language, and material product decisions. It should not become a duplicate of every capability.

## Templates

- [Product brief](../templates/product-brief.md)
- [Capability definition](../templates/capability-definition.md)
- [Product decision](../templates/product-decision.md)

These are prompts, not schemas. Remove sections that do not carry meaning.

## Project override

Preserve an existing coherent PRD or product-system convention. Map its local homes in `docs/README.md` or `AGENTS.md` rather than creating parallel artifacts.

## Example

See the [product capability example](product-capability-example.md).

## Related knowledge

- Use [Outcome and accepted meaning](outcome-and-accepted-meaning.md) for the brief.
- Use [Product language and model](product-language-and-model.md) for SSoT content.
- Use [Interface obligations](interface-obligations.md) for user-visible capability states.
- Use `$docs-governance` for first-level documentation topology and naming.
- Return to the [Product Definition map](../SKILL.md).
