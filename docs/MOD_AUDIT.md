# Auditoria local dos mods

A instalação Windows abriu por Hydra/Wine em uso normal. O executável instalado é `hoi4.exe` e seus metadados em `launcher-settings.json` informam **Operation Postern v1.19.3.0.c01a (5632)**. O diretório de instalação contém `common/`, `events/`, `interface/`, `history/` e demais arquivos vanilla. No prefixo Hydra 394360, o perfil fica em `drive_c/users/steamuser/Documents/Paradox Interactive/Hearts of Iron IV/`. Ali ficam `mod/`, `dlc_load.json`, `logs/` e `crashes/`. A pasta convencional `save games/` estava ausente na inspeção do perfil. Nenhum save existente foi usado.

| Mod | Versão do mod | Suporte declarado | Perfil Hydra |
|---|---|---|---|
| The Road to 56 | 1.19.* | 1.19.* | Ativo |
| Iron Secretary | 2.1.0 | 1.19.* | Ativo |
| Automated Research System | 1 | 1.19.2.0 | Ativo |
| Design Bureau | 1.19.3 | 1.19.4.2 | Ativo |
| Handy Game Tool — General Staff | 1.18.1 | 1.18.2.0 | Ativo |
| Modifier Icons | 0.1 | 1.19.* | Ativo |
| Council of Ministers | 1.14.10 | 1.16.6 | Instalado, desativado |
| Industrial Planner ACA | 1.31.3-single-state-marker | 1.19.* | Instalado, desativado |
| More Politics | 1.5 | 1.19.* | Instalado, desativado |
| Coloured Buttons | 1.9 | 1.9.* | Instalado, desativado |
| Minimalistic GUI | v3 | 1.16.* | Instalado, desativado |

A leitura dos descriptors internos e externos encontrou a diferença de nome no Coloured Buttons, cujo descriptor interno omite esse campo. The Road to 56 substitui `history/states` e `map/strategicregions`. More Politics substitui `common/ai_navy/{fleet,goals,taskforce}`. Nenhum dos descriptors analisados declarou um bloco de dependências. Requisitos de DLC ou referências internas precisam de verificação própria.

| Área | Evidência estática local | Teste em partida |
|---|---|---|
| Construção e logística | Iron Secretary expõe categoria com `is_ai = no` e usa `add_building_construction` com `instant_build = no` em projetos e suprimentos. Inspecionar habilitação e custos por módulo antes de integrar. | Pendente |
| Pesquisa | Automated Research System tem GUI, on-actions e `zzars_grant` em `zz_auto_research_grant.txt`, com chamadas a `set_technology`. O modo seguro precisa ser demonstrado antes da integração. | Pendente |
| Indústria e equipamentos | Design Bureau tem decisões para humanos, módulos de indústria militar e vários efeitos e modificadores próprios. Verificar custos e impactos no RT56. | Pendente |
| Aliados | General Staff oferece decisões para humanos e efeitos `add_ai_strategy`. Isso comprova configuração da IA por script, e a execução pelos aliados precisa de medição. | Pendente |
| Administração | Council of Ministers tem decisões para humanos, GUI e efeitos próprios de construção e pesquisa. A versão é anterior ao alvo e há disputa de localização com General Staff. | Pendente |
| Ícones | Modifier Icons adiciona ícones e entradas de localização. O cruzamento com RT56 encontrou apenas a miniatura em comum. | Pendente |

O levantamento é reproduzível com `python3 scripts/audit_mods.py PERFIL`. As contagens comparam bytes e caminhos sem distinguir maiúsculas e minúsculas. Consulte [compatibilidade](MOD_COMPATIBILITY.md) para a triagem inicial por tipo de colisão.
