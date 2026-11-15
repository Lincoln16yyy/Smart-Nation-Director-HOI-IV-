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
`context_type = decision_category` e consulta variáveis dinâmicas do país
diretamente na localização. O botão restante abre o relatório detalhado,
cuja captura continua separada. A interface anterior foi vista na Itália
com zeros antes do primeiro clique. Esta revisão ainda precisa de teste em jogo.

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

Na Itália de 1936, uma autorização do piloto criou a linha 17 de Carcano
M38 com uma fábrica. A linha original continuou com quatro. Mantenha o
limite de uso único até que exista uma forma confiável de identificar ou
reutilizar linhas de produção existentes.

O efeito documentado `add_equipment_production` cria uma linha. A versão
local da documentação não apresenta uma operação de alocação para uma
linha existente. O menu avisa explicitamente sobre duplicação. O teste
isolado pode ser preparado com `bash scripts/prepare_production_test.sh`.

A supervisão guarda o tipo e o estado da proposta antes de enfileirar. A autorização revalida a gestão da fila, o controle do estado e a vaga. Desligar as rotinas ou a supervisão descarta propostas pendentes. Uma recusa adia o planejamento por 90 dias. A construção automática continua sem essa etapa enquanto a supervisão estiver desativada.

O modo consultivo usa o mesmo planejador de construção, mas registra somente uma recomendação. Os modos consultivo e supervisionado são exclusivos. Trocar de modo descarta a proposta ou recomendação anterior. O planejamento continua sujeito aos controles de gestão externa e de obras pendentes.

A orientação de política interna lê as leis do país por `has_idea` e o poder político por variável dinâmica. Em guerra, prioriza revisar recrutamento com menos de 25 mil de mão de obra e lei de voluntariado ou recrutamento limitado. Depois considera a mobilização econômica inicial. A revisão é consultiva. Os scripts locais não expõem uma operação verificada equivalente à compra de uma lei com seus requisitos e custos.

O relatório lê o total de slots nativos em `amount_research_slots` e distingue o sistema virtual usando a variável `zzars_on` do Automated Research System versão 1. A sugestão consulta duas tecnologias, exclui as concluídas ou em andamento e não inicia pesquisa. A engine local documenta consulta de tecnologia em andamento e efeitos de concessão, mas não foi encontrada uma operação para enfileirar a pesquisa normal por script.

A orientação de focos prioriza estabilidade, logística e indústria militar, ou indústria civil e pesquisa. O acompanhamento nominal usa somente `BRA_coffee_crisis_aftermath` sob a árvore `brazil_tree`, presente no vanilla e no arquivo correspondente do Road to 56. Progresso registrado não confirma seleção atual. A documentação local expõe `focus_progress` por ID e conclusão forçada, sem consulta genérica verificada ao foco ativo.
