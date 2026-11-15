# Registro de fases

## Primeira entrega

1. Confirmada a instalação 1.19.3.0 e inventariados os 11 mods instalados.
2. Classificadas sobreposições por conteúdo idêntico ou diferente e registrado o comando `human_ai` presente no executável.
3. Criado o piloto de infraestrutura com flags persistentes, evento e localização em português brasileiro e inglês.
4. Quatro testes estáticos aprovados. A engine registrou a carga da categoria, das decisões e do evento no perfil temporário.
5. Brasil em 1936 exibiu a opção de cancelamento depois da autorização. O console confirmou a ativação de `human_ai`.

6. O Brasil humano recebeu uma obra de infraestrutura no Rio de Janeiro na virada mensal, com dez fábricas civis alocadas pela fila regular.

7. Adicionado guia de delegação à IA nativa no menu de decisões. Validado estaticamente.
8. Implementado relatório nacional sob demanda com contagem de fábricas e prioridade condicional. Validação estática concluída.
9. Adicionado acompanhamento industrial opcional ao relatório nacional, com amostragem mensal sem eventos automáticos. Validação estática concluída.
10. Adicionado controle manual para suspender ordens de construção do Director durante gestão externa. Validação estática concluída.
11. Relatório ampliado com estaleiros, mão de obra disponível e alerta de baixo apoio à guerra. Validação estática concluída.
12. Implementada construção recorrente por prioridade em paz e guerra. O despacho revalida a capital e respeita a gestão externa e o intervalo de 180 dias. Validação estática concluída.
13. A construção automática passou a procurar vagas em outros estados centrais quando a capital não é elegível. O relatório registra o último pedido. Validação estática concluída.
14. Adicionada revisão mensal opt-in para avisar o jogador quando a prioridade de risco muda. Validação estática concluída.
15. Adicionado controle único das rotinas automáticas, preservando a gestão externa e o intervalo de construção. Validação estática concluída.
16. Construção recorrente agora espera o aumento do nível no estado registrado. Cancelamentos podem liberar a espera sem apagar o intervalo. Validação estática concluída.
17. A revisão mensal ganhou um alerta de mão de obra abaixo de 25 mil em guerra, após as prioridades de estabilidade e apoio à guerra. Validação estática concluída.
18. O Director passou a consultar as flags que acionam construção no Iron Secretary 2.1.0 e suspende suas ordens enquanto houver sobreposição. Validação estática concluída.
19. Adicionado alerta de reserva baixa de equipamento de infantaria e status comercial do Iron Secretary no relatório. Validação estática concluída.
20. Primeiro painel do Director via scripted GUI dentro da categoria de decisões, reutilizando a captura do relatório. Validação estática concluída.
20. Implementado piloto opcional de linha de produção de infantaria. Validação estática concluída.
21. Adicionado controle de gestão externa da produção e status do piloto no relatório. Validação estática concluída.
22. Piloto de infantaria passou a escolher o modelo mais avançado entre os quatro níveis comuns ao vanilla e ao Road to 56. Validação estática concluída.
24. A abertura da Itália revelou erros de leitura no painel e no arquivo de decisões. Ajustados o vínculo da categoria e os botões conforme o vanilla.
25. O painel e as decisões carregaram após a correção. Na Itália, o piloto de infantaria abriu outra linha de Carcano M38 com uma fábrica, preservando as quatro da linha anterior.

26. O menu passou a explicitar que o piloto abre outra linha. O lançador isolado e o roteiro documentam a reprodução do teste.
27. O painel passou a ler os indicadores dinâmicos do país diretamente. Removidos o botão e o efeito de atualização manual. Validação estática concluída.

28. Adicionado modo supervisionado de construção com proposta persistente, aprovação e recusa. Validação estática concluída.

29. Adicionado modo consultivo de construção, com recomendação mensal e sem despacho. Validação estática concluída.

30. Adicionada avaliação consultiva de recrutamento e mobilização econômica ao relatório nacional. Validação estática concluída.

31. Adicionada leitura de slots nativos, identificação do sistema virtual e sugestão contextual de pesquisa. Validação estática concluída.

32. Adicionadas orientação de focos e leitura de progresso de um foco brasileiro conhecido. Validação estática concluída.

33. Adicionada a visão militar de guerra, forças e capitulação. Validação estática concluída.

34. Integrado alerta de risco de capitulação à revisão mensal. Transições para o risco abrem o relatório militar. Validação estática concluída.

35. Adicionada visão diplomática de facção, liderança e países subordinados. Validação estática concluída.

36. Adicionada auditoria reproduzível de símbolos do Director contra os mods locais.
    Em 15/11/2026, 346 definições comparadas a 11 mods, sem colisões ou duplicatas
    nos domínios cobertos. Versão 1.19.3.0 reconfirmada. 22 testes estáticos
    aprovados; nenhum novo teste em campanha.

37. Corrigido o status de construção para mostrar bloqueios também no modo
    consultivo e distinguir espera por aprovação, supervisão sem proposta e
    adiamento de 90 dias após recusa. Textos em português e inglês atualizados.
    23 testes aprovados, incluindo seleção única de status em 512 combinações.
    Auditoria atualizada: 354 definições, sem colisões nos domínios cobertos.
    Nenhuma campanha iniciada nesta etapa.

38. Preparado cenário descartável do Brasil para validar o ciclo de construção.
    O lançador compartilhado lê o país validado e mantém Itália como padrão
    para perfis antigos. Preparação registra commit-base e copia o roteiro.
    Verificados os perfis BRA/ITA, hashes dos 19 arquivos do mod, sintaxe shell
    e 23 testes Python. Engine não iniciada; observação em campanha pendente.

39. Usuário executou a campanha descartável do Brasil e forneceu capturas:
    painel com dados antes do relatório, proposta de construção em fevereiro,
    fila vazia antes da aprovação e uma fábrica civil no Paraná após aprovar,
    com 10/15 fábricas alocadas. `error.log` vazio na coleta. Progresso e
    save/load ainda pendentes; sem alteração de código nesta observação.

40. Captura do usuário em 11/2/1936 confirmou progresso regular da fábrica
    civil supervisionada no Paraná: 252/10800, velocidade 28/dia, dez fábricas
    alocadas e prazo previsto 23/2/1937. Save/load e conclusão pendentes.

41. Captura após o passo solicitado de save/load preserva a única fábrica
    do Paraná, 252/10800 e dez fábricas alocadas. Save localizado no perfil
    descartável; sem linha explícita de recarga em game.log. Verificação das
    flags via relatório e da virada seguinte continua pendente.

42. Relatório após recarga preservou última ordem e espera pela obra, mas
    pulou o cooldown. Save indica cooldown com valor zero. Adicionado
    `value = 1` às flags temporárias de 180/90 dias conforme vanilla local.
    Reteste em engine pendente; campanha aberta continua na cópia anterior.
    Relatório exibiu 17 civis enquanto fila indicava 15 próprias + 2 comerciais.

43. Reteste pelo usuário na cópia corrigida confirmou mensagem do intervalo
    de 180 dias em 1/2/1936 às 3h após aprovar fábrica civil na Bahia. Ainda
    faltam persistência do cooldown, expiração e teste do adiamento por recusa.

44. Captura após o passo de save/load na versão corrigida preservou a mensagem
    do cooldown de 180 dias e a última ordem na Bahia em 1/2/1936 às 3h.
    Expiração e bloqueio nas viradas seguintes ainda pendentes.

45. Captura de 1/3/1936 confirmou uma única obra na Bahia após nova virada
    mensal e save/load, com progresso 588/10800 e dez fábricas alocadas.
    Cooldown e espera pela obra não foram isolados; expiração ainda pendente.

46. Relatório do usuário em 3/9/1936 mostrou transição de cooldown para espera
    pela obra na Bahia, sem proposta pendente. Expiração observada até essa
    data; duração exata não medida. Conclusão e retomada ainda pendentes.

47. Fila em 3/9/1936 confirmou uma única fábrica na Bahia, 4494/10800 (41%)
    e dez fábricas alocadas após expiração do cooldown. Conclusão prevista
    para 1/7/1937; conclusão real e retomada ainda não observadas.

48. Em 3/8/1937, relatório apresentou nova proposta no Paraná, Bahia como
    última ordem e indicador civil aumentado de 17 para 18. Confirmada
    retomada do planejamento após liberação da espera. Recusa ainda pendente.

49. Recusa da proposta do Paraná em 3/8/1937 removeu a proposta e mostrou
    adiamento de 90 dias, mantendo a última ordem na Bahia. Persistência e
    expiração do adiamento ainda pendentes.

50. Captura de 14/9/1937 após o passo de save/load mostrou adiamento de
    90 dias ainda ativo e nenhuma proposta após virada de setembro.
    Expiração do adiamento permanece pendente.

51. Em 2/12/1937, relatório mostrou proposta em Minas Gerais após expiração
    do adiamento por recusa, com Bahia como última ordem. Consolidada a rodada
    de validação do Brasil; datas exatas de expiração não medidas. Próximas
    lacunas: gestão externa, modo consultivo e revalidação de estado inválido.

52. Gestão externa manual bloqueou aprovação preservando proposta; usuário
    confirmou desbloqueio ao permitir ordens. Em 2/1/1938, troca para modo
    consultivo gerou recomendação no Rio Grande do Sul, mantendo última ordem
    na Bahia. Conferência da fila consultiva ainda pendente.

53. Usuário confirmou em texto que a recomendação consultiva não iniciou obra
    na fila. Consolidado com o relatório de 2/1/1938; sem captura adicional
    desse passo. Gestão externa e consultivo não exigem repetição desta rodada.

54. Em 15/11/2026, consolidados os resultados de gestão externa e consultivo
    e preparado teste específico de revalidação de vaga na aprovação. Os 23
    testes estáticos passaram. Nenhuma nova validação de engine nesta sessão;
    PR #15 segue aberto, sem merge.
