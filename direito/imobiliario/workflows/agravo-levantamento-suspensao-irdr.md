---
type: workflow
title: Workflow — agravo de instrumento para levantamento de suspensão por IRDR exaurido
description: Da decisão agravada ao .docx protocolável, com o portão de instrução documental obrigatória (acórdão + EDcl do REsp 2.035.848/TO).
tags: [agravo-de-instrumento, irdr, suspensao]
timestamp: '2026-07-21'
status: em_teste
autor: escritorio
skills: [legal-orchestrator, peca-pma-builder]
playbook: /playbooks/playbook-agravo-levantamento-suspensao-irdr.md
---

# Workflow — agravo de levantamento de suspensão por IRDR

## Etapa 1 — Coleta

Entrada mínima: texto integral da decisão agravada, data da suspensão original, dados do processo (para verificar se há hipótese de *distinguishing*). PORTÃO: sem o texto da decisão agravada, não é possível confirmar se o fundamento é exatamente "aguardar julgamento dos recursos especiais" — entrevistar antes de seguir.

## Etapa 2 — Verificação de distinguishing

Checar as 4 hipóteses de [distinguishing do IRDR](/teses/distinguishing-irdr-fora-do-objeto.md) antes de montar o argumento de exaurimento. PORTÃO: se houver distinguishing aplicável, priorizá-lo como fundamento principal (mais direto, independe de discutir o ciclo recursal).

## Etapa 3 — Instrução documental obrigatória

Anexar os dois documentos de `raw/`: [acórdão de não conhecimento](/jurisprudencia/resp-2035848-to-acordao-nao-conhecimento.md) e [EDcl rejeitados](/jurisprudencia/resp-2035848-to-edcl-rejeitados.md). PORTÃO: agravo sem essa instrução documental não demonstra o exaurimento da premissa fática — não protocolar sem os anexos.

## Etapa 4 — Redação e validação (skill: legal-orchestrator)

Pipeline completo (writer → tipografia → validator), incluindo o pedido de efeito ativo/suspensivo com demonstração de urgência concreta.

## Etapa 5 — Entrega (skill: peca-pma-builder)

Gerar .docx no padrão PMA. Saída: peça + lista de anexos + relatório de fontes.
