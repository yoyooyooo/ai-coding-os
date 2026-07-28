---
name: product-harness-system
description: Make product behavior runnable, observable, diagnosable, and repeatable when tests pass without a clear claim, capabilities lack stable commands, failures cannot be reproduced, only final symptoms are visible, dependency realities are confused, or restart/reload/retry/reconnect behavior needs evidence.
---

# Product Harness System

A Harness makes a real product property runnable, observable, repeatable, and useful for diagnosis. It does not create a second product model, fact writer, or acceptance authority.

> **Observe Only What You Exercised.** The authority that defines a property gives an observation meaning, and one run supports only the path and dependencies it actually exercised.

## Semantic anchors

- **Observe Only What You Exercised.** Name the exact entry, environment, input, dependency reality, and path behind the observation.
- **Evidence Bounds Claims.** A passing command or browser flow supports a bounded property; it does not prove product acceptance, production safety, or unexercised behavior.
- **Find the First Wrong State.** Preserve the original symptom and follow the causal chain until the earliest owner deviates from its contract or invariant.
- **Feedback Horizon Sets the Safe Step Size.** Agent autonomy should not outrun the distance at which errors become visible and work can still stop or recover.
- **A Pass Is Not Product Acceptance.** Verification can support an accepted obligation, but cannot define the Quality Boundary or accept residual risk.

## Enter from the current pressure

| Current pressure | Continue into |
| --- | --- |
| it is unclear whether to use static, unit, headless, integration, browser, restart, or real-provider observation | [Choosing an observation surface](references/choosing-observation-surface.md) |
| fixture, fake, replay, local-real, and external-real are mixed | [Dependency realities](references/dependency-realities.md) |
| the project needs stable cross-project verification command slots | [Default project verification interface](references/default-project-verification-interface.md) |
| a capability lacks a stable command or a probe has dangerous side effects | [Command and probe design](references/command-and-probe-design.md) |
| render, navigation, focus, reload, accessibility, or browser integration must be observed | [Browser and UI observation](references/browser-and-ui-observation.md) |
| a frontend change needs the smallest honest test lane | [Frontend test selection](references/frontend-test-selection.md) |
| restart, retry, reconnect, duplicate delivery, timeout, or unknown outcome must be verified | [Recovery and continuity observation](references/restart-retry-reconnect-and-recovery.md) |
| only a final exception is visible and evidence must be preserved | [Investigation and the first wrong state](references/investigation-and-first-wrong-state.md) |
| a bug was fixed but the permanent defense layer is unclear | [Regression placement](references/regression-placement.md) |
| the Agent's safe step size is unclear | [Feedback horizon](references/feedback-horizon.md) |
| an observation may be over-interpreted | [Observation limits](references/observation-limits.md) |

These are not levels. Use the only surface that can honestly answer the current question.

## Harness owns

```text
how to run a property from a discoverable entry
which dependencies are fixture, fake, replay, local-real, or external-real
which state and boundaries can be observed directly
where the first wrong state appears
what happens after restart, reload, retry, or reconnect
what the observation cannot prove
where an escaped defect should be permanently caught
```

The answer may live in commands, tests, logs, browser flows, project-native documentation, or ordinary prose. Do not introduce descriptor/result schemas without a real machine consumer.

## Portable verification default

Every project should expose the command slots in [Default project verification interface](references/default-project-verification-interface.md) through `AGENTS.md`, the root README, or the native command system. The stable contract is the role of the command, not one package-manager spelling.

## Diagnose before editing

Preserve the original symptom, full error, input, environment, version, and exit status. Separate observation from hypothesis. Reduce the search space until the first wrong state is visible instead of repairing only the final exception or screenshot.

After the repair, replay the original failure and move the lesson to the lowest correct owner: type, schema, invariant, use case, adapter, state owner, test, monitor, tool guard, or durable project knowledge.

## Harness boundaries

A Harness must not become:

```text
a privileged fact writer
a second Query client, Runtime, socket, or state owner
a hidden production architecture
a parallel business implementation that exists only for tests
```

Exploration scripts and screenshots remain observations until repeated regression, discovery, and maintenance pressure earns a durable surface.

## Adjacent owners

- If the property itself is unclear, use `$product-definition`.
- If fact writer, transaction, capability, or production boundary is unclear, use `$evolvable-application-architecture`.
- If frontend state or realtime ownership is unclear, use `$frontend-architecture`.
- If Effect Scope, Runtime, or failure mechanism is unclear, use `$effect-best-practices`.
- If evidence placement or routes are unclear, use `$docs-governance`.

## Output principle

Prefer the smallest command, test, probe, or browser path that fails for the right reason and exposes the failing boundary. Report direct observations, the strongest honest conclusion, and unobserved areas. Improve project runnability and diagnosability before producing proof paperwork.
