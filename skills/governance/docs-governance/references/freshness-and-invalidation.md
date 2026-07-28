# Freshness and Invalidation

> **Freshness Is Part of Meaning.** A durable claim is incomplete when readers cannot tell which decision, source, version, environment, observation, or date can invalidate it.

A document is trustworthy only to the extent that readers can understand what it depends on and what could make it stale.

## Freshness questions

For a durable claim, be able to answer:

```text
what authority or source supports this claim
which scope, environment, or version it applies to
what change would invalidate it
who is expected to notice or update it
what evidence can confirm or challenge it
```

This can be expressed in prose and links. Do not require frontmatter everywhere.

## Common invalidators

```text
accepted product or policy decision
public API or protocol change
source boundary or fact-writer change
database schema or migration
provider or dependency major version
runtime topology or host-lifetime change
security classification or permission change
observed production behavior that contradicts the model
```

## Freshness is not recency

A recent report may be point-in-time evidence, not current authority. An old invariant may remain valid for years. Timestamps are useful signals but weak proof.

## Derived material

Generated docs, diagrams, client code, and snapshots should identify their source and regeneration route when practical. If regeneration is not available, readers need to know that the copy can drift.

## Staleness handling

When a claim is no longer reliable:

- update it when the owner and new meaning are clear;
- lower the claim and link to the current owner;
- mark temporary drift when resolution is pending;
- move it to history when its rationale remains useful;
- delete it when it has no remaining explanatory or evidentiary value.

Do not leave a strong current title with a small stale warning buried at the bottom.

## Version-sensitive technical knowledge

For libraries such as Effect, framework APIs, or infrastructure behavior, the local dependency lockfile and installed declarations are stronger than generic examples. Durable docs should say when a major-version or runtime assumption changes the answer.

## Related knowledge

- Use [Current Home and knowledge roles](current-home-and-knowledge-roles.md) to distinguish authority from evidence.
- Use [Source-document alignment](source-document-alignment.md) when implementation changes invalidate architecture docs.
- Use [Cleanup, history, and future](cleanup-history-and-future.md) to retain or remove stale material.
- Return to the [Docs Governance map](../SKILL.md).
