# Core Doctrine

Agentic architecture starts from a stricter version of ports and adapters:
external actors can influence the system, but accepted product facts remain
owned by the core.

## Primary Thesis

```text
Authority first
Capability ports before integrations
Adapters return candidates
Application services accept facts
Composition roots wire profiles
Evidence gates bound claims
Agents operate freely inside typed constraints
```

The goal is not to prevent agents from being useful. The goal is to give them a
large search and action space without letting provider output, runtime state,
transport messages, plugin hooks, caches, or logs become hidden authority.

## Principles

### Authority Before Integration

Before adding an integration, identify the fact it can affect and the current
authority for that fact.

If no authority exists, create or select one before accepting external output.
If an authority already exists, the integration must feed that authority rather
than bypass it.

### Capability Ports Over Plugin-first

A capability port is a narrow typed contract defined by the core or application
layer. A plugin, provider SDK, runtime, transport, memory engine, or tool is an
adapter behind that port.

Do not build a broad plugin platform when the real pressure point is one
capability. Promote capabilities into ports only when repeated use, risk,
replaceability, or testing pressure justifies the boundary.

### Adapters Return Candidates

External adapters return candidate facts, diagnostics, opaque handles, manifest
snapshots, or bounded projection inputs. Accepted business facts require an
application-service path with validation, permission, idempotency, persistence,
audit, and projection.

### Commands vs Projections

Commands represent intent. Projections represent accepted or observed state.
Realtime transports, notifications, logs, and UI caches are projection carriers,
not a second command model.

### One Core Across Profiles

Local, cloud, desktop, fake, relay, server, worker, CLI, and real-runtime
profiles should share one domain/application core. Profile variation belongs in
adapter selection, policy, configuration, deployment wiring, and composition
roots.

### Composition Root Owns Wiring

The composition root assembles dependencies, runtime resources, config,
observability, and adapter implementations. It must not become a business-rule
layer.

### Evidence Gates Are Architecture

If a boundary matters, there should be a way to prove it did not collapse.
Tests, smoke commands, fixture/replay, browser-visible proof, diagnostics,
positive tokens, `not_claimed`, and `not_proven` define what the system may
honestly claim.

### Agent Freedom Under Typed Constraints

Agents may plan, search, call tools, combine capabilities, write proposals, and
request actions. They may not create accepted business facts except through
bounded commands or policy-approved materialization paths.

## Relationship To Hexagonal Architecture

This doctrine is compatible with hexagonal architecture, but it adds AI-era
constraints:

- authority: which object owns the fact;
- evidence: what proves the claim;
- agent boundary: why model/runtime output is not automatically product truth;
- replaceability: why a provider or plugin cannot define core semantics;
- composition: how multiple deployment profiles share one core.

Use hexagonal language when it helps, but do not reduce this skill to directory
shape. The durable object is the authority and dependency direction, not the
diagram.
