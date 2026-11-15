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
        scripted_loc = '\n'.join(
            path.read_text() for path in (MOD / 'common/scripted_localisation').glob('snd_*.txt')
        )
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
                    for variable in re.findall(r"\[\?(?:ROOT\.)?(snd_\w+)", line):
                        self.assertIn(f"{variable} =", decisions + effect)
                self.assertEqual(set(re.findall(r'\[Root\.(GetSnd\w+)\]', '\n'.join(lines))), set(getters))

    def test_external_construction_blocks_authorization_and_dispatch(self):
        decisions = (MOD / 'common/decisions/snd_decisions.txt').read_text()
        on_actions = (MOD / 'common/on_actions/snd_on_actions.txt').read_text()
        guard = 'NOT = { has_country_flag = snd_external_construction }'

        external_controls, pilot = decisions.split('    snd_enable_pilot = {', 1)
        self.assertIn('set_country_flag = snd_external_construction', external_controls)
        self.assertIn('clr_country_flag = snd_external_construction', external_controls)
        self.assertNotIn('clr_country_flag = snd_pilot_enabled', external_controls)
        self.assertIn(guard, pilot)
        dispatch_check = on_actions.split('snd_update_industry_tracking = yes', 1)[1]
        self.assertIn(guard, dispatch_check.split('snd_dispatch_pilot = yes', 1)[0])

    def test_auto_construction_uses_regular_queue_and_observes_cooldown(self):
        effect = (MOD / 'common/scripted_effects/snd_effects.txt').read_text()
        auto_effect = effect.split('snd_dispatch_auto_construction = {', 1)[1]
        orders = re.findall(
            r'add_building_construction\s*=\s*\{\s*type = (\w+)\s+level = 1\s+instant_build = no\s*\}',
            auto_effect,
        )
        self.assertCountEqual(orders, ['arms_factory', 'industrial_complex', 'infrastructure'])
        self.assertIn('flag = snd_auto_construction_cooldown days = 180', auto_effect)
        self.assertIn('any_owned_state = { snd_auto_factory_candidate = yes }', auto_effect)
        self.assertIn('random_owned_controlled_state = {', auto_effect)
        self.assertIn('set_variable = { snd_auto_project_state = PREV }', auto_effect)

        triggers = (MOD / 'common/scripted_triggers/snd_triggers.txt').read_text()
        factory_candidate = triggers.split('snd_auto_factory_candidate = {', 1)[1]
        for guard in ('is_owned_by = ROOT', 'is_controlled_by = ROOT', 'is_core_of = ROOT'):
            self.assertIn(guard, factory_candidate)

        on_actions = (MOD / 'common/on_actions/snd_on_actions.txt').read_text()
        auto_check = on_actions.split('snd_dispatch_auto_construction = yes', 1)[0].rsplit('            if = {', 1)[1]
        for flag in ('snd_external_construction', 'snd_auto_construction_cooldown', 'snd_pilot_enabled'):
            self.assertIn(f'NOT = {{ has_country_flag = {flag} }}', auto_check)

    def test_national_alerts_use_a_single_report_and_track_risk_changes(self):
        effects = (MOD / 'common/scripted_effects/snd_effects.txt').read_text()
        decisions = (MOD / 'common/decisions/snd_decisions.txt').read_text()
        on_actions = (MOD / 'common/on_actions/snd_on_actions.txt').read_text()

        self.assertEqual(effects.count('country_event = { id = snd.3 }'), 1)
        self.assertIn('snd_show_national_report = yes', decisions)
        review = effects.split('snd_review_national_risk = {', 1)[1]
        self.assertIn('NOT = { check_variable = { snd_last_reported_risk = snd_current_risk } }', review)
        self.assertIn('set_variable = { snd_last_reported_risk = snd_current_risk }', review)
        self.assertIn('check_variable = { snd_current_risk > 0 }', review)
        self.assertIn('snd_show_national_report = yes', review)
        self.assertRegex(on_actions, r'has_country_flag = snd_risk_alerts_enabled\s*}\s*snd_review_national_risk = yes')

    def test_pilot_uses_regular_queue(self):
        effect = (MOD / 'common/scripted_effects/snd_effects.txt').read_text()
        self.assertIn('instant_build = no', effect)
        self.assertNotIn('instant_build = yes', effect)
        self.assertIn('set_country_flag = snd_pilot_dispatched', effect)
        self.assertIn('clr_country_flag = snd_pilot_enabled', effect)


if __name__ == '__main__':
    unittest.main()
