"""Fixtures for definition/reference and language separation in the local audit."""
import json
from pathlib import Path
import tempfile
import unittest

from scripts.audit_symbols import audit, definitions


class SymbolAuditTests(unittest.TestCase):
    def write(self, root, name, source):
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(source, encoding='utf-8-sig')

    def test_definitions_exclude_references_comments_and_strings(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write(root, 'events/snd.txt', '''
                # country_event = { id = snd.fake }
                country_event = {
                    id = snd.1
                    desc = "text # { id = snd.fake }"
                    option = { country_event = { id = snd.2 } }
                }
            ''')
            self.write(root, 'common/decisions/snd.txt', '''
                snd_category = {
                    snd_decision = { complete_effect = { snd_effect = yes } }
                }
            ''')
            self.write(root, 'common/scripted_effects/snd.txt', 'snd_effect = { log = "}" }')
            self.write(root, 'common/scripted_guis/snd.txt', 'scripted_gui = { snd_dashboard = { context_type = decision_category } }')
            self.assertEqual(set(definitions(root)), {
                ('scripted_gui', 'snd_dashboard'),
                ('event', 'snd.1'), ('decision', 'snd_decision'), ('effect', 'snd_effect')})

    def test_language_domains_and_duplicate_keys(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write(root, 'localisation/english/a.yml', 'l_english:\n snd_key:0 "A"\n snd_key:0 "B"\n')
            self.write(root, 'localisation/braz_por/a.yml', 'l_braz_por:\n snd_key:0 "C"\n')
            symbols = definitions(root)
            self.assertEqual(len(symbols[('localisation/l_english', 'snd_key')]), 2)
            self.assertEqual(len(symbols[('localisation/l_braz_por', 'snd_key')]), 1)

    def test_audit_includes_inactive_mods_and_reports_missing_paths(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / 'target'
            self.write(target, 'common/scripted_triggers/snd.txt', 'snd_shared = { always = yes }')
            self.write(root, 'mod/other.mod', 'path="mod/other"')
            self.write(root, 'mod/missing.mod', 'archive="missing.zip"')
            self.write(root, 'mod/other/common/scripted_triggers/other.txt', 'snd_shared = { always = no }')
            (root / 'dlc_load.json').write_text(json.dumps({'enabled_mods': []}))
            report = audit(root, target)
            self.assertEqual(report['collisions'][0]['id'], 'snd_shared')
            self.assertFalse(report['collisions'][0]['active'])
            self.assertEqual(report['skipped'][0]['mod'], 'missing')


if __name__ == '__main__':
    unittest.main()
