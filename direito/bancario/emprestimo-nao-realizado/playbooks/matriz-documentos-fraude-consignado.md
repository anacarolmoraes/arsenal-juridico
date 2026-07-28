---
type: matriz-documentos
title: Matriz de documentos — fraude em empréstimo consignado
description: O que coletar do cliente no atendimento e por quê, com criticidade — cada item justificado por tese, heurística ou exigência processual (LGPD, minimização).
tags: [atendimento, coleta, documentos, lgpd, fraude, consignado]
timestamp: '2026-07-06'
status: vigente
autor: escritorio
peca: peticao-inicial
---

# Matriz de documentos — fraude em consignado

Usada no **atendimento** (o que pedir ao cliente) e instanciada no `caso.md` da pasta do caso (C1) como checklist com estado: `presente` | `pendente` | `dispensado (motivo)`.

**Regra de minimização (LGPD):** só se coleta o que esta matriz justifica. Documento sem tese/heurística/exigência processual que o lastreie não entra na matriz — e não se pede ao cliente.

## A matriz

| Documento | Criticidade | Por quê (fundamento no bundle) |
|---|---|---|
| Procuração | bloqueante | representação processual; subscritoras e dados sempre de [/escritorio.md](/escritorio.md) |
| Documento de identidade (RG/CNH) | bloqueante | qualificação; idade ≥ 60 → prioridade de tramitação (playbook, preliminares); cotejo com o documento usado na contratação é indício de negligência — [/teses/dever-verificacao-identidade-res-4753.md](/teses/dever-verificacao-identidade-res-4753.md) |
| Comprovante de residência | alta | qualificação e competência; praça de contratação distante do domicílio é indício concreto — [/teses/dever-verificacao-identidade-res-4753.md](/teses/dever-verificacao-identidade-res-4753.md) |
| Declaração de hipossuficiência | alta | justiça gratuita — [/jurisprudencia/cpc-arts-98-99.md](/jurisprudencia/cpc-arts-98-99.md) (playbook, preliminares) |
| Extrato do benefício/contracheque com **todos** os descontos (datas e valores) | bloqueante | prova do desconto; consistência valor da causa × descontos × dano material (erro mais atacado em contestação — playbook); datas decidem a modulação do dobro — [/teses/devolucao-em-dobro-boa-fe-objetiva.md](/teses/devolucao-em-dobro-boa-fe-objetiva.md) |
| Extrato bancário do período do suposto crédito | bloqueante | destino do valor: não utilizado / jamais recebido / intocado → depósito judicial — [/heuristicas/demonstrar-nao-utilizacao-do-valor.md](/heuristicas/demonstrar-nao-utilizacao-do-valor.md) |
| Protocolos de reclamação administrativa (nº, data, meio, resultado) | alta | narrativa da tentativa prévia com detalhes — [/heuristicas/comprovar-tentativa-administrativa-previa.md](/heuristicas/comprovar-tentativa-administrativa-previa.md); se não houver, orientar o cliente a fazê-la antes de ajuizar |
| Contrato/cédula impugnado (se o cliente tiver) | média | impugnação expressa da assinatura — [/heuristicas/impugnar-assinatura-na-inicial.md](/heuristicas/impugnar-assinatura-na-inicial.md) e [/teses/onus-prova-assinatura-impugnada.md](/teses/onus-prova-assinatura-impugnada.md); a ausência não impede a ação — pedir **exibição de documentos** (playbook, pedidos) |
| Detalhamento da operação: canal, data, praça, correspondente envolvido | média | indícios concretos de negligência do banco (evita a "narrativa genérica de fraude" — playbook, erros a evitar); correspondente identificado → decidir inclusão como corréu — [/teses/solidariedade-correspondente-bancario.md](/teses/solidariedade-correspondente-bancario.md) |

## Comprovação reforçada de hipossuficiência (condicional)

Calibragem do titular (2026-07-06): a declaração de hipossuficiência sozinha frequentemente não basta — **juízes vêm exigindo documentação complementar** para deferir a gratuidade. Coletar **apenas quando a gratuidade for requerida** e conforme o perfil do cliente/histórico do juízo (minimização — não é coleta padrão):

| Documento | Observação |
|---|---|
| Extratos de **todos** os relacionamentos bancários | o juízo pode conferir via **Registrato** (site do Banco Central); o próprio cliente pode emitir o relatório lá |
| Declaração de imposto de renda (ou de isenção) | exercício mais recente |
| Conta de energia com tarifa social/baixa renda | se houver |
| Comprovante de auxílio/benefício governamental | se houver |
| Contracheques | período recente |

## Dados de triagem (perguntas, não documentos)

Do playbook, seção "Antes de redigir": como o cliente descobriu o desconto; houve correspondente bancário na contratação; perfil do cliente (idoso, analfabeto funcional, hipossuficiente). São insumo dos **Fatos essenciais** do `caso.md`, não coleta documental.

## Origem

Derivada do playbook da inicial + heurísticas + teses do bundle, validada contra a coleta real observada no primeiro caso estruturado no schema C1 (2026-07-06): todos os 9 itens presentes na pasta do cliente, coletados na prática do escritório antes de a matriz existir — a matriz descreve e sistematiza o que o atendimento já fazia.
