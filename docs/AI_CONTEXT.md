# Contexto para continuidade

O [prompt original do projeto](PROJECT_PROMPT.md) descreve a visão completa,
os módulos pretendidos e os critérios de aceitação. O [estado atual](STATUS.md)
tem precedência sobre as instruções históricas de iniciar o projeto do zero.

O projeto busca máxima autonomia legítima no país humano do HOI4 1.19.3.0. O perfil pessoal usa RT56, Iron Secretary, Automated Research System, Design Bureau, General Staff e Modifier Icons. Council of Ministers está instalado e desabilitado devido à versão e à colisão com localização do General Staff.

A implementação atual é um piloto independente de dependências. Seus arquivos, flags e eventos usam `snd`. As decisões ficam no menu vanilla. Não há controle de console pelo mod. Preserve o perfil pessoal e execute [o roteiro](TEST_PLAN.md) em campanhas descartáveis.

Leia [estado](STATUS.md), [evidências de execução](RUNTIME_TESTS.md) e [lacunas](GAP_ANALYSIS.md) antes de ampliar o escopo. A fila de construção, o estado após recarregar e a ativação de `human_ai` já foram verificados. O relatório e o acompanhamento industrial passaram pela validação estática. Verifique a rotina de concessão do Automated Research antes de qualquer integração. Rodar `python3 -m unittest discover -s tests -v` verifica o pacote estático.

A decisão **Consultar delegação à IA** abre um evento informativo. Ela não
altera a fila ou o modo de controle. O comando continua manual no console.

A decisão **Consultar situação nacional** captura as contagens de fábricas
civis e militares do país e abre um relatório consultivo. Estabilidade abaixo
de 50% tem prioridade sobre a recomendação de guerra ou de paz.

O acompanhamento industrial guarda as contagens anteriores e suas diferenças
em variáveis de país. As flags de país controlam a coleta e a exibição no
relatório. Só existem duas medições por indicador na comparação, sem série
histórica ou registro de causas da variação.

## Próxima sessão

- Veja a [auditoria dos mods](MOD_AUDIT.md) antes de criar integrações. O
  Automated Research observado usa slots virtuais; a IA nativa já mostrou uso
  dos slots normais no Brasil.
- Continue pelo código e pela documentação. Reserve testes em jogo para
  dúvidas concretas que afetam a implementação. Quando precisar do jogo,
  avise o usuário para que ele abra a tela necessária. O usuário não precisa
  fornecer números manualmente.
- O trabalho está no [PR inicial](https://github.com/Lincoln16yyy/Smart-Nation-Director-HOI-IV-/pull/1).
  Preserve a distinção entre resultados estáticos e resultados vistos em
  campanha e registre o avanço na documentação.

A gestão externa da construção pode ser declarada pelo jogador. O Director
também lê as flags que acionam o ciclo de construção no Iron Secretary
2.1.0. Se qualquer uma dessas condições corresponder, o Director bloqueia
novas autorizações e o despacho mensal. O relatório mostra a origem do
bloqueio. A autorização pendente continua disponível para cancelar.
Marque a gestão externa manualmente para `human_ai` e outros mods.

O relatório usa `num_of_naval_factories` para estaleiros e `manpower_k` para
mão de obra disponível em milhares. O alerta de baixo apoio à guerra (abaixo
de 50%) aparece em guerra, desde que a estabilidade esteja em pelo menos 50%.

A construção automática é opcional e continua entre viradas mensais até
ser desativada. O Director procura fábricas primeiro na capital e depois em outros estados centrais sob posse e controle
e prioriza fábrica civil em paz ou militar em guerra, com infraestrutura
na capital como alternativa. O intervalo de 180 dias limita novas ordens do Director.
Além do intervalo, a automação aguarda aumento no nível do mesmo tipo de
edifício no estado registrado. É um indicador indireto e outra obra do mesmo
tipo no local pode satisfazê-lo. Se a ordem tiver sido cancelada ou o estado
perdido, o jogador pode liberar a espera sem remover o intervalo.

O relatório registra o tipo e o estado da última ordem automática. Esse
registro indica o pedido de construção, cujo progresso pode ser conferido
na fila vanilla.

Os alertas automáticos são opt-in e rodam no ciclo mensal. A decisão e o
alerta compartilham o disparo de `snd.3`, com os mesmos indicadores e
prioridades. `snd_last_reported_risk` persiste o último risco. O risco zero
rearma a próxima ocorrência sem publicar relatório.

O controle único inicia os módulos sem reiniciar medições ou alertas ativos.
Ele só ativa a construção recorrente se a gestão externa estiver desmarcada
e não houver piloto pendente. A parada mantém o registro da última ordem,
o intervalo de construção e a preferência de gestão externa.

O alerta de mão de obra é uma heurística consultiva para países em guerra,
com limiar fixo de 25 mil. Ele fica atrás dos alertas de estabilidade e
apoio à guerra. Nenhuma lei de recrutamento é alterada pelo alerta.

O relatório lê as duas flags do comércio semanal do Iron Secretary 2.1.0.
Elas indicam configuração habilitada, sem confirmar contratos ou importações.
O alerta de equipamento de infantaria usa reserva abaixo de 500 em guerra,
após estabilidade, apoio à guerra e mão de obra na ordem de prioridade.

A categoria de decisões declara `scripted_gui = snd_dashboard`. O painel usa
`context_type = decision_category` e não mantém estado próprio: os botões
chamam `snd_refresh_dashboard` e `snd_show_national_report`, e a captura de
variáveis é compartilhada por `snd_capture_report_values`. O painel foi
dimensionado em 490x236 e ainda não foi visto em jogo.

O piloto de produção é opt-in separado das rotinas gerais e emite no máximo
uma solicitação por país. A rotina pede uma fábrica em uma linha de armas de
infantaria já desbloqueadas, sem alterar estoque, eficiência ou progresso.
Até confirmar a semântica das fábricas disponíveis e o comportamento com
linhas existentes, trate o piloto como experimental e não o combine com
gestão de produção externa.

A gestão externa da produção é uma opção manual independente da construção.
Ela impede novas autorizações e o despacho de um piloto já autorizado,
sem apagar a autorização pendente. O relatório mostra a gestão externa ou
o estado do piloto. Uma ordem emitida é um pedido, sujeito à fila do jogo.

A seleção de armamento usa a ordem 3, 2, 1 e 0, conforme a tecnologia.
Os quatro vínculos tecnologia/equipamento correspondem ao vanilla e ao
Road to 56 instalado. Estoque e capacidade militar não identificam linhas
existentes. A autorização permanece de uso único.
