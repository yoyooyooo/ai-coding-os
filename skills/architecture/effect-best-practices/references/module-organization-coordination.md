# Effect Module Organization Coordination

Establish semantic ownership before selecting Effect syntax.

```text
Context.Service does not automatically mean domain boundary
Layer does not automatically mean composition root
Stream does not automatically mean business-event authority
Queue does not automatically mean durable work queue
ManagedRuntime does not automatically mean application singleton
```

## Shared source doctrine

Inherit Bounded Semantic Flatness, module/package/deployable promotion, and core
vocabulary from `$evolvable-application-architecture`; load the machine-readable
portable vocabulary from `$ai-coding-os-suite-contracts` only when needed.

Recommended mapping:

```text
<capability>.port.ts                    ordinary application-owned contract
<capability>.service.ts                 Effect Service key only when genuinely useful
<capability>.<provider>.live.ts         live Layer/adapter implementation
<capability>.memory.fake.ts             Effect-specific deterministic implementation of the shared fake boundary
<subject>.<operation>.use-case.ts       application operation, Effect or ordinary TS
<host>.composition.ts                   Layer graph selection and host assembly
<host>.runtime.ts                       owned runtime facade when needed
<subject>.model.ts                      pure decisions and data
```

These are semantic patterns, not a requirement to create every file.

## Package boundary

A package using Effect internally normally exports:

```text
ordinary capability contract/factory
normalized public errors
explicit close/subscription contract when relevant
optional Effect-native entrypoint when the package intentionally exposes Effect
```

Keep internal Service keys, Layers, runtime construction, and transports private
unless the package is deliberately Effect-native.

## Host ownership

Each deployable host constructs and closes its own live Layer/runtime graph.
Packages may export Layer factories, not hidden process-global runtimes.

An Effect Layer graph is an execution dependency graph. It does not grant fact
authority and does not dictate module/package/process extraction.
