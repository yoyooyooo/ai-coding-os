# Version Adapter: Effect v3 Stable

Use only when the project installs Effect v3. Read local package types and the
matching official docs for the exact minor version.

Typical v3 idioms include:

```text
Effect.Effect<A, E, R>
Context.Tag or Effect.Service depending project convention/version
Layer.succeed / Layer.effect / Layer.scoped
Effect.scoped / Effect.acquireRelease
ManagedRuntime.make for long-lived closed Layer graphs
```

Do not rewrite a working v3 codebase to v4 syntax during an unrelated change.
Treat major migration as an explicit project with compile fixtures, resource
lifecycle tests, error-behavior characterization, and deletion of compatibility
bridges.

The bundled `examples/effect-v3-runtime-client.example.ts` is a compile fixture,
not a universal style mandate.
