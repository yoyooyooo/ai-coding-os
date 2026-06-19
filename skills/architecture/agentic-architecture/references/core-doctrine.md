# Core Doctrine

## Primary Thesis

Agentic architecture is hexagonal architecture strengthened for systems where
non-deterministic and externally operated components can influence behavior.

```text
Authority defines truth.
Use cases govern change.
Capability ports isolate external powers.
Composition profiles select implementations.
Evidence bounds claims.
Forward migration preserves durable facts without preserving every old API.
```

A hexagon is not a folder diagram. The meaningful boundaries are:

1. **Authority boundary** — who may define an accepted fact.
2. **Use-case boundary** — which operation may change that fact and under which
   policy, idempotency, and transaction.
3. **Capability boundary** — which replaceable external power the core needs.
4. **Deployment boundary** — which profile selects adapters and resource
   lifetimes.

## System Model

```text
External actor / UI / agent / transport
  -> input adapter
  -> typed command or candidate
  -> application use case
  -> authority-cell invariant and policy
  -> typed change set
  -> atomic commit + event/outbox
  -> projection/query/realtime carrier

Application use case
  -> capability port
  -> output adapter
  -> external observation/candidate/handle
  -> application validation and materialization
```

Dependency direction points toward product authority. Runtime SDKs, database
clients, UI frameworks, queues, model providers, vector stores, and plugin APIs
must not become the language of the core.

## Business Modules Are Not Adapters

A business module such as Orders, Results, Issues, Accounts, or Governance owns
product semantics. It is an **authority cell**, not a replaceable adapter.

Create capability ports for genuine outer-boundary powers such as payment,
model inference, runtime execution, object storage, email delivery, external
search, or third-party ingress. Do not trait- or interface-wrap every business
service merely to make a diagram look hexagonal.

## Stable Kernel, Evolvable Product Semantics

When product positioning is still changing, stabilize the mechanism by which
facts are accepted rather than freezing every fact type. A common evolution
kernel often includes:

```text
ActorRef / FactRef / SourceRef
CommandContext
Authorization and visibility
Idempotency and request identity
Causal or expected-version boundary
Candidate and DecisionRecord
Typed ChangeSet
CommitReceipt
Event / outbox / audit / provenance
```

Objects, workflows, classifications, and projections may evolve behind this
kernel.

## Abstraction Restraint

Add a boundary when at least one pressure is real:

- more than one implementation must coexist or be replaceable;
- a process, machine, trust, or deployment boundary exists;
- a dependency carries security, reliability, or vendor risk;
- a test/replay/fake needs a stable seam;
- a module owns distinct invariants or change cadence;
- a transaction or consistency boundary must be explicit.

Do not add a boundary merely because a future system might need it. Start with
private modules in one process; promote to packages, ports, or services only
when evidence justifies the cost.

## Forbidden Defaults

```text
one public global state object as the whole domain
one application god object owning every module and adapter
whole-state snapshot persistence as the long-term storage contract
one universal outcome containing optional fields for every use case
transport or realtime state treated as accepted product truth
provider/runtime/plugin output persisted without application materialization
core libraries enumerating every vendor implementation
test harnesses creating facts through a privileged alternate path
permanent dual-write or compatibility bridges with no deletion gate
microservices used to simulate module boundaries that do not exist in code
```
