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
        for path in sorted(MOD.rglob('*.txt')) + sorted(MOD.rglob('*.gui')):
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
        gui_text = '\n'.join(path.read_text() for path in (MOD / 'interface').glob('snd_*.gui'))
        required = {'snd_director_category'}
        required.update(re.findall(r'\b(?:text|buttonText)\s*=\s*"(snd_\w+)"', gui_text))
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
        guard = 'NOT = { snd_construction_managed_externally = yes }'

        external_controls = decisions.split('    snd_set_external_construction = {', 1)[1].split(
            '    snd_enable_auto_construction = {', 1
        )[0]
        pilot = decisions.split('    snd_enable_pilot = {', 1)[1]
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
        self.assertIn('flag = snd_auto_construction_cooldown value = 1 days = 180', auto_effect)
        self.assertIn('any_owned_state = { snd_auto_factory_candidate = yes }', auto_effect)
        self.assertIn('random_owned_controlled_state = {', auto_effect)
        self.assertIn('set_variable = { snd_auto_project_state = PREV }', auto_effect)

        triggers = (MOD / 'common/scripted_triggers/snd_triggers.txt').read_text()
        factory_candidate = triggers.split('snd_auto_factory_candidate = {', 1)[1]
        for guard in ('is_owned_by = ROOT', 'is_controlled_by = ROOT', 'is_core_of = ROOT'):
            self.assertIn(guard, factory_candidate)

        on_actions = (MOD / 'common/on_actions/snd_on_actions.txt').read_text()
        auto_check = on_actions.split('snd_dispatch_auto_construction = yes', 1)[0].rsplit('            if = {', 1)[1]
        self.assertIn('snd_can_plan_auto_construction = yes', auto_check)
        planning_guard = triggers.split('snd_can_plan_auto_construction = {', 1)[1].split('\n}', 1)[0]
        for flag in ('snd_auto_construction_cooldown', 'snd_pilot_enabled', 'snd_auto_project_pending'):
            self.assertIn(f'NOT = {{ has_country_flag = {flag} }}', planning_guard)

    def test_iron_secretary_gate_checks_construction_modules(self):
        triggers = (MOD / 'common/scripted_triggers/snd_triggers.txt').read_text()
        actions = (MOD / 'common/on_actions/snd_on_actions.txt').read_text()
        iron, external = triggers.split('snd_iron_secretary_runs_construction = {', 1)[1].split(
            'snd_construction_managed_externally = {', 1
        )
        groups = re.findall(r'OR = \{(.*?)\n    \}', iron, re.S)
        self.assertEqual(len(groups), 2)
        self.assertCountEqual(re.findall(r'has_country_flag = (\w+)', groups[0]),
                              ['ais_logistics_enabled', 'ais_air_enabled', 'ais_industry_enabled'])
        self.assertIn('has_country_flag = ais_enabled', groups[1])
        self.assertIn('any_owned_state = { has_state_flag = ais_railway_project_active }', groups[1])
        self.assertIn('snd_iron_secretary_runs_construction = yes', external)
        self.assertIn('has_country_flag = snd_external_construction', external)
        self.assertIn('NOT = { snd_construction_managed_externally = yes }', actions)
        planning_guard = triggers.split('snd_can_plan_auto_construction = {', 1)[1].split('\n}', 1)[0]
        self.assertIn('NOT = { snd_construction_managed_externally = yes }', planning_guard)
        self.assertIn('snd_can_plan_auto_construction = yes', actions)

    def test_iron_secretary_trade_status_checks_weekly_module_flags(self):
        triggers = (MOD / 'common/scripted_triggers/snd_triggers.txt').read_text()
        getter = (MOD / 'common/scripted_localisation/snd_trade_localisation.txt').read_text()
        trade = triggers.split('snd_iron_secretary_runs_trade = {', 1)[1].split('\n}', 1)[0]
        self.assertCountEqual(re.findall(r'has_country_flag = (\w+)', trade),
                              ['ais_enabled', 'ais_trade_enabled'])
        self.assertIn('trigger = { snd_iron_secretary_runs_trade = yes }', getter)
        self.assertIn('trigger = { NOT = { snd_iron_secretary_runs_trade = yes } }', getter)

    def test_supervised_construction_revalidates_the_selected_project(self):
        effects = (MOD / 'common/scripted_effects/snd_effects.txt').read_text()
        actions = (MOD / 'common/on_actions/snd_on_actions.txt').read_text()
        triggers = (MOD / 'common/scripted_triggers/snd_triggers.txt').read_text()
        decisions = (MOD / 'common/decisions/snd_decisions.txt').read_text()
        offer = effects.split('snd_offer_construction_project = {', 1)[1].split('\n}', 1)[0]
        self.assertIn('set_country_flag = snd_construction_proposal_pending', offer.split('else =', 1)[0])
        self.assertNotIn('snd_queue_planned_project = yes', offer.split('else =', 1)[0])
        self.assertIn('snd_queue_planned_project = yes', offer.split('else =', 1)[1])
        self.assertIn('NOT = { has_country_flag = snd_construction_proposal_pending }', actions)
        approve = decisions.split('snd_approve_construction_proposal = {', 1)[1].split('\n    }', 1)[0]
        self.assertIn('available = { snd_construction_proposal_is_eligible = yes }', approve)
        self.assertIn('limit = { snd_construction_proposal_is_eligible = yes }', approve)
        self.assertIn('snd_queue_planned_project = yes', approve)
        eligible = triggers.split('snd_construction_proposal_is_eligible = {', 1)[1]
        self.assertIn('snd_can_plan_auto_construction = yes', eligible)
        self.assertIn('var:snd_proposal_state = {', eligible)
        decline = decisions.split('snd_decline_construction_proposal = {', 1)[1].split('\n    }', 1)[0]
        self.assertIn('flag = snd_construction_proposal_deferred value = 1 days = 90', decline)
        self.assertNotIn('snd_queue_planned_project = yes', decline)

    def test_advisory_construction_only_refreshes_a_recommendation(self):
        effects = (MOD / 'common/scripted_effects/snd_effects.txt').read_text()
        actions = (MOD / 'common/on_actions/snd_on_actions.txt').read_text()
        decisions = (MOD / 'common/decisions/snd_decisions.txt').read_text()
        triggers = (MOD / 'common/scripted_triggers/snd_triggers.txt').read_text()
        offer = effects.split('snd_offer_construction_project = {', 1)[1].split('\n}', 1)[0]
        recommendation, dispatch = offer.split('else =', 1)
        self.assertIn('has_country_flag = snd_construction_advisory', recommendation)
        self.assertIn('set_country_flag = snd_construction_proposal_pending', recommendation)
        self.assertNotIn('snd_queue_planned_project = yes', recommendation)
        self.assertIn('snd_queue_planned_project = yes', dispatch)
        self.assertRegex(actions, r'OR = \{\s*has_country_flag = snd_construction_advisory\s*'
                                  r'NOT = \{ has_country_flag = snd_construction_proposal_pending }')
        advisory = decisions.split('snd_enable_construction_advisory = {', 1)[1].split('\n    }', 1)[0]
        self.assertIn('clr_country_flag = snd_construction_supervised', advisory)
        self.assertIn('clr_country_flag = snd_construction_proposal_pending', advisory)
        eligibility = triggers.split('snd_construction_proposal_is_eligible = {', 1)[1]
        self.assertIn('NOT = { has_country_flag = snd_construction_advisory }', eligibility)

    def test_dashboard_reads_live_values_and_opens_report(self):
        decisions = (MOD / 'common/decisions/snd_decisions.txt').read_text()
        gui = (MOD / 'common/scripted_guis/snd_dashboard_gui.txt').read_text()
        interface = (MOD / 'interface/snd_dashboard.gui').read_text()
        effects = (MOD / 'common/scripted_effects/snd_effects.txt').read_text()

        category = (MOD / 'common/decisions/categories/snd_categories.txt').read_text()
        self.assertIn('scripted_gui = snd_dashboard', category)
        self.assertNotIn('scripted_gui', decisions)
        buttons = re.findall(r'buttonType = \{(.*?)\n\t\t}', interface, re.S)
        self.assertEqual(len(buttons), 1)
        for button in buttons:
            self.assertNotIn('size =', button)
            self.assertIn('quadTextureSprite =', button)
        self.assertIn('buttonText = "snd_dash_report"', interface)
        self.assertIn('context_type = decision_category', gui)
        self.assertIn('window_name = "snd_dashboard"', gui)
        self.assertIn('name = "snd_dashboard"', interface)
        self.assertIn('snd_dash_report_click = {', gui)
        self.assertIn('snd_show_national_report = yes', gui.split('snd_dash_report_click = {', 1)[1])
        for widget in ('snd_dash_report', 'snd_dash_title',
                       'snd_dash_factories', 'snd_dash_dockyards', 'snd_dash_manpower'):
            self.assertIn(f'name = "{widget}"', interface)

        capture = effects.split('snd_capture_report_values = {', 1)[1].split('\n}', 1)[0]
        for variable in ('snd_report_civilian_factories', 'snd_report_military_factories',
                         'snd_report_dockyards', 'snd_report_manpower_k'):
            self.assertIn(f'{variable} =', capture)
        report = effects.split('snd_show_national_report = {', 1)[1]
        self.assertIn('snd_capture_report_values = yes', report)
        self.assertIn('country_event = { id = snd.3 }', report)
        for language in ('english', 'braz_por'):
            loc = (MOD / 'localisation' / language / f'snd_l_{language}.yml').read_text(encoding='utf-8-sig')
            dashboard = '\n'.join(line for line in loc.splitlines() if line.startswith(' snd_dash_'))
            for name in ('num_of_civilian_factories', 'num_of_military_factories',
                         'num_of_naval_factories', 'manpower_k'):
                self.assertIn(f'[?ROOT.{name}|', dashboard)
            self.assertNotIn('[?snd_report_', dashboard)
        self.assertNotIn('snd_refresh_dashboard', effects)
        self.assertNotIn('dirty =', gui)

    def test_auto_project_requires_level_growth_at_the_recorded_state(self):
        effects = (MOD / 'common/scripted_effects/snd_effects.txt').read_text()
        actions = (MOD / 'common/on_actions/snd_on_actions.txt').read_text()
        triggers = (MOD / 'common/scripted_triggers/snd_triggers.txt').read_text()
        decisions = (MOD / 'common/decisions/snd_decisions.txt').read_text()
        for building in ('industrial_complex', 'arms_factory', 'infrastructure'):
            self.assertIn(f'snd_auto_project_baseline = PREV.building_level@{building}', effects)
            self.assertIn(f'building_level@{building} > ROOT.snd_auto_project_baseline', triggers)
        self.assertIn('var:snd_auto_project_state = {', triggers)
        self.assertRegex(actions, r'snd_auto_project_level_increased = yes\s*}\s*clr_country_flag = snd_auto_project_pending')
        release = decisions.split('snd_release_pending_project = {', 1)[1].split('snd_enable_pilot = {', 1)[0]
        self.assertIn('clr_country_flag = snd_auto_project_pending', release)
        self.assertNotIn('snd_auto_construction_cooldown', release)

    def test_government_controls_preserve_construction_safeguards_and_history(self):
        decisions = (MOD / 'common/decisions/snd_decisions.txt').read_text()
        triggers = (MOD / 'common/scripted_triggers/snd_triggers.txt').read_text()
        effects = (MOD / 'common/scripted_effects/snd_effects.txt').read_text()

        safeguard = triggers.split('snd_can_start_auto_construction = {', 1)[1].split('}', 2)
        self.assertIn('NOT = { snd_construction_managed_externally = yes', safeguard[0])
        self.assertIn('NOT = { has_country_flag = snd_pilot_enabled', safeguard[1])

        start = effects.split('snd_start_government_routines = {', 1)[1]
        self.assertIn('limit = { snd_can_start_auto_construction = yes }', start)
        self.assertIn('limit = { NOT = { has_country_flag = snd_industry_tracking } }', start)
        self.assertIn('limit = { NOT = { has_country_flag = snd_risk_alerts_enabled } }', start)

        stop = decisions.split('snd_stop_automatic_government = {', 1)[1].split('snd_open_delegation_guide = {', 1)[0]
        self.assertIn('snd_stop_industry_tracking = yes', stop)
        for flag in ('snd_risk_alerts_enabled', 'snd_auto_construction', 'snd_pilot_enabled'):
            self.assertIn(f'clr_country_flag = {flag}', stop)
        self.assertNotIn('snd_auto_construction_cooldown', stop)
        self.assertNotIn('snd_external_construction', stop)

    def test_national_alerts_route_one_report_per_priority_change(self):
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
        self.assertEqual(effects.count('country_event = { id = snd.4 }'), 1)
        self.assertIn('snd_show_military_report = yes', decisions)
        self.assertLess(review.index('snd_has_surrender_risk = yes'), review.index('snd_has_stability_risk = yes'))
        self.assertRegex(review, r'check_variable = \{ snd_current_risk = 5 } }\s*snd_show_military_report = yes')
        self.assertRegex(on_actions, r'has_country_flag = snd_risk_alerts_enabled\s*}\s*snd_review_national_risk = yes')

    def test_external_production_preserves_pending_pilot_and_blocks_dispatch(self):
        decisions = (MOD / 'common/decisions/snd_decisions.txt').read_text()
        triggers = (MOD / 'common/scripted_triggers/snd_triggers.txt').read_text()
        guard = 'NOT = { has_country_flag = snd_external_production }'
        controls, pilot = decisions.split('    snd_set_external_production = {', 1)[1].split(
            '    snd_enable_rifle_production_pilot = {', 1
        )
        self.assertIn('set_country_flag = snd_external_production', controls)
        self.assertIn('clr_country_flag = snd_external_production', controls)
        self.assertNotIn('clr_country_flag = snd_rifle_production_enabled', controls)
        self.assertIn(f'available = {{ {guard} }}', pilot)
        self.assertIn(guard, triggers.split('snd_can_dispatch_rifle_order = {', 1)[1])

    def test_rifle_pilot_only_requests_one_regular_factory(self):
        effects = (MOD / 'common/scripted_effects/snd_effects.txt').read_text()
        actions = (MOD / 'common/on_actions/snd_on_actions.txt').read_text()
        triggers = (MOD / 'common/scripted_triggers/snd_triggers.txt').read_text()
        effect = effects.split('snd_dispatch_rifle_order = {', 1)[1]
        models = ('infantry_equipment_3', 'infantry_equipment_2', 'infantry_equipment_1', 'infantry_equipment_0')
        self.assertEqual(re.findall(r'type = (infantry_equipment_\d+)', effect), list(models))
        for tech, model in zip(('advanced_infantry_weapons', 'improved_infantry_weapons', 'infantry_weapons1'), models):
            self.assertRegex(effect, rf'has_tech = {tech} }}\s+add_equipment_production = {{\s+equipment = {{ type = {model} }}')
        self.assertEqual(effect.count('requested_factories = 1'), len(models))
        for bonus in ('efficiency', 'progress', 'add_equipment_to_stockpile'):
            self.assertNotIn(bonus, effect)
        self.assertIn('set_country_flag = snd_rifle_order_issued', effect)
        self.assertIn('NOT = { has_country_flag = snd_rifle_order_issued }', actions)
        self.assertIn('snd_has_infantry_equipment_risk = yes', triggers)
        self.assertIn('num_of_available_military_factories > 0', triggers)

    def test_research_review_distinguishes_virtual_and_native_research(self):
        triggers = (MOD / 'common/scripted_triggers/snd_triggers.txt').read_text()
        effects = (MOD / 'common/scripted_effects/snd_effects.txt').read_text()
        virtual = triggers.split('snd_automated_research_enabled = {', 1)[1].split('\n}', 1)[0]
        self.assertIn('has_variable = zzars_on', virtual)
        self.assertIn('check_variable = { zzars_on = 1 }', virtual)
        for technology in ('infantry_weapons1', 'basic_machine_tools'):
            self.assertIn(f'NOT = {{ has_tech = {technology} }}', triggers)
            self.assertIn(f'NOT = {{ is_researching_technology = {technology} }}', triggers)
        self.assertNotIn('set_technology =', effects)
        self.assertNotIn('set_research_slots =', effects)

    def test_military_report_displays_live_force_and_war_metrics(self):
        events = (MOD / 'events/snd_events.txt').read_text()
        report = events.split('id = snd.4', 1)[1]
        for condition in ('has_capitulated = yes', 'has_war = yes', 'has_war = no'):
            self.assertIn(condition, report)
        for locale in ('english', 'braz_por'):
            loc = (MOD / 'localisation' / locale / f'snd_l_{locale}.yml').read_text(encoding='utf-8-sig')
            descriptions = dict(line.strip().split(':0 ', 1) for line in loc.splitlines() if line.startswith(' snd.4.d_'))
            self.assertEqual(set(descriptions), {'snd.4.d_capitulated', 'snd.4.d_surrender_risk', 'snd.4.d_war', 'snd.4.d_peace'})
            for description in descriptions.values():
                for variable in ('num_divisions', 'num_ships', 'has_war_support'):
                    self.assertIn(f'[?ROOT.{variable}|', description)
            for key in ('snd.4.d_war', 'snd.4.d_surrender_risk'):
                self.assertIn('[?ROOT.surrender_progress|%0]', descriptions[key])
            self.assertNotIn('surrender_progress', descriptions['snd.4.d_peace'])

    def test_diplomatic_report_distinguishes_faction_role_and_subject_status(self):
        loc = (MOD / 'common/scripted_localisation/snd_diplomacy_localisation.txt').read_text()
        decisions = (MOD / 'common/decisions/snd_decisions.txt').read_text()
        self.assertIn('trigger = { is_faction_leader = yes }', loc)
        self.assertIn('is_faction_leader = no', loc)
        self.assertIn('is_in_faction = yes', loc)
        self.assertIn('trigger = { is_in_faction = no }', loc)
        for value in ('yes', 'no'):
            self.assertIn(f'trigger = {{ is_subject = {value} }}', loc)
        report = decisions.split('snd_open_diplomatic_report = {', 1)[1].split('\n    }', 1)[0]
        self.assertIn('complete_effect = {\n            country_event = { id = snd.5 }\n        }', report)

    def test_pilot_uses_regular_queue(self):
        effect = (MOD / 'common/scripted_effects/snd_effects.txt').read_text()
        self.assertIn('instant_build = no', effect)
        self.assertNotIn('instant_build = yes', effect)
        self.assertIn('set_country_flag = snd_pilot_dispatched', effect)
        self.assertIn('clr_country_flag = snd_pilot_enabled', effect)


if __name__ == '__main__':
    unittest.main()
