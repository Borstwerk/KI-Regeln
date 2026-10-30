"""Bounded P0/P1 native comparison on the same frozen public source packet."""
import argparse
from datetime import datetime, timezone
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

SOURCE = '6b80949fea00a427303a8dad9a612b59d7fd04ca'
CASES = Path(__file__).with_name('rule-routing-cases.json')
sha = lambda body: hashlib.sha256(body).hexdigest()


def grade(case, found, empty):
    return (not (set(case['required_skills']) - found)
            and all(found.intersection(group) for group in case['one_of'])
            and (empty if case['expect_empty'] else True))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run', action='store_true')
    parser.add_argument('--label', required=True, choices=['baseline', 'candidate'])
    args = parser.parse_args()
    if not args.run:
        parser.error('Explicit --run required; installs nothing, uses isolated synthetic Git state.')
    cases_bytes = CASES.read_bytes()
    data = json.loads(cases_bytes)
    cases = data['cases']
    assert data['source_commit'] == SOURCE
    assert len(cases) == 24 and len({c['id'] for c in cases}) == 24
    # Both implementations receive these exact original bytes, not their checkouts.
    _, original = search.read_snapshot(ROOT, revision=SOURCE, routing=True)
    for name in ['mara-project.json', 'skill-catalog.yml', 'routing-overlays.yml', 'workflow-index.yml']:
        original[name] = search.git(ROOT, 'show', SOURCE + ':' + name)
    for name in json.loads(original['mara-project.json'])['entrypoints'].values():
        if name not in original:
            original[name] = search.git(ROOT, 'show', SOURCE + ':' + name)
    workflows = set(search.yaml.safe_load(original['workflow-index.yml'])['workflows'])
    for case in cases:
        for evidence in case['evidence']:
            name = evidence['path']
            if name not in original:
                assert name in workflows, 'Only registered workflow evidence may extend the packet.'
                original[name] = search.git(ROOT, 'show', SOURCE + ':' + name)
    packet_hash = sha(json.dumps({p: sha(b) for p, b in sorted(original.items())}, sort_keys=True).encode())
    for case in cases:
        for evidence in case['evidence']:
            assert sha(original[evidence['path']]) == evidence['sha256'], case['id']
    node = search.resolve_node()
    (ROOT / '.validation/tmp').mkdir(parents=True, exist_ok=True)
    output = Path(tempfile.mkdtemp(prefix='rule-routing-' + args.label + '-', dir=ROOT / '.validation'))
    bound = ['tools/search_rules.py', 'tools/search_rules_qmd.mjs', 'tools/check_public_entrypoints.py',
             'tools/local_search/pnpm-lock.yaml', 'Evals/Onboarding/run_rule_routing_comparison.py']
    protocol = {'utc': datetime.now(timezone.utc).isoformat(), 'label': args.label,
                'source_commit': SOURCE, 'source_packet_sha256': packet_hash,
                'cases_sha256': sha(cases_bytes), 'qmd_version': search.QMD_VERSION,
                'node_version': subprocess.check_output([node, '--version'], text=True).strip(),
                'code_sha256': {p: sha((ROOT / p).read_bytes()) for p in bound},
                'model_calls': 0, 'held_out': False, 'per_query_limit': 10}
    (output / 'protocol.json').write_text(json.dumps(protocol, indent=2), encoding='utf-8')
    environment = {k: v for k, v in os.environ.items() if not k.startswith('GIT_')}
    environment.update(GIT_CONFIG_NOSYSTEM='1', GIT_CONFIG_GLOBAL=os.devnull, GIT_TERMINAL_PROMPT='0',
                       GIT_AUTHOR_DATE='2000-01-01T00:00:00+0000', GIT_COMMITTER_DATE='2000-01-01T00:00:00+0000')
    results = []
    with tempfile.TemporaryDirectory(prefix='routing-packet-', dir=ROOT / '.validation/tmp') as temporary:
        fixture = Path(temporary)
        def git(*arguments):
            return subprocess.check_output(['git', *arguments], cwd=fixture, env=environment, stderr=subprocess.PIPE)
        git('init', '--quiet', '--object-format=sha1')
        git('config', 'core.autocrlf', 'false')
        git('config', 'user.name', 'Public Routing Comparison')
        git('config', 'user.email', 'fixture@example.invalid')
        for name, body in original.items():
            target = fixture / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(body)
        (fixture / '.gitignore').write_text('.validation/\n', encoding='utf-8')
        git('add', '--all')
        git('commit', '--quiet', '-m', 'Frozen public routing source packet')
        fixture_revision = git('rev-parse', 'HEAD').decode().strip()
        built = search.build(fixture, node, routing=True)
        for case in cases:
            if case['phase'] != 'P1' or case['kind'] != 'retrieval':
                results.append({'id': case['id'], 'status': 'NOT RUN', 'reason': 'later implementation phase'})
                continue
            queries, found, all_empty = [], set(), True
            for query in case['queries']:
                response = search.search(fixture, query, node, routing=True)
                assert response['candidates_only'] is True
                hits = response['hits']
                all_empty = all_empty and not hits
                found.update(h['skill']['id'] for h in hits if h['kind'] == 'skill')
                queries.append({'query': query, 'hits': [
                    {key: h[key] for key in ('path', 'score', 'content_sha256', 'search_document_sha256', 'snippet_origin') if key in h}
                    for h in hits]})
            passed = grade(case, found, all_empty)
            results.append({'id': case['id'], 'status': 'PASS' if passed else 'FAIL',
                            'found_skills': sorted(found), 'missing_required': sorted(set(case['required_skills']) - found),
                            'unsuitable_candidates': sorted(found.intersection(case['unsuitable_skills'])),
                            'queries': queries})
            print(json.dumps({'case': case['id'], 'status': results[-1]['status']}), flush=True)
        unchanged = all((fixture / p).read_bytes() == b for p, b in original.items())
    assert unchanged
    counts = {state: sum(r['status'] == state for r in results) for state in ['PASS', 'FAIL', 'NOT RUN']}
    report = {'protocol': protocol, 'protocol_sha256': sha((output / 'protocol.json').read_bytes()),
              'fixture_revision': fixture_revision, 'build': built, 'cases': results, 'counts': counts,
              'original_bytes_unchanged': unchanged, 'status': 'PARTIAL' if counts['FAIL'] else 'PASS for P1 cases',
              'claims': {'general_recall': 'UNVERIFIED', 'agent_selection_quality': 'NOT RUN', 'model_calls': 0}}
    (output / 'result.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'report_directory': output.relative_to(ROOT).as_posix(), 'counts': counts, 'status': report['status']}))
    return 2 if counts['FAIL'] else 0


if __name__ == '__main__':
    raise SystemExit(main())
