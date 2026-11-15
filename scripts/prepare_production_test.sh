#!/usr/bin/env bash
set -euo pipefail

country=${1:-ITA}
case "$country" in
    ITA) scenario=production ;;
    BRA) scenario=construction ;;
    *) printf 'País de teste inválido: %s\n' "$country" >&2; exit 1 ;;
esac

repo=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)
mkdir -p -- "$repo/runtime"
trial=$(mktemp -d -- "$repo/runtime/$scenario-test.XXXXXXXX")
printf '%s\n' "$country" > "$trial/test-country"
cp -- "$repo/docs/TEST_PLAN.md" "$trial/TEST_PLAN.md"
git -C "$repo" rev-parse HEAD > "$trial/source-commit.txt"
profile="$trial/profile"
mkdir -p -- "$profile/mod"
cp -- "$repo/Smart_Nation_Director.mod" "$profile/mod/"
cp -R -- "$repo/Smart_Nation_Director" "$profile/mod/"
python3 - "$profile/dlc_load.json" <<'PY_CONFIG'
import json
from pathlib import Path
import sys
Path(sys.argv[1]).write_text(json.dumps({
    'enabled_mods': ['mod/Smart_Nation_Director.mod'],
    'disabled_dlcs': [],
}) + '\n')
PY_CONFIG
test -s "$profile/dlc_load.json"

install -m 700 -- "$repo/scripts/snd_open_production_test.sh" "$trial/open-test.sh"
test -s "$trial/open-test.sh"
bash -n "$trial/open-test.sh"
printf '%s\n' "$trial/open-test.sh"
