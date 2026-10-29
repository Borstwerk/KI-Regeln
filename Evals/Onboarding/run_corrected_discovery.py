"""Fixed D1/D3/D5 discovery check. Default: prepare only; --run: one CLI session."""
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
    text = stdout + '\n' + stderr
    category = ('AUTH' if re.search(r'\b401\b|unauthorized|authentication|login required', text, re.I) else
                'CONFIG' if re.search(r'configuration|config error|toml|permission.profile|unknown (?:key|argument)', text, re.I) else
                'TRANSPORT' if re.search(r'connection|network|timed? out|TLS|\b50[0234]\b', text, re.I) else 'UNKNOWN')
    excerpt = stderr
    excerpt = re.sub(r'[A-Za-z]:[\\/]+Users[\\/]+[^\\/\s]+', '<user-home>', excerpt)
    excerpt = re.sub(r'(?i)Bearer\s+\S+|\bsk-[A-Za-z0-9_-]+', '<credential-redacted>', excerpt)
    return {'category': category, 'stderr_present': bool(stderr), 'stderr_excerpt': excerpt[-600:]}


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


def prepare():
    old = json.loads(subprocess.check_output(
        ['git', 'show', SOURCE + ':Evals/Onboarding/Agent-Discovery-Pilot-2026-10-29.json'], cwd=ROOT))['protocol']
    paths = old['archive_paths'] + list(EXTRA)
    archive = subprocess.check_output(['git', '-c', 'core.autocrlf=false', 'archive', '--format=zip', SOURCE, *paths], cwd=ROOT)
    with zipfile.ZipFile(io.BytesIO(archive)) as zipped:
        files = {i.filename: zipped.read(i) for i in zipped.infolist()
                 if not i.is_dir() and not i.filename.startswith(tuple(old['excluded_prefixes']))}
    if any(n.startswith('Evals/') and n != 'Evals/README.md' for n in files):
        raise ValueError('Evaluator payload in snapshot')
    descriptors = check_overlays(files)
    inventory = [(n, digest(b), len(b)) for n, b in sorted(files.items())]
    protocol = {'source_commit': SOURCE, 'archive_paths': paths, 'excluded_prefixes': old['excluded_prefixes'],
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


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run', action='store_true')
    args = parser.parse_args()
    if (OUT / 'started.json').exists() or (OUT / 'response.json').exists():
        raise SystemExit('Existing batch retained; no retry or overwrite')
    files, protocol = prepare()
    OUT.mkdir(parents=True, exist_ok=True)
    dump(OUT / 'protocol.json', protocol)
    if not args.run:
        print(f"Prepared only: {len(files)} files, {len(protocol['overlay_descriptors_sha256'])} descriptors; no model call")
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
    with (OUT / 'started.json').open('x', encoding='utf-8') as handle:
        json.dump({'max_sessions': 1, 'protocol_sha256': digest((OUT / 'protocol.json').read_bytes())}, handle)
    controls = byte_preflight(cli, env)
    dump(OUT / 'preflight.json', controls)
    if not controls['pass']:
        raise SystemExit('Byte/read-only gate failed; model NOT RUN')
    schema = OUT / 'answer-schema.json'
    dump(schema, {'type': 'object', 'properties': {'answer': {'type': 'string'}}, 'required': ['answer'], 'additionalProperties': False})
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
                '--output-schema', str(schema), '--output-last-message', str(OUT / 'answer.json'), '-']
        start = time.monotonic()
        process = subprocess.Popen(argv, env=env, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE, text=True, encoding='utf-8')
        try:
            stdout, stderr = process.communicate(protocol['prompt'], timeout=180)
            row = {'exit_code': process.returncode, 'elapsed_seconds': round(time.monotonic() - start, 2)}
            if process.returncode:
                dump(OUT / 'response.json', dict(row, status='BLOCKED', diagnostic=failure_diagnostic(stdout, stderr)))
                raise SystemExit(2)
            events = [json.loads(line) for line in stdout.splitlines() if line.strip()]
            items = [e['item'] for e in events if e.get('type') == 'item.completed' and 'item' in e]
            # Local raw tool outputs, not reasoning or thread identifiers. Publish a reviewed subset.
            commands = [{k: i[k] for k in ('type', 'command', 'exit_code', 'status', 'aggregated_output') if k in i}
                        for i in items if i.get('type') == 'command_execution']
            row.update(status='RESPONSE_RECORDED', answer=json.loads((OUT / 'answer.json').read_text(encoding='utf-8'))['answer'],
                       completed_item_types=dict(Counter(i.get('type') for i in items)), command_events=commands,
                       event_types=dict(Counter(e.get('type') for e in events)), usage=[e['usage'] for e in events if 'usage' in e])
            dump(OUT / 'response.json', row)
            print(json.dumps({k: row[k] for k in ('status', 'elapsed_seconds')}), flush=True)
        except subprocess.TimeoutExpired:
            subprocess.run(['taskkill', '/PID', str(process.pid), '/T', '/F'], capture_output=True)
            try:
                process.communicate(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
            dump(OUT / 'response.json', {'status': 'BLOCKED', 'reason': '180s deadline; no retry'})
            raise SystemExit(2)


if __name__ == '__main__':
    main()
