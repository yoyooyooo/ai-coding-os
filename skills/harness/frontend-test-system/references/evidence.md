# Evidence Packet

Every testing response must separate what was proven from what was only inspected, assumed, mocked, skipped, or left untested.

## Required Packet

```text
claim:
lane:
runner_or_tool:
repo_state:
commands:
environment:
fixtures_or_seed:
artifacts:
positive_tokens:
not_claimed:
not_proven:
next_gap:
```

## Field Rules

- `claim`: one narrow statement. Avoid "the app works".
- `lane`: one routed lane from `SKILL.md`.
- `runner_or_tool`: exact tool, such as `vitest`, `jest`, `playwright`, `agent-browser`, `openapi`, `pact`, or `manual-none`.
- `repo_state`: discovered scripts/config relevant to this claim.
- `commands`: exact commands and pass/fail/skipped status.
- `environment`: OS/container if known, browser, viewport, base URL, env/CI, backend/mock boundary.
- `fixtures_or_seed`: auth user, seeded data, MSW handlers, database seed, cleanup.
- `artifacts`: trace, screenshot, video, HTML report, diff image, console/network log, coverage, schema output.
- `positive_tokens`: concrete success evidence from output or UI.
- `not_claimed`: areas intentionally outside scope.
- `not_proven`: desired but unverified areas due to mocks, missing env, missing authority, unavailable credentials, skipped commands, or tool limits.
- `next_gap`: smallest next action only when a gap remains.

## Positive Token Examples

Good:

```text
positive_tokens:
- `pnpm test src/cart/cart.test.ts` -> `8 passed`
- `/api/cart` mocked by MSW case `cart-empty`
- agent-browser observed heading `Your cart is empty`
- Playwright trace: `test-results/cart-empty/trace.zip`
```

Weak:

```text
positive_tokens:
- looks good
- should pass
- covered by tests without command/output
```

## Failure Packet

For failures, keep the same packet and add:

```text
failure_phase:
failing_command_or_step:
first_error:
reproduction:
likely_owner_boundary:
blocked_by:
```

A failed test run is still evidence. Do not replace failed evidence with a plan.

## Artifact Naming

Prefer stable, claim-scoped names:

```text
playwright: test-results/<spec-or-claim>/trace.zip
screenshots: artifacts/<claim>/<before|after|diff>-<viewport>.png
logs: artifacts/<claim>/console-network.log
contract: artifacts/<claim>/schema-or-pact-output.txt
```

If an artifact was expected but not produced, list it under `not_proven` or `next_gap`.
