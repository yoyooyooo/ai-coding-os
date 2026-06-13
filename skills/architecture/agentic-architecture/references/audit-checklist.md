# Audit Checklist

Use this checklist to review an existing repository or proposed architecture.

## 1. Classification

Pick the primary mode:

- `new-system`
- `capability-slice`
- `provider-integration`
- `runtime-adapter`
- `memory-system`
- `plugin-boundary`
- `composition-root`
- `harness-readiness`
- `audit`

## 2. Authority

Check:

- every durable fact has one owner;
- caches, indexes, logs, search results, provider output, and runtime events are
  not silent fact sources;
- memory acceptance is separated from memory retrieval;
- permission and visibility decisions have an authority;
- completion and artifact provenance are not owned by the runtime.

## 3. Commands And Projections

Check:

- command paths and projection paths are named separately;
- realtime transports do not become command semantics;
- UI state does not become domain state;
- backfill/replay/reconnect paths join the same materialization lane.

## 4. Ports And Adapters

Check:

- ports are named by capability, not vendor;
- adapter output is candidate/diagnostic/handle/snapshot/projection input;
- provider SDK objects do not leak into core terms;
- fake/replay/real adapters share a narrow contract;
- plugin boundaries do not create plugin-owned facts.

## 5. Composition

Check:

- binaries, servers, workers, daemons, and CLIs only wire dependencies;
- profile differences stay in assembly/config/policy;
- local, cloud, test, replay, and real-runtime paths share one core;
- deployment crates or packages do not import more than their profile needs.

## 6. Agent Freedom

Check:

- agents can explore and propose without being blocked by process ceremony;
- accepted facts still require typed commands or policy-approved materialization;
- tool calls, file writes, runtime requests, and model outputs have allow/deny
  boundaries;
- high-risk changes stop at product truth, security, protocol, private data,
  destructive behavior, or claim ceiling.

## 7. Evidence

Check:

- architecture claims have runnable proof where feasible;
- claim ceiling is explicit;
- positive tokens are stable;
- `not_claimed` and `not_proven` avoid overclaim;
- diagnostics can explain failure, replay, recovery, and redaction.

## 8. Output

Return:

```text
classification:
authority_map:
commands_vs_projections:
ports_and_adapters:
composition_root:
agent_freedom_boundary:
replaceability:
evidence_gate:
fits:
drift:
blockers:
auto_fix_candidates:
domain_skill_handoffs:
human_decisions:
verification:
not_claimed:
```
