---
name: evolvable-application-architecture
description: Design and evolve applications when small changes cross many modules, no one can name the final fact writer, business code calls databases or providers directly, replacing a dependency rewrites product logic, old writers cannot be fenced during migration, or an AI-generated MVP looks complete but cannot explain ownership and recovery.
---

# Evolvable Application Architecture

Architecture is not a static layer diagram. It is a set of relationships that lets the next real change be found, understood, implemented locally, observed, migrated, and eventually removed.

```text
accepted fact changes through a governed use case
external power enters through an application-owned capability boundary
composition roots choose live implementations and own their lifetimes
before authority moves, old writers are fenced
an observation supports only the path it actually exercised
```

## Semantic anchors

- **The Project Should Explain Itself.** A fresh Agent should be able to recover accepted meaning, the governed entry, the final writer, external capabilities, live composition, verification, and removal path.
- **One Fact, One Final Writer.** Within one consistency scope, each accepted fact has one final materialization authority, even when many processes can propose or observe it.
- **Candidates Propose; Authorities Materialize.** Commands, provider responses, imports, model output, drafts, and realtime frames remain candidates or observations until a governed use case accepts them.
- **Ports Describe Capabilities, Not Providers.** Application-owned boundaries name what the product needs and contain provider protocol, credentials, failure, and lifetime details.
- **Composition Chooses; It Does Not Decide.** A composition root selects live implementations and owns resources; it does not become product transition logic.

Ports, packages, Services, events, Actors, registries, deployables, and new layers must be earned by real change, failure, lifetime, trust, or reuse pressure.

## Permanent questions

### Who owns the accepted fact?

For every persistent fact, identify the final materialization authority, the relevant consistency scope, and any forbidden or legacy writers. Shared code or infrastructure does not grant write authority.

### How does a proposed change become authoritative?

A Command requests change. Provider responses, model output, realtime frames, imported files, and user drafts are candidates or observations. They become accepted facts only through a governed use case.

### Which external powers deserve an application-owned boundary?

Create a capability boundary when callers should not know provider protocols, credentials, failures, or lifetime details. An interface alone does not prove replaceability; substitutes need behavioral evidence.

### Who assembles and closes the live system?

A host composition root selects implementations, constructs resources, supervises background work, and closes them. Bootstrap does not own product transitions.

### How are failure, time, concurrency, permissions, and unknown outcomes contained?

Make writer, ordering, deadline, retry, interruption, partial failure, recovery, trust, and privilege visible where consequences occur. A timeout does not prove that an external effect did not happen.

### Can the next real change stay local?

Independent change axes should not force unrelated product meaning, database, worker, frontend, and deployment changes. Migrations need source of truth, bridge, fencing, divergence observation, and deletion conditions.

These are peer questions, not architecture steps.

## Enter from the current pressure

| Current pressure | Continue into |
| --- | --- |
| a fresh Agent cannot recover the complete change path for one capability | [Agent-legible change surface](references/agent-legible-change-surface.md) |
| final fact writer, candidate fact, or import relationship is unclear | [Fact authority and candidate boundaries](references/fact-authority-and-candidate-boundaries.md) |
| Commands, transactions, idempotency, outbox, or unknown outcome are unclear | [Use cases, transactions, and idempotency](references/use-cases-transactions-and-idempotency.md) |
| it is unclear whether a provider, database, model, filesystem, or plugin deserves a Port | [Capability boundaries and adapters](references/capability-boundaries-and-adapters.md) |
| Runtime, resources, background work, or live implementations lack an owner | [Composition roots and lifetimes](references/composition-roots-and-lifetimes.md) |
| multiple writers, events, shared state, CRDT, Saga, or imported facts need a consistency choice | [Consistency, events, and shared state](references/consistency-events-and-shared-state.md) |
| module, directory, package, repository, host, and deployable boundaries are being conflated | [Changeability, modularity, and repository shape](references/changeability-modularity-and-repository-shape.md) |
| a new project needs stable source and filename conventions | [Source topology and semantic naming](references/source-topology-and-semantic-naming.md) |
| a greenfield repository needs a compatible default application profile | [Default repository profile](references/default-repository-profile.md) |
| durable architecture knowledge needs stable project-owned filenames | [Default architecture knowledge shape](references/default-architecture-knowledge-shape.md) |
| authority, schema, API, or provider must move without a flag day | [Forward evolution and migration](references/forward-evolution-and-migration.md) |
| a reproducible symptom points to fact authority, use-case, capability, consistency, composition, or migration boundaries | [Architecture lens on the first wrong state](references/causal-diagnosis-and-first-wrong-state.md) |
| an existing or AI-generated system must be understood before redesign | [Reading and taking over existing systems](references/reading-and-taking-over-existing-systems.md) |
| product, frontend, architecture, and observed reality disagree | [Cross-owner reconciliation](references/cross-owner-reconciliation.md) |
| TypeScript backend shape is needed | [TypeScript backend projection](references/typescript-backend-projection.md) |
| Rust module/crate/host shape is needed | [Rust projection](references/rust-projection.md) |
| Agent runtime, activity, revision, artifact, or tool authority is being designed | [Agentic systems projection](references/agentic-systems-projection.md) |
| concrete mappings would help | [Scenario examples](references/scenario-examples.md) |

## Portable source defaults

Use [Source topology and semantic naming](references/source-topology-and-semantic-naming.md) for path grammar and [Default repository profile](references/default-repository-profile.md) for greenfield topology. A coherent existing repository remains authoritative; expose its local mapping rather than renaming it without material benefit.

## Invariants

```text
one accepted fact -> one final materialization authority within a consistency scope
Command           -> intent, not proof of change
provider result   -> candidate/observation until governed materialization
external detail   -> isolated where replacement, trust, or failure semantics matter
composition       -> selects implementations and owns lifecycle, not product meaning
migration         -> old writer fenced before authority promotion
```

## Common smells

- transport handlers write product facts directly;
- provider SDK or ORM types leak through the application core;
- every helper gets an interface or Service for symmetry;
- package boundaries are treated as fact authority;
- a host creates resources in feature modules or hooks;
- timeout is reported as failure without operation identity or reconciliation;
- events are used to hide ownership rather than express it;
- a rewrite is called a migration without a bridge, fence, or deletion condition;
- the repository has many layers but a fresh Agent still cannot find the writer, use case, composition root, or reproduction command.

## Adjacent owners

- Product meaning and quality belong to `$product-definition`.
- Frontend projection and interaction ownership belong to `$frontend-architecture`.
- Effect execution and resource mechanics belong to `$effect-best-practices`.
- Runtime proof, general investigation mechanics, and regression placement belong to `$product-harness-system`.
- Documentation placement and local routing belong to `$docs-governance`.

## Output principle

Describe the minimum architecture that makes the current authority, change path, failure, lifetime, and verification surface legible. Apply portable naming and repository defaults only where the project is silent. Do not create a complete pattern set, package family, or service layer for symmetry.
