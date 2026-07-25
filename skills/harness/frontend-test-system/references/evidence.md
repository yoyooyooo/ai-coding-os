# Frontend Test Observation Report

A frontend testing response should separate the executed observation from the
bounded conclusion and from adjacent behavior that was not exercised. Keep the
report proportional to the task; a small test may need only a few lines.

## Recommended shape

```text
property:
lane:
runner_or_tool:
commands_or_actions:
proof_surface:
test_environment:
fixtures_or_seed:
observed:
supports:
not_proven:
artifacts:
```

## Field rules

- `property`: one bounded behavior, not “the app works”.
- `lane`: unit, component, MSW, contract, Playwright, browser inspection, or the
  repository's established equivalent.
- `runner_or_tool`: exact tool when relevant.
- `commands_or_actions`: actual command/route/browser actions and status.
- `proof_surface`: canonical observation surface, dependency realities,
  environment class when material, and owner-local proof focus.
- `test_environment`: runner-specific browser, viewport, base URL, CI/local,
  auth subject, or configuration needed to reproduce the run.
- `fixtures_or_seed`: deterministic data, auth subject, MSW handler, database
  seed, or cleanup that influenced the result.
- `observed`: direct output, visible state, console/network status, trace, count,
  or value from the executed path.
- `supports`: bounded conclusion justified by those observations and project
  authority.
- `not_proven`: adjacent desired behavior not exercised because of lane,
  environment, fake dependencies, credentials, missing authority, skips, or tool
  limits.
- `artifacts`: trace, screenshot, video, report, diff, log, coverage, or schema
  output when useful.

## Observed examples

Good:

```text
observed:
- `pnpm test src/cart/cart.test.ts` exited 0 with `8 passed`
- MSW handler `cart-empty` returned the declared empty response
- browser showed heading `Your cart is empty`
- Playwright trace exists at `test-results/cart-empty/trace.zip`

supports:
- the frontend renders the declared empty-cart state under the MSW profile

not_proven:
- real backend empty-cart response
- production authentication
```

Weak:

```text
observed:
- looks good
- should pass
- covered by tests
```

Those statements contain no direct observation.

## Failure report

A failed run is still useful evidence. Add:

```text
failure_phase:
failing_command_or_step:
first_error:
reproduction:
likely_owner_boundary:
blocked_by:
```

Do not replace a failed observation with a plan or erase earlier instability
because a later retry passed.

## Artifact naming

Prefer stable property-scoped names:

```text
playwright: test-results/<property>/trace.zip
screenshots: artifacts/<property>/<before|after|diff>-<viewport>.png
logs: artifacts/<property>/console-network.log
contract: artifacts/<property>/schema-or-pact-output.txt
```

Persist full provenance only when the result must survive across Agents,
commits, release decisions, or audits.
