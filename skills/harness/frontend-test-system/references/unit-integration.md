# Unit, Component, and Frontend Integration Playbook

Use for deterministic frontend tests below the browser-journey layer.

## Runner Rule

- Prefer the repo runner and scripts.
- Use global `vitest` guidance when the repo uses Vitest.
- Jest is legacy context: keep existing tests working, but do not introduce Jest as the default or migrate automatically.
- Read `vitest.config.*`, `jest.config.*`, setup files, aliases, test environment, and test utilities before writing tests.

## Target Routing

| Target | Preferred proof | Mock policy |
| --- | --- | --- |
| Utility / parser / mapper / reducer | Unit test | No mocks except time/randomness |
| Hook / state machine / view model | Integration-style unit test | Real state transitions; mock outside services |
| React component | Testing Library component test | Real DOM queries and user events |
| Frontend HTTP behavior | Integration test with MSW | Mock HTTP, not fetch/client internals |
| Router/cache/query behavior | Integration around real adapter | Mock HTTP/time only as needed |

## Assertion Rules

- Assert behavior visible to users, callers, or contracts.
- Prefer accessible queries: role/name, label, text, alt text; use test IDs only when semantics cannot identify the element.
- Prefer `userEvent`-style interactions over low-level event firing when available.
- Use async queries/waits for async UI; avoid redundant waits around already-waiting queries.
- Avoid snapshot-only tests, private state assertions, and tests that duplicate implementation logic.

## Mock Boundary

Every mock needs:

```text
mocked_thing:
why_outside_boundary:
what_real_behavior_is_not_proven:
```

Use the narrowest mock that preserves the claim:

- Time/randomness: fake timer or deterministic value.
- HTTP: MSW handlers.
- Missing browser API: small adapter mock.
- Module mock: only when the dependency is outside the behavior boundary.

## MSW Boundary

MSW is frontend HTTP mocking, not proof of the real service.

- Keep handlers aligned to the contract authority when one exists.
- Use default happy-path handlers plus per-test overrides for errors, empty states, auth failures, pagination, malformed/stale shapes, and retries.
- Reset runtime handlers after each test.
- Treat unhandled requests as missing contract coverage unless intentionally bypassed and documented.
- Prefer asserting UI/result caused by the response over asserting that a request happened.

## Run Loop

1. Run the target file or focused test.
2. Fix assertion/fixture/setup gaps.
3. Run the changed package test script or relevant CI group.
4. Add coverage only if the repo requires it or the user asks.

## Evidence Additions

```text
target:
runner:
environment:
command:
mock_boundary:
assertions:
msw_cases:
observed:
supports:
not_proven:
```

## Claim Ceiling

These tests prove deterministic behavior at a chosen boundary. They do not prove browser reachability, CSS layout, production auth, real backend correctness, cross-browser behavior, or a complete user journey.
