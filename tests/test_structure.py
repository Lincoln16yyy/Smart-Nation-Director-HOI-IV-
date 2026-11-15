"""Static checks for the original pilot package. Runtime semantics are tested in HOI4."""
from pathlib import Path
import re
import unittest

REPO = Path(__file__).resolve().parents[1]
MOD = REPO / 'Smart_Nation_Director'


class PackageTests(unittest.TestCase):
    def test_descriptors_match(self):
        inner = (MOD / 'descriptor.mod').read_text()
        outer = (REPO / 'Smart_Nation_Director.mod').read_text()
        self.assertEqual(outer, inner + 'path="mod/Smart_Nation_Director"\n')
        self.assertNotIn('replace_path', inner)
        self.assertIn('supported_version="1.19.3.*"', inner)

    def test_script_braces_and_prefixes(self):
        for path in MOD.rglob('*.txt'):
            with self.subTest(path=path):
                self.assertTrue(path.name.startswith('snd_'))
                source = re.sub(r'"(?:\\.|[^"\\])*"|#[^\n]*', '', path.read_text())
                depth = 0
                for brace in re.findall(r'[{}]', source):
                    depth += 1 if brace == '{' else -1
                    self.assertGreaterEqual(depth, 0)
                self.assertEqual(depth, 0)

    def test_event_references_and_localisation(self):
        event_text = (MOD / 'events/snd_events.txt').read_text()
        event_ids = re.findall(r'\bid\s*=\s*(snd\.\d+)', event_text)
        effect = (MOD / 'common/scripted_effects/snd_effects.txt').read_text()
        decisions = (MOD / 'common/decisions/snd_decisions.txt').read_text()
        references = re.findall(r'country_event\s*=\s*\{\s*id\s*=\s*(snd\.\d+)', effect + decisions)
        self.assertCountEqual(event_ids, references)
        scripted_loc = (MOD / 'common/scripted_localisation/snd_industry_localisation.txt').read_text()
        required = {'snd_director_category'}
        required.update(re.findall(r'localization_key\s*=\s*(snd_\w+)', scripted_loc))
        getters = re.findall(r'name\s*=\s*(GetSnd\w+)', scripted_loc)
        for decision in re.findall(r'^    (snd_\w+) =', decisions, re.M):
            required.update([decision, decision + '_desc'])
        required.update(re.findall(r'\b(?:title|desc|text|name)\s*=\s*(snd\.\S+?)(?=\s)', event_text))
        for language in ('english', 'braz_por'):
            with self.subTest(language=language):
                path = MOD / 'localisation' / language / f'snd_l_{language}.yml'
                self.assertTrue(path.read_bytes().startswith(b'\xef\xbb\xbf'))
                header, *lines = path.read_text(encoding='utf-8-sig').splitlines()
                self.assertEqual(header, f'l_{language}:')
                keys = [re.fullmatch(r' ([\w.]+):0 "[^"]+"', line)[1] for line in lines]
                self.assertCountEqual(keys, required)
                for line in lines:
                    for variable in re.findall(r"\[\?(snd_\w+)", line):
                        self.assertIn(f"{variable} =", decisions + effect)
                self.assertEqual(set(re.findall(r'\[Root\.(GetSnd\w+)\]', '\n'.join(lines))), set(getters))

    def test_pilot_uses_regular_queue(self):
        effect = (MOD / 'common/scripted_effects/snd_effects.txt').read_text()
        self.assertIn('instant_build = no', effect)
        self.assertNotIn('instant_build = yes', effect)
        self.assertIn('set_country_flag = snd_pilot_dispatched', effect)
        self.assertIn('clr_country_flag = snd_pilot_enabled', effect)


if __name__ == '__main__':
    unittest.main()
