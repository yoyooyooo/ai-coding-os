---
name: docs-governance
description: Govern project knowledge Current Homes, discovery routes, freshness, documentation topology, naming, and cleanup when documents compete for authority, Agents cannot discover knowledge from code/tests/errors, docs conflict with source or runtime reality, working notes look authoritative, or documentation structure drifts across projects.
---

# Docs Governance

Docs Governance makes project knowledge discoverable from the Agent's current location and gives each scoped meaning one Current Home. It does not require a universal reading sequence or a metadata schema on every file.

## Semantic anchors

- **One Scoped Meaning, One Current Home.** A scoped current claim has one authoritative home; maps, reports, and local notes route to it instead of cloning it.
- **Route Is an Edge, Not a Sequence.** Documentation should be enterable from source, failure, term, command, or repository entry without imposing one reading order.
- **Freshness Is Part of Meaning.** Knowledge is incomplete when readers cannot tell which decisions, versions, environments, observations, or dates can invalidate it.
- **Build Documentation In; Do Not Bolt It On.** Keep durable knowledge close to the decisions, interfaces, commands, and code that keep it alive.
- **Shape Must Be Earned.** New homes, partitions, identifiers, registries, and schemas need real authority, ownership, lifecycle, navigation, or machine-consumer pressure.

```text
Authority     who currently owns a scoped meaning
Route         a low-cost edge from a real entry point to that authority
Freshness     what the knowledge depends on and what invalidates it
Default shape the portable topology and naming used when the project is silent
Earned shape  whether additional structure solves a real navigation, ownership, or policy problem
Cleanup       removing, lowering, merging, or relocating misleading and obsolete knowledge
```

## Enter from the current pressure

| Current pressure | Continue into |
| --- | --- |
| two documents both claim to be current, or source/observation is mistaken for product authority | [Current Home and knowledge roles](references/current-home-and-knowledge-roles.md) |
| the repository needs a deterministic first-level documentation topology | [Default documentation topology](references/default-documentation-topology.md) |
| file names, README routers, numbering, or depth are inconsistent | [Document naming and local routing](references/document-naming-and-local-routing.md) |
| adopted cross-project source, architecture, naming, or verification rules need stable project-owned files | [Default project Standard surfaces](references/default-project-standard-surfaces.md) |
| the Agent needs stable project authority routes, commands, constraints, or language policy | [Repository Agent entry](references/repository-agent-entry.md) |
| knowledge cannot be found from source, tests, errors, terms, or repository entry points | [Multi-entry discovery](references/multi-entry-discovery.md) |
| a document may become stale when code, version, environment, decisions, or runtime behavior changes | [Freshness and invalidation](references/freshness-and-invalidation.md) |
| a new folder, identifier, registry, graph, or schema is being proposed | [Earned shape and identifiers](references/earned-shape-and-identifiers.md) |
| important knowledge exists only in chat, GUI, personal memory, or far from the work | [Knowledge near work and plain text](references/knowledge-near-work-and-plain-text.md) |
| documentation and implementation need explicit alignment without confusing authority | [Source-document alignment](references/source-document-alignment.md) |
| knowledge must be merged, moved, lowered, retained as history/future, or deleted | [Cleanup, history, and future](references/cleanup-history-and-future.md) |

These are independent surfaces. Fixing one broken route does not require redesigning the entire docs tree.

## Minimum distinctions

Prefer ordinary prose. Add metadata only when physical placement or a real machine consumer needs it.

```text
current authority  accepted meaning or binding constraint
source / evidence  implementation structure or bounded observation
working material   investigation, draft, plan, or temporary synthesis
future              accepted target or unaccepted candidate, visibly separated
history             a decision or explanation that used to be current
```

A file may contain more than one role, but each current claim still needs an owner and a reachable route.

## Portable documentation default

When durable project documentation exists:

```text
docs/README.md is required as the documentation router.
```

The default first-level vocabulary is defined in [Default documentation topology](references/default-documentation-topology.md). Core homes are reserved defaults and are created when their role first gains durable content; conditional homes appear only under explicit pressure. Do not create empty folders for symmetry.
When `docs/standards/` exists, use [Default project Standard surfaces](references/default-project-standard-surfaces.md) before inventing parallel filenames for source topology, architecture profile, naming vocabulary, or verification policy.

## Multi-entry project knowledge

Healthy projects support routes such as:

```text
failing test -> affected invariant/capability -> owning product/architecture knowledge
source module -> formal use case -> fact writer / external capability / composition root
runtime error -> reproduction command -> first wrong state -> owning contract or decision
product term -> accepted meaning -> source / projection / proof routes
ADR or Standard -> source/evidence that can confirm or challenge it
```

`AGENTS.md`, the root README, and `docs/README.md` are maps, not mandatory roots.

## Structure must be earned

Add partitions only when they protect durable:

```text
independent ownership or permission
retention or lifecycle
reader audience and update cadence
repeated navigation pressure
machine consumption or stable citation
```

Visual symmetry, maturity labels, project phases, and "we may need it later" are not reasons.

## Domain meaning remains with domain owners

- Product outcomes, rules, permissions, and quality belong to `$product-definition`.
- Fact writing, transactions, modules, and migration belong to the relevant architecture owner.
- Runtime observations, reproduction, and regression belong to `$product-harness-system` or the project's test/operations surface.
- Docs Governance owns the Current Home, route, freshness, naming, and lifecycle of that knowledge, not its domain meaning.

## Blocking boundary

Stop only the affected knowledge change when:

```text
two plausible Current Homes cannot be distinguished
cleanup would lose important source/evidence or break the only route
resolution requires a new product, safety, legal, policy, or public-contract decision
the repository operation may be irreversible
```

Preserve the conflict, identify the smallest external decision, and continue unrelated routing, naming, freshness, or cleanup work.

## Output principle

Make the smallest change that restores one Current Home and low-cost discovery: link, clarify, lower, merge, move, flatten, retain, rename, or delete. Apply the portable default when the project is silent. Add metadata, a new home, a registry, or a durable graph only when simpler forms cannot solve the real problem.
