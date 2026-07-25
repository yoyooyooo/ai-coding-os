# Decision Calculus

Decision rules belong to their semantic Skill. This Skill composes only the
rules relevant to the current question.

## Rule Contract

```yaml
rule_id: eaa.CAP.001
owner: evolvable-application-architecture
applies_when:
  dependency_crosses: [process, vendor, trust, external-lifecycle]
asks:
  - Can the effect complete after local timeout?
  - Who materializes the accepted local fact?
requires:
  - application-owned capability boundary
forbids:
  - provider SDK types in the authority core
agent_may_decide_when:
  - product semantics and public compatibility are settled
  - the choice is reversible
escalate_when:
  - money, permission, destructive data, or irreversible effects change
probes:
  - timeout-after-start
  - duplicate-delivery
proof_focus:
  - adapter conformance
  - reconciliation after restart
```

Rules expose decision variables and bounds; they do not prescribe a universal
project workflow.

## Local Decision Tree

A tree is generated for one question from applicable rules. It is not the
persistent source of truth.

```text
Does the dependency cross an outer capability boundary?
  no  -> keep private collaboration
  yes -> is replacement/fake/failure isolation real?
           no  -> retain a light seam
           yes -> application-owned port
         can completion occur after timeout?
           yes -> receipt / outcome-unknown / reconciliation
```

## Decision Rights

The Agent normally decides reversible, private, technical choices inside
accepted product semantics and binding constraints. Route decisions when they
change product meaning, authority ownership outside architecture, security or
legal policy, public compatibility, durable data meaning, or destructive and
irreversible behavior.
