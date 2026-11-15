# Prova de conceito de human_ai

O executável 1.19.3 contém o comando e uma descrição de alternância da IA para países humanos. Em uma campanha descartável do Brasil, o comando respondeu `Human AI is now ON` em 2 de janeiro de 1936. O teste confirmou a ativação no Brasil humano, com o piloto instalado e autorizado antes de seu primeiro ciclo mensal. Ainda falta a comparação em vanilla e com cada mod externo. O piloto do Director não chama o console. Não há interface de script confirmada para acionar `human_ai` ou escolher quais tarefas ele executa.

Compare quatro execuções de Brasil em 1936 a partir de um save descartável copiado. Use uma execução humana sem automação, uma com `human_ai`, uma com o comando e um mod de automação e outra acrescentando mods individualmente. Teste também alternância desligada e save/load. Evite clicar em filas, decisões ou ordens durante a observação.

| Ação | Baseline | human_ai | human_ai com mods |
|---|---|---|---|
| Focos | Pendente | Aftermath of the Coffee Crisis em curso em março | Pendente |
| Construção | Pendente | Nova obra em São Paulo e mudança na prioridade | Pendente |
| Pesquisa | Pendente | Basic Machine Tools e Construction I ocupavam slots nativos, com progresso e dias restantes | Pendente |
| Produção | Pendente | Pendente | Pendente |
| Comércio | Pendente | Observado na interface após ativação | Pendente |
| Recrutamento e modelos | Pendente | Pendente | Pendente |
| Comandantes e organização em teatros | Pendente | Observados após ativação | Pendente |
| Planos de batalha | Pendente | Pendente | Pendente |
| Ações terrestres, aéreas e navais | Pendente | Pendente | Pendente |
| Diplomacia, política e respostas a eventos | Pendente | Pendente | Pendente |

Em cada caso, salve evidência de ações concretas, como novo item na fila, troca de comandante ou ação diplomática, e registre quem realizou a ação. Se a IA iniciar uma obra, isso confirma somente a obra observada. Consulte [testes](TEST_PLAN.md).


## Observação de 30 dias

Veja [evidências em jogo](RUNTIME_TESTS.md). Entre 2 de fevereiro e 4 de março,
a sessão com IA ativa exibiu uma nova obra em São Paulo, recursos de comércio
na interface e organização militar com comandantes e teatros. O jogador
manteve o Brasil selecionado e não emitiu ordens. O piloto do Director já
estava inativo após sua única ordem. Falta comparar com um controle no mesmo
checkpoint para separar todos os efeitos.
