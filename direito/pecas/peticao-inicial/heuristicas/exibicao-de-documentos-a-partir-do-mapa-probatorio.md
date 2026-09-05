---
type: heuristica
title: Exibição de documentos a partir do mapa probatório — todo fato "a produzir" cuja prova está com o réu vira pedido do art. 396
description: O mapa probatório da ANALISE.md classifica cada fato como comprovado, frágil ou a produzir. Fato "a produzir" cuja prova está em poder do réu (contrato, log, gravação, ficha cadastral, extrato interno) recebe pedido de exibição na própria inicial, com os três incisos do art. 397 preenchidos; a recusa gera presunção de veracidade (400).
tags: [peticao-inicial, prova, exibicao-de-documentos, mapa-probatorio]
timestamp: '2026-09-04'
status: vigente
autor: escritorio
peca: peticao-inicial
fundamentos:
  - /peticao-inicial/jurisprudencia/cpc-arts-396-400.md
  - /peticao-inicial/jurisprudencia/cpc-arts-319-321-330-331-334.md
---

# Exibição de documentos a partir do mapa probatório

O protesto genérico por provas cumpre o inciso VI do art. 319 no papel e nada na prática. O que muda o processo é o pedido de exibição bem feito na inicial, porque ele transfere ao réu o ônus de mostrar o que só ele tem e converte o silêncio em presunção (art. 400).

## A regra

Para cada linha do mapa probatório da `ANALISE.md` marcada **a produzir** com a anotação "prova em poder do réu", a inicial traz um pedido de exibição com os três elementos do art. 397:

| Inciso | O que escrever | Exemplo (golpe bancário) |
|---|---|---|
| I — descrição ou categoria | O documento ou a categoria, "tão completa quanto possível"; a Lei 14.195/2021 admite categoria, então não é preciso saber o nome interno do relatório | "os registros de autenticação, dispositivo e geolocalização das operações de DD/MM/AAAA" |
| II — finalidade | O fato do mapa que o documento prova | "demonstrar que as operações partiram de dispositivo e localidade estranhos ao perfil do autor" |
| III — por que existe e está com o réu | Dever regulatório de guarda, alusão do réu em resposta administrativa, natureza da operação | "registros de guarda obrigatória pela regulação do Banco Central, mencionados pela ré na resposta ao protocolo n. X" |

Documento **comum às partes** (contrato, extrato, ficha cadastral) entra sempre: a recusa é inadmissível pelo art. 399, III, e não exige o inciso III do 397 em detalhe.

## Onde entra no esqueleto

No capítulo de provas, antes dos pedidos, um parágrafo por documento ou categoria; e nos pedidos, uma alínea própria ("a exibição, pela ré, de ..., no prazo do art. 398, sob as consequências do art. 400"). O mapa probatório e a alínea têm de bater um a um; o `legal-consistency-validator` confere.

## O que a exibição rende além da prova

- **Presunção de veracidade** (400, I e II): fato que a exibição provaria passa a ser tido por verdadeiro se o réu não exibe nem se justifica em 5 dias, ou se a recusa é ilegítima. Em fraude bancária, é o fato central (a operação foi feita de outro dispositivo) que se prova pelo silêncio do banco.
- **Medidas coercitivas** (400, parágrafo único): multa e outras medidas quando a presunção não basta.
- **Réplica pronta**: a contestação que junta o documento parcialmente ou alude a ele sem juntar cai no art. 399, II.

## Erros que já custaram

- Pedir "a exibição de todos os documentos relativos ao contrato". Sem categoria descrita nem finalidade, não é pedido do 397; é indeferido sem análise.
- Deixar a exibição para a fase de instrução. O ônus só se transfere quando o pedido está feito; na inicial ele já condiciona a contestação.
- Fato marcado "a produzir" no mapa sem meio nomeado. O mapa existe para que cada linha vire testemunha, perícia, ofício ou exibição; linha sem meio é fato que a peça não pode afirmar.
