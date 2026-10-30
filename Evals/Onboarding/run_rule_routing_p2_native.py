"""Explicit native P2 checks: bounded QMD pages and model-free catalog enumeration."""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
from unittest.mock import patch

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from tools import search_rules as search
from tools.check_public_entrypoints import PROJECT_CORE

MARKER = 'zznativepaginationb8e349c2'
sha = lambda body: hashlib.sha256(body).hexdigest()
json_sha = lambda value: sha(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8'))


def main():
    if sys.argv[1:] != ['--run']:
        raise SystemExit('Explicit --run required; installs nothing and uses an isolated fixture.')
    metadata, originals = search.read_snapshot(ROOT, routing=True)
    catalog_bytes = search.git(ROOT, 'show', metadata['revision'] + ':skill-catalog.yml')
    catalog = yaml.safe_load(catalog_bytes)
    bound = ['tools/search_rules.py', 'tools/search_rules_qmd.mjs', 'Search-KI-Regeln.ps1',
             'tools/check_public_entrypoints.py', 'tools/local_search/pnpm-lock.yaml',
             'Evals/Onboarding/run_rule_routing_p2_native.py']
    node = search.resolve_node()
    (ROOT / '.validation/tmp').mkdir(parents=True, exist_ok=True)
    output = Path(tempfile.mkdtemp(prefix='native-rule-routing-p2-', dir=ROOT / '.validation'))
    expected_paths = [f'Fixture/Skills/page-{i:02d}/SKILL.md' for i in range(14)]
    protocol = {'utc': datetime.now(timezone.utc).isoformat(), 'source_commit': metadata['revision'],
                'code_sha256': {p: sha((ROOT / p).read_bytes()) for p in bound},
                'cases_sha256': sha((ROOT / 'Evals/Onboarding/rule-routing-cases.json').read_bytes()),
                'contracts': ['contract-pagination', 'contract-stale', 'contract-descriptors'],
                'node_version': subprocess.check_output([node, '--version'], text=True).strip(),
                'qmd_version': search.QMD_VERSION, 'mode': 'bm25', 'model_calls': 0, 'held_out': False,
                'query': MARKER, 'expected_paths': expected_paths, 'expected_documents': 24, 'page_size': 4}
    (output / 'protocol.json').write_text(json.dumps(protocol, indent=2), encoding='utf-8')
    before = {p: sha((ROOT / p).read_bytes()) for p in
              [*originals, 'skill-catalog.yml', 'routing-overlays.yml', 'workflow-index.yml', 'mara-project.json']}
    environment = {k: v for k, v in os.environ.items() if not k.startswith('GIT_')}
    environment.update(GIT_CONFIG_NOSYSTEM='1', GIT_CONFIG_GLOBAL=os.devnull, GIT_TERMINAL_PROMPT='0',
                       GIT_AUTHOR_DATE='2000-01-01T00:00:00+0000', GIT_COMMITTER_DATE='2000-01-01T00:00:00+0000')
    with tempfile.TemporaryDirectory(prefix='p2-native-fixture-', dir=ROOT / '.validation/tmp') as temporary:
        fixture = Path(temporary)
        def git(*arguments):
            return subprocess.check_output(['git', *arguments], cwd=fixture, env=environment, stderr=subprocess.PIPE)
        git('init', '--quiet', '--object-format=sha1')
        git('config', 'core.autocrlf', 'false')
        git('config', 'user.name', 'Synthetic P2 Fixture')
        git('config', 'user.email', 'fixture@example.invalid')
        for path in sorted(PROJECT_CORE | {'Workflows/README.md'}):
            target = fixture / path; target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text('# Synthetic guide\nNo query marker.\n', encoding='utf-8', newline='\n')
        skills = []
        for i, path in enumerate(expected_paths):
            identifier = f'page-{i:02d}'
            target = fixture / path; target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(f'---\nname: {identifier}\ndescription: Synthetic pagination skill.\n---\n\n# Synthetic skill\n{MARKER}\n', encoding='utf-8', newline='\n')
            skills.append({'id': identifier, 'path': path, 'area': 'Fixture', 'maturity': 'experimental',
                           'eval_coverage': 'none', 'purpose': 'Synthetic purpose for a bounded pagination fixture.'})
        manifest = {'schema_version': 1, 'id': 'ki-regeln', 'kind': 'collection',
                    'entrypoints': {'overview': 'PROJECT.md', 'status': 'README.md', 'plan': 'CONTRIBUTING.md', 'contents': 'START-HIER.md'},
                    'search': {'include': sorted(PROJECT_CORE), 'exclude': []}}
        for path, value in {'mara-project.json': manifest, 'skill-catalog.yml': {'schema_version': 2, 'skills': skills},
                            'workflow-index.yml': {'schema_version': 1, 'workflows': []},
                            'routing-overlays.yml': {'schema_version': 2, 'overlays': []}}.items():
            (fixture / path).write_text(json.dumps(value), encoding='utf-8', newline='\n')
        (fixture / '.gitignore').write_text('.validation/\n', encoding='utf-8', newline='\n')
        git('add', '--all'); git('commit', '--quiet', '-m', 'Synthetic P2 sources')
        built = search.build(fixture, node, routing=True)
        assert built['documents'] == 24 and built['routing_coverage']['indexed_skills'] == 14
        pages, hits, cursor = [], [], None
        while True:
            assert len(pages) < 4, 'Pagination did not terminate within the known four-page fixture.'
            page = search.search(fixture, MARKER, node, routing=True, limit=4, cursor=cursor)
            assert page['total_matches'] == 14 and page['offset'] == len(hits) and page['page_size'] == 4
            assert page['has_more'] == (page['next_cursor'] is not None)
            pages.append(page); hits.extend(page['hits']); cursor = page['next_cursor']
            if cursor is None: break
        assert len(hits) == 14 and len({h['path'] for h in hits}) == 14
        assert sorted(h['path'] for h in hits) == expected_paths
        assert hits == sorted(hits, key=lambda h: (-h['score'], h['path']))
        old_cursor, blocked_calls = pages[0]['next_cursor'], []
        def forbidden_worker(*arguments):
            blocked_calls.append(True); raise AssertionError('Changed source reached the QMD worker.')
        changed = fixture / expected_paths[0]
        changed.write_bytes(changed.read_bytes() + b'\nChanged source after page one.\n')
        try: search.search(fixture, MARKER, node, worker=forbidden_worker, routing=True, cursor=old_cursor)
        except search.SearchError as exc: stale = {'status': exc.status, 'message': str(exc)}
        else: raise AssertionError('Old cursor accepted after source edit.')
        assert stale['status'] in ('stale', 'invalid-cursor') and not blocked_calls
        git('add', '--all'); git('commit', '--quiet', '-m', 'Changed synthetic source')
        search.build(fixture, node, routing=True)
        try: search.search(fixture, MARKER, node, worker=forbidden_worker, routing=True, cursor=old_cursor)
        except search.SearchError as exc: rebuilt = {'status': exc.status, 'message': str(exc)}
        else: raise AssertionError('Old cursor accepted after rebuilding changed sources.')
        assert rebuilt['status'] == 'invalid-cursor' and not blocked_calls
        native = {'build': built, 'pages': pages, 'unique_hits': len(hits), 'score_groups': len({h['score'] for h in hits}),
                  'global_order_matches': True, 'source_edit': stale, 'after_rebuild': rebuilt, 'stale_worker_calls': 0}
    descriptors, descriptor_pages, cursor = [], [], None
    with patch.object(search, 'resolve_node', side_effect=AssertionError('Catalog listing invoked Node.')) as blocked_node, \
         patch.object(search, 'call_worker', side_effect=AssertionError('Catalog listing invoked QMD.')) as blocked_worker, \
         patch.object(search, 'current', side_effect=AssertionError('Catalog listing required a ready QMD index.')) as blocked_index:
        while True:
            assert len(descriptor_pages) < (len(catalog['skills']) + 24) // 25
            page = search.list_skills(ROOT, limit=25, cursor=cursor)
            assert page['mode'] == 'catalog' and page['assessment_performed'] is False
            assert page['total_skills'] == len(catalog['skills']) and page['offset'] == len(descriptors)
            assert page['has_more'] == (page['next_cursor'] is not None)
            descriptor_pages.append(page); descriptors.extend(page['skills']); cursor = page['next_cursor']
            if cursor is None: break
        blocked_node.assert_not_called(); blocked_worker.assert_not_called(); blocked_index.assert_not_called()
    expected = {entry['id']: entry for entry in catalog['skills']}
    assert [d['id'] for d in descriptors] == sorted(expected)
    for descriptor in descriptors:
        entry = expected[descriptor['id']]; path = entry['path']
        source = (ROOT / path).read_text(encoding='utf-8')
        lines = source.splitlines(); closing = lines.index('---', 1)
        assert descriptor['description'] == yaml.safe_load('\n'.join(lines[1:closing]))['description']
        for field in ['id', 'path', 'purpose', 'area', 'maturity', 'eval_coverage']:
            assert descriptor[field] == entry[field]
        for field in ['capabilities', 'related']: assert descriptor[field] == entry.get(field, [])
        assert descriptor['content_sha256'] == sha(originals[path])
        sources = {s['path']: s['sha256'] for s in descriptor['sources']}
        assert sources[path] == sha(originals[path]) and sources['skill-catalog.yml'] == sha(catalog_bytes)
    assert all(sha((ROOT / p).read_bytes()) == checksum for p, checksum in before.items())
    catalog_pages = [{**{key: page[key] for key in ('revision', 'fingerprint', 'offset', 'page_size', 'total_skills',
                                                  'has_more', 'next_cursor', 'assessment_performed')},
                      'ids': [skill['id'] for skill in page['skills']], 'skills_sha256': json_sha(page['skills'])}
                     for page in descriptor_pages]
    report = {'protocol': protocol, 'protocol_sha256': sha((output / 'protocol.json').read_bytes()), 'native': native,
              'catalog': {'pages': catalog_pages, 'descriptors_sha256': json_sha(descriptors),
                          'unique_skills': len(descriptors), 'node_calls': 0, 'worker_calls': 0,
                          'ready_index_calls': 0, 'canonical_descriptions_match': True, 'assessment_performed': False},
              'original_bytes_unchanged': True, 'contracts': {name: 'PASS' for name in protocol['contracts']},
              'claims': {'general_recall': 'UNVERIFIED', 'agent_selection_quality': 'NOT RUN', 'model_calls': 0}}
    (output / 'result.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'report_directory': output.relative_to(ROOT).as_posix(), 'hits': len(hits), 'skills': len(descriptors), 'contracts': report['contracts']}))


if __name__ == '__main__':
    main()
