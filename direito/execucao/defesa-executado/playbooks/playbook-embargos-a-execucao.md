---
type: playbook
title: Playbook — embargos à execução (arts. 914-920)
description: Como construir os embargos do executado contra execução de título extrajudicial — prazo e suas pegadinhas, requisitos da inicial, valor da causa, efeito suspensivo e matérias de defesa.
tags: [embargos-a-execucao, titulo-extrajudicial, efeito-suspensivo, art-914]
timestamp: '2026-08-01'
status: em_teste
autor: escritorio
peca: embargos-a-execucao
teses:
  - /teses/reserva-ate-40sm-impenhoravel-em-qualquer-aplicacao.md
  - /teses/bem-de-familia-ordem-publica-alegavel-ate-arrematacao.md
skills: [pre-peticionamento, peca-pma-builder, humanizer-forense]
---

# Playbook — embargos à execução

Ação autônoma de conhecimento (não incidente), distribuída por dependência ao juízo da execução (art. 914, §1º; competência funcional absoluta — art. 61). Independe de penhora, depósito ou caução (art. 914). Cabe **qualquer matéria de defesa** (art. 917): a via de cognição ampla do executado.

**Fronteira — execução fiscal.** A dispensa de garantia é regra do CPC. Na LEF, "Não são admissíveis embargos do executado antes de garantida a execução" (art. 16, § 1º, [depósito](/raw/lei-6830-1980-execucao-fiscal.md)), e penhora ínfima pode ser tratada como ausência de garantia, não como garantia parcial: foi o que o TRF3 decidiu no caso do [AREsp 2.711.567/SP](/jurisprudencia/aresp-2711567-sp-garantia-infima-embargos-execucao-fiscal.md), que o STJ manteve só por negar omissão, sem exame de mérito. Intimado o reforço da penhora, responder no prazo.

## Prazo — onde se perde o caso

- **15 dias úteis** da juntada do comprovante de citação (art. 915), suspensos de 20/12 a 20/01 (art. 220).
- **Individual por executado** (juntada do respectivo AR) — **não** se aplica a regra da contestação (art. 231, §1º) nem a dobra por procuradores distintos (art. 915, §3º — natureza de ação).
- **Exceção dos cônjuges/companheiros:** prazo comum contado da juntada do **último** comprovante (art. 915, §1º).
- Comparecimento espontâneo antes da citação dispara o prazo (art. 239, §1º).
- **Trade-off do art. 916:** no mesmo prazo cabe a moratória legal (30% de entrada + 6 parcelas). Embargar **faz perder** o direito ao parcelamento (art. 916, §6º) — decisão estratégica com o cliente antes de redigir.

## Petição inicial (art. 319)

- **Partes:** embargante pode ser o devedor, o responsável patrimonial (art. 779, II-VI) e o cônjuge intimado da penhora de imóvel (art. 842); defesa comum a todos os credores → litisconsórcio passivo necessário dos exequentes.
- **Valor da causa** = proveito econômico: totalidade do crédito, se ataca tudo; a **diferença** entre cobrado e incontroverso, no excesso de execução; o valor do bem, se a matéria é a penhora.
- **Pedido:** declaratório (inexistência da dívida) ou constitutivo negativo (desfazimento de ato executivo). **Nunca condenatório** — não há reconvenção/pedido contraposto em embargos; dano do executado é ação própria.
- **Prova documental completa na inicial** (art. 434): título, demonstrativo, auto de penhora se houver, documentos do fato extintivo. Cognição é ampla, mas quem não instrui perde o timing.
- **Excesso de execução:** declarar o valor correto + memória de cálculo, sob pena de rejeição liminar se for o único fundamento (art. 917, §§3º-4º).

## Efeito suspensivo (art. 919)

Não é automático. Requerimento expresso + requisitos de tutela provisória + **execução garantida** (penhora/depósito/caução). Concedido a um executado, não aproveita aos demais se o fundamento for pessoal (§4º); o exequente ainda pode prosseguir prestando caução (art. 525, §10, por analogia).

## Matérias típicas do tema (cruzar com o bundle)

Impenhorabilidade (arts. 833 e Lei 8.009/90 — [teses](/teses/index.md)), nulidade do título (Súmulas 233/258 STJ), vícios de citação, excesso, prescrição. Impenhorabilidade do 833, X **deve** vir nos embargos se não foi arguida antes ([heurística](/heuristicas/arguir-impenhorabilidade-na-primeira-manifestacao.md)).

## Portões

Protocolo de leitura do AGENTS.md (definições canônicas em `perfil/definicoes.md` — valor da causa, gratuidade, assinatura); `md2docx` com os três lints; páginas `em_teste` citadas exigem conferência oficial ou `cita_em_teste: sim`.
