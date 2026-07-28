---
type: workflow
title: Workflow — petição inicial de rescisão de compromisso de compra e venda de imóvel
description: Da entrevista de fatos ao .docx protocolável no padrão PMA, com portões de validação.
tags: [peticao-inicial, rescisao-contratual, loteamento]
timestamp: '2026-07-21'
status: em_teste
autor: escritorio
skills: [pre-peticionamento, legal-orchestrator, peca-pma-builder]
playbook: /playbooks/playbook-peticao-inicial-rescisao-imovel.md
---

# Workflow — petição inicial de rescisão de imóvel

## Etapa 1 — Coleta (skill: pre-peticionamento)

Entrada mínima: data do contrato original, valor e percentual pago, natureza do empreendimento (lote × apartamento), motivo do desinteresse na manutenção do contrato. PORTÃO: se faltar mais de um item, entrevistar antes de seguir.

## Etapa 2 — Determinação do regime aplicável

Verificar a data do contrato contra o marco de 28/12/2018 ([tese de irretroatividade](/teses/irretroatividade-lei-distrato-contratos-anteriores-2018.md)) e a natureza do empreendimento (loteamento × incorporação). PORTÃO: sem essa determinação, não prosseguir — ela define qual bloco de teses/jurisprudência é aplicável.

## Etapa 3 — Fundamentação (leitura obrigatória)

Ler o playbook, as teses vigentes do regime aplicável e o índice de jurisprudência. PORTÃO: toda tese empregada deve ter fundamento no bundle — jurisprudência fora do bundle só por citação indireta, sinalizada como tal.

## Etapa 4 — Redação e validação (skill: legal-orchestrator)

Pipeline completo (writer → tipografia → validator). PORTÃO: consistência numérica (valor da causa, percentual de retenção calculado, valores a restituir) verificada pelo validator.

## Etapa 5 — Entrega (skill: peca-pma-builder)

Gerar .docx no padrão PMA. Saída: peça + lista das teses e fontes empregadas (insumo para o ritual de encerramento, quando houver desfecho — schema 7.2).
