# Testes na instalação real

- A tentativa em sandbox falhou na abertura do socket do wineserver.
- Uma execução autorizada via Wine em prefixo temporário inicializou o HOI4 com debug e apenas o piloto habilitado. `setup.log` registrou uma categoria, duas decisões e um evento do piloto. `game.log` registrou a execução do histórico até 1º de janeiro de 1936. Na coleta inicial, `error.log` estava vazio.
- A revisão da sessão de campanha e as medições de efeito estão em andamento. Registros de carga, histórico e ausência de erro inicial são evidência de inicialização. A execução de ações no país humano exige evidência separada.
