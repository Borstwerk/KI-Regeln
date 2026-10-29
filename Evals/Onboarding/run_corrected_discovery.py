"""Fixed discovery checks. Prepare only by default; --remaining selects three fresh cases."""
import argparse
import base64
from collections import Counter
import hashlib
import io
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import time
import zipfile

import yaml

ROOT = Path(__file__).resolve().parents[2]
SOURCE = '211048868a4fc713710450c3c4d3ff17a0923698'
REMAINING_SOURCE = 'cc8f8b6b945bc1cd0d5078433d67c03fb97e97d9'
OUT = ROOT / '.validation/discovery-corrected-20261029'
EXTRA = ('Recherche/Skills/citation-audit/SKILL.md',
         'Schreiben/Skills/adressatengerechte-kommunikation/SKILL.md')


def digest(body):
    return hashlib.sha256(body).hexdigest()


def exact_bytes(actual, expected):
    if not isinstance(actual, bytes) or not isinstance(expected, bytes):
        raise TypeError('Byte gate requires bytes; no implicit text conversion')
    return actual == expected


def denied_target_write(exit_code, event, target, exists):
    return (exit_code == 17 and not exists and isinstance(event, dict)
            and event.get('stage') == 'target_write' and event.get('outcome') == 'permission_denied'
            and event.get('error_type') == 'System.UnauthorizedAccessException'
            and isinstance(event.get('target'), str)
            and os.path.normcase(os.path.abspath(event['target'])) == os.path.normcase(os.path.abspath(target)))


def failure_diagnostic(stdout, stderr):
    def category(text):
        return ('RATE_LIMIT' if re.search(r'usage limit|rate.?limit|\b429\b|UsageLimitExceeded', text, re.I) else
                'AUTH' if re.search(r'\b401\b|\bunauthorized\b|authentication|login required', text, re.I) else
                'CONFIG' if re.search(r'configuration|config error|toml|permission.profile|unknown (?:key|argument)', text, re.I) else
                'TRANSPORT' if re.search(r'connection|network|timed? out|TLS|\b50[0234]\b', text, re.I) else 'UNKNOWN')
    def excerpt(text):
        text = re.sub(r'[A-Za-z]:[\\/]+Users[\\/]+[^\\/\s]+', '<user-home>', text)
        text = re.sub(r'(?i)Bearer\s+\S+|\bsk-[A-Za-z0-9_-]+', '<credential-redacted>', text)
        return text[-600:]
    errors = []
    for line in stdout.splitlines():
        try:
            event = json.loads(line)
        except ValueError:
            continue
        if isinstance(event, dict) and event.get('type') in ('error', 'turn.failed'):
            error = event.get('error', {})
            message = event.get('message') or (error.get('message') if isinstance(error, dict) else None)
            if isinstance(message, str):
                errors.append(message)
    stdout_category, stderr_category = category('\n'.join(errors)), category(stderr)
    return {'category': stdout_category if stdout_category != 'UNKNOWN' else stderr_category,
            'stderr_present': bool(stderr), 'stderr_excerpt': excerpt(stderr),
            'stdout_error_count': len(errors), 'stdout_error_excerpt': excerpt('\n'.join(errors)),
            'stderr_category': stderr_category}


def check_overlays(files):
    catalog = yaml.safe_load(files['skill-catalog.yml'])
    paths = {s['id']: s['path'] for s in catalog['skills']}
    registry = yaml.safe_load(files['routing-overlays.yml'])
    selected = {}
    for overlay in registry['overlays']:
        path = paths[overlay['skill']]
        if path not in files:
            raise ValueError('Missing canonical descriptor: ' + path)
        text = files[path].decode('utf-8')
        front = yaml.safe_load(text.split('---', 2)[1]) if text.startswith('---\n') else {}
        if (not isinstance(front, dict) or front.get('name') != overlay['skill']
                or not isinstance(front.get('description'), str) or not front['description'].strip()):
            raise ValueError('Invalid canonical descriptor: ' + path)
        selected[path] = digest(files[path])
    return selected


def prepare(source=SOURCE):
    old = json.loads(subprocess.check_output(
        ['git', 'show', source + ':Evals/Onboarding/Agent-Discovery-Pilot-2026-10-29.json'], cwd=ROOT))['protocol']
    paths = old['archive_paths'] + list(EXTRA)
    archive = subprocess.check_output(['git', '-c', 'core.autocrlf=false', 'archive', '--format=zip', source, *paths], cwd=ROOT)
    with zipfile.ZipFile(io.BytesIO(archive)) as zipped:
        files = {i.filename: zipped.read(i) for i in zipped.infolist()
                 if not i.is_dir() and not i.filename.startswith(tuple(old['excluded_prefixes']))}
    if any(n.startswith('Evals/') and n != 'Evals/README.md' for n in files):
        raise ValueError('Evaluator payload in snapshot')
    descriptors = check_overlays(files)
    inventory = [(n, digest(b), len(b)) for n, b in sorted(files.items())]
    protocol = {'source_commit': source, 'archive_paths': paths, 'excluded_prefixes': old['excluded_prefixes'],
                'archive_eol': 'git -c core.autocrlf=false archive; canonical LF',
                'files': len(files), 'bytes': sum(map(len, files.values())),
                'inventory_sha256': digest(json.dumps(inventory).encode('utf-8')),
                'overlay_descriptors_sha256': descriptors,
                'prompt': old['prompt'], 'prompt_sha256': digest(old['prompt'].encode('utf-8')),
                'model_requested': 'gpt-6.1-sol', 'reasoning_requested': 'high',
                'max_cli_sessions': 1, 'deadline_seconds': 180, 'retry': False,
                'script_sha256': digest(Path(__file__).read_bytes()),
                'execution_commit': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()}
    return files, protocol


def remaining_cases(base_prompt):
    header = base_prompt.split('1. ', 1)[0]
    return [
        {'id': 'orientation', 'questions': ['D2', 'D4', 'D6'], 'deadline': 180,
         'prompt': header + '1. Ein bestehender Skill scheitert wiederholt. Wo finde ich den Verbesserungsweg?\n'
                   '2. Brauche ich eine Teststrategie oder konkrete Grenzwertfälle?\n'
                   '3. Ich möchte einen Workflow ergänzen. Welche Datei ist maßgeblich?\n'},
        {'id': 'ambiguous', 'questions': ['D7'], 'deadline': 120,
         'prompt': 'Ich möchte „Zugriffe prüfen“. Welcher Skill passt?\n'},
        {'id': 'trivial', 'questions': ['D8'], 'deadline': 45,
         'prompt': 'Formatiere nur diesen Text: „eins,zwei“ → „eins, zwei“.\n'},
    ]


def dump(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def byte_preflight(cli, env):
    """Fixed Windows control: reversible Base64 transport, strict decoded bytes."""
    expected = b'KI-Regeln\x00\r\nbyte\n\xc3\xa4\xff'
    with tempfile.TemporaryDirectory(prefix='ki-regeln-byte-gate-') as tmp:
        workspace = Path(tmp)
        (workspace / 'canary.bin').write_bytes(expected)
        prefix = [cli, 'sandbox', '--include-managed-config', '--permission-profile', ':read-only',
                  '-c', 'windows.sandbox="elevated"', '-C', tmp, '--',
                  'powershell.exe', '-NoProfile', '-NonInteractive', '-Command']
        read = subprocess.run(prefix + ["[Console]::Write([Convert]::ToBase64String([IO.File]::ReadAllBytes('canary.bin')))"],
                              env=env, capture_output=True, timeout=30)
        try:
            actual = base64.b64decode(read.stdout, validate=True)
        except ValueError:
            actual = b''
        write_command = ("$target=[IO.Path]::GetFullPath('denied-write.txt'); "
                         "try { Set-Content -LiteralPath $target -Value controlled -ErrorAction Stop; "
                         "[Console]::Write((@{stage='target_write';outcome='allowed';target=$target}|ConvertTo-Json -Compress)); exit 0 } "
                         "catch { [Console]::Write((@{stage='target_write';outcome='permission_denied';target=$target;"
                         "error_type=$_.Exception.GetType().FullName}|ConvertTo-Json -Compress)); exit 17 }")
        write = subprocess.run(prefix + [write_command],
                               env=env, capture_output=True, timeout=30)
        try:
            write_event = json.loads(write.stdout)
        except (ValueError, UnicodeError):
            write_event = None
        denied = denied_target_write(write.returncode, write_event, workspace / 'denied-write.txt',
                                     (workspace / 'denied-write.txt').exists())
        result = {'read_exit': read.returncode, 'exact_byte_match': exact_bytes(actual, expected),
                  'source_bytes': len(expected), 'source_sha256': digest(expected),
                  'received_bytes': len(actual), 'received_sha256': digest(actual),
                  'write_exit': write.returncode, 'write_target_exists': (workspace / 'denied-write.txt').exists(),
                  'write_permission_denied': denied,
                  'write_attempt_stage': write_event.get('stage') if isinstance(write_event, dict) else None,
                  'write_error_type': write_event.get('error_type') if isinstance(write_event, dict) else None,
                  'known_good_accepted': exact_bytes(expected, expected),
                  'extra_lf_rejected': not exact_bytes(expected + b'\n', expected),
                  'extra_crlf_rejected': not exact_bytes(expected + b'\r\n', expected)}
        result['pass'] = (read.returncode == 0 and result['exact_byte_match']
                      and result['write_permission_denied'] and not result['write_target_exists']
                      and result['extra_lf_rejected'] and result['extra_crlf_rejected'])
    return result


def run_one(cli, env, files, prompt, out, prefix='', deadline=180):
    schema = out / 'answer-schema.json'
    with tempfile.TemporaryDirectory(prefix='ki-regeln-corrected-discovery-') as tmp:
        workspace = Path(tmp)
        for name, body in files.items():
            target = workspace / name
            if not target.resolve().is_relative_to(workspace.resolve()):
                raise ValueError('Unsafe archive path')
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(body)
        argv = [cli, '-a', 'never', 'exec', '--ignore-user-config', '--ephemeral', '--skip-git-repo-check',
                '--cd', tmp, '--json', '--color', 'never', '--model', 'gpt-6.1-sol',
                '-c', 'model_reasoning_effort="high"', '-c', 'default_permissions=":read-only"',
                '-c', 'windows.sandbox="elevated"', '-c', 'model_provider="openai"',
                '-c', 'forced_login_method="chatgpt"', '-c', 'web_search="disabled"',
                '--output-schema', str(schema), '--output-last-message', str(out / (prefix + 'answer.json')), '-']
        start = time.monotonic()
        process = subprocess.Popen(argv, env=env, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE, text=True, encoding='utf-8')
        try:
            stdout, stderr = process.communicate(prompt, timeout=deadline)
            row = {'exit_code': process.returncode, 'elapsed_seconds': round(time.monotonic() - start, 2)}
            if process.returncode:
                dump(out / (prefix + 'response.json'), dict(row, status='BLOCKED', diagnostic=failure_diagnostic(stdout, stderr)))
                raise SystemExit(2)
            events = [json.loads(line) for line in stdout.splitlines() if line.strip()]
            items = [e['item'] for e in events if e.get('type') == 'item.completed' and 'item' in e]
            # Local raw tool outputs, not reasoning or thread identifiers. Publish a reviewed subset.
            commands = [{k: i[k] for k in ('type', 'command', 'exit_code', 'status', 'aggregated_output') if k in i}
                        for i in items if i.get('type') == 'command_execution']
            row.update(status='RESPONSE_RECORDED', answer=json.loads((out / (prefix + 'answer.json')).read_text(encoding='utf-8'))['answer'],
                       completed_item_types=dict(Counter(i.get('type') for i in items)), command_events=commands,
                       event_types=dict(Counter(e.get('type') for e in events)), usage=[e['usage'] for e in events if 'usage' in e])
            dump(out / (prefix + 'response.json'), row)
            print(json.dumps(dict(case=prefix or 'D1-D3-D5', **{k: row[k] for k in ('status', 'elapsed_seconds')})), flush=True)
            return row
        except subprocess.TimeoutExpired:
            subprocess.run(['taskkill', '/PID', str(process.pid), '/T', '/F'], capture_output=True)
            try:
                process.communicate(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
            dump(out / (prefix + 'response.json'), {'status': 'BLOCKED', 'reason': f'{deadline}s deadline; no retry'})
            raise SystemExit(2)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run', action='store_true')
    parser.add_argument('--remaining', action='store_true')
    args = parser.parse_args()
    out = OUT.with_name('discovery-remaining-20261029') if args.remaining else OUT
    if (out / 'started.json').exists() or (out / 'response.json').exists():
        raise SystemExit('Existing batch retained; no retry or overwrite')
    files, protocol = prepare(REMAINING_SOURCE if args.remaining else SOURCE)
    cases = remaining_cases(protocol['prompt']) if args.remaining else [
        {'id': '', 'questions': ['D1', 'D3', 'D5'], 'prompt': protocol['prompt'], 'deadline': 180}]
    if args.remaining:
        protocol.pop('prompt')
        protocol.pop('prompt_sha256')
        protocol.update(cases=cases, max_cli_sessions=3, deadline_seconds=[c['deadline'] for c in cases])
        for case in cases:
            case['prompt_sha256'] = digest(case['prompt'].encode('utf-8'))
    out.mkdir(parents=True, exist_ok=True)
    dump(out / 'protocol.json', protocol)
    if not args.run:
        print(f"Prepared only: {len(files)} files, {len(protocol['overlay_descriptors_sha256'])} descriptors, {len(cases)} sessions; no model call")
        return
    cli = shutil.which('codex')
    if not cli or os.name != 'nt':
        raise SystemExit('Fixed live check needs existing Windows Codex CLI; no installation/fallback')
    env = os.environ.copy()
    for key in ('OPENAI_API_KEY', 'CODEX_API_KEY', 'OPENAI_BASE_URL', 'OPENAI_API_BASE', 'CODEX_MODEL_PROVIDER'):
        env.pop(key, None)
    auth = subprocess.run([cli, 'login', 'status'], env=env, capture_output=True, text=True)
    if auth.returncode or 'Logged in using ChatGPT' not in auth.stdout + auth.stderr:
        raise SystemExit('Existing ChatGPT login required; no fallback')
    with (out / 'started.json').open('x', encoding='utf-8') as handle:
        json.dump({'max_sessions': len(cases), 'protocol_sha256': digest((out / 'protocol.json').read_bytes())}, handle)
    controls = byte_preflight(cli, env)
    dump(out / 'preflight.json', controls)
    if not controls['pass']:
        raise SystemExit('Byte/read-only gate failed; model NOT RUN')
    dump(out / 'answer-schema.json', {'type': 'object', 'properties': {'answer': {'type': 'string'}},
                                    'required': ['answer'], 'additionalProperties': False})
    for case in cases:
        run_one(cli, env, files, case['prompt'], out,
                prefix=case['id'] + '-' if args.remaining else '', deadline=case['deadline'])


if __name__ == '__main__':
    main()
