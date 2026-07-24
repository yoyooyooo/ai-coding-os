# Frontend / Backend Contract Playbook

Use when the risk is drift between frontend expectations and backend/API behavior.

## Contract Authority

Find the strongest local source of truth:

1. OpenAPI/Swagger spec.
2. GraphQL schema and operation documents.
3. tRPC/router types or generated client.
4. Shared TypeScript types plus server route tests.
5. Pact or another consumer/provider contract suite.
6. Documented examples/fixtures, marked as weak authority.

If no authority exists, report `contract_authority=missing` before writing broad tests.

## Proof Levels

| Level | Proves | Does not prove |
| --- | --- | --- |
| Static/type/schema check | Shape compatibility with named authority | Runtime behavior or semantics |
| Frontend consumer test with MSW | UI/client handles modeled responses | Real backend behavior |
| Provider/server contract test | Endpoint satisfies contract cases | Frontend consumption |
| Real-backend E2E smoke | One visible path through both sides | Exhaustive API behavior or all states |

Choose the lowest level that proves the claim. Combine levels only when the user asked for cross-boundary confidence.

## Case Selection

Model cases from product behavior:

- Loading.
- Success with representative data.
- Empty data.
- Validation/client error.
- Auth/permission failure.
- Server failure/retry state.
- Pagination/filtering/sorting when visible.
- Stale or changed shape when drift is the concern.

## MSW Alignment

- MSW fixtures must mirror the authority or be labeled `fixture_only`.
- Keep happy path as baseline; override per test for error/empty/edge cases.
- Do not let MSW become a second undocumented API spec.
- When mocks and contract disagree, fix the mock or flag contract drift; do not hide it with broader E2E.

## Real Backend Boundary

Only claim real backend behavior when the command actually hit the real/staged backend and evidence includes environment/base URL/seed. If credentials, seed data, or server logs are unavailable, report the gap.

## Evidence Additions

```text
contract_authority:
proof_level:
frontend_command:
backend_or_schema_command:
mock_cases:
real_backend_used:
base_url_or_env:
observed:
supports:
not_proven:
```

## Claim Ceiling

Contract work proves compatibility at a named seam. It does not prove full business semantics, UI reachability, or production readiness unless those are separately tested with appropriate lanes.
