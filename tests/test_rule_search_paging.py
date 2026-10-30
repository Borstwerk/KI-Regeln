"""P2 paging and descriptor contracts; real Git sources, controlled worker only."""
from __future__ import annotations

import copy
from contextlib import ExitStack
import hashlib
import io
import json
from pathlib import Path
import shutil
import unittest
from unittest.mock import patch

from tests import test_rule_search_routing as routing_fixture
from tools import search_rules


def sha(body):
    return hashlib.sha256(body).hexdigest()


@unittest.skipUnless(shutil.which('git'), 'Git is required for paging snapshot tests')
class RuleSearchPagingTests(unittest.TestCase):
    def setUp(self):
        self.fixture = routing_fixture.RuleRoutingTests('runTest')
        self.addCleanup(self.fixture.doCleanups)
        self.fixture.setUp()
        self.root = self.fixture.root
        self.catalog = copy.deepcopy(self.fixture.catalog)
        self.original = dict(self.fixture.routing_files)
        self.catalog['skills'][0]['capabilities'] = ['repository-read']
        self.catalog['skills'][0]['related'] = ['spec-cases']
        for identifier in ('alpha-check', 'beta-check', 'omega-check'):
            path = f'Fixture/Skills/{identifier}/SKILL.md'
            body = self.fixture.skill_body(identifier, f'Canonical description for {identifier}.')
            self.fixture.write(path, body)
            self.original[path] = body
            self.catalog['skills'].append({
                'id': identifier, 'area': 'Fixture', 'path': path,
                'purpose': f'Catalog purpose for the synthetic {identifier} skill.',
                'maturity': 'experimental', 'eval_coverage': 'none',
            })
        self.write_catalog(self.catalog, 'five synthetic canonical skills')
        self.calls = []
        self.empty = False
        self.bad_path = None
        self.duplicate = False
        self.score_drift = False
        # Input arrives reversed, with intentional ties; the expected global
        # order follows the public score/path contract, not a production helper.
        self.scores = {path: (0.6, 0.9, 0.6, 1.0)[number % 4]
                       for number, path in enumerate(sorted(self.original))}
        self.expected = sorted(self.original, key=lambda path: (-self.scores[path], path))

    def write_catalog(self, catalog, message):
        self.fixture.write('skill-catalog.yml', self.fixture.yaml_bytes(catalog))
        self.fixture.commit(message)

    def worker(self, node, request):
        self.assertEqual(node, 'fixture-node')
        self.calls.append(dict(request))
        corpus = Path(request['corpus'])
        actual = {path.relative_to(corpus).as_posix(): path.read_bytes()
                  for path in corpus.rglob('*') if path.is_file()}
        self.assertEqual(set(actual), set(self.original))
        self.assertEqual(request['paths'], sorted(self.original))
        if request['action'] == 'build':
            Path(request['db']).touch()
            return {'paths': sorted(actual), 'skipped': 0}
        self.assertEqual(request['action'], 'search')
        self.assertEqual(request['limit'], len(self.original))
        rows = [] if self.empty else [
            {'path': path, 'score': self.scores[path] + (0.01 if self.score_drift else 0),
             'snippet': 'Controlled corpus match',
             'content_sha256': '0' * 64 if path == self.bad_path else sha(actual[path])}
            for path in reversed(sorted(actual))]
        if self.duplicate:
            rows[-1] = dict(rows[0])  # Same count: only uniqueness validation can reject it.
        return {'hits': rows}

    def build(self):
        return search_rules.build(self.root, node='fixture-node', worker=self.worker, routing=True)

    def search(self, query='shared fixture term', **kwargs):
        return search_rules.search(self.root, query, node='fixture-node', worker=self.worker,
                                   routing=True, **kwargs)

    def assert_cursor_error(self, action):
        with self.assertRaises(search_rules.SearchError) as raised:
            action()
        self.assertEqual(raised.exception.status, 'invalid-cursor')

    def no_runtime(self):
        stack = ExitStack()
        for name in ('resolve_node', 'call_worker', 'build', 'search'):
            stack.enter_context(patch.object(search_rules, name, side_effect=AssertionError(
                'Descriptor listing must not reach a Node/QMD path')))
        return stack

    def test_global_order_and_complete_nonoverlapping_pages_beyond_ten(self):
        self.build()
        page = self.search(limit=4)
        paths, offsets = [], []
        while True:
            self.assertEqual(page['total_matches'], 15)
            self.assertEqual(page['page_size'], 4)
            offsets.append(page['offset'])
            paths.extend(hit['path'] for hit in page['hits'])
            self.assertEqual(page['has_more'], page['next_cursor'] is not None)
            if not page['has_more']:
                break
            # Omitted size must retain the size selected on the first page.
            page = self.search(cursor=page['next_cursor'])
        self.assertEqual(paths, self.expected)
        self.assertEqual(len(set(paths)), len(self.original))
        self.assertEqual(offsets, [0, 4, 8, 12])
        self.assertEqual(len(page['hits']), 3)
        self.assertIsNone(page['next_cursor'])

    def test_offpage_bad_hash_and_same_length_duplicates_are_rejected(self):
        self.build()
        self.bad_path = self.expected[-1]
        with self.assertRaises(search_rules.SearchError) as raised:
            self.search(limit=1)
        self.assertIn('content', str(raised.exception).lower())
        self.bad_path = None
        self.duplicate = True
        with self.assertRaises(search_rules.SearchError):
            self.search(limit=1)

    def test_size_boundaries_empty_results_and_nonrouting_options(self):
        self.build()
        self.assertEqual(len(self.search()['hits']), 10)
        self.assertEqual(len(self.search(limit=1)['hits']), 1)
        self.assertEqual(len(self.search(limit=50)['hits']), 15)
        for value in (0, -1, 51, True, 1.5, '2'):
            with self.subTest(limit=value):
                with self.assertRaises(search_rules.SearchError):
                    self.search(limit=value)
        for options in ({'limit': 5}, {'cursor': 'not-a-cursor'}):
            with self.subTest(options=options):
                with self.assertRaises(search_rules.SearchError):
                    search_rules.search(self.root, 'term', node='fixture-node',
                                        worker=self.worker, **options)
        self.empty = True
        page = self.search()
        self.assertEqual(page['hits'], [])
        self.assertEqual(page['total_matches'], 0)
        self.assertEqual(page['offset'], 0)
        self.assertFalse(page['has_more'])
        self.assertIsNone(page['next_cursor'])

    def test_cursor_rejects_changed_query_size_corruption_and_result_set(self):
        self.build()
        cursor = self.search(limit=4)['next_cursor']
        calls = len(self.calls)
        for action in (lambda: self.search(query='different query', cursor=cursor),
                       lambda: self.search(limit=3, cursor=cursor),
                       lambda: self.search(cursor='!broken!'),
                       lambda: self.search(cursor=cursor + 'x'),
                       lambda: self.search(cursor='')):
            with self.subTest(action=action):
                self.assert_cursor_error(action)
        self.assertEqual(len(self.calls), calls)
        self.score_drift = True
        self.assert_cursor_error(lambda: self.search(cursor=cursor))
        self.assertEqual(len(self.calls), calls + 1)

    def test_search_source_change_blocks_cursor_before_worker(self):
        self.build()
        cursor = self.search(limit=4)['next_cursor']
        before = len(self.calls)
        self.fixture.write('README.md', self.original['README.md'] + b'\nChanged source\n')
        self.fixture.commit('source changes between result pages')
        with self.assertRaises(search_rules.SearchError) as raised:
            self.search(cursor=cursor)
        self.assertEqual(raised.exception.status, 'stale')
        self.assertEqual(len(self.calls), before)

    def test_all_descriptors_preserve_metadata_sources_without_node_or_index(self):
        self.assertFalse((self.root / '.validation/rule-routing/current.json').exists())
        descriptors = []
        with self.no_runtime():
            page = search_rules.list_skills(self.root, limit=2)
            while True:
                self.assertEqual(page['mode'], 'catalog')
                self.assertEqual(page['total_skills'], 5)
                self.assertEqual(page['page_size'], 2)
                self.assertIs(page['assessment_performed'], False)
                self.assertIs(page['candidates_only'], True)
                descriptors.extend(page['skills'])
                if not page['has_more']:
                    self.assertIsNone(page['next_cursor'])
                    break
                page = search_rules.list_skills(self.root, cursor=page['next_cursor'])
        self.assertEqual([item['id'] for item in descriptors], sorted(item['id'] for item in self.catalog['skills']))
        self.assertEqual(len({item['id'] for item in descriptors}), 5)
        entries = {item['id']: item for item in self.catalog['skills']}
        catalog_hash = sha((self.root / 'skill-catalog.yml').read_bytes())
        for item in descriptors:
            entry = entries[item['id']]
            for field in ('path', 'area', 'purpose', 'maturity', 'eval_coverage'):
                self.assertEqual(item[field], entry[field])
            self.assertEqual(item['capabilities'], entry.get('capabilities', []))
            self.assertEqual(item['related'], entry.get('related', []))
            self.assertEqual(item['content_sha256'], sha(self.original[entry['path']]))
            self.assertIn('Canonical description' if entry['area'] == 'Fixture' else
                          self.fixture.skills[entry['path']]['description'], item['description'])
            sources = {source['path']: source for source in item['sources']}
            self.assertEqual(sources[entry['path']]['sha256'], item['content_sha256'])
            self.assertEqual(sources['skill-catalog.yml']['sha256'], catalog_hash)
            catalog_reference = json.dumps(sources['skill-catalog.yml'])
            self.assertIn(item['id'], catalog_reference)
            self.assertIn('purpose', catalog_reference)
        self.assertFalse((self.root / '.validation/rule-routing/current.json').exists())

    def test_descriptor_cursors_bind_action_size_and_snapshot(self):
        self.build()
        descriptor_cursor = search_rules.list_skills(self.root, limit=2)['next_cursor']
        search_cursor = self.search(limit=2)['next_cursor']
        before = len(self.calls)
        self.assert_cursor_error(lambda: self.search(cursor=descriptor_cursor))
        self.assert_cursor_error(lambda: search_rules.list_skills(self.root, cursor=search_cursor))
        self.assert_cursor_error(lambda: search_rules.list_skills(self.root, limit=3, cursor=descriptor_cursor))
        self.assertEqual(len(self.calls), before)
        catalog = copy.deepcopy(self.catalog)
        catalog['skills'][0]['purpose'] = 'Changed canonical catalog purpose between descriptor pages.'
        self.write_catalog(catalog, 'change descriptor source')
        with self.assertRaises(search_rules.SearchError) as raised:
            search_rules.list_skills(self.root, cursor=descriptor_cursor)
        self.assertIn(raised.exception.status, ('stale', 'invalid-cursor'))
        self.assertEqual(len(self.calls), before)

    def test_descriptor_limits_and_malformed_optional_lists_are_rejected(self):
        for value in (0, -1, 51, True, 1.5, '2'):
            with self.subTest(limit=value):
                with self.assertRaises(search_rules.SearchError):
                    search_rules.list_skills(self.root, limit=value)
        for field, value in (('capabilities', 'not a list'), ('capabilities', [7]),
                             ('capabilities', ['repository-read', 'repository-read']),
                             ('related', 'not a list'), ('related', [None]),
                             ('related', ['spec-cases', 'spec-cases'])):
            with self.subTest(field=field, value=value):
                catalog = copy.deepcopy(self.catalog)
                catalog['skills'][0][field] = value
                self.write_catalog(catalog, 'malformed descriptor list')
                with self.assertRaises(search_rules.SearchError):
                    search_rules.list_skills(self.root)
        self.assertEqual(self.calls, [])

    def test_python_cli_lists_descriptors_with_paging_without_node(self):
        with (self.no_runtime(), patch.object(search_rules, 'ROOT', self.root),
              patch('sys.argv', ['search_rules.py', '--routing', '--limit', '2', 'list-skills']),
              patch('sys.stdout', new_callable=io.StringIO) as output):
            code = search_rules.main()
        self.assertEqual(code, 0)
        page = json.loads(output.getvalue())
        self.assertEqual(page['total_skills'], 5)
        self.assertEqual(page['page_size'], 2)
        self.assertEqual(len(page['skills']), 2)
        self.assertTrue(page['has_more'])


if __name__ == '__main__':
    unittest.main()
