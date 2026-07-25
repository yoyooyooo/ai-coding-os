---
name: frontend-test-system
description: >-
  Frontend test-lane selection for a bounded property. Use when concrete
  frontend behavior needs the smallest honest unit, component, MSW, contract,
  Playwright, accessibility, visual, or browser-inspection lane; reusable UI
  proof architecture stays with $ui-product-harness.
---

# Frontend Test System

Match one changed property to the smallest test lane that can observe it. Reuse
the repository's runner, fixtures, clients, and nearby conventions.

## Ownership

```text
Owns:
  concrete frontend test-lane and runner selection for one bounded property
  repository-native execution and durable regression judgment

Adjacent Suite owners, when installed:
  InterfaceCapability source -> $interface-capability-planning
  reusable UI proof surface and claim ceiling -> $ui-product-harness
  cross-surface proof architecture -> $product-harness-system
```

## Test Coverage

Cover applicable decisions in the order exposed by the property and repository; this is lane selection, not a project workflow.

| Decision | Completion criterion |
| --- | --- |
| Ground | `AGENTS.md`, scripts, lockfile, runner config, app start path, contracts/clients/mocks, and nearby tests establish the available lanes. |
| Property | The bounded property is stated in ordinary language with the relevant fake/live environment. |
| Lane | One primary lane can fail on the property for the right reason; additional lanes cover distinct claims only. |
| Execute | Repository-native commands or browser actions run and produce direct observations. |
| Interpret | The report separates observation, supported conclusion, artifacts, and adjacent `not_proven` surfaces. |
| Retain | A durable regression test is added only when its future signal exceeds maintenance cost; exploratory inspection may remain an observation. |

## Lane Selection

| Property | Primary lane |
| --- | --- |
| Pure mapper, parser, reducer | unit logic |
| Component, hook, form, local state | component behavior |
| Frontend handles modeled HTTP | MSW integration |
| API/client/provider compatibility | contract |
| Browser journey | Playwright E2E |
| Current rendered debugging | browser inspection |
| Keyboard or focus | browser or Playwright |
| Automated accessibility | installed browser scanner |
| Screenshot/layout regression | existing visual lane |
| Responsive spot | browser or Playwright viewport |

Reusable surfaces, routes, coverage, and cross-state proof architecture belong
to `$ui-product-harness`.

## Claim Ceilings

```text
unit/component
  chosen deterministic boundary; not browser or real backend

MSW
  frontend behavior against modeled responses; not backend correctness

contract
  compatibility at a named seam; not full product behavior

Playwright
  bounded browser path under stated data and environment

browser inspection
  current runtime observation; not durable regression by itself

a11y scan
  detectable issues in scanned states; not complete accessibility acceptance

visual screenshot
  comparison to a baseline/environment; not design approval or semantic correctness
```

## Output

```text
property
test_lane
commands_or_browser_actions
proof_surface
test_environment
observed
supports
not_proven
artifacts
```

## Read When Needed

- Broad claim decomposition: [Claim Discovery](references/claim-discovery.md)
- Playwright details: [E2E Playwright](references/e2e-playwright.md)
- Unit/component/MSW details: [Unit and Integration](references/unit-integration.md)
- Repository quality gates: [Quality Gates](references/quality-gates.md)
- Contract proof: [Contract](references/contract.md)
- Evidence reporting: [Evidence](references/evidence.md)
- Tool-source guidance: [Upstream Sources](references/upstream-sources.md)
