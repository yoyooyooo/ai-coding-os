# Agent-Legible Change Surface

> **The Project Should Explain Itself.** A fresh capable Agent should recover the smallest complete change path from product meaning, source, commands, tests, logs, and local knowledge.

A project is Agent-legible when a fresh capable Agent can start from one real capability and recover the smallest complete path needed to change it safely.

## The surface

For a material capability, make these relationships discoverable:

```text
accepted product meaning or invariant
formal command/query/use-case entry
final fact writer and consistency scope
external capability boundary
live composition and resource owner
smallest run or reproduction command
observation and claim limits
migration fence or old-path deletion condition when relevant
```

This is a project property, not a required artifact. It may be expressed through names, types, source layout, tests, local READMEs, `AGENTS.md`, and durable project knowledge.

## Why it matters

A project can be modular on a diagram yet remain hard to change because readers cannot find the real writer, composition root, failure boundary, or observation route. AI reduces mechanical editing cost but does not reduce the cost of misunderstanding distributed authority.

## Entry from source

A useful source path often looks like:

```text
transport or UI intent
  -> formal use case
  -> domain policy and fact transition
  -> Port / transaction boundary
  -> live adapter selected by host composition
  -> verification command or Harness
```

Not every capability needs every role as a separate file. The relation must be recoverable.

## Entry from failure

```text
symptom
  -> stable reproduction
  -> first wrong state
  -> owning contract/resource/fact
  -> accepted meaning
  -> lowest permanent regression layer
```

## Entry from product knowledge

```text
accepted capability
  -> interface obligation
  -> use case and state owner
  -> source module and public surface
  -> observation route
```

## Legibility signals

Healthy signals include:

- semantic filenames and feature/module names;
- explicit public surfaces instead of deep imports;
- one visible composition root per host;
- stable commands with readable output and exit status;
- source-adjacent routes to non-obvious decisions;
- tests that name the invariant or contract they protect;
- migration code with explicit old/new authority and deletion conditions.

## Anti-signals

```text
business changes begin in framework handlers
writers are discovered only by full-text search for table names
a global context or service locator hides dependencies
live providers are selected inside ordinary modules
runtime resources are created in callbacks or components
only final symptoms are logged
an architecture document has no route to current source
```

## Related knowledge

- Use [Source topology and semantic naming](source-topology-and-semantic-naming.md) to make roles visible.
- Use [Fact authority and candidate boundaries](fact-authority-and-candidate-boundaries.md) for accepted writes.
- Use [Composition roots and lifetimes](composition-roots-and-lifetimes.md) for live ownership.
- Use [Causal diagnosis and the first wrong state](causal-diagnosis-and-first-wrong-state.md) for failures.
- Use `$docs-governance` for project routes and Current Homes.
- Use `$product-harness-system` for runnable observation.
- Return to the [EAA map](../SKILL.md).
