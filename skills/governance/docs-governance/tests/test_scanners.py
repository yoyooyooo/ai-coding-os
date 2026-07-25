from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = SKILL_ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from common import parse_frontmatter  # noqa: E402
from scan_artifact_graph import scan as scan_graph  # noqa: E402
from scan_docs_baseline import scan as scan_baseline  # noqa: E402
from scan_docs_links import scan as scan_links  # noqa: E402
from scan_docs_agent_readability import scan as scan_readability  # noqa: E402
from scan_docs_structure import scan as scan_structure  # noqa: E402
from scan_future_capsules import scan as scan_future  # noqa: E402
from scan_agent_entry import scan as scan_agent_entry  # noqa: E402


class ScannerFixtures(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory(prefix="docs-governance-fixture-")
        self.repo = Path(self.tmp.name)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def write(self, relative: str, content: str = "") -> Path:
        path = self.repo / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def audit_cli(self, *flags: str) -> dict:
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
        result = subprocess.run(
            [sys.executable, str(SCRIPTS / "run_docs_audit.py"), "--repo", str(self.repo), *flags],
            cwd=SKILL_ROOT,
            check=False,
            capture_output=True,
            text=True,
            env=env,
        )
        self.assertIn(result.returncode, (0, 1), result.stderr)
        return json.loads(result.stdout)

    def test_no_docs_is_valid_and_does_not_require_fixed_layers(self) -> None:
        baseline = scan_baseline(self.repo)
        self.assertEqual(baseline["summary"]["blocker"], 0)
        self.assertIn("DOCS_ROOT_ABSENT", {item["ruleId"] for item in baseline["findings"]})
        result = self.audit_cli()
        self.assertEqual(result["summary"]["blocker"], 0)
        self.assertFalse(result["extensions"]["artifactGraph"])
        self.assertNotIn("artifactGraph", result["reports"])

    def test_flat_and_asymmetric_shapes_remain_healthy(self) -> None:
        self.write("docs/README.md", "# Docs\n\n## Discovery Surfaces\n")
        self.write("docs/ssot/README.md", "# SSoT\n\n## Owns\n\n## Must Not Own\n\n## Routes\n")
        for name in ("glossary.md", "runtime.md", "security.md"):
            self.write(f"docs/ssot/{name}", f"# {name}\n")
        self.write("docs/ssot/audit/README.md", "# Audit\n\n## Routes\n")
        self.write("docs/ssot/audit/domain.md", "# Domain\n")
        self.write("docs/ssot/audit/retention.md", "# Retention\n")
        report = scan_structure(self.repo)
        self.assertEqual(report["summary"]["blocker"], 0)
        rules = {item["ruleId"] for item in report["findings"]}
        self.assertNotIn("DOCS_SINGLE_ARTIFACT_PARTITION", rules)

    def test_single_file_partition_is_review_signal_not_failure(self) -> None:
        self.write("docs/ssot/README.md", "# SSoT\n")
        self.write("docs/ssot/audit.md", "# Audit\n")
        report = scan_structure(self.repo)
        self.assertEqual(report["summary"]["blocker"], 0)
        self.assertIn("DOCS_SINGLE_ARTIFACT_PARTITION", {item["ruleId"] for item in report["findings"]})
        self.assertEqual(report["summary"]["info"], 1)

    def test_single_file_layer_with_explicit_router_link_is_not_a_shape_signal(self) -> None:
        self.write("docs/architecture/README.md", "# Architecture\n\n## Routes\n\n- [Ownership map](repository-layer-breakdown.md)\n")
        self.write("docs/architecture/repository-layer-breakdown.md", "# Ownership Map\n")
        report = scan_structure(self.repo)
        self.assertNotIn("DOCS_SINGLE_ARTIFACT_PARTITION", {item["ruleId"] for item in report["findings"]})

    def test_explicit_identity_duplicate_is_blocker_but_node_id_is_graph_opt_in(self) -> None:
        self.write("docs/a.md", "---\nrequirement_id: R-1\n---\n# A\n")
        self.write("docs/b.md", "---\nrequirement_id: R-1\n---\n# B\n")
        report = scan_structure(self.repo)
        self.assertEqual(report["summary"]["blocker"], 1)

        self.write("docs/c.md", "---\nnode_id: graph-a\n---\n# C\n")
        self.assertTrue(scan_graph(self.repo)["optIn"])
        default = self.audit_cli()
        self.assertTrue(default["extensions"]["artifactGraph"])
        self.assertIn("artifactGraph", default["reports"])

    def test_future_supports_flat_route_capsule_and_blocks_shadow_authority(self) -> None:
        self.write("docs/roadmap/payment-replay.md", "# Payment Replay\n")
        flat = scan_future(self.repo)
        self.assertEqual(flat["routes"][0]["kind"], "flat-route")
        self.write("docs/roadmap/future/search/README.md", "# Search\n\nFuture delta.\n")
        capsule = scan_future(self.repo)
        self.assertEqual(capsule["summary"]["blocker"], 0)
        self.write("docs/roadmap/future/ssot/README.md", "# Future SSoT\n")
        shadow = scan_future(self.repo)
        self.assertEqual(shadow["summary"]["blocker"], 1)

    def test_future_route_cannot_claim_current_authority(self) -> None:
        self.write(
            "docs/roadmap/future/search/README.md",
            "---\nauthority_scope: current-fact\n---\n# Search\n",
        )
        report = scan_future(self.repo)
        self.assertIn("FUTURE_ROUTE_CLAIMS_CURRENT_AUTHORITY", {item["ruleId"] for item in report["findings"]})

    def test_common_frontmatter_handles_lists_and_multiline_fields(self) -> None:
        parsed = parse_frontmatter(
            "---\n"
            "summary: |\n"
            "  first line\n"
            "  second line\n"
            "tags:\n"
            "  - one\n"
            "  - two\n"
            "---\n# Example\n"
        )
        self.assertIsNotNone(parsed)
        assert parsed is not None
        self.assertIn("first line", str(parsed["summary"]))
        self.assertEqual(parsed["tags"], ["one", "two"])

    def test_links_cover_encoded_targets_directories_anchors_and_escape(self) -> None:
        self.write("docs/README.md", "# Docs\n\n## Target\n")
        self.write("docs/space name.md", "# Space\n")
        self.write("docs/guide/README.md", "# Guide\n")
        self.write("docs/image.png", "png")
        (self.repo / "docs/outside-link").symlink_to("/etc/hosts")
        self.write(
            "docs/index.md",
            "[space](space%20name.md#Space)\n[guide](guide/)\n![image](image.png)\n[out](../../outside.txt)\n[symlink](outside-link)\n[bad-anchor](README.md#Missing)\n",
        )
        report = scan_links(self.repo)
        rules = {item["ruleId"] for item in report["findings"]}
        self.assertIn("DOCS_LINK_ROOT_ESCAPE", rules)
        self.assertIn("DOCS_LINK_ANCHOR_MISSING", rules)
        self.assertNotIn("DOCS_RELATIVE_LINK_MISSING", rules)

    def test_agent_entry_is_conditional_and_reports_evidence_driven_topology(self) -> None:
        self.write("package.json", '{"workspaces": ["packages/*"]}\n')
        self.write("packages/core/package.json", '{"name": "core"}\n')
        report = scan_agent_entry(self.repo)
        self.assertEqual(report["repoTopology"]["mode"], "workspace-monorepo")
        self.assertEqual(report["repoTopology"]["confidence"], "high")
        self.assertEqual(report["summary"]["blocker"], 0)

    def test_candidate_preset_snapshot_is_not_rejected_as_dynamic_inheritance(self) -> None:
        self.write("docs/standards/architecture-profile.yaml", "preset:\n  mode: candidate-snapshot\nprofiles:\n  - monorepo-core\n")
        report = scan_agent_entry(self.repo)
        self.assertNotIn("PRESET_MODE_UNSAFE", {item["ruleId"] for item in report["findings"]})

        self.write("docs/standards/architecture-profile.yaml", "preset:\n  mode: dynamic\nprofiles:\n  - monorepo-core\n")
        report = scan_agent_entry(self.repo)
        self.assertIn("PRESET_MODE_UNSAFE", {item["ruleId"] for item in report["findings"]})

    def test_multi_entry_routes_do_not_require_a_shortest_reading_path(self) -> None:
        self.write(
            "docs/README.md",
            "# Docs\n\n## Discovery Surfaces\n\n- [SSoT](ssot/README.md)\n- [Architecture](architecture/README.md)\n",
        )
        self.write("docs/ssot/README.md", "# SSoT\n\n## Routes\n\n- [Architecture](../architecture/README.md)\n")
        self.write("docs/architecture/README.md", "# Architecture\n\n## Routes\n\n- [SSoT](../ssot/README.md)\n")
        report = scan_readability(self.repo)
        self.assertNotIn("DOCS_DISCOVERY_SURFACES_MISSING", {item["ruleId"] for item in report["findings"]})
        self.assertNotIn("DOCS_LOCAL_ROUTES_MISSING", {item["ruleId"] for item in report["findings"]})

    def test_managed_marker_conflict_is_warning(self) -> None:
        self.write(
            "AGENTS.md",
            "<!-- preset:begin -->\nmanaged\n<!-- preset:end -->\n<!-- other:begin -->\n",
        )
        report = scan_agent_entry(self.repo)
        self.assertIn("AGENT_MANAGED_SECTION_MARKER_INVALID", {item["ruleId"] for item in report["findings"]})
        self.assertEqual(report["summary"]["blocker"], 0)


if __name__ == "__main__":
    unittest.main()
