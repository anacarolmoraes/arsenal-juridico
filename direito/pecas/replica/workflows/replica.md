---
type: workflow
title: Workflow — Réplica
description: Sequência executável com portões para redigir uma réplica, compondo técnica (este bundle) com matéria (bundle temático e seu repertório de defesas típicas) — do mapa da contestação em cinco eixos, incontrovérsia, pedidos não combatidos, confissões e documentos invocados sem prova até a entrega compilada, o prazo do art. 357, § 1º e o caso decidido.
tags: [replica, workflow]
timestamp: '2026-09-05'
status: vigente
autor: escritorio
skills: [legal-orchestrator, legal-writer, legal-consistency-validator, humanizer-forense, peca-pma-builder]
playbook: /replica/playbooks/playbook-replica.md
---

# Workflow — Réplica

## Etapa 0 — Prazos (na intimação da decisão que abre vista)

Anotar a data fatal (15 dias) em `cronologia.md` do caso (C1), contada da **ciência da decisão** que determina a manifestação sobre a contestação (arts. 350 e 351), não da data da contestação. Se a intimação apenas abre vista sem decisão fundamentada (praxe comum), tratar como determinação implícita e seguir o mesmo prazo. **No mesmo ato, ler o fim da contestação:** se há reconvenção, anotar o prazo da contestação à reconvenção (15 dias da intimação, art. 343, § 1º); se há arguição de falsidade de documento do autor, os 15 dias do art. 430; se o réu agravou da tutela, o prazo da contraminuta corre no tribunal. Todos vão para a `cronologia.md` ao lado do da réplica, e a decisão de peça conjunta ou separada é da titular.

## Etapa 1 — Mapa da contestação (portão de cabimento)

**Ler a inicial, a contestação e todos os anexos dela, integralmente** (PDF sem `.md` irmão passa pelo `pdfmd` antes). Preencher a [tabela de alegações e resposta](/replica/heuristicas/tabela-alegacoes-resposta.md), Partes 0 a 4, como seção 6 da `ANALISE.md` do caso:

- **Parte 0:** roteiro de entrevista do autor gerado dos fatos novos e documentos da contestação; sai antes da reunião com o cliente e volta preenchido.
- **Parte 1:** cada alegação da contestação em um dos cinco eixos (preliminar, fato novo, documento, tese jurídica, negativa pura), com a **prova do réu e o estado dela** (comprovado, frágil, sem prova, invocado e não juntado). O estado decide a resposta antes do mérito.
- **Parte 2-A:** cada fato da inicial contra o que a contestação fez com ele (impugnado, negativa geral, admitido, silenciado); os silenciados e os de negativa geral são incontroversos (art. 341). Documentos do autor sem impugnação entram em bloco.
- **Parte 2-B:** cada pedido da inicial contra o que a contestação fez com ele (combatido, combatido só por consequência, não combatido); o não combatido vira requerimento de julgamento parcial (art. 356, I).
- **Parte 3:** o que a contestação e os anexos dela confessam, provam contra o réu, contradizem ou **invocam sem juntar** (arts. 389 a 395, 408 e 396 a 400), com a cisão do art. 395 anotada quando o réu acrescentou fato novo.
- **Parte 4:** posturas acessórias do réu (reconvenção, pedido contraposto, impugnação à gratuidade, tutela, julgamento antecipado, denunciação, falsidade), cada uma com prazo e decisão da titular.

**Portão:** se toda linha da Parte 1 cair em "negativa pura" e as Partes 2 a 4 estiverem vazias, a réplica é dispensável; levar a conclusão à titular como parecer curto e não redigir sem determinação em contrário. Uma linha nos eixos 1 a 4, uma incontrovérsia que valha fixar, um pedido não combatido ou uma confissão colhida bastam para prosseguir.

## Etapa 2 — Composição com a matéria

**Primeiro o repertório.** Abrir o [repertório de defesas típicas](/replica/heuristicas/repertorio-de-defesas-tipicas.md) do bundle temático e conferir cada linha dos eixos 2 e 4 da Parte 1 contra ele: linha "coberta" já traz a página do acervo; linha "lacuna" vai para a estrutura como lacuna; tese que não está no repertório se responde pelo bundle e, ao fim do caso, a titular a acrescenta. Depois o bundle: teses e jurisprudência com vigência conferida para responder aos fatos novos e às **teses jurídicas da defesa** (eixo 4), que é onde a réplica mais depende do acervo; para preliminar de mérito disfarçado (inépcia alegada para discutir o direito material), a resposta também é de matéria. Para impugnação à gratuidade, o bundle [gratuidade](/gratuidade/index.md). A técnica é deste bundle; a matéria de fundo vem do temático. **Portão:** tese da defesa ou fato novo sem fundamento no bundle temático → lacuna declarada à titular na estrutura, nunca preenchida de memória (regra dura 3).

## Etapa 3 — Arquitetura e redação

Estrutura do playbook (I. Síntese → II. Preliminares → III. Incontrovérsia e confissões → IV. Fato(s) novo(s) → V. Tese(s) da defesa → VI. Documentos → VII. Pedidos e provas, capítulos II a VI só quando a Parte correspondente da tabela os aciona), gravada e aprovada no `<PECA>.estrutura.md` antes de qualquer prosa, com o **espelho da contestação**: cada linha das Partes 1 a 3 aponta o capítulo que a absorve; cada pedido não combatido aponta o requerimento de julgamento parcial; cada documento invocado e não juntado aponta o pedido de exibição; cada linha da Parte 4 aponta um capítulo ou uma peça própria. Regras [AI-first](/heuristicas/estrutura-ai-first.md) (BLUF, títulos-tese, transcrição com fonte adjacente, prosa sem rótulos). Regra de ouro: nenhum fato constitutivo ou pedido novo (art. 329, II); argumento de direito novo, julgamento parcial e exibição são permitidos. Incontrovérsia e confissão se escrevem pela justaposição (trecho da inicial, trecho da contestação ou do documento dela, norma), sem adjetivo. Fato novo se responde pelo estado da prova antes do mérito. Provas especificadas no último capítulo, fato a fato, calibradas para o saneamento (art. 357).

## Etapa 4 — Validação (portões bloqueantes)

1. Checklist do playbook (13 itens), todos "sim".
2. Tabela da Etapa 1 espelhada 1:1 na peça (alegação, incontrovérsia, pedido não combatido, confissão e documento invocado ↔ capítulo; postura acessória ↔ capítulo ou peça com prazo anotado).
3. Conferência letra por letra das citações normativas contra a página do bundle e das transcrições da contestação contra o `.md` dela na pasta do caso (o `lint-citacoes` cobra literalidade de bloco `>` com autos identificados); remissões cruzadas reconferidas após renumeração.
4. Skill `legal-consistency-validator` sobre a peça (bloco "Em réplica").
5. Skill `humanizer-forense` sobre a prosa própria (`scripts/lint-ia.js` + correções), sem tocar transcrições.
6. **Banca (a pedido da titular ou caso de alto valor):** skill `banca-revisora` na versão pós-lints. A lente do adversário testa se cada preliminar, fato novo e tese recebeu resposta específica; a lente do juiz testa se a lista de incontroversos é mesmo de fatos silenciados e não de fatos que a defesa impugnou de outro modo, e se o pedido dado como não combatido não foi combatido por consequência.

## Etapa 5 — Entrega e relógios armados

`md2docx` do `peca-pma-builder` (portões e padrão tipográfico do escritório) + relatório de fontes + tabela de alegações anexada ao dossiê do caso (C1). Na `cronologia.md`, três anotações: (a) aguardar decisão de saneamento (art. 357) ou julgamento conforme o estado (arts. 353 a 356); (b) **quando o saneamento sair, prazo comum de 5 dias do art. 357, § 1º** para pedir esclarecimento ou ajuste, com a instrução "conferir contra os capítulos III e VII da réplica: incontroversos fixados? pedido não combatido julgado? provas e ônus como pedidos?"; (c) se houve reconvenção respondida em peça separada, conferir o protocolo das duas.

## Etapa 6 — Depois da sentença: caso decidido

Publicada a sentença, a titular escreve a página em `casos_decididos/` do **bundle temático** (não deste), anonimizada, com o desfecho e três respostas obrigatórias: o juiz fixou como incontroversos os fatos que a réplica apontou? acolheu a confissão ou o documento do réu colhidos no capítulo III? julgou parcialmente o pedido não combatido, ou o deixou para a sentença? Com as respostas, atualizar o **repertório de defesas** do tema (linha nova, estado de "lacuna" para "coberto" quando a decisão trouxe o precedente, nota de frequência). É a única via pela qual o caso alimenta o acervo (AGENTS.md, regra 5) e a única forma de saber se o capítulo III funciona ou só parece bom.
