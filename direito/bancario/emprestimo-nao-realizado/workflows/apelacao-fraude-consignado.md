---
type: workflow
title: Workflow — apelação contra improcedência em fraude de consignado
description: Da análise da sentença ao .docx da apelação no padrão PMA, com preliminar de cerceamento e mérito subsidiário.
tags: [apelacao, fraude, consignado, execucao]
timestamp: '2026-07-05'
status: vigente
autor: escritorio
skills: [legal-orchestrator, legal-writer, tipografia-pma, legal-consistency-validator, peca-pma-builder]
playbook: /playbooks/playbook-apelacao-fraude-consignado.md
---

# Workflow — Apelação (improcedência em fraude de consignado)

## Etapa 1 — Análise dos autos

Entrada mínima: sentença completa, inicial, contestação, réplica; saber se houve perícia grafotécnica.
**PORTÃO:** sem a sentença completa, não redija — a apelação ataca os fundamentos dela, um a um.

## Etapa 2 — Fundamentação (leitura obrigatória)

Ler o [playbook de apelação](/playbooks/playbook-apelacao-fraude-consignado.md) e a [tese central](/teses/onus-prova-assinatura-impugnada.md). Mapear: (a) onde a assinatura foi impugnada nos autos; (b) o que o banco deixou de produzir.
**PORTÃO:** confirmar que a impugnação da assinatura consta da inicial ou da réplica — sem ela a preliminar de cerceamento não se sustenta e a estratégia da peça muda (só mérito).

## Etapa 3 — Redação e validação (skill: legal-orchestrator)

Pipeline completo, com a estrutura do playbook: preliminar → méritos → pedidos em cascata (anulação; subsidiário de causa madura).
**PORTÃO 1 — Matriz de cobertura:** todo fundamento autônomo da sentença tem seção que o impugna (ver portão obrigatório do playbook); nenhuma linha vazia.
**PORTÃO 2:** pedidos em cascata presentes e coerentes; consistência numérica confirmada pelo validator.

## Etapa 4 — Entrega (skill: peca-pma-builder)

Gerar o `.docx` no padrão PMA.

**Entregáveis obrigatórios junto com a peça:** relatório de fontes (mesma especificação do workflow da inicial, incluindo a matriz de cobertura como anexo) + checklist pré-protocolo.
