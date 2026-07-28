# Current Home and Knowledge Roles

> **One Scoped Meaning, One Current Home.** Many representations may exist, but one current surface owns a scoped meaning and the others route, explain, derive, or preserve history.

A project can have many representations of the same subject without giving them equal authority. The governing question is not "which file is newest?" but "which surface owns this kind of meaning in this scope?"

## Question-scoped authority

```text
what should the product do?             accepted product/business decision
what does a shared term mean?           project SSoT or accepted semantic decision
which rule currently binds work?        adopted Standard or accountable policy
why was a choice accepted?              applicable product decision or ADR
what does an interface accept?          adopted protocol/schema
what implementation exists?             source, schema, migration, configuration, lockfile
what behavior was observed?             executed test, Harness, runtime, browser, operations
what is being attempted or completed?    the project's selected execution/delivery surface
```

No document is globally highest for every question.

## Knowledge roles

### Current authority

Accepted meaning or a binding constraint. It can be changed only by its accountable owner or an accepted decision that updates it.

### Source input

Business material, legacy documents, stakeholder statements, external standards, user feedback, or imported data used to learn. A source can be valuable without being current authority.

### Source reality

Code, schema, configuration, dependencies, generated artifacts, and deployed topology. Source can expose documentation drift, but accidental implementation does not become intent by default.

### Observed evidence

A bounded runtime, test, browser, provider, or operational observation. It supports only the path, environment, and dependency reality actually exercised.

### Working material

Notes, investigations, plans, candidate models, and drafts. Working material may be excellent reasoning while remaining non-authoritative.

### Future

An accepted target or an unaccepted candidate. The two must not be conflated. Future material does not describe current implementation merely because it is approved.

### History

A decision, architecture, or explanation that used to be current. History remains useful when it explains why the current shape exists or prevents rediscovery of a rejected path.

## One scoped meaning, one Current Home

A Current Home may be a document, schema, source module, external system, or accountable decision surface. The rule is not "put everything in docs". The rule is that readers can find the owner and distinguish derived representations.

When two surfaces both look current:

- identify the exact claim and scope;
- identify the authority type each surface can legitimately hold;
- preserve source and evidence even when lowering their claim;
- update, supersede, link, or remove the competing current claim;
- do not let recency alone decide.

## DRY as authority, not textual deduplication

A shared rule may appear in product prose, code, tests, help text, and API contracts. DRY does not require one physical file. It requires one authoritative meaning and a reliable derivation or validation relationship for the other forms.

Two similar paragraphs may express different independently changing knowledge. Two different formats may express the same rule and therefore need a common owner.

## Decision impact

When an accepted decision changes another Current Home, the affected owner must eventually:

```text
update the Home
record temporary drift and lower the claim
or explain why the decision does not apply
```

The order is contextual; the obligation is not.

## Related knowledge

- Use [Default documentation topology](default-documentation-topology.md) to choose a default physical home.
- Use [Freshness and invalidation](freshness-and-invalidation.md) to explain when a claim becomes stale.
- Use [Source-document alignment](source-document-alignment.md) when source and durable knowledge diverge.
- Use [Cleanup, history, and future](cleanup-history-and-future.md) to lower or retire a competing claim.
- Return to the [Docs Governance map](../SKILL.md).
