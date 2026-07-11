# Authority Model

Authority is the right to finally materialize an accepted fact within a declared
consistency domain and authority epoch. Observation, transport, execution,
replication, ranking, rendering, and caching do not imply that right.

## Authority Map

For every important fact, record:

```text
fact:
consistency_domain:
authority_epoch_or_membership:
final_materialization_authority:
authority_topology:
accepted_commands:
queries_and_projections:
observation_and_candidate_sources:
materialization_path:
transaction_or_merge_boundary:
forbidden_writers:
evidence:
not_claimed:
```

If an important durable fact has multiple silent final writers, no named merge
rule, or no epoch/membership rule, the architecture is not ready for broad
automation.

## Authority Cell

An authority cell is the smallest product module that can defend its own
invariants. It owns:

```text
commands / use cases
private state or aggregates
invariants and transition policy
typed changes, decisions, or domain events
queries or projection inputs
module-specific error semantics
```

An authority cell does not require a process, service, package, crate, trait, or
interface. Begin as a private module when that is sufficient. The boundary is
real when callers cannot mutate its internal state directly.

Cross-cell interaction should use stable references, typed commands, queries,
or explicit application orchestration. Avoid giving one cell another cell's
mutable collections, ORM entities, repositories, or transaction internals.

## Authority Is Logical, Not Necessarily Singular Infrastructure

“One fact, one authority” does not mean one machine or one proposer. Valid
forms include:

- one leader during an authority epoch;
- many proposers with one compare-and-set acceptance rule;
- an event-sourced aggregate whose reducer defines accepted history;
- a CRDT whose declared merge algebra and membership define convergence;
- an external source authoritative for its source record, plus a local cell
  authoritative for imported product meaning;
- a saga where each participant owns local facts and the coordinator owns only
  the process state.

Read [Consistency and Authority Topologies](consistency-and-authority-topologies.md)
before diagnosing replicated or federated systems as “multiple writers.”

## Global State Smell

A global state container can be a prototype implementation detail, but becomes
an evolvability bottleneck when:

- its maps or collections are public;
- tests and adapters mutate it directly;
- every use case receives full mutable access;
- projections scan unrelated modules' internals;
- persistence serializes the entire state graph;
- adding one fact type changes every storage adapter;
- module invariants exist only by developer convention.

The first remediation is usually privacy and module APIs, not microservices.
Partition state into authority-cell-owned state and close mutation escape
hatches before changing deployment topology.

## Candidate-to-Fact Boundary

```text
source observation or computation
  -> normalized Candidate + provenance
  -> authorization / policy / freshness / dedupe decision
  -> typed materialization plan
  -> authoritative commit or declared merge
  -> projection and evidence
```

Candidates may come from humans, importers, algorithms, agents, models,
plugins, transports, sensors, search engines, gateways, or remote systems.
Origin affects validation and trust; it does not silently transfer authority.

## Common Authority Separations

### External System or Gateway

The external system may own its source-side record. The application owns how
that observation changes local orders, entitlements, workflow, or accounting.
For example, a payment webhook is evidence about a provider transaction, not by
itself the application's settled-order fact.

### Executor or Runtime

An executor owns opaque handles and protocol observations. The application owns
product lifecycle, accepted output, provenance, recovery, and completion.

### Scheduler or Workflow Engine

A scheduler owns wake-up delivery and lease diagnostics. It does not own the
business deadline disposition or workflow transition unless the product has
explicitly delegated that fact.

### Search, Cache, Index, and Retrieval

These systems own their internal index state and diagnostics. The source
application owns canonical facts. A retrieved or ranked item is a candidate for
use, not proof of truth.

### Transport

Transport owns delivery, signing, acknowledgement, reconnect, cursor, retry,
and frame diagnostics. It does not own business completion.

### Frontend

Frontend owns local interaction state, drafts, and optimistic proposals. The
server or local application authority owns accepted product state.
Reconciliation consumes committed projections rather than letting UI stores
become an alternate domain.

### Harness

A harness owns proof orchestration and evidence artifacts. It must not become a
privileged production-bypass materialization path.

## Stop Lines

Require higher-authority approval before changing:

- fact ownership or permission authority;
- security, privacy, retention, disclosure, or redaction posture;
- irreversible or destructive data behavior;
- public protocol/API compatibility promises;
- regulatory or financial semantics;
- the claim ceiling or definition of completion.
