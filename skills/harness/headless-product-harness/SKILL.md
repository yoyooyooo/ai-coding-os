---
name: headless-product-harness
description: >-
  Headless product proof through capability commands, structured output,
  fixture/fake/replay, adapter/database/restart paths, and boundary checks. Use
  when a product property should be runnable without a browser or headless
  execution is the smallest honest proof surface.
---

# Headless Product Harness

Turn one product property into a runnable, machine-readable observation path
through the formal product boundary. Shared vocabulary and cross-surface trace
belong to `$product-harness-system`.

## Ownership

```text
Owns:
  headless command surface
  structured JSON/JSONL output
  fixture/fake/replay selection
  adapter and persistence proof
  restart and recovery paths
  architecture boundary checks
  empirical Probe Request and headless claim ceiling

Adjacent Suite owners, when installed:
  Product AC/UAT source semantics -> $product-definition
  fact authority and production boundary -> $evolvable-application-architecture
  shared proof architecture -> $product-harness-system
  UI/browser proof -> $ui-product-harness
```

## Headless Coverage

Cover applicable decisions in the order exposed by the property; the selected command path may have runtime order, but this table is not a project workflow.

| Decision | Completion criterion |
| --- | --- |
| Ground | Repository authority, existing commands/tests/descriptors, and the production entrypoint are identified. |
| Name | One capability and one observable property determine the command name and result contract. |
| Select | The lowest sufficient surface—boundary, fixture, replay, adapter conformance, projection, real DB, restart/recovery, or real external runtime—is chosen. |
| Drive | The harness enters through the same command/use-case/materialization path as production; dependency reality is explicit. |
| Observe | Failure returns non-zero; stdout follows the machine contract; diagnostics locate the failed boundary. |
| Bound | `observed`, `supports`, `does_not_decide`, `not_proven`, and `claim_ceiling` match the executed surface. |

Select any level directly when the property requires it. Real external paths
remain explicit because credentials, cost, privacy, and irreversible effects
are environment risks.

## Command Contract

Prefer capability names:

```text
pnpm verify order.checkout.retry
just verify-order-checkout-restart
cargo xtask verify order-checkout-replay
```

Progress labels such as `phase-2-done` or generic `smoke-all` are replaced by
the capability and property they actually exercise. One command covers one
bounded slice and emits actionable diagnostics.

```json
{
  "schema_version": 2,
  "harness": "order.checkout.retry",
  "status": "pass",
  "proof_surface": {
    "surface_kind": "headless",
    "dependency_reality": ["fake", "real_local"],
    "environment_class": "local_stack",
    "proof_focus": ["idempotent_retry", "persistence_restart"]
  },
  "claim_ceiling": "one local retry path under declared dependencies",
  "observed": {
    "order_version_before": 7,
    "order_version_after": 8,
    "duplicate_version_after": 8
  },
  "supports": [
    "duplicate retry produced no second committed transition"
  ],
  "does_not_decide": [
    "whether product policy should allow another retry"
  ],
  "not_proven": [
    "multi-process contention",
    "real provider behavior"
  ]
}
```

Use JSONL for observation streams. Keep machine stdout clean and send
human-oriented diagnostics to stderr.

## Dependency Reality

```text
fixture       static deterministic data
fake          deterministic capability implementation
replay        recorded normalized sequence
real_local    actual DB/queue/runtime in local or test environment
real_external credentialed provider/device/runtime
```

## Boundary Checks

High-value checks include:

```text
use-case cannot import live adapter
policy cannot import DB, SDK, or HTTP
HTTP handler cannot write repository directly
cross-module callers use public surface
business modules cannot import wiring surface
fake cannot enter production composition
tooling/harness cannot materialize facts directly
old writer stays fenced during migration
```

Use the isolation required by the claim: a restart claim needs a restart; a
pure policy claim does not need a fresh database.

## Output

```text
capability
formal_entrypoint
command_contract
proof_surface
observed
supports
does_not_decide
not_proven
claim_ceiling
new_or_reused_harness_files
```

## Read When Needed

- Designing commands: [Command Surface](references/command-surface.md)
- Choosing fixture, fake, replay, or real: [Fixture and Replay Ladder](references/fixture-replay-ladder.md)
- Defining output: [Evidence Output](references/evidence-envelope.md)
- Enforcing architecture boundaries: [Boundary Check](references/boundary-check.md)
