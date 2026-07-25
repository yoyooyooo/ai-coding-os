---
name: interface-capability-planning
description: >-
  Interface capability planning from user work to IA, surfaces, interaction
  states, frontend ownership, and proof needs. Use when planning app shells,
  navigation, routes or pages, UI states, frontend handoff, existing-interface
  increments, or headless-to-interface growth.
---

# Interface Capability Planning

Plan user-facing capabilities as traceable interface contracts rather than a
page list.

```text
Accepted Product Obligation + source IDs
  -> InterfaceCapability
     -> IA / Surface / Region
     -> Interaction State Contract
     -> frontend owner map
     -> UI and/or Headless Harness refs
```

## Ownership

```text
Owns:
  user work -> InterfaceCapability mapping
  surface, region, and entrypoint trace
  pending/success/failure/recovery contract
  technology-neutral frontend ownership needs
  testability and harness handoff needs

Adjacent Suite owners, when installed:
  product obligations, Requirement/Rule/AC IDs, and Product Design Handoff -> $product-definition
  frontend implementation topology -> $frontend-architecture
  shared proof language -> $product-harness-system
  UI proof -> $ui-product-harness
  product-fact proof -> $headless-product-harness
```

Product/domain/API/database truth, concrete test code, evidence lifecycle, and
brand/visual-system decisions remain with their owners.

## Capability Coverage

Cover applicable decisions in the order exposed by the current interface concern; this is not a project workflow.

| Decision | Completion criterion |
| --- | --- |
| Ground | Relevant Product, SSoT, Architecture, Standards, interface/design material, and existing harnesses are identified. |
| Start from work | The user's job and owning product capability are stated before any page or component decomposition. |
| Choose mode | One mode—generic capability, headless-to-interface, existing-interface increment, or provisional interaction island—fits the known authority. |
| Contract | Entrypoint, surfaces/regions, intent, state owners, pending/success/failure/recovery, projection/realtime behavior, and proof needs are explicit. |
| Hand off | Framework choices are left to `$frontend-architecture`; required headless and UI proof surfaces are named by capability rather than implementation detail. |
| Persist proportionately | Output stays inline unless durable trace will serve future work; persisted artifacts have a project-governed home and stable IDs. |

## Rules

- Use `InterfaceCapability` and `InterfaceSurface` as stable object kinds.
- Reference accepted Product Requirement, Rule, and AC IDs when they exist;
  map their obligations without redefining product rules.
- Reference Harness IDs; retain execution evidence with its owning harness or
  evidence method.
- Distinguish local interaction, remote projection, async command, realtime,
  URL, derived view model, and canonical Proof Surface fields. `render_wiring`
  is a render proof focus; browser is an observation surface.
- Keep selectors and framework internals in implementation artifacts.
- Interface proof supports interface claims; backend fact correctness requires
  a backend proof surface.
- A provisional `interaction-island` may remain `sketch` or `candidate` with
  explicit gaps.

A repository-selected execution method may reference the InterfaceCapability
artifact; execution state remains with that method and this skill stays
independently usable.

## Output

```text
capability
user_work
entrypoints
surfaces_and_regions
interaction_states
frontend_owner_map
proof_needs
trace_refs
gaps
not_proven
```

For the detailed artifact workflow, read
[Planning Workflow](references/planning-workflow.md) when durable trace or a
multi-surface handoff is needed.
