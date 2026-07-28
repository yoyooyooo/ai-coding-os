# Product Language and Model

Names are compressed product models. Stable vocabulary lets product, code, tests, and documentation refer to the same concepts without repeatedly translating through page or database terminology.

## Product model elements

Use only the elements that matter to the capability:

```text
actors and stakeholders
objects and identities
relationships and ownership
states and transitions
actions and events
rules and semantic invariants
permissions and visibility
time, deadlines, retention, and version
outcomes and observable consequences
```

## Formal terms

A project term should answer:

```text
what it means
what it does not mean
its scope
nearby concepts that are often confused
which product or policy owner can change it
```

Keep important English terms when they are the external technical or domain language, even if project prose uses another language.

## Same word, different concept

A common modeling failure is one word carrying several lifecycles:

```text
Task -> user objective, runtime execution, queue message
Complete -> investigation finished, payment settled, record closed
Owner -> business accountable person, current assignee, technical maintainer
Status -> business state, request lifecycle, visibility, SLA, archive state
```

Split concepts when their owners, transitions, or failure semantics differ.

## Different words, same concept

Synonyms across business, UI, API, and database create authority drift. Select one canonical product term and map external or legacy aliases explicitly.

## Identity

Use stable product identity rather than mutable attributes such as email, phone number, display name, region code, or provider handle. External identifiers may be valuable references without becoming the internal identity.

## Invariant, policy, and configuration

```text
semantic invariant        true because the product would mean something else if violated
policy                    an accountable rule that may change independently
operational configuration runtime/environment choice that must not redefine product meaning
```

Do not make a semantic invariant a toggle. Do not hard-code a frequently changing policy as scattered control flow.

## Model pressure from naming

A concept that cannot be named often hides mixed responsibilities. Names such as `data`, `manager`, `process`, or `item` are signals to investigate, not automatic failures.

## Default home

When the project has no coherent alternative, shared language belongs in:

```text
docs/ssot/product-language.md
```

A small project may keep the glossary in `docs/product/README.md`. Do not create a separate file until the vocabulary has durable cross-capability use.

## Related knowledge

- Use [Workflow, state, and exceptions](workflow-state-and-exceptions.md) when concepts move over time.
- Use [Rules, permissions, quality, and metrics](rules-permissions-quality-and-metrics.md) for invariant/policy distinctions.
- Use [Default product knowledge shape](default-product-knowledge-shape.md) for the default home.
- Use `$evolvable-application-architecture` when product identity must map to fact authority.
- Return to the [Product Definition map](../SKILL.md).
