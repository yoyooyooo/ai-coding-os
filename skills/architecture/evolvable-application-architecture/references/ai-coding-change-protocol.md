# AI Coding Change Protocol

This reference concerns AI as a software-development Agent. It is distinct from
product-internal LLM or agent architecture.

## Repository materialization analogy

```text
AI-generated patch
  = repository candidate

project authority + compiler + architecture checks + behavior harnesses
  = evaluation surfaces

accepted merge/release
  = repository materialization
```

The analogy is useful when it sharpens repository acceptance without creating
a parallel approval system. Planning, implementation, checks, interpretation,
and continuation may remain one coherent loop.

## Durable constraints

These constraints protect repository semantics:

```text
project authority overrides generic defaults
new code must not silently create a second fact writer
public contracts and stored facts require deliberate migration
architecture claims must match exercised surfaces
fake/replay/real paths remain distinguishable
bridges need fencing and deletion conditions
```

## Execution-policy boundary

Keep cost, credential, production-data, irreversible-effect, security, and
privacy limits in the runtime or project policy that owns those risks. Planning
roles, retry limits, diff budgets, staged reasoning artifacts, and execution
methods remain selectable rather than universal architecture doctrine.

## Agent-friendly architecture

Prefer systems where an Agent can discover locally:

```text
who owns the fact
which public command/query surface applies
which files form the capability cluster
where live implementations are selected
which harnesses exist
what evidence a command actually provides
what remains unproven
```

Machine checks should protect durable semantic edges. Heuristics should remain
review signals when a universal hard rule would block sound judgment.
