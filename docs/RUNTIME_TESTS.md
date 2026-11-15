# Testes na instalação real

- A tentativa em sandbox falhou na abertura do socket do wineserver.
- A primeira tentativa vanilla com Wine fora do sandbox gerou logs em Documents padrão do usuário, pois o prefixo novo trazia um link para essa pasta. A execução não criou um save. Antes de carregar o piloto, substituí apenas o link do prefixo temporário por um diretório interno.
- Uma execução autorizada via Wine em prefixo temporário inicializou o HOI4 com debug e apenas o piloto habilitado. `setup.log` registrou uma categoria, duas decisões e um evento do piloto. `game.log` registrou a execução do histórico até 1º de janeiro de 1936. Na coleta inicial, `error.log` estava vazio.
- Em uma tela virtual, `-start_tag=BRA` abriu a campanha de Brasil em 1º de janeiro de 1936. No menu inglês, a categoria Smart Nation Director e a decisão de autorização estavam visíveis, com a decisão habilitada. Em uma segunda execução, o clique de autorização revelou a opção de revogar o piloto. `error.log` permaneceu vazio nas coletas iniciais. `game.log` também contém uma mensagem sobre Conflict Risk, sem atribuição ao piloto.
- Em 2 de janeiro de 1936, com o país humano pausado e o piloto apenas autorizado, o console respondeu `Human AI is now ON` a `human_ai`. A ativação foi confirmada; a fila do piloto, a persistência e os efeitos de cada tarefa exigem verificação adicional.
- O limite de cinco minutos da sessão isolada encerrou o jogo antes da próxima virada mensal. A campanha chegou a 2 de janeiro durante a observação. Sem evidência de trabalho efetivamente realizado pela IA, as tarefas da matriz permanecem pendentes.

## Virada mensal e fila de construção

Em nova campanha descartável do Brasil, com apenas o Director e sem ativar
`human_ai`, autorizei a ação pela decisão. Executei `fast_forward 32` no console
de debug sem passar para observador. O console confirmou o avanço de 32 dias.
Em 2 de fevereiro de 1936, a bandeira do Brasil continuava no HUD, o evento de
despacho estava visível e a fila tinha uma única obra de infraestrutura no Rio
de Janeiro. A linha mostrava **10/15 fábricas civis** alocadas, depois das sete
destinadas a bens de consumo. Nenhuma ordem de obra foi emitida manualmente.

Esse teste confirma que a autorização e o ciclo mensal acionaram uma ordem real
pela fila regular, com consumo de capacidade civil. A persistência foi testada separadamente;
a conclusão da obra ainda não foi medida.

## Primeiras ações de human_ai

Na mesma campanha descartável, em 2 de fevereiro, ativei `human_ai` após o
encerramento da ação única do piloto. O console confirmou `Human AI is now ON`.
Avancei 30 dias sem emitir ordens manuais. Em 4 de março, o painel de
construção mostrava uma nova obra em São Paulo com 7/15 fábricas e a obra
anterior do Rio continuava na fila com 0/15. O painel passou a mostrar bens
comercializados e contratos de mercado. Surgiram três retratos de comandantes
e grupos nos painéis Brazilian Theater 1 e South America. No painel político,
o foco Aftermath of the Coffee Crisis estava em andamento. Os dois slots
nativos exibiam Basic Machine Tools (98 dias restantes) e Construction I
(150 dias restantes), ambos com progresso. O Automated Research System
estava fora da configuração do teste.

Essa é uma observação sequencial com o piloto já despachado. Uma execução de
controle com o mesmo checkpoint de fevereiro é necessária para atribuir toda
mudança ao comando e medir efeitos ao longo do tempo.


## Persistência depois do despacho

Salvei a partida pausada em 4 de março de 1936 com `savegame`. O arquivo foi
gravado no perfil temporário. A flag `snd_pilot_dispatched` aparece no save;
`snd_pilot_enabled` está ausente. Reabri o arquivo pelo menu **Load Game** e
confirmei que o Brasil voltou à data do save. O console retornou
`Result = yes` em escopo de país para
`eval_trigger has_country_flag = snd_pilot_dispatched`.

Avancei 30 dias após recarregar e cheguei a 3 de abril de 1936. O evento do
piloto não reapareceu na observação da virada. O jogo exibiu a conclusão do
foco Aftermath of the Coffee Crisis, que já estava em andamento no save.

## Guia de delegação

A nova decisão e seu evento passaram pelas verificações estáticas de
referências e localização. A exibição do guia ainda não foi testada em jogo.

## Relatório nacional

As referências de evento, as três descrições condicionais e as variáveis de
localização passaram pela validação estática. A renderização e os valores
exibidos ainda precisam de uma verificação em jogo.

## Acompanhamento industrial

Validado estaticamente. A checagem em jogo pode ser feita em uma única
campanha de teste. Ative, confira a mensagem de espera e passe uma virada de
mês após uma mudança conhecida na contagem de fábricas. Compare a variação
com as contagens observadas. Desative e reative para conferir a limpeza da
comparação anterior.

## Coordenação da fila de construção

As verificações estáticas cobrem os dois bloqueios e as referências do
relatório. Para conferir em jogo, autorize o piloto, marque gestão externa e
passe a virada de mês. Confira que a autorização permanece pendente e que
não houve despacho. Libere o Director antes da virada seguinte e confira
uma única ordem, desde que a capital continue elegível.
