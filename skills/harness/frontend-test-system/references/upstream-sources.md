# Upstream Sources

Stable routing, claim ceilings, and evidence rules live in this skill. Volatile tool syntax, flags, APIs, and version-specific edge cases must be checked from project config and official docs when needed.

## Official Sources

```text
Playwright best practices:
https://playwright.dev/docs/best-practices

Playwright actionability / auto-waiting:
https://playwright.dev/docs/actionability

Playwright traces:
https://playwright.dev/docs/trace-viewer

Playwright visual comparisons:
https://playwright.dev/docs/test-snapshots

Playwright accessibility:
https://playwright.dev/docs/accessibility-testing

Vitest:
https://vitest.dev/guide/

Testing Library queries:
https://testing-library.com/docs/queries/about/

Testing Library user-event:
https://testing-library.com/docs/user-event/intro/

MSW:
https://mswjs.io/docs/
```

## Distilled Source Set

These former runtime skills were absorbed as design input only; do not route to them or reintroduce them as separate governed skills:

```text
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

## Refresh Rules

- Trust project config over generic examples for command names and local conventions.
- Trust official docs over this file for API syntax and version-specific behavior.
- Update this skill only for stable routing, claim discovery, evidence, and claim ceiling changes.
- Do not copy upstream tutorials into runtime skills.
