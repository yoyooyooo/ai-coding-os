# Forward Evolution and Migration

Architecture evolution changes authority, contract, data, or runtime shape while the system remains useful. It is not a flag-day rewrite with a new name.

## Preserve semantics; re-earn scaffolding

Keep accepted product meaning and critical invariants stable unless an accountable decision changes them. Recreate packages, frameworks, adapters, and temporary bridges only when the new environment still needs them.

## Migration dimensions

A migration may move one or more of:

```text
fact authority
storage schema
public API or protocol
provider implementation
runtime host or deployable
read model or event contract
source module/package boundary
```

Name the dimension. Do not describe every migration as "move the service".

## Authority migration

A safe authority move normally makes discoverable:

```text
old source of truth
new source of truth
bridge or synchronization relationship
which writer is allowed at each stage
fence preventing old writes after promotion
divergence detection and reconciliation
delete/retire conditions
```

Before the new writer is promoted, prove it can satisfy the required invariants. Before the old writer is removed, prove no live path can still use it.

## Expand and contract

For schema and contract changes:

```text
expand       accept old and new representation
migrate      move producers/consumers/data
observe      detect divergence and remaining old use
contract     remove the old representation
```

This relation is useful, but it is not a mandatory four-stage project workflow. Some migrations are atomic; others need longer coexistence.

## Read and write strategies

Use deliberately:

```text
single write + dual read
dual write with reconciliation
shadow write
backfill from authoritative source
change-data capture
versioned protocol
compatibility adapter
```

Dual write is not automatically safe. Define ordering, failure, idempotency, and divergence ownership.

## Rollback

Rollback is valid only while the old system can still represent the accepted facts and no irreversible external effect has crossed the boundary. Otherwise design forward recovery or compensation.

## Deletion is part of migration

Temporary bridges, flags, aliases, duplicate fields, and old routes need explicit deletion conditions. A permanent "temporary" path becomes a second authority.

## AI-generated takeover

Do not preserve generated scaffolding merely because it exists. Preserve accepted behavior, real data, public compatibility, and useful tests; re-earn internal structure from current pressure.

## Related knowledge

- Use [Fact authority and candidate boundaries](fact-authority-and-candidate-boundaries.md) for writer promotion.
- Use [Consistency, events, and shared state](consistency-events-and-shared-state.md) for dual-write and reconciliation.
- Use [Reading and taking over existing systems](reading-and-taking-over-existing-systems.md) before redesign.
- Use `$product-harness-system` for restart, replay, divergence, and rollback evidence.
- Use `$docs-governance` to align current and target documentation.
- Return to the [EAA map](../SKILL.md).
