# Agentic Systems Profile

Load this profile for agents, LLMs, model providers, autonomous runtimes, tools,
memory/retrieval systems, plugins, or agent-to-agent protocols. It specializes
the generic doctrine; it does not replace it.

## Pressure

Most agentic slices are at least P2 because output is external or
nondeterministic. Add P3 for durable queues, remote runtimes, replay, or partial
failure. Use P4 when agents can affect money, permissions, private data,
external systems, or other participants.

## Authority Separations

### Model or Agent Output

A model response, tool choice, classification, plan, or structured object is a
Candidate. The application decides whether it becomes routing, memory, message,
result, artifact, action, or no fact at all.

### Runtime

Runtime owns:

```text
opaque execution handles
protocol events and diagnostics
provider session mechanics
cancellation/interrupt observations
resource usage samples
```

Application authority owns:

```text
invocation lifecycle
accepted context and visibility
canonical output
terminal settlement
product-facing completion
recovery and provenance
```

A runtime acknowledgement does not prove the product transition committed.

### Memory and Retrieval

Separate:

```text
source fact
memory Candidate
acceptance Decision
accepted memory or representation
retrieval evidence
run-context use
```

A vector store, graph engine, or provider session is normally a retrieval or
continuity adapter, not product-memory authority. Hidden provider memory needs a
capability/evidence ceiling and must not silently exceed visibility rules.

### Tools and External Effects

A tool proposal is a Candidate or external-effect intent. The application
freezes actor, capability, arguments/schema, policy version, idempotency, and
visibility before dispatch. Record attempt/receipt/unknown outcome and
reconcile without repeating irreversible effects blindly.

### Agent-to-Agent and Plugins

Remote agents and plugins are external participants/adapters. They may submit
only the candidate/action classes allowed by a versioned contract. They cannot
choose their own authority, grant, actor identity, target fact, or product
completion semantics.

## Common Capability Ports

```text
StructuredInferencePort
AgentRuntimeExecutionPort
RuntimeControlPort
MemoryRetrievalPort
ToolExecutionPort
ExternalParticipantPort
ModelUsageDiagnosticsPort
```

Keep these separate when semantics, trust, lifecycle, or evidence differ, even
if one vendor implements several.

## Governed Actions

When an action depends on a turn, phase, reviewer role, vote state, secret view,
or shared simulation state, do not publish it first as an ordinary product fact.
Use:

```text
scoped activation/context
-> runtime Candidate ingress
-> governed action Candidate
-> owning reducer Decision
-> typed materialization into Message/Result/Effect/etc.
```

The domain owner/reducer is an authority cell. The runtime and model remain
capability adapters.

## Composition

Construct concrete model, runtime, memory, and tool adapters only in composition
profiles. Core modules depend on normalized application-owned contracts, not
vendor SDK types or provider enums.

## Evidence

Before claiming replaceability or safe autonomy, test:

```text
fake/replay and one real adapter
schema and capability negotiation
late/duplicate/partial output
cancel/terminal/effect races
restart with pending work
visibility and secret leakage
unknown outcome and reconciliation
cross-runtime differential behavior where claimed
```

Do not retain private chain-of-thought or secrets merely to improve replay.
Store bounded provenance and accepted decision evidence.
