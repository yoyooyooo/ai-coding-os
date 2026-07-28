# Agentic Systems Projection

Agent systems amplify the same authority, state, failure, and evolution problems as ordinary applications. Model-generated content does not escape architecture merely because it is probabilistic.

## Core roles

```text
Activity / objective       accepted user or system intent
Run                         one execution attempt with bounded lifetime
Revision                    proposed or accepted change to an artifact/plan/state
Artifact                    durable long output or generated object
Tool capability             application-owned contract to external power
Model output                candidate result, not automatic authority
Harness observation         evidence from a bounded execution
Accepted fact/decision      promoted only by the accountable authority or governed rule
```

Names may differ by project; keep the distinctions.

## Candidate and authority

Model output, retrieved text, web pages, tool responses, and peer-Agent messages are inputs. They must not silently become:

```text
project instructions
accepted product decisions
persistent memory truth
privileged tool authorization
final external facts
```

Promotion requires provenance, validation, authority, and the relevant product rule.

## Tool boundaries

A tool contract includes more than JSON shape:

```text
permission and workspace scope
preconditions
idempotency and operation identity
side effects and reversibility
postconditions
failure and unknown-outcome semantics
audit and evidence
resource lifetime
```

Prompt text cannot override the tool's independent permission checks.

## Loop and lifetime

The Agent loop may remain a black box while the host owns:

```text
cancellation
resource budget
timeout/deadline
artifact storage
context retrieval
revision and conflict handling
recovery or handoff
observability
```

Do not use a workflow engine merely because the system has many activities. Add explicit orchestration only when product semantics, external coordination, or recovery requires it.

## Shared state and multi-Agent work

Several Agents editing one plan or artifact create a shared-state problem. Use versioned candidates, conflict detection, explicit acceptance, and stable ownership rather than "everyone writes the latest value".

A blackboard-like fact space may be useful when capabilities join dynamically, but distinguish candidate facts from accepted facts and define dedupe, version, termination, and authority.

## Context and artifacts

Large outputs should become addressable Artifacts rather than being copied into every prompt. Retrieval should preserve provenance and version. Prompt caching and shared prefixes are optimizations, not authority models.

## Steering and interruption

User steering is a new intent or constraint entering an active Run. Define whether it updates the current Run, creates a Revision, cancels, forks, or queues. Do not let arrival timing implicitly decide semantics.

## Related knowledge

- Use [Fact authority and candidate boundaries](fact-authority-and-candidate-boundaries.md) for model output and memory.
- Use [Use cases, transactions, and idempotency](use-cases-transactions-and-idempotency.md) for tool effects.
- Use [Consistency, events, and shared state](consistency-events-and-shared-state.md) for multi-Agent state.
- Use [Composition roots and lifetimes](composition-roots-and-lifetimes.md) for Run ownership.
- Use `$product-harness-system` for evaluation and runtime observation.
- Use `$product-definition` for user outcome, permission, and quality boundaries.
- Return to the [EAA map](../SKILL.md).
