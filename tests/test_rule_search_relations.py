"""P3 controller contracts; synthetic Git sources, no simulated retrieval quality."""
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
from tools.check_public_entrypoints import MAX_PROJECT_BYTES, MAX_PROJECT_FILE_BYTES


def sha(body):
    return hashlib.sha256(body).hexdigest()


@unittest.skipUnless(shutil.which('git'), 'Git is required for relation snapshot tests')
class RuleSearchRelationTests(unittest.TestCase):
    def setUp(self):
        self.fixture = routing_fixture.RuleRoutingTests('runTest')
        self.addCleanup(self.fixture.doCleanups)
        self.fixture.setUp()
        self.root = self.fixture.root
        self.catalog = copy.deepcopy(self.fixture.catalog)
        self.catalog['skills'][0]['related'] = ['spec-cases']
        self.workflow = 'Workflows/Synthetic-review.md'
        self.workflow_body = (b'# Synthetic review\n## Skills\n'
                              b'- `scope-review` optional.\n- `spec-cases` for cases.\n'
                              b'Again `scope-review`.\n')
        self.workflow_paths = [self.workflow]
        self.overlays = {'schema_version': 2, 'overlays': [
            {'skill': 'scope-review', 'phase': 'assurance', 'checkpoints': ['pre-completion']},
            {'skill': 'spec-cases', 'phase': 'presentation', 'checkpoints': ['pre-output']},
        ]}
        self.fixture.write(self.workflow, self.workflow_body)
        self.write_catalog(self.catalog)
        self.fixture.write('routing-overlays.yml', self.fixture.yaml_bytes(self.overlays))
        self.fixture.commit('explicit relation sources')
        self.original = dict(self.fixture.routing_files)
        self.paths = [item['path'] for item in self.catalog['skills']]
        self.calls = []
        self.empty = False

    def write_catalog(self, catalog):
        self.fixture.write('skill-catalog.yml', self.fixture.yaml_bytes(catalog))

    def write_workflow_index(self):
        self.fixture.write('workflow-index.yml', self.fixture.yaml_bytes({
            'schema_version': 1, 'workflows': self.workflow_paths}))

    def worker(self, node, request):
        self.assertEqual(node, 'fixture-node')
        self.calls.append(dict(request))
        corpus = Path(request['corpus'])
        actual = {p.relative_to(corpus).as_posix(): p.read_bytes()
                  for p in corpus.rglob('*') if p.is_file()}
        self.assertEqual(set(actual), set(self.original))
        self.assertEqual(request['paths'], sorted(self.original))
        if request['action'] == 'build':
            Path(request['db']).touch()
            return {'paths': sorted(actual), 'skipped': 0}
        self.assertEqual(request['action'], 'search')
        return {'hits': [] if self.empty else [
            {'path': path, 'score': 0.9 - index / 10, 'snippet': 'Controlled source match',
             'content_sha256': sha(actual[path])} for index, path in enumerate(self.paths)]}

    def build(self):
        return search_rules.build(self.root, 'fixture-node', worker=self.worker, routing=True)

    def search(self, **kwargs):
        return search_rules.search(self.root, 'controlled query', 'fixture-node',
                                   worker=self.worker, routing=True, **kwargs)

    def no_runtime(self):
        stack = ExitStack()
        for name in ('resolve_node', 'call_worker', 'current', 'build', 'search'):
            stack.enter_context(patch.object(search_rules, name, side_effect=AssertionError(
                'Relation listing must not open Node/QMD or a ready index')))
        return stack

    def test_snapshot_binds_workflow_bytes_without_expanding_indexed_corpus(self):
        metadata, files = search_rules.read_snapshot(self.root, routing=True)
        self.assertEqual(metadata['routing_format'], 3)
        self.assertEqual(files, self.original)
        self.assertNotIn(self.workflow, files)
        self.assertEqual(metadata['files'], {p: sha(b) for p, b in self.original.items()})
        self.assertEqual(metadata['routing_dependencies'][self.workflow], sha(self.workflow_body))
        edges = metadata['routing_relations']
        pairs = {(e['type'], e['from'], e['to']) for e in edges}
        self.assertIn(('related', 'skill:scope-review', 'skill:spec-cases'), pairs)
        self.assertIn(('mentions', 'workflow:' + self.workflow, 'skill:scope-review'), pairs)
        self.assertIn(('checkpoint', 'checkpoint:pre-completion', 'skill:scope-review'), pairs)
        _, content = search_rules.read_snapshot(self.root)
        self.assertEqual(content, self.fixture.content_files)

    def test_workflow_changes_block_search_and_relation_cursor_without_worker(self):
        self.build()
        search_cursor = self.search(limit=1)['next_cursor']
        relations_cursor = search_rules.list_relations(self.root, workflow=self.workflow, limit=1)['next_cursor']
        before = len(self.calls)
        self.fixture.write(self.workflow, self.workflow_body + b'New workflow context.\n')
        for action in (lambda: self.search(cursor=search_cursor),
                       lambda: search_rules.list_relations(self.root, workflow=self.workflow, cursor=relations_cursor)):
            with self.subTest(action=action), self.assertRaises(search_rules.SearchError) as raised:
                action()
            self.assertIn(raised.exception.status, ('stale', 'invalid-cursor'))
        self.assertEqual(len(self.calls), before)
        self.fixture.commit('workflow-only source change')
        with self.assertRaises(search_rules.SearchError) as raised:
            search_rules.list_relations(self.root, workflow=self.workflow, cursor=relations_cursor)
        self.assertEqual(raised.exception.status, 'invalid-cursor')
        self.assertEqual(len(self.calls), before)

    def test_qmd_free_selectors_page_explicit_edges_with_sources_and_direction(self):
        self.assertFalse((self.root / '.validation/rule-routing/current.json').exists())
        with self.no_runtime():
            scoped = search_rules.list_relations(self.root, skill_id='scope-review')
            first = search_rules.list_relations(self.root, workflow=self.workflow, limit=1)
            second = search_rules.list_relations(self.root, workflow=self.workflow, cursor=first['next_cursor'])
            overlay = search_rules.list_relations(self.root, checkpoint='pre-completion')
        self.assertEqual(scoped['mode'], 'relations')
        self.assertIs(scoped['assessment_performed'], False)
        self.assertIs(scoped['candidates_only'], True)
        self.assertEqual(scoped['total_relations'], 2)
        self.assertEqual({e['type'] for e in scoped['relations']}, {'related', 'mentions'})
        related = next(e for e in scoped['relations'] if e['type'] == 'related')
        self.assertEqual((related['from'], related['to'], related['target_path']),
                         ('skill:scope-review', 'skill:spec-cases', self.paths[1]))
        self.assertEqual(related['source']['sha256'], sha((self.root / 'skill-catalog.yml').read_bytes()))
        self.assertIn('scope-review', related['source']['field'])
        workflow_edges = first['relations'] + second['relations']
        self.assertEqual({e['to'] for e in workflow_edges}, {'skill:scope-review', 'skill:spec-cases'})
        self.assertEqual(first['total_relations'], 2)
        self.assertTrue(first['has_more'])
        self.assertFalse(second['has_more'])
        scope = next(e for e in workflow_edges if e['to'] == 'skill:scope-review')
        self.assertEqual(scope['source']['lines'], [3, 5])
        self.assertEqual(scope['source']['sha256'], sha(self.workflow_body))
        self.assertNotIn('requires', {e['type'] for e in workflow_edges})
        self.assertEqual(overlay['relations'][0]['phase'], 'assurance')
        self.assertEqual(overlay['relations'][0]['source']['sha256'],
                         sha((self.root / 'routing-overlays.yml').read_bytes()))
        self.assertFalse((self.root / '.validation/rule-routing/current.json').exists())

    def test_search_hints_use_visible_seeds_are_bounded_and_do_not_invent_seeds(self):
        self.build()
        first = self.search(limit=1)
        hints = first['routing_hints']
        self.assertEqual(hints['total_relations'], 2)
        self.assertEqual(hints['limit'], 20)
        self.assertFalse(hints['truncated'])
        self.assertEqual({e['type'] for e in hints['items']}, {'related', 'mentions'})
        second = self.search(cursor=first['next_cursor'])
        self.assertEqual(len(second['routing_hints']['items']), 1)
        self.assertEqual(second['routing_hints']['items'][0]['to'], 'skill:spec-cases')
        self.empty = True
        empty = self.search()
        self.assertEqual(empty['hits'], [])
        self.assertEqual(empty['routing_hints']['items'], [])
        self.assertEqual(empty['routing_hints']['total_relations'], 0)
        self.empty = False
        for number in range(21):
            path = f'Workflows/Extra-{number:02d}.md'
            self.workflow_paths.append(path)
            self.fixture.write(path, b'# Extra workflow\n`scope-review` optional.\n')
        self.write_workflow_index()
        self.fixture.commit('many explicit workflow neighbors')
        self.build()
        bounded = self.search(limit=1)['routing_hints']
        self.assertEqual(bounded['total_relations'], 23)
        self.assertEqual(len(bounded['items']), 20)
        self.assertTrue(bounded['truncated'])

    def test_explicit_checkpoint_is_not_activation_and_is_cursor_bound(self):
        self.build()
        self.empty = True
        empty = self.search(checkpoint='pre-completion')
        self.assertEqual(empty['hits'], [])
        edges = empty['routing_hints']['items']
        self.assertEqual([(e['type'], e['from'], e['to']) for e in edges],
                         [('checkpoint', 'checkpoint:pre-completion', 'skill:scope-review')])
        self.assertIs(empty['candidates_only'], True)
        self.assertNotIn('activated_skills', empty)
        self.empty = False
        first = self.search(limit=1, checkpoint='pre-completion')
        before = len(self.calls)
        for options in ({}, {'checkpoint': 'pre-output'}):
            with self.subTest(options=options), self.assertRaises(search_rules.SearchError) as raised:
                self.search(cursor=first['next_cursor'], **options)
            self.assertEqual(raised.exception.status, 'invalid-cursor')
        self.assertEqual(len(self.calls), before)
        self.search(cursor=first['next_cursor'], checkpoint='pre-completion')
        self.assertEqual(len(self.calls), before + 1)

    def test_unknown_structured_targets_block_worker_and_revoke_readiness(self):
        for kind in ('related', 'overlay'):
            with self.subTest(kind=kind):
                self.write_catalog(self.catalog)
                self.fixture.write('routing-overlays.yml', self.fixture.yaml_bytes(self.overlays))
                if self.fixture.git('status', '--porcelain').strip():
                    self.fixture.commit('restore valid relations')
                self.build()
                before = len(self.calls)
                if kind == 'related':
                    bad = copy.deepcopy(self.catalog)
                    bad['skills'][0]['related'] = ['missing-owner']
                    self.write_catalog(bad)
                else:
                    bad = copy.deepcopy(self.overlays)
                    bad['overlays'][0]['skill'] = 'missing-owner'
                    self.fixture.write('routing-overlays.yml', self.fixture.yaml_bytes(bad))
                self.fixture.commit('unknown structured relation target')
                with self.assertRaises(search_rules.SearchError) as raised:
                    self.build()
                self.assertIn('missing-owner', str(raised.exception))
                self.assertEqual(len(self.calls), before)
                self.assertFalse((self.root / '.validation/rule-routing/current.json').exists())
                self.assertNotEqual(search_rules.status(self.root, routing=True)['status'], 'ready')

    def test_workflow_missing_nonregular_and_dependency_budgets_fail_before_worker(self):
        (self.root / self.workflow).unlink()
        self.fixture.commit('missing registered workflow')
        with self.assertRaises(search_rules.SearchError):
            self.build()
        self.assertEqual(self.calls, [])
        self.fixture.write(self.workflow, self.workflow_body)
        self.fixture.commit('restore workflow')
        blob = self.fixture.git('rev-parse', f'HEAD:{self.workflow}').decode().strip()
        self.fixture.git('update-index', '--cacheinfo', f'120000,{blob},{self.workflow}')
        self.fixture.git('commit', '--quiet', '-m', 'synthetic nonregular Git entry')
        with self.assertRaises(search_rules.SearchError) as raised:
            self.build()
        self.assertIn('regular', str(raised.exception).lower())
        self.assertEqual(self.calls, [])
        self.fixture.git('update-index', '--cacheinfo', f'100644,{blob},{self.workflow}')
        self.fixture.git('commit', '--quiet', '-m', 'restore regular tracked workflow')
        self.fixture.write(self.workflow, b'x' * (MAX_PROJECT_FILE_BYTES + 1))
        self.fixture.commit('workflow above file budget')
        with self.assertRaises(search_rules.SearchError) as raised:
            self.build()
        self.assertIn('256 KiB', str(raised.exception))
        self.assertEqual(self.calls, [])
        self.fixture.write(self.workflow, self.workflow_body)
        self.workflow_paths = [self.workflow]
        for number in range(5):
            path = f'Workflows/Budget-{number}.md'
            self.workflow_paths.append(path)
            self.fixture.write(path, b'x' * (220 * 1024))
        self.write_workflow_index()
        self.fixture.commit('workflow dependency total above budget')
        self.assertGreater(sum((self.root / p).stat().st_size for p in self.workflow_paths), MAX_PROJECT_BYTES)
        with self.assertRaises(search_rules.SearchError) as raised:
            self.build()
        self.assertIn('1 MiB', str(raised.exception))
        self.assertEqual(self.calls, [])

    def test_selector_validation_and_known_inventory_members_without_edges(self):
        bad = ({}, {'skill_id': 'missing-owner'}, {'workflow': 'Workflows/Missing.md'},
               {'checkpoint': 'not-a-checkpoint'}, {'skill_id': 'scope-review', 'workflow': self.workflow})
        with self.no_runtime():
            for options in bad:
                with self.subTest(options=options), self.assertRaises(search_rules.SearchError):
                    search_rules.list_relations(self.root, **options)
        catalog = copy.deepcopy(self.catalog)
        catalog['skills'][0]['related'] = []
        self.write_catalog(catalog)
        self.fixture.write(self.workflow, b'# One mention\n`scope-review`\n')
        path = 'Workflows/No-mentions.md'
        self.workflow_paths.append(path)
        self.fixture.write(path, b'# No skill mentions\n')
        self.write_workflow_index()
        self.fixture.commit('valid isolated inventory nodes')
        with self.no_runtime():
            for options in ({'skill_id': 'spec-cases'}, {'workflow': path}):
                page = search_rules.list_relations(self.root, **options)
                self.assertEqual(page['status'], 'ready')
                self.assertEqual(page['relations'], [])
                self.assertEqual(page['total_relations'], 0)
                self.assertFalse(page['has_more'])

    def test_invalid_cli_relation_combinations_stop_before_mutating_dispatch(self):
        arguments = [
            ['--routing', '--skill-id', 'scope-review', 'build'],
            ['--routing', '--workflow', self.workflow, 'status'],
            ['--routing', 'relations'],
            ['--routing', '--skill-id', 'scope-review', '--checkpoint', 'pre-completion', 'relations'],
            ['--skill-id', 'scope-review', 'relations'],
            ['--routing', '--skill-id', 'scope-review', 'search', '--', 'term'],
        ]
        for argv in arguments:
            with (self.subTest(argv=argv), patch.object(search_rules, 'ROOT', self.root),
                  patch('sys.argv', ['search_rules.py', *argv]),
                  patch.object(search_rules, 'build', side_effect=AssertionError('build reached')) as build,
                  patch.object(search_rules, 'status', side_effect=AssertionError('status reached')) as status,
                  patch.object(search_rules, 'search', side_effect=AssertionError('search reached')) as search,
                  patch('sys.stdout', new_callable=io.StringIO) as output):
                self.assertEqual(search_rules.main(), 2)
                self.assertEqual(json.loads(output.getvalue())['status'], 'error')
                build.assert_not_called(); status.assert_not_called(); search.assert_not_called()


if __name__ == '__main__':
    unittest.main()
