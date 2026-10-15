"""Fixed instruction pilots through an existing Codex ChatGPT login.

Prepare only by default. --run consumes at most eight CLI sessions; the fixed
--evidence-gap-v2 follow-up consumes at most two. Historical inputs stay pinned.
This records responses; semantic grading is a separate, visible review.
"""
import argparse
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import time

import yaml

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / '.validation/codex-rule-pilot-20261015'
PUBLIC_BLOBS = {
    'Agentenarbeit/Skills/verification-loop/SKILL.md': '31ee04189852a7e681af4dd7b3230e3fb4a75fc1',
    'Agentenarbeit/Task-Graph-und-Loops.md': '7fc1f08fd7d9501ab2a5ae2d299086e68b696cc3',
    'Agentenarbeit/Human-Gates-und-Freigaben.md': '23b43dc35081ebf36462f16dff683d5b8145a3cd',
    'Evals/Agentenarbeit/verification-loop/cases.yml': '0552cab33ecd25fac162ceccf1288cf4e7cb5546',
}
CASE_IDS = ('explain-existing-result-near-miss', 'validator-cannot-run',
            'do-not-weaken-check', 'checker-must-demonstrate-failure')
CASES_PATH = 'Evals/Agentenarbeit/verification-loop/cases.yml'
EVIDENCE_GAP_V2_BLOB = 'b5b96950b09e8deb8970e7cbfef6602f428289e8'
MODEL, EFFORT = 'gpt-6.1-sol', 'high'  # Existing user settings, held constant in both arms.


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run', action='store_true')
    parser.add_argument('--evidence-gap-v2', action='store_true')
    args = parser.parse_args()
    blobs = dict(PUBLIC_BLOBS)
    out = OUT
    ids = CASE_IDS
    if args.evidence_gap_v2:
        blobs[CASES_PATH] = EVIDENCE_GAP_V2_BLOB
        out = OUT.with_name('codex-evidence-gap-v2-20261015')
        ids = ('validator-cannot-run',)
    try:
        sources = {name: subprocess.check_output(['git', 'cat-file', 'blob', blob], cwd=ROOT)
                   for name, blob in blobs.items()}
    except subprocess.CalledProcessError:
        raise SystemExit('Pinned input blob unavailable; review repository history. No automatic fetch or fallback.') from None
    out.mkdir(exist_ok=True)
    cases = yaml.safe_load(sources[CASES_PATH].decode('utf-8'))['cases']
    selected = [next(case for case in cases if case['id'] == name) for name in ids]
    protocol = {'scope': f'{len(selected)} paired text-scenario probes; one fresh response per arm/case',
                'input_binding': 'Exact pinned Git blobs; current working-tree input files are not substituted',
                'model_requested': MODEL, 'reasoning_requested': EFFORT,
                'max_cli_sessions': 2 * len(selected), 'timeout_seconds_per_session': 90,
                'retry_or_fallback': False, 'repetitions': 1,
                'public_repository': 'https://github.com/Borstwerk/KI-Regeln',
                'public_git_blobs': blobs,
                'source_sha256': {name: hashlib.sha256(body).hexdigest() for name, body in sources.items()},
                'script_sha256': digest(Path(__file__)),
                'source_commit': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
                'grading': 'Review every expected/forbidden criterion, not keyword matching. No invented execution evidence.',
                'limits': ['Instruction bundle includes its two mandatory reference documents',
                           'No natural routing, real code repair or B2 admission measured',
                           'No independent/held-out benchmark or maturity promotion'],
                'cases': selected}
    protocol_path = out / 'protocol.json'
    if (out / 'responses.json').exists():
        raise SystemExit('Existing responses retained; this fixed batch does not overwrite or retry runs.')
    protocol_path.write_text(json.dumps(protocol, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    if not args.run:
        print(f'Prepared {len(selected)} pairs; no model call. Protocol: ' + str(protocol_path))
        return
    cli = shutil.which('codex')
    if not cli:
        raise SystemExit('Codex CLI missing; no fallback')
    env = os.environ.copy()
    for name in ('OPENAI_API_KEY', 'CODEX_API_KEY', 'OPENAI_BASE_URL', 'OPENAI_API_BASE', 'CODEX_MODEL_PROVIDER'):
        env.pop(name, None)
    auth = subprocess.run([cli, 'login', 'status'], env=env, capture_output=True, text=True, check=False)
    if auth.returncode or 'Logged in using ChatGPT' not in auth.stdout + auth.stderr:
        raise SystemExit('Existing ChatGPT login required; no login/key fallback')
    schema = {'type': 'object', 'properties': {'answer': {'type': 'string'}},
              'required': ['answer'], 'additionalProperties': False}
    schema_path = out / 'response-schema.json'
    schema_path.write_text(json.dumps(schema), encoding='utf-8')
    bundle = '\n\n'.join(sources[name].decode('utf-8') for name in list(blobs)[:3])
    rows = []
    for index, case in enumerate(selected):
        for arm in (('baseline', 'skill') if index % 2 == 0 else ('skill', 'baseline')):
            prompt = ('Beantworte den Auftrag auf Deutsch in hoechstens zwoelf Saetzen. '
                      'Es ist ein fiktives Textszenario: keine Tools, Dateien, weiteren Agenten oder Webrecherche.\n\n')
            if arm == 'skill':
                prompt += '<instructions>\n' + bundle + '\n</instructions>\n\n'
            prompt += 'Auftrag: ' + case['input']
            if case['id'] == CASE_IDS[0]:
                prompt += '\nVorliegendes Log: validator failed: JSON syntax error at line 3. Exit code: 1.'
            prompt_path = out / f"{index + 1}-{arm}-prompt.txt"
            prompt_path.write_text(prompt, encoding='utf-8')
            response_path = out / f"{index + 1}-{arm}-response.json"
            row = {'case': case['id'], 'arm': arm, 'prompt_sha256': digest(prompt_path), 'status': 'NOT_RUN'}
            with tempfile.TemporaryDirectory(prefix='ki-regeln-codex-case-') as workspace:
                argv = [cli, 'exec', '--ignore-user-config', '--ephemeral', '--sandbox', 'read-only',
                        '--skip-git-repo-check', '--cd', workspace, '--color', 'never', '--json', '--model', MODEL,
                        '-c', f'model_reasoning_effort="{EFFORT}"', '-c', 'model_provider="openai"',
                        '-c', 'forced_login_method="chatgpt"', '-c', 'web_search="disabled"',
                        '-c', 'project_doc_max_bytes=0', '--output-schema', str(schema_path),
                        '--output-last-message', str(response_path), '-']
                start = time.monotonic()
                process = subprocess.Popen(argv, env=env, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE, text=True, encoding='utf-8')
                try:
                    stdout, stderr = process.communicate(prompt, timeout=90)
                    row.update(exit_code=process.returncode, elapsed_seconds=round(time.monotonic() - start, 2))
                    if process.returncode:
                        row.update(status='BLOCKED', reason='CLI failed; batch stopped without retry')
                    else:
                        events = [json.loads(line) for line in stdout.splitlines() if line.strip()]
                        items = [e['item'] for e in events if 'item' in e]
                        row.update(status='RESPONSE_RECORDED', response=json.loads(response_path.read_text(encoding='utf-8')),
                                   event_types=dict(Counter(e.get('type', 'unknown') for e in events)),
                                   item_types=dict(Counter(item.get('type', 'unknown') for item in items)),
                                   usage=[e['usage'] for e in events if 'usage' in e],
                                   model_identity='Requested model recorded; no independent server model attestation')
                except subprocess.TimeoutExpired:
                    subprocess.run(['taskkill', '/PID', str(process.pid), '/T', '/F'], capture_output=True, check=False)
                    try: process.communicate(timeout=5)
                    except subprocess.TimeoutExpired: process.kill()
                    row.update(status='BLOCKED', reason='90s deadline; batch stopped without retry')
            rows.append(row)
            (out / 'responses.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
            print(json.dumps({k: row[k] for k in ('case', 'arm', 'status')}) , flush=True)
            if row['status'] != 'RESPONSE_RECORDED':
                raise SystemExit(2)


if __name__ == '__main__':
    main()
