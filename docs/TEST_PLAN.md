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
