# Harness Artifact Model

Use a small shared language so Agents can discover and compose proof surfaces
without creating a parallel product architecture.

## Core concepts

```text
Harness Scenario
  bounded semantic proof story for one capability

Harness Fixture
  static deterministic input or seed

Harness Fake
  deterministic behavioral replacement

Harness Replay
  recorded normalized input sequence

Harness Surface
  runnable headless, interface-headless, render, browser, or external-runtime path

Harness Descriptor
  discoverability record: command, surface, observations, exclusions

Harness Result
  structured observations plus bounded supports and not_proven

Harness Coverage Matrix
  optional durable view mapping capabilities to available surfaces and gaps
```

A driver or probe is introduced only when it is a real reusable role. A simple
scenario may be one `<subject>.<case>.harness.ts` file.

## Trace spine

```text
product capability id
  -> interface capability id when applicable
  -> harness scenario/descriptor id
  -> command/route/component/test
  -> current observation/result or durable evidence reference
```

Suggested IDs remain optional:

```text
ic.<domain>.<action>
hs.<domain>.<case>
hr.<domain>.<case>
hc.<domain>.<case>
hf.<domain>.<case>
hp.<domain>.<case>
uh.<domain>.<case>
```

## Rules

- Harness artifacts support claims; they do not become product authority.
- UI Harness Surfaces are proof infrastructure, not final UI.
- Fixture data is not a real business fact.
- Test steps remain semantic; low-level selectors stay in executable code.
- Keep `observed`, `supports`, and `not_proven` distinguishable.
- `claim_ceiling` is descriptive metadata, not an Agent permission gate.
