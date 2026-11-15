# Contexto para continuidade

O projeto busca máxima autonomia legítima no país humano do HOI4 1.19.3.0. O perfil pessoal usa RT56, Iron Secretary, Automated Research System, Design Bureau, General Staff e Modifier Icons. Council of Ministers está instalado e desabilitado devido à versão e à colisão com localização do General Staff.

A implementação atual é um piloto independente de dependências. Seus arquivos, flags e eventos usam `snd`. As decisões ficam no menu vanilla. Não há controle de console pelo mod. Preserve o perfil pessoal e execute [o roteiro](TEST_PLAN.md) em campanhas descartáveis.

Leia [estado](STATUS.md), [evidências de execução](RUNTIME_TESTS.md) e [lacunas](GAP_ANALYSIS.md) antes de ampliar o escopo. Confirme a fila de construção e `human_ai` primeiro. Verifique a rotina de concessão do Automated Research antes de qualquer integração. Rodar `python3 -m unittest discover -s tests -v` verifica o pacote estático.
