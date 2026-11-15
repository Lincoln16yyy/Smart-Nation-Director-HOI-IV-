# Evidências sobre a engine 1.19.3

| Mecanismo | Evidência | Resultado |
|---|---|---|
| IA nativa em país humano | Binário instalado contém `human_ai` e a descrição `Toggles AI for Human countries` | Presença no executável confirmada. Comportamento e persistência pendentes. |
| Debug | Metadados do launcher indicam `-gdpr-compliant -debug_mode`; binário contém `trigger_docs`, `effect_docs`, `eval_effect`, `eval_trigger`, `aiview`, `list_vars`, `list_flags`, `reloadinterface` e `imgui` | Presença textual. Argumentos, saídas e escopos ainda exigem execução. |
| On-actions | `common/on_actions/_documentation.md` e exemplo de `on_monthly` em `12_wuw_on_actions.txt` | Ciclo mensal e exemplo em escopo de país documentados localmente. |
| Construção | `common/decisions/HUN.txt` usa `add_building_construction` em estado; Iron Secretary usa a variante não instantânea; construção vanilla define `infrastructure` | Piloto combina os padrões. Aceitação na fila, custo e duração pendentes. |
| AI strategies, plans e pesos de foco | Diretórios vanilla e scripts do General Staff | Tratar como entradas da IA. A execução pela IA no país humano ainda precisa de teste. |
| Scripted GUI | Exemplos instalados nos mods de pesquisa, conselho, indústria e aliados | Interface e acionamento por cliques são candidatos ao painel; leitura e interação pendentes. |
| Eventos e decisões | Referência local em `common/decisions/_documentation.md` e exemplos de país humano nos mods | Usados pelo piloto. Renderização e execução pendentes. |

O wiki oficial retornou HTTP 401 durante a consulta. A primeira implementação utiliza os arquivos instalados como referência. [Documentação da Paradox](https://hoi4.paradoxwikis.com/Modding)
