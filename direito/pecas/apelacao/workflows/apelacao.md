---
type: workflow
title: Workflow — Apelação
description: Sequência executável com portões para redigir uma apelação, compondo técnica (este bundle) com matéria (bundle temático) e o legal-orchestrator.
tags: [apelacao, workflow]
timestamp: '2026-07-09'
status: vigente
autor: escritorio
skills: [legal-orchestrator, legal-writer, legal-consistency-validator, humanizer-forense, peca-pma-builder]
playbook: /apelacao/playbooks/playbook-apelacao.md
---

# Workflow — Apelação

## Etapa 0 — Prazo, preparo e eficácia (mesmo dia da intimação)

Anotar a data fatal (15 dias úteis) em `prazos:` da `ANALISE.md` do caso (C1; `cronologia.md` foi abolida em 01/10/2026). Conferir o espelho da publicação: nome da advogada que atua e OAB, parte sem abreviatura, respeito a pedido de intimação exclusiva; defeito aí não gera petição de devolução de prazo, e sim prazo contado pelo pior cenário e preliminar de nulidade na própria apelação ([272, § 8º](/apelacao/heuristicas/intimacao-nula-arguir-no-proprio-ato.md)). Providenciar **preparo** (comprovação no ato — 1.007) e prova de feriado local se houver (1.003, §6º). Conferir o [CPC 1.012, §1º](/apelacao/jurisprudencia/cpc-arts-1012-1014.md): sentença com eficácia imediata → decidir **hoje** entre pedido de efeito suspensivo *ope judicis* (nosso cliente sucumbente) ou cumprimento provisório (nosso cliente vencedor). Antes de redigir o apelo, avaliar EDcl (2/5 dias!): vício na sentença ou prequestionamento — [fluxo próprio](/embargos-declaracao/index.md); os EDcl interrompem o prazo da apelação.

## Etapa 1 — Inventário (portão de leitura e anti-preclusão)

**Ler integralmente** a sentença e varrer **todas as decisões do processo** desde a inicial. Preencher as duas partes da [tabela de capítulos e interlocutórias](/apelacao/heuristicas/tabela-capitulos-interlocutorias.md), inclusive, na Parte A, as colunas de decisão de cada capítulo desfavorável (prejuízo, chance, ganho, risco, rota) e a linha dos honorários fixados contra o cliente, com a rota "pedir ou calar" da [heurística de sucumbência](/sucumbencia/heuristicas/honorarios-na-apelacao-do-vencido-pedir-ou-calar.md). **Portão:** a tabela completa vai ao titular como parecer de estratégia recursal (o que atacar, o que deixar transitar, apelo próprio × aguardar e aderir × contrarrazões, posição sobre causa madura, honorários); sem aprovação, não redigir. A decisão aprovada vai para a seção 9 da `ANALISE.md`. Se a rota for "aguardar e aderir", o prazo a vigiar passa a ser o das contrarrazões (adesivo no mesmo prazo, 997, § 2º, I).

## Etapa 2 — Composição com a matéria

Do bundle temático do caso: teses de mérito, jurisprudência com vigência conferida, perfil do órgão julgador (`perfis/` quando existir). Se houve recurso anterior no processo, o relator da apelação está prevento (930, parágrafo único): levantar as decisões dele no tema (DJEN pelo `radar-jurisprudencia`, consulta do TJTO, `casos_decididos/`) e devolver o achado à coluna "chance" da tabela da Etapa 1 antes do parecer à titular ([heurística](/apelacao/heuristicas/relator-prevento-pelo-primeiro-recurso.md)). A técnica é deste bundle; o mérito é matéria. **Portão:** tese de mérito sem fundamento no bundle temático → sinalizar lacuna ao titular (nunca inventar).

## Etapa 3 — Redação

Estrutura canônica do playbook (síntese → cabimento → preliminares → mérito → pedidos); cada preliminar de nulidade com os cinco elos do [teste do processo alternativo](/apelacao/heuristicas/nulidade-teste-do-processo-alternativo.md) (sem o prejuízo reconstruído, a linha sai da peça e volta à tabela como "não atacar"); regras [AI-first](/heuristicas/estrutura-ai-first.md) (títulos-conclusão, BLUF, jurisprudência transcrita com fonte adjacente — em prosa, sem rótulos meta-textuais visíveis), impugnação específica dos fundamentos da sentença com transcrição literal só do trecho atacado; peça [enxuta](/apelacao/heuristicas/apelacao-enxuta.md) (cabimento em um parágrafo, sem capítulo de fatos, apelante/apelado, dispositivo federal no título). Geração do .docx pelo `md2docx` (`peca-pma-builder`). Pedidos por capítulo + posição sobre causa madura + prequestionamento dos dispositivos do futuro REsp/RE.

## Etapa 4 — Validação (portões bloqueantes)

1. Checklist do playbook (10 itens) — TODOS "sim".
2. Tabela da Etapa 1 espelhada 1:1 na peça (capítulo/interlocutória ↔ seção).
3. Conferência documental: preparo + comprovante correspondentes; feriado local; procuração.
4. Citações normativas letra por letra; remissões cruzadas reconferidas após renumeração.
5. skill `legal-consistency-validator` sobre a peça.
6. skill `humanizer-forense` sobre a prosa própria (`scripts/lint-ia.js` + correções) — sem tocar transcrições, rótulos e citações.
7. **Banca (a pedido do titular ou em caso de alto valor):** skill `banca-revisora` sobre a versão pós-lints, antes do protocolo.

## Etapa 5 — Entrega

.docx no padrão do escritório + relatório de fontes + tabela do inventário anexada ao dossiê (C1). Agendar em `prazos:` da `ANALISE.md`: prazo de contrarrazões da parte contrária (e eventual adesiva → nossas contrarrazões em 15 dias).
