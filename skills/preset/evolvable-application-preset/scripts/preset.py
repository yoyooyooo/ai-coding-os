#!/usr/bin/env python3
"""Render and validate the Evolvable Application Preset.

The renderer is intentionally conservative. It produces a resolved project
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
PRESET_VERSION = "1.0.0-experimental.1"
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


def validate_inputs(preset_input: dict[str, Any], overlay: dict[str, Any]) -> tuple[list[str], dict[str, Any]]:
    if preset_input.get("schema_version") != 1:
        raise ValueError("preset-input schema_version must be 1")
    ids = preset_input.get("profiles")
    if not isinstance(ids, list) or not ids:
        raise ValueError("profiles must be a non-empty list")
    if "agent-entry" not in ids:
        ids = ["agent-entry", *ids]
    if overlay.get("schema_version") != 1:
        raise ValueError("project-overlay schema_version must be 1")
    validate_overlay_shape(overlay)
    _, resolved_ids = load_profiles(ids)
    return resolved_ids, overlay["project"]


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


def managed_agents_section(overlay: dict[str, Any], profile_ids: list[str]) -> str:
    zh = is_zh(overlay)
    project = overlay["project"]
    commands = overlay.get("commands") or {}
    if zh:
        language = "持久叙事文档使用中文；路径、命令、Schema 字段、协议名和代码符号保留 canonical 形式。"
        text = f"""{MANAGED_BEGIN}
本仓库采用 `docs/standards/architecture-profile.yaml` 中声明的 Evolvable Application Preset 解析快照。

未采用的 Preset 与 Skill 默认值不能覆盖项目 authority；当前事实、规则、决策和实现证据按其 claim 类型读取。已采用的 Preset 输出归入对应项目 docs layer。

## Read First

1. `docs/README.md`
2. `docs/ssot/README.md`
3. `docs/standards/README.md`
4. `docs/standards/architecture-profile.yaml`
5. `docs/standards/source-topology-and-naming.md`
6. `docs/standards/naming-vocabulary.yaml`
7. 最近的 app/package/module README 或局部 `AGENTS.md`

## Working Rules

- 复用 `docs/standards/naming-vocabulary.yaml` 中的 canonical terms。
- 遵守 module public / host wiring 边界与事实 writer 约束。
- 不通过测试、Harness、Adapter、Worker、前端状态或直接持久化创造第二条 accepted-fact 写入路径。
- 优先复用现有 Harness；缺失时补最薄、可证伪的执行面。
- 区分实际观察、观察支持的结论与尚未证明的邻接能力。
- 只有当前事实、标准、合同、决策或拓扑变化时才更新持久文档。

## Commands

{command_lines(commands, True)}

## Skill Routing

当 AI Coding OS Skill Suite 可用时，跨域或不明确任务使用 `$ai-coding-os` 作为知识路由；明确任务可直接使用专业 Skill。Skill 建议不能覆盖仓库内当前权威。

## Language

{language}

Preset profiles: {', '.join(profile_ids)}
Project: {project['name']} (`{project['id']}`)
{MANAGED_END}"""
    else:
        language = "Use the repository narrative language for durable prose; preserve canonical paths, commands, schema fields, protocol names, and code symbols."
        text = f"""{MANAGED_BEGIN}
This repository adopts the resolved Evolvable Application Preset declared in `docs/standards/architecture-profile.yaml`.

Unadopted Preset and Skill defaults cannot override project authority; resolve current facts, rules, decisions, and implementation evidence by claim type. Adopted Preset output belongs to its project docs layer.

## Read First

1. `docs/README.md`
2. `docs/ssot/README.md`
3. `docs/standards/README.md`
4. `docs/standards/architecture-profile.yaml`
5. `docs/standards/source-topology-and-naming.md`
6. `docs/standards/naming-vocabulary.yaml`
7. The nearest app/package/module README or local `AGENTS.md`

## Working Rules

- Reuse canonical terms from `docs/standards/naming-vocabulary.yaml`.
- Respect module public/host-wiring and fact-writer boundaries.
- Do not create another accepted-fact writer through tests, harnesses, adapters, workers, frontend state, or direct persistence.
- Prefer existing Harness surfaces; add the thinnest falsifiable surface when needed.
- Separate observations, supported conclusions, and unproven adjacent behavior.
- Update durable docs only when current truth, rules, contracts, decisions, or topology change.

## Commands

{command_lines(commands, False)}

## Skill Routing

Use `$ai-coding-os` for ambiguous or cross-cutting work when the Suite is available. Clear tasks may use the owning specialist directly. Skill guidance never overrides repository-local authority.

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
    if MANAGED_BEGIN in existing and MANAGED_END in existing:
        before, rest = existing.split(MANAGED_BEGIN, 1)
        _, after = rest.split(MANAGED_END, 1)
        return before.rstrip() + "\n\n" + managed + "\n\n" + after.lstrip()
    return existing.rstrip() + "\n\n" + managed + "\n"


def layer_readme(title: str, owns: list[str], not_owns: list[str], reads: list[str], zh: bool) -> str:
    links = chr(10).join(f"- [{item}]({item})" for item in reads)
    is_router = title == "Documentation Router"
    if zh:
        reading_heading = "## 最短阅读路径 / 下一步阅读" if is_router else "## Read Next"
        return f"""# {title}

## Owns

{chr(10).join('- ' + x for x in owns)}

## Must Not Own

{chr(10).join('- ' + x for x in not_owns)}

## Boundary / Conflict

仓库当前权威优先；本层只拥有上面列出的语义。与其他层重复时，移动到唯一 owner 并保留必要链接。

## Promotion / Demotion

候选内容只有在被采用并与源码/合同对齐后才能晋升为当前权威；过期内容应降级为 source/report 或删除。

{reading_heading}

{links}
"""
    reading_heading = "## Read First / Read Next" if is_router else "## Read Next"
    return f"""# {title}

## Owns

{chr(10).join('- ' + x for x in owns)}

## Must Not Own

{chr(10).join('- ' + x for x in not_owns)}

## Boundary / Conflict

Repository current authority wins. This layer owns only the semantics listed above. Move duplicate current content to one owner and keep links where useful.

## Promotion / Demotion

Candidates become current authority only after adoption and source/contract alignment. Obsolete content becomes source/report evidence or is deleted.

{reading_heading}

{links}
"""


def render_architecture_profile(preset_input: dict[str, Any], overlay: dict[str, Any], profiles: list[str]) -> str:
    project = overlay["project"]
    data = {
        "schema_version": 1,
        "preset": {"id": PRESET_ID, "version": PRESET_VERSION, "mode": "resolved-snapshot"},
        "profiles": profiles,
        "decisions": {
            "repository_mode": project.get("repository_mode", "monorepo"),
            "backend_module_style": "private-capability-module-first",
            "source_layout": "bounded-semantic-flat",
            "package_promotion": "pressure-driven",
            "deployable_promotion": "pressure-driven",
        },
        "resolved_standards": {
            "source_topology": "./source-topology-and-naming.md",
            "vocabulary": "./naming-vocabulary.yaml",
            "verification_policy": "./verification-policy.md" if "verification-core" in profiles else None,
        },
        "enforcement": overlay.get("enforcement") or {
            "architecture_check": (overlay.get("commands") or {}).get("architecture_check"),
            "verify_affected": (overlay.get("commands") or {}).get("verify_affected"),
        },
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
    if zh:
        return f"""# Source Topology and Naming

本文件是当前项目生效的 resolved standard。通用理论来自 Suite Skills；本文件记录本仓库采用结果。

## Repository Topology

- Repository mode: `{overlay['project'].get('repository_mode', 'monorepo')}`
- Deployable hosts: {apps_text}
- Workspace packages: {pkg_text}
- 后端默认从 `apps/api/src/modules/<capability>` 的私有 capability module 开始。
- 跨 module 普通调用只使用 `<subject>.public.ts`；host composition 可额外使用 `<subject>.wiring.ts`。
- package 不得 import app internals；module 不因使用 Effect 自动成为 package。

## Bounded Semantic Flatness

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

## Canonical Patterns

```text
order.create.use-case.ts
order.by-id.query.ts
order.repository.port.ts
order.repository.postgres.live.ts
order.repository.memory.fake.ts
order.http.contract.ts
order.http.handlers.ts
order.public.ts
order.wiring.ts
channel.client.browser.live.ts
channel.query.ts
channel.store.ts
channel.realtime.ts
channel.view-model.ts
channel.surface.tsx
order.checkout.retry.harness.ts
```

不机械生成完整后缀套装。框架保留文件名可以例外，但 adapter 应保持薄。

## Import Boundaries

- `*.policy.ts` 不依赖 HTTP、DB、SDK 或 live adapter。
- `*.use-case.ts` 不依赖 `*.live.ts` 或 transport handler。
- `*.port.ts` 不泄露 provider SDK / ORM 类型。
- `*.http.*.ts` 只 decode/map/call use case，不直接写数据库。
- 普通业务 module 不 import `*.wiring.ts`。
- `*.fake.ts` 不能无提示进入 production composition。
- Harness 不得绕过正式 use-case/materialization path。

## Promotion Ladder

```text
lexical cluster -> private submodule -> workspace package -> deployable process
```

每次晋升都需要真实压力；目录或 package 本身不授予 accepted-fact 写入权。

## Profiles

{chr(10).join('- `' + x + '`' for x in profiles)}
"""
    return f"""# Source Topology and Naming

This is the project's current resolved standard. Generic rationale remains in the Suite Skills; this file records the repository's adopted result.

## Repository Topology

- Repository mode: `{overlay['project'].get('repository_mode', 'monorepo')}`
- Deployable hosts: {apps_text}
- Workspace packages: {pkg_text}
- Backend capability modules start private under `apps/api/src/modules/<capability>` by default.
- Cross-module business calls use `<subject>.public.ts`; host composition may also use `<subject>.wiring.ts`.
- Packages do not import app internals; Effect usage does not automatically create a package.

## Bounded Semantic Flatness

Directories express durable ownership; filenames express local subject, responsibility, implementation, and proof role; packages enforce compile/import boundaries; apps run.

Use `<subject>[.<facet>...].<responsibility>[.<qualifier>...].<extension>` with kebab-case inside a segment and dots between dimensions. A repeated prefix is a lexical cluster, not a module/package/authority.

## Canonical Patterns

```text
order.create.use-case.ts
order.by-id.query.ts
order.repository.port.ts
order.repository.postgres.live.ts
order.repository.memory.fake.ts
order.http.contract.ts
order.http.handlers.ts
order.public.ts
order.wiring.ts
channel.client.browser.live.ts
channel.query.ts
channel.store.ts
channel.realtime.ts
channel.view-model.ts
channel.surface.tsx
order.checkout.retry.harness.ts
```

Do not mechanically generate a complete suffix set. Framework-reserved filenames
may be exceptions, but adapters should remain thin.

## Import Boundaries

- `*.policy.ts` does not depend on HTTP, DB, SDK, or live adapters.
- `*.use-case.ts` does not depend on `*.live.ts` or transport handlers.
- `*.port.ts` does not expose provider SDK/ORM types.
- `*.http.*.ts` decodes/maps/calls use cases and does not write persistence directly.
- Business modules do not import `*.wiring.ts`.
- `*.fake.ts` is never a silent production fallback.
- Harnesses do not bypass the formal materialization path.

## Promotion Ladder

`lexical cluster -> private submodule -> workspace package -> deployable process`

## Profiles

{chr(10).join('- `' + x + '`' for x in profiles)}
"""


def render_vocabulary(overlay: dict[str, Any], profiles: list[str]) -> str:
    preset_root = Path(__file__).resolve().parents[1]
    snapshot = preset_root / "references/suite-contract-snapshot"
    vocabulary = load_yaml(snapshot / "semantic-vocabulary.yaml")
    patterns = load_yaml(snapshot / "filename-patterns.yaml")
    guarded = load_yaml(snapshot / "guarded-terms.yaml")
    terms = overlay.get("domain_terms") or {}
    project_terms: dict[str, Any] = {}
    for token, info in terms.items():
        if not isinstance(info, dict):
            info = {"meaning": str(info)}
        project_terms[token] = {
            "status": info.get("status", "canonical"),
            "product_term": info.get("product_term", token),
            "source_token": info.get("source_token", token),
            "kind": info.get("kind", "product-term"),
            "meaning": info.get("meaning", "not-yet-established"),
            "not_the_same_as": info.get("not_the_same_as", []),
            "aliases": info.get("aliases", {}),
        }
    data = {
        "schema_version": 1,
        "preset_snapshot": {
            "id": PRESET_ID,
            "version": PRESET_VERSION,
            "profiles": profiles,
            "note": "Resolved copy. Project standards are current authority; Suite files are provenance, not dynamic inheritance.",
        },
        "syntax": vocabulary.get("syntax") or {},
        "canonical_terms": vocabulary.get("terms") or {},
        "canonical_qualifiers": vocabulary.get("qualifiers") or {},
        "filename_patterns": patterns.get("patterns") or [],
        "directory_admission": patterns.get("directory_admission") or [],
        "promotion_ladder": patterns.get("promotion_ladder") or [],
        "guarded_terms": guarded.get("terms") or {},
        "project_terms": project_terms,
        "implementation_qualifiers": overlay.get("implementation_qualifiers") or {},
        "deprecated_terms": overlay.get("deprecated_terms") or {},
    }
    return dump_yaml(data)


def render_product_language(overlay: dict[str, Any]) -> str:
    zh = is_zh(overlay)
    terms = overlay.get("domain_terms") or {}
    if zh:
        lines = ["# Product Language", "", "本文件记录产品 canonical terms。它拥有产品词义，不拥有源码目录规则。", "", "| Canonical term | Meaning | Kind | Not the same as |", "| --- | --- | --- | --- |"]
    else:
        lines = ["# Product Language", "", "This file records canonical product terms. It owns product meaning, not source-directory rules.", "", "| Canonical term | Meaning | Kind | Not the same as |", "| --- | --- | --- | --- |"]
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


def render_authority_map(overlay: dict[str, Any]) -> str:
    zh = is_zh(overlay)
    authorities = overlay.get("authorities") or []
    intro = "本文件记录当前 accepted facts 与 writer 权威。未知项不得凭 Preset 推断。" if zh else "This file records current accepted facts and writer authority. Unknown entries must not be inferred from the Preset."
    lines = ["# Authority Map", "", intro, "", "| Fact | Authority module | Writer host | Allowed entry | Forbidden path | Transaction / consistency |", "| --- | --- | --- | --- | --- | --- |"]
    if not authorities:
        lines.append("| not-yet-established | - | - | - | - | - |")
    else:
        for item in authorities:
            lines.append("| {fact} | {authority_module} | {writer_host} | {allowed_entry} | {forbidden_path} | {transaction} |".format(
                fact=item.get("fact", "-"), authority_module=item.get("authority_module", "-"), writer_host=item.get("writer_host", "-"), allowed_entry=item.get("allowed_entry", "-"), forbidden_path=item.get("forbidden_path", "-"), transaction=item.get("transaction", item.get("consistency", "-"))))
    return "\n".join(lines) + "\n"


def render_topology(overlay: dict[str, Any]) -> str:
    zh = is_zh(overlay)
    intro = "本文件描述当前实际拓扑，不重新定义标准。" if zh else "This file describes current actual topology; it does not redefine standards."
    lines = ["# Repository Topology", "", intro, ""]
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
        return """# Verification Policy

## Owns

- 可发现的 Harness command/descriptor 约定。
- fixture、fake、replay、real-local、real-external 的明确标识。
- 结构化结果中的 `observed`、`supports`、`not_proven`。

## Must Not Own

- 产品事实或第二套业务算法。
- Agent 的固定修复循环、重试次数或模型角色。
- 原始运行日志的长期文档副本。

## Commands

项目命令以 `AGENTS.md` 和 `package.json` 为准。推荐提供 `verify:list`、`verify:affected` 与 `verify` 等可发现入口，但不要求统一工具。

## Claim Boundary

Harness 只支持实际执行表面对应的结论。Fake、Replay、Headless、Browser 与 External Runtime 必须明确区分。
"""
    return """# Verification Policy

## Owns

- Discoverable Harness command/descriptor conventions.
- Explicit fixture/fake/replay/real-local/real-external labels.
- Structured `observed`, `supports`, and `not_proven` output.

## Must Not Own

- Product truth or a second business algorithm.
- Fixed Agent repair loops, retry counts, or model roles.
- Durable copies of every raw run log.

## Commands

Repository commands in `AGENTS.md` and package scripts are authoritative. Prefer discoverable `verify:list`, `verify:affected`, and `verify` entries when useful, without mandating one tool.

## Claim Boundary

Harness conclusions must match the exercised surface. Fake, replay, headless, browser, and external-runtime paths remain explicit.
"""


def render_harness_readme(zh: bool) -> str:
    return layer_readme(
        "Product Harness",
        ["稳定 Harness descriptor/scenario 引用、coverage 与 lifecycle" if zh else "stable Harness descriptor/scenario references, coverage, and lifecycle"],
        ["产品事实、可执行测试源码、原始日志、Goal progress" if zh else "product truth, executable test source, raw logs, or Goal progress"],
        ["coverage.yaml", "../standards/verification-policy.md"], zh,
    )


def render_adoption_adr(overlay: dict[str, Any], profiles: list[str]) -> str:
    zh = is_zh(overlay)
    adoption_date = str(overlay.get("adoption_date") or "not-yet-established")
    if zh:
        return f"""# ADR-0001: Adopt Evolvable Application Preset

- Status: accepted
- Date: {adoption_date}

## Context

本项目希望复用稳定的 authority-first、Monorepo/reference topology、Bounded Semantic Flatness、语义词汇与 Harness 默认值，同时让项目内 Docs 保持当前权威。

## Decision

采用 Evolvable Application Preset `{PRESET_VERSION}`，profiles：{', '.join(profiles)}。
Preset 以 `resolved-snapshot` 模式渲染；项目 `AGENTS.md` 与 `docs/**` 是当前权威。

## Consequences

- 通用规则不需要每个项目重新讨论。
- 项目仍必须填写自身产品语言、authority、实际拓扑与例外。
- Preset 升级必须显式比较并采纳，不能动态覆盖当前标准。
"""
    return f"""# ADR-0001: Adopt Evolvable Application Preset

- Status: accepted
- Date: {adoption_date}

## Context

The project wants reusable authority-first, Monorepo reference topology, Bounded Semantic Flatness, vocabulary, and Harness defaults while keeping project Docs authoritative.

## Decision

Adopt Evolvable Application Preset `{PRESET_VERSION}` with profiles: {', '.join(profiles)}. The Preset renders in `resolved-snapshot` mode; project `AGENTS.md` and `docs/**` are current authority.

## Consequences

- Cross-project defaults are not re-designed for every repository.
- The project still owns product language, authority, actual topology, and exceptions.
- Preset upgrades require explicit comparison and adoption.
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

- Status: accepted
- Date: {date}

## Context

`{scope}` 需要偏离通用 Preset 默认。

## Decision

在该 scope 内采用例外：{reason}

## Consequences

- 例外只适用于声明的 scope。
- 非框架/工具强制代码仍遵循 `docs/standards/source-topology-and-naming.md`。
- 例外失去必要性时应删除并更新架构检查。

## Revisit Conditions

当框架约束、route topology 或生成方式变化时重新评估。
"""
    return f"""# ADR: {identifier}

- Status: accepted
- Date: {date}

## Context

`{scope}` requires a deliberate deviation from the generic Preset defaults.

## Decision

Adopt the exception within that scope: {reason}

## Consequences

- The exception applies only to the declared scope.
- Non-framework/tool-controlled code still follows `docs/standards/source-topology-and-naming.md`.
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
    profiles, _ = validate_inputs(preset_input, overlay)
    zh = is_zh(overlay)
    managed = managed_agents_section(overlay, profiles)
    files: dict[str, str] = {}
    files["AGENTS.md"] = merge_agents(existing_agents, managed, zh)
    files["docs/README.md"] = layer_readme(
        "Documentation Router",
        ["当前文档入口与层级路由" if zh else "current documentation entry and layer routing"],
        ["产品事实、架构标准或执行进度本身" if zh else "product truth, architecture standards, or execution progress itself"],
        ["product/README.md", "ssot/README.md", "standards/README.md", "architecture/README.md", "adr/README.md"], zh)
    files["docs/product/README.md"] = layer_readme("Product", ["产品含义与用户/运营语义" if zh else "product and user/operator meaning"], ["源码目录规则、事实 writer、实施进度" if zh else "source layout rules, fact writers, or implementation progress"], ["../ssot/product-language.md"], zh)
    files["docs/ssot/README.md"] = layer_readme("SSoT", ["当前事实、对象所有权与不变量" if zh else "current facts, object ownership, and invariants"], ["未来候选、目录规范、运行日志" if zh else "future candidates, directory rules, or run logs"], ["product-language.md", "authority-map.md", "../standards/README.md"], zh)
    if zh:
        files["docs/ssot/README.md"] += """\n## Authority Resolution\n\n权威按 claim 类型解析，而不是使用一条无条件文件排序：\n\n```text\nhost instructions and repository AGENTS.md\n  -> adopted project authority for the claim\n     current facts -> docs/ssot/**\n     executable rules -> docs/standards/**\n     accepted tradeoffs -> docs/adr/**\n     wire compatibility -> project protocol/schema contract\n  -> executable reality for implementation claims\n     source, lockfiles, tests, command evidence\n  -> unadopted Preset source/candidate\n  -> specialist doctrine and router recommendation\n```\n\n已采用的 Preset 输出归入对应项目 docs layer，不是第二套 Preset authority。\n项目 authority 与 executable reality 冲突时，记录 stale-doc 或 implementation-drift，\n不能静默选择一方。\n"""
    else:
        files["docs/ssot/README.md"] += """\n## Authority Resolution\n\nAuthority is resolved by claim type rather than one unconditional file order:\n\n```text\nhost instructions and repository AGENTS.md\n  -> adopted project authority for the claim\n     current facts -> docs/ssot/**\n     executable rules -> docs/standards/**\n     accepted tradeoffs -> docs/adr/**\n     wire compatibility -> project protocol/schema contract\n  -> executable reality for implementation claims\n     source, lockfiles, tests, command evidence\n  -> unadopted Preset source/candidate\n  -> specialist doctrine and router recommendation\n```\n\nAn adopted Preset output belongs to its project docs layer; it is not a second\nPreset authority. If project authority and executable reality disagree, record\nstale-doc or implementation-drift instead of silently choosing one.\n"""
    files["docs/ssot/product-language.md"] = render_product_language(overlay)
    files["docs/ssot/authority-map.md"] = render_authority_map(overlay)
    files["docs/standards/README.md"] = layer_readme("Standards", ["当前可执行规则、命名、检查与命令" if zh else "current executable rules, naming, checks, and commands"], ["产品事实、实际拓扑、未来路线" if zh else "product truth, actual topology, or future roadmap"], ["architecture-profile.yaml", "source-topology-and-naming.md", "naming-vocabulary.yaml"], zh)
    files["docs/standards/architecture-profile.yaml"] = render_architecture_profile(preset_input, overlay, profiles)
    files["docs/standards/source-topology-and-naming.md"] = render_source_standard(overlay, profiles)
    files["docs/standards/naming-vocabulary.yaml"] = render_vocabulary(overlay, profiles)
    files["docs/architecture/README.md"] = layer_readme("Architecture", ["当前实际系统拓扑、运行视图与接受的 seam" if zh else "current actual topology, runtime views, and accepted seams"], ["强制标准、产品事实、未来候选" if zh else "binding standards, product truth, or future candidates"], ["repository-topology.md", "../ssot/README.md", "../ssot/authority-map.md", "../standards/source-topology-and-naming.md"], zh)
    files["docs/architecture/repository-topology.md"] = render_topology(overlay)
    exception_files = exception_adr_files(overlay, zh)
    adr_reads = ["0001-adopt-evolvable-application-preset.md", *[Path(path).name for path in sorted(exception_files)], "_template.md"]
    files["docs/adr/README.md"] = layer_readme("Architecture Decision Records", ["已采用取舍、替代方案与重新评估条件" if zh else "adopted tradeoffs, alternatives, and revisit conditions"], ["当前标准全文、实施进度、未来猜测" if zh else "full current standards, execution progress, or future speculation"], adr_reads, zh)
    files["docs/adr/_template.md"] = "# ADR-XXXX: <Decision>\n\n- Status: proposed | accepted | superseded | rejected\n- Date: YYYY-MM-DD\n\n## Context\n\n## Decision\n\n## Alternatives\n\n## Consequences\n\n## Revisit Conditions\n"
    files["docs/adr/0001-adopt-evolvable-application-preset.md"] = render_adoption_adr(overlay, profiles)
    files.update(exception_files)
    if "verification-core" in profiles:
        files["docs/standards/verification-policy.md"] = render_verification_policy(overlay)
        files["docs/product-harness/README.md"] = render_harness_readme(zh)
        files["docs/product-harness/coverage.yaml"] = dump_yaml({"schema_version": 1, "capabilities": overlay.get("harness_coverage") or []})
    if "typescript-node" in profiles:
        files["tooling/architecture_check.py"] = architecture_checker_template()
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
    adopted: dict[str, Any] = {}
    if profile_path.is_file():
        try:
            profile = load_yaml(profile_path)
            adopted = {
                "mode": (profile.get("preset") or {}).get("mode"),
                "version": (profile.get("preset") or {}).get("version"),
                "profiles": profile.get("profiles") or [],
            }
        except Exception as exc:
            adopted = {"parse_error": str(exc)}
    surface_candidates = [
        "AGENTS.md",
        "docs/README.md",
        "docs/ssot/README.md",
        "docs/ssot/product-language.md",
        "docs/ssot/authority-map.md",
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
        "adopted_preset": adopted or None,
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
    resolved_snapshot = False
    if profile_path.is_file():
        try:
            profile = load_yaml(profile_path)
            mode = ((profile.get("preset") or {}).get("mode"))
            resolved_snapshot = mode == "resolved-snapshot"
            if not resolved_snapshot:
                findings.append({"severity": "error", "path": str(profile_path), "message": "preset.mode must be resolved-snapshot"})
            selected = profile.get("profiles") or []
            if not isinstance(selected, list) or not selected:
                findings.append({"severity": "error", "path": str(profile_path), "message": "resolved snapshot must declare profiles"})
            else:
                try:
                    _, resolved_ids = load_profiles(selected)
                    if selected != resolved_ids:
                        findings.append({"severity": "error", "path": str(profile_path), "message": "profile list is not the resolved dependency closure"})
                except ValueError as exc:
                    findings.append({"severity": "error", "path": str(profile_path), "message": str(exc)})
        except Exception as exc:
            findings.append({"severity": "error", "path": str(profile_path), "message": f"invalid YAML: {exc}"})
    else:
        findings.append({"severity": "warn", "path": "docs/standards/architecture-profile.yaml", "message": "no resolved snapshot found; validation is limited to adopted project surfaces"})

    full_required = [
        "AGENTS.md", "docs/README.md", "docs/ssot/README.md", "docs/standards/README.md",
        "docs/standards/architecture-profile.yaml", "docs/standards/source-topology-and-naming.md",
        "docs/standards/naming-vocabulary.yaml", "docs/architecture/repository-topology.md",
        "docs/adr/0001-adopt-evolvable-application-preset.md",
    ]
    if resolved_snapshot:
        for rel in full_required:
            if not (root / rel).is_file():
                findings.append({"severity": "error", "path": rel, "message": "required resolved Preset file is missing"})

    agents = root / "AGENTS.md"
    if agents.is_file():
        text = agents.read_text(encoding="utf-8", errors="ignore")
        if MANAGED_BEGIN not in text or MANAGED_END not in text:
            findings.append({"severity": "warn", "path": "AGENTS.md", "message": "Preset managed markers missing; upgrades cannot merge the section safely"})
        for rel in ("docs/README.md", "docs/standards/architecture-profile.yaml", "docs/standards/naming-vocabulary.yaml"):
            if rel not in text:
                findings.append({"severity": "warn", "path": "AGENTS.md", "message": f"Read First link missing: {rel}"})
    summary = {"error": sum(x["severity"] == "error" for x in findings), "warn": sum(x["severity"] == "warn" for x in findings), "total": len(findings)}
    return {"repo": str(root), "scope": "resolved-snapshot" if resolved_snapshot else "partial", "summary": summary, "findings": findings}


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
    print(json.dumps({"status":"rendered","out":str(out),"files":sorted(files)}, ensure_ascii=False, indent=2))


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
