# Arquitetura do piloto

A categoria de decisões do mod controla duas flags persistentes em escopo de país. A flag `snd_pilot_enabled` indica autorização revogável. `snd_pilot_dispatched` registra a única tentativa de envio por país. O ciclo mensal avalia o controlador humano, a autorização, a titularidade e o controle da capital e o nível de infraestrutura. O efeito atua em escopo de estado e emite um evento em escopo de país. A ocorrência do evento registra a tentativa. A fila mostra se o jogo aceitou a ordem.

O limite de uma tentativa protege esta primeira experiência contra repetição acumulada. Cancelar antes do ciclo remove a autorização. Depois do envio, o jogador usa os controles vanilla da fila.

Atribua um único responsável a cada área de automação antes de adicionar integrações. Os modos Disabled, Advisor, Supervised e Autonomous e o painel são objetivos das próximas fases. Use o teste de IA nativa para determinar quais operações podem ser delegadas, observadas ou aprovadas pelo jogador.
