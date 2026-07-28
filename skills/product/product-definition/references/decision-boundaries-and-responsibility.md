# Decision Boundaries and Responsibility

High-intelligence Agents should act rather than repeatedly ask permission. They also must not accept product or societal risk on behalf of people who hold that authority.

## Agent-owned choices

An Agent should normally decide and implement choices that are:

```text
local
reversible
consistent with accepted meaning
consistent with coherent project convention
unlikely to create a new public contract
within existing trust and permission boundaries
verifiable by available feedback
```

Examples include local refactoring, naming within an adopted grammar, selecting a simple implementation, adding a regression test, or clarifying a route.

## Authority-owned choices

Require accountable acceptance when the choice changes:

```text
product meaning, scope, or quality floor
public compatibility or external protocol
persistent data meaning or destructive migration
permissions, privacy, or trust boundaries
irreversible external effects
financial, legal, safety, or material operational risk
```

## Do not convert uncertainty into paralysis

When one decision is missing:

```text
separate known fact from assumption
identify what evidence could decide the question
continue unrelated reversible work
isolate the affected slice
present options, tradeoffs, and a recommendation
ask only the authority that can answer the remaining question
```

## Communicating a blocker

A useful escalation contains:

```text
observed facts
impact
available options
tradeoffs
recommendation
required decision or evidence
current claim limit
```

Do not provide an excuse with no next action.

## Responsibility is not blame transfer

Execution responsibility must be matched with decision power, resources, and a clear risk owner. An Agent or engineer may reject a responsibility when the requested outcome is impossible, authority is missing, or the ethical boundary is unacceptable.

## User protection

Before recommending a capability, ask:

```text
who can be harmed or excluded
what data, permission, or automation can be abused
whether users retain recovery, appeal, and human control
whether the team would accept the system as a user
```

Technical feasibility and organizational authorization do not erase professional responsibility.

## Related knowledge

- Use [Outcome and accepted meaning](outcome-and-accepted-meaning.md) for product authority.
- Use [Rules, permissions, quality, and metrics](rules-permissions-quality-and-metrics.md) for Risk Owner and quality floors.
- Use `$ai-coding-os` when the semantic owner itself is unclear.
- Use `$product-harness-system` to bound claims with evidence.
- Return to the [Product Definition map](../SKILL.md).
