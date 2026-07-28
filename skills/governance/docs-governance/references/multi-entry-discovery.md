# Multi-entry Discovery

A project should be understandable from the place where a real question appears. Central indexes help, but they must not be the only path to knowledge.

## Useful entry surfaces

```text
current question or product term
source file, module, package, or host
failing test or reproduction command
runtime error, log, trace, or alert
schema, protocol, migration, or configuration
ADR, Standard, product capability, or architecture document
AGENTS.md, root README, docs/README.md, or local README
```

## Route patterns

### From a failing test

```text
failing case
  -> violated product rule or technical invariant
  -> owning use case/state owner
  -> fact writer or external capability
  -> Current Home for accepted meaning
```

### From source

```text
handler/component
  -> formal use case or user intent
  -> fact writer / client / projection owner
  -> composition root or host
  -> verification entry
```

### From a runtime symptom

```text
error/trace
  -> reproduction command
  -> first wrong state
  -> owning contract, resource, or decision
  -> regression layer
```

### From a term

```text
term
  -> glossary/SSoT definition
  -> relevant product capability
  -> source symbol and public contract
  -> proof or runtime observation
```

## Route quality

A good route:

- reaches the owner in a few meaningful hops;
- names why the link matters;
- avoids duplicating the destination's content;
- remains valid when implementation detail changes;
- lets a reader enter locally without reading an entire hierarchy.

A link list with no semantic labels is less useful than a few explicit relationships.

## Knowledge near source

Source modules may contain a short README, public-surface comment, or link when the relationship is not obvious from names and types. Do not paste the full product model beside every implementation.

## Generated and external systems

When authority lives in an external product or policy system, provide a stable route and, when necessary, an explicitly labeled snapshot. A copied export does not become the Current Home automatically.

## Related knowledge

- Use [Repository Agent entry](repository-agent-entry.md) for root-level project routes.
- Use [Source-document alignment](source-document-alignment.md) for links between source and durable knowledge.
- Use `$evolvable-application-architecture` for implementation-side Agent-legible change surfaces.
- Return to the [Docs Governance map](../SKILL.md).
