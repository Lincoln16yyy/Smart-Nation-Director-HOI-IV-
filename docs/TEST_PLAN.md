# Plano de teste reproduzível

## Piloto isolado

1. Em um perfil de teste, inicie Brasil em 1936, fora de Ironman e com o Director como único mod. A capital brasileira na instalação vanilla usa o estado 500, com infraestrutura inicial 3.
2. Salve em um slot descartável. Anote a infraestrutura, a fila e as fábricas civis já alocadas.
3. Autorize o piloto; salve e recarregue antes da virada do mês. Confirme que a opção de cancelar continua visível.
4. Passe a virada do mês sem `human_ai`. Verifique se há exatamente um evento, um novo item de infraestrutura no estado da capital e nível construído inalterado até a conclusão normal. Registre alocação e progresso.
5. Salve e recarregue após o evento. Passe mais um mês. Confirme que a ordem não se repete.
6. Refaça a partir da cópia inicial, autorize e cancele antes da virada. A fila e os eventos devem permanecer sem ações do Director.
7. Repita com capital inelegível e com mods adicionados individualmente.

## IA nativa e campanhas

Siga as quatro variantes de [human_ai](HUMAN_AI_RESEARCH.md) com um save novo por configuração. Colete filas e ações efetivamente executadas em 30 dias, 180 dias, 1 ano, 3 anos, 5 anos e, se viável, 10 anos. Use Brasil, Alemanha, França ou Reino Unido, União Soviética, Japão e um país pequeno. No teste de guerra, registre ações terrestres, aéreas e navais separadamente. Conte intervenções manuais por categoria e compare desempenho entre vanilla, RT56, automações e Director.

## Piloto de produção da Itália

Gere um perfil descartável com `bash scripts/prepare_production_test.sh`.
Abra o lançador impresso quando quiser iniciar o teste. Ele usa um prefixo
Wine separado com apenas o Director e abre a Itália de 1936. Se necessário,
passe o caminho de `hoi4.exe` como argumento do lançador.

1. Pause a campanha e abra **Production**. Salve com a Itália em guerra,
   reserva de infantaria abaixo de 500 e capacidade militar disponível.
   O histórico vanilla começa em guerra com a Etiópia e com uma linha de
   Carcano M38. **Logistics** permite conferir a situação sem usar o console.
2. Na variante com linha existente, preserve a fila. Na outra variante,
   parta do mesmo save e retire a linha correspondente antes de autorizar.
3. Autorize uma nova linha no menu do Director, avance até a próxima
   virada e compare o modelo, a linha e a quantidade de fábricas alocadas.
   Registre também o status do relatório. O teste com linha existente já
   está registrado em [RUNTIME_TESTS.md](RUNTIME_TESTS.md).


## Mensagens de estado da construção

Prepare a campanha do Brasil com
`bash scripts/prepare_construction_test.sh`. O comando imprime o caminho de
`open-test.sh`; execute-o com `bash CAMINHO/open-test.sh`. O lançador abre
Brasil em 1936 com apenas o Director, em prefixo Wine separado. O perfil
pessoal não deve ser usado neste roteiro. Cada preparação cria uma pasta
nova em `runtime/construction-test.*`, com cópia do mod, país em
`test-country`, commit-base em `source-commit.txt` e cópia deste plano.
O commit identifica a base Git; alterações locais ainda não commitadas
podem estar presentes na cópia. O cenário da Itália continua disponível
pelo preparador de produção, sem argumentos.

Na primeira abertura, pause e abra **Decisões → Smart Nation Director**.
Confira primeiro se os indicadores do painel aparecem antes de abrir o
relatório. Para o primeiro ciclo de supervisão, registre fila e fábricas
civis antes da autorização, após a proposta e após a aprovação. Uma proposta
não deve criar obra; a aprovação deve enfileirar uma única obra com progresso
normal. Não ative o piloto de infraestrutura neste ciclo.

Em campanha descartável com apenas o Director, consulte o relatório nacional
entre as etapas; deixe `human_ai` desligado.

1. Ative o modo consultivo e as rotinas. Marque gestão externa de construção:
   o status deve indicar suspensão. Remova a marca e confirme o modo consultivo.
2. Troque para supervisão e avance uma virada elegível. Com proposta pendente,
   o relatório deve pedir sua decisão e a fila deve continuar sem nova ordem.
3. Recuse a proposta. Confira o aviso de adiamento de 90 dias. Trocar para modo
   consultivo durante esse período deve preservar o aviso de adiamento.
4. Depois do prazo, volte à supervisão, espere uma proposta e aprove. Confira
   a ordem na fila e o aviso do intervalo de 180 dias. Quando só restar a flag
   de obra pendente, confira o aviso para verificar a fila ou liberar a espera.
5. Desative as rotinas: o status deve indicar desativação, preservando o registro
   da última ordem e o intervalo. Repita os estados principais após salvar e
   recarregar; registre idiomas testados e erros de localização em RUNTIME_TESTS.


## Reteste das flags temporárias corrigidas

Use um perfil novo gerado após a correção de `value = 1`. Na variante de
aprovação, o relatório deve mostrar intervalo mínimo de 180 dias logo após
a ordem e após salvar/recarregar. Na variante de recusa, deve mostrar
adiamento de 90 dias, inclusive após salvar/recarregar e ao trocar para modo
consultivo. Confira a duração efetiva cruzando os prazos, sem confundir
intervalo expirado com liberação da espera de obra. Saves da versão anterior
podem conter temporizadores de valor zero e não validam essa correção.

## Revalidação de vaga na aprovação supervisionada

Este é o próximo teste isolado; gestão externa manual e modo consultivo já
foram observados e não precisam ser repetidos. Use uma cópia descartável da
campanha, com apenas o Director e `human_ai` desligado. Preserve o save da
rodada anterior. Não avance o calendário durante a comparação.

1. Com supervisão ativa e proposta de fábrica pendente, registre o tipo e o
   estado propostos, a aprovação habilitada e a fila antes de qualquer ação.
2. Pela interface vanilla, enfileire manualmente fábricas no estado proposto
   até ocupar as vagas compartilhadas disponíveis. Registre essas ordens
   manuais separadamente; elas não são ações do Director. Se a interface não
   permitir esgotar as vagas, registre a limitação e não declare o cenário
   inelegível como testado.
3. Volte às decisões. A proposta deve permanecer, mas a aprovação deve ficar
   indisponível. Confira o tooltip e registre a fila: nenhuma ordem adicional
   do Director deve ter sido emitida.
4. Cancele uma das ordens manuais recém-criadas para liberar uma vaga. Confira
   se a mesma proposta volta a permitir aprovação. Não cancele obras anteriores
   nem aprove antes de registrar a comparação.
5. Aprove uma vez e confira que entrou exatamente uma ordem do tipo e estado
   registrados, com progresso normal e intervalo de 180 dias no relatório.

O roteiro verifica como `free_building_slots` considera vagas ocupadas por
obras enfileiradas nesta versão da engine. O resultado ainda é desconhecido;
se a fila manual não tornar o estado inelegível para o trigger, isso é uma
limitação do cenário e precisa ser investigado antes de alterar o código.
Perda de posse/controle, desmilitarização e mudança entre paz e guerra
continuam sendo variantes distintas, ainda sem execução demonstrada.
