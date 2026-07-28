# Knowledge Near Work and Plain Text

> **Build Documentation In; Do Not Bolt It On.** Durable knowledge should live near the decisions, interfaces, commands, and code that keep it current, using forms that people and general tools can recover.

Long-lived project knowledge should remain readable, searchable, comparable, and recoverable independently of one proprietary interface.

## Plain text as the default interchange surface

Prefer Markdown, source, schemas, configuration, command output, and other self-describing text for durable knowledge. Plain text is not unstructured; it is a format that people and general tools can inspect, diff, search, and transform.

A binary or external system may still be authoritative. Provide an open route, export, or concise durable explanation when future work would otherwise depend on a disappearing GUI or personal memory.

## Keep knowledge near the change

Place knowledge where the responsible reader is likely to encounter the need:

```text
product meaning        -> product/SSoT current home
public protocol        -> protocol/schema plus usage route
architecture boundary  -> architecture home plus source-adjacent route
strange source choice  -> local comment or README explaining why
operational recovery   -> runbook near commands and observability
repeated defect         -> test/assertion/tool guard plus durable explanation when needed
```

Do not copy the same rule into every location. Link or derive from the owner.

## Comments

Code already explains how. Comments should preserve why, constraints, surprising safety properties, abandoned alternatives, or external contracts that names and types cannot carry.

Remove comments that merely narrate the current line; they create a second implementation to maintain.

## Chat and Agent output

Temporary conversation is working material. Move stable terms, decisions, constraints, commands, and acceptance boundaries into durable project knowledge before the conversation becomes the only route.

Do not preserve every reasoning transcript. Preserve the meaning that future work needs.

## Engineering logs

A low-friction daybook can preserve observations, commands, hypotheses, and decisions during investigation. It does not become authority automatically. Promote only durable conclusions to the owning Home, test, command, or source boundary.

## Related knowledge

- Use [Multi-entry discovery](multi-entry-discovery.md) to connect knowledge near source to durable owners.
- Use [Freshness and invalidation](freshness-and-invalidation.md) for derived or external material.
- Use [Current Home and knowledge roles](current-home-and-knowledge-roles.md) before promoting notes.
- Return to the [Docs Governance map](../SKILL.md).
