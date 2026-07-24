# Claim Discovery

Use before selecting tests. Convert the request, bug, diff, or browser symptom into a small claim register.

## Register

```text
claim:
source:
risk:
priority: P0_must_prove | P1_should_prove | P2_optional
observable:
candidate_lane:
assumptions:
does_not_cover:
not_proven_if_skipped:
```

| Priority | Meaning | Action |
| --- | --- | --- |
| `P0_must_prove` | Central requested behavior or bug fix | Prove it or report blocked / `not_proven` |
| `P1_should_prove` | Important adjacent regression risk | Prove if cheap; otherwise list as gap |
| `P2_optional` | Useful but not required | Do not expand unless requested |

## Inputs

Inspect only what is needed to avoid guessing:

```text
user request / bug reproduction / failing command
changed files and nearby tests
affected route, component, hook, form, store, cache, API client, schema, or mock
project scripts, CI command, runner config, seed/auth notes
agent-browser observation when runtime state is unclear
```

## Surface Map

| Surface | Good claim shape | Lane |
| --- | --- | --- |
| Utility, parser, mapper | Given X, output/error Y occurs | `unit_logic` |
| Reducer, store, state machine | Transition X -> Y occurs | `unit_logic` or `frontend_integration` |
| Component / conditional UI | Text, role, state appears or disappears | `component_behavior` |
| Form | Validation, disabled state, submit result, or error display occurs | `component_behavior` or `frontend_integration` |
| HTTP client behavior | Frontend handles success/error/empty response | `frontend_integration` with MSW |
| API schema/client | Frontend/backend seam stays compatible | `frontend_backend_contract` |
| Route, auth, navigation | User reaches or is blocked from expected page | `browser_journey` |
| Dialog, menu, focus | Keyboard and focus behavior works | `keyboard_focus` |
| CSS/layout/responsive | Critical UI remains visible/usable | `responsive_spot` or `visual_regression` |
| Broad refactor | Representative behavior still holds | existing suite + targeted smoke |

## Rules

- Keep ordinary work to 1-5 high-value claims.
- Group broad refactors by behavior, not by file.
- Do not create claims for private implementation details.
- Rewrite tool-shaped requests into behavior-shaped claims.
- Ask only when ambiguity blocks safe implementation or proof; otherwise state the assumption and continue.
- Select all P0 claims, cheap P1 claims, and no P2 claims unless requested or already covered.

Bad:

```text
Cart works.
Add Playwright coverage.
Hook calls setState.
```

Good:

```text
When /api/cart returns { items: [] }, the Cart page shows "Your cart is empty" and does not show the Checkout button.
A signed-in new user can complete onboarding and land on Dashboard.
Frontend order client accepts the current Orders response schema.
```

## Completion

Claim discovery is complete when every selected P0 behavior has a candidate lane, observable token, explicit assumptions, and adjacent scope listed under `does_not_cover` and skipped desired behavior under `not_proven_if_skipped`.
