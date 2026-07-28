# Composition Roots and Lifetimes

> **Composition Chooses; It Does Not Decide.** A host root selects implementations and owns lifetimes without becoming product policy or fact-transition logic.

A composition root is the place where a runnable host chooses live implementations, constructs resources, and owns shutdown. It is not a product workflow or a global service locator.

## Host responsibilities

A host root may construct:

```text
configuration and secrets references
database pools and transaction capabilities
HTTP/provider clients
message consumers and producers
Effect Runtime or Layer graph
query cache, socket, worker, or browser resources
background jobs and supervisors
transport/router handlers
```

It selects implementation; ordinary product modules consume contracts.

## One root per lifetime domain

Typical hosts include:

```text
API process
worker or scheduler
CLI command
browser tab/application
SSR request or server process
web/service worker
desktop shell
migration or one-shot job
```

Each host must define acquisition, operation, interruption, and shutdown semantics for its resources.

## Import direction

```text
business modules / use cases
  may depend on Ports and pure model
  must not import host composition or live providers

composition root
  may import Ports, use cases, and live implementations
  remains a leaf selected by the executable entry
```

## Configuration

Configuration enters at the host boundary, is decoded once, and becomes typed capability construction input. Deep business code should not read process environment or global config directly.

## Background work

Every long-lived loop, subscription, poller, Fiber, worker, or listener needs:

```text
owner
start condition
resource budget
failure policy
cancellation and shutdown path
observability
```

Detached work without a parent lifetime is a leak even if it eventually finishes in tests.

## Multiple hosts

Sharing a package between API and worker does not grant both hosts fact authority. State which host can execute which governed use case and how concurrency is controlled.

## Testing

A test or Harness host may use different implementations, but it should preserve the same semantic Ports and make dependency reality explicit.

## Related knowledge

- Use [Default repository profile](default-repository-profile.md) for host directory defaults.
- Use [Capability boundaries and adapters](capability-boundaries-and-adapters.md) for implementation selection.
- Use [Fact authority and candidate boundaries](fact-authority-and-candidate-boundaries.md) for writer ownership.
- Use `$effect-best-practices` for Scope, Layer, and Runtime details.
- Use `$frontend-architecture` for browser/SSR host composition.
- Return to the [EAA map](../SKILL.md).
