# Smart Nation Director

Mod experimental para Hearts of Iron IV 1.19.3.0. O objetivo é delegar a administração do país do jogador preservando as regras e os custos do jogo.

A versão 0.1.0 contém um piloto de infraestrutura. Em **Decisões → Smart Nation Director**, autorize o piloto. No próximo ciclo mensal elegível, o script solicita um nível de infraestrutura na capital pela fila normal. A autorização pode ser revogada antes do envio. O lançamento é limitado a uma ordem por país e campanha. O evento indica a emissão do pedido. Confira a aceitação e o progresso na fila.

## Instalação para teste

Copie `Smart_Nation_Director.mod` e a pasta `Smart_Nation_Director/` para `mod/` em um perfil de teste. Habilite apenas o Director e inicie uma campanha nova em modo normal. Teste sem Iron Secretary, outras automações e `human_ai` para atribuir o resultado ao script certo.

O protótipo ainda não tem os quatro modos de autonomia, integração com mods externos ou painel. Consulte [estado](docs/STATUS.md), [roteiro reproduzível](docs/TEST_PLAN.md) e [auditoria de mods](docs/MOD_AUDIT.md).

```bash
python3 -m unittest discover -s tests -v
python3 scripts/audit_mods.py "/caminho/perfil-hoi4"
```

## Delegar à IA nativa

Abra **Decisões → Smart Nation Director → Consultar delegação à IA** para ver as instruções de `human_ai`. O comando é executado pelo jogador no console. Em um teste isolado, a IA ocupou slots normais de pesquisa, escolheu um foco e administrou construção, comércio e organização militar.

**Consultar situação nacional** mostra a contagem de fábricas civis e militares e sugere uma prioridade conforme a estabilidade e a situação de guerra. A decisão atualiza os números a cada abertura.

Use **Ativar acompanhamento industrial** para adicionar a variação de fábricas ao relatório nacional. A primeira comparação vai da ativação à próxima virada de mês. As demais comparam duas viradas consecutivas. Reativar começa uma nova comparação.

Antes de deixar a IA nativa ou outro mod cuidar da construção, use **Indicar construção gerida externamente**. Isso pausa as ordens do Director e preserva uma autorização pendente. Quando a outra automação parar, **Liberar construção para o Director** permite retomá-la.

O relatório também mostra estaleiros e mão de obra disponível, em milhares. Em guerra, prioriza um alerta de apoio à guerra abaixo de 50% quando a estabilidade está em pelo menos 50%.

**Ativar construção automática** mantém a avaliação mensal de obras ligada. O Director prioriza uma fábrica civil em paz, uma militar em guerra e infraestrutura na capital se a fábrica preferida não couber em um estado central controlado. Cada ordem usa a fila normal. A rotina espera pelo menos 180 dias e um aumento do nível desse edifício no estado antes de pedir outra obra. Se você cancelar a obra ou perder o estado, libere o planejamento pelo menu. A gestão externa suspende novos despachos. O relatório registra o tipo e o local da última ordem automática.

A categoria **Smart Nation Director** também mostra um painel compacto com fábricas civis e militares, estaleiros, mão de obra e o status do comércio. O painel consulta esses dados do jogo sem exigir atualização manual. **Abrir relatório detalhado** tira uma nova leitura e mostra a prioridade sugerida.

**Ativar alertas nacionais automáticos** abre o relatório quando começa ou muda uma prioridade de risco. Em condições estáveis, ou enquanto a mesma prioridade persistir, a revisão mensal segue em silêncio.

**Iniciar rotinas automáticas do Director** liga acompanhamento, alertas e, quando a fila estiver livre para o Director, construção recorrente. **Parar rotinas automáticas do Director** interrompe novas ações, cancela o piloto pendente e mantém as obras que já estão na fila.

O Director reconhece automaticamente a configuração de construção do Iron Secretary 2.1.0 e aguarda enquanto ela puder emitir ordens. Use o controle manual de gestão externa para a IA nativa e outros mods.

O **piloto de produção de infantaria** é uma autorização separada. Em guerra, a rotina avalia mensalmente a reserva e a capacidade militar. Pode solicitar uma única linha para o modelo mais avançado já pesquisado entre os quatro níveis compatíveis com o vanilla e o Road to 56. Use com a produção sob seu controle até a validação em jogo.

Se a IA nativa ou outro mod assumir a produção militar, use **Indicar produção gerida externamente**. A autorização pendente fica guardada até você liberar a produção para o Director.

**Autorizar nova linha de infantaria** é uma autorização de uso único.
Confira a fila de produção primeiro: o teste da Itália confirmou que o
efeito cria outra linha mesmo quando o modelo já está em produção. Para
aumentar a alocação da linha atual, use os controles normais de produção.

Com a construção recorrente ligada, **Exigir aprovação para novas obras** faz o Director escolher o projeto na virada do mês e aguardar sua decisão. O relatório mostra o tipo e o estado. Aprovar revalida as condições e usa a fila normal. Recusar adia a próxima proposta por pelo menos 90 dias.

Com a construção recorrente ligada, **Usar modo consultivo na construção** atualiza a recomendação do Director nas viradas elegíveis. Consulte o tipo e o estado no relatório. A decisão de construir continua na fila normal do jogador.

O relatório também mostra o poder político e avalia se vale revisar as leis de recrutamento ou de mobilização econômica. A escolha e o custo continuam no menu de leis do jogo.

Na seção de pesquisa, o relatório mostra o total de slots nativos e indica se o Automated Research System está ativo pelos indicadores do mod. O Director sugere tecnologias com base na situação e omite as que já foram pesquisadas ou estão em andamento.

O relatório também sugere áreas para o próximo foco e pode mostrar o progresso registrado ou a conclusão de **Consequências da crise do café** na árvore brasileira que contém esse foco.
