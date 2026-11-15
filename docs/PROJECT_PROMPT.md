> **Para retomar o projeto**, leia primeiro [AI_CONTEXT.md](AI_CONTEXT.md) e
> [STATUS.md](STATUS.md). O texto abaixo é o prompt original da missão. Use-o
> para orientar a construção e consulte os registros atuais para saber quais
> etapas já foram executadas e quais decisões foram ajustadas desde então.

# MISSÃO: DESENVOLVER O SMART NATION DIRECTOR PARA HEARTS OF IRON IV

Você é meu agente principal de desenvolvimento, pesquisa, engenharia de mods, integração, testes e documentação.

Sua missão é desenvolver um mod completo chamado **Smart Nation Director**, para Hearts of Iron IV, inspirado nos meus projetos de automação para Victoria 3.

**Repositório obrigatório:**
https://github.com/Lincoln16yyy/Smart-Nation-Director-HOI-IV-

**Versão inicial do jogo:** Hearts of Iron IV 1.19.3. Confirme a versão diretamente na instalação antes de desenvolver.

**Ambiente:** Linux CachyOS, com jogo executado via Hydra Launcher/Wine.

**Diretório conhecido dos mods:**

`$HOME/.config/hydralauncher/wine-prefixes/394360/drive_c/users/steamuser/Documents/Paradox Interactive/Hearts of Iron IV/mod`

Esse caminho é uma referência inicial. Descubra os caminhos reais do executável, dos arquivos vanilla, dos logs, dos saves e das pastas de cada mod.

Você tem autorização para investigar os arquivos locais, criar scripts auxiliares, desenvolver o projeto, instalar dependências de desenvolvimento adequadas, executar testes não destrutivos e publicar código no repositório informado.

Não altere arquivos originais de terceiros, não sobrescreva saves, não distribua arquivos proprietários do jogo e não faça merge de pull requests sem minha aprovação.

---

# 1. OBJETIVO CENTRAL

Quero transformar Hearts of Iron IV em uma experiência na qual **eu escolho o país e observo uma inteligência administrativa governá-lo praticamente sozinha**.

Não quero ficar administrando manualmente fábricas, pesquisas, exércitos, comércio, produção, focos nacionais ou decisões repetitivas.

Quero agir como observador e autoridade política final.

O comportamento ideal é:

1. Inicio uma campanha escolhendo um país.
2. Ativo o Smart Nation Director.
3. Escolho o nível de autonomia.
4. A IA analisa a situação nacional.
5. O governo decide suas prioridades.
6. Os sistemas existentes e nossos módulos executam ações.
7. O país desenvolve sua economia, tecnologia, política e forças armadas.
8. A IA reage automaticamente a crises, ameaças e oportunidades.
9. Recebo eventos explicando decisões relevantes e suas consequências.
10. Acompanho tudo em um painel simples, em português brasileiro.

**O objetivo é minimizar minhas ações obrigatórias, idealmente limitando-as a aceitar, rejeitar ou acompanhar grandes decisões.**

Não invente capacidades que a engine não oferece.

Descubra e documente exatamente o que pode ser automatizado por:

- Inteligência artificial nativa.
- Comandos de depuração e funcionalidades de teste.
- AI strategies.
- AI strategy plans.
- Scripted GUI.
- Scripted effects e triggers.
- On-actions.
- Eventos e decisões.
- Focos nacionais e seus pesos de IA.
- Mods já instalados.
- Outras interfaces de automação comprovadamente disponíveis.

Quando não existir uma forma confiável de realizar uma ação, registre a limitação e proponha alternativas, sem fingir que a função está implementada.

---

# 2. RESULTADO QUE QUERO NO JOGO

O sucesso não é simplesmente o jogo abrir sem erros.

O sucesso é iniciar como Brasil, Alemanha, França, União Soviética, Japão ou outro país, deixar o tempo passar e observar o governo tomar decisões concretas.

Quero que, na medida em que a engine permitir, o sistema:

- Construa e expanda infraestrutura e fábricas.
- Organize produção industrial e militar.
- Administre importação de recursos.
- Pesquise tecnologias.
- Escolha focos nacionais.
- Organize recrutamento e modelos de divisões.
- Prepare tropas e logística.
- Planeje e conduza conflitos militares.
- Decida políticas diplomáticas.
- Defina prioridades políticas.
- Escolha líderes e governos quando as mecânicas permitirem.
- Considere mudanças de ideologia diante de crises e oportunidades.
- Acompanhe riscos econômicos e militares.
- Reavalie suas estratégias ao longo da campanha.
- Explique o que fez e por quê.

Tudo isso deverá funcionar **com o país controlado pelo jogador**, não apenas com países controlados pela IA do jogo.

Se uma operação só funcionar com a IA nativa e não puder ser aplicada diretamente ao país humano, investigue se é possível delegar essa operação de forma controlada.

Nunca confunda ajustar prioridades da IA com executar efetivamente a ação.

---

# 3. PRINCÍPIO FUNDAMENTAL: PRIMEIRO APROVEITAR O QUE JÁ EXISTE

Não recrie funcionalidades prontas se os mods instalados já as executam corretamente.

O novo mod precisa atuar como um **orquestrador inteligente**, complementando e integrando as melhores funcionalidades existentes.

## 3.1 Mods aprovados como base inicial

Investigue estes mods:

1. The Road to 56 — expansão histórica principal.
2. Iron Secretary — automação econômica e logística.
3. Automated Research System — pesquisas.
4. Council of Ministers — automação administrativa, caso seja instalado e aprovado.
5. Design Bureau — sistemas industriais e de equipamentos.
6. Handy Game Tool — General Staff — ferramentas de gestão estratégica de aliados.
7. Modifier Icons — melhorias visuais, caso compatível.

## 3.2 Mods excluídos da configuração principal

Não incorpore automaticamente:

- More Politics.
- Coloured Buttons v1.9.
- Minimalistic GUI.
- Millennium Dawn.
- Kaiserreich.
- Road to 56: Expanded.

O motivo é reduzir conflitos, sobreposições de funcionalidades e incompatibilidades.

Esses mods podem ser estudados como referências de design quando permitido, mas não devem ser dependências da configuração inicial.

**Council of Ministers pode estar ausente. Não presuma que foi instalado.**

## 3.3 Auditoria obrigatória

Antes de escrever o Director:

- Identifique todos os mods realmente instalados.
- Identifique quais estão ativos e inativos.
- Leia todos os arquivos `.mod` e `descriptor.mod` relevantes.
- Verifique `supported_version`, dependências e `replace_path`.
- Confirme versões reais.
- Localize as funcionalidades disponíveis.
- Liste arquivos que disputam os mesmos caminhos.
- Identifique arquivos que apenas duplicam conteúdo e arquivos que efetivamente entram em conflito.
- Analise IDs de eventos, decisões, ideias, variáveis, GUI e localização.
- Verifique se cada mod funciona no país do jogador.
- Identifique funções que exigem interface manual.
- Verifique se os mods existentes oferecem configurações para desativar módulos específicos.
- Não considere compatibilidade garantida só porque o jogo inicia.

Produza `docs/MOD_AUDIT.md`.

Produza `docs/MOD_COMPATIBILITY.md`.

Produza `docs/GAP_ANALYSIS.md`.

Para cada funcionalidade, informe:

- Mod responsável.
- Mecanismo utilizado.
- Compatibilidade.
- Ação realmente realizada.
- Forma de ativação.
- Problemas conhecidos.
- Lacunas.
- Evidência obtida.
- Se foi testada em jogo real.

---

# 4. PESQUISA OBRIGATÓRIA: COMO MODDERS EXPERIENTES DESENVOLVEM MODS DO HOI4

Antes de implementar, estude a documentação, exemplos comunitários e os arquivos vanilla.

Referências iniciais:

**Documentação geral**
https://hoi4.paradoxwikis.com/Modding

**Estrutura dos mods**
https://hoi4.paradoxwikis.com/Mod_structure

**IA**
https://hoi4.paradoxwikis.com/AI_modding

**Scripted GUI**
https://hoi4.paradoxwikis.com/Scripted_GUI_modding

**Eventos**
https://hoi4.paradoxwikis.com/Event_modding

**Decisões**
https://hoi4.paradoxwikis.com/Decision_modding

**Comandos**
https://hoi4.paradoxwikis.com/Console_commands

**CWTools**
https://github.com/cwtools/cwtools-vscode

**Regras de validação**
https://github.com/cwtools/cwtools-hoi4-config

**Ferramentas adicionais**
https://marketplace.visualstudio.com/items?itemName=UC-ModdingUtilities.hoi4-modding-tools

Use essas fontes como pontos de partida, não como substitutos da versão instalada do jogo. Links ou ferramentas podem estar desatualizados; confirme antes de confiar neles.

## 4.1 Técnicas práticas que você deve aprender

### Técnica A — Procurar exemplos no próprio jogo

Antes de escrever um efeito, trigger ou mecanismo de IA, procure exemplos equivalentes nos arquivos vanilla da versão 1.19.3.

Descubra:

- Onde o comando aparece.
- Qual escopo utiliza.
- Quais parâmetros aceita.
- Como o jogo aciona esse comando.
- Se ele pode atingir o país humano.
- Quais condições tornam a execução válida.

Prefira reproduzir padrões válidos a inventar sintaxe.

### Técnica B — Desenvolver com debug mode

Configure uma maneira segura de executar o jogo com `-debug`.

Investigue os comandos:

- `human_ai`
- `aiview`
- `gui`
- `reload`
- `reloadinterface`
- `trigger_docs`
- `effect_docs`
- `eval_effect`
- `eval_trigger`
- `list_vars`
- `list_flags`
- `imgui`

Confirme a sintaxe disponível em 1.19.3.

Use os comandos apenas em saves de teste.

### Técnica C — Examinar os logs corretos

Investigue, conforme disponibilidade:

- `error.log`
- `game.log`
- `text.log`
- `scripted_ai.log`
- `setup.log`
- Logs de inicialização e relatórios de crash.

Compare uma execução vanilla com uma execução modificada.

Diferencie erros anteriores do jogo e novos erros introduzidos pelo mod.

### Técnica D — Testar as menores alterações possíveis

Desenvolva primeiro um efeito mínimo que produza um resultado observável.

Depois valide:

1. O arquivo é carregado?
2. O script está correto?
3. O trigger é satisfeito?
4. A ação foi executada?
5. O resultado apareceu no país humano?
6. A ação respeitou seus custos?
7. A mudança persistiu após salvar e carregar?
8. A integração com outros mods continuou funcionando?

Somente depois amplie a funcionalidade.

### Técnica E — Evitar sobrescrever o vanilla

Use arquivos novos com prefixo único.

Prefira integrações por scripted effects, triggers, eventos, decisões e interfaces próprias quando possível.

Não copie arquivos vanilla inteiros sem necessidade.

Quando um override for inevitável, registre exatamente:

- Arquivo substituído.
- Motivo.
- Alterações introduzidas.
- Versão de origem.
- Mods afetados.
- Plano de atualização.

### Técnica F — Desenvolvimento modular

Centralize lógica reutilizável.

Evite repetir efeitos e condições.

Use namespace `snd` ou equivalente, respeitando convenções de cada tipo de arquivo.

Não use IDs genéricos que possam colidir com outros mods.

### Técnica G — Controlar desempenho

Evite executar verificações globais complexas todos os dias.

Prefira verificações espaçadas, eventos oportunos e cooldowns.

Não percorra todos os países, estados e unidades em loops aninhados sem necessidade.

Investigue ferramentas de profiling do HOI4, inclusive comandos `imgui` disponíveis.

Meça impacto de desempenho no jogo real.

### Técnica H — Ferramentas de validação

Configure CWTools ou alternativa equivalente.

Investigue HOI4 Modding Tools e Hearts of Modding.

Valide:

- Sintaxe.
- Chaves e escopos.
- Triggers e efeitos.
- Referências de eventos.
- Decisões.
- Localização.
- Elementos gráficos.
- Sprites.
- Definições duplicadas.
- Arquivos e caminhos.

Um lint aprovado não substitui teste em jogo real.

Documente essas técnicas em `docs/DEVELOPMENT_GUIDE.md`, com exemplos que funcionem na instalação local.

---

# 5. PROVA DE CONCEITO CRÍTICA: IA NO PAÍS HUMANO

Esta é a etapa mais importante do projeto.

Investigue detalhadamente o comando `human_ai`.

Quero descobrir se ele permite que a IA nativa administre meu país enquanto continuo sendo o jogador.

Crie uma campanha de teste com um país adequado, preferencialmente Brasil em 1936.

Faça backup dos saves.

Compare:

1. País humano sem automação.
2. País humano com `human_ai`.
3. País humano com `human_ai` e um mod de automação individual.
4. País humano com `human_ai` e outros mods, acrescentados gradualmente.

Observe se a IA consegue:

- Selecionar focos.
- Pesquisar.
- Construir.
- Administrar produção.
- Importar recursos.
- Recrutar tropas.
- Atribuir comandantes.
- Organizar exércitos.
- Criar planos de batalha.
- Executar ofensivas.
- Administrar forças aéreas.
- Administrar marinha.
- Praticar diplomacia.
- Tomar decisões políticas.
- Responder a eventos.

Para cada ação, registre se ela:

- É executada automaticamente.
- É executada parcialmente.
- Exige intervenção do jogador.
- Não funciona.
- Não pôde ser testada.

**Não conclua que o comando resolve tudo apenas porque a IA começou a construir fábricas.**

Verifique também conflitos entre o `human_ai` e os módulos de automação.

Descubra se é possível ajustar a IA para não disputar controle com Iron Secretary e Automated Research.

Se o controle for global, não prometa uma delegação seletiva que não existe.

Documente tudo em `docs/HUMAN_AI_RESEARCH.md` e `docs/ENGINE_CAPABILITIES.md`.

---

# 6. ARQUITETURA DO SMART NATION DIRECTOR

Quero uma estrutura de módulos independentes.

## 6.1 Smart Nation Controller

É o coordenador central.

Responsabilidades:

- Habilitar e desabilitar automação.
- Detectar condições nacionais.
- Definir objetivos estratégicos.
- Priorizar módulos.
- Evitar decisões contraditórias.
- Aplicar cooldowns.
- Registrar decisões importantes.
- Coordenar mods externos.
- Gerar relatórios.

Modos:

**Autonomous**
O sistema executa tudo que for tecnicamente possível e solicita aprovação somente quando configurado.

**Supervised**
Executa ações administrativas e pede aprovação para decisões estratégicas.

**Advisor**
Apenas recomenda e explica.

**Disabled**
Não interfere na campanha.

A implementação desses modos deve respeitar as limitações reais da engine. Se uma função não permitir confirmação prévia, não anuncie que ela está sujeita à aprovação.

## 6.2 Smart Economic Director

Responsável por:

- Prioridades de industrialização.
- Fábricas civis.
- Fábricas militares.
- Estaleiros.
- Infraestrutura.
- Ferrovias.
- Suprimentos.
- Recursos estratégicos.
- Comércio.
- Ajustes de economia de guerra.
- Equilíbrio entre indústria civil e militar.

Integre primeiro o Iron Secretary.

Não duplique funcionalidades que ele já executa corretamente.

Não conceda fábricas ou recursos gratuitamente para simular construção.

## 6.3 Smart Research Director

Integre o Automated Research System.

Descubra suas configurações e prioridades.

O objetivo é pesquisar tecnologias de maneira legítima, usando os slots e tempos de pesquisa normais.

Não conceda tecnologias instantaneamente, a menos que o usuário tenha ativado explicitamente um modo de sandbox.

## 6.4 Smart Production Director

Responsável por:

- Identificar déficits de equipamentos.
- Priorizar armas, artilharia, veículos, aviões e navios.
- Equilibrar fábricas.
- Preparar equipamentos necessários para os planos militares.
- Evitar linhas excessivas de produção.
- Coordenar o Design Bureau.

Verifique até que ponto a IA nativa consegue executar essas ações no país humano.

## 6.5 Smart Military Director

Responsável por:

- Recrutamento.
- Modelos de divisões.
- Exércitos.
- Comandantes.
- Guarnições.
- Logística.
- Preparação militar.
- Coordenação terrestre, aérea e naval.

Aproveite mecanismos vanilla sempre que possível.

Não considere comando de exército implementado apenas porque é possível ajustar `ai_strategy`.

A ação precisa produzir efeito real sobre tropas do país humano.

## 6.6 Smart War Director

Este será um dos módulos mais importantes.

Quero que, idealmente, meu país consiga combater sem que eu precise movimentar unidades.

Investigue:

- Planos de batalha.
- Frentes.
- Linhas ofensivas.
- Defesa de regiões.
- Desembarques.
- Superioridade aérea.
- Apoio aéreo.
- Operações navais.
- Logística.
- Reação a invasões.
- Encerramento de guerras.
- Conferências de paz.

Não declare guerras totalmente automáticas até conseguir demonstrar o comportamento em uma campanha real.

Se a engine não permitir comandar certos aspectos, registre as lacunas e crie um modo de orientação que minimize a intervenção manual.

## 6.7 Smart Political Director

Quero um sistema que avalie o rumo político do país.

Ele deve considerar:

- Estabilidade.
- Apoio à guerra.
- Poder político.
- Situação militar.
- Capacidade industrial.
- Riscos de golpe.
- Apoio partidário.
- Diplomacia.
- Prioridades nacionais.
- Personagens e líderes disponíveis.
- Condições dos focos nacionais.
- Consequências políticas de cada escolha.

O governo poderá considerar democracia, comunismo, fascismo ou não alinhamento quando essas opções existirem no país e na versão/modpack.

**Não configure uma ideologia como permanentemente superior.**

Trate cada ideologia como uma estratégia possível dentro da simulação.

Analise oportunidades, riscos, estabilidade, custos, apoio político e consequências internacionais.

O sistema deverá preservar as condições e mecanismos reais do jogo para eleições, golpes, transições de governo e mudanças de líderes.

Não troque presidentes arbitrariamente apenas mudando uma variável ou usando um efeito que ignore todo o contexto político.

Quando for possível, implemente escolhas automáticas contextualizadas.

Quando não for possível, ofereça decisões e eventos explicativos.

## 6.8 Smart Focus Director

Quero que o sistema escolha focos nacionais de acordo com as necessidades do país.

Investigue:

- Pesos de IA existentes.
- Prioridades econômicas.
- Prioridades militares.
- Focos políticos.
- Focos diplomáticos.
- Focos exclusivos.
- Dependências.
- Condições de desbloqueio.
- Árvores alteradas pelo Road to 56.

Não dependa de IDs exclusivos da Alemanha.

O sistema deve funcionar, dentro das capacidades disponíveis, com vários países.

## 6.9 Smart Diplomacy Director

Responsável por:

- Relações internacionais.
- Alianças.
- Garantias.
- Acordos.
- Justificativas de guerra.
- Política externa.
- Avaliação de ameaças.
- Oportunidades estratégicas.
- Gestão de estados subordinados.
- Participação em facções.

Integre o General Staff somente nas funções realmente disponíveis.

As decisões devem considerar consequências e não apenas bônus imediatos.

---

# 7. SMART NATION DASHBOARD — INTERFACE SIMPLES

A interface é uma prioridade do projeto.

Eu considero a interface original do HOI4 muito confusa.

Quero uma experiência próxima à do Victoria 3, com indicadores nacionais claros.

Crie um painel em português brasileiro, com design limpo, organizado, acessível em 1920×1080 e sem poluição visual.

## 7.1 Informações desejadas

- Nome e bandeira do país.
- Líder atual.
- Ideologia e governo.
- Situação política.
- Estabilidade.
- Apoio à guerra.
- Indústria civil.
- Indústria militar.
- Estaleiros.
- Evolução industrial.
- Recursos disponíveis.
- Situação logística.
- Mão de obra.
- Divisões e equipamentos.
- Poder aéreo.
- Poder naval.
- Pesquisa.
- Guerras e ameaças.
- Prioridades do governo automático.
- Últimas decisões.
- Alertas e recomendações.

## 7.2 Ranking nacional

Quero acompanhar minha posição comparada a outros países.

Crie um sistema de classificação próprio, se os scripts fornecerem os dados necessários.

Sugestões:

- Ranking industrial.
- Ranking militar.
- Ranking de capacidade produtiva.
- Ranking de poder nacional composto.

O ranking deve informar sua fórmula e limitações.

Não invente um PIB ou dinheiro como se fosse um indicador nativo do HOI4.

Não anuncie métricas impossíveis de calcular.

## 7.3 Crescimento ao longo do tempo

Quero saber:

- Como estava meu país em 1936.
- Como está em 1938.
- Como está em 1940.
- Se estou melhorando ou piorando.
- Quais decisões contribuíram para as mudanças.

Investigue persistência de dados por variáveis, flags e histórico.

Use amostragem limitada e econômica.

Não crie loops pesados apenas para alimentar gráficos.

## 7.4 Relatórios inteligentes

Exemplo do comportamento desejado:

"O governo priorizou a construção de fábricas militares devido à ameaça de guerra. A capacidade produtiva aumentou, mas o país ainda enfrenta escassez de aço."

O relatório deve corresponder a dados observáveis.

Diferencie fatos medidos, inferências e previsões.

## 7.5 Integração com interface dos outros mods

Antes de criar janelas:

- Identifique todos os arquivos `.gui` alterados pelos mods.
- Descubra quais janelas foram substituídas.
- Verifique quais botões precisam continuar visíveis.
- Evite sobrescrever janelas de terceiros.
- Prefira painel independente ou integração mínima.
- Teste legibilidade em 1080p.
- Teste clique, navegação, tooltips e atualização de números.

Se precisar de um patch de compatibilidade, mantenha-o separado e documentado.

---

# 8. EVENTOS E APROVAÇÕES DO JOGADOR

Quero uma experiência de governante observador.

Crie eventos significativos para situações como:

- Mudança de governo.
- Aproximação com uma facção.
- Crise política.
- Guerra potencial.
- Reforma importante.
- Reorientação industrial.
- Mobilização extraordinária.
- Mudança de prioridade estratégica.

Evite transformar cada ação pequena em uma janela.

Uma boa experiência seria:

**Decisão do governo: reorientação industrial**

O diretor propõe priorizar fábricas militares devido a ameaças internacionais.

Opções:

- Aprovar.
- Rejeitar.
- Adiar.

As opções precisam ter efeitos reais e documentados.

Evite eventos repetidos, loops infinitos e notificações excessivas.

No modo autônomo, decisões ordinárias devem acontecer sem minha intervenção.

---

# 9. COMO INTEGRAR OS MODS SEM QUE ELES BRIGUEM

Crie uma matriz de responsabilidades.

Exemplo:

| Área | Responsável inicial |
|---|---|
| Construção | Iron Secretary |
| Comércio | Iron Secretary |
| Pesquisa | Automated Research System |
| Produção | IA nativa / Director, conforme testes |
| Design militar | Design Bureau / integração comprovada |
| Comando de aliados | General Staff |
| Política | Smart Political Director |
| Focos | Smart Focus Director |
| Guerra | IA nativa / Smart War Director, conforme viabilidade |
| Interface | Smart Nation Dashboard |

A tabela é uma hipótese de arquitetura, não prova de integração.

Você deverá confirmar cada linha.

Não faça o Smart Nation Director pressionar botões ou alterar estados que outro mod já esteja gerenciando.

Crie mecanismos de detecção e exclusão quando disponíveis.

Se não for possível detectar um mod de maneira confiável, documente a limitação e ofereça configuração explícita.

Nunca suponha que um mod possui uma API de integração apenas porque seus arquivos estão instalados.

---

# 10. SEM TRAPAÇAS

O objetivo é automatizar a administração legítima.

Não quero que o mod simplesmente deixe o país artificialmente poderoso.

Proibido como comportamento padrão:

- Criar fábricas instantaneamente sem custo.
- Dar recursos gratuitos.
- Gerar tropas gratuitamente.
- Ignorar tempo de pesquisa.
- Adicionar estabilidade artificialmente para compensar decisões ruins.
- Ignorar requisitos de focos.
- Ignorar custos políticos.
- Alterar resultados de guerra para favorecer o jogador.
- Fazer modificações ocultas para maquiar rankings.

Se algum mod de terceiros já oferecer recursos semelhantes, identifique-os e desative os módulos de trapaça quando possível.

Se o jogo não oferecer forma legítima de realizar determinada ação automaticamente, não substitua a ação por um bônus grátis.

---

# 11. ESTRUTURA DO REPOSITÓRIO

Use o repositório existente:

https://github.com/Lincoln16yyy/Smart-Nation-Director-HOI-IV-

Organize de maneira modular, adaptando esta estrutura às exigências reais do HOI4:

```text
Smart-Nation-Director-HOI-IV-/
├── README.md
├── AGENTS.md
├── CHANGELOG.md
├── LICENSE
├── .gitignore
├── Smart_Nation_Director.mod
├── Smart_Nation_Director/
│   ├── descriptor.mod
│   ├── common/
│   │   ├── scripted_effects/
│   │   ├── scripted_triggers/
│   │   ├── scripted_guis/
│   │   ├── on_actions/
│   │   ├── decisions/
│   │   ├── ai_strategy/
│   │   └── ai_strategy_plans/
│   ├── events/
│   ├── interface/
│   ├── gfx/
│   └── localisation/
│       ├── english/
│       └── braz_por/
├── compatibility/
├── scripts/
├── tests/
├── .github/
│   └── workflows/
└── docs/
    ├── AI_CONTEXT.md
    ├── ENGINE_CAPABILITIES.md
    ├── HUMAN_AI_RESEARCH.md
    ├── MOD_AUDIT.md
    ├── MOD_COMPATIBILITY.md
    ├── GAP_ANALYSIS.md
    ├── ARCHITECTURE.md
    ├── DEVELOPMENT_GUIDE.md
    ├── TEST_PLAN.md
    ├── RUNTIME_TESTS.md
    ├── PERFORMANCE.md
    ├── PHASE_LOG.md
    └── STATUS.md
```

Essa estrutura é inicial.

Não crie diretórios vazios apenas para seguir o desenho.

Confirme nomes e caminhos aceitos pela engine.

Use a convenção de localização exigida pelo HOI4 e encoding adequado, incluindo UTF-8 com BOM quando necessário.

Não publique arquivos proprietários copiados do jogo ou de mods de terceiros sem autorização.

Arquivos de compatibilidade precisam ser originais ou distribuíveis conforme suas licenças.

---

# 12. PLANO DE DESENVOLVIMENTO

## Fase 0 — Reconhecimento

- Confirmar jogo e versão.
- Identificar instalação Wine.
- Localizar mods e logs.
- Auditar configurações.
- Ler o repositório.
- Pesquisar documentação.
- Registrar capacidades da engine.

Entregável: auditoria verificável.

## Fase 1 — Prova do `human_ai`

- Testar o comando.
- Observar ações concretas.
- Investigar logs.
- Verificar efeitos sobre país humano.
- Testar interação com mods existentes.

Entregável: matriz de capacidades comprovadas.

## Fase 2 — Mod mínimo funcional

- Criar descriptor e arquivo `.mod`.
- Criar uma decisão de habilitação.
- Criar configuração persistente.
- Criar um efeito administrativo real.
- Confirmar execução com país humano.
- Verificar logs.
- Verificar save/load.

Entregável: primeira versão funcional.

## Fase 3 — Integração econômica

- Integrar Iron Secretary.
- Integrar pesquisa.
- Investigar produção industrial.
- Evitar sistemas duplicados.

Entregável: automação administrativa inicial.

## Fase 4 — Inteligência política

- Desenvolver sistema de prioridades.
- Investigar escolhas de focos.
- Implementar eventos políticos contextuais.
- Testar mudança de governo e ideologia quando realmente permitidas.

Entregável: decisões políticas observáveis.

## Fase 5 — Administração militar

- Investigar recrutamento.
- Investigar comando de exércitos.
- Investigar IA de guerra.
- Testar operações militares.
- Documentar lacunas impossíveis de resolver.

Entregável: máximo de autonomia militar comprovada.

## Fase 6 — Dashboard

- Criar painel em português.
- Mostrar indicadores reais.
- Apresentar tendências.
- Registrar decisões.
- Garantir legibilidade e navegação.

Entregável: interface simples e funcional.

## Fase 7 — Campanhas longas

- Brasil.
- Alemanha.
- França ou Reino Unido.
- União Soviética.
- Japão.
- Pelo menos um país pequeno.

Entregável: validação de compatibilidade entre países.

## Fase 8 — Qualidade e lançamento

- Correção de erros.
- Teste de desempenho.
- Documentação.
- Instalação simplificada.
- Atualização do README.
- Publicação no GitHub.

Não avance afirmando que uma fase foi concluída se seus critérios ainda não foram demonstrados.

---

# 13. TESTES OBRIGATÓRIOS

## 13.1 Testes estáticos

Verifique:

- Arquivos Paradox válidos.
- Chaves equilibradas.
- Escopos corretos.
- Triggers existentes.
- Efeitos válidos.
- IDs exclusivos.
- Localização correta.
- Referências a arquivos existentes.
- Compatibilidade de descriptors.
- Modificações não intencionais.

Use CWTools ou alternativa adequada.

## 13.2 Testes em jogo

Verifique:

- A campanha inicia.
- O mod é carregado.
- O botão ou decisão aparece.
- O modo automático ativa.
- O governo toma decisões.
- Os resultados são observáveis.
- Os custos são respeitados.
- Os mods não disputam controle.
- O jogo pode salvar.
- O jogo pode carregar.
- A automação continua funcionando após carregar.

Uma função não está pronta só porque não gerou erros.

## 13.3 Testes por módulo

Teste cada módulo sozinho antes de integrar.

Depois teste combinações progressivas.

Compare logs e comportamento.

## 13.4 Testes de duração

Execute campanhas de referência com checkpoints aproximados:

- 30 dias.
- 180 dias.
- 1 ano.
- 3 anos.
- 5 anos.
- 10 anos, quando viável.

Registre desempenho e resultados.

Para automação militar, observe pelo menos uma guerra real.

Para política, observe situações efetivas em que opções de governo estejam disponíveis.

Não invente screenshots, logs, resultados ou campanhas.

## 13.5 Métrica central de sucesso

Além de testar sistemas, meça uma coisa fundamental:

**Quantas ações manuais o jogador ainda precisa realizar por ano?**

Faça uma contagem por categoria:

- Economia.
- Construção.
- Pesquisa.
- Produção.
- Exército.
- Diplomacia.
- Política.
- Eventos.
- Interface.

A meta é reduzir o esforço manual ao mínimo possível, sem usar trapaças e sem esconder limitações.

---

# 14. TESTES DE DESEMPENHO

Compare:

1. HOI4 vanilla.
2. HOI4 com Road to 56.
3. HOI4 com os mods de automação aprovados.
4. HOI4 com Smart Nation Director.

Meça:

- Tempo de carregamento.
- Velocidade de passagem dos dias.
- Travamentos.
- Uso de recursos, quando possível.
- Volume de logs.
- Eventos repetidos.
- Impacto dos scripts.

Não faça loops diários pesados para recalcular estatísticas que podem ser atualizadas mensalmente.

Registre resultados no `docs/PERFORMANCE.md`.

---

# 15. REGRAS DE QUALIDADE

1. Pesquisar antes de implementar.
2. Conferir exemplos na instalação real.
3. Não inventar efeitos ou triggers.
4. Não prometer controle de ações não expostas pela engine.
5. Não mascarar falhas com recursos gratuitos.
6. Não sobrescrever arquivos originais de terceiros.
7. Não substituir milhares de arquivos vanilla desnecessariamente.
8. Não criar sistemas paralelos conflitantes.
9. Não depender de um único país.
10. Não afirmar testes que não executou.
11. Não declarar integração apenas por detectar a presença de um mod.
12. Não deixar logs de debug excessivos na versão final.
13. Não alterar saves pessoais.
14. Não incluir dados pessoais, tokens ou arquivos proprietários no repositório.
15. Não usar ferramentas de acesso externo ao processo, automação de mouse ou injeção de código como solução oculta. Se isso se mostrar necessário, documente separadamente a proposta, os riscos e as limitações antes de implementar.

O resultado deve ser confiável, não apenas impressionante na documentação.

---

# 16. FLUXO DE TRABALHO NO GITHUB

O repositório oficial do projeto é:

https://github.com/Lincoln16yyy/Smart-Nation-Director-HOI-IV-

Confirme acesso e examine o estado real do repositório.

Se estiver vazio, inicialize com README, AGENTS.md, estrutura mínima e documentação.

Configure `.gitignore` para impedir envio de:

- Saves pessoais.
- Logs locais.
- Arquivos de crash.
- Cache.
- Executáveis do jogo.
- Arquivos proprietários.
- Dados do Wine prefix.
- Credenciais.
- Configurações privadas.

Crie branches pequenas, por exemplo:

`feat/foundation-and-engine-audit`

`feat/human-ai-proof-of-concept`

`feat/economic-coordination`

`feat/political-director`

`feat/nation-dashboard`

Utilize commits claros e descritivos.

Sempre que concluir uma unidade funcional:

1. Execute a validação disponível.
2. Atualize a documentação.
3. Registre testes e limitações.
4. Faça commit.
5. Envie a branch para o GitHub.
6. Abra um pull request com descrição e evidências.

Não faça merge sem minha aprovação.

Não declare que um PR foi criado se o envio ao GitHub não tiver funcionado.

Se o acesso ao GitHub não estiver configurado, registre o bloqueio e preserve o trabalho local.

Configure CI para verificações estáticas, mas não apresente CI como substituto de teste em jogo real.

---

# 17. DOCUMENTAÇÃO PARA FUTUROS AGENTES

O projeto terá continuidade e poderá ser desenvolvido por outros agentes.

Crie `AGENTS.md` e `docs/AI_CONTEXT.md`.

Eles deverão explicar:

- Objetivo do projeto.
- Arquitetura atual.
- Versão do jogo.
- Mods suportados.
- Limitações comprovadas.
- Funcionalidades implementadas.
- Funcionalidades não implementadas.
- Testes realizados.
- Bugs conhecidos.
- Próxima tarefa recomendada.
- Como instalar e executar.
- Como revisar o progresso.
- Como evitar regressões.

Crie `docs/PHASE_LOG.md`, registrando cronologicamente mudanças e descobertas importantes.

Atualize `docs/STATUS.md` após cada fase.

Nenhum agente futuro deve precisar reconstruir toda a pesquisa do zero.

---

# 18. CRITÉRIOS DE ACEITAÇÃO

Considere o projeto completo somente quando houver evidências verificáveis de que:

- O mod carrega corretamente.
- A automação funciona no país humano.
- As funções existentes dos outros mods foram aproveitadas.
- Os conflitos foram eliminados ou claramente documentados.
- O governo toma decisões reais.
- Há evolução observável do país.
- A interface mostra dados corretos.
- Os controles de automação funcionam.
- Os eventos e relatórios têm efeitos coerentes.
- Saves podem ser carregados.
- Campanhas longas funcionam.
- A documentação descreve fielmente o produto.
- O código foi publicado no GitHub.

Caso a engine impeça algumas metas, mantenha a melhor automação possível e liste explicitamente as funcionalidades impossíveis ou dependentes de intervenção manual.

**O objetivo final é a máxima autonomia tecnicamente demonstrável, não uma promessa falsa de 100%.**

---

# 19. SUA PRIMEIRA AÇÃO AGORA

Você está autorizado a começar imediatamente.

Não fique apenas propondo ideias ou fazendo outro roadmap abstrato.

Execute nesta ordem:

1. Inspecione a instalação real do HOI4 e confirme a versão.
2. Localize os mods presentes, incluindo os ativos e os desativados.
3. Analise o conteúdo real desses mods.
4. Identifique conflitos e sobreposições.
5. Pesquise as capacidades da engine para o país humano.
6. Teste o `human_ai` em ambiente controlado, se o jogo puder ser executado.
7. Produza a primeira matriz de funcionalidades comprovadas.
8. Inicialize o repositório.
9. Crie uma prova de conceito mínima que possa ser carregada pelo jogo.
10. Execute os testes disponíveis.
11. Faça commit e push de uma branch.
12. Abra um PR inicial e me apresente o link.

Se não conseguir executar o jogo automaticamente, implemente o que puder, prepare os testes reproduzíveis e informe precisamente o que falta validar.

Não marque testes de runtime como concluídos quando apenas verificações estáticas foram executadas.

Ao final da primeira entrega, apresente:

- Diagnóstico do ambiente.
- Mods encontrados.
- Conflitos identificados.
- Capacidades confirmadas.
- Limitações da engine.
- Arquivos desenvolvidos.
- Testes executados e respectivos resultados.
- URL da branch e do PR.
- Próximas tarefas concretas.

**Prioridade absoluta: fazer o país do jogador agir sozinho, de verdade, aproveitando a IA existente e sem trapaças.**

O Smart Nation Dashboard será a ferramenta para eu acompanhar o desenvolvimento do país, mesmo sem compreender todos os menus complexos do Hearts of Iron IV.

Comece agora pela investigação, pela prova de conceito e pela primeira entrega versionada no GitHub.
