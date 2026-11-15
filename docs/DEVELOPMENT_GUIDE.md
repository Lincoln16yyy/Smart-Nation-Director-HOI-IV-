# Desenvolvimento

Use o executável Windows e os arquivos vanilla da instalação 1.19.3.0 como referência. Em um perfil Wine temporário, configure uma pasta Documents interna ao prefixo. Confirme que ela aponta para a pasta temporária antes de abrir o jogo. O launcher da instalação usa `-gdpr-compliant -debug_mode`. Use somente campanhas de teste fora de Ironman.

Para conferir o ciclo mensal, busque `on_monthly` em `common/on_actions/_documentation.md` e `12_wuw_on_actions.txt`. Para um exemplo de validação de escopo em decisões, procure `capital_scope` e `is_controlled_by` nos scripts vanilla. Compare novos mecanismos com exemplos existentes antes de usar `eval_effect`.

Use `setup.log` para confirmar carga, `error.log` para comparar erros com a mesma instalação vanilla, `game.log` para histórico e `executed_commands.log` para rastros de comandos, quando disponíveis. Registre o efeito produzido no país humano separadamente da carga do arquivo.

A CI inclui quatro verificações específicas do piloto. Elas cobrem estrutura, descritores, referências de evento, localização e uso explícito da fila regular. Validação semântica continua dependente da engine. [CWTools](https://github.com/cwtools/cwtools-vscode) e [regras HOI4](https://github.com/cwtools/cwtools-hoi4-config) são candidatos para ampliar as verificações. As ferramentas do Marketplace e Hearts of Modding não foram configuradas.
