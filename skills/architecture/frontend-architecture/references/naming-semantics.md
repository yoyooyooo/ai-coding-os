# Frontend Naming Semantics

Use `$ai-coding-os-suite-contracts` for Suite-wide grammar, canonical terms,
filename patterns, and guarded terms. Cross-Skill lookup uses the canonical
Skill name rather than an assumed sibling directory.

This reference defines frontend extensions. It does not create a second source
for `public`, `wiring`, module/package promotion, or dot/hyphen semantics.

## Decision rule

1. Name the product/capability subject first.
2. Use kebab-case inside one semantic segment and dots between dimensions.
3. Add a suffix only when it communicates a stable responsibility.
4. Reuse project canonical terms from `docs/standards/naming-vocabulary.yaml`.
5. Treat generic names as review signals, not automatic failures.
6. Register a new long-lived frontend responsibility before it spreads.
7. Do not generate a full suffix set mechanically.

Examples:

```text
channel.query.ts
channel.realtime.ts
channel.view-model.ts
channel.client.browser.live.ts
result.surface.tsx
transport.http.ts
```

## Frontend suffix semantics

`.client.ts` — typed product capability contract/facade; no React/query/store/view code.

`.client.<host>.live.ts` — host-specific real implementation and resource construction.

`.client.fake.ts` — explicit deterministic behavioral replacement; never silent production fallback.

`.query.ts` — query/mutation options or hooks consuming an injected client.

`.store.ts` — local interaction state; not a remote projection mirror.

`.realtime.ts` — typed projection reduction, continuity, dedupe, gap/backfill glue; no transport construction.

`.mapper.ts` — pure conversion between named wire/projection/view representations. Prefer a singular stable responsibility, for example `order.wire-to-projection.mapper.ts`.

`.view-model.ts` — pure combination of projection and local interaction for a surface.

`.page.tsx` — route/page container glue.

`.surface.tsx` — harnessable UI consuming a view model and callbacks.

`.fixture.ts` — static sample data; not mutable fake behavior.

`.public.ts` — explicit feature public surface when useful. Package `index.ts` may be a thin explicit re-export for tooling convention.

## Generic bucket test

Names such as `utils`, `helpers`, `common`, `services`, `components`, `core`,
`internal`, or `lib` are acceptable only when callers can predict scope and
responsibility. Rename when unrelated imports accumulate, public/private scope
is unclear, or the bucket exists only because no owner was identified.

## Import semantics

Do not hide dependency direction behind broad aliases or wildcard barrels.
Aliases and barrels are acceptable when they preserve an explicit public API and
checks reject private/deep imports.
