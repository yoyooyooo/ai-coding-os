# Scenario Mappings

These mappings show how the generic doctrine changes vocabulary without
changing the architecture.

## Payments and Orders

```text
customer checkout                 -> Command
payment-gateway callback          -> Observation
normalized provider status        -> Candidate
payment/order authority cell      -> final local Decision
charge/refund call                 -> external effect through capability port
provider transaction ID           -> source evidence, not local settlement alone
```

Use P4 for money movement. Preserve unknown outcome, reconciliation, ledger
boundaries, and irreversible-effect limits.

## Approval and Review

```text
submit request        -> Command
reviewer recommendation-> Candidate or governed Command by policy
ReviewCase            -> authority cell
approval execution    -> typed downstream command/obligation
notification          -> post-commit capability
```

Separate proposer, reviewer, executor, and final acceptance authority. A message
or email saying “approved” is not the approval fact.

## Logistics and External Records

```text
carrier scan/webhook  -> external Observation
shipment update       -> Candidate with source version/provenance
local shipment cell   -> local business interpretation
carrier               -> authority for its source claim
application           -> authority for local SLA/status/workflow
```

Handle corrections, supersession, delayed events, and source disagreement.

## IoT and Device Control

```text
sensor telemetry      -> Observation
canonical device state-> governed materialization
control request       -> Command + durable effect intent
device acknowledgement-> Receipt, not proof of physical outcome
```

Use device identity, firmware/capability version, command idempotency, timeout,
and reconciliation. Safety-critical control is P4.

## Data Pipelines and Publishing

```text
raw input/checkpoint  -> source fact or Observation
computed dataset      -> Candidate
validation/promotion  -> Decision
published version     -> accepted fact
object store/compute  -> capability adapters
```

Separate successful computation from accepted publication. Make checkpoints,
schema versions, and replay ceilings explicit.

## Realtime Collaboration

```text
local draft/selection -> frontend authority
submitted operation   -> Command or CRDT operation
merge/admission rule  -> collaborative-state authority
business status       -> separate non-commutative authority cell
realtime frame        -> projection carrier
```

CRDT convergence does not grant permission or settle workflow facts. See
[Consistency and Authority Topologies](consistency-and-authority-topologies.md).

## Plugin Platforms

Define finite extension classes. A renderer, importer, payment connector,
workflow action, or inference provider implements a named capability port and
returns bounded outputs. Plugin packaging never grants product authority.

## Small Transactional CRUD

Start at P0/P1:

```text
private module
explicit use cases
transaction for durable transitions
simple composition
```

Do not add event sourcing, a plugin framework, microservices, or a generic bus
without real pressure. Preserve an evolution path by keeping state private and
transactions explicit.
