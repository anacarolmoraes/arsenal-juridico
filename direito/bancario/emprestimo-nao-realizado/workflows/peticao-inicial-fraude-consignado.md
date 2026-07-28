---
type: workflow
title: Workflow — petição inicial de fraude em consignado
description: Da entrevista de fatos ao .docx protocolável no padrão PMA, com portões de validação em cada etapa.
tags: [peticao-inicial, fraude, consignado, execucao]
timestamp: '2026-07-05'
status: vigente
autor: escritorio
skills: [pre-peticionamento, legal-orchestrator, legal-writer, tipografia-pma, legal-consistency-validator, peca-pma-builder]
playbook: /playbooks/playbook-peticao-inicial-fraude-consignado.md
---

# Workflow — Petição inicial de fraude em consignado

Execute as etapas na ordem. Cada PORTÃO é bloqueante: não avance sem satisfazê-lo.

## Etapa 1 — Coleta (skill: pre-peticionamento)

Entrada mínima: fatos do caso, documentos disponíveis, valor da causa pretendido, destino do valor creditado.
**PORTÃO:** se mais de um item da entrada mínima estiver ausente, entreviste o usuário antes de prosseguir (regra herdada do legal-orchestrator).

## Etapa 2 — Fundamentação (leitura obrigatória)

Ler, nesta ordem: o [playbook](/playbooks/playbook-peticao-inicial-fraude-consignado.md), **todas** as teses vigentes em [/teses/](/teses/index.md), as [heurísticas](/heuristicas/index.md) (checando as condições de "quando NÃO usar" contra os fatos do caso), o [índice de jurisprudência](/jurisprudencia/index.md), os [perfis](/perfis/index.md) aplicáveis e [/escritorio.md](/escritorio.md). Para cada fundamento central, **minerar o trecho literal** na seção "Trechos-chave" da página (ou no `raw/` paginado), anotando a localização (página / folha e-STJ).
**PORTÃO:** toda tese empregada na peça deve ter fundamento neste bundle; jurisprudência que não esteja no bundle entra apenas como citação indireta, jamais com número de processo ou ementa literal inventados.

## Etapa 3 — Redação e validação (skill: legal-orchestrator)

Executar o pipeline completo (legal-writer → tipografia-pma → legal-consistency-validator), passando o contexto do caso + as teses e fundamentos selecionados na Etapa 2.
**PORTÃO:** consistência numérica (valor da causa × somatório de danos × datas de descontos) confirmada pelo validator; checagem da modulação do EAREsp 600.663/RS contra as datas dos descontos.

## Etapa 4 — Entrega (skill: peca-pma-builder)

Gerar o `.docx` no padrão PMA (Montserrat 12pt, banner e logo — nunca formatação improvisada).

**Entregáveis obrigatórios junto com a peça:**

1. **Relatório de fontes** (`relatorio-fontes.md`): uma linha por citação da peça, com — fonte; URL oficial (`resource` do frontmatter); localização no `raw/` (página / folha e-STJ) quando literal; trecho citado; e **nível de confiança**: `literal-do-raw` (verificável na página indicada) | `derivado-do-bundle` (enunciado curado) | `fora-do-bundle-conferir` (sinalizado para conferência humana). É o roteiro da checagem manual do titular e o insumo do ritual de encerramento.
2. **Checklist pré-protocolo** (`checklist-pre-protocolo.md`): placeholders a preencher, subscritoras confirmadas contra [/escritorio.md](/escritorio.md), prioridade de tramitação verificada, datas/valores conferidos, itens `fora-do-bundle-conferir` listados.
