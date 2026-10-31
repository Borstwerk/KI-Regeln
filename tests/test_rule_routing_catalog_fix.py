"""Admission of the one explicit catalog-data repair, not a BM25 simulation."""
import copy
import unittest

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


if __name__ == '__main__':
    unittest.main()
