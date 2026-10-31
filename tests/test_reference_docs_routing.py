"""The bounded native comparison must reject unrelated source edits."""
import unittest

from Evals.Onboarding import run_reference_docs_routing as runner


class ReferenceCatalogAdmissionTests(unittest.TestCase):
    def setUp(self):
        self.before = ('skills:\n  - id: reference-docs\n    purpose: "' + runner.BEFORE +
                       '"\n    maturity: experimental\n').encode('utf-8')
        self.after = self.before.replace(runner.BEFORE.encode('utf-8'), runner.AFTER.encode('utf-8'), 1)

    def test_accepts_the_exact_declared_catalog_replacement(self):
        self.assertEqual(runner.checked_catalog_fix(self.before, self.after), self.after)

    def test_rejects_unchanged_or_additional_metadata_edits(self):
        for candidate in (self.before, self.after + b'new: field\n',
                          self.after.replace(b'experimental', b'stable')):
            with self.subTest(candidate=candidate):
                with self.assertRaises(ValueError): runner.checked_catalog_fix(self.before, candidate)

    def test_rejects_missing_or_ambiguous_baseline_text(self):
        for original in (self.after, self.before + self.before):
            with self.subTest(original=original):
                with self.assertRaises(ValueError): runner.checked_catalog_fix(original, self.after)


if __name__ == '__main__':
    unittest.main()
