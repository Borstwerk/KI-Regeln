"""Pure relationship derivation: explicit declarations, no routing activation."""
import copy
import hashlib
import json
from pathlib import Path
import unittest


def sha(body):
    return hashlib.sha256(body).hexdigest()


class RuleRelationsTests(unittest.TestCase):
    def setUp(self):
        self.catalog = {'skills': [
            {'id': 'alpha', 'path': 'Area/Skills/alpha/SKILL.md', 'related': ['beta']},
            {'id': 'beta', 'path': 'Area/Skills/beta/SKILL.md'},
            {'id': 'gamma', 'path': 'Area/Skills/gamma/SKILL.md'},
        ]}
        self.overlays = {'overlays': [{'skill': 'beta', 'phase': 'assurance',
                                      'checkpoints': ['pre-execution', 'pre-completion']}]}
        self.workflows = {
            'Workflows/A.md': (b'# A\nUse `alpha` optionally.\nThen `beta` as core in prose.\n'
                               b'Again `alpha`.\n```python\n`gamma`\n```\n~~~text\n`gamma`\n~~~\n'
                               b'Unknown `not-a-skill`.\n'),
            'Workflows/B.md': b'# B\nUse `gamma`.\n',
        }

    def hashes(self, catalog=None, overlays=None, workflows=None):
        return {'skill-catalog.yml': sha(json.dumps(catalog or self.catalog, sort_keys=True).encode()),
                'routing-overlays.yml': sha(json.dumps(overlays or self.overlays, sort_keys=True).encode()),
                **{path: sha(body) for path, body in (workflows or self.workflows).items()}}

    def derive(self, catalog=None, overlays=None, workflows=None, hashes=None):
        from tools.rule_relations import derive_relations
        catalog = self.catalog if catalog is None else catalog
        overlays = self.overlays if overlays is None else overlays
        workflows = self.workflows if workflows is None else workflows
        return derive_relations(catalog, overlays, workflows,
                                self.hashes(catalog, overlays, workflows) if hashes is None else hashes)

    def test_related_edge_preserves_direction_target_and_source(self):
        before = copy.deepcopy((self.catalog, self.overlays, self.workflows))
        related = [edge for edge in self.derive() if edge['type'] == 'related']
        self.assertEqual(related, [{
            'type': 'related', 'from': 'skill:alpha', 'to': 'skill:beta',
            'target_path': 'Area/Skills/beta/SKILL.md',
            'source': {'path': 'skill-catalog.yml', 'sha256': self.hashes()['skill-catalog.yml'],
                       'field': 'skills[alpha].related'},
        }])
        self.assertEqual((self.catalog, self.overlays, self.workflows), before)

    def test_workflow_mentions_merge_lines_skip_fences_and_never_become_requirements(self):
        self.workflows['Workflows/A.md'] += b'Escaped \\`gamma\\`.\nDouble ``gamma`` and `` `gamma` ``.\n'
        mentions = [edge for edge in self.derive() if edge['type'] == 'mentions']
        self.assertEqual([(edge['from'], edge['to']) for edge in mentions], [
            ('workflow:Workflows/A.md', 'skill:alpha'),
            ('workflow:Workflows/A.md', 'skill:beta'),
            ('workflow:Workflows/B.md', 'skill:gamma'),
        ])
        self.assertEqual(mentions[0]['source'], {
            'path': 'Workflows/A.md', 'sha256': sha(self.workflows['Workflows/A.md']), 'lines': [2, 4]})
        self.assertEqual(mentions[1]['source']['lines'], [3])
        self.assertNotIn('requires', json.dumps(mentions))

    def test_checkpoint_edges_preserve_phase_and_registry_provenance(self):
        edges = self.derive()
        checkpoints = [edge for edge in edges if edge['type'] == 'checkpoint']
        self.assertEqual([(edge['from'], edge['to'], edge['phase']) for edge in checkpoints], [
            ('checkpoint:pre-completion', 'skill:beta', 'assurance'),
            ('checkpoint:pre-execution', 'skill:beta', 'assurance'),
        ])
        for edge in checkpoints:
            self.assertEqual(edge['target_path'], 'Area/Skills/beta/SKILL.md')
            self.assertEqual(edge['source'], {'path': 'routing-overlays.yml',
                'sha256': self.hashes()['routing-overlays.yml'], 'field': 'overlays[beta].checkpoints'})
        self.assertEqual([(edge['type'], edge['from'], edge['to']) for edge in edges], [
            ('checkpoint', 'checkpoint:pre-completion', 'skill:beta'),
            ('checkpoint', 'checkpoint:pre-execution', 'skill:beta'),
            ('mentions', 'workflow:Workflows/A.md', 'skill:alpha'),
            ('mentions', 'workflow:Workflows/A.md', 'skill:beta'),
            ('mentions', 'workflow:Workflows/B.md', 'skill:gamma'),
            ('related', 'skill:alpha', 'skill:beta'),
        ])

    def test_cycles_are_declared_edges_without_reverse_or_transitive_expansion(self):
        catalog = copy.deepcopy(self.catalog)
        catalog['skills'][1]['related'] = ['gamma']
        catalog['skills'][2]['related'] = ['alpha']
        related = [edge for edge in self.derive(catalog=catalog) if edge['type'] == 'related']
        self.assertEqual([(edge['from'], edge['to']) for edge in related], [
            ('skill:alpha', 'skill:beta'), ('skill:beta', 'skill:gamma'), ('skill:gamma', 'skill:alpha')])
        self.assertEqual(len(related), 3)

    def test_duplicate_or_invalid_catalog_identities_are_rejected(self):
        from tools.rule_relations import derive_relations
        catalogs = [None, [], {'skills': []}]
        for field, value in [('id', 'Uppercase'), ('path', ''), ('id', None)]:
            catalog = copy.deepcopy(self.catalog)
            catalog['skills'][0][field] = value
            catalogs.append(catalog)
        duplicate_id = copy.deepcopy(self.catalog)
        duplicate_id['skills'].append(dict(duplicate_id['skills'][0]))
        catalogs.append(duplicate_id)
        duplicate_path = copy.deepcopy(self.catalog)
        duplicate_path['skills'][1]['path'] = 'area/skills/ALPHA/skill.md'
        catalogs.append(duplicate_path)
        for catalog in catalogs:
            with self.subTest(catalog=catalog):
                with self.assertRaisesRegex(ValueError, 'Invalid|Duplicate'):
                    derive_relations(catalog, self.overlays, self.workflows, self.hashes())

    def test_unknown_and_malformed_related_targets_are_rejected(self):
        for related in (['missing-owner'], ['beta', 'beta'], 'beta', None, [7], [{}]):
            with self.subTest(related=related):
                catalog = copy.deepcopy(self.catalog)
                catalog['skills'][0]['related'] = related
                with self.assertRaisesRegex(ValueError, 'related'):
                    self.derive(catalog=catalog)

    def test_unknown_duplicate_or_invalid_overlay_declarations_are_rejected(self):
        invalid = []
        for field, value in [('skill', 'missing-owner'), ('skill', []), ('phase', 'unknown'),
                             ('phase', None), ('checkpoints', []), ('checkpoints', ['unknown']),
                             ('checkpoints', ['pre-output', 'pre-output']), ('checkpoints', [None])]:
            overlays = copy.deepcopy(self.overlays)
            overlays['overlays'][0][field] = value
            invalid.append(overlays)
        duplicate = copy.deepcopy(self.overlays)
        duplicate['overlays'].append(dict(duplicate['overlays'][0]))
        invalid.append(duplicate)
        extra = copy.deepcopy(self.overlays)
        extra['overlays'][0]['activate'] = True
        invalid.extend([extra, {'overlays': 'not a list'}])
        for overlays in invalid:
            with self.subTest(overlays=overlays):
                with self.assertRaisesRegex(ValueError, 'overlay'):
                    self.derive(overlays=overlays)

    def test_workflow_bytes_and_source_hashes_fail_closed(self):
        bad = dict(self.workflows)
        bad['Workflows/A.md'] += b'Changed source\n'
        with self.assertRaisesRegex(ValueError, 'hash mismatch'):
            self.derive(workflows=bad, hashes=self.hashes())
        for path in ('skill-catalog.yml', 'routing-overlays.yml', 'Workflows/A.md'):
            hashes = self.hashes()
            del hashes[path]
            with self.subTest(missing_hash=path):
                with self.assertRaisesRegex(ValueError, 'source hash'):
                    self.derive(hashes=hashes)
        invalid_utf8 = {'Workflows/A.md': b'\xff'}
        with self.assertRaisesRegex(ValueError, 'UTF-8'):
            self.derive(workflows=invalid_utf8)
        with self.assertRaisesRegex(ValueError, 'UTF-8 bytes'):
            self.derive(workflows={'Workflows/A.md': 'Text'}, hashes=self.hashes())
        with self.assertRaisesRegex(ValueError, 'workflow path'):
            self.derive(workflows={'../outside.md': b'Untrusted path'})
        with self.assertRaisesRegex(ValueError, 'workflow sources'):
            self.derive(workflows=[], hashes=self.hashes())

    def test_overlay_enums_match_the_canonical_schema(self):
        from tools.rule_relations import CHECKPOINTS, PHASES
        path = Path(__file__).resolve().parents[1] / 'Schemas/routing-overlays.schema.json'
        schema = json.loads(path.read_text(encoding='utf-8'))['properties']['overlays']['items']['properties']
        self.assertEqual(PHASES, set(schema['phase']['enum']))
        self.assertEqual(CHECKPOINTS, set(schema['checkpoints']['items']['enum']))


if __name__ == '__main__':
    unittest.main()
