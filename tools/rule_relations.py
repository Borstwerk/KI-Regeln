"""Derive source-backed relationship hints; never decide which skill to activate."""
import hashlib
import re

PHASES = frozenset({'presentation', 'communication', 'assurance', 'security'})
CHECKPOINTS = frozenset({'post-primary', 'pre-execution', 'pre-completion', 'pre-output'})


def _strings(value, label, required=False):
    if (not isinstance(value, list) or (required and not value)
            or any(not isinstance(item, str) or not item.strip() for item in value)
            or len(value) != len(set(value))):
        raise ValueError('Invalid or duplicate ' + label)
    return value


def _mentions(text, skills):
    found, fence = {}, None
    for number, line in enumerate(text.splitlines(), 1):
        marker = re.match(r' {0,3}(`{3,}|~{3,})(.*)$', line)
        if fence:
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= fence[1] and not marker[2].strip():
                fence = None
            continue
        if marker:
            fence = (marker[1][0], len(marker[1]))
            continue
        # Consume longer code spans as a whole, so nested-looking single ticks
        # inside them are literal text rather than another mention.
        for span in re.finditer(r'(?<![\\`])(`+)(.*?)\1(?!`)', line):
            identifier = span[2]
            if len(span[1]) == 1 and identifier in skills:
                found.setdefault(identifier, set()).add(number)
    return found


def derive_relations(catalog, overlays, workflow_sources, source_hashes):
    """Use declarations from one validated snapshot; return one-hop edges only."""
    if not isinstance(source_hashes, dict):
        raise ValueError('Invalid source hashes')

    def source(path):
        checksum = source_hashes.get(path)
        if not isinstance(checksum, str) or not re.fullmatch('[0-9a-f]{64}', checksum):
            raise ValueError('Invalid source hash: ' + path)
        return {'path': path, 'sha256': checksum}

    if not isinstance(catalog, dict) or not isinstance(catalog.get('skills'), list) or not catalog['skills']:
        raise ValueError('Invalid skill catalog')
    skills, folded_paths = {}, set()
    for entry in catalog['skills']:
        if (not isinstance(entry, dict) or not isinstance(entry.get('id'), str)
                or not re.fullmatch('[a-z0-9][a-z0-9-]*', entry['id'])
                or not isinstance(entry.get('path'), str) or not entry['path'].strip()):
            raise ValueError('Invalid skill identity')
        identifier, path = entry['id'], entry['path']
        if identifier in skills or path.casefold() in folded_paths:
            raise ValueError('Duplicate skill identity or path: ' + identifier)
        skills[identifier] = path
        folded_paths.add(path.casefold())

    edges = []
    catalog_source = source('skill-catalog.yml')
    for entry in catalog['skills']:
        for target in _strings(entry.get('related', []), 'related targets'):
            if target not in skills:
                raise ValueError('Unknown related target: ' + target)
            edges.append({'type': 'related', 'from': 'skill:' + entry['id'], 'to': 'skill:' + target,
                          'target_path': skills[target],
                          'source': {**catalog_source, 'field': f"skills[{entry['id']}].related"}})
    if not isinstance(overlays, dict) or not isinstance(overlays.get('overlays'), list):
        raise ValueError('Invalid overlay registry')
    overlay_source, seen_overlays = source('routing-overlays.yml'), set()
    for entry in overlays['overlays']:
        if not isinstance(entry, dict) or set(entry) != {'skill', 'phase', 'checkpoints'}:
            raise ValueError('Invalid overlay fields')
        target = entry['skill']
        if not isinstance(target, str) or target not in skills:
            raise ValueError('Unknown overlay target: ' + str(target))
        if target in seen_overlays:
            raise ValueError('Duplicate overlay target: ' + target)
        seen_overlays.add(target)
        phase = entry['phase']
        if not isinstance(phase, str) or phase not in PHASES:
            raise ValueError('Invalid overlay phase')
        for checkpoint in _strings(entry['checkpoints'], 'overlay checkpoints', required=True):
            if checkpoint not in CHECKPOINTS:
                raise ValueError('Invalid overlay checkpoint: ' + checkpoint)
            edges.append({'type': 'checkpoint', 'from': 'checkpoint:' + checkpoint,
                          'to': 'skill:' + target, 'target_path': skills[target], 'phase': phase,
                          'source': {**overlay_source, 'field': f'overlays[{target}].checkpoints'}})
    if not isinstance(workflow_sources, dict):
        raise ValueError('Invalid workflow sources')
    for path, body in workflow_sources.items():
        if (not isinstance(path, str) or not path.startswith('Workflows/') or not path.endswith('.md')
                or '\\' in path or ':' in path or '..' in path.split('/')):
            raise ValueError('Invalid workflow path')
        evidence = source(path)
        if not isinstance(body, bytes):
            raise ValueError('Workflow source must be UTF-8 bytes: ' + path)
        if hashlib.sha256(body).hexdigest() != evidence['sha256']:
            raise ValueError('Workflow source hash mismatch: ' + path)
        try:
            text = body.decode('utf-8')
        except UnicodeError as exc:
            raise ValueError('Workflow source is not UTF-8: ' + path) from exc
        for target, lines in _mentions(text, skills).items():
            edges.append({'type': 'mentions', 'from': 'workflow:' + path, 'to': 'skill:' + target,
                          'target_path': skills[target], 'source': {**evidence, 'lines': sorted(lines)}})
    return sorted(edges, key=lambda edge: (edge['type'], edge['from'], edge['to']))
