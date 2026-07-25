# Core Doctrine

## Frontend Model

A frontend is not a second backend. It is a system for:

```text
expressing intent
consuming authoritative projections
owning local interaction
coordinating host resources
reconciling optimistic and realtime change
rendering derived views
```

The central path is:

```text
user intent
  -> local proposal / command
  -> backend or local authority accepts or rejects
  -> committed projection becomes observable
  -> frontend reconciles cache, proposal, and interaction state
  -> view model renders
```

## Architectural Roles

Use roles even when a framework uses different folders:

```text
host composition   boot, providers, router/runtime/client wiring, global policy
route adapter       URL/search/loader/action/error/not-found translation
feature capability  product-facing queries, commands, local interaction, view model
shared capability   app-local business-neutral capability with explicit ownership
generated contract  read-only generated DTO/protocol/schema output
reusable package    cross-host or cross-app capability with a public API
```

A common React layout is `app / routes / features / shared / generated`, but the
invariant is dependency direction, not the spelling of directories.

## Dependency Direction

Prefer:

```text
host composition -> route adapters -> feature capabilities
host composition -> feature capabilities
feature capabilities -> shared capabilities / reusable packages / generated contracts
client capability -> wire contract
UI primitives -> design tokens
```

Reject:

```text
low-level capability -> host composition
wire contract -> feature implementation
UI primitive package -> product client or business workflow
package -> app internals
feature -> another feature's private files
transport frame -> component state without decode/reconciliation
```

Cross-feature collaboration is allowed through an explicit public capability or
at a composition layer when the product relationship is real. The rule is “no
private/deep imports and no accidental cycles,” not “features can never relate.”

## Authority

Frontend may authoritatively own:

- drafts and unsent input;
- selection, focus, panels, filters, and navigation state;
- device-local preferences or offline facts when the product explicitly assigns
  that authority;
- resource status such as connecting/reconnecting;
- optimistic proposal metadata.

Frontend usually holds projections, not authority, for:

- durable business completion;
- permissions and audit facts;
- server workflow/issue state;
- multi-user results;
- runtime/provider completion.

Explicitly document exceptions such as local-first applications, offline queues,
or browser-owned documents.

## Boundary Shape

```text
command adapter
  accepts feature intent and returns acceptance/rejection/needs-review metadata

query adapter
  reads a purpose-built projection

realtime adapter
  announces committed projection changes and continuity metadata

mapper / view model
  converts decoded projections + local interaction into render data
```

Keep wire DTOs, provider payloads, event-spine internals, and runtime diagnostics
out of components.

## Evidence

Use the lowest proof that matches the claim:

```text
pure reducer/mapper test
fake client contract test
headless feature test
component/surface test
browser scenario
real backend/realtime scenario
declared local-stack or staging failure/recovery scenario
```

Do not claim browser behavior from a reducer test or realtime continuity from a
single happy-path mock.
