---
type: workflow
title: Workflow — Réplica
description: Sequência executável com portões para redigir uma réplica, compondo técnica (este bundle) com matéria (bundle temático).
tags: [replica, workflow]
timestamp: '2026-07-16'
status: vigente
autor: escritorio
skills: [legal-orchestrator, legal-writer, legal-consistency-validator, humanizer-forense, peca-pma-builder]
playbook: /replica/playbooks/playbook-replica.md
---

# Workflow — Réplica

## Etapa 0 — Prazo (na intimação da decisão que abre vista)

Anotar a data fatal (15 dias) em `cronologia.md` do caso (C1), contada da **ciência da decisão** que determina a manifestação sobre a contestação (arts. 350/351) — não da data da contestação. Se a intimação não trouxer decisão fundamentada e apenas abrir vista (praxe comum em muitos juízos/Juizados), tratar como determinação implícita e seguir o mesmo prazo.

## Etapa 1 — Mapa de alegações (portão de cabimento)

**Ler a contestação e os documentos que a acompanham, integralmente.** Preencher a [tabela de alegações e resposta](/replica/heuristicas/tabela-alegacoes-resposta.md): cada preliminar, fato novo e documento classificado em um dos quatro eixos (preliminar / fato novo / documento / mero mérito). **Portão:** se toda linha cair em "mero mérito", a réplica é dispensável — levar essa conclusão ao titular como parecer curto; sem determinação em contrário, não redigir peça alguma. Se houver ao menos uma linha nos outros três eixos, prosseguir.

## Etapa 2 — Composição com a matéria

Do bundle temático do caso: teses de mérito que sustentem a resposta a fatos novos ou a preliminares de mérito disfarçado (ex.: inépcia alegada para na verdade discutir o direito material), jurisprudência com vigência conferida. A técnica é deste bundle; a matéria de fundo vem do bundle temático. **Portão:** resposta a fato novo sem fundamento no bundle temático → sinalizar lacuna ao titular (nunca inventar).

## Etapa 3 — Redação

Estrutura do playbook (I. Síntese → II. Preliminares → III. Fato(s) novo(s) → IV. Documentos → V. Pedidos, capítulos II-IV só quando o eixo correspondente foi acionado), regras [AI-first](/heuristicas/estrutura-ai-first.md) (BLUF, títulos-tese, jurisprudência transcrita com fonte adjacente — em prosa, sem rótulos meta-textuais visíveis). Cada preliminar/fato novo/documento vira um capítulo, espelhando 1:1 a tabela da Etapa 1. Aplicar a regra de ouro do playbook: nenhuma inovação de pedido ou causa de pedir (CPC, art. 329, II). Especificar provas no capítulo de pedidos, calibrado para o que o juízo vai decidir no saneamento (art. 357).

## Etapa 4 — Validação (portões bloqueantes)

1. Checklist do playbook (8 itens) — TODOS "sim".
2. Tabela da Etapa 1 espelhada 1:1 na peça (alegação ↔ capítulo).
3. Conferência de citações normativas letra por letra contra a página do bundle ou a fonte oficial; remissões cruzadas reconferidas após qualquer renumeração.
4. skill `legal-consistency-validator` sobre a peça.
5. skill `humanizer-forense` sobre a prosa própria (`scripts/lint-ia.js` + correções) — sem tocar transcrições e citações.
6. **Banca (a pedido do titular ou caso de alto valor):** skill `banca-revisora` sobre a versão pós-lints, antes do protocolo — a lente do adversário é a mais útil aqui, porque ela testa se cada preliminar/fato novo/documento realmente recebeu resposta específica, ou se algum ficou "concordado por omissão".

## Etapa 5 — Entrega

`peca-pma-builder` (padrão tipográfico do escritório) + relatório de fontes + tabela de alegações anexada ao dossiê do caso (C1). Agendar em `cronologia.md`: aguardar a decisão de saneamento (art. 357) ou o julgamento conforme o estado do processo (art. 353 e ss.) — a especificação de provas da réplica é o que orienta essa decisão seguinte.
