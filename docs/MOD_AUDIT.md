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
| Pesquisa | Automated Research System avança slots virtuais no evento `zzars.1`, compara progresso ao custo e chama `zzars_grant`, que concede a tecnologia com `set_technology`. Esse caminho tem espera simulada, mas usa a rotina de concessão em vez da fila nativa. Excluído da integração de pesquisa legítima enquanto não se demonstrar um modo com slots normais. | Pendente |
| Indústria e equipamentos | Design Bureau tem decisões para humanos, módulos de indústria militar e vários efeitos e modificadores próprios. Verificar custos e impactos no RT56. | Pendente |
| Aliados | General Staff oferece decisões para humanos e efeitos `add_ai_strategy`. Isso comprova configuração da IA por script, e a execução pelos aliados precisa de medição. | Pendente |
| Administração | Council of Ministers tem decisões para humanos, GUI e efeitos próprios de construção e pesquisa. A versão é anterior ao alvo e há disputa de localização com General Staff. | Pendente |
| Ícones | Modifier Icons adiciona ícones e entradas de localização. O cruzamento com RT56 encontrou apenas a miniatura em comum. | Pendente |

O levantamento é reproduzível com `python3 scripts/audit_mods.py PERFIL`. As contagens comparam bytes e caminhos sem distinguir maiúsculas e minúsculas. Consulte [compatibilidade](MOD_COMPATIBILITY.md) para a triagem inicial por tipo de colisão.

## Auditoria dos símbolos do Director — 15/11/2026

A execução de `scripts/audit_symbols.py PERFIL` examinou **346 definições**
do Director contra os **11 mods locais**, incluindo os seis ativos. Não
houve duplicatas internas nem colisões com esses mods nos domínios cobertos.
Nenhum descriptor foi ignorado. O resumo reproduzível está em
[SYMBOL_AUDIT.json](SYMBOL_AUDIT.json), sem conteúdo proprietário.

A ferramenta distingue definições de referências e ignora comentários e
textos entre aspas. Compara eventos, decisões, categorias, efeitos e triggers
scriptados, scripted GUIs e nomes de localização scriptada. As chaves de
localização são comparadas por idioma; traduções não contam como duplicatas.
O bloco `scripted_gui` é um contêiner, não um ID de interface.

O escopo é o cruzamento **Director × cada mod**, não todos os pares entre
terceiros. Não cobre ideias, focos, sprites, nomes de janelas, variáveis,
flags, namespaces compartilhados sem IDs repetidos ou overrides vanilla.
Os arquivos são lidos como texto, sem executar preprocessamento da engine;
subpastas de scripts fora dos diretórios reconhecidos não são indexadas.
Mods exclusivamente gráficos podem ter zero definições cobertas. Ausência
de colisão de ID não comprova coexistência das automações em campanha.
A versão local foi reconfirmada em `launcher-settings.json`:
Operation Postern v1.19.3.0.c01a (5632).

Após a revisão dos estados informativos de construção, o resumo JSON foi
atualizado para **354 definições** (oito novas entradas de localização),
ainda contra 11 mods e sem colisões, duplicatas internas ou descriptors
ignorados. O escopo da auditoria permanece o descrito acima.
