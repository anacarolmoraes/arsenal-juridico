---
type: workflow
title: Workflow — Embargos de Declaração
description: Sequência executável com portões para redigir EDcl, nos papéis corretivo e prequestionador, compondo técnica (este bundle) com matéria (bundle temático).
tags: [embargos-declaracao, workflow]
timestamp: '2026-07-09'
status: vigente
autor: escritorio
skills: [legal-orchestrator, legal-writer, legal-consistency-validator, humanizer-forense, peca-pma-builder]
playbook: /embargos-declaracao/playbooks/playbook-embargos-declaracao.md
---

# Workflow — Embargos de Declaração

## Etapa 0 — Prazo e papel (mesmo dia da intimação)

Anotar a data fatal em `cronologia.md` do caso (C1): **5 dias úteis no cível; 2 dias no penal (CPP 619)** — é o prazo mais curto do sistema. Declarar o papel: **corretivo** (vício real a sanar) ou **prequestionador** (preparar REsp/RE). **Portão:** se a decisão for inadmissão de REsp/RE, EDcl é erro grosseiro sem interrupção — parar e ir ao [mapa de rotas](/recurso-especial/playbooks/mapa-rotas-pos-inadmissao.md).

## Etapa 1 — Mapa de vícios (portão de leitura)

**Ler integralmente** a decisão embargada E as peças que suscitaram as questões (apelação/contrarrazões/inicial) — não trabalhar de resumo. Preencher a [tabela de vícios e prequestionamento](/embargos-declaracao/heuristicas/tabela-vicios-prequestionamento.md): questão → onde suscitada (folha) → o que a decisão disse/silenciou → vício do 1.022 → dispositivo a prequestionar. Conferir o **voto vencido** (941, §3º — pode já prequestionar). **Portão:** linha sem transcrição da suscitação anterior = inovação, não omissão — remover ou repensar; tabela vazia = não há EDcl a opor.

## Etapa 2 — Composição com a matéria (papel prequestionador)

A tese que o futuro REsp/RE levará define **quais** dispositivos precisam de decisão expressa: vêm do parecer de viabilidade do fluxo do REsp (Etapa 1 de [/recurso-especial/workflows/recurso-especial.md](/recurso-especial/workflows/recurso-especial.md)) e do bundle temático. Matéria constitucional destina-se ao RE: prequestionar na origem, nunca pedir isso ao STJ. **Portão:** dispositivo sem tese que o exija é menu legislativo — cortar.

## Etapa 3 — Redação

Estrutura do playbook em prosa, sem rótulos meta-textuais visíveis (um capítulo por vício, sempre na sequência vício/inciso → suscitação transcrita → silêncio transcrito → dispositivo → conclusão — [AI-first](/heuristicas/estrutura-ai-first.md), rev. 2026-07-16), síntese de abertura, Súmula 98 declarada, pedidos individualizados. Redigir **para acolher** (o 1.025 só socorre se o vício for reconhecido). Regras do escritório: transcrição literal, granularidade máxima, relatório de fontes.

## Etapa 4 — Validação (portões bloqueantes)

1. Checklist do playbook (8 itens) — TODOS "sim".
2. Tabela da Etapa 1 espelhada 1:1 nos capítulos.
3. Conferência de citações normativas letra por letra contra página do bundle ou fonte oficial; remissões cruzadas reconferidas após qualquer renumeração.
4. skill `legal-consistency-validator` sobre a peça.
5. skill `humanizer-forense` sobre a prosa própria (`scripts/lint-ia.js` + correções) — sem tocar transcrições, rótulos e citações.
6. **Banca (EDcl prequestionador de recurso a tribunal superior, ou a pedido do titular):** skill `banca-revisora` sobre a versão pós-lints, antes do protocolo — os 4 elementos do prequestionador eficaz são exatamente o que o assessor vai procurar depois.

## Etapa 5 — Entrega

skill `peca-pma-builder` + relatório de fontes + tabela de vícios anexada ao dossiê (C1). Registrar em `cronologia.md` a interrupção do prazo e **agendar o gatilho**: publicado o julgamento dos EDcl, reabre-se integralmente o prazo do recurso principal (REsp: 15 dias).
