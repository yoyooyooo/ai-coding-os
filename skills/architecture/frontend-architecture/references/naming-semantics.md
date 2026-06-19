# Naming Semantics

Names should reveal product subject and architectural responsibility. A naming
system is useful only when it makes ownership and imports easier to predict.

## Decision Rule

1. Name the product/capability subject first.
2. Add a semantic suffix only when it communicates a stable responsibility.
3. Prefer project-established vocabulary over a universal word list.
4. Treat generic names as review signals, not automatic failures.
5. Document new long-lived suffix semantics before they spread.

Examples:

```text
channel.query.ts
channel.realtime.ts
channel.view-model.ts
channel.client.browser.live.ts
result.surface.tsx
transport.http.ts
```

Do not generate a full suffix set mechanically.

## Generic Bucket Test

Names such as `utils`, `helpers`, `common`, `services`, `components`, `core`,
`internal`, or `lib` can become dumping grounds, but some projects use them
legitimately. Reject or rename when at least one is true:

```text
no coherent authority or subject
unrelated imports accumulate
callers cannot predict public/private scope
file placement is chosen only because no better owner was identified
bucket creates dependency cycles or deep imports
```

Allow a generic name when scope and responsibility are explicit, for example a
published component library, a package-private `internal/`, or a tiny pure
utility module with a narrow public API.

## Common Suffix Semantics

`.client.ts`: typed capability contract/facade; no React/query/store/view code.

`.client.<host>.live.ts`: host-specific implementation and resource construction.

`.client.fake.ts`: deterministic fake for tests/harnesses; never silent
production fallback.

`.query.ts`: query/mutation options or hooks consuming an injected client.

`.store.ts`: local interaction state; not a remote projection mirror.

`.realtime.ts`: typed projection reduction and lifecycle glue; no transport
construction.

`.mappers.ts`: pure boundary conversion from decoded DTO/envelope to feature
projection.

`.view-model.ts`: pure combination of projection and local interaction for a
surface.

`.page.tsx`: page/container glue for feature capabilities.

`.surface.tsx`: harnessable UI consuming a view model and callbacks.

`.fixture.ts`: static sample data; not mutable fake behavior.

`.public.ts`: optional explicit feature public surface when framework or project
rules prefer it. A package root `index.ts` may also define its public API.

## Import Semantics

Do not hide dependency direction behind broad aliases or barrels. Aliases and
barrels are acceptable when they preserve an explicit public API and boundary
checks reject private/deep imports.
