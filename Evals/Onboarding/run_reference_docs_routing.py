"""Model-free native comparison of one catalog-purpose edit; no installs."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from tools import search_rules as search
from Evals.Onboarding.run_rule_routing_comparison import grade as grade_case

BASELINE_REVISION = '03cdee52bdd38955e81b48d6f46f585db8e18c17'
CANDIDATE_REVISION = 'd07334ec0089812c047f6a9db3bbb0f79181d789'
BEFORE = 'Nachschlagbare Referenz eng an der tatsächlichen Source of Truth dokumentieren.'
AFTER = ('Nachschlagbare Referenzdokumentation für Datenbank, Tabelle, Schema und andere '
         'technische Fakten eng an der tatsächlichen Source of Truth dokumentieren.')
TARGET = 'Dokumentationserstellung/Skills/reference-docs/SKILL.md'
QUERIES = ['Datenbank Tabelle dokumentieren', 'Schema Referenzdokumentation',
           'Tabelle dokumentieren', 'Schema dokumentieren', 'reference docs schema']
NEGATIVE = 'zzroutingabsentf72ea4bd'


def checked_catalog_fix(original, candidate):
    old, new = BEFORE.encode('utf-8'), AFTER.encode('utf-8')
    if original.count(old) != 1 or candidate != original.replace(old, new, 1):
        raise ValueError('Only the declared reference-docs purpose edit is admitted.')
    return candidate


def main():
    if sys.argv[1:] != ['--run']:
        raise SystemExit('Use --run; builds isolated local Git snapshots and uses existing QMD.')
    revision = BASELINE_REVISION
    metadata, files = search.read_snapshot(ROOT, revision=revision, routing=True)
    for name in ('mara-project.json', 'skill-catalog.yml', 'routing-overlays.yml', 'workflow-index.yml'):
        files[name] = search.git(ROOT, 'show', revision + ':' + name)
    for path in search.yaml.safe_load(files['workflow-index.yml'])['workflows']:
        files[path] = search.git(ROOT, 'show', revision + ':' + path)
    for path in json.loads(files['mara-project.json'])['entrypoints'].values():
        files[path] = search.git(ROOT, 'show', revision + ':' + path)
    before_catalog = files['skill-catalog.yml']
    candidate = checked_catalog_fix(before_catalog,
        search.git(ROOT, 'show', CANDIDATE_REVISION + ':skill-catalog.yml'))
    cases_bytes = search.git(ROOT, 'show', revision + ':Evals/Onboarding/rule-routing-cases.json')
    cases = [c for c in json.loads(cases_bytes)['cases']
             if c['phase'] == 'P1' and c['kind'] == 'retrieval']
    assert len(cases) == 16
    for case in cases:
        for evidence in case['evidence']:
            assert hashlib.sha256(files[evidence['path']]).hexdigest() == evidence['sha256'], case['id']
    queries = list(dict.fromkeys(QUERIES + [NEGATIVE] + [q for c in cases for q in c['queries']]))
    out = Path(tempfile.mkdtemp(prefix='reference-docs-routing-', dir=ROOT / '.validation'))
    sha = lambda b: hashlib.sha256(b).hexdigest()
    node = search.resolve_node()
    bound = ['tools/search_rules.py', 'tools/search_rules_qmd.mjs', 'tools/rule_relations.py',
             'tools/check_public_entrypoints.py', 'tools/local_search/pnpm-lock.yaml',
             'Evals/Onboarding/run_rule_routing_comparison.py',
             'Evals/Onboarding/run_reference_docs_routing.py',
             'Evals/Onboarding/Routing-Praxischeck-2026-10-31.md']
    inventory = lambda packet: {path: sha(body) for path, body in sorted(packet.items())}
    protocol = {'revision': revision, 'candidate_revision': CANDIDATE_REVISION,
                'execution_commit': search.git(ROOT, 'rev-parse', 'HEAD').decode().strip(),
                'code_sha256': {path: sha((ROOT / path).read_bytes()) for path in bound},
                'source_inventory': inventory(files),
                'qmd_version': search.QMD_VERSION, 'per_query_limit': 10,
                'node_version': subprocess.check_output([node, '--version'], text=True).strip(),
                'before_catalog_sha256': sha(before_catalog),
                'candidate_catalog_sha256': sha(candidate), 'cases_sha256': sha(cases_bytes),
                'queries': queries, 'target': TARGET, 'model_calls': 0, 'held_out': False,
                'contract': 'target in top ten for five target queries; negative empty; '
                            'no loss of baseline P1 required/one-of outcomes'}
    (out / 'protocol.json').write_text(json.dumps(protocol, ensure_ascii=False, indent=2), encoding='utf-8')
    env = {k: v for k, v in os.environ.items() if not k.startswith('GIT_')}
    env.update(GIT_CONFIG_NOSYSTEM='1', GIT_CONFIG_GLOBAL=os.devnull, GIT_TERMINAL_PROMPT='0',
               GIT_AUTHOR_DATE='2000-01-01T00:00:00+0000', GIT_COMMITTER_DATE='2000-01-01T00:00:00+0000')
    results = {}
    (ROOT / '.validation/tmp').mkdir(parents=True, exist_ok=True)
    for label, catalog in [('baseline', before_catalog), ('candidate', candidate)]:
        with tempfile.TemporaryDirectory(prefix='reference-docs-', dir=ROOT / '.validation/tmp') as temp:
            fixture = Path(temp)
            def git(*args):
                return subprocess.check_output(['git', *args], cwd=fixture, env=env, stderr=subprocess.PIPE)
            git('init', '--quiet', '--object-format=sha1')
            git('config', 'core.autocrlf', 'false')
            git('config', 'user.name', 'Routing Fixture')
            git('config', 'user.email', 'fixture@example.invalid')
            packet = dict(files, **{'skill-catalog.yml': catalog})
            for path, body in packet.items():
                dest = fixture / path
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(body)
            (fixture / '.gitignore').write_text('.validation/\n', encoding='utf-8')
            git('add', '--all')
            git('commit', '--quiet', '-m', 'Local routing fixture')
            build = search.build(fixture, node, routing=True)
            observed = {}
            for query in queries:
                response = search.search(fixture, query, node, routing=True)
                assert response['status'] == 'ready' and response['candidates_only']
                observed[query] = [{'path': h['path'], 'id': h.get('skill', {}).get('id'),
                                    **{key: h[key] for key in ('score', 'content_sha256', 'search_document_sha256', 'snippet_origin') if key in h}}
                                   for h in response['hits']]
                print(json.dumps({'condition': label, 'query': query}, ensure_ascii=False), flush=True)
            assert all((fixture / path).read_bytes() == body for path, body in packet.items())
            results[label] = {'build': build, 'queries': observed, 'source_bytes_unchanged': True,
                              'effective_inventory_sha256': sha(search.canonical_json(inventory(packet)))}
            (out / (label + '.json')).write_text(json.dumps(results[label], ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    def grade(case, condition):
        hits = [hit for query in case['queries'] for hit in results[condition]['queries'][query]]
        found = {h['id'] for h in hits if h['id']}
        return grade_case(case, found, not hits)
    comparisons = [{'id': c['id'], 'baseline': grade(c, 'baseline'),
                    'candidate': grade(c, 'candidate')} for c in cases]
    target = {q: any(h['path'] == TARGET for h in results['candidate']['queries'][q]) for q in QUERIES}
    negative = all(not result['queries'][NEGATIVE] for result in results.values())
    no_regression = all(not c['baseline'] or c['candidate'] for c in comparisons)
    passed = all(target.values()) and negative and no_regression
    report = {'protocol': protocol, 'protocol_sha256': sha((out / 'protocol.json').read_bytes()),
              'results': results, 'p1': comparisons, 'target': target,
              'negative_empty': negative, 'no_p1_regression': no_regression, 'pass': passed,
              'limits': 'development cases; no general recall, natural agent selection, or efficiency claim'}
    (out / 'result.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'report_directory': out.relative_to(ROOT).as_posix(), 'pass': passed,
                      'target': target, 'negative_empty': negative,
                      'p1_baseline_pass': sum(c['baseline'] for c in comparisons),
                      'p1_candidate_pass': sum(c['candidate'] for c in comparisons),
                      'no_p1_regression': no_regression}, ensure_ascii=False), flush=True)
    return 0 if passed else 2


if __name__ == '__main__':
    raise SystemExit(main())
