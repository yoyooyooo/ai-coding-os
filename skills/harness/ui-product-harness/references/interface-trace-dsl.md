# Interface Trace DSL

This is a thin YAML convention for connecting user-facing capabilities to
runnable UI Harness surfaces. It is not a UI generation language, workflow
engine, test implementation, evidence authority, or replacement for project
contracts.

## Ownership

```text
$interface-capability-planning
  owns user intent, entrypoint, interaction, state/data ownership, and coverage intent

$ui-product-harness
  owns UI Harness surface descriptions and local observation shape

$product-harness-system
  owns shared Harness vocabulary, discovery, claim ceilings, and cross-surface trace

$docs-governance
  owns durable project placement, indexing, lifecycle, and cleanup

project authority
  owns product facts, accepted contracts, and the interpretation baseline
```

An explicitly adopted tracker or execution method may reference these IDs. This
DSL does not depend on Goal Proof or any other execution method.

## Goals

- connect interface intent, frontend ownership, Harness surface, and evidence;
- make concrete proof paths discoverable from stable capability IDs;
- support coverage and gap inspection across headless and UI surfaces;
- avoid brittle DOM steps and framework-specific implementation in durable docs.

## Object references

```text
InterfaceCapability  # defined by interface-capability artifacts
InterfaceSurface     # defined by interface-capability artifacts
HarnessDescriptor    # runnable surface discovery record
HarnessResult        # local or durable structured observation
```

Recommended ID prefixes:

```text
ic.<domain>.<action>
surface.<area>.<name>
region.<area>.<name>
uh.<domain>.<scenario>
hp.<domain>.<scenario>
```

## InterfaceCapability reference

Do not define long-lived InterfaceCapability records here. This shape only shows
what Harness records may reference.

```yaml
kind: InterfaceCapability
id: ic.<domain>.<action>
status: sketch | candidate | accepted | regression
intent: ...
authority_refs: {}
surface_refs: []
entrypoint: {}
interaction_contract: {}
state_ownership: {}
data_contract: {}
coverage_intent: {}
forbidden_paths: []
evidence_links: []
```

Use `authority_refs` or an explicit missing-authority note when facts are not yet
grounded.

## InterfaceSurface reference

```yaml
kind: InterfaceSurface
id: surface.<area>.<name>
title: ...
regions:
  - id: region.<area>.<name>
    role: ...
capabilities:
  - ic.<domain>.<action>
```

Surface records are IA/navigation indexes. They do not become product truth or
test code.

## UI Harness Descriptor

Durable project-level descriptors may live under `docs/product-harness/**` or a
repository-selected equivalent. Executable code remains near the feature or
Harness host.

```yaml
schema_version: 1
kind: HarnessDescriptor
id: uh.<domain>.<scenario>
capability: ic.<domain>.<action>
surface: browser
command: pnpm verify <domain>.<scenario>
entrypoint:
  route: /example
uses:
  backend: fake | real-local | real-external
  browser: chromium
can_observe:
  - visible success and error states
  - navigation and reload behavior
  - console and network failures
does_not_cover:
  - backend materialization unless paired with a headless/database Harness
  - production authentication
claim_ceiling: local browser-visible behavior under the declared dependencies
```

## UI Harness Result

```yaml
schema_version: 1
kind: HarnessResult
harness: uh.<domain>.<scenario>
status: pass | fail | blocked | skipped
observed:
  success_affordance_visible: true
  reload_state_consistent: true
  console_errors: []
supports:
  - the declared local browser path remained visible after reload
not_proven:
  - production authentication
  - real-provider behavior
artifacts:
  - type: screenshot
    ref: artifacts/example.png
```

Use `observed`, `supports`, and `not_proven` rather than treating a passing test
label as a complete conclusion. Add commit/runtime provenance only when the
result must survive across Agents, commits, release decisions, or audits.

## Example

```yaml
schema_version: 1
kind: HarnessDescriptor
id: uh.issue-intake.browser
capability: ic.issue-intake.from-channel-message
surface: browser
command: pnpm verify issue-intake.browser
entrypoint:
  route: /channels/demo
uses:
  backend: real-local
  external-provider: fake
can_observe:
  - issue affordance on the source message
  - issue detail navigation
  - visible source-message context
  - reload reconciliation
  - console and network failures
does_not_cover:
  - production authentication
  - real external provider
claim_ceiling: local browser plus real local backend; external provider remains fake
```

## Rules

- Link conclusions to an executed result or mark the surface unproven.
- Record visual details only when they are test-relevant.
- Keep unstable descriptors `candidate`; promote to `regression` only when the
  entrypoint semantics and command are stable.
- Do not duplicate test code, selectors, or transient logs in the DSL.
- Do not use the DSL to invent product objects, API schemas, facts, or writers.
- Do not report browser proof as backend materialization or provider proof.
