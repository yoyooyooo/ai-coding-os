# AI Coding OS Skill Coordination

This is the portable knowledge kernel for cross-Skill coordination. It defines
ownership and claim boundaries, not an Agent workflow.

## Minimal Knowledge Kernel

### Project Authority First

Applicable, current project Authority for the question and scope overrides an
unadopted Preset, Router suggestion, or generic Skill default. File existence,
recency, detail, and implementation existence do not establish Authority by
themselves.

Host instructions and `AGENTS.md` constrain Agent conduct, access, tools, and
repository-local working rules. They do not silently redefine product meaning,
policy, public contracts, or observed runtime facts.

### Question-scoped Ownership

Select the semantic owner by the question, not by file count, directory depth,
or invocation order.

| Question | Primary semantic owner | Evidence or constraint that remains distinct |
| --- | --- | --- |
| What should the product do? | accepted product/business decision or baselined requirement | binding policy, SSoT constraints, delivery evidence |
| What does a shared term, object, state, or invariant mean? | project SSoT or accepted semantic decision | product change input, contracts, implementation evidence |
| Which rule currently binds work? | adopted Standard or accountable policy owner | enforcement and runtime evidence |
| Why was a choice accepted? | product decision record or technical ADR | later implementation and outcome evidence |
| What does an interface accept? | adopted protocol/schema contract | contract tests and implementation |
| What implementation exists? | source, schema, migration, lockfile, generated artifact | reachability and runtime behavior remain unproven |
| What behavior was observed? | executed test, Harness, runtime, release, or operational evidence | accepted intent and whole-capability completion remain separate |
| Where does documentation belong? | `$docs-governance` plus the content's semantic owner | placement does not transfer semantic ownership |

There is no universal file ranking across these questions.

### One Scoped Meaning, One Current Home

For one claim, representation, and effective scope, keep one canonical
definition Home. Version, module, environment, market, and other real scope
boundaries may justify distinct variants. Product meaning, wire representation,
persistence representation, source implementation, and observed evidence may
coexist when their different ownership is explicit and they reference rather
than redefine one another.

### Binding Constraint Is Not Semantic Ownership

Security, privacy, legal, policy, platform, and adopted Standard constraints may
limit or veto a decision without taking over its product, architecture,
interface, or documentation meaning. Name the primary semantic owner, each
applicable binding constraint, and the Evidence that supports the current
claim.

### Evidence Bounds Claims

```text
source exists                != runtime path is reachable
local Harness passes         != production behavior is proven
accepted product target      != implementation is complete
document accepted            != delivery is verified
partial Evidence             != whole capability is done
```

Source may establish implementation structure, static properties, and explicit
logic. Runtime, reachability, deployment, and environment claims require
executed or observed Evidence appropriate to that claim. Neither source nor
Evidence decides accepted product intent by itself.

### Route Is an Edge; Change Creates an Impact Obligation

A Route discovers adjacent Authority, Evidence, source, or a neighboring owner;
it does not prescribe traversal or implementation order. When an accepted
decision changes another Current Home's meaning, identify the affected Homes
and either update them, record temporary drift, lower the affected claim, or
state why the impact does not apply. The active Agent chooses a safe order.

## Collaboration Judgment

- Use the smallest owner set that covers the decision surfaces that actually
  change.
- Add a supporting Skill for an orthogonal decision, not as an extra reviewer by
  default.
- Infer ordinary reversible details from current Authority and local patterns.
- Prefer low-commitment choices that do not widen public, data, permission, or
  trust boundaries.
- Isolate a genuinely undecidable local claim and continue unaffected work.
- Ask for an external decision only when materially different answers would
  change Product, SSoT, binding policy, a public contract, durable data, or a
  trust boundary and current Authority cannot answer.
- Keep planning strategy, model selection, retries, work state, and completion
  with the active execution context.

When claims appear to conflict, first test whether they answer the same
question and share object, representation, scope, version, and environment.
Natural-language dispositions such as coexist by scope, supersede, classify as
drift, require Evidence, require a decision, or retain as source are outcomes,
not a global status machine.

## Handoff Guidance

Ordinary cross-Skill continuation is natural language. State only:

```text
what is settled
what remains open
the next semantic owner
the current claim boundary
```

Use a structured durable handoff only when an external system, machine consumer,
long-lived review, or repeated transfer earns it. Cross-Skill references use
`$skill-name`; grouped repository paths and a static Suite roster are not part
of the portable contract.
