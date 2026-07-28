---
type: router
title: Roteador de atividades
description: Mapeia cada atividade executável deste bundle para seu workflow, skills e conhecimento obrigatório.
tags: [roteador, execucao]
timestamp: '2026-07-05'
status: vigente
autor: escritorio
---

# Roteador de atividades

Agente: localize a atividade pelos gatilhos, depois siga o workflow indicado **na ordem**, lendo antes o conhecimento obrigatório. Se a entrada mínima estiver incompleta, entreviste o usuário antes de executar.

## Peticionar fraude em empréstimo consignado

- **Gatilhos:** "petição inicial de fraude", "empréstimo que o cliente não fez", "consignado não contratado", "desconto indevido de empréstimo no benefício"
- **Workflow:** /workflows/peticao-inicial-fraude-consignado.md
- **Skills (ordem):** pre-peticionamento → legal-orchestrator (legal-writer, tipografia-pma, legal-consistency-validator) → peca-pma-builder
- **Conhecimento obrigatório antes de redigir:**
  /playbooks/playbook-peticao-inicial-fraude-consignado.md,
  /teses/index.md (todas as teses vigentes), /jurisprudencia/index.md,
  /heuristicas/index.md
- **Entrada mínima:** fatos do caso, documentos disponíveis, valor da causa pretendido, destino do valor creditado (usado? devolvido? depositado em juízo?)

## Apelar de improcedência em fraude de consignado

- **Gatilhos:** "apelação de improcedência", "recorrer da sentença", "julgou improcedente sem perícia"
- **Workflow:** /workflows/apelacao-fraude-consignado.md
- **Skills (ordem):** legal-orchestrator (legal-writer, tipografia-pma, legal-consistency-validator) → peca-pma-builder
- **Conhecimento obrigatório antes de redigir:**
  /playbooks/playbook-apelacao-fraude-consignado.md,
  /teses/onus-prova-assinatura-impugnada.md (preliminar de cerceamento),
  /teses/index.md, /jurisprudencia/index.md
- **Entrada mínima:** sentença completa, peças anteriores do processo (inicial, contestação, réplica), houve ou não perícia grafotécnica
