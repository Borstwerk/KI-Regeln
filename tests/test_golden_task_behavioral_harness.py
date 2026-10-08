from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import yaml

from tools.behavioral_harness import (
    HarnessError,
    default_actions,
    default_evidence,
    default_trace,
    evaluate_gates,
    verify_prepared_integrity,
)
from tools import behavioral_harness_claude as claude_adapter
from tools.golden_task_behavioral_harness import prepare
from tools.golden_task_execution_view import assert_blind, project


class GoldenTaskBlindnessTests(unittest.TestCase):
    def test_execution_projection_hides_editorial_routing_hints(self):
        task = {
            "schema_version": 1,
            "id": "GT-99",
            "title": "Use visual-answer and no other skill",
            "goal": "The expected route is tool-permission-review.",
            "assignment": "Explain the supplied note.",
            "fixtures": ["note.md"],
            "sources_of_truth": [{"path": "note.md", "role": "This wording must not leak."}],
            "required_capabilities": ["source-access"],
            "behavioral_routing_mode": "outcome-primary",
            "behavioral_execution_mode": "writable",
            "expected_domain": "none",
            "required_skills": [],
            "rubric": {"routing": ["none"]},
        }
        view = project(task)
        assert_blind(view)
        dumped = yaml.safe_dump(view, sort_keys=False)
        self.assertNotIn("visual-answer", dumped)
        self.assertNotIn("tool-permission-review", dumped)
        self.assertNotIn("GT-99", dumped)
        self.assertNotIn("sources_of_truth", view)
        self.assertNotIn("behavioral_routing_mode", view)
        self.assertNotIn("behavioral_execution_mode", view)
        self.assertEqual(
            {"schema_version", "assignment", "fixtures", "required_capabilities"},
            set(view),
        )

    def _repo(self, root: Path) -> Path:
        root.mkdir(parents=True)
        for name, content in {
            "AGENTS.md": "# Bootstrap\nRead skill-catalog.yml only as needed.\n",
            "skill-catalog.yml": "skills: []\n",
            "routing-overlays.yml": "schema_version: 2\noverlays: []\n",
            "workflow-index.yml": "schema_version: 1\nworkflows: []\n",
            "CHANGELOG.md": "GT-99 secret evaluator notes\n",
        }.items():
            (root / name).write_text(content, encoding="utf-8")

        (root / "Dokumentation").mkdir()
        (root / "Dokumentation" / "Skill-Handbuch.md").write_text("# Router\n", encoding="utf-8")

        visual_docs = root / "Dokumentationserstellung"
        visual_docs.mkdir()
        (visual_docs / "Visual-Answer-Explorativer-AB-Test-2026-10-06.md").write_text(
            "# Human A/B note\nThree options; HTML preferred.\n", encoding="utf-8"
        )

        skill = root / "Recherche" / "Skills" / "example"
        skill.mkdir(parents=True)
        (skill / "SKILL.md").write_text(
            "---\nname: example\ndescription: Verwenden bei einem synthetischen Beispiel; nicht für anderes.\n---\n# Example\n",
            encoding="utf-8",
        )

        workflows = root / "Workflows"
        workflows.mkdir()
        (workflows / "Synthetic.md").write_text("# Synthetic\n", encoding="utf-8")

        excluded = root / "Skill-Engineering"
        excluded.mkdir()
        (excluded / "Cross-Cutting-Skill-Discovery.md").write_text(
            "GT-09 must never reach the runner.\n", encoding="utf-8"
        )
        (excluded / "Quellen-und-Inspirationen.md").write_text(
            "Human/eval inspiration must never reach the runner.\n", encoding="utf-8"
        )

        evals = root / "Evals"
        evals.mkdir()
        (evals / "README.md").write_text("GT-10 expects no skill.\n", encoding="utf-8")
        return root

    def _task(self, repo: Path) -> Path:
        fixture = repo / "fixture.md"
        fixture.write_text("fixture truth\n", encoding="utf-8")
        task = repo / "task.yml"
        task.write_text(
            yaml.safe_dump(
                {
                    "schema_version": 1,
                    "id": "GT-99",
                    "title": "No-skill control",
                    "goal": "Do not load a skill.",
                    "assignment": "Summarize fixture.md in one sentence.",
                    "fixtures": ["fixture.md"],
                    "sources_of_truth": [{"path": "fixture.md", "role": "authoritative-source"}],
                    "required_capabilities": ["source-access"],
                    "behavioral_routing_mode": "outcome-primary",
                    "expected_domain": "none",
                    "allowed_secondary_domains": [],
                    "workflow": {"required": False, "allowed": []},
                    "required_skills": [],
                    "allowed_optional_skills": [],
                    "forbidden_skills": ["example"],
                    "expected_evidence": ["fixture truth"],
                    "expected_artifacts": ["one sentence"],
                    "expected_verification": ["compare to fixture"],
                    "allowed_uncertainty": [],
                    "expected_status": "pass",
                    "forbidden_behaviors": ["invent facts"],
                    "rubric": {
                        "routing": ["no skill"],
                        "grounding": ["fixture"],
                        "scope": ["one sentence"],
                        "gates": ["none"],
                        "verification": ["fixture"],
                        "result_quality": ["correct"],
                    },
                },
                allow_unicode=True,
                sort_keys=False,
            ),
            encoding="utf-8",
        )
        return task

    def test_prepare_builds_curated_neutral_runner_workspace(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self._repo(Path(tmp) / "repo")
            out = Path(tmp) / "prepared"
            prepare(self._task(root), root, "abc123", out)

            execution = yaml.safe_load((out / "runner-package" / "execution-view.yml").read_text(encoding="utf-8"))
            self.assertEqual("GT-99", execution["test_id"])
            self.assertEqual("Summarize fixture.md in one sentence.", execution["user_prompt"])
            fixture_path = execution["fixtures"][0]["path"]
            self.assertTrue(fixture_path.startswith("workspace/task/fixture-01-"))
            self.assertNotIn("Evals", fixture_path)

            repository = out / "runner-package" / "workspace" / "repository"
            self.assertTrue((repository / "AGENTS.md").is_file())
            self.assertTrue((repository / "Recherche" / "Skills" / "example" / "SKILL.md").is_file())
            self.assertFalse((repository / "Evals").exists())
            self.assertFalse((repository / "CHANGELOG.md").exists())
            self.assertFalse((repository / "Skill-Engineering" / "Cross-Cutting-Skill-Discovery.md").exists())
            self.assertFalse((repository / "Skill-Engineering" / "Quellen-und-Inspirationen.md").exists())
            self.assertFalse(
                (repository / "Dokumentationserstellung" / "Visual-Answer-Explorativer-AB-Test-2026-10-06.md").exists()
            )

            judge = yaml.safe_load((out / "judge-view.yml").read_text(encoding="utf-8"))
            self.assertEqual("outcome-primary", judge["routing_evaluation"]["mode"])
            self.assertFalse(judge["routing_evaluation"]["required_skill_read_enforced"])
            self.assertEqual("read-only", judge["execution_requirements"]["mode"])

            readiness = yaml.safe_load((out / "readiness.yml").read_text(encoding="utf-8"))
            self.assertTrue(readiness["ready_for_behavioral_execution"])
            self.assertTrue(readiness["default_read_only_runner_compatible"])

            verify_prepared_integrity(out)

    def test_reverse_engineering_skills_are_in_curated_runner_view(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self._repo(Path(tmp) / "repo")
            for skill_name in ("binary-triage", "binary-analysis"):
                skill = root / "Reverse-Engineering-und-Binaeranalyse" / "Skills" / skill_name
                skill.mkdir(parents=True)
                (skill / "SKILL.md").write_text(
                    "---\nname: " + skill_name
                    + "\ndescription: Verwenden zur autorisierten Analyse kompilierter Artefakte.\n---\n",
                    encoding="utf-8",
                )
            out = Path(tmp) / "prepared"
            prepare(self._task(root), root, "abc123", out)
            repository = out / "runner-package" / "workspace" / "repository"
            for skill_name in ("binary-triage", "binary-analysis"):
                self.assertTrue(
                    (repository / "Reverse-Engineering-und-Binaeranalyse" / "Skills"
                     / skill_name / "SKILL.md").is_file()
                )
            self.assertFalse((repository / "Evals").exists())
            verify_prepared_integrity(out)

    def test_writable_task_is_not_ready_for_default_read_only_runner(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self._repo(Path(tmp) / "repo")
            task = self._task(root)
            data = yaml.safe_load(task.read_text(encoding="utf-8"))
            data["behavioral_execution_mode"] = "writable"
            task.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")

            out = Path(tmp) / "prepared-writable"
            prepare(task, root, "abc123", out)

            execution = yaml.safe_load((out / "execution-view.yml").read_text(encoding="utf-8"))
            readiness = yaml.safe_load((out / "readiness.yml").read_text(encoding="utf-8"))
            judge = yaml.safe_load((out / "judge-view.yml").read_text(encoding="utf-8"))

            self.assertEqual("writable", execution["runtime"]["execution_mode"])
            self.assertEqual("writable-isolated-runner-required", execution["runtime"]["allowed_tools"])
            self.assertFalse(readiness["ready_for_behavioral_execution"])
            self.assertFalse(readiness["default_read_only_runner_compatible"])
            self.assertIn("writable task requires", readiness["blocker"])
            self.assertEqual("writable", judge["execution_requirements"]["mode"])
            self.assertFalse(judge["execution_requirements"]["default_read_only_adapter_compatible"])

    def test_repository_bootstrap_contract_names_mandatory_router_reads(self):
        repo_root = Path(__file__).resolve().parents[1]
        agents = (repo_root / "AGENTS.md").read_text(encoding="utf-8")
        handbook = (repo_root / "Dokumentation" / "Skill-Handbuch.md").read_text(encoding="utf-8")
        workflow = (repo_root / "Workflows" / "Architekturentscheidung-und-Tradeoff.md").read_text(encoding="utf-8")
        visual_runtime = (
            repo_root / "Dokumentationserstellung" / "Visuelle-Antworten-und-HTML-Artefakte.md"
        ).read_text(encoding="utf-8")

        for required in (
            "Dokumentation/Skill-Handbuch.md",
            "skill-catalog.yml",
            "routing-overlays.yml",
        ):
            self.assertIn(required, agents)

        self.assertIn("verbindlicher Bootstrap-Read-Vertrag", agents)
        self.assertIn("im aktuellen Lauf tatsächlich öffnen", agents)
        self.assertIn("Workflow einen Skill ausdrücklich als **Kern**", agents)
        self.assertIn("Skill-Handbuch öffnen", handbook)
        self.assertIn("routing-overlays.yml öffnen", handbook)
        self.assertIn("architecture-tradeoff-analysis", workflow)
        self.assertIn("verpflichtend zu prüfende Kernkandidat", workflow)
        self.assertNotIn("HTML wurde in allen drei Fällen bevorzugt", visual_runtime)

    def test_outcome_primary_does_not_turn_missing_skill_read_into_hard_fail(self):
        trace = default_trace()
        trace["observability"]["skill_file_reads"] = True
        base = {
            "required_skills": ["example"],
            "forbidden_skills": [],
            "expected_workflow": {"mode": "none", "allowed": []},
        }

        outcome = dict(base, routing_evaluation={"mode": "outcome-primary"})
        discovery = dict(base, routing_evaluation={"mode": "discovery-required"})

        outcome_gates = evaluate_gates(outcome, trace, default_actions(), default_evidence())
        discovery_gates = evaluate_gates(discovery, trace, default_actions(), default_evidence())

        self.assertTrue(outcome_gates["gates"]["required_skill_read"])
        self.assertFalse(discovery_gates["gates"]["required_skill_read"])
        self.assertEqual("outcome-primary", outcome_gates["routing_evaluation_mode"])
        self.assertEqual("discovery-required", discovery_gates["routing_evaluation_mode"])

    def test_workspace_tamper_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self._repo(Path(tmp) / "repo")
            out = Path(tmp) / "prepared"
            prepare(self._task(root), root, "abc123", out)
            target = out / "runner-package" / "workspace" / "repository" / "AGENTS.md"
            target.write_text("# tampered\n", encoding="utf-8")
            with self.assertRaisesRegex(HarnessError, "runner workspace artifact hash mismatch"):
                verify_prepared_integrity(out)

    def test_claude_trace_records_observed_skill_and_workflow_reads(self):
        with tempfile.TemporaryDirectory() as tmp:
            task = Path(tmp)
            skill = task / "workspace" / "repository" / "Recherche" / "Skills" / "research-synthesis" / "SKILL.md"
            skill.parent.mkdir(parents=True)
            skill.write_text(
                "---\nname: research-synthesis\ndescription: Verwenden bei mehreren Quellen; nicht für Einzelclaims.\n---\n",
                encoding="utf-8",
            )
            workflow = task / "workspace" / "repository" / "Workflows" / "Deep-Research.md"
            workflow.parent.mkdir(parents=True)
            workflow.write_text("# Deep Research\n", encoding="utf-8")

            reads = [
                {"target": "workspace/repository/Recherche/Skills/research-synthesis/SKILL.md", "timestamp": "2026-10-06T16:00:00Z"},
                {"target": "workspace/repository/Workflows/Deep-Research.md", "timestamp": "2026-10-06T16:00:01Z"},
            ]
            trace = claude_adapter._trace({"runtime": {}}, reads, task, False, "2026-10-06T16:00:02Z")
            self.assertEqual(["research-synthesis"], [x["skill_id"] for x in trace["skill_events"]])
            self.assertEqual(["Workflows/Deep-Research.md"], [x["workflow"] for x in trace["workflow_events"]])
            self.assertEqual("unknown", trace["observability"]["skill_selected"])
            self.assertEqual("unknown", trace["observability"]["skill_applied"])


if __name__ == "__main__":
    unittest.main()
