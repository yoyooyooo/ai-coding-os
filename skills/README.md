# AI Coding OS Core Skill Suite

当前 Core Suite 面向能够自主判断和验证的 AI Coding Agent。它提供语义 Owner、局部决策接口、可发现 Reference、Proof Surface 与演进机制，而不规定统一阅读、规划、Ticket 或执行 Workflow。

## Core Doctrine

```text
Project Authority First
Question-scoped Ownership
One Scoped Meaning, One Current Home
Source Is Not Decision
No Silent Material Assumption
Evidence Bounds Claims
Route Is an Edge, Not a Sequence
Strong Invariants, Weak Choreography
Minimal Context, Maximal Legibility
Earned Persistence
Preserve Semantics; Re-earn Scaffolding
```

## Skill Groups

```text
architecture/
  architecture-decision-system
  evolvable-application-architecture
  frontend-architecture
  effect-best-practices

capability/
  interface-capability-planning

contracts/
  ai-coding-os-suite-contracts

governance/
  docs-governance

harness/
  product-harness-system
  headless-product-harness
  ui-product-harness
  frontend-test-system

meta/
  skill-evaluation-system
  ai-coding-os-evolution

preset/
  evolvable-application-preset

product/
  product-definition

router/
  ai-coding-os

tooling/
  effect-api-app-kit
```

`$ai-coding-os` 只在意图含混或跨 Owner 时选择最小知识 Owner 集；它不保存项目状态，也不控制执行循环。

## Verification

```bash
python3 tooling/suite_audit.py --suite . --out ../release/suite-audit.json
```

该审计只证明离线源码结构、链接、Schema/Eval 合同、Preset/Kit fixture 和发布 provenance；不证明模型运行质量或生产行为。
