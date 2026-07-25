# Harness Artifact Model

Use a small shared language so Agents can discover and compose proof without
creating a parallel product architecture.

## Core concepts

```text
Harness Scenario
  bounded semantic proof story for one capability

Harness Fixture / Fake / Replay
  explicit deterministic or recorded dependency material

Proof Surface
  surface_kind + dependency_reality + optional environment_class + proof_focus

Harness Descriptor
  discoverability record: command, Proof Surface, observations, exclusions

Harness Result
  direct observations plus bounded supports, not_proven, and claim_ceiling

Harness Coverage Matrix
  optional durable view mapping capabilities to available surfaces and gaps
```

A driver or probe is introduced only when it is a real reusable role. A simple
scenario may be one `<subject>.<case>.harness.ts` file.

## Trace spine

```text
product capability or AC/UAT ref
  -> interface capability id when applicable
  -> harness scenario/descriptor id
  -> command/route/component/test
  -> Harness Result or durable evidence reference
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

- Harness artifacts support claims; they do not become product decision authority.
- UI Harness surfaces are proof infrastructure, not final UI.
- Fixture data is not a real business fact.
- Test steps remain semantic; low-level selectors stay in executable code.
- Keep `observed`, `supports`, `not_proven`, and `claim_ceiling` distinguishable.
- `claim_ceiling` is descriptive metadata, not an Agent permission gate.
