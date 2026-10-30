"""Derived routing text keeps canonical provenance; no fake retrieval claim.

Real temporary Git sources are reused by composition. The injected worker only
observes corpus bytes and returns controlled hashes, not a simulated BM25 score.
"""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import shutil
import unittest

from tests import test_rule_search_routing as routing_fixture
from tools import search_rules
from tools.check_public_entrypoints import MAX_PROJECT_BYTES, MAX_PROJECT_FILE_BYTES


def sha(body):
    return hashlib.sha256(body).hexdigest()


@unittest.skipUnless(shutil.which("git"), "Git is required for routing facet tests")
class RuleRoutingFacetTests(unittest.TestCase):
    def setUp(self):
        self.fixture = routing_fixture.RuleRoutingTests("runTest")
        self.addCleanup(self.fixture.doCleanups)
        self.fixture.setUp()
        self.root = self.fixture.root
        self.catalog = copy.deepcopy(self.fixture.catalog)
        self.path = self.catalog["skills"][0]["path"]
        self.marker = "fixturecatalogfacetmarker937"
        self.catalog["skills"][0]["purpose"] = self.marker + " exists only in catalog purpose."
        self.commit_catalog(self.catalog, "distinct catalog-only facet")
        self.calls = []
        self.corpus = {}
        self.return_canonical_worker_hash = False

    def commit_catalog(self, catalog, message):
        self.fixture.write("skill-catalog.yml", self.fixture.yaml_bytes(catalog))
        self.fixture.commit(message)

    def worker(self, node, request):
        self.assertEqual(node, "fixture-node")
        self.calls.append(dict(request))
        corpus = Path(request["corpus"])
        actual = {path.relative_to(corpus).as_posix(): path.read_bytes()
                  for path in corpus.rglob("*") if path.is_file()}
        self.assertEqual(set(actual), set(request["paths"]))
        if request["action"] == "build":
            self.corpus = actual
            Path(request["db"]).touch()
            return {"paths": sorted(actual), "skipped": 0}
        self.assertEqual(request["action"], "search")
        body = self.fixture.routing_files[self.path] if self.return_canonical_worker_hash else actual[self.path]
        return {"hits": [{"path": self.path, "score": 0.8, "snippet": self.marker,
                          "content_sha256": sha(body)}]}

    def build(self):
        return search_rules.build(self.root, node="fixture-node", worker=self.worker, routing=True)

    def search(self):
        return search_rules.search(self.root, self.marker, node="fixture-node", worker=self.worker, routing=True)

    def test_catalog_only_text_is_in_corpus_with_original_prefix_and_distinct_hashes(self):
        metadata, original = search_rules.read_snapshot(self.root, routing=True)
        self.assertEqual(original, self.fixture.routing_files)
        self.assertNotIn(self.marker.encode(), original[self.path])
        built = self.build()
        self.assertEqual(built["documents"], len(original))
        self.assertEqual(metadata["routing_format"], 2)
        self.assertEqual(metadata["files"], {path: sha(body) for path, body in original.items()})
        self.assertEqual(metadata["skills"], self.fixture.skills)
        self.assertEqual(metadata["routing_facets"], {
            item["path"]: {key: item[key] for key in ("id", "area", "purpose")}
            for item in self.catalog["skills"]})
        self.assertEqual(metadata["search_documents"], {
            path: sha(body) for path, body in self.corpus.items()})
        for item in self.catalog["skills"]:
            path = item["path"]
            self.assertTrue(self.corpus[path].startswith(original[path]))
            for key in ("id", "area", "purpose"):
                self.assertIn(item[key].encode("utf-8"), self.corpus[path])
            self.assertNotEqual(metadata["files"][path], metadata["search_documents"][path])
        for path in set(original) - set(self.fixture.skills):
            self.assertEqual(self.corpus[path], original[path])
        self.assertEqual((self.root / self.path).read_bytes(), original[self.path])

    def test_invalid_area_or_purpose_is_rejected_before_worker(self):
        for key, value in (("area", None), ("area", "  "), ("area", []),
                           ("purpose", None), ("purpose", "  "), ("purpose", "short"),
                           ("purpose", ["not a string"])):
            with self.subTest(key=key, value=value):
                catalog = copy.deepcopy(self.catalog)
                catalog["skills"][0][key] = value
                self.commit_catalog(catalog, "invalid routing facet")
                with self.assertRaises(search_rules.SearchError) as raised:
                    self.build()
                self.assertIn("facet", str(raised.exception).lower())
                self.assertEqual(self.calls, [])

    def test_purpose_only_edit_makes_index_stale_without_a_worker_call(self):
        self.build()
        before_calls = len(self.calls)
        original = (self.root / self.path).read_bytes()
        changed = copy.deepcopy(self.catalog)
        changed["skills"][0]["purpose"] = "Changed catalog-only purpose for the same canonical skill."
        self.fixture.write("skill-catalog.yml", self.fixture.yaml_bytes(changed))
        with self.assertRaises(search_rules.SearchError) as raised:
            self.search()
        self.assertEqual(raised.exception.status, "stale")
        self.assertEqual(len(self.calls), before_calls)
        self.assertEqual((self.root / self.path).read_bytes(), original)

    def test_worker_cannot_substitute_canonical_hash_for_derived_document_hash(self):
        self.build()
        self.assertNotEqual(sha(self.corpus[self.path]), sha(self.fixture.routing_files[self.path]))
        self.return_canonical_worker_hash = True
        with self.assertRaises(search_rules.SearchError) as raised:
            self.search()
        self.assertIn("content", str(raised.exception).lower())
        self.assertEqual([call["action"] for call in self.calls], ["build", "search"])

    def test_public_hit_separates_canonical_source_from_derived_snippet(self):
        self.build()
        hit = self.search()["hits"][0]
        self.assertEqual(hit["path"], self.path)
        self.assertEqual(hit["content_sha256"], sha(self.fixture.routing_files[self.path]))
        self.assertEqual(hit["search_document_sha256"], sha(self.corpus[self.path]))
        self.assertNotEqual(hit["content_sha256"], hit["search_document_sha256"])
        self.assertEqual(hit["snippet_origin"], "derived-search-document")
        self.assertEqual(hit["snippet"], self.marker)
        sources = {source["path"]: source for source in hit["sources"]}
        self.assertEqual(sources[self.path]["sha256"], hit["content_sha256"])
        self.assertEqual(sources["skill-catalog.yml"]["sha256"],
                         sha((self.root / "skill-catalog.yml").read_bytes()))
        catalog_reference = json.dumps(sources["skill-catalog.yml"])
        self.assertIn("purpose", catalog_reference)
        self.assertIn(self.catalog["skills"][0]["id"], catalog_reference)

    def test_actual_derived_file_and_total_budgets_are_checked_before_worker(self):
        catalog = copy.deepcopy(self.catalog)
        catalog["skills"][0]["purpose"] = "x" * MAX_PROJECT_FILE_BYTES
        self.commit_catalog(catalog, "derived file exceeds budget")
        self.assertLess(sum(map(len, self.fixture.routing_files.values())), MAX_PROJECT_BYTES)
        self.assertTrue(all(len(body) < MAX_PROJECT_FILE_BYTES
                            for body in self.fixture.routing_files.values()))
        with self.assertRaises(search_rules.SearchError) as raised:
            self.build()
        self.assertIn("256 KiB", str(raised.exception))
        self.assertEqual(self.calls, [])

        catalog = copy.deepcopy(self.catalog)
        for number in range(3):
            identifier = f"budget-{number}"
            path = f"Budget/Skills/{identifier}/SKILL.md"
            self.fixture.write(path, self.fixture.skill_body(identifier, "Synthetic budget-only skill."))
            catalog["skills"].append({**catalog["skills"][0], "id": identifier,
                                      "area": "Budget", "path": path})
        for item in catalog["skills"]:
            item["purpose"] = "x" * (220 * 1024)
        self.commit_catalog(catalog, "derived corpus exceeds total budget")
        with self.assertRaises(search_rules.SearchError) as raised:
            self.build()
        self.assertIn("1 MiB", str(raised.exception))
        self.assertEqual(self.calls, [])


if __name__ == "__main__":
    unittest.main()
