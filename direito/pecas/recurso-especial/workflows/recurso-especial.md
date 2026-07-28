---
type: workflow
title: Workflow — Recurso Especial
description: Sequência executável com portões de validação para redigir um REsp, compondo técnica (este bundle) com matéria (bundle temático).
tags: [recurso-especial, workflow]
timestamp: '2026-07-06'
status: vigente
autor: escritorio
skills: [legal-orchestrator, legal-writer, legal-consistency-validator, humanizer-forense, peca-pma-builder]
playbook: /recurso-especial/playbooks/playbook-recurso-especial.md
---

# Workflow — Recurso Especial

## Etapa 0 — Composição com a matéria

Identifique o bundle temático do caso no roteador global. Dele vêm: teses de mérito, precedentes, perfil do tribunal. Deste bundle vem a técnica. **Portão:** sem bundle de matéria identificado, pare e pergunte.

## Etapa 1 — Triagem de cabimento

Percorra os 8 portões do playbook sobre o acórdão recorrido. Produto: **parecer de viabilidade** (1 página): alínea(s), dispositivos violados, estado do prequestionamento (explícito/implícito/ficto-possível), óbices sumulares com risco e mitigação, necessidade de RE simultâneo (Súmula 126), tema repetitivo incidente. **Portão:** parecer vai ao titular; sem aprovação, não redigir.

## Etapa 2 — Prequestionamento (se necessário)

Ponto omisso → EDcl na origem citando a Súmula 98/STJ, indicando o inciso do 1.022 e o dispositivo cuja análise se requer. Persistindo omissão → registrar a rota ficta para a peça (1.022 + pedido de aplicação do 1.025).

## Etapa 3 — Redação

Siga a estrutura do playbook (interposição → **resumo 343-A** → tempestividade/preparo → cabimento → fatos pela moldura do acórdão → violações começando pelo dispositivo → pedido). Regras de citação e verificabilidade do escritório: fundamento central com transcrição literal da fonte oficial; legislação na granularidade máxima; **relatório de fontes** (URL oficial + localização + confiança) como entregável.

## Etapa 4 — Validação (portões bloqueantes)

1. Checklist anti-284 (14 itens do playbook) — TODOS "sim".
2. Tabela de fundamentos × abordado (anti-283) preenchida e completa.
3. Conferência documental: GRU+comprovante correspondentes; feriado local documentado; procuração; custas locais do TJ se exigidas.
4. skill `legal-consistency-validator` sobre a peça.
5. skill `humanizer-forense` sobre a prosa própria (`scripts/lint-ia.js` + correções) — sem tocar transcrições, rótulos e citações.
6. **Banca (REsp sempre é peça de tribunal superior):** skill `banca-revisora` sobre a versão pós-lints, ANTES do protocolo — atenção redobrada aqui: defeito de REsp não se conserta no AREsp (preclusão consumativa); achados CONFIRMADOS bloqueiam o protocolo.

## Etapa 5 — Entrega

skill `peca-pma-builder` (padrão tipográfico do escritório) + relatório de fontes + a tabela anti-283 anexada ao dossiê do caso (C1).
