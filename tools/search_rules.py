"""Small, opt-in QMD BM25 search over this repository's explicit source selection."""
from __future__ import annotations

import argparse
from contextlib import contextmanager
import hashlib
import io
import json
import math
import os
from pathlib import Path, PurePosixPath
import shutil
import stat
import subprocess
import sys
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.check_public_entrypoints import validate_project_manifest

QMD_VERSION = '2.8.3'
BRIDGE = Path(__file__).with_name('search_rules_qmd.mjs')


class SearchError(Exception):
    def __init__(self, message, status='error'):
        super().__init__(message)
        self.status = status


def digest(body):
    return hashlib.sha256(body).hexdigest()


def git(root, *args):
    try:
        return subprocess.check_output(['git', *args], cwd=root, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as exc:
        raise SearchError('Git source snapshot could not be read.') from exc


def state_dir(root):
    root = Path(root).resolve()
    state = root / '.validation' / 'rule-search'
    for path in (root / '.validation', state):
        if path.is_symlink() or path.is_junction() or not path.resolve().is_relative_to(root):
            raise SearchError('Redirected search state is not allowed.')
    state.mkdir(parents=True, exist_ok=True)
    return state


def read_snapshot(root, revision=None):
    """Validate the exported regular Git blobs, not a different working tree."""
    root = Path(root).resolve()
    commit = git(root, 'rev-parse', '--verify', (revision or 'HEAD') + '^{commit}').decode().strip()
    manifest = git(root, 'show', commit + ':mara-project.json')
    try:
        config = json.loads(manifest)
        selected = config['search']['include']
        entries = list(config['entrypoints'].values())
        if not isinstance(selected, list):
            raise ValueError('not a list')
        names = list(dict.fromkeys([*selected, *entries, 'mara-project.json']))
        for name in names:
            if (not isinstance(name, str) or not name or '\\' in name or ':' in name
                    or PurePosixPath(name).is_absolute() or '..' in PurePosixPath(name).parts
                    or any(c in name for c in '*?[]')):
                raise ValueError('unsafe literal path')
    except (ValueError, TypeError, KeyError, AttributeError) as exc:
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
    with tempfile.TemporaryDirectory(prefix='validate-', dir=state_dir(root)) as temporary:
        snapshot = Path(temporary)
        for name, body in exported.items():
            target = snapshot / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(body)
        errors, _ = validate_project_manifest(snapshot)
        if errors:
            raise SearchError('Source selection rejected: ' + '; '.join(errors))
    files = {name: exported[name] for name in selected}
    metadata = {'revision': commit, 'engine': 'qmd', 'version': QMD_VERSION, 'mode': 'bm25',
                'manifest_sha256': digest(manifest),
                'files': {name: digest(body) for name, body in sorted(files.items())}}
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
def locked(root):
    lock = state_dir(root) / 'search.lock'
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
    env = os.environ.copy()
    for name in tuple(env):
        if name.startswith(('OPENAI_', 'ANTHROPIC_', 'CODEX_API_')) or name in ('NODE_OPTIONS', 'NODE_PATH', 'QMD_TRUST_UPDATE_HOOKS'):
            env.pop(name, None)
    try:
        done = subprocess.run([node, str(BRIDGE)], input=json.dumps(request), capture_output=True,
                              text=True, encoding='utf-8', env=env, timeout=120)
        if done.returncode or len(done.stdout.encode()) > 1024 * 1024:
            raise SearchError('QMD runtime failed; no fallback. Check its local installation.')
        return json.loads(done.stdout)
    except (OSError, ValueError, subprocess.TimeoutExpired) as exc:
        raise SearchError('QMD runtime unavailable; install the pinned optional runtime.') from exc


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


def current(root):
    state = state_dir(root)
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
    actual, _ = read_snapshot(root)
    if metadata != actual:
        raise SearchError('Index is stale. Rebuild explicitly.', 'stale')
    return directory, metadata


def build(root, node='node', worker=call_worker):
    root = Path(root).resolve()
    with locked(root):
        state = state_dir(root)
        (state / 'current.json').unlink(missing_ok=True)
        metadata, files = read_snapshot(root)
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
        after, _ = read_snapshot(root)
        if after != metadata:
            raise SearchError('Sources changed during index build.', 'stale')
        (directory / 'snapshot.json').write_text(json.dumps(metadata, sort_keys=True), encoding='utf-8')
        with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', prefix='publish-', dir=state, delete=False) as handle:
            handle.write(json.dumps({'directory': directory.name}))
            pending = Path(handle.name)
        pending.replace(state / 'current.json')
        return {'status': 'ready', 'revision': metadata['revision'], 'documents': len(files),
                'mode': 'bm25', 'fingerprint': metadata['fingerprint']}


def search(root, query, node='node', worker=call_worker):
    if not isinstance(query, str) or not query.strip() or len(query) > 500 or not query.isprintable():
        raise SearchError('Query must contain 1–500 printable characters.')
    with locked(root):
        directory, metadata = current(root)
        result = invoke(worker, node, {'action': 'search', 'query': query, 'corpus': str(directory / 'corpus'),
                               'db': str(directory / 'index.sqlite'), 'paths': sorted(metadata['files'])})
        hits = result.get('hits')
        if not isinstance(hits, list) or len(hits) > 5:
            raise SearchError('Invalid QMD results.')
        for hit in hits:
            if (not isinstance(hit, dict) or not isinstance(hit.get('path'), str) or hit['path'] not in metadata['files']
                    or hit.get('content_sha256') != metadata['files'][hit['path']]
                    or not isinstance(hit.get('snippet'), str) or len(hit['snippet']) > 600
                    or type(hit.get('score')) not in (int, float) or not math.isfinite(hit['score'])):
                raise SearchError('Unexpected source or content in QMD results.')
        _, after = current(root)
        if metadata != after:
            raise SearchError('Sources changed during search.', 'stale')
        return {'status': 'ready', 'revision': metadata['revision'], 'mode': 'bm25',
                'fingerprint': metadata['fingerprint'], 'hits': hits}


def status(root):
    try:
        with locked(root):
            _, metadata = current(root)
            return {'status': 'ready', 'revision': metadata['revision'], 'mode': 'bm25',
                    'documents': len(metadata['files']), 'fingerprint': metadata['fingerprint']}
    except SearchError as exc:
        return {'status': exc.status, 'message': str(exc)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('build', 'status', 'search'))
    parser.add_argument('query', nargs='?')
    parser.add_argument('--node', default=shutil.which('node') or 'node')
    args = parser.parse_args()
    try:
        result = (build(ROOT, args.node) if args.action == 'build' else status(ROOT)
                  if args.action == 'status' else search(ROOT, args.query, args.node))
    except SearchError as exc:
        result = {'status': exc.status, 'message': str(exc)}
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result['status'] == 'ready' else 2


if __name__ == '__main__':
    raise SystemExit(main())
