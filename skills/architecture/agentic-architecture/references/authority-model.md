# Authority Model

Authority is the right to define an accepted fact. Observation, transport,
rendering, caching, ranking, and execution do not imply authority.

## Authority Map

For every important fact, record:

```text
fact:
authority_cell:
accepted_commands:
queries_and_projections:
candidate_sources:
materialization_path:
transaction_boundary:
forbidden_writers:
evidence:
not_claimed:
```

If an important durable fact has multiple silent writers or no named owner, the
architecture is not ready for broad automation.

## Authority Cell

An authority cell is the smallest product module that can defend its own
invariants. It owns:

```text
commands / use cases
private state or aggregates
invariants and transition policy
typed changes or domain events
queries or projection inputs
module-specific error semantics
```

An authority cell does not require a process, service, package, crate, or
interface. Begin as a private module when that is sufficient. The boundary is
real when callers cannot mutate its internal state directly.

Cross-cell interaction should use stable references, commands, queries, or
explicit orchestration. Avoid giving one cell another cell's mutable maps,
ORM entities, or repository internals.

## Global State Smell

A global state container is acceptable as a prototype implementation detail,
but it becomes an evolvability bottleneck when:

- its maps or collections are public;
- tests and adapters mutate it directly;
- every use case receives full mutable access;
- projections scan unrelated modules' internals;
- persistence serializes the entire state graph;
- adding one fact type changes every storage adapter;
- module invariants exist only by developer convention.

The first remediation is usually privacy and module APIs, not microservices.
Partition state into authority-cell-owned state and close direct mutation
escape hatches before changing deployment topology.

## Candidate-to-Fact Boundary

```text
source observation
  -> normalized candidate
  -> authorization / policy / freshness / dedupe decision
  -> typed materialization plan
  -> atomic commit
  -> projection and evidence
```

Candidates may come from humans, agents, models, plugins, transports, importers,
search engines, or runtimes. Candidate origin affects validation and trust; it
does not change who owns the accepted fact.

## Common Authority Separations

### Runtime

Runtime owns opaque execution handles and protocol observations. Application
owns product lifecycle, completion, accepted outputs, provenance, and recovery
state.

### Model Provider

Provider owns response transport and usage diagnostics. Application owns whether
structured output becomes a routing decision, summary, classification, or fact.

### Memory

Separate source fact, memory candidate, acceptance decision, accepted memory,
retrieval evidence, and run-context use. A vector or graph engine is normally a
retrieval adapter, not memory authority.

### Transport

Transport owns delivery, signing, ack, reconnect, cursor, retry, and frame
diagnostics. It does not own business completion.

### Frontend

Frontend owns local interaction state and optimistic proposals. Server or local
application authority owns accepted product state. Reconciliation uses
projections rather than allowing UI stores to become an alternate domain.

### Harness

A harness owns proof orchestration and evidence files. It must not become a
privileged production-bypass materialization path.

## Stop Lines

Require a higher-authority decision before changing:

- fact ownership or permission authority;
- security, privacy, retention, or redaction posture;
- irreversible or destructive data behavior;
- public protocol/API compatibility promises;
- the claim ceiling or definition of completion.
