# Core Doctrine

## Primary Thesis

Evolvable application architecture is hexagonal architecture strengthened by
explicit fact authority, transaction ownership, lifecycle, migration, and
proof.

```text
Authority defines accepted truth.
Use cases govern change.
Capability ports isolate external powers.
Composition profiles select implementations.
Evidence bounds claims.
Forward migration preserves durable facts without preserving every old API.
```

A hexagon is not a folder diagram. The meaningful boundaries are:

1. **Authority boundary** — who may finally accept a fact, in which consistency
   domain and authority epoch.
2. **Use-case boundary** — which operation may change that fact and under which
   authorization, idempotency, version, and transaction.
3. **Capability boundary** — which external power the application needs without
   surrendering product semantics.
4. **Deployment boundary** — which profile selects adapters, resources, and
   lifetimes.
5. **Evidence boundary** — which behavior has actually been proven.

## System Model

```text
External actor / UI / protocol / scheduler
  -> input adapter
  -> typed Command, Observation, or Candidate
  -> application use case
  -> authority-cell invariant and policy
  -> typed ChangeSet / Decision
  -> atomic commit + event/audit/outbox
  -> projection/query/realtime carrier

Application use case
  -> capability port
  -> output adapter
  -> external observation/candidate/receipt/opaque handle
  -> application validation, reconciliation, and materialization
```

Dependency direction points toward product authority. Database clients, UI
frameworks, queues, payment SDKs, model providers, device protocols, workflow
engines, and plugin APIs must not become the language of the core.

## Authority-First Hexagonal Modular Monolith

Prefer one system-level hexagonal shell containing multiple private authority
cells. An authority cell owns business facts and invariants; it is not an
adapter and does not need an interface merely because another internal module
calls it.

Internal collaboration should use typed commands, queries, stable references,
or explicit application orchestration. Promote an internal boundary to a port
or process only when replacement, trust, lifecycle, deployment, scaling,
ownership, or proof pressure is real.

## Command and Candidate Are Different

Do not force every change through a candidate pipeline.

```text
Command
  = an authoritative request to attempt a governed transition

Candidate
  = a non-authoritative proposal from observation, import, computation,
    external execution, inference, plugin, or remote participant
```

A command can be rejected, conflict, no-op, or commit. A candidate requires a
separate materialization decision before it can become accepted truth.

## Stable Kernel, Evolvable Product Semantics

When product semantics are moving, stabilize how facts are accepted rather than
freezing every fact type. A useful kernel may include:

```text
ActorRef / FactRef / SourceRef
CommandContext
Authorization and visibility
Idempotency and request identity
ConsistencyDomain / AuthorityEpoch
Causal or expected-version boundary
Observation / Candidate / DecisionRecord
Typed ChangeSet
CommitReceipt
Event / outbox / audit / provenance
```

Objects, workflows, classifications, policies, and projections may evolve
behind this kernel.

## Abstraction Restraint

Add a boundary when at least one pressure is real:

- more than one implementation must coexist or be replaceable;
- a process, machine, trust, or deployment boundary exists;
- a dependency carries security, reliability, data, or vendor risk;
- a test, replay, simulator, or fake needs a stable seam;
- a module owns distinct invariants or change cadence;
- a transaction, consistency, or lifecycle boundary must be explicit.

Do not add a boundary merely because a future system might need it. Start with
private modules in one process; promote only when evidence justifies the cost.
Use [Pressure Profiles](pressure-profiles.md) to scale the design.

## Forbidden Defaults

```text
one public global state object as the whole domain
one application god object owning every module, adapter, and invariant
whole-state snapshot persistence as the long-term storage contract
one universal result containing optional fields for every use case
transport, cache, scheduler, or realtime state treated as product truth
external/provider/plugin output persisted without application materialization
core libraries enumerating every vendor implementation
one generic JSON command/event bus for all internal authority collaboration
test harnesses creating facts through a privileged alternate path
permanent dual-write or compatibility bridges with no deletion gate
microservices used to simulate module boundaries that do not exist in code
maximum distributed machinery applied to a low-pressure local application
```
