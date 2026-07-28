# Document Naming and Local Routing

Predictable names lower cross-project search cost without requiring every project to have the same content.

## Default naming

```text
ordinary directory or file             kebab-case
local router                            README.md
append-only ordered decision            0001-short-title.md
ordinary document                       no numeric prefix
project glossary                        product-language.md or glossary.md
current architecture overview           README.md or current-architecture.md
point-in-time report                     <subject>-<date-or-scope>.md when date is material
```

Use English for paths, commands, schema fields, protocol names, and code symbols unless an external contract requires otherwise. Project narrative prose follows the project language policy.

Do not create singular/plural twins or synonyms for the same role:

```text
standard/ + standards/
architecture/ + architectures/
decision/ + adr/
requirements/ + features/ + product/requirements/ without a declared distinction
```

## Router contract

A top-level documentation home should have a `README.md` when it exists. The router should remain thin and normally state:

```text
scope and role
what it owns
what it must not own when confusion is likely
current routes or entry points
local naming or partition rules
conflict or supersession behavior when relevant
```

A child partition README is a local router. It inherits the parent's authority role and should not restate a competing global doctrine.

## Numbering

Use numeric prefixes only when order and stable citation are part of the meaning, most commonly append-only decisions:

```text
docs/adr/0001-adopt-postgres.md
docs/adr/0002-separate-worker-host.md
```

Do not number ordinary documents merely to make a tree look organized. Numeric order often turns into a false reading sequence and makes insertion expensive.

## File granularity

Keep one coherent meaning together until one of these pressures appears:

```text
independent authority or owner
independent update cadence
independent retention or access policy
repeated direct linking to one subtopic
repeated edit conflicts
machine consumption
```

Split by stable concern, not by arbitrary length. A long but coherent document may be better than five fragments with no route.

## Naming by semantic role

Prefer names that survive implementation changes:

```text
order-lifecycle.md
payment-idempotency.md
fact-authority.md
source-topology-and-naming.md
```

Avoid names that describe temporary activity or vague content:

```text
notes.md
final-v2.md
new-architecture.md
misc.md
agent-output.md
phase-2-plan.md
```

## Project override

Keep a coherent local convention. Record only material differences in `docs/README.md` or `AGENTS.md`. Do not create a second naming dialect inside the same repository.

## Template

Use the [decision record template](../templates/decision-record.md) when an ordered accepted decision collection is genuinely present.

## Related knowledge

- Use [Default documentation topology](default-documentation-topology.md) for first-level homes.
- Use [Repository Agent entry](repository-agent-entry.md) for repository-level routing.
- Use [Earned shape and identifiers](earned-shape-and-identifiers.md) before assigning IDs broadly.
- Return to the [Docs Governance map](../SKILL.md).
