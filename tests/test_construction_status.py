"""Check status selection across combinations of independent construction flags."""
from itertools import product
from pathlib import Path
import unittest

from scripts.audit_symbols import TOKEN


SOURCE = Path(__file__).resolve().parents[1] / 'Smart_Nation_Director/common/scripted_localisation/snd_construction_localisation.txt'


def parse(source):
    tokens = iter(m.group() for m in TOKEN.finditer(source) if not m.group().startswith('#'))

    def block():
        result = []
        for key in tokens:
            if key == '}':
                break
            if next(tokens) != '=':
                raise ValueError('Expected assignment')
            value = next(tokens)
            result.append((key, block() if value == '{' else value))
        return result

    return block()


def matches(conditions, flags, external):
    for key, value in conditions:
        if key == 'NOT':
            passed = not matches(value, flags, external)
        elif key == 'AND':
            passed = matches(value, flags, external)
        elif key == 'has_country_flag':
            passed = value in flags
        elif key == 'snd_construction_managed_externally':
            passed = external
        else:
            raise ValueError(f'Unsupported condition: {key}')
        if not passed:
            return False
    return True


class ConstructionStatusTests(unittest.TestCase):
    def test_all_flag_combinations_select_one_accurate_status(self):
        branches = next(value for key, value in parse(SOURCE.read_text())
                        if key == 'defined_text' and ('name', 'GetSndAutoConstructionStatus') in value)
        branches = [dict(value) for key, value in branches if key == 'text']
        names = ('snd_auto_construction', 'snd_pilot_enabled', 'snd_auto_construction_cooldown',
                 'snd_auto_project_pending', 'snd_construction_proposal_deferred',
                 'snd_construction_advisory', 'snd_construction_supervised', 'snd_construction_proposal_pending')
        for values in product((False, True), repeat=len(names) + 1):
            flags = {name for name, enabled in zip(names, values) if enabled}
            external = values[-1]
            if names[0] not in flags:
                expected = 'snd_auto_construction_off'
            elif external:
                expected = 'snd_auto_construction_suspended'
            elif names[1] in flags:
                expected = 'snd_auto_construction_pilot_waiting'
            elif names[2] in flags:
                expected = 'snd_auto_construction_waiting'
            elif names[3] in flags:
                expected = 'snd_auto_construction_pending'
            elif names[4] in flags:
                expected = 'snd_auto_construction_deferred'
            elif names[5] in flags:
                expected = 'snd_construction_advisory_active'
            elif names[6] in flags and names[7] in flags:
                expected = 'snd_auto_construction_approval'
            elif names[6] in flags:
                expected = 'snd_auto_construction_supervised'
            else:
                expected = 'snd_auto_construction_active'
            selected = [branch['localization_key'] for branch in branches
                        if matches(branch['trigger'], flags, external)]
            self.assertEqual(selected, [expected], (flags, external))


if __name__ == '__main__':
    unittest.main()
