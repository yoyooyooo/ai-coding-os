#!/usr/bin/env python3
"""Render and validate the Evolvable Application Preset.

The renderer is intentionally conservative. It produces a candidate project
snapshot and never makes the project dynamically inherit a newer Preset.
"""
from __future__ import annotations

import argparse
import difflib
import json
import shutil
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover
    raise SystemExit("PyYAML is required: pip install pyyaml") from exc

PRESET_ID = "evolvable-application"
PRESET_VERSION = (Path(__file__).resolve().parents[1] / "VERSION").read_text(encoding="utf-8").strip()
MANAGED_BEGIN = "<!-- evolvable-application-preset:begin -->"
MANAGED_END = "<!-- evolvable-application-preset:end -->"


def load_yaml(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"expected YAML object: {path}")
    return data


def dump_yaml(data: Any) -> str:
    return yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=1000)


def profile_root() -> Path:
    return Path(__file__).resolve().parents[1] / "profiles"


def load_profiles(ids: list[str]) -> tuple[list[dict[str, Any]], list[str]]:
    catalog = profile_root()
    known = {p.parent.name for p in catalog.glob("*/profile.yaml")}
    cache: dict[str, dict[str, Any]] = {}
    resolved: list[str] = []
    visiting: set[str] = set()

    def load(profile_id: str) -> dict[str, Any]:
        if profile_id not in cache:
            path = catalog / profile_id / "profile.yaml"
            if not path.is_file():
                raise ValueError(f"unknown profile {profile_id!r}; known={sorted(known)}")
            profile = load_yaml(path)
            if profile.get("id") != profile_id:
                raise ValueError(f"profile id mismatch: requested {profile_id!r}, file declares {profile.get('id')!r}")
            cache[profile_id] = profile
        return cache[profile_id]

    def visit(profile_id: str) -> None:
        if profile_id in resolved:
            return
        if profile_id in visiting:
            raise ValueError(f"profile dependency cycle includes {profile_id!r}")
        visiting.add(profile_id)
        profile = load(profile_id)
        for requirement in profile.get("requires", []) or []:
            if not isinstance(requirement, str) or not requirement:
                raise ValueError(f"profile {profile_id!r} has an invalid requires entry")
            visit(requirement)
        visiting.remove(profile_id)
        resolved.append(profile_id)

    for profile_id in dict.fromkeys(ids):
        if not isinstance(profile_id, str) or not profile_id:
            raise ValueError("profiles must contain non-empty strings")
        visit(profile_id)

    selected = set(resolved)
    conflicts: list[str] = []
    for profile_id in resolved:
        for conflict in load(profile_id).get("conflicts", []) or []:
            if conflict in selected:
                pair = " / ".join(sorted({profile_id, conflict}))
                if pair not in conflicts:
                    conflicts.append(pair)
    if conflicts:
        raise ValueError("conflicting profiles: " + "; ".join(conflicts))
    return [load(profile_id) for profile_id in resolved], resolved


def contract_selection(profile_ids: list[str]) -> dict[str, Any]:
    profiles, _ = load_profiles(profile_ids)
    selected: dict[str, Any] = {
        "term_owners": set(),
        "terms": set(),
        "filename_pattern_owners": set(),
        "guarded_terms": set(),
        "qualifiers": {},
    }
    for profile in profiles:
        contract = profile.get("suite_contract") or {}
        if not isinstance(contract, dict):
            raise ValueError(f"profile {profile['id']!r} suite_contract must be an object")
        for key in ("term_owners", "terms", "filename_pattern_owners", "guarded_terms"):
            values = contract.get(key) or []
            if not isinstance(values, list) or any(not isinstance(value, str) or not value for value in values):
                raise ValueError(f"profile {profile['id']!r} suite_contract.{key} must be an array of strings")
            selected[key].update(values)
        qualifiers = contract.get("qualifiers") or {}
        if not isinstance(qualifiers, dict):
            raise ValueError(f"profile {profile['id']!r} suite_contract.qualifiers must be an object")
        for key, value in qualifiers.items():
            if value is True:
                selected["qualifiers"][key] = True
            elif isinstance(value, list) and all(isinstance(item, str) and item for item in value):
                if selected["qualifiers"].get(key) is not True:
                    current = selected["qualifiers"].setdefault(key, [])
                    current.extend(item for item in value if item not in current)
            else:
                raise ValueError(f"profile {profile['id']!r} suite_contract.qualifiers.{key} must be true or an array of strings")
    return selected


def validate_overlay_shape(overlay: dict[str, Any]) -> None:
    def require_mapping(value: Any, label: str) -> dict[str, Any]:
        if not isinstance(value, dict):
            raise ValueError(f"{label} must be an object")
        return value

    def require_list(value: Any, label: str) -> list[Any]:
        if not isinstance(value, list):
            raise ValueError(f"{label} must be an array")
        return value

    def validate_path_items(key: str) -> None:
        value = overlay.get(key)
        if value is None:
            return
        for index, item in enumerate(require_list(value, key)):
            if isinstance(item, str):
                continue
            obj = require_mapping(item, f"{key}[{index}]")
            if not (obj.get("path") or obj.get("id")):
                raise ValueError(f"{key}[{index}] must contain path or id")

    project = require_mapping(overlay.get("project"), "project")
    if not project.get("id") or not project.get("name"):
        raise ValueError("project.id and project.name are required")
    for key in ("commands", "enforcement"):
        value = overlay.get(key)
        if value is not None:
            obj = require_mapping(value, key)
            if any(not isinstance(item, str) for item in obj.values()):
                raise ValueError(f"{key} values must be strings")
    for key in ("deployables", "packages", "modules", "workflows"):
        validate_path_items(key)
    authorities = overlay.get("authorities")
    if authorities is not None:
        for index, item in enumerate(require_list(authorities, "authorities")):
            obj = require_mapping(item, f"authorities[{index}]")
            if not obj.get("fact"):
                raise ValueError(f"authorities[{index}] must contain fact")
    exceptions = overlay.get("exceptions")
    if exceptions is not None:
        for index, item in enumerate(require_list(exceptions, "exceptions")):
            obj = require_mapping(item, f"exceptions[{index}]")
            if not obj.get("id") or not obj.get("adr"):
                raise ValueError(f"exceptions[{index}] must contain id and adr")
    terms = overlay.get("domain_terms")
    if terms is not None:
        terms = require_mapping(terms, "domain_terms")
        for token, info in terms.items():
            if not isinstance(token, str) or not token:
                raise ValueError("domain_terms keys must be non-empty strings")
            if not isinstance(info, (str, dict)):
                raise ValueError(f"domain_terms.{token} must be a string or object")
    for key in ("topology_notes",):
        value = overlay.get(key)
        if value is not None and any(not isinstance(item, str) for item in require_list(value, key)):
            raise ValueError(f"{key} entries must be strings")
    for key in ("implementation_qualifiers", "deprecated_terms"):
        value = overlay.get(key)
        if value is not None:
            require_mapping(value, key)
    coverage = overlay.get("harness_coverage")
    if coverage is not None:
        for index, item in enumerate(require_list(coverage, "harness_coverage")):
            require_mapping(item, f"harness_coverage[{index}]")


def resolve_profile_selection(requested: list[str]) -> dict[str, list[str]]:
    requested_ids = list(dict.fromkeys(requested))
    defaults_added = [] if "agent-entry" in requested_ids else ["agent-entry"]
    _, resolved_ids = load_profiles([*defaults_added, *requested_ids])
    dependency_added = [
        profile_id
        for profile_id in resolved_ids
        if profile_id not in requested_ids and profile_id not in defaults_added
    ]
    return {
        "requested": requested_ids,
        "defaults_added": defaults_added,
        "dependency_added": dependency_added,
        "resolved": resolved_ids,
    }


def validate_inputs(preset_input: dict[str, Any], overlay: dict[str, Any]) -> tuple[dict[str, list[str]], dict[str, Any]]:
    if preset_input.get("schema_version") != 1:
        raise ValueError("preset-input schema_version must be 1")
    ids = preset_input.get("profiles")
    if not isinstance(ids, list) or not ids:
        raise ValueError("profiles must be a non-empty list")
    if any(not isinstance(profile_id, str) or not profile_id for profile_id in ids):
        raise ValueError("profiles must contain non-empty strings")
    if overlay.get("schema_version") != 1:
        raise ValueError("project-overlay schema_version must be 1")
    validate_overlay_shape(overlay)
    return resolve_profile_selection(ids), overlay["project"]


def is_zh(overlay: dict[str, Any]) -> bool:
    return str((overlay.get("project") or {}).get("narrative_language", "")).lower().startswith("zh")


def command_lines(commands: dict[str, Any], zh: bool) -> str:
    labels = {
        "install": "安装" if zh else "Install",
        "typecheck": "类型检查" if zh else "Typecheck",
        "test": "测试" if zh else "Tests",
        "architecture_check": "架构检查" if zh else "Architecture checks",
        "verify_affected": "受影响验证" if zh else "Affected verification",
        "verify": "完整验证" if zh else "Full verification",
    }
    lines = []
    for key in labels:
        value = commands.get(key)
        if value:
            lines.append(f"- {labels[key]}: `{value}`")
    if not lines:
        lines.append("- " + ("尚未建立；请从仓库脚本解析后补充。" if zh else "Not established; resolve from repository scripts."))
    return "\n".join(lines)


def managed_rule_lines(profile_ids: list[str], zh: bool) -> str:
    selected = set(profile_ids)
    rules = [
        "采纳后复用项目 vocabulary 中的 canonical terms。" if zh else "After adoption, reuse canonical terms from the project vocabulary.",
        "只有当前事实、标准、合同、决策或拓扑变化时才更新持久文档。" if zh else "Update durable docs only when current truth, rules, contracts, decisions, or topology change.",
    ]
    if "monorepo-core" in selected:
        rules.extend([
            "遵守 module public / host wiring 边界与事实 writer 约束。" if zh else "Respect module public/host-wiring boundaries and fact-writer constraints.",
            "测试、Adapter、Worker、前端状态或直接持久化不能创造第二条 accepted-fact 写入路径。" if zh else "Tests, adapters, workers, frontend state, and direct persistence do not create another accepted-fact writer.",
        ])
    if "react" in selected:
        rules.append("远端投影只有一个 owner；本地 store 不镜像 server truth。" if zh else "Remote projection has one owner; local stores do not mirror server truth.")
    if "effect" in selected:
        rules.append("Effect API 与运行时规则服从已安装 major 和声明文件。" if zh else "Effect API and runtime rules follow the installed major and declarations.")
    if "verification-core" in selected:
        rules.extend([
            "优先复用现有 Harness；缺失时补最薄、可证伪的执行面。" if zh else "Prefer existing Harnesses; add the thinnest falsifiable surface when needed.",
            "区分 Proof Surface、依赖真实性、实际观察、支持结论与未证明项。" if zh else "Separate Proof Surface, dependency reality, observations, supported conclusions, and unproven neighbors.",
        ])
    return "\n".join(f"- {rule}" for rule in rules)


def managed_agents_section(overlay: dict[str, Any], profile_ids: list[str]) -> str:
    zh = is_zh(overlay)
    project = overlay["project"]
    commands = overlay.get("commands") or {}
    if zh:
        language = "持久叙事文档使用中文；路径、命令、Schema 字段、协议名和代码符号保留 canonical 形式。"
        text = f"""{MANAGED_BEGIN}
本节来自 Evolvable Application Preset 候选快照，尚未成为项目 Authority。

Preset 与 Skill 默认值不能覆盖项目 authority；当前事实、规则、决策和实现证据按其 claim 类型读取。只有经对应 semantic owner 显式采纳的内容才进入项目 Current Home。

## Knowledge Surfaces

- `docs/README.md`（存在时）索引项目 Authority 网络。
- 当前问题、code area、artifact、owning layer 和直接 Evidence 都可以作为入口。
- app/package/module README 或局部 `AGENTS.md` 只声明真实 local delta。
- Portable Skill 输出路径是候选默认值；现有项目 Current Home 优先。

## Candidate Working Rules

{managed_rule_lines(profile_ids, True)}

## Commands

{command_lines(commands, True)}

## Skill Routing

当 AI Coding OS Skill Suite 可用时，跨域或不明确任务可按需使用 `$ai-coding-os`；明确任务可直接使用专业 Skill。Skill 建议不能覆盖仓库内当前权威。

## Language

{language}

Preset profiles: {', '.join(profile_ids)}
Project: {project['name']} (`{project['id']}`)
{MANAGED_END}"""
    else:
        language = "Use the repository narrative language for durable prose; preserve canonical paths, commands, schema fields, protocol names, and code symbols."
        text = f"""{MANAGED_BEGIN}
This section comes from an Evolvable Application Preset candidate snapshot and is not yet project Authority.

Preset and Skill defaults cannot override project authority; resolve current facts, rules, decisions, and implementation evidence by claim type. Only content explicitly adopted by the applicable semantic owner enters a project Current Home.

## Knowledge Surfaces

- `docs/README.md`, when present, indexes the project Authority network.
- The current question, code area, artifact, owning layer, or direct Evidence may be an entry.
- App/package/module READMEs and local `AGENTS.md` describe only real local deltas.
- Portable Skill output paths are candidate defaults; existing project Current Homes win.

## Candidate Working Rules

{managed_rule_lines(profile_ids, False)}

## Commands

{command_lines(commands, False)}

## Skill Routing

Ambiguous or cross-cutting work may use `$ai-coding-os` when useful and the Suite is available. Clear tasks may use the owning specialist directly. Skill guidance never overrides repository-local authority.

## Language

{language}

Preset profiles: {', '.join(profile_ids)}
Project: {project['name']} (`{project['id']}`)
{MANAGED_END}"""
    return text


def merge_agents(existing: str | None, managed: str, zh: bool) -> str:
    if not existing:
        title = "# Repository Agent Guide" if not zh else "# Repository Agent Guide"
        local = "## Repository-Specific Notes\n\n- Add local commands, restricted paths, generated paths, security constraints, and deliberate deviations here."
        if zh:
            local = "## Repository-Specific Notes\n\n- 在这里补充本仓库特有命令、受限路径、生成路径、安全约束与有意偏差。"
        return f"{title}\n\n{managed}\n\n{local}\n"
    begin_count = existing.count(MANAGED_BEGIN)
    end_count = existing.count(MANAGED_END)
    if begin_count != end_count or begin_count > 1:
        raise ValueError("Preset managed AGENTS.md markers are unbalanced or repeated; inspect the diff before adoption")
    if begin_count == 1:
        before, rest = existing.split(MANAGED_BEGIN, 1)
        _, after = rest.split(MANAGED_END, 1)
        return before.rstrip() + "\n\n" + managed + "\n\n" + after.lstrip()
    return existing.rstrip() + "\n\n" + managed + "\n"


def layer_readme(title: str, owns: list[str], not_owns: list[str], reads: list[str], zh: bool) -> str:
    links = chr(10).join(f"- [{item}]({item})" for item in reads)
    is_router = title == "Documentation Router"
    if zh:
        reading_heading = "## Discovery Surfaces" if is_router else "## Routes"
        return f"""# {title}

> Preset 候选快照：本文件尚未成为项目 Authority，只有 semantic owner 显式采纳的内容才进入 Current Home。

## Proposed Ownership

{chr(10).join('- ' + x for x in owns)}

## Must Not Own

{chr(10).join('- ' + x for x in not_owns)}

## Boundary / Conflict

仓库当前权威优先；候选层只建议上面列出的语义。与项目 Current Home 重复时，不得形成平行 Authority。

## Promotion / Demotion

候选内容只有在对应 semantic owner 明确采用后才能进入 Current Home；源码或合同存在本身不足以完成晋升。

## Internal Shape

本层候选默认保持扁平。只有在 durable ownership、安全、保留、生命周期、读者路由或重复导航压力成立后才建议子目录。

{reading_heading}

{links}
"""
    reading_heading = "## Discovery Surfaces" if is_router else "## Routes"
    return f"""# {title}

> Preset candidate snapshot: this file is not project Authority until the applicable semantic owner explicitly adopts it into a Current Home.

## Proposed Ownership

{chr(10).join('- ' + x for x in owns)}

## Must Not Own

{chr(10).join('- ' + x for x in not_owns)}

## Boundary / Conflict

Repository current authority wins. The candidate layer proposes only the semantics listed above and must not create a parallel Authority.

## Promotion / Demotion

Candidates enter a Current Home only after adoption by the applicable semantic owner; source or contract existence alone is insufficient.

## Internal Shape

The candidate stays flat by default. Suggest child partitions only after durable ownership, security, retention, lifecycle, reader-routing, or repeated navigation pressure is established.

{reading_heading}

{links}
"""


def render_architecture_profile(overlay: dict[str, Any], resolution: dict[str, list[str]]) -> str:
    profiles = resolution["resolved"]
    project = overlay["project"]
    selected = set(profiles)
    decisions: dict[str, Any] = {}
    if "monorepo-core" in selected:
        decisions.update({
            "repository_mode": project.get("repository_mode", "monorepo"),
            "backend_module_style": "private-capability-module-first",
            "source_layout": "bounded-semantic-flat",
            "docs_shape": "earned-semantic-layers",
            "package_promotion": "pressure-driven",
            "deployable_promotion": "pressure-driven",
        })
    if "react" in selected:
        decisions["frontend_projection_ownership"] = "single-owner-reconciliation"
    if "effect" in selected:
        decisions["effect_runtime_ownership"] = "per-host"
    if "verification-core" in selected:
        decisions["proof_contract"] = "orthogonal-proof-surface-v2"
    commands = overlay.get("commands") or {}
    configured_enforcement = overlay.get("enforcement") or {}
    default_enforcement: dict[str, Any] = {}
    if "typescript-node" in selected:
        default_enforcement["architecture_check"] = configured_enforcement.get("architecture_check", commands.get("architecture_check"))
    if "verification-core" in selected:
        default_enforcement["verify_affected"] = configured_enforcement.get("verify_affected", commands.get("verify_affected"))
    data = {
        "schema_version": 1,
        "preset": {"id": PRESET_ID, "version": PRESET_VERSION, "mode": "candidate-snapshot"},
        "profiles": list(profiles),
        "profile_resolution": {key: list(values) for key, values in resolution.items()},
        "decisions": decisions,
        "resolved_standards": {
            "source_topology": "./source-topology-and-naming.md",
            "vocabulary": "./naming-vocabulary.yaml",
            "verification_policy": "./verification-policy.md" if "verification-core" in selected else None,
        },
        "enforcement": default_enforcement,
        "exceptions": overlay.get("exceptions") or [],
    }
    # Remove nulls without hiding explicitly empty structures.
    data["resolved_standards"] = {k: v for k, v in data["resolved_standards"].items() if v}
    data["enforcement"] = {k: v for k, v in data["enforcement"].items() if v}
    return dump_yaml(data)


def render_source_standard(overlay: dict[str, Any], profiles: list[str]) -> str:
    zh = is_zh(overlay)
    deployables = overlay.get("deployables") or []
    packages = overlay.get("packages") or []
    apps_text = ", ".join(item.get("path", str(item)) if isinstance(item, dict) else str(item) for item in deployables) or "not-yet-established"
    pkg_text = ", ".join(item.get("path", str(item)) if isinstance(item, dict) else str(item) for item in packages) or "not-yet-established"
    selection = contract_selection(profiles)
    owners = set(selection["term_owners"]) | set(selection["filename_pattern_owners"])
    snapshot = Path(__file__).resolve().parents[1] / "references/suite-contract-snapshot"
    pattern_contract = load_yaml(snapshot / "filename-patterns.yaml")
    selected_patterns = [
        item["pattern"]
        for item in pattern_contract.get("patterns", [])
        if item.get("owner") in selection["filename_pattern_owners"]
    ]
    if not owners and "monorepo-core" not in profiles:
        note = "当前 profiles 未采用源码命名合同。" if zh else "The selected profiles adopt no source naming contract."
        return f"# Source Topology and Naming\n\n{note}\n\n## Profiles\n\n" + "\n".join(f"- `{item}`" for item in profiles) + "\n"
    pattern_text = "\n".join(selected_patterns) or "not-yet-established"
    topology_zh = []
    topology_en = []
    boundaries_zh = []
    boundaries_en = []
    if "monorepo-core" in profiles:
        topology_zh.extend([
            "- capability module 默认保持私有，跨边界只暴露明确 public surface。",
            "- host composition 与普通业务调用分离。",
            "- package 不得 import app internals。",
        ])
        topology_en.extend([
            "- Capability modules stay private by default and expose explicit public surfaces across boundaries.",
            "- Host composition stays separate from ordinary business calls.",
            "- Packages do not import app internals.",
        ])
    if "evolvable-application-architecture" in owners:
        topology_zh.append("- TypeScript 跨 module 普通调用使用 `<subject>.public.ts`；host composition 可使用 `<subject>.wiring.ts`。")
        topology_en.append("- TypeScript cross-module business calls use `<subject>.public.ts`; host composition may use `<subject>.wiring.ts`.")
        boundaries_zh.extend([
            "- `*.policy.ts` 不依赖 HTTP、DB、SDK 或 live adapter。",
            "- `*.use-case.ts` 不依赖 `*.live.ts` 或 transport handler。",
            "- `*.port.ts` 不泄露 provider SDK / ORM 类型。",
            "- `*.http.*.ts` 只 decode/map/call use case，不直接写数据库。",
            "- 普通业务 module 不 import `*.wiring.ts`。",
        ])
        boundaries_en.extend([
            "- `*.policy.ts` does not depend on HTTP, DB, SDK, or live adapters.",
            "- `*.use-case.ts` does not depend on `*.live.ts` or transport handlers.",
            "- `*.port.ts` does not expose provider SDK/ORM types.",
            "- `*.http.*.ts` decodes/maps/calls use cases and does not write persistence directly.",
            "- Business modules do not import `*.wiring.ts`.",
        ])
    if "effect-best-practices" in owners:
        topology_zh.append("- Effect 使用不自动创建 package；API 与 runtime 规则服从已安装 major。")
        topology_en.append("- Effect usage does not create a package; API/runtime rules follow the installed major.")
        boundaries_zh.append("- `*.fake.ts` 不能无提示进入 production composition。")
        boundaries_en.append("- `*.fake.ts` is never a silent production fallback.")
    if "frontend-architecture" in owners:
        boundaries_zh.append("- 本地 store 不镜像 remote projection；host root 组装 live client 与资源。")
        boundaries_en.append("- Local stores do not mirror remote projection; host roots assemble live clients and resources.")
    if "product-harness-system" in owners:
        boundaries_zh.append("- Harness 不得绕过正式 use-case/materialization path。")
        boundaries_en.append("- Harnesses do not bypass the formal materialization path.")
    topology_zh_text = "\n".join(topology_zh)
    topology_en_text = "\n".join(topology_en)
    boundaries_zh_text = "\n".join(boundaries_zh) or "- 当前 profiles 未采用额外 import boundary。"
    boundaries_en_text = "\n".join(boundaries_en) or "- The selected profiles adopt no additional import boundary."
    promotion_zh = "每次晋升都需要真实压力；目录或 package 本身不授予事实写入权。" if "monorepo-core" in profiles else "当前 profiles 未采用 promotion ladder。"
    promotion_en = "Each promotion needs real pressure; a directory or package does not grant fact-writing authority." if "monorepo-core" in profiles else "The selected profiles adopt no promotion ladder."
    if zh:
        return f"""# Source Topology and Naming

本文件是 Preset 生成的候选 standard，不是当前项目 Authority。只有对应 owner 审阅并合入 Current Home 后才生效。

## Repository Topology

- Repository mode: `{overlay['project'].get('repository_mode', 'monorepo')}`
- Deployable hosts: {apps_text}
- Workspace packages: {pkg_text}
{topology_zh_text}

## Source Topology: Bounded Semantic Flatness

```text
目录表达 durable ownership
文件名表达 local subject / responsibility / implementation / proof role
package 表达 compile/import boundary
app 表达 runnable/deployable lifecycle
```

文件名语法：

```text
<subject>[.<facet>...].<responsibility>[.<qualifier>...].<extension>
```

一个 segment 内使用 kebab-case；不同语义维度使用点号。按“产品语义 -> 局部能力/操作 -> 架构职责 -> 实现细节”排序。

重复点号前缀只是 lexical cluster，不是 module/package/authority。只有独立 owner、依赖规则、资源生命周期、替换/迁移、编译或部署压力出现时才晋升。

## Documentation Shape

项目 `docs/**` 的 layer、partition 与 identity 由 `$docs-governance` 负责。Preset 输出可以提供 broad candidate，但不是每个项目都必须采用的目录树；未使用的 layer 可以省略，layer 默认保持扁平，二级目录只有在 durable ownership、安全、保留、生命周期、读者路由或重复导航压力成立后才建立。Preset 不自动创建 `node_id`、编号体系或未来影子 authority。

## Canonical Patterns

```text
{pattern_text}
```

不机械生成完整后缀套装。框架保留文件名可以例外，但 adapter 应保持薄。

## Import Boundaries

{boundaries_zh_text}

## Promotion Ladder

```text
lexical cluster -> private submodule -> workspace package -> deployable process
```

{promotion_zh}

## Profiles

{chr(10).join('- `' + x + '`' for x in profiles)}
"""
    return f"""# Source Topology and Naming

This is a Preset-generated candidate standard, not current project Authority. It takes effect only after the applicable owner reviews and merges it into the project Current Home.

## Repository Topology

- Repository mode: `{overlay['project'].get('repository_mode', 'monorepo')}`
- Deployable hosts: {apps_text}
- Workspace packages: {pkg_text}
{topology_en_text}

## Source Topology: Bounded Semantic Flatness

Directories express durable ownership; filenames express local subject, responsibility, implementation, and proof role; packages enforce compile/import boundaries; apps run.

Use `<subject>[.<facet>...].<responsibility>[.<qualifier>...].<extension>` with kebab-case inside a segment and dots between dimensions. A repeated prefix is a lexical cluster, not a module/package/authority.

## Documentation Shape

The project's `docs/**` layer, partition, and identity decisions belong to `$docs-governance`. A Preset render is a broad candidate snapshot, not a mandatory docs tree: unused layers may be omitted, layers stay flat by default, and child partitions require durable ownership, security, retention, lifecycle, reader-routing, or repeated navigation pressure. The Preset does not automatically create `node_id`, numbering schemes, or future shadow authority.

## Canonical Patterns

```text
{pattern_text}
```

Do not mechanically generate a complete suffix set. Framework-reserved filenames
may be exceptions, but adapters should remain thin.

## Import Boundaries

{boundaries_en_text}

## Promotion Ladder

`lexical cluster -> private submodule -> workspace package -> deployable process`

{promotion_en}

## Profiles

{chr(10).join('- `' + x + '`' for x in profiles)}
"""


def render_vocabulary(overlay: dict[str, Any], profiles: list[str]) -> str:
    preset_root = Path(__file__).resolve().parents[1]
    snapshot = preset_root / "references/suite-contract-snapshot"
    vocabulary = load_yaml(snapshot / "semantic-vocabulary.yaml")
    patterns = load_yaml(snapshot / "filename-patterns.yaml")
    guarded = load_yaml(snapshot / "guarded-terms.yaml")
    selection = contract_selection(profiles)
    selected_terms = {
        token: spec
        for token, spec in (vocabulary.get("terms") or {}).items()
        if spec.get("owner") in selection["term_owners"] or token in selection["terms"]
    }
    selected_patterns = [
        item
        for item in (patterns.get("patterns") or [])
        if item.get("owner") in selection["filename_pattern_owners"]
    ]
    selected_guarded = {
        token: spec
        for token, spec in (guarded.get("terms") or {}).items()
        if token in selection["guarded_terms"]
    }
    selected_qualifiers: dict[str, Any] = {}
    for key, selector in selection["qualifiers"].items():
        canonical = (vocabulary.get("qualifiers") or {}).get(key)
        if selector is True:
            selected_qualifiers[key] = canonical
        elif isinstance(canonical, list):
            selected_qualifiers[key] = [item for item in canonical if item in selector]
    domain_terms = overlay.get("domain_terms") or {}
    project_terms: dict[str, Any] = {}
    for token, info in domain_terms.items():
        if not isinstance(info, dict):
            info = {"meaning": str(info)}
        project_terms[token] = {
            "status": info.get("status", "canonical"),
            "product_term": info.get("product_term", token),
            "source_token": info.get("source_token", token),
            "kind": info.get("kind", "product-term"),
            "meaning_ref": "../ssot/product-language.md",
            "aliases": info.get("aliases", {}),
        }
    data = {
        "schema_version": 1,
        "preset_snapshot": {
            "id": PRESET_ID,
            "version": PRESET_VERSION,
            "profiles": profiles,
            "note": "Candidate owner-declared source-naming copy. Project Standards and SSoT own meaning only after explicit adoption; Suite files remain provenance, not dynamic inheritance.",
        },
        "contract_selection": {
            "term_owners": sorted(selection["term_owners"]),
            "extra_terms": sorted(selection["terms"]),
            "filename_pattern_owners": sorted(selection["filename_pattern_owners"]),
            "guarded_terms": sorted(selection["guarded_terms"]),
            "qualifiers": selection["qualifiers"],
        },
        "syntax": vocabulary.get("syntax") or {},
        "canonical_terms": selected_terms,
        "canonical_qualifiers": selected_qualifiers,
        "filename_patterns": selected_patterns,
        "directory_admission": (patterns.get("directory_admission") or []) if "monorepo-core" in profiles else [],
        "promotion_ladder": (patterns.get("promotion_ladder") or []) if "monorepo-core" in profiles else [],
        "guarded_terms": selected_guarded,
        "project_terms": project_terms,
        "implementation_qualifiers": overlay.get("implementation_qualifiers") or {},
        "deprecated_terms": overlay.get("deprecated_terms") or {},
    }
    return dump_yaml(data)


def render_product_language(overlay: dict[str, Any]) -> str:
    zh = is_zh(overlay)
    terms = overlay.get("domain_terms") or {}
    if zh:
        lines = ["# Product Language Candidate", "", "本文件是产品 canonical terms 的候选输入，不是项目 SSoT；产品 owner 采纳后才拥有当前词义。", "", "| Canonical term | Meaning | Kind | Not the same as |", "| --- | --- | --- | --- |"]
    else:
        lines = ["# Product Language Candidate", "", "This file is candidate input for canonical product terms, not project SSoT; product ownership adopts current meaning.", "", "| Canonical term | Meaning | Kind | Not the same as |", "| --- | --- | --- | --- |"]
    if not terms:
        lines.append("| not-yet-established | - | - | - |")
    else:
        for token, info in terms.items():
            if not isinstance(info, dict): info = {"meaning": str(info)}
            name = info.get("product_term", token)
            meaning = str(info.get("meaning", "not-yet-established")).replace("|", "\\|")
            kind = info.get("kind", "product-term")
            not_same = ", ".join(info.get("not_the_same_as", []) or []) or "-"
            lines.append(f"| {name} | {meaning} | {kind} | {not_same} |")
    return "\n".join(lines) + "\n"


def render_fact_authority_map(overlay: dict[str, Any]) -> str:
    zh = is_zh(overlay)
    authorities = overlay.get("authorities") or []
    intro = "本文件是技术 fact writer 与 consistency boundary 的架构候选，不是全局 Authority Map；架构 owner 采纳前不得视为当前规则。" if zh else "This is an architecture candidate for technical fact writers and consistency boundaries, not a global Authority Map; it is not current until adopted by the architecture owner."
    lines = ["# Fact Authority Map Candidate", "", intro, "", "| Fact | Authority module | Writer host | Allowed entry | Forbidden path | Transaction / consistency |", "| --- | --- | --- | --- | --- | --- |"]
    if not authorities:
        lines.append("| not-yet-established | - | - | - | - | - |")
    else:
        for item in authorities:
            lines.append("| {fact} | {authority_module} | {writer_host} | {allowed_entry} | {forbidden_path} | {transaction} |".format(
                fact=item.get("fact", "-"), authority_module=item.get("authority_module", "-"), writer_host=item.get("writer_host", "-"), allowed_entry=item.get("allowed_entry", "-"), forbidden_path=item.get("forbidden_path", "-"), transaction=item.get("transaction", item.get("consistency", "-"))))
    return "\n".join(lines) + "\n"


def render_topology(overlay: dict[str, Any]) -> str:
    zh = is_zh(overlay)
    intro = "本文件是基于 overlay 的拓扑候选；架构 owner 采纳前不证明当前实际拓扑，也不重新定义标准。" if zh else "This is an overlay-derived topology candidate; it does not prove current topology or redefine standards before architecture adoption."
    lines = ["# Repository Topology Candidate", "", intro, ""]
    for title, key in (("Deployables", "deployables"), ("Packages", "packages"), ("Authority Modules", "modules"), ("Workflows", "workflows")):
        lines.append(f"## {title}")
        items = overlay.get(key) or []
        if not items:
            lines.append("\n- not-yet-established\n")
            continue
        lines.append("")
        for item in items:
            if isinstance(item, str):
                lines.append(f"- `{item}`")
            else:
                path = item.get("path", item.get("id", "unknown"))
                desc = item.get("description", item.get("role", ""))
                lines.append(f"- `{path}` — {desc}" if desc else f"- `{path}`")
        lines.append("")
    lines.extend(["## Boundary Notes", ""])
    notes = overlay.get("topology_notes") or []
    lines.extend([f"- {n}" for n in notes] or ["- not-yet-established"])
    return "\n".join(lines) + "\n"


def render_verification_policy(overlay: dict[str, Any]) -> str:
    zh = is_zh(overlay)
    if zh:
        return """# Verification Policy Candidate

> Preset 候选：verification owner 采纳前不构成当前项目规则。

## Proposed Ownership

- 可发现的 Harness command/descriptor 约定。
- `surface_kind` 与 `dependency_reality` 的正交标识；纯静态证明使用 `[none]`。
- 必要时记录 `environment_class`、`proof_focus` 和 `claim_ceiling`。
- 结构化结果中的 `observed`、`supports`、`not_proven`。

## Must Not Own

- 产品事实或第二套业务算法。
- Agent 的固定修复循环、重试次数或模型角色。
- 原始运行日志的长期文档副本。

## Commands

项目命令以 `AGENTS.md` 和 `package.json` 为准。推荐提供 `verify:list`、`verify:affected` 与 `verify` 等可发现入口，但不要求统一工具。

## Claim Boundary

Harness 只支持实际 Proof Surface 对应的结论。Browser 不表示真实后端；fixture/fake/replay/local/external 依赖必须独立声明。
"""
    return """# Verification Policy Candidate

> Preset candidate: this is not a current project rule before adoption by the verification owner.

## Proposed Ownership

- Discoverable Harness command/descriptor conventions.
- Orthogonal `surface_kind` and `dependency_reality` labels; pure static proof uses `[none]`.
- `environment_class`, `proof_focus`, and `claim_ceiling` when material.
- Structured `observed`, `supports`, and `not_proven` output.

## Must Not Own

- Product truth or a second business algorithm.
- Fixed Agent repair loops, retry counts, or model roles.
- Durable copies of every raw run log.

## Commands

Repository commands in `AGENTS.md` and package scripts are authoritative. Prefer discoverable `verify:list`, `verify:affected`, and `verify` entries when useful, without mandating one tool.

## Claim Boundary

Harness conclusions match the exercised Proof Surface. Browser does not imply a real backend; fixture/fake/replay/local/external dependencies remain independently explicit.
"""


def render_harness_readme(zh: bool) -> str:
    return layer_readme(
        "Product Harness",
        ["稳定 Harness descriptor/scenario 引用、coverage 与 lifecycle" if zh else "stable Harness descriptor/scenario references, coverage, and lifecycle"],
        ["产品事实、可执行测试源码、原始日志或执行方法进度" if zh else "product truth, executable test source, raw logs, or execution-method progress"],
        ["coverage.yaml", "../standards/verification-policy.md"], zh,
    )


def render_adoption_adr(overlay: dict[str, Any], profiles: list[str]) -> str:
    zh = is_zh(overlay)
    proposal_date = str(overlay.get("adoption_date") or "not-yet-established")
    if zh:
        return f"""# ADR-0001: Proposed Evolvable Application Preset Adoption

- Status: proposed
- Date: {proposal_date}

## Context

本候选解析所选 profiles 的最小默认值，供项目 semantic owners 审阅；未选择领域不进入候选快照。

## Proposed Decision

建议采用 Evolvable Application Preset `{PRESET_VERSION}`，profiles：{', '.join(profiles)}。
Renderer 只生成 `candidate-snapshot`；各内容只有在对应 owner 审阅并合入 Current Home 后才成为项目 Authority。

## Consequences If Adopted

- 通用规则不需要每个项目重新讨论。
- 项目仍拥有产品语言、fact authority、实际拓扑与例外。
- source naming 只引用项目 SSoT 的产品词义，不复制第二份定义。
- Preset 升级必须显式比较并采纳，不能动态覆盖当前标准。
- docs layer 可按项目需要省略；二级目录和 identity 字段必须经过 `$docs-governance` 的 earned-shape 判断。
"""
    return f"""# ADR-0001: Proposed Evolvable Application Preset Adoption

- Status: proposed
- Date: {proposal_date}

## Context

This candidate resolves the minimum defaults from the selected profiles for review by project semantic owners; unselected domains do not enter the candidate snapshot.

## Proposed Decision

Propose adopting Evolvable Application Preset `{PRESET_VERSION}` with profiles: {', '.join(profiles)}. The renderer emits only a `candidate-snapshot`; content becomes project Authority only after its owner reviews and merges it into a Current Home.

## Consequences If Adopted

- Cross-project defaults are not re-designed for every repository.
- The project still owns product language, fact authority, actual topology, and exceptions.
- Source naming references product meaning in project SSoT instead of copying a second definition.
- Preset upgrades require explicit comparison and adoption.
- Docs layers may be omitted when unused; child partitions and identity fields require an earned-shape decision from `$docs-governance`.
"""


def architecture_checker_template() -> str:
    # Deliberately conservative review/check script. It protects durable edges
    # without pretending to parse TypeScript perfectly.
    return r'''#!/usr/bin/env python3
"""Lightweight project architecture checks generated by the Preset."""
from __future__ import annotations
import argparse, json, re
from pathlib import Path

SKIP = {"node_modules", ".git", "dist", "build", ".next", "coverage", ".turbo"}
GUARDED_BASENAMES = {"utils.ts", "helpers.ts", "common.ts", "service.ts", "manager.ts", "handler.ts", "handlers.ts", "types.ts"}
IMPORT_RE = re.compile(r"(?:from\s+|import\s*\()\s*[\"']([^\"']+)[\"']")

def files(root: Path):
    for p in root.rglob("*"):
        if any(part in SKIP for part in p.relative_to(root).parts):
            continue
        if p.suffix in {".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs"} and p.is_file():
            yield p

def scan(root: Path):
    findings=[]
    for p in files(root):
        rel=p.relative_to(root).as_posix()
        text=p.read_text(encoding="utf-8", errors="ignore")
        if p.name in GUARDED_BASENAMES:
            findings.append({"severity":"warn","rule":"guarded-filename","path":rel,"message":"use a subject-qualified responsibility when possible"})
        imports=IMPORT_RE.findall(text)
        if ".use-case." in p.name and any(".live" in i for i in imports):
            findings.append({"severity":"error","rule":"use-case-imports-live","path":rel,"message":"use case must depend on a port, not a live implementation"})
        if ".policy." in p.name and any(token in i.lower() for i in imports for token in ("http", "pg", "prisma", "stripe", "sdk")):
            findings.append({"severity":"error","rule":"policy-imports-platform","path":rel,"message":"policy should remain pure or explicitly contextual"})
        if "/modules/" in "/"+rel and ".wiring" in " ".join(imports) and "/host/" not in "/"+rel:
            findings.append({"severity":"error","rule":"business-imports-wiring","path":rel,"message":"ordinary business modules should use public surfaces"})
        semantic = p.name
        for suffix in (".integration.test.ts", ".contract.test.ts", ".recovery.test.ts", ".test.ts", ".tsx", ".ts"):
            if semantic.endswith(suffix):
                semantic=semantic[:-len(suffix)]
                break
        if semantic.count(".")+1 > 5:
            findings.append({"severity":"warn","rule":"long-semantic-name","path":rel,"message":"review whether the name is compensating for a missing sub-boundary"})
    return findings

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--repo", default="."); args=ap.parse_args()
    root=Path(args.repo).resolve(); findings=scan(root)
    summary={"error":sum(x["severity"]=="error" for x in findings),"warn":sum(x["severity"]=="warn" for x in findings),"total":len(findings)}
    print(json.dumps({"summary":summary,"findings":findings}, indent=2))
    if summary["error"]: raise SystemExit(1)
if __name__ == "__main__": main()
'''



def render_exception_adr(exception: dict[str, Any], zh: bool, default_date: str) -> str:
    identifier = exception.get("id", "repository-exception")
    scope = exception.get("scope", "not-yet-established")
    reason = exception.get("reason", "not-yet-established")
    date = str(exception.get("date") or default_date)
    if zh:
        return f"""# ADR: {identifier}

- Status: proposed
- Date: {date}

## Context

`{scope}` 可能需要偏离通用 Preset 默认。

## Proposed Decision

建议在该 scope 内采用例外：{reason}

## Consequences If Adopted

- 例外只适用于声明的 scope。
- 非框架/工具强制代码仍遵循项目采纳后的 source standard。
- 例外失去必要性时应删除并更新架构检查。

## Revisit Conditions

当框架约束、route topology 或生成方式变化时重新评估。
"""
    return f"""# ADR: {identifier}

- Status: proposed
- Date: {date}

## Context

`{scope}` may require a deliberate deviation from generic Preset defaults.

## Proposed Decision

Propose the exception within that scope: {reason}

## Consequences If Adopted

- The exception applies only to the declared scope.
- Non-framework/tool-controlled code follows the source standard after project adoption.
- Remove the exception and update checks when the pressure disappears.

## Revisit Conditions

Revisit when framework constraints, route topology, or generation strategy changes.
"""


def exception_adr_files(overlay: dict[str, Any], zh: bool) -> dict[str, str]:
    import posixpath
    files: dict[str, str] = {}
    default_date = str(overlay.get("adoption_date") or "not-yet-established")
    for exception in overlay.get("exceptions") or []:
        if not isinstance(exception, dict) or not exception.get("adr"):
            continue
        rel = posixpath.normpath(posixpath.join("docs/standards", str(exception["adr"])))
        if not rel.startswith("docs/adr/") or not rel.endswith(".md") or ".." in Path(rel).parts:
            raise ValueError(f"exception ADR must resolve under docs/adr/**: {exception['adr']!r}")
        files[rel] = render_exception_adr(exception, zh, default_date)
    return files

def render_files(preset_input: dict[str, Any], overlay: dict[str, Any], existing_agents: str | None = None) -> dict[str, str]:
    resolution, _ = validate_inputs(preset_input, overlay)
    profiles = resolution["resolved"]
    zh = is_zh(overlay)
    managed = managed_agents_section(overlay, profiles)
    files: dict[str, str] = {"AGENTS.md": merge_agents(existing_agents, managed, zh)}

    has_product_language = bool(overlay.get("domain_terms"))
    has_fact_authority_map = bool(overlay.get("authorities"))
    has_ssot = has_product_language
    has_topology = any(overlay.get(key) for key in ("deployables", "packages", "modules", "workflows", "topology_notes"))
    has_architecture = has_topology or has_fact_authority_map
    has_harness = "verification-core" in profiles and bool(overlay.get("harness_coverage"))

    standard_reads = ["architecture-profile.yaml", "source-topology-and-naming.md", "naming-vocabulary.yaml"]
    if "verification-core" in profiles:
        standard_reads.append("verification-policy.md")
    files["docs/standards/README.md"] = layer_readme(
        "Standards",
        ["供项目 owner 采纳的规则、命名、检查与命令候选" if zh else "candidate rules, naming, checks, and commands for project-owner adoption"],
        ["产品事实、实际拓扑、未来路线" if zh else "product truth, actual topology, or future roadmap"],
        standard_reads,
        zh,
    )
    files["docs/standards/architecture-profile.yaml"] = render_architecture_profile(overlay, resolution)
    files["docs/standards/source-topology-and-naming.md"] = render_source_standard(overlay, profiles)
    files["docs/standards/naming-vocabulary.yaml"] = render_vocabulary(overlay, profiles)
    if "verification-core" in profiles:
        files["docs/standards/verification-policy.md"] = render_verification_policy(overlay)

    if has_ssot:
        files["docs/ssot/README.md"] = layer_readme(
            "SSoT",
            ["共享术语、对象、状态与不变量的候选 Current Home" if zh else "candidate Current Home for shared terms, objects, states, and invariants"],
            ["技术 writer/transaction 规则、目录规范、运行日志或所有 claim 的全局最高权威" if zh else "technical writer/transaction rules, directory rules, run logs, or a globally highest authority for every claim"],
            ["product-language.md", "../standards/README.md"],
            zh,
        )
        files["docs/ssot/product-language.md"] = render_product_language(overlay)

    if has_architecture:
        architecture_reads = ["../standards/source-topology-and-naming.md"]
        if has_topology:
            architecture_reads.insert(0, "repository-topology.md")
        if has_fact_authority_map:
            architecture_reads.append("fact-authority-map.md")
        if has_ssot:
            architecture_reads.append("../ssot/README.md")
        files["docs/architecture/README.md"] = layer_readme(
            "Architecture",
            ["系统拓扑、技术 fact writer、consistency boundary 与接受 seam 的候选" if zh else "candidate system topology, technical fact writers, consistency boundaries, and accepted seams"],
            ["强制标准、产品事实、未来候选" if zh else "binding standards, product truth, or future candidates"],
            architecture_reads,
            zh,
        )
        if has_topology:
            files["docs/architecture/repository-topology.md"] = render_topology(overlay)
        if has_fact_authority_map:
            files["docs/architecture/fact-authority-map.md"] = render_fact_authority_map(overlay)

    exception_files = exception_adr_files(overlay, zh)
    adr_reads = ["0001-adopt-evolvable-application-preset.md", *[Path(path).name for path in sorted(exception_files)], "_template.md"]
    files["docs/adr/README.md"] = layer_readme(
        "Architecture Decision Records",
        ["待项目 owner 决定的取舍、替代方案与重新评估条件" if zh else "proposed tradeoffs, alternatives, and revisit conditions for project-owner decision"],
        ["当前标准全文、实施进度、未来猜测" if zh else "full current standards, execution progress, or future speculation"],
        adr_reads,
        zh,
    )
    files["docs/adr/_template.md"] = "# ADR-XXXX: <Decision>\n\n- Status: proposed | accepted | superseded | rejected\n- Date: YYYY-MM-DD\n\n## Context\n\n## Decision\n\n## Alternatives\n\n## Consequences\n\n## Revisit Conditions\n"
    files["docs/adr/0001-adopt-evolvable-application-preset.md"] = render_adoption_adr(overlay, profiles)
    files.update(exception_files)

    if has_harness:
        files["docs/product-harness/README.md"] = render_harness_readme(zh)
        files["docs/product-harness/coverage.yaml"] = dump_yaml({"schema_version": 1, "capabilities": overlay.get("harness_coverage") or []})
    if "typescript-node" in profiles:
        files["tooling/architecture_check.py"] = architecture_checker_template()

    docs_reads = ["standards/README.md", "adr/README.md"]
    if has_ssot:
        docs_reads.append("ssot/README.md")
    if has_architecture:
        docs_reads.append("architecture/README.md")
    if has_harness:
        docs_reads.append("product-harness/README.md")
    files["docs/README.md"] = layer_readme(
        "Documentation Router",
        ["候选文档入口与层级路由" if zh else "candidate documentation entry and layer routing"],
        ["产品事实、架构标准或执行进度本身" if zh else "product truth, architecture standards, or execution progress itself"],
        docs_reads,
        zh,
    )
    return files


def write_files(out: Path, files: dict[str, str], force: bool) -> None:
    collisions = [rel for rel in files if (out / rel).exists() and rel != "AGENTS.md"]
    if collisions and not force:
        raise FileExistsError("refusing to overwrite project-owned files without --force: " + ", ".join(collisions[:10]))
    for rel, content in files.items():
        p = out / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")
        if rel.endswith(".py"):
            p.chmod(0o755)


def workspace_manifest_paths(root: Path, package_data: dict[str, Any]) -> list[Path]:
    patterns: list[str] = []
    workspaces = package_data.get("workspaces")
    if isinstance(workspaces, list):
        patterns.extend(item for item in workspaces if isinstance(item, str))
    elif isinstance(workspaces, dict):
        patterns.extend(item for item in (workspaces.get("packages") or []) if isinstance(item, str))
    pnpm_workspace = root / "pnpm-workspace.yaml"
    if pnpm_workspace.is_file():
        try:
            pnpm = load_yaml(pnpm_workspace)
            patterns.extend(item for item in (pnpm.get("packages") or []) if isinstance(item, str))
        except (OSError, ValueError):
            pass
    manifests = {root / "package.json"} if (root / "package.json").is_file() else set()
    for pattern in patterns:
        for candidate in root.glob(pattern):
            manifest = candidate / "package.json" if candidate.is_dir() else candidate
            if manifest.is_file():
                manifests.add(manifest.resolve())
    return sorted(manifests)


def inspect_repo(repo: Path) -> dict[str, Any]:
    root = repo.resolve()
    package = root / "package.json"
    package_data = {}
    if package.is_file():
        try: package_data = json.loads(package.read_text(encoding="utf-8"))
        except Exception: package_data = {"parse_error": True}
    manifest_paths = workspace_manifest_paths(root, package_data)
    manifest_data: list[tuple[Path, dict[str, Any]]] = []
    for manifest in manifest_paths:
        try:
            data = json.loads(manifest.read_text(encoding="utf-8"))
            if isinstance(data, dict):
                manifest_data.append((manifest, data))
        except (OSError, json.JSONDecodeError):
            continue
    locks = [n for n in ("pnpm-lock.yaml", "package-lock.json", "yarn.lock", "bun.lock", "bun.lockb") if (root/n).exists()]
    apps = sorted(p.name for p in (root/"apps").iterdir() if p.is_dir()) if (root/"apps").is_dir() else []
    packages = sorted(p.name for p in (root/"packages").iterdir() if p.is_dir()) if (root/"packages").is_dir() else []
    dependency_versions: dict[str, set[str]] = {}
    for _, data in manifest_data:
        deps = {**(data.get("dependencies") or {}), **(data.get("devDependencies") or {})}
        for name, version in deps.items():
            if isinstance(version, str):
                dependency_versions.setdefault(name, set()).add(version)
    agents_path = root / "AGENTS.md"
    agents_text = agents_path.read_text(encoding="utf-8", errors="replace") if agents_path.is_file() else ""
    profile_path = root / "docs/standards/architecture-profile.yaml"
    snapshot: dict[str, Any] = {}
    if profile_path.is_file():
        try:
            profile = load_yaml(profile_path)
            snapshot = {
                "mode": (profile.get("preset") or {}).get("mode"),
                "version": (profile.get("preset") or {}).get("version"),
                "profiles": profile.get("profiles") or [],
            }
        except Exception as exc:
            snapshot = {"parse_error": str(exc)}
    surface_candidates = [
        "AGENTS.md",
        "docs/README.md",
        "docs/ssot/README.md",
        "docs/ssot/product-language.md",
        "docs/architecture/fact-authority-map.md",
        "docs/standards/README.md",
        "docs/standards/architecture-profile.yaml",
        "docs/standards/source-topology-and-naming.md",
        "docs/standards/naming-vocabulary.yaml",
        "docs/standards/verification-policy.md",
        "docs/architecture/README.md",
        "docs/architecture/repository-topology.md",
        "docs/product-harness/coverage.yaml",
        "tooling/architecture_check.py",
    ]
    return {
        "repo": str(root),
        "existing_surfaces": [rel for rel in surface_candidates if (root / rel).is_file()],
        "managed_agents_section": MANAGED_BEGIN in agents_text and MANAGED_END in agents_text,
        "preset_snapshot": snapshot or None,
        "adopted_preset": snapshot if snapshot.get("mode") == "resolved-snapshot" else None,
        "package_manager_locks": locks,
        "workspace_manifests": [str(path.relative_to(root)) for path, _ in manifest_data],
        "apps": apps,
        "packages": packages,
        "detected": {
            "typescript": "typescript" in dependency_versions,
            "react": "react" in dependency_versions,
            "effect": "effect" in dependency_versions or any(k.startswith("effect-") for k in dependency_versions),
        },
        "dependency_versions": {name: sorted(versions) for name, versions in sorted(dependency_versions.items()) if name in {"typescript", "react", "effect"}},
        "scripts": package_data.get("scripts") or {},
    }


def validate_repo(repo: Path) -> dict[str, Any]:
    root = repo.resolve()
    findings: list[dict[str, str]] = []
    profile_path = root / "docs/standards/architecture-profile.yaml"
    snapshot_mode: str | None = None
    declared_snapshot = False
    selected_profiles: list[str] = []
    declared_surfaces: list[str] = []
    if profile_path.is_file():
        try:
            profile = load_yaml(profile_path)
            mode = ((profile.get("preset") or {}).get("mode"))
            snapshot_mode = mode if isinstance(mode, str) else None
            declared_snapshot = snapshot_mode in {"candidate-snapshot", "resolved-snapshot"}
            if not declared_snapshot:
                findings.append({"severity": "error", "path": str(profile_path), "message": "preset.mode must be candidate-snapshot or legacy resolved-snapshot"})
            selected = profile.get("profiles") or []
            if not isinstance(selected, list) or not selected:
                findings.append({"severity": "error", "path": str(profile_path), "message": "Preset snapshot must declare profiles"})
            else:
                selected_profiles = selected
                try:
                    _, resolved_ids = load_profiles(selected)
                    if selected != resolved_ids:
                        findings.append({"severity": "error", "path": str(profile_path), "message": "profile list is not the resolved dependency closure"})
                except ValueError as exc:
                    findings.append({"severity": "error", "path": str(profile_path), "message": str(exc)})
            resolution = profile.get("profile_resolution") or {}
            if not isinstance(resolution, dict):
                findings.append({"severity": "error", "path": str(profile_path), "message": "profile_resolution must be an object"})
            elif "defaults_added" in resolution:
                keys = ("requested", "defaults_added", "dependency_added", "resolved")
                if any(not isinstance(resolution.get(key), list) or any(not isinstance(item, str) or not item for item in resolution.get(key, [])) for key in keys):
                    findings.append({"severity": "error", "path": str(profile_path), "message": "profile_resolution fields must be arrays of non-empty profile ids"})
                else:
                    requested = list(dict.fromkeys(resolution["requested"]))
                    defaults_added = list(dict.fromkeys(resolution["defaults_added"]))
                    if set(requested).intersection(defaults_added):
                        findings.append({"severity": "error", "path": str(profile_path), "message": "profile_resolution requested/defaults_added must be disjoint"})
                    else:
                        try:
                            _, expected_resolved = load_profiles([*defaults_added, *requested])
                        except ValueError as exc:
                            findings.append({"severity": "error", "path": str(profile_path), "message": str(exc)})
                        else:
                            expected_dependencies = [item for item in expected_resolved if item not in requested and item not in defaults_added]
                            if resolution["resolved"] != expected_resolved or resolution["dependency_added"] != expected_dependencies or selected_profiles != expected_resolved:
                                findings.append({"severity": "error", "path": str(profile_path), "message": "profile_resolution provenance does not match defaults, dependencies, and resolved closure"})
            resolved_standards = profile.get("resolved_standards") or {}
            if not isinstance(resolved_standards, dict):
                findings.append({"severity": "error", "path": str(profile_path), "message": "resolved_standards must be an object"})
            else:
                for value in resolved_standards.values():
                    if not isinstance(value, str) or not value:
                        continue
                    candidate = (profile_path.parent / value).resolve()
                    try:
                        declared_surfaces.append(candidate.relative_to(root).as_posix())
                    except ValueError:
                        findings.append({"severity": "error", "path": str(profile_path), "message": f"resolved standard escapes repository: {value}"})
        except Exception as exc:
            findings.append({"severity": "error", "path": str(profile_path), "message": f"invalid YAML: {exc}"})
    else:
        findings.append({"severity": "warn", "path": "docs/standards/architecture-profile.yaml", "message": "no Preset snapshot found; validation is limited to project surfaces"})

    if declared_snapshot:
        required = ["docs/standards/architecture-profile.yaml", *declared_surfaces]
        if "agent-entry" in selected_profiles:
            required.append("AGENTS.md")
        for rel in dict.fromkeys(required):
            if not (root / rel).is_file():
                findings.append({"severity": "error", "path": rel, "message": "declared resolved Preset surface is missing"})

    agents = root / "AGENTS.md"
    if agents.is_file():
        text = agents.read_text(encoding="utf-8", errors="ignore")
        if MANAGED_BEGIN not in text or MANAGED_END not in text:
            findings.append({"severity": "warn", "path": "AGENTS.md", "message": "Preset managed markers missing; upgrades cannot merge the section safely"})
        required_links = ["docs/README.md"] if (root / "docs" / "README.md").is_file() else []
        for rel in required_links:
            if rel not in text:
                findings.append({"severity": "warn", "path": "AGENTS.md", "message": f"knowledge-network route missing: {rel}"})
    summary = {"error": sum(x["severity"] == "error" for x in findings), "warn": sum(x["severity"] == "warn" for x in findings), "total": len(findings)}
    return {"repo": str(root), "scope": snapshot_mode or "partial", "summary": summary, "findings": findings}


def unified_diff(repo: Path, rendered: Path) -> str:
    # A Preset candidate owns only the files it renders. Unrelated repository
    # files must never appear as candidate deletions.
    paths = {
        p.relative_to(rendered).as_posix()
        for p in rendered.rglob("*")
        if p.is_file() and ".git" not in p.parts and ".evolvable-preset" not in p.parts
    }
    chunks=[]
    for rel in sorted(paths):
        a=(repo/rel).read_text(encoding="utf-8", errors="replace").splitlines(True) if (repo/rel).is_file() else []
        b=(rendered/rel).read_text(encoding="utf-8", errors="replace").splitlines(True) if (rendered/rel).is_file() else []
        if a!=b:
            chunks.extend(difflib.unified_diff(a,b,fromfile=f"project/{rel}",tofile=f"preset-candidate/{rel}"))
    return "".join(chunks)


def cmd_render(args: argparse.Namespace) -> None:
    preset_input=load_yaml(Path(args.input)); overlay=load_yaml(Path(args.overlay))
    out=Path(args.out).resolve(); existing=(out/"AGENTS.md").read_text(encoding="utf-8") if (out/"AGENTS.md").is_file() else None
    files=render_files(preset_input, overlay, existing)
    write_files(out, files, args.force)
    print(json.dumps({"status":"candidate-rendered","out":str(out),"files":sorted(files),"claim":"not-adopted"}, ensure_ascii=False, indent=2))


def cmd_diff(args: argparse.Namespace) -> None:
    repo=Path(args.repo).resolve(); preset_input=load_yaml(Path(args.input)); overlay=load_yaml(Path(args.overlay))
    with tempfile.TemporaryDirectory(prefix="evo-preset-") as td:
        rendered=Path(td)
        existing=(repo/"AGENTS.md").read_text(encoding="utf-8") if (repo/"AGENTS.md").is_file() else None
        write_files(rendered, render_files(preset_input, overlay, existing), True)
        print(unified_diff(repo, rendered))


def cmd_upgrade(args: argparse.Namespace) -> None:
    repo=Path(args.repo).resolve(); preset_input=load_yaml(Path(args.input)); overlay=load_yaml(Path(args.overlay))
    stamp=datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    candidate=repo/".evolvable-preset"/"upgrade-candidate"/stamp
    existing=(repo/"AGENTS.md").read_text(encoding="utf-8") if (repo/"AGENTS.md").is_file() else None
    write_files(candidate, render_files(preset_input, overlay, existing), True)
    diff=unified_diff(repo, candidate)
    (candidate/"PRESET-DIFF.patch").write_text(diff, encoding="utf-8")
    print(json.dumps({"status":"staged","candidate":str(candidate),"diff":str(candidate/"PRESET-DIFF.patch"),"note":"project files were not overwritten"}, indent=2))


def main() -> None:
    ap=argparse.ArgumentParser(description="Evolvable Application Preset")
    sub=ap.add_subparsers(dest="cmd", required=True)
    p=sub.add_parser("inspect"); p.add_argument("--repo", default=".")
    p=sub.add_parser("render"); p.add_argument("--input", required=True); p.add_argument("--overlay", required=True); p.add_argument("--out", required=True); p.add_argument("--force", action="store_true")
    p=sub.add_parser("validate"); p.add_argument("--repo", default=".")
    p=sub.add_parser("diff"); p.add_argument("--repo", required=True); p.add_argument("--input", required=True); p.add_argument("--overlay", required=True)
    p=sub.add_parser("upgrade"); p.add_argument("--repo", required=True); p.add_argument("--input", required=True); p.add_argument("--overlay", required=True)
    args=ap.parse_args()
    try:
        if args.cmd=="inspect": print(json.dumps(inspect_repo(Path(args.repo)), ensure_ascii=False, indent=2))
        elif args.cmd=="render": cmd_render(args)
        elif args.cmd=="validate":
            report=validate_repo(Path(args.repo)); print(json.dumps(report, ensure_ascii=False, indent=2));
            if report["summary"]["error"]: raise SystemExit(1)
        elif args.cmd=="diff": cmd_diff(args)
        elif args.cmd=="upgrade": cmd_upgrade(args)
    except (ValueError, FileExistsError) as exc:
        print(json.dumps({"status":"error","error":str(exc)}, ensure_ascii=False, indent=2), file=sys.stderr)
        raise SystemExit(2)

if __name__=="__main__": main()
