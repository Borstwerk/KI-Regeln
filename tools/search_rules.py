"""Small, opt-in QMD BM25 search over this repository's explicit source selection."""
from __future__ import annotations

import argparse
from contextlib import contextmanager
import hashlib
import io
import json
import math
import os
import re
from pathlib import Path, PurePosixPath
import shutil
import stat
import subprocess
import sys
import tempfile
import zipfile
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.check_public_entrypoints import PROJECT_CORE, validate_project_manifest

QMD_VERSION = '2.8.3'
BRIDGE = Path(__file__).with_name('search_rules_qmd.mjs')


class SearchError(Exception):
    def __init__(self, message, status='error'):
        super().__init__(message)
        self.status = status


def digest(body):
    return hashlib.sha256(body).hexdigest()


def resolve_node(explicit=None):
    """Reuse an installed executable; never install or replace an explicit choice."""
    found = shutil.which(explicit if explicit is not None else 'node') if explicit != '' else None
    if not found and explicit is None:
        executable = 'node.exe' if os.name == 'nt' else 'node'
        bundled = Path.home() / '.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin' / executable
        if bundled.is_file():
            found = str(bundled)
    if not found:
        raise SearchError('Node.js executable not found. Supply -NodePath (or --node) for an existing Node.js 22+ runtime.',
                          'runtime-missing')
    return str(Path(found).resolve())


def git(root, *args):
    try:
        return subprocess.check_output(['git', *args], cwd=root, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as exc:
        raise SearchError('Git source snapshot could not be read.') from exc


def state_dir(root, routing=False):
    root = Path(root).resolve()
    state = root / '.validation' / ('rule-routing' if routing else 'rule-search')
    for path in (root / '.validation', state):
        if path.is_symlink() or path.is_junction() or not path.resolve().is_relative_to(root):
            raise SearchError('Redirected search state is not allowed.')
    state.mkdir(parents=True, exist_ok=True)
    return state


def read_snapshot(root, revision=None, routing=False):
    """Validate the exported regular Git blobs, not a different working tree."""
    root = Path(root).resolve()
    commit = git(root, 'rev-parse', '--verify', (revision or 'HEAD') + '^{commit}').decode().strip()
    manifest = git(root, 'show', commit + ':mara-project.json')
    dependencies = {}
    skill_entries = {}
    try:
        config = json.loads(manifest)
        selected = config['search']['include']
        entries = list(config['entrypoints'].values())
        if routing:
            for name in ('skill-catalog.yml', 'workflow-index.yml', 'routing-overlays.yml'):
                dependencies[name] = git(root, 'show', commit + ':' + name)
            catalog = yaml.safe_load(dependencies['skill-catalog.yml'])
            workflows = yaml.safe_load(dependencies['workflow-index.yml'])
            overlays = yaml.safe_load(dependencies['routing-overlays.yml'])
            ids, folded_ids, folded_paths = set(), set(), set()
            if not isinstance(catalog.get('skills'), list) or not catalog['skills']:
                raise ValueError('missing skill catalog')
            for item in catalog['skills']:
                identifier, path = item['id'], item['path']
                if (not isinstance(identifier, str) or not re.fullmatch(r'[a-z0-9][a-z0-9-]*', identifier)
                        or not isinstance(path, str)
                        or not path.endswith('/Skills/' + identifier + '/SKILL.md')
                        or identifier.casefold() in folded_ids or path.casefold() in folded_paths):
                    raise ValueError('duplicate or invalid canonical skill')
                ids.add(identifier)
                folded_ids.add(identifier.casefold())
                folded_paths.add(path.casefold())
                skill_entries[path] = item
            if (not isinstance(workflows.get('workflows'), list)
                    or any(not isinstance(path, str) or not path.startswith('Workflows/') or not path.endswith('.md')
                           for path in workflows['workflows'])):
                raise ValueError('invalid workflow index')
            if (not isinstance(overlays.get('overlays'), list)
                    or any(item.get('skill') not in ids for item in overlays['overlays'])):
                raise ValueError('unknown overlay owner')
            selected = sorted(PROJECT_CORE | {'Workflows/README.md'} | set(skill_entries))
            # Derived selection only: no second maintained catalog or modified source manifest.
            config = {**config, 'search': {'include': selected, 'exclude': config['search']['exclude']}}
        if not isinstance(selected, list):
            raise ValueError('not a list')
        names = list(dict.fromkeys([*selected, *entries, 'mara-project.json', *dependencies]))
        for name in names:
            if (not isinstance(name, str) or not name or '\\' in name or ':' in name
                    or PurePosixPath(name).is_absolute() or '..' in PurePosixPath(name).parts
                    or any(c in name for c in '*?[]')):
                raise ValueError('unsafe literal path')
    except (ValueError, TypeError, KeyError, AttributeError, yaml.YAMLError) as exc:
        raise SearchError('Invalid explicit source manifest.') from exc
    tree = {}
    for row in git(root, 'ls-tree', '-rz', '--full-tree', commit, '--', *names).split(b'\0'):
        if not row:
            continue
        entry, path = row.split(b'\t', 1)
        mode, kind, object_id = entry.split()
        if kind != b'blob' or mode not in (b'100644', b'100755'):
            raise SearchError('Source snapshot contains a non-regular Git entry.')
        tree[path.decode('utf-8')] = object_id.decode()
    if set(tree) != set(names):
        raise SearchError('Source snapshot is incomplete.')
    archive = git(root, '-c', 'core.autocrlf=false', 'archive', '--format=zip', commit, '--', *names)
    exported = {}
    with zipfile.ZipFile(io.BytesIO(archive)) as zipped:
        for info in zipped.infolist():
            if info.is_dir():
                continue
            mode = info.external_attr >> 16
            if info.filename not in names or (mode and not stat.S_ISREG(mode)):
                raise SearchError('Source snapshot contains a non-regular or unexpected file.')
            body = zipped.read(info)
            object_id = tree[info.filename]
            algorithm = hashlib.sha1 if len(object_id) == 40 else hashlib.sha256
            if algorithm(b'blob ' + str(len(body)).encode() + b'\0' + body).hexdigest() != object_id:
                raise SearchError('Archive content differs from the committed source blob.')
            exported[info.filename] = body
    if set(exported) != set(names):
        raise SearchError('Source snapshot is incomplete.')
    # The existing manifest validator owns selection limits and forbidden sources.
    with tempfile.TemporaryDirectory(prefix='validate-', dir=state_dir(root, routing)) as temporary:
        snapshot = Path(temporary)
        for name, body in exported.items():
            target = snapshot / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(body)
        if routing:
            (snapshot / 'mara-project.json').write_text(json.dumps(config), encoding='utf-8')
        errors, _ = validate_project_manifest(snapshot)
        if errors:
            raise SearchError('Source selection rejected: ' + '; '.join(errors))
    files = {name: exported[name] for name in selected}
    metadata = {'revision': commit, 'engine': 'qmd', 'version': QMD_VERSION, 'mode': 'bm25',
                'manifest_sha256': digest(manifest),
                'files': {name: digest(body) for name, body in sorted(files.items())}}
    if routing:
        skills = {}
        for path, entry in skill_entries.items():
            try:
                text = files[path].decode('utf-8')
                front = yaml.safe_load(text.split('---', 2)[1]) if text.startswith('---\n') else None
                if (not isinstance(front, dict) or front.get('name') != entry['id']
                        or not isinstance(front.get('description'), str) or not front['description'].strip()):
                    raise ValueError('invalid canonical descriptor')
            except (UnicodeError, ValueError, IndexError, yaml.YAMLError) as exc:
                raise SearchError('Invalid canonical skill description: ' + path) from exc
            skills[path] = {'id': entry['id'], 'description': front['description'],
                            'maturity': entry.get('maturity'), 'eval_coverage': entry.get('eval_coverage')}
        metadata.update(skills=skills, routing_dependencies={name: digest(body) for name, body in dependencies.items()},
                        routing_coverage={'skills': len(skills), 'indexed_skills': len(skills)})
    metadata['fingerprint'] = digest(json.dumps(metadata, sort_keys=True).encode())
    if revision is None:
        # Git LF blobs are canonical; ordinary Windows checkout CRLF is equivalent.
        for name, expected in exported.items():
            path = root / name
            parts = PurePosixPath(name).parts
            redirected = any(root.joinpath(*parts[:i]).is_symlink() or root.joinpath(*parts[:i]).is_junction()
                             for i in range(1, len(parts) + 1))
            if (redirected or not path.is_file()
                    or not path.resolve().is_relative_to(root)):
                raise SearchError('Current sources are missing or redirected.', 'stale')
            if path.read_bytes().replace(b'\r\n', b'\n') != expected.replace(b'\r\n', b'\n'):
                raise SearchError('Commit selected source changes before building/searching.', 'stale')
        if git(root, 'rev-parse', 'HEAD').decode().strip() != commit:
            raise SearchError('Source revision changed during inspection.', 'stale')
    return metadata, files


@contextmanager
def locked(root, routing=False):
    lock = state_dir(root, routing) / 'search.lock'
    try:
        handle = lock.open('x')
    except FileExistsError as exc:
        raise SearchError('Another search/build holds the lock.', 'busy') from exc
    try:
        with handle:
            handle.write(str(os.getpid()))
        yield
    finally:
        lock.unlink(missing_ok=True)


def call_worker(node, request):
    node = resolve_node(node)
    env = os.environ.copy()
    for name in tuple(env):
        if name.startswith(('OPENAI_', 'ANTHROPIC_', 'CODEX_API_')) or name in ('NODE_OPTIONS', 'NODE_PATH', 'QMD_TRUST_UPDATE_HOOKS'):
            env.pop(name, None)
    try:
        done = subprocess.run([node, str(BRIDGE)], input=json.dumps(request), capture_output=True,
                              text=True, encoding='utf-8', env=env, timeout=120)
        if done.returncode or len(done.stdout.encode()) > 1024 * 1024:
            raise SearchError('QMD runtime failed; no fallback. Check its local installation.')
        try:
            return json.loads(done.stdout)
        except ValueError as exc:
            raise SearchError('QMD returned an invalid JSON response.', 'runtime-error') from exc
    except subprocess.TimeoutExpired as exc:
        raise SearchError('QMD exceeded its 120 second runtime limit.', 'runtime-timeout') from exc
    except OSError as exc:
        raise SearchError('The selected Node.js executable could not be started. Check -NodePath (or --node).',
                          'runtime-missing') from exc


def invoke(worker, node, request):
    try:
        result = worker(node, request)
        if not isinstance(result, dict):
            raise ValueError('invalid worker response')
        return result
    except SearchError:
        raise
    except Exception as exc:
        raise SearchError('QMD operation failed; index/results are not ready.') from exc


def plain_cache_entry(path, boundary):
    if path.is_symlink() or path.is_junction() or not path.resolve().is_relative_to(boundary):
        raise SearchError('Redirected cache entries are not allowed.')


def current(root, routing=False):
    state = state_dir(root, routing)
    try:
        plain_cache_entry(state / 'current.json', state)
        pointer = json.loads((state / 'current.json').read_text(encoding='utf-8'))
        folder = pointer['directory']
        if not isinstance(folder, str) or not folder.startswith('build-') or Path(folder).name != folder:
            raise ValueError('invalid build directory')
        directory = state / folder
        if directory.is_symlink() or directory.is_junction() or not directory.resolve().is_relative_to(state):
            raise ValueError('redirected build')
        for name in ('snapshot.json', 'corpus', 'index.sqlite', 'index.sqlite-wal', 'index.sqlite-shm', 'index.sqlite-journal'):
            plain_cache_entry(directory / name, directory)
        metadata = json.loads((directory / 'snapshot.json').read_text(encoding='utf-8'))
        if not (directory / 'index.sqlite').is_file():
            raise ValueError('missing database')
        if not (directory / 'corpus').is_dir():
            raise ValueError('missing corpus')
    except (OSError, ValueError, KeyError, TypeError) as exc:
        raise SearchError('No complete index. Build it explicitly first.', 'missing') from exc
    actual, _ = read_snapshot(root, routing=routing)
    if metadata != actual:
        raise SearchError('Index is stale. Rebuild explicitly.', 'stale')
    return directory, metadata


def build(root, node=None, worker=call_worker, routing=False):
    root = Path(root).resolve()
    with locked(root, routing):
        state = state_dir(root, routing)
        (state / 'current.json').unlink(missing_ok=True)
        metadata, files = read_snapshot(root, routing=routing)
        directory = Path(tempfile.mkdtemp(prefix='build-', dir=state))
        corpus = directory / 'corpus'
        corpus.mkdir()
        for name, body in files.items():
            target = corpus / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(body)
        db = directory / 'index.sqlite'
        result = invoke(worker, node, {'action': 'build', 'corpus': str(corpus), 'db': str(db), 'paths': sorted(files)})
        if (result.get('skipped') != 0 or result.get('paths') != sorted(files) or not db.is_file()):
            raise SearchError('QMD produced an incomplete index.')
        after, _ = read_snapshot(root, routing=routing)
        if after != metadata:
            raise SearchError('Sources changed during index build.', 'stale')
        (directory / 'snapshot.json').write_text(json.dumps(metadata, sort_keys=True), encoding='utf-8')
        with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', prefix='publish-', dir=state, delete=False) as handle:
            handle.write(json.dumps({'directory': directory.name}))
            pending = Path(handle.name)
        pending.replace(state / 'current.json')
        output = {'status': 'ready', 'revision': metadata['revision'], 'documents': len(files),
                  'mode': 'bm25', 'fingerprint': metadata['fingerprint']}
        if routing:
            output['routing_coverage'] = metadata['routing_coverage']
        return output


def search(root, query, node=None, worker=call_worker, routing=False):
    if not isinstance(query, str) or not query.strip() or len(query) > 500 or not query.isprintable():
        raise SearchError('Query must contain 1–500 printable characters.')
    with locked(root, routing):
        directory, metadata = current(root, routing)
        limit = 10 if routing else 5
        result = invoke(worker, node, {'action': 'search', 'query': query, 'corpus': str(directory / 'corpus'),
                               'db': str(directory / 'index.sqlite'), 'paths': sorted(metadata['files']), 'limit': limit})
        hits = result.get('hits')
        if not isinstance(hits, list) or len(hits) > limit:
            raise SearchError('Invalid QMD results.')
        for hit in hits:
            if (not isinstance(hit, dict) or not isinstance(hit.get('path'), str) or hit['path'] not in metadata['files']
                    or hit.get('content_sha256') != metadata['files'][hit['path']]
                    or not isinstance(hit.get('snippet'), str) or len(hit['snippet']) > 600
                    or type(hit.get('score')) not in (int, float) or not math.isfinite(hit['score'])):
                raise SearchError('Unexpected source or content in QMD results.')
        _, after = current(root, routing)
        if metadata != after:
            raise SearchError('Sources changed during search.', 'stale')
        output = {'status': 'ready', 'revision': metadata['revision'], 'mode': 'bm25',
                  'fingerprint': metadata['fingerprint'], 'hits': hits}
        if routing:
            for hit in hits:
                if hit['path'] in metadata['skills']:
                    hit.update(kind='skill', skill=metadata['skills'][hit['path']])
                else:
                    hit['kind'] = 'guide'
            output.update(candidates_only=True, routing_coverage=metadata['routing_coverage'],
                          routing_sources={'master': 'Dokumentation/Skill-Handbuch.md', 'catalog': 'skill-catalog.yml',
                                           'overlays': 'routing-overlays.yml', 'workflows': 'workflow-index.yml'})
        return output


def status(root, routing=False):
    try:
        with locked(root, routing):
            _, metadata = current(root, routing)
            output = {'status': 'ready', 'revision': metadata['revision'], 'mode': 'bm25',
                      'documents': len(metadata['files']), 'fingerprint': metadata['fingerprint']}
            if routing:
                output['routing_coverage'] = metadata['routing_coverage']
            return output
    except SearchError as exc:
        return {'status': exc.status, 'message': str(exc)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('build', 'status', 'search'))
    parser.add_argument('query', nargs='?')
    parser.add_argument('--node')
    parser.add_argument('--routing', action='store_true', help='Search every catalogued canonical skill, independently of the pilot selection')
    args = parser.parse_args()
    try:
        options = {'routing': True} if args.routing else {}
        result = (build(ROOT, args.node, **options) if args.action == 'build' else status(ROOT, **options)
                  if args.action == 'status' else search(ROOT, args.query, args.node, **options))
    except SearchError as exc:
        result = {'status': exc.status, 'message': str(exc)}
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result['status'] == 'ready' else 2


if __name__ == '__main__':
    raise SystemExit(main())
