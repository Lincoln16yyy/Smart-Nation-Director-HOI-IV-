# Smart Nation Director

- A versão-alvo inicial é HOI4 1.19.3.0. Compare capacidades com a instalação e mantenha as evidências em docs.
- Use arquivos e IDs com prefixo `snd` e preserve os arquivos do jogo e dos mods de terceiros.
- Use exclusivamente campanhas descartáveis para debug. Preserve os saves pessoais e o perfil ativo.
- Valide com `python3 -m unittest discover -s tests -v` e siga docs/TEST_PLAN.md para verificar a engine e o país humano.
- Registre resultados reais e limitações em docs/RUNTIME_TESTS.md e atualize docs/STATUS.md, docs/PHASE_LOG.md e docs/AI_CONTEXT.md.
- Preserve custos, requisitos e progresso normal de construção e pesquisa. Registre efeitos de terceiros antes de criar adaptadores.
- Faça PRs pequenos. A aprovação do mantenedor é necessária antes do merge.
