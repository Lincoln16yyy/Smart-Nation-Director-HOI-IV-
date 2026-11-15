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
