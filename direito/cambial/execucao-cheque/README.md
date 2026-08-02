# Bundle de Competência — Execução de Cheque

Este bundle carrega o conhecimento necessário para **cobrar judicialmente um cheque devolvido**: conferir se o papel é mesmo título executivo, calcular a janela em que a execução ainda cabe, definir os encargos com base legal correta e montar a petição inicial de execução. Um agente que o leia consegue executar o caso inteiro, da imagem da cártula ao `.docx` protocolável, e consegue também dizer **quando não executar** e qual via resta.

## Prompt de instalação

```
Aqui está um bundle de competência: direito/cambial/execucao-cheque.
Leia o README, configure-o e me diga o que você consegue executar com ele.
```

## Setup para o agente

1. Ler o [index.md](index.md) para conhecer o tema, e o [atividades.md](atividades.md) para despachar o pedido.
2. Rodar a verificação estrutural a partir da raiz do acervo: `python lint-bundle.py direito/cambial/execucao-cheque`. Esperado: 0 erros, 0 avisos.
3. Confirmar que as fontes estão depositadas em `raw/`: texto integral da Lei nº 7.357/1985 e a Carta-Circular BCB nº 1.256/1985.

## Como executar

Entre sempre pelo [atividades.md](atividades.md), que mapeia quatro atividades: executar cheque devolvido, avaliar se ainda cabe execução, definir juros e correção, e decidir sobre reapresentação.

Navegue por revelação progressiva: índice, depois a página, e só então `raw/` se precisar do texto integral. Cite as fontes pelo campo `resource` do frontmatter, nunca pela memória.

**O portão inaugural não é opcional.** Toda execução de cheque começa pela [conferência do preenchimento da cártula](heuristicas/conferir-preenchimento-do-cheque-antes-de-executar.md), feita sobre a imagem do documento, com resultado registrado por escrito na pasta do caso antes de qualquer redação. A conferência é feita na imagem porque cheque manuscrito derrota conversores de PDF: texto extraído por OCR não serve para ler valor, data ou carimbo.

**Nunca cite o que não está aqui.** O bundle tem um único acórdão ingerido, o [REsp 1.556.834/SP, Tema 942/STJ](jurisprudencia/resp-1556834-sp-termo-inicial-juros-e-correcao.md), repetitivo sobre os termos iniciais de juros e correção. Súmula 531/STJ e Tema 564/STJ são pendências declaradas no [log.md](log.md); até que haja fonte em `raw/`, a fundamentação se apoia no que está depositado, e o que faltar entra como citação indireta explícita ou não entra.

**Duas armadilhas que este bundle existe para evitar:** pedir juros de 1% ao mês sem convenção escrita, quando a taxa legal do art. 406 do Código Civil é outra desde a Lei nº 14.905/2024; e reapresentar cheque que já não comporta reapresentação, hipótese em que a devolução se dá por remessa nula (motivo 49) a qualquer tempo. Os códigos do carimbo se leem pela [tabela oficial do Banco Central](jurisprudencia/motivos-de-devolucao-de-cheque-bcb.md), não pela Carta-Circular nº 1.256/1985, que enumera os motivos por nome.

## Contrato de uso

Consumidores não modificam o bundle. Produtores seguem o schema do acervo: fonte oficial em `raw/` antes da página derivada, `status` declarado em toda página, e superação de página apenas com confirmação da titular.

O bundle **não contém dados de cliente**. Casos concretos vivem na camada C1, fora do acervo, e referenciam este bundle, nunca o contrário.

## Versão

`bundle_version: 0.1.0` — semente de 28/07/2026. Histórico e pendências no [log.md](log.md).
