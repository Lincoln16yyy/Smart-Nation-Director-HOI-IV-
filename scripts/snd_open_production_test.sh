#!/usr/bin/env bash
set -euo pipefail

trial=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
game=${1:-"$HOME/Downloads/Hearts of Iron IV/Hearts of Iron IV/hoi4.exe"}
if [[ ! -f "$game" ]]; then
    printf 'Executável não encontrado: %s\n' "$game" >&2
    exit 1
fi

printf '%s\n' 'Preparando o perfil Wine isolado da Itália…'
export WINEPREFIX="$trial/wine"
if [[ ! -f "$WINEPREFIX/user.reg" ]]; then
    wineboot -i
fi
windows_documents=$(wine reg query 'HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders' /v Personal | sed -n 's/^[[:space:]]*Personal[[:space:]]*REG_SZ[[:space:]]*//p' | tr -d '\r')
document_path=$(printf '%s' "$windows_documents" | tr '\\' '/')
if [[ ! "$document_path" =~ ^[Cc]:/[Uu]sers/([^/:]+)/[Dd]ocuments$ ]]; then
    printf 'Documents não aponta para o disco C isolado: %s\n' "$windows_documents" >&2
    exit 1
fi
wine_user=${BASH_REMATCH[1]}
if [[ "$wine_user" == '.' || "$wine_user" == '..' ]]; then
    printf 'Usuário inválido no prefixo Wine.\n' >&2
    exit 1
fi
documents="$WINEPREFIX/drive_c/users/$wine_user/Documents"
if [[ -L "$documents" ]]; then
    unlink -- "$documents"
fi
mkdir -p -- "$documents"
case "$(realpath -- "$documents")" in
    "$WINEPREFIX"/drive_c/users/*/Documents) ;;
    *) printf 'O caminho real de Documents não é isolado.\n' >&2; exit 1 ;;
esac

target="$documents/Paradox Interactive/Hearts of Iron IV"
if [[ ! -s "$trial/profile/dlc_load.json" ]]; then
    printf 'Configuração do mod ausente no perfil de teste. Gere o perfil novamente.\n' >&2
    exit 1
fi
if [[ ! -e "$target" ]]; then
    mkdir -p -- "$(dirname -- "$target")"
    cp -R -- "$trial/profile" "$target"
fi
if [[ ! -s "$target/dlc_load.json" ]]; then
    install -m 600 -- "$trial/profile/dlc_load.json" "$target/dlc_load.json"
fi
cd -- "$(dirname -- "$game")"
printf '%s\n' 'Abrindo o HOI4. A campanha pode demorar para carregar.'
exec wine "./$(basename -- "$game")" -gdpr-compliant -debug_mode -start_tag=ITA
