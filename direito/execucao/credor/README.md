# Bundle de Competência — Execução pelo Credor

Este bundle carrega o conhecimento para **transformar crédito reconhecido em dinheiro recebido**: qualificar o título, montar o requerimento sem errar o cálculo, procurar patrimônio em sequência quando as consultas voltam negativas, alcançar o bem que está registrado em nome de terceiro e impedir que a execução morra por inércia.

## Prompt de instalação

```
Aqui está um bundle de competência: direito/execucao/credor.
Leia o README, configure-o e me diga o que você consegue executar com ele.
```

## Setup para o agente

1. Ler o [index.md](index.md), inclusive o aviso de maturidade, e o [atividades.md](atividades.md) para despachar o pedido.
2. Rodar a verificação estrutural a partir da raiz do acervo: `python lint-bundle.py direito/execucao/credor`.
3. **Ler o [catálogo do raw](raw/index.md) antes de recorrer à fonte** — ele traz o inventário dos erros de citação do material original. Os arquivos `curso-execucao-*` são obra comercial e podem não existir na sua máquina.

## Como executar

Entre pelo [atividades.md](atividades.md). Duas perguntas organizam quase todo caso: **em que fase está** e **já se sabe onde está o patrimônio?**

**A pergunta que o bundle existe para você não esquecer:** há algum requerimento pendente nos autos? Execução sem pedido em curso vai ao arquivo, e do arquivo corre a prescrição intercorrente. No Juizado a consequência é pior — extinção imediata.

**Nunca cite o que não está conferido.** Semente v0.1.0: **todas as páginas estão `em_teste`**, e nenhuma citação foi conferida contra fonte oficial. Conferir e depositar em `raw/`, ou declarar `cita_em_teste: sim` no frontmatter da peça. O `lint-citacoes` bloqueia o caminho descuidado.

**Três armadilhas que este bundle existe para evitar:** requerer o cumprimento de sentença **depois de um ano** do trânsito e intimar pelo Diário, quando a lei exige carta com AR ao devedor; deixar de pedir os honorários de 10% do art. 523, §1º porque a fonte afirma que "ainda não há honorários"; e montar demonstrativo de crédito sem critério de juros, já que o material não trata do art. 406 do Código Civil, cuja redação mudou em 2024.

**Antes de peticionar, leia o outro lado.** O bundle irmão [defesa do executado](../defesa-executado/index.md) diz exatamente o que virá contra você — em especial as impenhorabilidades, que este material não cobre.

## Contrato de uso

Consumidores não modificam o bundle. Produtores seguem o schema do acervo: fonte oficial em `raw/` antes de promover página a `vigente`.

O bundle **não contém dados de cliente**. A varredura da ingestão não encontrou CPF, nome de parte real nem número de processo de terceiro no material — os exemplos são fictícios e os processos citados são de julgados públicos.

## Versão

`bundle_version: 0.1.0` — semente de 2026-08-01. Histórico e pendências no [log.md](log.md).
