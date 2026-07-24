---
name: ui-product-harness
description: >-
  UI product proof across interface-headless state, render wiring, and real
  browser paths. Use when validating interaction states, frontend
  reconciliation, routes, reload/focus/navigation, browser-visible behavior, or
  an InterfaceCapability's proof surfaces.
---

# UI Product Harness

Make one user-facing capability observable from frontend state through render
and, when required, a real browser. A UI harness is proof infrastructure; it
uses the same frontend ownership model as the product.

Shared harness language comes from `$product-harness-system`; frontend state and
host semantics come from `$frontend-architecture`; concrete runner selection
comes from `$frontend-test-system`.

## Ownership

```text
Owns:
  interface-headless proof
  harnessable component and surface design
  render-wiring proof
  browser-visible proof
  frontend adapter/state/query/realtime observation points
  UI claim ceilings and gaps

Adjacent owners:
  interface capability contract -> $interface-capability-planning
  frontend topology -> $frontend-architecture
  backend fact proof -> $headless-product-harness
  concrete test lane -> $frontend-test-system
  docs placement -> $docs-governance
```

## UI Proof Pass

| Step | Completion criterion |
| --- | --- |
| Ground | Interface capability, frontend owner map, route tree, host composition, state/query/realtime code, and existing tests/harnesses are identified. |
| Trace | One user intent and its authoritative projection are named from dispatch through reconciliation and render. |
| Select | Interface-headless, render-wiring, browser-visible, or production-near is the smallest surface that can observe the property. |
| Reuse | Product clients, Query/store/realtime boundaries, commands, and resource owners remain the harness path. |
| Observe | Required pending/success/error/recovery, projection, route, reload/focus/navigation, console/network, accessibility, or layout observations are collected. |
| Bound | Fake/live conditions, supported conclusion, backend dependencies, `not_proven`, and claim ceiling match the executed surface. |

## Surface Model

### Interface-headless

Use for pure mapper/view-model, client/query/store, optimistic reconciliation,
realtime decode/dedupe/cursor/gap/backfill, and router-state properties. It
supports no browser reachability or backend-materialization claim.

### Render wiring

Use a thin component or surface harness to observe control dispatch, accessible
affordances, and bounded rendered states. Real reload, backend, and visual
approval remain separate claims.

### Browser-visible

Use a real browser for user paths, focus and keyboard, navigation and deep
links, reload, console/network, hydration, responsive spots, and visible
recovery. Pair with backend proof before claiming accepted product facts.

### Production-near

Use real local or staged dependencies when the property requires them. Name
every fake, local, excluded, credentialed, and externally deployed boundary.

## Topology

Keep feature-specific harnesses near the feature:

```text
apps/web/src/features/orders/
  order.checkout.surface.tsx
  order.checkout.view-model.ts
  order.checkout.interface.harness.ts
  order.checkout.browser.test.ts
```

Create a dedicated harness route or host when durable discovery or runtime value
justifies it. Framework route files stay thin and outside formal product
navigation unless adopted as product routes.

## False-Proof Audit

Check for:

```text
frontend fake reported as backend correctness
render test reported as browser path
reload reported as realtime continuity without gap/backfill evidence
transport frame mutating canonical product state
harness creating an accidental second QueryClient/runtime/resource owner
raw transport DTO driving components without mapping
assertion weakened instead of implementation repaired
```

## Output

```text
capability
frontend_owner_map
selected_surface
entry_route_or_component
fake_live_reality
observed
supports
not_proven
claim_ceiling
headless_or_contract_refs
```

Read [Harness Ladder](references/harness-ladder.md) when choosing among proof
surfaces, [Frontend Boundary Model](references/frontend-boundary-model.md) when
ownership is unclear, [Adapter Discovery](references/adapter-discovery.md) for
existing seams, and [Interface Trace DSL](references/interface-trace-dsl.md)
when durable trace is required.
