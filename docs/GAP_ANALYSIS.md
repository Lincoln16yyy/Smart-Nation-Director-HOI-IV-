# Lacunas e responsáveis candidatos

| Função | Candidato | O que precisa ser comprovado |
|---|---|---|
| Construção | Iron Secretary, piloto isolado | Fila, consumo de capacidade civil, cancelamento, save/load e proprietário exclusivo das ordens |
| Comércio e logística | Iron Secretary, IA nativa | Importações reais e custos; controle por módulo |
| Pesquisa | IA nativa, Automated Research System | Ocupação e progresso normais de slots; separar rotina de concessão |
| Produção e design | IA nativa, Design Bureau | Alteração observável em linhas e modelos com custo normal |
| Recrutamento, comandantes e operações | IA nativa | Execução no país humano e efeitos de desligar delegação |
| Focos e decisões políticas | IA nativa | Respeito a pré-requisitos, custos e mudanças políticas permitidas |
| Diplomacia | IA nativa; General Staff para aliados | Separar ações do país humano das instruções aos aliados |
| Conselho administrativo | Council of Ministers | Compatibilidade 1.19.3, custos e colisão de localização |
| Painel e ranking | Director | Triggers e valores verificáveis, interface em 1080p, atualização econômica |

Nenhum adaptador de terceiros foi implementado. A escolha do responsável por uma função depende da execução demonstrada em jogo.

O padrão terrestre de `add_equipment_production` está em
`history/units/BRA_1936.txt`. O piloto usa os modelos 0 a 3, com as mesmas
tecnologias vanilla e Road to 56. A documentação local 1.19.3 descreve
consultas de estoque e capacidade, mas não encontrei nela um trigger de
consulta a uma linha de produção por equipamento. O piloto continua
limitado a uma solicitação por país. É necessário testar se uma linha
existente interfere na alocação e, antes de automatizar novas solicitações,
confirmar um método de evitar duplicatas.
