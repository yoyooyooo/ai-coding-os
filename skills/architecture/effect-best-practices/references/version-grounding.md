# Version Grounding

Effect APIs can differ materially across major versions and beta lines. The local repository, not a remembered example, is the authority for concrete syntax.

## Evidence order

```text
package manager lockfile
installed package metadata
type declarations and editor/compiler diagnostics
official documentation for the exact version
local working examples and tests
community examples with explicit version
memory or generic snippets
```

## Ground the question

Before recommending code, identify:

```text
Effect package version
related platform/http/schema package versions
TypeScript version and module settings
runtime (Node/Bun/Deno/browser)
existing project conventions
```

## API drift examples

Version changes may affect:

```text
Service/Context definition
Layer constructors and composition
Runtime creation and execution
Scope/finalizer helpers
Schema/Config APIs
HttpApi packages and handler composition
Queue/Stream operators
TestClock and testing helpers
```

Do not provide one blended example that compiles in no actual version.

## Migration

When moving between major versions:

- preserve capability and failure semantics first;
- isolate API translation at owner boundaries;
- compile and test one coherent slice;
- avoid mixing old and new patterns throughout the repository;
- remove compatibility wrappers once no consumer remains.

A version migration does not justify changing product authority or source topology unless new evidence makes that change independently valuable.

## Uncertainty

When exact syntax cannot be verified, state the semantic recommendation and the local evidence still required. Do not invent plausible API names.

## Related knowledge

- Use [Default Effect module conventions](default-effect-module-conventions.md) for version-independent file roles.
- Use [Testing Effect](testing-effect.md) to validate the local API.
- Use [HttpApi integration](httpapi-integration.md) for version-sensitive HTTP concerns.
- Use `$docs-governance` for freshness and invalidation of technical docs.
- Return to the [Effect map](../SKILL.md).
