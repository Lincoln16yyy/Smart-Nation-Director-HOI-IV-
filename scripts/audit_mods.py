#!/usr/bin/env python3
"""Inventory local descriptors and compare byte-identical and divergent paths."""
import argparse
from collections import Counter
from itertools import combinations
import json
from pathlib import Path
import re

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('profile', type=Path, help='HOI4 user directory with mod/ and dlc_load.json')
args = parser.parse_args()
active = set(json.loads((args.profile / 'dlc_load.json').read_text())['enabled_mods'])
inventories = {}
for descriptor in sorted((args.profile / 'mod').glob('*.mod')):
    raw = descriptor.read_text(encoding='utf-8-sig')
    match = re.search(r'(?m)^path\s*=\s*"([^"]+)"', raw)
    if not match:
        print(f'{descriptor.name}: sem path local; exige inspeção separada')
        continue
    root = args.profile / match[1]
    inner = (root / 'descriptor.mod').read_text(encoding='utf-8-sig')
    header = re.compile(r'(?m)^(?:name|version|supported_version|remote_file_id|replace_path)\s*=.*$')
    files = {
        item.relative_to(root).as_posix().casefold(): item
        for item in root.rglob('*') if item.is_file() and item != root / 'descriptor.mod'
    }
    inventories[descriptor.stem] = files
    print(descriptor.stem, 'ativo' if f'mod/{descriptor.name}' in active else 'inativo', len(files))
    for line in header.findall(raw):
        print(' ', line)
    if header.findall(raw) != header.findall(inner):
        print('  campos internos:', header.findall(inner))
    for source in [raw, inner]:
        if 'dependencies' in source:
            print('  dependências:', re.findall(r'dependencies\s*=\s*\{([^}]*)\}', source))

for (left, first), (right, second) in combinations(inventories.items(), 2):
    matches = Counter()
    example = []
    for key in sorted(first.keys() & second.keys()):
        a, b = first[key], second[key]
        if a.stat().st_size == b.stat().st_size and a.read_bytes() == b.read_bytes():
            matches['idênticos'] += 1
        else:
            matches['diferentes'] += 1
            if len(example) < 3:
                example.append(key)
    if matches:
        print(left, '+', right, dict(matches), example)
