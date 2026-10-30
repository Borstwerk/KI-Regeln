"""Routing-controller contracts, using two synthetic skills and real temporary Git.

The fake worker checks exported bytes, not QMD quality. Full catalog indexing is
not full semantic recall; neither ranked candidates nor empty hits choose an owner.
"""
from __future__ import annotations

import copy
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
from unittest.mock import patch

import yaml

from tools import search_rules
from tools.check_public_entrypoints import PROJECT_CORE, ROOT


@unittest.skipUnless(shutil.which("git"), "Git is required for routing snapshot tests")
class RuleRoutingTests(unittest.TestCase):
    def setUp(self):
        temporary = ROOT / ".validation" / "tmp"
        temporary.mkdir(parents=True, exist_ok=True)
        self.tmp = tempfile.TemporaryDirectory(prefix="rule-routing-test-", dir=temporary)
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        environment = {
            **{key: value for key, value in os.environ.items() if not key.startswith("GIT_")},
            "GIT_CONFIG_NOSYSTEM": "1", "GIT_CONFIG_GLOBAL": os.devnull,
            "GIT_TERMINAL_PROMPT": "0",
        }
        clean_git = patch.dict(os.environ, environment, clear=True)
        clean_git.start()
        self.addCleanup(clean_git.stop)
        self.git("init", "--quiet", "--object-format=sha1")
        self.git("config", "core.autocrlf", "false")
        self.git("config", "user.name", "Routing Fixture")
        self.git("config", "user.email", "fixture@example.invalid")
        self.content_files = {name: f"# Synthetic guide {name}\n".encode()
                              for name in sorted(PROJECT_CORE)}
        self.skills = {
            "Analysis/Skills/scope-review/SKILL.md": {
                "id": "scope-review", "description": "Prüft den konkreten Scope einer Änderung.",
                "maturity": "experimental", "eval_coverage": "partial",
            },
            "Quality/Skills/spec-cases/SKILL.md": {
                "id": "spec-cases", "description": "Entwirft Fälle mit fachlichem Erwartungswert.",
                "maturity": "candidate", "eval_coverage": "none",
            },
        }
        self.routing_files = {**self.content_files, "Workflows/README.md": b"# Workflow navigation\n"}
        for path, skill in self.skills.items():
            self.routing_files[path] = self.skill_body(skill["id"], skill["description"])
        for path, body in self.routing_files.items():
            self.write(path, body)
        self.catalog = {"schema_version": 2, "skills": [
            {"id": skill["id"], "path": path, "area": path.split("/")[0],
             "purpose": "Catalog summary deliberately differs from canonical description.",
             "maturity": skill["maturity"], "eval_coverage": skill["eval_coverage"]}
            for path, skill in self.skills.items()
        ]}
        self.dependencies = {
            "skill-catalog.yml": self.yaml_bytes(self.catalog),
            "workflow-index.yml": self.yaml_bytes({
                "schema_version": 1, "workflows": ["Workflows/Synthetic-review.md"]}),
            "routing-overlays.yml": self.yaml_bytes({"schema_version": 2, "overlays": [{
                "skill": "scope-review", "phase": "assurance", "checkpoints": ["pre-completion"]}]}),
        }
        for path, body in self.dependencies.items():
            self.write(path, body)
        self.manifest = json.dumps({
            "schema_version": 1, "id": "ki-regeln", "kind": "collection",
            "entrypoints": {"overview": "PROJECT.md", "contents": "START-HIER.md",
                            "status": "README.md", "plan": "CONTRIBUTING.md"},
            "search": {"include": sorted(self.content_files), "exclude": []},
        }).encode()
        self.write("mara-project.json", self.manifest)
        self.write("Workflows/Synthetic-review.md", b"# Referenced workflow, not an indexed skill\n")
        self.write(".gitignore", b".validation/\n")
        self.commit("synthetic routing baseline")
        self.requests = []

    @staticmethod
    def yaml_bytes(value):
        return yaml.safe_dump(value, sort_keys=False, allow_unicode=True).encode("utf-8")

    @staticmethod
    def skill_body(identifier, description):
        return ("---\n" + yaml.safe_dump({"name": identifier, "description": description},
                                       sort_keys=False, allow_unicode=True)
                + "---\n\n# Canonical skill\nFull operational text.\n").encode("utf-8")

    def git(self, *arguments):
        process = subprocess.run(["git", *arguments], cwd=self.root, capture_output=True, timeout=20)
        self.assertEqual(process.returncode, 0, process.stderr.decode(errors="replace"))
        return process.stdout

    def write(self, name, body):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(body)

    def commit(self, message):
        self.git("add", "--all")
        self.git("commit", "--quiet", "--message", message)

    def worker(self, expected, hits=None):
        def execute(node, request):
            self.assertEqual(node, "fixture-node")
            self.requests.append(dict(request))
            self.assertEqual(request["paths"], sorted(expected))
            corpus = Path(request["corpus"])
            actual = {path.relative_to(corpus).as_posix(): path.read_bytes()
                      for path in corpus.rglob("*") if path.is_file()}
            self.assertEqual(actual, expected)
            if request["action"] == "build":
                Path(request["db"]).touch()
                return {"paths": sorted(actual), "skipped": 0}
            self.assertEqual(request["action"], "search")
            paths = list(self.skills) if hits is None else hits
            return {"hits": [{"path": path, "score": 0.8, "snippet": "Synthetic match",
                              "content_sha256": hashlib.sha256(expected[path]).hexdigest()}
                             for path in paths]}
        return execute

    def build(self, routing=True):
        expected = self.routing_files if routing else self.content_files
        return search_rules.build(self.root, node="fixture-node", worker=self.worker(expected), routing=routing)

    def search(self, *, hits=None, routing=True):
        expected = self.routing_files if routing else self.content_files
        if not routing and hits is None:
            hits = ["README.md"]
        return search_rules.search(self.root, "Prüfauftrag", node="fixture-node",
                                   worker=self.worker(expected, hits), routing=routing)

    def rejected_before_worker(self):
        calls = len(self.requests)
        with self.assertRaises(search_rules.SearchError):
            self.build()
        self.assertEqual(len(self.requests), calls)

    def assert_stale_without_worker(self):
        calls = len(self.requests)
        self.assertEqual(search_rules.status(self.root, routing=True)["status"], "stale")
        with self.assertRaises(search_rules.SearchError):
            self.search()
        self.assertEqual(len(self.requests), calls)

    def test_snapshot_includes_every_catalog_skill_and_its_canonical_description(self):
        metadata, files = search_rules.read_snapshot(self.root, routing=True)
        self.assertEqual(files, self.routing_files)
        self.assertEqual(metadata["skills"], self.skills)
        self.assertEqual(metadata["routing_coverage"], {"skills": 2, "indexed_skills": 2})
        self.assertEqual(metadata["files"], {
            path: hashlib.sha256(body).hexdigest() for path, body in self.routing_files.items()})
        self.assertEqual(metadata["routing_dependencies"], {
            path: hashlib.sha256(body).hexdigest() for path, body in self.dependencies.items()})
        self.assertNotIn("Workflows/Synthetic-review.md", files)
        self.assertTrue(set(self.dependencies).isdisjoint(files))
        _, content = search_rules.read_snapshot(self.root)
        self.assertEqual(content, self.content_files)
        self.assertEqual((self.root / "mara-project.json").read_bytes(), self.manifest)

    def test_skill_hits_are_enriched_candidates_and_routing_limit_is_ten(self):
        self.build()
        paths = [*self.skills, *sorted(set(self.routing_files) - set(self.skills))]
        result = self.search(hits=paths[:10])
        self.assertEqual(len(result["hits"]), 10)
        self.assertEqual(self.requests[-1]["limit"], 10)
        self.assertIs(result["candidates_only"], True)
        self.assertEqual(result["routing_coverage"], {"skills": 2, "indexed_skills": 2})
        self.assertEqual(result["routing_sources"], {
            "master": "Dokumentation/Skill-Handbuch.md", "catalog": "skill-catalog.yml",
            "overlays": "routing-overlays.yml", "workflows": "workflow-index.yml"})
        for hit in result["hits"]:
            if hit["path"] in self.skills:
                self.assertEqual(hit["kind"], "skill")
                self.assertEqual(hit["skill"], self.skills[hit["path"]])
        with self.assertRaises(search_rules.SearchError):
            self.search(hits=paths[:11])

    def test_content_and_routing_caches_are_isolated_and_content_stays_unchanged(self):
        self.build(routing=False)
        content_db = Path(self.requests[-1]["db"])
        before = {path.relative_to(content_db.parent): path.read_bytes()
                  for path in content_db.parent.rglob("*") if path.is_file()}
        content_status = search_rules.status(self.root)
        self.build()
        self.assertNotEqual(Path(self.requests[-1]["db"]), content_db)
        self.search()
        self.assertEqual(search_rules.status(self.root), content_status)
        self.assertEqual(self.search(routing=False)["hits"][0]["path"], "README.md")
        after = {path.relative_to(content_db.parent): path.read_bytes()
                 for path in content_db.parent.rglob("*") if path.is_file()}
        self.assertEqual(after, before)
        self.assertEqual((self.root / "mara-project.json").read_bytes(), self.manifest)

    def test_invalid_canonical_name_or_description_blocks_before_worker(self):
        path = next(iter(self.skills))
        for body in (self.skill_body("another-name", "Description"),
                     self.skill_body("scope-review", "   "), b"# No frontmatter\n"):
            with self.subTest(body=body):
                self.write(path, body)
                self.commit("invalid canonical descriptor")
                self.rejected_before_worker()

    def test_missing_catalog_skill_file_blocks_before_worker(self):
        (self.root / next(iter(self.skills))).unlink()
        self.commit("remove catalogued skill file")
        self.rejected_before_worker()

    def test_duplicate_ids_and_casefolded_path_aliases_block_before_worker(self):
        for identifier, path in (
            ("scope-review", "Other/Skills/scope-review/SKILL.md"),
            ("SCOPE-REVIEW", "OtherUpper/Skills/SCOPE-REVIEW/SKILL.md"),
            ("scope-review", "Analysis/Skills/scope-review/SKILL.md"),
            ("scope-review", "analysis/Skills/scope-review/SKILL.md"),
        ):
            with self.subTest(identifier=identifier, path=path):
                catalog = copy.deepcopy(self.catalog)
                catalog["skills"].append({**catalog["skills"][0], "id": identifier, "path": path})
                if path.startswith(("Other/", "OtherUpper/")):
                    self.write(path, self.skill_body(identifier, "Duplicate identity"))
                self.write("skill-catalog.yml", self.yaml_bytes(catalog))
                self.commit("duplicate skill identity or path")
                self.rejected_before_worker()

    def test_unknown_overlay_skill_blocks_before_worker(self):
        self.write("routing-overlays.yml", self.yaml_bytes({
            "schema_version": 2, "overlays": [{"skill": "missing-owner"}]}))
        self.commit("unknown overlay owner")
        self.rejected_before_worker()

    def test_noncanonical_catalog_id_blocks_without_duplicate_identity_or_path(self):
        catalog = copy.deepcopy(self.catalog)
        path = "OtherUpper/Skills/UNIQUE-ID/SKILL.md"
        catalog["skills"].append({**catalog["skills"][0], "id": "UNIQUE-ID", "path": path})
        self.write(path, self.skill_body("UNIQUE-ID", "Invalid identifier format"))
        self.write("skill-catalog.yml", self.yaml_bytes(catalog))
        self.commit("isolated invalid catalog identifier")
        self.rejected_before_worker()

    def test_uncommitted_changes_to_each_yaml_dependency_make_routing_stale(self):
        self.build()
        for path, original in self.dependencies.items():
            with self.subTest(path=path):
                self.write(path, original + b"\n# uncommitted dependency change\n")
                try:
                    self.assert_stale_without_worker()
                finally:
                    self.write(path, original)
                self.assertEqual(search_rules.status(self.root, routing=True)["status"], "ready")

    def test_committed_changes_to_each_yaml_dependency_make_routing_stale(self):
        for path, original in self.dependencies.items():
            with self.subTest(path=path):
                self.build()
                self.write(path, original + b"\n# committed dependency change\n")
                self.commit("change routing dependency")
                self.assert_stale_without_worker()

    def test_missing_yaml_dependencies_block_before_worker(self):
        for path, original in self.dependencies.items():
            with self.subTest(path=path):
                (self.root / path).unlink()
                self.commit("remove routing dependency")
                self.rejected_before_worker()
                self.write(path, original)
                self.commit("restore routing dependency")

    def test_empty_hits_remain_candidates_only_without_an_owner_decision(self):
        self.build()
        result = self.search(hits=[])
        self.assertEqual(result["hits"], [])
        self.assertIs(result["candidates_only"], True)
        self.assertEqual(set(result["routing_sources"]), {"master", "catalog", "overlays", "workflows"})
        self.assertNotIn("owner", result)


if __name__ == "__main__":
    unittest.main()
