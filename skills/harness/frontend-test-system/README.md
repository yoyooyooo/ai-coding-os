# Frontend Test System

Single frontend testing skill for AI coding. It replaces the previous test-skill cluster with one proof router plus short references.

## Model

```text
change -> claim register -> smallest proof lane -> command/browser/contract evidence -> claim ceiling
```

The skill should make an agent answer:

```text
What am I proving?
What is the smallest sufficient lane?
What evidence did I produce?
What did I not prove?
```

## Layout

```text
<skill-root>/frontend-test-system/
  SKILL.md
  README.md
  references/
    claim-discovery.md
    e2e-playwright.md
    unit-integration.md
    quality-gates.md
    contract.md
    evidence.md
    upstream-sources.md
```

| File | Purpose |
| --- | --- |
| `SKILL.md` | only model-invoked entry; workflow, routing, claim ceilings, evidence packet |
| `claim-discovery.md` | turn request / bug / diff into claims |
| `e2e-playwright.md` | durable Playwright E2E lane |
| `unit-integration.md` | Vitest/Jest/Testing Library/MSW lane |
| `quality-gates.md` | agent-browser runtime, a11y, visual, responsive gates |
| `contract.md` | frontend/backend contract seam |
| `evidence.md` | response packet shape |
| `upstream-sources.md` | official docs and absorbed source list |

## Boundaries

- `agent-browser` stays global: live browser exploration, screenshots, console, network, dogfood.
- `vitest` stays global: Vitest runner details and API guidance.
- Playwright is for committed browser regression tests.
- MSW proves frontend handling of modeled HTTP responses, not backend truth.
- A11y scans are gates, not full WCAG audits.
- Visual screenshots are regression evidence, not design approval.
- Cypress and Jest are legacy runner context only; do not add new leaf skills here.

## Migration / Maintenance

Keep this as the only concrete frontend testing proof router in its catalog. Old local harnesses and leaf skills should remain deleted:

```text
frontend-e2e-playwright-harness
frontend-unit-integration-harness
frontend-quality-gates
fullstack-contract-harness
testing-strategy
playwright-best-practices
e2e-testing-patterns
browser-testing-with-devtools
javascript-typescript-jest
msw
playwright-testing
api-contract-testing
visual-regression-testing
react-testing-library
```

Do not register this skill as tracked upstream. Do not reintroduce deleted leaf skills as install sources or upstream records. Upstream URLs belong only in `references/upstream-sources.md`.

## Done State

The canonical catalog should contain one governed `$frontend-test-system`, and projected router/docs indexes should point frontend test-proof work to it.
