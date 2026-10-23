---
type: heuristica
title: Inquirir o preposto do banco — mapa de quatro colunas e perguntas que não se respondem com sim ou não
description: Antes da audiência, mapa em quatro colunas (o que o cliente afirma / o que o banco afirma / o que os documentos mostram / o que falta esclarecer); as perguntas nascem da quarta coluna. Abertura obrigatória "conhece os termos do processo?". Cada pergunta pede um registro, um horário ou um procedimento: "não sei" vira desconhecimento registrado, "o banco tem" vira "por que não juntou" (art. 400).
tags: [audiencia-de-instrucao, preposto, golpe-pix, contratacao-digital, exibicao-de-documentos, art-400]
timestamp: '2026-10-20'
status: em_teste
autor: escritorio
peca: audiencia
momento: [audiencia, alegacoes-finais]
casos_origem: []
fundamentos:
  - /jurisprudencia/resp-2222059-sp-falsa-central-perfil-consumo.md
---

# Inquirir o preposto do banco

Complementa a técnica geral de [inquirir pela matriz de perguntas](../../../audiencias/heuristicas/inquirir-testemunha-pela-matriz-de-perguntas.md) (bundle `audiencias`). Aqui, só o que é do banco.

## Antes: o mapa

| O cliente afirma | O banco afirma | Os documentos mostram | Falta esclarecer |
|---|---|---|---|
| nunca usou aquele aparelho | "dispositivo cadastrado" | log não juntado | qual registro identifica o dispositivo? |
| avisou às 11h03 | "MED acionado" | sem protocolo do MED | que horas? que documento? |

As perguntas saem da quarta coluna. Pergunta sem coluna não vai.

## A primeira pergunta

"O senhor conhece os termos do processo? Sabe por que está aqui?" Se sim, tem de responder ao resto; se não, o desconhecimento fica na ata e pesa na valoração (o preposto representa a parte, art. 75, VIII, e seu desconhecimento é da parte).

## As perguntas (escolher pelo mapa)

| Pergunta | O que registra |
|---|---|
| Como o banco confirmou que foi o autor quem fez a operação? Qual mecanismo, nesta operação? | abre IP, dispositivo, geolocalização, *liveness*, logs |
| A operação destoava do histórico da conta? Houve alerta? Que validação adicional foi feita? | perfil ([REsp 2.222.059](/jurisprudencia/resp-2222059-sp-falsa-central-perfil-consumo.md)) |
| A chave recebedora foi consultada no DICT antes? Tinha marcação? | [DICT](marcacao-de-fraude-no-dict-antes-do-pix.md) |
| Que horas o banco foi avisado? Que horas abriu o MED? Que documento comprova? | [MED](med-e-conduta-do-banco-apos-o-aviso.md) |
| Além das telas do sistema, há documento de terceiro que prove a liberação do crédito? | tela sistêmica é unilateral |
| Depois da contratação, houve ligação gravada, SMS ou e-mail confirmando com o cliente? | ausência de confirmação |
| Se o banco tem esse registro, por que não está nos autos? | art. 400 |

Nenhuma se responde com sim/não. Não buscar o espetáculo: a oitiva serve à causa, não ao corte de vídeo; registrar a resposta com precisão para as alegações finais.

## Quando NÃO usar

Preposto que é o gerente que atendeu o cliente: aí a inquirição é de fato, pela matriz geral, e não por esta lista.

## Origem

Triagem de perfil público (@jessicaabreuadv, posts DayVrVHRp_n, DdrF4SMoEih, DasnSbhINLH, DecGmNPIA6o, jul–out/2026).
