---
type: heuristica
title: Empréstimo não reconhecido seguido de Pix imediato é um fato só, não dois
description: Quando o golpista contrata empréstimo na conta da vítima e esvazia o crédito por Pix em minutos, a inicial narra uma única sequência (contratação → liberação → Pix → esvaziamento) e pergunta que mecanismo de segurança reagiu a ela. Separar os fatos deixa o banco defender cada um isoladamente ("o empréstimo foi autenticado", "o Pix foi autorizado").
tags: [golpe-pix, emprestimo-fraudulento, falso-advogado, cronologia, perfil-de-consumo, peticao-inicial]
timestamp: '2026-10-20'
status: em_teste
autor: escritorio
peca: peticao-inicial
momento: [inicial]
casos_origem: []
fundamentos:
  - /jurisprudencia/apciv-1002595-tjsp-falso-advogado-emprestimo-dobro.md
  - /jurisprudencia/apciv-1003655-tjsp-falso-advogado-consignado.md
---

# Empréstimo seguido de Pix é um fato só

**Regra:** uma cronologia, não dois capítulos. Horário da contratação, horário da liberação, horário de cada Pix, destinatários, dispositivo, autenticação, alertas gerados. A pergunta da peça: *que mecanismo de segurança foi acionado diante dessa sequência?*

## Por que favorece a vítima

Crédito que entra e sai em minutos para destinatário novo é a assinatura da fraude eletrônica e, por si, operação fora do perfil. O TJSP já trata o mútuo contratado no golpe como inexigível e devolve em dobro as parcelas descontadas ([ApCiv 1002595](/jurisprudencia/apciv-1002595-tjsp-falso-advogado-emprestimo-dobro.md)); a culpa da vítima, quando há, não exclui a do banco que liberou crédito e Pix na mesma janela ([ApCiv 1003655](/jurisprudencia/apciv-1003655-tjsp-falso-advogado-consignado.md)). O erro do banco a explorar: analisar cada operação isoladamente e tratar a autenticação como resposta para tudo.

Consequência patrimonial: a vítima não teve proveito do crédito, logo não devolve ([compensação só com proveito](../../emprestimo-nao-realizado/heuristicas/compensacao-so-com-proveito-economico.md)); os pedidos são inexigibilidade do mútuo, restituição das parcelas e do Pix, baixa no SCR.

## Quando NÃO usar

Empréstimo tomado dias antes pelo próprio cliente, sob orientação do golpista: aí a contratação é dele e a tese fica no Pix e na indução (engenharia social), não na sequência.

## Origem

Triagem de perfil público (@jessicaabreuadv, post DdSKNtsoBIF, 14/09/2026), que cita ementa sem número tratando a sequência como fortuito interno; a capturar.
