"""Small, opt-in QMD BM25 search over this repository's explicit source selection."""
from __future__ import annotations

import argparse
import base64
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
from tools.check_public_entrypoints import PROJECT_CORE, MAX_PROJECT_BYTES, MAX_PROJECT_FILE_BYTES, validate_project_manifest
from tools.rule_relations import derive_relations

QMD_VERSION = '2.8.3'
BRIDGE = Path(__file__).with_name('search_rules_qmd.mjs')
ROUTING_SOURCES = {'master': 'Dokumentation/Skill-Handbuch.md', 'catalog': 'skill-catalog.yml',
                   'overlays': 'routing-overlays.yml', 'workflows': 'workflow-index.yml'}


class SearchError(Exception):
    def __init__(self, message, status='error'):
        super().__init__(message)
        self.status = status


def digest(body):
    return hashlib.sha256(body).hexdigest()


def canonical_json(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(',', ':')).encode('utf-8')


def encode_cursor(payload):
    """Corruption check and context binding, not a signature or authorization."""
    data = {**payload, 'checksum': digest(canonical_json(payload))}
    return base64.urlsafe_b64encode(canonical_json(data)).rstrip(b'=').decode('ascii')


def page_request(fingerprint, action, query, limit, cursor, default):
    payload = None
    if cursor is not None:
        try:
            if not isinstance(cursor, str) or len(cursor) > 2048 or not re.fullmatch(r'[A-Za-z0-9_-]+', cursor):
                raise ValueError('invalid encoding')
            data = json.loads(base64.b64decode(cursor + '=' * (-len(cursor) % 4), altchars=b'-_', validate=True))
            if not isinstance(data, dict) or set(data) != {'v', 'context', 'limit', 'offset', 'results', 'checksum'}:
                raise ValueError('invalid fields')
            payload = {key: value for key, value in data.items() if key != 'checksum'}
            if (type(data['v']) is not int or data['v'] != 1
                    or type(data['limit']) is not int or not 1 <= data['limit'] <= 50
                    or type(data['offset']) is not int or data['offset'] <= 0
                    or data['offset'] % data['limit']
                    or any(not isinstance(data[key], str) or not re.fullmatch('[0-9a-f]{64}', data[key])
                           for key in ('context', 'results', 'checksum'))
                    or encode_cursor(payload) != cursor):
                raise ValueError('invalid cursor')
        except (ValueError, TypeError, KeyError, UnicodeError) as exc:
            raise SearchError('Invalid or damaged continuation cursor.', 'invalid-cursor') from exc
    size = (payload['limit'] if payload else default) if limit is None else limit
    if type(size) is not int or not 1 <= size <= 50:
        raise SearchError('Routing page size must be an integer from 1 to 50.')
    context = digest(canonical_json({'fingerprint': fingerprint, 'action': action, 'query': query, 'limit': size}))
    if payload and payload['context'] != context:
        raise SearchError('Cursor does not match the source snapshot, action, query or page size.', 'invalid-cursor')
    return {'v': 1, 'context': context, 'limit': size, 'offset': payload['offset'] if payload else 0,
            'results': payload['results'] if payload else None}


def finish_page(items, request):
    result_hash = digest(canonical_json(items))
    offset, size = request['offset'], request['limit']
    if (request['results'] is not None and request['results'] != result_hash) or (offset and offset >= len(items)):
        raise SearchError('Cursor result set changed or its position is invalid.', 'invalid-cursor')
    selected = items[offset:offset + size]
    more = offset + len(selected) < len(items)
    cursor = encode_cursor({**request, 'offset': offset + size, 'results': result_hash}) if more else None
    return selected, {'offset': offset, 'page_size': size, 'has_more': more, 'next_cursor': cursor}


def derive_search_documents(files, facets):
    """Append source-bound catalog text; keep canonical bytes and paths intact."""
    documents = dict(files)
    for path, facet in facets.items():
        appendix = ('\n\n# Routing-Metadaten (abgeleitet)\nQuelle: skill-catalog.yml\n'
                    f"Skill-ID: {facet['id']}\nFachbereich: {facet['area']}\nZweck: {facet['purpose']}\n")
        documents[path] += appendix.encode('utf-8')
    return documents


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
    workflow_paths = []
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
                if not isinstance(item.get('area'), str) or not item['area'].strip():
                    raise SearchError('Invalid routing facet: area must be a nonempty string.')
                if not isinstance(item.get('purpose'), str) or len(item['purpose'].strip()) < 20:
                    raise SearchError('Invalid routing facet: purpose must be a string of at least 20 characters.')
                skill_entries[path] = item
            if (not isinstance(workflows.get('workflows'), list)
                    or any(not isinstance(path, str) or not path.startswith('Workflows/') or not path.endswith('.md')
                           for path in workflows['workflows'])):
                raise ValueError('invalid workflow index')
            workflow_paths = workflows['workflows']
            if len({path.casefold() for path in workflow_paths}) != len(workflow_paths):
                raise ValueError('duplicate workflow path')
            if not isinstance(overlays.get('overlays'), list):
                raise ValueError('invalid overlay registry')
            selected = sorted(PROJECT_CORE | {'Workflows/README.md'} | set(skill_entries))
            # Derived selection only: no second maintained catalog or modified source manifest.
            config = {**config, 'search': {'include': selected, 'exclude': config['search']['exclude']}}
        if not isinstance(selected, list):
            raise ValueError('not a list')
        names = list(dict.fromkeys([*selected, *entries, 'mara-project.json', *dependencies, *workflow_paths]))
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
    if routing:
        workflow_sources = {path: exported[path] for path in workflow_paths}
        if any(len(body) > MAX_PROJECT_FILE_BYTES for body in workflow_sources.values()):
            raise SearchError('Workflow dependency above 256 KiB.')
        if sum(map(len, workflow_sources.values())) > MAX_PROJECT_BYTES:
            raise SearchError('Workflow dependencies total above 1 MiB.')
        dependencies.update(workflow_sources)
        try:
            relations = derive_relations(catalog, overlays, workflow_sources,
                                         {path: digest(body) for path, body in dependencies.items()})
        except (ValueError, TypeError, KeyError, UnicodeError) as exc:
            raise SearchError('Invalid routing relations: ' + str(exc)) from exc
    files = {name: exported[name] for name in selected}
    facets = {path: {key: entry[key] for key in ('id', 'area', 'purpose')}
              for path, entry in skill_entries.items()}
    documents = derive_search_documents(files, facets)
    # Validate both original export and actual indexed bytes with the same budgets.
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
        if routing:
            for name, body in documents.items():
                (snapshot / name).write_bytes(body)
            errors, _ = validate_project_manifest(snapshot)
            if errors:
                raise SearchError('Derived search selection rejected: ' + '; '.join(errors))
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
        metadata.update(routing_format=3, routing_facets=facets, routing_relations=relations,
                        search_documents={name: digest(body) for name, body in sorted(documents.items())},
                        skills=skills, routing_dependencies={name: digest(body) for name, body in dependencies.items()},
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
        documents = derive_search_documents(files, metadata.get('routing_facets', {}))
        directory = Path(tempfile.mkdtemp(prefix='build-', dir=state))
        corpus = directory / 'corpus'
        corpus.mkdir()
        for name, body in documents.items():
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


def check_checkpoint(metadata, checkpoint):
    if checkpoint is not None:
        known = {edge['from'] for edge in metadata['routing_relations'] if edge['type'] == 'checkpoint'}
        if not isinstance(checkpoint, str) or 'checkpoint:' + checkpoint not in known:
            raise SearchError('Unknown registered checkpoint: ' + str(checkpoint))


def relation_subset(metadata, skill_id=None, workflow=None, checkpoint=None):
    if sum(value is not None for value in (skill_id, workflow, checkpoint)) != 1:
        raise SearchError('Specify exactly one relation selector: skill ID, workflow or checkpoint.')
    if any(value is not None and (not isinstance(value, str) or not value) for value in (skill_id, workflow, checkpoint)):
        raise SearchError('Relation selectors must be nonempty strings.')
    edges = metadata['routing_relations']
    if skill_id is not None:
        if skill_id not in {skill['id'] for skill in metadata['skills'].values()}:
            raise SearchError('Unknown canonical skill ID: ' + skill_id)
        node = 'skill:' + skill_id
        return [edge for edge in edges if (edge['type'] == 'related' and edge['from'] == node)
                or (edge['type'] == 'mentions' and edge['to'] == node)]
    if workflow is not None:
        if not workflow.startswith('Workflows/') or workflow not in metadata['routing_dependencies']:
            raise SearchError('Unknown registered workflow: ' + workflow)
        return [edge for edge in edges if edge['type'] == 'mentions' and edge['from'] == 'workflow:' + workflow]
    check_checkpoint(metadata, checkpoint)
    return [edge for edge in edges if edge['type'] == 'checkpoint' and edge['from'] == 'checkpoint:' + checkpoint]


def list_relations(root, skill_id=None, workflow=None, checkpoint=None, limit=None, cursor=None):
    """One explicitly selected neighborhood, without QMD or activation decisions."""
    with locked(root, routing=True):
        metadata, _ = read_snapshot(root, routing=True)
        edges = relation_subset(metadata, skill_id, workflow, checkpoint)
        selector = {'skill_id': skill_id, 'workflow': workflow, 'checkpoint': checkpoint}
        request = page_request(metadata['fingerprint'], 'relations', selector, limit, cursor, 25)
        selected, paging = finish_page(edges, request)
        after, _ = read_snapshot(root, routing=True)
        if metadata != after:
            raise SearchError('Sources changed during relation listing.', 'stale')
        return {'status': 'ready', 'mode': 'relations', 'revision': metadata['revision'],
                'fingerprint': metadata['fingerprint'], 'relations': selected, 'total_relations': len(edges),
                'assessment_performed': False, 'candidates_only': True,
                'routing_sources': dict(ROUTING_SOURCES), **paging}


def search(root, query, node=None, worker=call_worker, routing=False, limit=None, cursor=None, checkpoint=None):
    if not routing and (limit is not None or cursor is not None or checkpoint is not None):
        raise SearchError('Pagination and checkpoint hints are available only for routing search.')
    if not isinstance(query, str) or not query.strip() or len(query) > 500 or not query.isprintable():
        raise SearchError('Query must contain 1–500 printable characters.')
    with locked(root, routing):
        directory, metadata = current(root, routing)
        if routing:
            check_checkpoint(metadata, checkpoint)
        context = {'query': query, 'checkpoint': checkpoint}
        page = page_request(metadata['fingerprint'], 'search', context, limit, cursor, 10) if routing else None
        worker_limit = len(metadata['files']) if routing else 5
        result = invoke(worker, node, {'action': 'search', 'query': query, 'corpus': str(directory / 'corpus'),
                               'db': str(directory / 'index.sqlite'), 'paths': sorted(metadata['files']), 'limit': worker_limit})
        hits = result.get('hits')
        expected_hashes = metadata['search_documents'] if routing else metadata['files']
        if not isinstance(hits, list) or len(hits) > worker_limit:
            raise SearchError('Invalid QMD results.')
        seen = set()
        for hit in hits:
            if (not isinstance(hit, dict) or not isinstance(hit.get('path'), str) or hit['path'] not in metadata['files']
                    or hit['path'] in seen
                    or hit.get('content_sha256') != expected_hashes[hit['path']]
                    or not isinstance(hit.get('snippet'), str) or len(hit['snippet']) > 600
                    or type(hit.get('score')) not in (int, float) or not math.isfinite(hit['score'])):
                raise SearchError('Unexpected source or content in QMD results.')
            seen.add(hit['path'])
        _, after = current(root, routing)
        if metadata != after:
            raise SearchError('Sources changed during search.', 'stale')
        output = {'status': 'ready', 'revision': metadata['revision'], 'mode': 'bm25',
                  'fingerprint': metadata['fingerprint'], 'hits': hits}
        if routing:
            hits.sort(key=lambda hit: (-hit['score'], hit['path']))
            for hit in hits:
                path = hit['path']
                hit.update(search_document_sha256=hit['content_sha256'], content_sha256=metadata['files'][path],
                           snippet_origin='canonical-source', sources=[{'path': path, 'sha256': metadata['files'][path]}])
                if hit['path'] in metadata['skills']:
                    hit.update(kind='skill', skill=metadata['skills'][hit['path']])
                    hit['snippet_origin'] = 'derived-search-document'
                    hit['sources'].append({'path': 'skill-catalog.yml',
                                           'sha256': metadata['routing_dependencies']['skill-catalog.yml'],
                                           'fields': [f"skills[{hit['skill']['id']}].{key}" for key in ('id', 'area', 'purpose')]})
                else:
                    hit['kind'] = 'guide'
            output['total_matches'] = len(hits)
            output['hits'], paging = finish_page(hits, page)
            output.update(paging)
            seeds = {'skill:' + hit['skill']['id'] for hit in output['hits'] if hit['kind'] == 'skill'}
            hints = [edge for edge in metadata['routing_relations']
                     if (edge['type'] == 'related' and edge['from'] in seeds)
                     or (edge['type'] == 'mentions' and edge['to'] in seeds)
                     or (edge['type'] == 'checkpoint' and checkpoint is not None
                         and edge['from'] == 'checkpoint:' + checkpoint)]
            hints.sort(key=lambda edge: ({'checkpoint': 0, 'related': 1, 'mentions': 2}[edge['type']], edge['from'], edge['to']))
            output['routing_hints'] = {'items': hints[:20], 'total_relations': len(hints),
                                       'limit': 20, 'truncated': len(hints) > 20}
            output.update(candidates_only=True, routing_coverage=metadata['routing_coverage'],
                          routing_sources=dict(ROUTING_SOURCES))
        return output


def list_skills(root, limit=None, cursor=None):
    """Enumerate canonical descriptors, without opening QMD or a ready index."""
    with locked(root, routing=True):
        metadata, _ = read_snapshot(root, routing=True)
        page = page_request(metadata['fingerprint'], 'list-skills', None, limit, cursor, 25)
        catalog = yaml.safe_load(git(root, 'show', metadata['revision'] + ':skill-catalog.yml'))
        descriptors = []
        for entry in catalog['skills']:
            path = entry['path']
            lists = {}
            for field in ('capabilities', 'related'):
                values = entry.get(field, [])
                if (not isinstance(values, list) or any(not isinstance(value, str) for value in values)
                        or len(values) != len(set(values))):
                    raise SearchError('Invalid catalog descriptor list: ' + field)
                lists[field] = values
            descriptor = {**metadata['skills'][path], **metadata['routing_facets'][path], **lists,
                          'path': path, 'content_sha256': metadata['files'][path],
                          'sources': [{'path': path, 'sha256': metadata['files'][path]},
                                      {'path': 'skill-catalog.yml',
                                       'sha256': metadata['routing_dependencies']['skill-catalog.yml'],
                                       'fields': [f"skills[{entry['id']}].{key}" for key in
                                                  ('id', 'area', 'purpose', 'maturity', 'eval_coverage', 'capabilities', 'related')]}]}
            descriptors.append(descriptor)
        descriptors.sort(key=lambda item: item['id'])
        after, _ = read_snapshot(root, routing=True)
        if metadata != after:
            raise SearchError('Sources changed during descriptor listing.', 'stale')
        selected, paging = finish_page(descriptors, page)
        return {'status': 'ready', 'mode': 'catalog', 'revision': metadata['revision'],
                'fingerprint': metadata['fingerprint'], 'skills': selected, 'total_skills': len(descriptors),
                'assessment_performed': False, 'candidates_only': True,
                'routing_sources': dict(ROUTING_SOURCES), **paging}


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
    parser.add_argument('action', choices=('build', 'status', 'search', 'list-skills', 'relations'))
    parser.add_argument('query', nargs='?')
    parser.add_argument('--node')
    parser.add_argument('--routing', action='store_true', help='Search every catalogued canonical skill, independently of the pilot selection')
    parser.add_argument('--limit', type=int, help='Routing entries per page, from 1 to 50')
    parser.add_argument('--cursor', help='Continue the same routing request and source snapshot')
    parser.add_argument('--skill-id', help='Canonical skill whose direct relationships to list')
    parser.add_argument('--workflow', help='Registered workflow whose skill mentions to list')
    parser.add_argument('--checkpoint', help='Registered checkpoint whose candidates to inspect')
    args = parser.parse_args()
    try:
        options = {'routing': True} if args.routing else {}
        paging = {key: value for key, value in (('limit', args.limit), ('cursor', args.cursor)) if value is not None}
        selectors = {key: value for key, value in (('skill_id', args.skill_id), ('workflow', args.workflow),
                                                  ('checkpoint', args.checkpoint)) if value is not None}
        if args.action != 'search' and args.query is not None:
            raise SearchError('Query text is accepted only for search.')
        if not args.routing and (paging or selectors or args.action in ('list-skills', 'relations')):
            raise SearchError('These routing options require --routing.')
        if args.action in ('build', 'status') and (paging or selectors):
            raise SearchError('Paging and relation selectors do not apply to build/status.')
        if args.action != 'relations' and (args.skill_id is not None or args.workflow is not None):
            raise SearchError('Skill/workflow selectors apply only to relations.')
        if args.action == 'list-skills' and selectors:
            raise SearchError('Relation selectors do not apply to list-skills.')
        if args.action == 'relations':
            if len(selectors) != 1:
                raise SearchError('Specify exactly one relation selector.')
            result = list_relations(ROOT, **selectors, **paging)
        elif args.action == 'list-skills':
            result = list_skills(ROOT, **paging)
        elif args.action == 'search':
            if args.checkpoint is not None:
                options['checkpoint'] = args.checkpoint
            result = search(ROOT, args.query, args.node, **options, **paging)
        elif args.action == 'build':
            result = build(ROOT, args.node, **options)
        else:
            result = status(ROOT, **options)
    except SearchError as exc:
        result = {'status': exc.status, 'message': str(exc)}
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result['status'] == 'ready' else 2


if __name__ == '__main__':
    raise SystemExit(main())
