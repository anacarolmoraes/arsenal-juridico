---
type: workflow
title: Workflow — Petição inicial
description: Sequência executável com portões para redigir uma petição inicial, compondo técnica (este bundle) com matéria (bundle temático) e o pipeline do legal-orchestrator do workspace (ANALISE.md → estrutura aprovada → redação → validação → compilação).
tags: [peticao-inicial, workflow]
timestamp: '2026-09-04'
status: vigente
autor: escritorio
skills: [legal-orchestrator, legal-writer, tipografia-pma, legal-consistency-validator, humanizer-forense, peca-pma-builder, inicial-rescisao-lote, ficha-rescisao-lote]
playbook: /peticao-inicial/playbooks/playbook-peticao-inicial.md
---

# Workflow — Petição inicial

As etapas espelham os estágios do `legal-orchestrator` do workspace; o que é do acervo está linkado, o que é do escritório (forma, valores, assinatura) está em `perfil/definicoes.md` e não se repete aqui.

## Etapa 0 — Inventário e análise (Estágio 0)

1. Pasta local do caso, Drive do escritório, acervo: `<bundles>/index.md` → bundle da matéria → `index.md`, `jurisprudencia/`, `teses/`, `heuristicas/`, `casos_decididos/`, `playbooks/playbook-peticao-inicial-<tema>.md` → este bundle (`/peticao-inicial/`). PDF sem `.md` irmão passa pelo `pdfmd` antes.
2. Matéria com skill de apuração numérica (`ficha-rescisao-lote`) roda aqui; a ficha é a fonte dos números.
3. Escrever ou atualizar `clientes/<caso>/ANALISE.md`: cronologia com prescrição, teses candidatas do bundle com regime, responsabilidade, ônus, tutela e autocomposição decididos, mapa probatório em três estados, ataques previstos.

**Portão:** documento que sustenta um número ausente → parar e pedir. Tese sem página no bundle → não é candidata.

## Etapa 1 — Decisões de abertura e estrutura (Estágio 0.5)

1. Rito ([juizado ou vara comum](/peticao-inicial/heuristicas/juizado-ou-vara-comum.md)), foro ([competência e foro](/peticao-inicial/heuristicas/competencia-e-foro-na-inicial.md)), tutela e posição ([tutela provisória](/peticao-inicial/heuristicas/tutela-provisoria-na-inicial.md)), autocomposição: registrados na `ANALISE.md`, seção 2.
2. `<PECA>.estrutura.md` pelo [esqueleto único](/peticao-inicial/playbooks/playbook-peticao-inicial.md): seções na ordem com o estado de cada fato, destaque, peso, provas a produzir, fora, ataques respondidos, falta saber (até quatro perguntas à titular).

**Portão humano:** `aprovada: sim` da titular antes de qualquer prosa. Peça com template (`inicial-rescisao-lote`) segue sem parar e lista só os desvios.

## Etapa 2 — Redação (Estágios 1 e 2)

Skill `legal-writer` com a estrutura como entrada vinculante e a disciplina do encadeamento canônico PMA; `tipografia-pma` para a estrutura visual. Fato comprovado se afirma com `Doc. N`; frágil se narra como relato; a produzir se anuncia e vai para a seção de provas com o meio nomeado e, quando a prova está com o réu, o [pedido de exibição](/peticao-inicial/heuristicas/exibicao-de-documentos-a-partir-do-mapa-probatorio.md). Jurisprudência só transcrita da página do bundle.

**Portão:** placeholder não substitui fato que falta; o que falta volta ao "falta saber".

## Etapa 3 — Validação (Estágios 3 a 6)

1. `legal-consistency-validator` grava `<PECA>.validacao.md`: aderência à estrutura, fato a produzir afirmado como provado, ataque previsto sem resposta, valor da causa contra `definicoes.md` §1.
2. `humanizer-forense` na prosa própria; `lint-ia.js` verde não é prosa aprovada.
3. [Checklist de saída](/peticao-inicial/index.md) do bundle (319 I–VII, 320, encargos, tutela, requerimentos, forma) + os quatro testes do playbook.
4. **Banca** (`banca-revisora`) a pedido da titular ou em causa de alto valor.

## Etapa 4 — Compilação e protocolo (Estágio 7)

`md2docx` com `pipeline:`, `bundle:` e veredito no rastro; `lint-citacoes`, `lint-remissoes`, `lint-ia`, `lint-docx`. Exit 3 é página `em_teste`: decisão da titular no frontmatter. Depois do protocolo, anotar em `cronologia.md` (C1) o prazo esperado do despacho inicial.

## Etapa 5 — Depois do despacho

Tutela indeferida → agravo de instrumento (1.015, I). Emenda → [heurística de emenda](/peticao-inicial/heuristicas/emenda-da-inicial.md), 15 dias, e a causa vai para o `log.md` deste bundle. Indeferimento → apelação com retratação (331). Decisão que aplique tese do bundle → `casos_decididos/` do bundle temático.
