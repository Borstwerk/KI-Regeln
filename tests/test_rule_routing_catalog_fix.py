"""Admission of the one explicit catalog-data repair, not a BM25 simulation."""
import copy
import json
import unittest
from unittest.mock import patch

import yaml

from Evals.Onboarding import run_rule_routing_comparison as comparison


class CatalogFixAdmissionTests(unittest.TestCase):
    def setUp(self):
        self.before = {'schema_version': 2, 'skills': [
            {'id': 'acceptance-criteria-design', 'purpose':
             'Beobachtbare Acceptance Criteria und Verification Intent für bestehende Requirements formulieren, ohne konkrete Testfälle vorwegzunehmen.',
             'maturity': 'experimental', 'related': ['test-design']},
            {'id': 'test-design', 'purpose': 'Concrete test cases.'}]}
        self.after = copy.deepcopy(self.before)
        self.after['skills'][0]['purpose'] = (
            'Beobachtbare Akzeptanzkriterien (Acceptance Criteria) und Verification Intent für bestehende Requirements formulieren, ohne konkrete Testfälle vorwegzunehmen.')

    @staticmethod
    def body(value):
        return yaml.safe_dump(value, allow_unicode=True, sort_keys=False).encode('utf-8')

    def check(self, candidate):
        return comparison.checked_catalog_fix(self.body(self.before), self.body(candidate))

    def test_accepts_only_the_declared_purpose_repair(self):
        self.assertEqual(self.check(self.after), self.body(self.after))

    def test_rejects_unchanged_or_different_purpose(self):
        with self.assertRaises(ValueError):
            self.check(self.before)
        self.after['skills'][0]['purpose'] += ' Another undeclared search term.'
        with self.assertRaises(ValueError):
            self.check(self.after)

    def test_rejects_other_fields_entries_and_missing_owner(self):
        for mutation in ('maturity', 'foreign-purpose', 'related', 'remove', 'duplicate'):
            with self.subTest(mutation=mutation):
                changed = copy.deepcopy(self.after)
                if mutation == 'maturity': changed['skills'][0]['maturity'] = 'stable'
                elif mutation == 'foreign-purpose': changed['skills'][1]['purpose'] = 'Changed other owner.'
                elif mutation == 'related': changed['skills'][0]['related'] = []
                elif mutation == 'remove': changed['skills'].pop(0)
                else: changed['skills'].append(copy.deepcopy(changed['skills'][0]))
                with self.assertRaises(ValueError): self.check(changed)

    def run_to_runtime_boundary(self, valid_pin):
        """Exercise main's order: frozen pins, declared overlay, then runtime."""
        original, repaired = self.body(self.before), self.body(self.after)
        cases = {'source_commit': comparison.SOURCE, 'cases': [
            {'id': str(i), 'phase': 'P1' if i < 16 else 'P3', 'evidence': [{'path': 'skill-catalog.yml',
             'sha256': comparison.sha(original) if valid_pin or i != 23 else '0' * 64}]}
            for i in range(24)]}
        sources = {'skill-catalog.yml': original,
                   'mara-project.json': b'{"entrypoints":{}}',
                   'workflow-index.yml': b'workflows: []',
                   'routing-overlays.yml': b'overlays: []'}

        def git(root, *args):
            if args[0] == 'rev-parse': return b'a' * 40
            if args[1].startswith('a' * 40 + ':'): return repaired
            return sources[args[1].split(':', 1)[1]]

        with (patch.object(comparison, 'CASES') as case_file,
              patch.object(comparison.sys, 'argv', ['comparison', '--run', '--label', 'candidate',
                                                   '--catalog-revision', 'declared-commit']),
              patch.object(comparison.search, 'read_snapshot', return_value=({}, {})),
              patch.object(comparison.search, 'git', side_effect=git),
              patch.object(comparison, 'checked_catalog_fix', wraps=comparison.checked_catalog_fix) as guard,
              patch.object(comparison.search, 'resolve_node', side_effect=RuntimeError('runtime boundary reached')) as resolver,
              patch.object(comparison.search, 'build') as build):
            case_file.read_bytes.return_value = json.dumps(cases).encode('utf-8')
            error = None
            try:
                comparison.main()
            except Exception as exc:
                error = exc
            return error, guard.call_args_list, resolver.call_count, build.call_count

    def test_declared_catalog_repair_preserves_original_evidence_pins(self):
        error, guard_calls, resolver_calls, build_calls = self.run_to_runtime_boundary(valid_pin=True)
        self.assertIsInstance(error, RuntimeError)
        self.assertEqual(str(error), 'runtime boundary reached')
        self.assertEqual(guard_calls, [unittest.mock.call(self.body(self.before), self.body(self.after))])
        self.assertEqual((resolver_calls, build_calls), (1, 0))

    def test_wrong_frozen_evidence_pin_stops_before_runtime(self):
        error, guard_calls, resolver_calls, build_calls = self.run_to_runtime_boundary(valid_pin=False)
        self.assertIsInstance(error, AssertionError)
        self.assertEqual(str(error), '23')
        self.assertEqual(guard_calls, [])
        self.assertEqual((resolver_calls, build_calls), (0, 0))


if __name__ == '__main__':
    unittest.main()
