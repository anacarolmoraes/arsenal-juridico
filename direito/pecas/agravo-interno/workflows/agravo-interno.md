---
type: workflow
title: Workflow — Agravo Interno
description: Sequência executável com portões de validação para redigir um agravo interno, compondo técnica (este bundle) com matéria (bundle temático).
tags: [agravo-interno, workflow]
timestamp: '2026-07-08'
status: vigente
autor: escritorio
skills: [legal-orchestrator, legal-writer, legal-consistency-validator, humanizer-forense, peca-pma-builder]
playbook: /agravo-interno/playbooks/playbook-agravo-interno.md
---

# Workflow — Agravo Interno

## Etapa 0 — Portão zero e prazo (mesmo dia da intimação)

Confirmar que a decisão é **monocrática** (contra acórdão o AgInt é erro grosseiro sem interrupção de prazo — parar e identificar o recurso correto). Classificar a matéria: **cível = 15 dias úteis; penal no STJ = 5 dias corridos (RISTJ 258)**. Anotar a data fatal em `cronologia.md` do caso (C1).

## Etapa 1 — Papel do agravo

Classificar pelo playbook: (1) esgotamento de instância, (2) distinguishing contra inadmissão por precedente qualificado (CPC 1.030, §2º), (3) ataque à monocrática no STJ. **Portão:** papel 2 desprovido não comporta Reclamação nem novo REsp (Rcl 36.476/SP) — avaliar com o titular se a distinção é forte antes de gastar a via; papel 3 exige demonstrar não dominância ou distinção frente à Súmula 568.

## Etapa 2 — Composição com a matéria

Papel 2 e, às vezes, o 3 dependem do bundle temático: precedentes que sustentam a **distinção** frente à tese aplicada. A técnica é deste bundle; a distinção é matéria. **Portão:** distinguishing sem precedente ou fato distintivo concreto → parecer de viabilidade ao titular; sem aprovação, não redigir.

## Etapa 3 — Redação

Estrutura do playbook: endereçamento ao relator → tempestividade → papel declarado → síntese da decisão agravada → impugnação especificada (um capítulo por fundamento, transcrição literal + enfrentamento **novo**) → pedido (retratação; subsidiariamente colegiado; afastamento de multa quando aplicável). Regras do escritório: transcrição literal das fontes oficiais, granularidade máxima, **relatório de fontes** como entregável.

## Etapa 4 — Validação (portões bloqueantes)

1. Checklist do playbook (7 itens) — TODOS "sim".
2. Mapa fundamento ↔ capítulo 1:1 para tudo que se decidiu impugnar; capítulos autônomos deixados de fora listados com o "por quê" no dossiê.
3. Risco de multa avaliado por escrito (papel 1 → Tema 434 invocado).
4. skill `legal-consistency-validator` sobre a peça.
5. skill `humanizer-forense` sobre a prosa própria (`scripts/lint-ia.js` + correções) — sem tocar transcrições, rótulos e citações.
6. **Banca (se dirigido a tribunal superior ou a pedido do titular):** skill `banca-revisora` sobre a versão pós-lints, antes do protocolo.

## Etapa 5 — Entrega

skill `peca-pma-builder` (padrão tipográfico do escritório) + relatório de fontes anexado ao dossiê do caso (C1).
