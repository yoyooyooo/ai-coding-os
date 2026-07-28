# Source-Document Alignment

Source and documentation answer different questions, but they must remain mutually discoverable when a change in one can invalidate the other.

## Source is implementation authority

Source, schema, configuration, migrations, and dependency lockfiles describe what implementation exists. They do not automatically define intended product meaning or accepted architecture.

## Durable knowledge explains the governing relationship

Architecture and Standards should make source relationships discoverable when names and types are not enough:

```text
formal use-case entry
final fact writer
external capability boundary
host composition root
resource owner and shutdown path
public compatibility boundary
migration fence and deletion condition
```

These routes are the documentation side of the Agent-legible change surface owned by `$evolvable-application-architecture`.

## Alignment outcomes

When durable knowledge and source disagree, classify the mismatch:

### Stale knowledge

The implementation changed legitimately and the document was not updated. Update or lower the document.

### Implementation drift

Source violates an accepted rule, boundary, or product meaning. Repair source or make the product/technical decision that changes the accepted knowledge.

### Candidate target

The document describes a future state. Label it as target or proposal and keep current architecture discoverable.

### Missing evidence

The source looks correct but the claimed runtime behavior has not been observed. Use `$product-harness-system` rather than promoting a claim from static inspection.

## Anchors

Use explicit links or source paths when they remain stable enough to reduce discovery cost. Do not create a universal anchor schema. A source module README, architecture map, or `AGENTS.md` route may be sufficient.

## Generated documentation

Generated API and schema docs should identify their generator or source. Generated material is a projection, not a second owner. Hand-edited generated output is a drift signal.

## Related knowledge

- Use [Current Home and knowledge roles](current-home-and-knowledge-roles.md) to decide which side owns the disputed meaning.
- Use [Freshness and invalidation](freshness-and-invalidation.md) to record invalidating changes.
- Use [Multi-entry discovery](multi-entry-discovery.md) to add low-cost routes.
- Use `$evolvable-application-architecture` causal diagnosis when runtime behavior is the problem.
- Return to the [Docs Governance map](../SKILL.md).
