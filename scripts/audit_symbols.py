#!/usr/bin/env python3
"""Compare Director definition IDs with local mods without reading saves or logs."""
import argparse
from collections import defaultdict
import json
from pathlib import Path
import re

TOKEN = re.compile(r'#[^\n]*|"(?:\\.|[^"\\])*"|[{}=]|[^\s{}=#"]+')


def assignments(source):
    """Yield (parent keys, key, scalar or None) for Paradox assignments."""
    tokens = [m.group() for m in TOKEN.finditer(source) if not m.group().startswith('#')]
    parents = []
    index = 0
    while index < len(tokens):
        token = tokens[index]
        if token == '}':
            if parents:
                parents.pop()
        elif index + 2 < len(tokens) and tokens[index + 1] == '=':
            value = tokens[index + 2]
            yield tuple(parents), token, None if value == '{' else value.strip('"')
            if value == '{':
                parents.append(token)
            index += 2
        elif token == '{':
            parents.append('')
        index += 1


def definitions(root):
    """Collect definitions, keeping localisation languages in separate domains."""
    result = defaultdict(list)
    top_level = {
        'common/scripted_effects': 'effect',
        'common/scripted_triggers': 'trigger',
        'common/decisions/categories': 'decision_category',
    }
    for path in sorted(root.rglob('*')):
        if not path.is_file() or path.suffix.lower() not in ('.txt', '.gui', '.yml'):
            continue
        relative = path.relative_to(root).as_posix()
        source = path.read_text(encoding='utf-8-sig', errors='replace')
        if relative.startswith(('localisation/', 'localisation_synced/')) and path.suffix == '.yml':
            language = re.search(r'^\s*(l_\w+):', source, re.M)
            if language:
                for key in re.findall(r'^\s*([^\s:#]+):\d*\s+"', source, re.M):
                    result[(f'localisation/{language[1]}', key)].append(relative)
            continue
        folder = path.parent.relative_to(root).as_posix()
        for parents, key, value in assignments(source):
            kind = None
            symbol = key
            if folder in top_level and not parents and value is None:
                kind = top_level[folder]
            elif folder == 'common/scripted_guis' and parents == ('scripted_gui',) and value is None:
                kind = 'scripted_gui'
            elif relative.startswith('events/') and len(parents) == 1 and parents[0] in ('country_event', 'news_event', 'state_event') and key == 'id' and value:
                kind, symbol = 'event', value
            elif folder == 'common/decisions' and len(parents) == 1 and value is None:
                kind = 'decision'
            elif folder == 'common/scripted_localisation' and parents == ('defined_text',) and key == 'name' and value:
                kind, symbol = 'scripted_localisation', value
            if kind:
                result[(kind, symbol)].append(relative)
    return result


def audit(profile, target):
    if not target.is_dir():
        raise FileNotFoundError(f'Target directory does not exist: {target}')
    active = set(json.loads((profile / 'dlc_load.json').read_text())['enabled_mods'])
    own = definitions(target)
    report = {'target_definition_count': sum(map(len, own.values())),
              'target_duplicates': [{'kind': k, 'id': s, 'files': paths}
                                    for (k, s), paths in sorted(own.items()) if len(paths) > 1],
              'mods': [], 'collisions': [], 'skipped': []}
    for descriptor in sorted((profile / 'mod').glob('*.mod')):
        match = re.search(r'^\s*path\s*=\s*"([^"]+)"', descriptor.read_text(encoding='utf-8-sig'), re.M)
        if not match:
            report['skipped'].append({'mod': descriptor.stem, 'reason': 'no local path'})
            continue
        root = profile / match[1]
        if not root.is_dir():
            report['skipped'].append({'mod': descriptor.stem, 'reason': 'missing directory'})
            continue
        if root.resolve() == target.resolve():
            continue
        other = definitions(root)
        enabled = f'mod/{descriptor.name}' in active
        report['mods'].append({'mod': descriptor.stem, 'active': enabled,
                               'definition_count': sum(map(len, other.values()))})
        for kind, symbol in sorted(own.keys() & other.keys()):
            report['collisions'].append({'mod': descriptor.stem, 'active': enabled,
                'kind': kind, 'id': symbol, 'target_files': own[(kind, symbol)],
                'other_files': other[(kind, symbol)]})
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('profile', type=Path)
    parser.add_argument('--target', type=Path, default=Path(__file__).resolve().parents[1] / 'Smart_Nation_Director')
    args = parser.parse_args()
    print(json.dumps(audit(args.profile, args.target), ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
