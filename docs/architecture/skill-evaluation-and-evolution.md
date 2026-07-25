# Skill Evaluation And Suite Evolution

## Two Meta Capabilities

```text
$skill-evaluation-system
  -> 某个 Skill / Candidate 在指定 Agent Profile、任务和 Harness 下表现如何

$ai-coding-os-evolution
  -> 这些证据是否足以改变 Canonical Suite、兼容边界和版本
```

二者不能合并。前者生成行为证据，后者治理 Suite 变更。

## SkillOpt Assimilation

本 Suite 吸收 SkillOpt 的方法，而不 vendoring 其工程或把 OS 退化为单一 Markdown Prompt optimizer：

```text
rollout -> reflect -> aggregate -> select -> bounded update -> held-out gate
```

同时保留：Checkpoint、rejected proposal buffer、longitudinal comparison、transfer eval、staged adoption 和 rollback。

关键扩展是：

> **Train strategy; govern semantics。**

执行策略、Reference 路由、输出脚手架和上下文可以被实验优化；Product Authority、Fact Authority、Current Home、Evidence Boundary 和 Stop Line 不能被一个平均分自动改写。

## Failure Attribution

失败先归因，再决定修改面：

```text
skill-defect
execution-lapse
routing-defect
retrieval-defect
tool-interface-defect
project-knowledge-gap
semantic-owner-gap
evaluator-defect
model-capability-limit
stochastic-noise
```

只有可归因的真实 Skill defect 才直接进入 Canonical Skill 候选。否则应修 Router、Reference、Tool、项目知识、Evaluator、Harness 或兼容声明。

## Evaluation Ladder

```text
L0 Static Contract
L1 Direct Skill Eval
L2 Routed Composition Eval
L3 Repository Task Eval
L4 Long-horizon Eval
L5 Field / Canary Evidence
```

数据拆分为 Discovery/Train、Selection、Sealed Release Test 与 Transfer/Canary；同一 case family 不跨 Split。Candidate author、optimizer 和 evaluator 的暴露边界必须可追溯。

## Hierarchical Gate

```text
Gate 0 Evaluation Integrity
Gate 1 Mechanical Integrity
Gate 2 Constitutional Invariants
Gate 3 Protected Regression
Gate 4 Behavioral Utility
Gate 5 Efficiency / Context Cost
Gate 6 Transfer
```

Constitutional 或关键 Protected Regression 是 veto，不被平均收益抵消。行为等价但显著减少 Context、输出冗余、错误升级和规则冲突，也可以构成有效改进。

## Capability Epoch

评估对象不是单一模型名，而是：

```text
model + reasoning mode + context loading + tools + harness + memory
+ subagents + permissions + cost/latency envelope + target task classes
```

新模型发布只触发 Capability Probe。Fresh-context review 可以覆盖 clean-room、failure archaeology、first-principles rebuild、capability maximization、adversarial review 和 project simulation，但不固定 Agent 数量或 Workflow。

## Self-evolution Boundary

Suite 可以自主发现问题、形成候选、编写 Evals 和执行对照；不能仅凭候选自己的判断成为 Current Suite。发布需要当前基线、Protected Corpus、held-out Evidence、机械审计、Checkpoint、Rollback 和 Release Authority。

> Recursive, but not circular。
