"""Explicit, model-free QMD routing checks; no installation or general recall claim."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from tools import search_rules as search


def main():
    if sys.argv[1:] != ['--run']:
        raise SystemExit('Explicit --run required; installs nothing, rebuilds the derived routing index.')
    node = search.resolve_node()
    metadata, files = search.read_snapshot(ROOT, routing=True)
    _, pilot = search.read_snapshot(ROOT)
    # Known development cases, fixed before this native run. No held-out benchmark.
    cases = [
        ('Rechtschreibung Zeichensetzung', 'Schreiben/Skills/korrekturlektorat/SKILL.md'),
        ('DCF Comparable Companies', 'Finanzen/Skills/bewertungsanalyse/SKILL.md'),
        ('Figuren Motivation Agency', 'Storyentwicklung-und-Fiktion/Skills/figurenentwicklung/SKILL.md'),
        ('Architekturentscheidungen Alternativen Konsequenzen', 'Dokumentationserstellung/Skills/adr/SKILL.md'),
        ('zzroutingabsentf72ea4bd', None),
    ]
    assert all(not expected or expected in files for _, expected in cases)
    assert all(not expected or expected not in pilot for _, expected in cases)
    assert all(b'zzroutingabsentf72ea4bd' not in body for body in files.values())
    sha = lambda body: hashlib.sha256(body).hexdigest()
    output = Path(tempfile.mkdtemp(prefix='native-rule-routing-', dir=ROOT / '.validation'))
    bound = ['tools/search_rules.py', 'tools/search_rules_qmd.mjs', 'Search-KI-Regeln.ps1',
             'tools/local_search/pnpm-lock.yaml', 'Evals/Onboarding/run_rule_routing_native.py']
    protocol = {
        'utc': datetime.now(timezone.utc).isoformat(), 'source_commit': metadata['revision'],
        'node_version': subprocess.check_output([node, '--version'], text=True).strip(),
        'qmd_version': '2.8.3', 'mode': 'bm25', 'held_out': False, 'model_calls': 0,
        'code_sha256': {name: sha((ROOT / name).read_bytes()) for name in bound},
        'cases': [{'query': query, 'expected_top_ten': expected, 'expect_empty': expected is None}
                  for query, expected in cases],
    }
    (output / 'protocol.json').write_text(json.dumps(protocol, ensure_ascii=False, indent=2), encoding='utf-8')
    before = {name: sha((ROOT / name).read_bytes()) for name in files}
    built = search.build(ROOT, node, routing=True)
    results = []
    for query, expected in cases:
        result = search.search(ROOT, query, node, routing=True)
        paths = [hit['path'] for hit in result['hits']]
        passed = expected in paths if expected else not paths
        assert result['candidates_only'] is True
        for hit in result['hits']:
            if hit['kind'] == 'skill':
                assert hit['skill'] == metadata['skills'][hit['path']]
        results.append({'query': query, 'pass': passed, 'result': result})
    after = {name: sha((ROOT / name).read_bytes()) for name in files}
    report = {
        'protocol': protocol, 'protocol_sha256': sha((output / 'protocol.json').read_bytes()),
        'build': built, 'queries': results, 'original_bytes_unchanged': before == after,
        'coverage': {'catalogued_skills': len(metadata['skills']),
                     'indexed_skills': built['routing_coverage']['indexed_skills'],
                     'indexed_documents': built['documents'],
                     'skills_outside_content_pilot': len(set(metadata['skills']) - set(pilot)),
                     'expected_skills_outside_content_pilot': True},
        'claims': {'coverage_is_source_coverage': True, 'general_recall': 'UNVERIFIED',
                   'agent_skill_selection_quality': 'NOT RUN', 'semantic_search': 'NOT RUN', 'model_calls': 0},
    }
    (output / 'result.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    passed = all(item['pass'] for item in results) and before == after
    print(json.dumps({'report_directory': output.relative_to(ROOT).as_posix(), 'pass': passed,
                      'build': built, 'cases': [{'query': r['query'], 'pass': r['pass']} for r in results]}))
    return 0 if passed else 2


if __name__ == '__main__':
    raise SystemExit(main())
