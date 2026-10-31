"""Three fixed fresh CLI sessions; prepare by default, no install or model judge."""
from collections import Counter
from datetime import datetime, timezone
import hashlib
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time
import zipfile

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from Evals.Onboarding.run_corrected_discovery import byte_preflight, failure_diagnostic
from tools import search_rules

SOURCE = 'e815a0b'
OUT = ROOT / '.validation/routing-p4-20261031'
CASES = Path(__file__).with_name('rule-routing-p4-cases.json')
sha = lambda body: hashlib.sha256(body).hexdigest()


def dump(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def packet():
    archive = search_rules.git(ROOT, '-c', 'core.autocrlf=false', 'archive', '--format=zip', SOURCE)
    scripts = {'Search-KI-Regeln.ps1', 'tools/search_rules.py', 'tools/rule_relations.py',
               'tools/search_rules_qmd.mjs', 'tools/check_public_entrypoints.py'}
    with zipfile.ZipFile(io.BytesIO(archive)) as zipped:
        files = {entry.filename: zipped.read(entry) for entry in zipped.infolist()
                 if not entry.is_dir() and not entry.filename.startswith(('Evals/', 'tests/', '.github/', '.codex/', '.agents/'))
                 and entry.filename != 'Dokumentation/Skill-Routing-Suche-Umsetzungsplan.md'
                 and (entry.filename in scripts or (not entry.filename.startswith('tools/')
                      and Path(entry.filename).suffix in ('.md', '.yml', '.yaml', '.json')))}
    assert 'AGENTS.md' in files and 'tools/search_rules.py' in files
    assert not any(path.startswith(('Evals/', 'tests/')) for path in files)
    return files


def junction(path, target):
    # Both resolved paths are locally generated/known; no source or runtime copy.
    quote = lambda value: "'" + str(value).replace("'", "''") + "'"
    subprocess.run(['powershell.exe', '-NoProfile', '-NonInteractive', '-Command',
                    'New-Item -ItemType Junction -Path ' + quote(path) + ' -Target ' + quote(target) + ' | Out-Null'],
                   check=True, capture_output=True)


def main():
    if sys.argv[1:] not in ([], ['--run']):
        raise SystemExit('Only optional --run is supported.')
    live = sys.argv[1:] == ['--run']
    if (OUT / 'started.json').exists():
        raise SystemExit('Existing batch retained; no retry/overwrite.')
    data = json.loads(CASES.read_text(encoding='utf-8'))
    assert [case['id'] for case in data['cases']] == ['development', 'fallback', 'trivial']
    files = packet()
    operational = ['tools/search_rules.py', 'tools/rule_relations.py',
                   'tools/search_rules_qmd.mjs', 'tools/check_public_entrypoints.py']
    for path in operational:
        assert (ROOT / path).read_bytes().replace(b'\r\n', b'\n') == files[path], 'Root build tooling differs from fixed product source: ' + path
    inventory = {path: sha(body) for path, body in sorted(files.items())}
    bound = ['Evals/Onboarding/run_rule_routing_p4.py', 'Evals/Onboarding/rule-routing-p4-cases.json',
             'Evals/Onboarding/Rule-Routing-P4.md', 'Evals/Onboarding/run_corrected_discovery.py']
    execution = search_rules.git(ROOT, 'rev-parse', 'HEAD').decode().strip()
    if live:
        for path in bound:
            assert (ROOT / path).read_bytes().replace(b'\r\n', b'\n') == search_rules.git(ROOT, 'show', execution + ':' + path), 'Commit protocol before run: ' + path
    protocol = {'utc': datetime.now(timezone.utc).isoformat(), 'source_commit': search_rules.git(ROOT, 'rev-parse', SOURCE).decode().strip(),
                'execution_commit': execution, 'source_inventory': inventory,
                'inventory_sha256': sha(json.dumps(inventory, sort_keys=True).encode()),
                'code_sha256': {path: sha((ROOT / path).read_bytes()) for path in bound},
                'root_build_code_sha256': {path: sha((ROOT / path).read_bytes()) for path in operational},
                'cases': data['cases'], 'model_requested': 'gpt-6.1-sol', 'reasoning_requested': 'high',
                'sessions': 3, 'deadline_seconds_each': 240, 'retry': False, 'held_out': False,
                'direct_api_calls': 0, 'permission_boundary': 'workspace-write for development; source integrity checked afterward; others read-only'}
    OUT.mkdir(parents=True, exist_ok=True)
    dump(OUT / 'protocol.json', protocol)
    if not live:
        print(json.dumps({'status': 'PREPARED ONLY', 'files': len(files), 'sessions': 3, 'model_calls': 0}))
        return
    cli = shutil.which('codex')
    if not cli or os.name != 'nt':
        raise SystemExit('Existing Windows Codex CLI required; no fallback.')
    env = {key: value for key, value in os.environ.items()
           if not key.startswith(('OPENAI_', 'ANTHROPIC_', 'CODEX_API_'))
           and key not in ('CODEX_MODEL_PROVIDER', 'NODE_OPTIONS', 'NODE_PATH', 'QMD_TRUST_UPDATE_HOOKS')}
    auth = subprocess.run([cli, 'login', 'status'], env=env, capture_output=True, text=True)
    if auth.returncode or 'Logged in using ChatGPT' not in auth.stdout + auth.stderr:
        raise SystemExit('ChatGPT subscription login required; no API fallback.')
    with (OUT / 'started.json').open('x', encoding='utf-8') as handle:
        json.dump({'protocol_sha256': sha((OUT / 'protocol.json').read_bytes()),
                   'cli_version': subprocess.check_output([cli, '--version'], env=env, text=True).strip()}, handle)
    controls = byte_preflight(cli, env)
    dump(OUT / 'preflight.json', controls)
    if not controls['pass']:
        raise SystemExit('Byte/read-only preflight failed; model NOT RUN.')
    schema = OUT / 'answer-schema.json'
    dump(schema, {'type': 'object', 'properties': {'answer': {'type': 'string'}}, 'required': ['answer'], 'additionalProperties': False})
    git_env = {key: value for key, value in env.items() if not key.startswith('GIT_')}
    git_env.update(GIT_CONFIG_NOSYSTEM='1', GIT_CONFIG_GLOBAL=os.devnull, GIT_TERMINAL_PROMPT='0',
                   GIT_AUTHOR_DATE='2000-01-01T00:00:00+0000', GIT_COMMITTER_DATE='2000-01-01T00:00:00+0000')
    for case in data['cases']:
        workspace = OUT / ('workspace-' + case['id'])
        workspace.mkdir()
        for path, body in files.items():
            target = workspace / path
            assert target.resolve().is_relative_to(workspace.resolve())
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(body)
        def git(*args):
            return subprocess.check_output(['git', *args], cwd=workspace, env=git_env, stderr=subprocess.PIPE)
        git('init', '--quiet', '--object-format=sha1')
        git('config', 'core.autocrlf', 'false')
        git('config', 'user.name', 'P4 Snapshot')
        git('config', 'user.email', 'fixture@example.invalid')
        (workspace / '.gitignore').write_text('.validation/\n', encoding='utf-8')
        git('add', '--all'); git('commit', '--quiet', '-m', 'Canonical product snapshot without evaluator payload')
        state = workspace / '.validation'; state.mkdir()
        junction(state / 'runtime', ROOT / '.validation/runtime')
        if case['runtime'] == 'indexed':
            junction(state / 'qmd-runtime', ROOT / '.validation/qmd-runtime')
            built = search_rules.build(workspace, routing=True)
            assert built['documents'] == 165
            dump(OUT / 'development-index.json', built)
        permission = ':workspace-write' if case['runtime'] == 'indexed' else ':read-only'
        answer = OUT / (case['id'] + '-answer.json')
        argv = [cli, '-a', 'never', 'exec', '--ignore-user-config', '--ephemeral', '--skip-git-repo-check',
                '--cd', str(workspace), '--json', '--color', 'never', '--model', 'gpt-6.1-sol',
                '-c', 'model_reasoning_effort="high"', '-c', 'default_permissions="' + permission + '"',
                '-c', 'windows.sandbox="elevated"', '-c', 'model_provider="openai"',
                '-c', 'forced_login_method="chatgpt"', '-c', 'web_search="disabled"',
                '--output-schema', str(schema), '--output-last-message', str(answer), '-']
        prompt = ('Arbeite ausschließlich mit den Quellen in deinem aktuellen Arbeitsverzeichnis. '
                  'Keine Installation, Außenaktionen oder Quellenänderungen. Lokale abgeleitete Suchcaches sind erlaubt.\n\n' + case['prompt'])
        dump(OUT / (case['id'] + '-invocation.json'), {'argv': argv, 'prompt': prompt, 'prompt_sha256': sha(prompt.encode())})
        start = time.monotonic()
        process = subprocess.Popen(argv, env=env, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8')
        try:
            stdout, stderr = process.communicate(prompt, timeout=240)
        except subprocess.TimeoutExpired:
            subprocess.run(['taskkill', '/PID', str(process.pid), '/T', '/F'], capture_output=True)
            stdout, stderr = process.communicate(timeout=10)
            dump(OUT / (case['id'] + '-response.json'), {'status': 'BLOCKED', 'reason': '240s deadline; no retry'})
            raise SystemExit(2)
        row = {'status': 'RESPONSE_RECORDED' if process.returncode == 0 else 'BLOCKED', 'exit_code': process.returncode,
               'elapsed_seconds': round(time.monotonic() - start, 2),
               'source_bytes_unchanged': all((workspace / path).read_bytes() == body for path, body in files.items()),
               'git_status': git('status', '--porcelain').decode()}
        events = []
        for line in stdout.splitlines():
            try: events.append(json.loads(line))
            except ValueError: pass
        items = [event['item'] for event in events if event.get('type') == 'item.completed' and isinstance(event.get('item'), dict)]
        row.update(command_events=[{key: item[key] for key in ('type', 'command', 'exit_code', 'status', 'aggregated_output') if key in item}
                                   for item in items if item.get('type') == 'command_execution'],
                   completed_item_types=dict(Counter(item.get('type') for item in items)),
                   usage=[event['usage'] for event in events if 'usage' in event])
        if process.returncode:
            row['diagnostic'] = failure_diagnostic(stdout, stderr)
        else:
            row['answer'] = json.loads(answer.read_text(encoding='utf-8'))['answer']
        dump(OUT / (case['id'] + '-response.json'), row)
        print(json.dumps({'case': case['id'], 'status': row['status'], 'elapsed_seconds': row['elapsed_seconds']}), flush=True)
        if process.returncode or not row['source_bytes_unchanged'] or row['git_status']:
            raise SystemExit(2)


if __name__ == '__main__':
    main()
