---
type: workflow
title: Workflow — Agravo em REsp (AREsp)
description: Sequência executável com portões de validação para redigir um AREsp, compondo técnica (este bundle) com matéria (bundle temático).
tags: [aresp, workflow]
timestamp: '2026-07-08'
status: vigente
autor: escritorio
skills: [legal-orchestrator, legal-writer, legal-consistency-validator, humanizer-forense, peca-pma-builder]
playbook: /agravo-em-resp/playbooks/playbook-agravo-em-resp.md
---

# Workflow — Agravo em REsp

## Etapa 0 — Rota e prazo (mesmo dia da intimação)

Ler a decisão de inadmissão contra o [mapa de rotas](/recurso-especial/playbooks/mapa-rotas-pos-inadmissao.md): AREsp × AgInt × ambos. Anotar o prazo (15 dias — úteis no cível, **corridos no penal**) e a data fatal em `cronologia.md` do caso (C1). **Portão:** rota errada é preclusão; na dúvida entre rotas, interpor os dois. Lembrete: EDcl da inadmissão não interrompe o prazo.

## Etapa 1 — Autópsia da decisão

**Portão de leitura (antes de qualquer análise):** ler **TODAS as peças da pasta do caso, integralmente** — decisão de inadmissão, REsp, acórdão, voto dos EDcl **e a petição dos EDcl** (é ela que prova o que foi suscitado, para a rota do CPC 1.025). Não redigir a partir de resumos ou inferências sobre peça não lida.

Preencher a [tabela de fundamentos da inadmissão](/agravo-em-resp/heuristicas/tabela-fundamentos-inadmissao.md): fundamento literal → rota → resposta técnica → prova. Recuperar o REsp e o acórdão (a resposta a quase todo óbice é apontar trechos deles). **Portão:** linha sem resposta técnica → parecer de viabilidade ao titular antes de prosseguir; sem aprovação, não redigir.

## Etapa 2 — Composição com a matéria

Se algum óbice exigir demonstração de mérito (ex.: Súmula 83 — distinção frente à orientação do STJ), buscar no bundle temático do caso os precedentes de distinção. A técnica é deste bundle; a distinção é matéria. **Portão:** sem bundle de matéria identificado quando necessário, pare e pergunte.

## Etapa 3 — Redação

Estrutura do playbook: endereçamento → **resumo do RISTJ 343-A** (com dispositivos invocados) → tempestividade → síntese da decisão agravada → **um capítulo por fundamento** (transcrição literal + resposta) → pedido (com julgamento conjunto e sustentação oral, CPC 1.042, §5º; autuação pela alínea "d" do RISTJ 253, p.u., II). Aplicar a [heurística estrutura AI-first](/heuristicas/estrutura-ai-first.md): conclusão nas primeiras linhas de cada capítulo, títulos autodescritivos, jurisprudência transcrita com fonte adjacente — tudo dissolvido em prosa, sem rótulos meta-textuais visíveis (rev. 2026-07-16). Regras do escritório: transcrição literal das fontes oficiais, granularidade máxima na legislação, **relatório de fontes** como entregável. Proibições absolutas: copiar razões do REsp; tese nova.

## Etapa 4 — Validação (portões bloqueantes)

1. Checklist anti-182 do playbook — TODOS "sim".
2. Tabela da Etapa 1 completa e espelhada nos capítulos da peça (fundamento ↔ capítulo, 1:1).
3. Se rota dupla: o AgInt correspondente está pronto para protocolo simultâneo?
4. skill `legal-consistency-validator` sobre a peça.
5. **Conferência de citações normativas:** toda norma citada conferida letra por letra (artigo, parágrafo, inciso, alínea) contra a página `jurisprudencia/` do bundle ou fonte oficial — nunca de memória ou de resumo.
6. **Remissões cruzadas:** cada "(Capítulo X)" da síntese e do corpo aponta para o capítulo certo (obrigatório reconferir após qualquer renumeração).
7. **Desrobotização:** skill `humanizer-forense` sobre a prosa própria (rodar `scripts/lint-ia.js`; corrigir acima dos limites: travessões, paralelismos negativos, perguntas retóricas, frases-clone, registro inflado) — sem tocar transcrições, rótulos e citações.
8. **Banca (peça a tribunal superior — este AREsp sempre é):** skill `banca-revisora` sobre a versão pós-lints, ANTES do protocolo; achados CONFIRMADOS bloqueiam até resolvidos; parecer arquivado no dossiê (C1).

## Etapa 5 — Entrega

skill `peca-pma-builder` (padrão tipográfico do escritório) + relatório de fontes + tabela de fundamentos anexada ao dossiê do caso (C1).
