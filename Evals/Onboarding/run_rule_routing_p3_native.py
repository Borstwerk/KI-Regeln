"""Fixed P3 source/relation checks; explicit native BM25, no model or installs."""
from contextlib import ExitStack
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

CASES = 'Evals/Onboarding/rule-routing-cases.json'
WORKFLOW = 'Workflows/Architekturentscheidung-und-Tradeoff.md'
CONTRACTS = {
    'relation-related': 'Visible bewertungsanalyse seed and explicit related hint to unternehmensanalyse.',
    'relation-workflow': 'Explicit frozen evidence workflow selector exposes both required skill mentions; natural query is reported separately.',
    'relation-overlay': 'Visible research-synthesis seed and explicit pre-completion checkpoint hint to citation-audit.',
    'relation-no-seed': 'Frozen nonsense query has zero direct matches and zero hints without a checkpoint.',
    'contract-invalid-relation': 'Unknown related and overlay targets fail before worker and publish no ready pointer.',
}
sha = lambda body: hashlib.sha256(body).hexdigest()


def error_from(action):
    try:
        action()
    except search.SearchError as exc:
        return {'status': exc.status, 'message': str(exc)}
    raise AssertionError('Invalid state was accepted.')


def paged_relations(root, **selector):
    pages, edges, cursor = [], [], None
    while True:
        assert len(pages) < 100, 'Relation pagination did not terminate.'
        page = search.list_relations(root, limit=2, cursor=cursor, **selector)
        assert page['offset'] == len(edges) and page['page_size'] == 2
        assert page['assessment_performed'] is False and page['candidates_only'] is True
        assert page['has_more'] == (page['next_cursor'] is not None)
        pages.append({key: page[key] for key in ('offset', 'total_relations', 'has_more')})
        edges.extend(page['relations']); cursor = page['next_cursor']
        if cursor is None:
            break
    assert len(edges) == page['total_relations']
    identities = [(edge['type'], edge['from'], edge['to']) for edge in edges]
    assert len(set(identities)) == len(edges) and identities == sorted(identities)
    return {'pages': pages, 'relations': edges, 'total_relations': len(edges)}


def fixture_checks(node):
    """Tiny native source-state fixture, independent of live catalog mutations."""
    environment = {key: value for key, value in os.environ.items() if not key.startswith('GIT_')}
    environment.update(GIT_CONFIG_NOSYSTEM='1', GIT_CONFIG_GLOBAL=os.devnull, GIT_TERMINAL_PROMPT='0',
                       GIT_AUTHOR_DATE='2000-01-01T00:00:00+0000', GIT_COMMITTER_DATE='2000-01-01T00:00:00+0000')
    with tempfile.TemporaryDirectory(prefix='p3-native-fixture-', dir=ROOT / '.validation/tmp') as temporary:
        fixture = Path(temporary)
        def git(*args):
            return subprocess.check_output(['git', *args], cwd=fixture, env=environment, stderr=subprocess.PIPE)
        def write(path, body):
            target = fixture / path; target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(body, encoding='utf-8', newline='\n')
        def commit(message):
            git('add', '--all'); git('commit', '--quiet', '-m', message)
        git('init', '--quiet', '--object-format=sha1')
        git('config', 'core.autocrlf', 'false')
        git('config', 'user.name', 'Synthetic P3 Fixture')
        git('config', 'user.email', 'fixture@example.invalid')
        for path in sorted(PROJECT_CORE | {'Workflows/README.md'}):
            write(path, '# Synthetic guide\n')
        workflow = 'Workflows/Synthetic.md'
        body = '# Workflow\n`alpha` optional.\n`beta` for another job.\n'
        write(workflow, body)
        skills = []
        for identifier in ('alpha', 'beta'):
            path = f'Fixture/Skills/{identifier}/SKILL.md'
            write(path, f'---\nname: {identifier}\ndescription: Synthetic relation skill.\n---\n\n# Synthetic\nzzp3nativeseed248a\n')
            skills.append({'id': identifier, 'path': path, 'area': 'Fixture', 'maturity': 'experimental',
                           'eval_coverage': 'none', 'purpose': 'Synthetic purpose for explicit native relation checks.',
                           'related': ['beta'] if identifier == 'alpha' else []})
        catalog = {'schema_version': 2, 'skills': skills}
        overlays = {'schema_version': 2, 'overlays': [
            {'skill': 'beta', 'phase': 'assurance', 'checkpoints': ['pre-completion']}]}
        manifest = {'schema_version': 1, 'id': 'ki-regeln', 'kind': 'collection',
                    'entrypoints': {'overview': 'PROJECT.md', 'status': 'README.md', 'plan': 'CONTRIBUTING.md', 'contents': 'START-HIER.md'},
                    'search': {'include': sorted(PROJECT_CORE), 'exclude': []}}
        for path, value in {'mara-project.json': manifest, 'skill-catalog.yml': catalog,
                            'workflow-index.yml': {'schema_version': 1, 'workflows': [workflow]},
                            'routing-overlays.yml': overlays}.items():
            write(path, json.dumps(value))
        write('.gitignore', '.validation/\n')
        commit('Valid synthetic P3 sources')
        built = search.build(fixture, node, routing=True)
        metadata, _ = search.read_snapshot(fixture, routing=True)
        query = 'zzp3nativeseed248a'
        first = search.search(fixture, query, node, routing=True, limit=1)
        relation_page = search.list_relations(fixture, workflow=workflow, limit=1)
        assert first['next_cursor'] and relation_page['next_cursor']
        blocked = []
        def forbidden(*args):
            blocked.append(True); raise AssertionError('Invalid source reached QMD.')
        write(workflow, body + '\nChanged only the workflow dependency.\n')
        uncommitted = error_from(lambda: search.search(fixture, query, node, worker=forbidden, routing=True,
                                                     limit=1, cursor=first['next_cursor']))
        assert uncommitted['status'] == 'stale' and not blocked
        commit('Change only workflow dependency')
        committed = error_from(lambda: search.search(fixture, query, node, worker=forbidden, routing=True))
        assert committed['status'] == 'stale' and not blocked
        rebuilt = search.build(fixture, node, routing=True)
        changed, _ = search.read_snapshot(fixture, routing=True)
        assert changed['files'] == metadata['files'] and changed['search_documents'] == metadata['search_documents']
        assert changed['fingerprint'] != metadata['fingerprint'] and rebuilt['documents'] == built['documents']
        old_search = error_from(lambda: search.search(fixture, query, node, worker=forbidden, routing=True,
                                                    limit=1, cursor=first['next_cursor']))
        old_relations = error_from(lambda: search.list_relations(fixture, workflow=workflow, limit=1,
                                                               cursor=relation_page['next_cursor']))
        assert old_search['status'] == old_relations['status'] == 'invalid-cursor' and not blocked
        invalid = {}
        for kind in ('related', 'overlay'):
            skills[0]['related'] = ['missing-owner'] if kind == 'related' else ['beta']
            overlays['overlays'][0]['skill'] = 'missing-owner' if kind == 'overlay' else 'beta'
            write('skill-catalog.yml', json.dumps(catalog))
            write('routing-overlays.yml', json.dumps(overlays))
            commit('Unknown synthetic ' + kind + ' target')
            failure = error_from(lambda: search.build(fixture, node, worker=forbidden, routing=True))
            assert 'Unknown ' + kind + ' target: missing-owner' in failure['message']
            assert not (search.state_dir(fixture, True) / 'current.json').exists() and not blocked
            invalid[kind] = {**failure, 'ready_pointer_exists': False, 'worker_calls': 0}
        return {'build': built, 'workflow_only_change': {'uncommitted': uncommitted, 'committed': committed,
                'old_search_cursor': old_search, 'old_relation_cursor': old_relations,
                'canonical_and_search_document_hashes_unchanged': True, 'worker_calls': 0}, 'invalid_targets': invalid}


def main():
    if sys.argv[1:] != ['--run']:
        raise SystemExit('Explicit --run required; installs nothing and makes no model calls.')
    metadata, originals = search.read_snapshot(ROOT, routing=True)
    cases = {case['id']: case for case in json.loads((ROOT / CASES).read_text(encoding='utf-8'))['cases'] if case['phase'] == 'P3'}
    assert set(cases) == set(CONTRACTS)
    bound = ['tools/search_rules.py', 'tools/rule_relations.py', 'tools/search_rules_qmd.mjs', 'Search-KI-Regeln.ps1',
             'tools/check_public_entrypoints.py', 'tools/local_search/pnpm-lock.yaml',
             'Evals/Onboarding/Rule-Routing-P3.md', 'Evals/Onboarding/run_rule_routing_p3_native.py', CASES]
    checksums = {path: sha((ROOT / path).read_bytes()) for path in bound}
    for path in bound:
        committed = search.git(ROOT, 'show', metadata['revision'] + ':' + path)
        assert (ROOT / path).read_bytes().replace(b'\r\n', b'\n') == committed, 'Commit the fixed implementation/protocol before running: ' + path
    node = search.resolve_node()
    (ROOT / '.validation/tmp').mkdir(parents=True, exist_ok=True)
    output = Path(tempfile.mkdtemp(prefix='native-rule-routing-p3-', dir=ROOT / '.validation'))
    protocol = {'utc': datetime.now(timezone.utc).isoformat(), 'source_commit': metadata['revision'],
                'code_sha256': checksums, 'cases_sha256': checksums[CASES], 'criteria': CONTRACTS,
                'queries': {key: value['queries'] for key, value in cases.items()},
                'workflow_selector': WORKFLOW, 'checkpoint': 'pre-completion', 'held_out': False,
                'node_version': subprocess.check_output([node, '--version'], text=True).strip(),
                'qmd_version': search.QMD_VERSION, 'mode': 'bm25', 'model_calls': 0}
    (output / 'protocol.json').write_text(json.dumps(protocol, ensure_ascii=False, indent=2), encoding='utf-8')
    before = {path: sha((ROOT / path).read_bytes()) for path in set(originals) | set(metadata['routing_dependencies']) | {'mara-project.json'}}
    built = search.build(ROOT, node, routing=True)
    results = {}
    for identifier, case in cases.items():
        if case['queries']:
            kwargs = {'checkpoint': 'pre-completion'} if identifier == 'relation-overlay' else {}
            results[identifier] = search.search(ROOT, case['queries'][0], node, routing=True, **kwargs)
    with ExitStack() as stack:
        mocks = [stack.enter_context(patch.object(search, name, side_effect=AssertionError('Relation listing invoked ' + name)))
                 for name in ('resolve_node', 'call_worker', 'current')]
        workflow = paged_relations(ROOT, workflow=WORKFLOW)
        skill = paged_relations(ROOT, skill_id='bewertungsanalyse')
        checkpoint = paged_relations(ROOT, checkpoint='pre-completion')
        for mock in mocks:
            mock.assert_not_called()
    catalog = yaml.safe_load(search.git(ROOT, 'show', metadata['revision'] + ':skill-catalog.yml'))
    targets = {entry['id']: entry['path'] for entry in catalog['skills']}
    for listing in (workflow, skill, checkpoint):
        for edge in listing['relations']:
            source = edge['source']; identifier = edge['to'].removeprefix('skill:')
            assert source['sha256'] == metadata['routing_dependencies'][source['path']]
            assert edge['target_path'] == targets[identifier]
            if edge['type'] == 'mentions':
                lines = search.git(ROOT, 'show', metadata['revision'] + ':' + source['path']).decode('utf-8').splitlines()
                assert source['lines'] and all('`' + identifier + '`' in lines[number - 1] for number in source['lines'])
    hit_ids = lambda result: {hit['skill']['id'] for hit in result['hits'] if hit['kind'] == 'skill'}
    has_edge = lambda edges, kind, start, end: any(edge['type'] == kind and edge['from'] == start and edge['to'] == end for edge in edges)
    related = results['relation-related']; overlay = results['relation-overlay']; empty = results['relation-no-seed']
    predicates = {
        'relation-related': 'bewertungsanalyse' in hit_ids(related) and has_edge(related['routing_hints']['items'], 'related', 'skill:bewertungsanalyse', 'skill:unternehmensanalyse'),
        'relation-workflow': all(has_edge(workflow['relations'], 'mentions', 'workflow:' + WORKFLOW, 'skill:' + identifier) for identifier in cases['relation-workflow']['required_skills']),
        'relation-overlay': 'research-synthesis' in hit_ids(overlay) and has_edge(overlay['routing_hints']['items'], 'checkpoint', 'checkpoint:pre-completion', 'skill:citation-audit'),
        'relation-no-seed': not empty['hits'] and empty['total_matches'] == 0 and empty['routing_hints']['total_relations'] == 0 and not empty['routing_hints']['items'],
    }
    fixture = fixture_checks(node)
    predicates['contract-invalid-relation'] = True  # Both fixed negative controls asserted above.
    assert checksums == {path: sha((ROOT / path).read_bytes()) for path in bound}
    assert all(sha((ROOT / path).read_bytes()) == checksum for path, checksum in before.items())
    report = {'protocol': protocol, 'protocol_sha256': sha((output / 'protocol.json').read_bytes()), 'build': built,
              'routing_format': metadata['routing_format'], 'documents': len(originals),
              'dependency_sha256': metadata['routing_dependencies'],
              'relation_counts': {kind: sum(edge['type'] == kind for edge in metadata['routing_relations']) for kind in ('related', 'mentions', 'checkpoint')},
              'query_results': results, 'selectors': {'workflow': workflow, 'skill': skill, 'checkpoint': checkpoint,
              'node_calls': 0, 'worker_calls': 0, 'ready_index_calls': 0}, 'fixture': fixture,
              'technical_contracts': {key: 'PASS' if value else 'FAIL' for key, value in predicates.items()},
              'workflow_natural_query_required_skills_present': set(cases['relation-workflow']['required_skills']) <= hit_ids(results['relation-workflow']),
              'workflow_selector_supplied_by_evaluator_from_frozen_case': True, 'original_bytes_unchanged': True,
              'claims': {'agent_selection_quality': 'NOT RUN', 'general_semantic_recall': 'UNVERIFIED', 'model_calls': 0}}
    (output / 'result.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'report_directory': output.relative_to(ROOT).as_posix(), 'technical_contracts': report['technical_contracts'],
                      'workflow_natural_query_required_skills_present': report['workflow_natural_query_required_skills_present']}))
    return 0 if all(predicates.values()) else 1


if __name__ == '__main__':
    raise SystemExit(main())
