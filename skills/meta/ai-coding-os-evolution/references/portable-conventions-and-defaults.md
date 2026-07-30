# Portable Conventions and Defaults

> **A Strong Agent Does Not Make Defaults Obsolete.** Stable defaults remain valuable when they reduce cross-project invention, search, review, and tooling ambiguity at low cost.

A strong Agent can often invent a valid structure. Cross-project work still benefits from deterministic defaults that reduce dialect drift and repeated discovery. These conventions do not own product, documentation, architecture, frontend, Effect, or Harness details; those defaults remain with their semantic Owners.

## Precedence

```text
1. accepted project authority
2. coherent adopted project convention
3. AI Coding OS portable default
4. free invention
```

A local convention is coherent when its meaning, scope, entry points, and exceptions are discoverable and it preserves the relevant invariant. Preserve such a convention unless its ambiguity or cost is material.

## Convention labels

### Invariant

A semantic, safety, or ownership property that must remain true regardless of directory or tool choice.

Examples:

```text
one accepted fact has one final materialization authority within a consistency scope
local interaction state does not silently become server truth
an observation supports only the path and dependencies it actually exercised
```

### Default

The network choice when the project has no coherent adopted alternative. A default resolves an underdetermined decision consistently; it is not a universal law.

Examples:

```text
use docs/README.md as the documentation router when durable docs exist
use kebab-case for ordinary paths
use semantic dot filenames for TypeScript responsibilities
```

### Conditional

A shape or mechanism introduced only when a stated pressure exists.

Examples:

```text
create a workspace package after compile, reuse, ownership, trust, or public API pressure
create docs/runbook/ when operational diagnosis and recovery are durable knowledge
introduce an Actor when a long-lived identity genuinely owns private state and a mailbox
```

### Project override

A coherent local convention that replaces the portable default while preserving the invariant. Record the mapping once in a discoverable project entry rather than explaining it repeatedly.

## A convention is not obsolete because it is inferable

Retain a portable default when it:

```text
resolves a recurring underdetermined choice
reduces cross-project search and review cost
improves tooling and Agent predictability
remains short and owner-local
preserves a real invariant
is easy to override coherently
does not require unused files or mechanisms
```

Documentation first-level homes, TypeScript semantic suffixes, frontend state-role suffixes, and project verification command slots are examples.

## A convention is not an invariant

A project may use a different coherent directory or filename grammar while preserving authority and dependency direction. The default should not force migration for visual conformity.

## Semantic roles do not require artifact symmetry

A semantic distinction can change judgment without earning a separate file, document, package, Service, Schema, or Registry.

```text
first preserve the role and boundary
then choose the smallest physical shape that keeps it legible
promote the shape only after independent pressure appears
```

A role vocabulary is not a manifest. Command, Outcome, Receipt, Policy, transaction, idempotency, Port, Service, fake, and public surface may be meaningful while remaining co-located or absent from the first physical slice.

## Admission test

```text
does this change semantic judgment?
does it provide a deterministic default where several valid choices otherwise drift?
does it reduce repeated cross-project reinvention?
is it owned by the correct specialist?
can it be expressed without a registry, profile engine, or generator?
what real pressure justifies a conditional variant?
```

## Default projection index

| Concern | Portable default | Owning Skill |
| --- | --- | --- |
| Repository Agent entry | thin root `AGENTS.md` when durable local instructions exist | `$docs-governance` |
| Documentation router and first-level Homes | `docs/README.md`; reserved `product/`, `ssot/`, `standards/`, `architecture/`; conditional Homes by pressure | `$docs-governance` |
| Project Standard filenames | source topology, architecture profile, naming vocabulary, verification policy | `$docs-governance` with the semantic Owner |
| Product knowledge | `docs/product/`, `docs/ssot/product-language.md`, selective capability documents | `$product-definition` |
| Application repository | single-host `src/` or multi-host `apps/`; `modules/`, conditional `workflows/` and `packages/` | `$evolvable-application-architecture` |
| Architecture knowledge | `docs/architecture/README.md`; conditional fact-authority, topology, host-runtime, and integration-boundary files | `$evolvable-application-architecture` |
| TypeScript application filenames | kebab-case semantic segments separated by dots; semantic roles co-locate until independent pressure earns files | `$evolvable-application-architecture` |
| Frontend source | `app/` or `host/`, `features/`, `shared/`; stable suffix responsibilities | `$frontend-architecture` |
| Effect source | Effect-specific Service, Layer, Runtime, Queue, Stream, Actor, and failure/resource projections over the project/EAA source grammar | `$effect-best-practices` |
| Verification interface | stable command roles, preferred `verify:affected` and `verify` aliases when practical | `$product-harness-system` |

## Shared path and naming defaults

These defaults apply only when the owning Skill does not define a more specific projection.

```text
ordinary directories and files      kebab-case
local routing document               README.md
append-only ordered decision         0001-short-title.md
TypeScript semantic dimensions       dots between dimensions
one semantic segment                 kebab-case inside the segment
public portable Skill prose          English
project narrative prose              project language policy
paths, commands, schemas, symbols     English unless an external contract requires otherwise
```

Names should expose subject, operation or facet, semantic responsibility, and provider or host qualifier when needed. Generic buckets such as `utils`, `common`, `core`, `services`, `manager`, `types`, or `misc` are review signals when callers cannot predict their scope.

## Shape defaults

- Start with the smallest coherent private boundary.
- Keep distinct semantic roles co-located while their physical separation adds no value.
- Add a directory when it improves stable lexical grouping or discovery.
- Add an explicit public surface when private imports need enforcement.
- Add a package or crate when compilation, reuse, ownership, trust, or public compatibility pressure exists.
- Add a host when runtime, resource, or independent operation pressure exists.
- Add a deployable only for real fault, scaling, trust, or operational separation.

Each promotion is independent. A role does not imply a file; a directory does not imply a package; a package does not imply a deployable; none grants product fact authority.

## Writing shape

Owner-local convention references may use this semantic shape when it helps:

```text
Default
Required invariants
Conditional additions
Project override
Example
Related knowledge
```

This is writing consistency, not an execution workflow.

## Template and example policy

A template or example is retained only when it repeatedly reduces cross-project ambiguity at low cost.

- Delete unused sections.
- Do not create empty siblings for symmetry.
- Do not treat a template as an authority merely because it is complete.
- Present the smallest valid base before conditional shape.
- Express optional files, directories, mechanisms, and documents as pressure-labelled deltas rather than a complete tree followed by disclaimers.
- Treat role and suffix lists as vocabularies, not generation manifests.
- Prefer a few realistic examples over a large form library.
- Introduce a machine schema only when a real consumer needs deterministic validation.

## Deviating from a default

A deviation is healthy when it states:

```text
which invariant remains protected
which local pressure invalidates the default
what the alternative convention is
where future readers can discover it
```

Do not require a formal exception record for every harmless local choice. Record only deviations that materially affect search, ownership, public contracts, tooling, or cross-project review.

## Avoid cargo-cult defaults

Do not retain a convention merely because a successful company or previous version used it. Explain the mechanism: lower search entropy, explicit ownership, mechanical dependency checking, or stable command discovery.

## Default decay

A default may become obsolete when project ecosystems change, the mechanism no longer solves the pressure, or stronger Agent or project affordances remove its value. Re-evaluate behavior, not fashion.

## Related knowledge

- Use [Knowledge portfolio](knowledge-portfolio.md) to choose Owner and form.
- Use [Behavior evidence and failure attribution](behavior-evidence-and-failure-attribution.md) to compare default versus invention.
- Use [Self-application and cargo cult](self-application-and-cargo-cult.md) to challenge inherited form.
- Return to the [Evolution map](../SKILL.md).
