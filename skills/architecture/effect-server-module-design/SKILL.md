---
name: effect-server-module-design
description: Effect v4 server-module review and planning. Use when adding or substantially reshaping a TypeScript server module, admitting a *.public.ts surface, moving a provider behind a Host bridge, resolving Port/Service/Layer/Fake/Live placement, or testing extraction readiness. Skip routine module-local edits and generic Effect API lookup.
---

# Effect Server Module Design

Review or plan the smallest source shape that expresses one settled server capability. This is a thought-and-template Skill: the Agent adapts normal edits or a one-off script to the repository instead of maintaining a generator, manifest, registry, or repair runtime.

## Authority

Project architecture, source standards, accepted decisions, and current source remain authoritative. Use `$evolvable-application-architecture` when owner, final writer, transaction, or package admission is open; use `$effect-best-practices` when Effect failure, Scope, Layer, Runtime, or exact API semantics are open. This Skill starts where those decisions can be projected into files.

Effect v4 is the only default narrative. Bind concrete syntax to the target repository's exact pin, lockfile, installed declarations, typecheck, and tests. A v4 server may still keep pure models, policies, decoders, and transformations as ordinary TypeScript.

## Run

### 1. Recover the change surface

Read the nearest Agent guidance, owning architecture/source rules, target module, its importers, Host composition, and focused tests.

Complete when the following are known or recorded as decision gaps:

```text
owned capability and accepted facts
final writer and governed use cases
real module/Host/test consumers
Host-owned config, credential, transport, pool, Runtime, and lifetime
exact Effect v4 source reality
```

### 2. Classify the boundary

Use the smallest applicable classification:

| Classification      | Completion criterion                                                                      |
| ------------------- | ----------------------------------------------------------------------------------------- |
| `owner-private`     | no real cross-module consumer; no public surface                                          |
| `module-public`     | an admitted consumer can use one narrow `*.public.ts` surface                             |
| `host-bridge`       | Host resources stay outside the module kernel and composition selects the bridge          |
| `package-candidate` | stable multi-host/build/review/trust pressure is evidenced and promotion remains explicit |

`index.ts` carries no visibility meaning. A capability may combine a private implementation, one admitted public surface, and a Host bridge.

Complete when every external import has one allowed entry and every Host dependency has one owner.

### 3. Produce an earned shape

Use [the Module Design Card](templates/module-design-card.md) and propose the minimum concrete tree.

Apply these anchors:

- **Private first.** Future possibility keeps the module private; a real consumer earns public admission.
- **Earned files.** A separate file needs an independent change, reuse, contract, substitution, lifecycle, trust, navigation, or enforcement pressure.
- **One contract.** Choose an ordinary Port or an Effect Service as the canonical capability contract; add translation only for distinct consumers or trust boundaries.
- **Host owns power.** Config, credentials, concrete transports, pools, Layer/Runtime composition, startup, shutdown, and resource lifetime stay with the Host.
- **Kernel owns meaning.** Rules, normalized provider protocol, error algebra, and transaction meaning stay with the owning module.
- **Behavioral substitutes.** Fake and Live implement the same observable contract; Host composition selects required Live dependencies explicitly.
- **Boundary proof.** Private tests may inspect internals; contract/adoption consumers use the public surface; integration tests exercise the selected Host graph and name their dependency reality.

Complete when every proposed file states the pressure that earns it. Remove any file whose only reason is symmetry.

### 4. Return the review or plan

For an existing module, classify each delta as `keep`, `move`, `rename`, `merge`, `remove`, `add`, or `block`. For a new module, return the target tree directly.

Return in this order:

1. boundary verdict;
2. decision gaps that can change the shape;
3. minimal target tree;
4. delta;
5. allowed and forbidden import edges;
6. earned Effect v4 mechanisms;
7. focused proof delta, dependency reality, claim ceiling, and `not_proven`.

When implementation is requested, edit the actual repository and run its existing quality/proof commands selected by the changed property. The work is complete only when every changed boundary has source evidence or an explicit unresolved decision; a plausible file tree alone is not completion evidence.
