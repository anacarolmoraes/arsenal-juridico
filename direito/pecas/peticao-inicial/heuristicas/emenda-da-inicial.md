---
type: heuristica
title: Emenda da inicial — o que fazer quando o juízo manda emendar e como não voltar a precisar
description: O despacho de emenda (art. 321) é a segunda chance e a última — não cumprida, a inicial é indeferida (330, IV) e o remédio é apelação com juízo de retratação em 5 dias (331). A resposta é curta, cumpre exatamente o que foi pedido, e cada causa de emenda volta para o checklist de saída do escritório.
tags: [peticao-inicial, emenda, indeferimento, retratacao, checklist]
timestamp: '2026-09-04'
status: vigente
autor: escritorio
peca: peticao-inicial
fundamentos:
  - /peticao-inicial/jurisprudencia/cpc-arts-319-321-330-331-334.md
---

# Emenda da inicial

## O que o art. 321 dá e o que tira

Dá **15 dias** e o dever do juízo de indicar **com precisão** o que corrigir. Tira a possibilidade de discutir: emenda não cumprida é indeferimento (321, parágrafo único, e 330, IV), e o indeferimento se ataca por apelação, com o juízo podendo retratar-se em 5 dias (331).

## A resposta

1. **Ler o despacho como uma lista.** Cada item indicado vira um parágrafo da petição de emenda, na mesma ordem, com o mesmo nome que o juízo usou. Nada além do que foi pedido: emenda não é réplica nem aditamento.
2. **Despacho genérico** ("regularize a inicial", "junte os documentos indispensáveis" sem dizer quais) não cumpre o art. 321. A resposta cumpre o que dá para inferir e pede, no mesmo ato, que o juízo indique com precisão o que falta, transcrevendo o dispositivo. Não deixar o prazo correr esperando esclarecimento.
3. **Emenda que muda a peça** (valor da causa, pedido, réu): substituir a inicial inteira em vez de remendar, com o `.md` recompilado pelo pipeline. Peça remendada em três petições é a que a contestação explora.
4. **Valor da causa** é a causa de emenda mais frequente e a mais fácil de evitar: a regra por inciso do art. 292 está em `perfil/definicoes.md` §1 do workspace; conferir antes de protocolar, não depois.

## Se indeferiu

Apelação em 15 dias, dirigida ao juízo de primeiro grau, com pedido expresso de retratação (331). A apelação argumenta o cumprimento da emenda ou a imprecisão do despacho; o réu ainda não foi citado, e é citado para contrarrazoar (331, § 1º). Ver [fluxo da apelação](/apelacao/index.md).

## Retroalimentação obrigatória

Cada despacho de emenda recebido pelo escritório entra no `log.md` deste bundle com a causa em uma linha (valor da causa, documento faltante, qualificação, pedido indeterminado, gratuidade). Quando uma causa se repete, ela vira item do checklist de saída em [`/peticao-inicial/index.md`](/peticao-inicial/index.md) com a contagem anotada. É assim que o checklist deixa de ser opinião.

## Erros que já custaram

- Responder emenda com argumentação de mérito. O juízo pediu um documento; a peça trouxe três páginas de direito e o documento não veio.
- Deixar vencer o prazo enquanto se espera o cliente mandar o comprovante de residência. Pedir dilação dentro do prazo, com o motivo.
- Tratar o indeferimento como definitivo. A retratação em 5 dias existe e costuma funcionar quando a emenda foi cumprida e o juízo não viu.
