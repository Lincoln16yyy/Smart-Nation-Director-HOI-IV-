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

## Estaleiros e mobilização

As variáveis de estaleiros e mão de obra disponível seguem exemplos vanilla
em `events/SEA_Japan.txt` e `common/scripted_effects/RAJ_GOE_scripted_effects.txt`.
A ligação entre decisão, evento e textos passou nos testes estáticos. Em jogo,
compare o relatório com a barra do país e confirme que o alerta de baixo apoio
só aparece em guerra quando a estabilidade não dispara o primeiro alerta.

## Construção automática

Validação estática cobre o agendamento mensal, o intervalo e o uso explícito
da fila normal nos três ramos. Em jogo, confirme fábrica civil em paz e
militar em guerra; quando a fábrica preferida estiver sem vaga, confira a
alternativa de infraestrutura. Depois do primeiro despacho, passe mais uma
virada antes dos 180 dias e verifique que não surge outra ordem. Ativar ou
desativar a opção não apaga o timer. Deixe a obra sem alocação até depois
dos 180 dias e confira que outra ordem não surge. Se for cancelada, libere
o planejamento na decisão própria. Em outro teste, deixe o nível subir no
estado registrado e confira que a construção retoma após o intervalo.

Para testar a seleção territorial junto com a construção automática, use uma
capital sem vaga e outro estado central com vaga. Compare o local e tipo
registrados no relatório com a ordem na fila. Confirme que território ocupado
não se torna candidato e que só há tentativa de infraestrutura na capital
quando nenhum estado elegível comporta a fábrica prioritária.

## Alertas nacionais automáticos

Validação estática cobre o disparo compartilhado do relatório e a comparação
com a prioridade anterior. Em uma campanha, ative com estabilidade abaixo
de 50% e espere duas viradas. Confira um aviso na primeira e nenhum na
segunda. Deixe o risco desaparecer e reaparecer para conferir o novo
aviso. Em guerra, confira a transição de estabilidade baixa para apoio à
guerra baixo quando apenas este último risco permanecer.

## Controle das rotinas automáticas

Validação estática cobre as condições de ativação conjunta e a parada.
Em jogo, inicie as rotinas com gestão externa e confira que alertas e
acompanhamento funcionam enquanto a construção permanece desativada.
Repita sem gestão externa, confira o despacho elegível e pare as rotinas.
A ordem já emitida deve ficar na fila. Reative para conferir que o intervalo
de construção anterior continua valendo.

## Iron Secretary 2.1.0

Validado estaticamente contra o ramo de `ais_run_construction_cycle` em
`common/on_actions/ais_on_actions.txt` do Iron Secretary instalado. Para
a validação em jogo, compare uma virada com logística, aviação ou indústria
ligadas e outra com os três módulos desligados. Antes de cada virada,
confira a origem do bloqueio no relatório. Comércio sozinho não bloqueia.
O ramo que só finaliza ou libera uma ferrovia anterior não bloqueia
quando os três módulos de construção estão desligados.

Na mesma rodada de testes, o alerta de mão de obra deve aparecer em guerra
abaixo de 25 mil quando estabilidade e apoio à guerra não são prioritários.

## Reserva de equipamento e comércio

O limiar de estoque usa o padrão vanilla de `events/SEA_Warlords.txt`.
Verifique durante uma guerra que a reserva abaixo de 500 dispara um aviso
quando os riscos prioritários estiverem ausentes. Confira o status do
comércio ao alternar o módulo comercial do Iron Secretary, independentemente
dos módulos de construção.

## Painel do Director

O painel é um scripted GUI anexado à categoria `snd_director_category`, com
`context_type = decision_category` e `window_name = snd_dashboard`. A ligação
segue `common/decisions/categories/AST_decision_categories.txt`, o painel do
Council of Ministers e o do Automated Research System. Ainda não foi visto em
jogo.

Para verificar, abra **Decisões → Smart Nation Director** e confirme que o
painel aparece acima da lista de decisões, sem cobrir os botões. Compare fábricas, estaleiros e mão de obra com a barra do país sem clicar em atualização. Confirme que o botão **Abrir relatório detalhado** continua abrindo
o evento `snd.3`. Repita com o Iron Secretary ligado e desligado para conferir
a linha de comércio. Registre a resolução usada, porque o painel foi dimensionado
em 490x236 para 1080p.

## Piloto de produção de infantaria

O padrão terrestre está em `history/units/BRA_1936.txt` do vanilla. Em uma
campanha descartável em guerra, compare a fila antes e depois de uma virada
com reserva baixa, tecnologia liberada e capacidade militar disponível.
Confira o modelo, a alocação, a eficiência inicial e o estoque. Repita uma
virada para conferir o limite de uma solicitação. A semântica de capacidade
disponível e o efeito sobre linhas existentes ainda precisam de teste.

No teste da produção, autorize o piloto e marque gestão externa antes
da primeira virada. Confira que a autorização fica suspensa. Libere
a produção e observe a próxima virada elegível. Verifique que o relatório
registra a solicitação e compare com a fila para confirmar a aceitação.

O piloto também cobre equipamento 2 e 3. Em uma campanha descartável com
tecnologia avançada, confirme que o modelo solicitado corresponde à
tecnologia mais alta desbloqueada. Para avaliar duplicatas, compare a
fila antes e depois em variações com e sem uma linha de infantaria existente.

A Itália abriu com o Director no perfil isolado. O setup registrou a
categoria e os três eventos. Os logs identificaram erros no painel
(orientação do contêiner e dimensões dos botões) e rejeitaram as decisões
quando a referência Scripted GUI estava no arquivo de decisões. A correção
move a referência para a categoria e usa sprites vanilla para dimensionar
os botões. A cópia de teste foi sincronizada. Ainda é preciso reler o log
depois de reiniciar antes de testar produção.

### Itália de 1936, com linha de infantaria existente

Após corrigir a categoria e os botões, o setup carregou 19 decisões e três
eventos do Director. O log não registrou erros do Director, e a categoria
apareceu no jogo. As capturas do usuário identificam a mesma campanha antes
da autorização, em 4 de janeiro, e depois do despacho, em 2 de fevereiro.

| Indicador | Antes | Depois |
|---|---|---|
| Fábricas militares em uso | 10/20 | 11/20 |
| Carcano M38 original | 4 fábricas | 4 fábricas |
| Solicitação do piloto | Ausente | Linha 17, Carcano M38, 1 fábrica, 2,54 unidades por semana |

O efeito somou uma fábrica em uma nova linha para o mesmo modelo. Não
aproveitou a linha original. Este cenário confirma a produção pela fila
militar normal e reproduz a duplicata com uma linha preexistente. A variante
sem uma linha existente e o comportamento após recarregar ainda estão
pendentes.


Na captura da Itália, a versão anterior do painel exibia zeros antes de
atualizar. A nova versão consulta variáveis dinâmicas do país sem passar
pelo botão. As ligações foram verificadas estaticamente. Falta conferir se
os valores aparecem corretamente na primeira abertura em jogo.

## Construção supervisionada

Com a construção recorrente e a supervisão ligadas, passe uma virada e confira que há proposta no relatório e nenhuma ordem nova. Salve e recarregue para verificar a persistência. Aprove e confira o mesmo projeto na fila. Em outra variante, marque a gestão externa ou ocupe a última vaga antes de aprovar. A aprovação deve ficar indisponível. Confira também a recusa e o intervalo de 90 dias.

## Construção consultiva

Com a construção recorrente ligada, selecione o modo consultivo. Passe uma virada elegível e confira o estado e a obra sugerida no relatório. Confirme a fila inalterada e a ausência das decisões de aprovação. Troque para supervisão e confira que a recomendação antiga não pode ser aprovada. A cobertura atual é estática.

## Política interna no relatório

Validação estática cobre a ligação do texto e o uso dos identificadores vanilla. Compare em jogo uma campanha em paz, uma em guerra sob economia civil e outra em guerra com pouca mão de obra e recrutamento limitado. Confira o poder político e a prioridade sem mudar a lei.

## Pesquisa no relatório

A leitura e as referências passaram na validação estática. Em jogo, compare o total de slots com a interface de pesquisa, alterne o Automated Research System e confira o aviso. Coloque a tecnologia recomendada em um slot e confirme que a próxima leitura deixa de sugeri-la.

## Focos nacionais no relatório

Em uma campanha com a árvore brasileira `brazil_tree`, compare o texto antes de iniciar, durante e após concluir Consequências da crise do café. Use outra árvore para conferir a orientação genérica. O relatório não seleciona nem conclui focos. Validação atual estática.

## Situação militar

Compare uma campanha em paz e outra em guerra. Confira divisões e navios com a interface do jogo. Confirme que o percentual rumo à capitulação só aparece em guerra antes da capitulação. Validação atual estática.

Com os alertas ligados e o país em guerra, passe uma virada com progresso rumo à capitulação acima de 50%. Confira que a situação militar tem prioridade sobre os outros avisos. Mantenha a condição por mais uma virada para conferir que o aviso não repete. A validação atual é estática.

## Situação diplomática

Abra a visão diplomática com um líder de facção, outro membro e um país fora de facção. Confira o nome e a contagem no menu diplomático. Use um país subordinado para validar o texto de dependência. A validação atual é estática.

## Auditoria estática — 15/11/2026

Executados `python3 scripts/audit_symbols.py PERFIL` e
`python3 -m unittest discover -s tests -v`: 346 definições do Director,
11 mods locais, nenhuma colisão nos domínios cobertos e 22 testes aprovados.
O manifesto da instalação mantém a versão 1.19.3.0. Não foi iniciada uma
campanha nesta etapa. Os testes pendentes do painel, relatórios, modos de
construção e variante de produção continuam pendentes.

## Estados informativos de construção — 15/11/2026

A revisão do relatório passou por 23 testes estáticos. O teste de status
interpreta os triggers de localização e verifica uma única mensagem correta
para cada uma das 512 combinações de oito flags e bloqueio externo. Isso
verifica a lógica booleana, não a interpretação ou apresentação da engine.
A auditoria atualizada conta 354 definições, sem colisões nos tipos cobertos.
Nenhum teste novo em campanha; roteiro acrescentado em TEST_PLAN.md.

## Preparação do ciclo de construção — 15/11/2026

Criados perfis descartáveis BRA e ITA pelos scripts. Confirmados país,
ativação exclusiva do Director e igualdade SHA-256 dos 19 arquivos de cada
cópia com o código do mod. `bash -n` aprovado nos três scripts envolvidos;
os 23 testes Python continuam aprovados. A versão do manifesto local
continua 1.19.3.0. Nesta etapa Wine e campanhas não foram iniciados.
A observação da proposta, aprovação e consumo de capacidade civil continua
pendente; o lançador do Brasil e as instruções estão preparados.

## Construção supervisionada no Brasil — evidências do usuário, 15/11/2026

Na campanha descartável `construction-test.1giVJOvA`, o usuário operou a
interface e forneceu quatro capturas. Em 1º de janeiro de 1936, o painel
mostrou 15 fábricas civis, 3 militares, 2 estaleiros e mão de obra de 572,0
milhares antes de abrir o relatório. O HUD mostrava 572,05 mil; a diferença
é compatível com a precisão de exibição. Confirmação visual em inglês,
resolução 1440×900; português e 1920×1080 continuam pendentes.

Após habilitar supervisão e construção automática, em 2 de fevereiro de
1936 às 21h apareceram as opções de aprovar e recusar proposta. Antes da
aprovação, a fila estava vazia: 7/17 fábricas destinadas a bens de consumo,
15 próprias e 2 de comércio. Após o clique de aprovação, no mesmo horário,
a fila mostrou uma única fábrica civil no Paraná, nível solicitado 1, com
10/15 fábricas alocadas. Bens de consumo permaneceram em 7; o total alocado
passou a 17/17. Isso demonstra proposta sem despacho antecipado e ordem
pela fila regular com consumo de capacidade civil após aprovação.

Não confirma conclusão, avanço de progresso, repetição após intervalo,
recusa, revalidação de estado inválido ou persistência após salvar/carregar.
O `error.log` estava vazio na coleta após aprovação. As capturas fornecidas
foram preservadas apenas na pasta local ignorada `runtime/.../evidence/`.

### Progresso da fábrica supervisionada

Captura fornecida pelo usuário em 11/2/1936 às 8h: a única fábrica civil
no Paraná continuava com 10/15 fábricas alocadas e tinha 252/10800 de
progresso (2% na interface). O tooltip indicava velocidade de construção
28,00, saída das dez fábricas de 50,00, modificadores de economia civil
−30%, foco em exportações +10%, Neglected State −40% e infraestrutura
estadual ×1,40. A previsão exibida era 23/2/1937 à 1h. O custo mostrado era
10800. São valores observados nesta configuração, não constantes do Director.
Isso confirma avanço pela construção regular, sujeito aos modificadores
exibidos pelo jogo; conclusão e persistência após recarregar ainda pendentes.
Captura local: `evidence/queue-progress-feb11.png` no perfil descartável.

### Fila após salvar/recarregar

Após a instrução de salvar e recarregar, o usuário forneceu nova captura em
11/2/1936 às 8h. A fila continuava com uma única fábrica civil no Paraná,
252/10800 (2%), 10/15 fábricas alocadas e previsão de 23/2/1937 à 1h.
O save ` snd_teste_construcao.hoi4` foi localizado exclusivamente no perfil
descartável (o nome contém um espaço inicial). O game.log consultado não
traz uma linha explícita de recarga; a evidência visual posterior ao passo
solicitado sustenta a preservação da fila e do progresso, sem demonstrar
por si só as flags internas do Director. Falta conferir o relatório após
recarga e atravessar outra virada mensal sem gerar duplicatas.
Captura local: `evidence/queue-after-reload-feb11.png`.

### Relatório após recarga e falha no temporizador

A captura seguinte, ainda em 11/2/1936 às 8h, mostrou última ordem de fábrica
civil no Paraná, proposta ausente e espera por aumento de nível da obra.
O relatório também exibiu 17 civis/3 militares, 2 estaleiros, 572,8 mil de
mão de obra, dois slots nativos e alerta de estabilidade abaixo de 50%.
Os 17 civis do relatório contrastam com as 15 próprias mais duas de comércio
na fila: a contagem dinâmica inclui capacidade de comércio nesta observação;
não equivale exclusivamente ao total de fábricas próprias. A interpretação
completa desse indicador ainda exige comparação adicional.

O status pulou o intervalo de 180 dias, que deveria ter prioridade sobre a
obra pendente. Inspeção somente de leitura do save binário encontrou o nome
da flag de cooldown com valor zero e a flag de obra pendente com valor um.
Os exemplos vanilla locais em `common/national_focus/usa.txt`
(`USA_great_depression_cooldown`) e `common/decisions/TUR.txt` definem flags
temporárias com `value = 1`. O Director omitia esse campo em ambos os
intervalos (180 dias e 90 dias após recusa). Corrigidas as duas definições
para usar valor explícito e ajustadas as asserções estáticas.

A correção ainda não foi executada na engine. A campanha aberta usa a cópia
anterior; alterar o repositório não atualiza esse processo nem corrige o
valor já salvo. A obra pendente continua sendo uma barreira independente,
mas o intervalo da versão testada não deve ser considerado validado.
Repetir aprovação/recusa em perfil novo com código corrigido e conferir o
status e a persistência dos temporizadores antes de declarar a correção
confirmada em runtime.
