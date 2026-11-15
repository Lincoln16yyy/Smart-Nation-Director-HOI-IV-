# Compatibilidade

| Par | Resultado da comparação local | Decisão inicial |
|---|---|---|
| Road to 56 e More Politics | 6.474 arquivos idênticos e 115 diferentes no mesmo caminho. As diferenças incluem configurações de equipamento da IA. | Somente RT56 no perfil principal |
| More Politics e Modifier Icons | 598 idênticos e 4 diferentes, incluindo entradas de localização em inglês, alemão e polonês. | More Politics desativado |
| More Politics e Coloured Buttons | 42 idênticos e 5 diferentes em imagens de interface. | Ambos desativados |
| Road to 56 e Minimalistic GUI | Cinco caminhos diferentes, incluindo imagens de relatórios de evento. | Minimalistic GUI desativado |
| Road to 56 e Modifier Icons | Só a miniatura no mesmo caminho. Uma varredura de chaves encontrou 55 entradas de localização em inglês declaradas pelos dois mods, incluindo `CAN_state_manpower_tt` e `DEN_Low_Low`. | Modifier Icons ativo no perfil pessoal |
| Council of Ministers e General Staff | Dois caminhos diferentes, incluindo `common/scripted_localisation/game_assistant_hoi4_scripted_loc.txt`. As definições têm IDs diferentes e podem sumir se o arquivo de um mod ganhar prioridade. | Teste isolado antes de combinar |
| Iron Secretary e o piloto | Ambos podem emitir ordens de construção. | Testar separadamente |

A auditoria compara arquivos e confirma algumas referências e pontos de entrada. Uma busca de IDs no formato namespace.número em `events/*.txt` encontrou 10.472 IDs distintos entre os seis ativos e o Council, sem IDs repetidos entre esses mods. Essa busca é textual e não substitui o parser da engine. A comparação completa de IDs de eventos, ideias, decisões, variáveis, janelas e chaves de localização entre todos os mods continua pendente. Os caminhos sem colisão tampouco comprovam que decisões e automações podem coexistir. O piloto tem namespace `snd`, interface por decisões e nenhum `replace_path`.

A auditoria reproduzível do Director em 15/11/2026 não encontrou colisões
nas 346 definições cobertas contra os 11 mods locais. Consulte o
[escopo e as limitações](MOD_AUDIT.md#auditoria-dos-símbolos-do-director--15112026)
e o [resumo JSON](SYMBOL_AUDIT.json). Isso não encerra a auditoria exaustiva
entre terceiros nem valida a disputa de controle em jogo.
