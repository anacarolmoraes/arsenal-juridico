---
type: workflow
title: Workflow — execução de cheque, da cártula ao .docx protocolável
description: Sequência com quatro portões: conferência da cártula, cálculo da data-limite, redação fundamentada no bundle e compilação com os lints do padrão PMA.
tags: [workflow, execucao, cheque]
timestamp: '2026-07-28'
status: vigente
autor: escritorio
skills: [pdfmd, legal-orchestrator, humanizer-forense, peca-pma-builder]
playbook: /playbooks/playbook-execucao-cheque.md
---

# Workflow — execução de cheque

## Etapa 1 — Leitura dos documentos do caso

Converter os PDFs da pasta do caso com a skill `pdfmd`. **PORTÃO:** a cártula não se lê por OCR. Cheque manuscrito produz texto ilegível mesmo com Tesseract; renderizar a página como imagem e conferir visualmente, ampliando o verso para ler data, motivo e banco de cada carimbo de devolução.

## Etapa 2 — Conferência do título

Executar integralmente a [checagem de preenchimento](/heuristicas/conferir-preenchimento-do-cheque-antes-de-executar.md), incluindo a consulta cadastral do emitente. **PORTÃO:** resultado "não executável" encerra o workflow e abre a análise das vias dos arts. 61 e 62 da Lei do Cheque. O resultado da conferência é registrado por escrito na pasta do caso antes de qualquer redação.

## Etapa 3 — Prazo

Calcular a data-limite: emissão, mais 30 dias na mesma praça ou 60 em praça diversa, mais seis meses. **PORTÃO:** faltando menos de trinta dias, a distribuição precede qualquer nova tentativa de composição, e a etapa 4 roda em regime de urgência.

## Etapa 4 — Redação

Ler o [playbook](/playbooks/playbook-execucao-cheque.md) e as três teses do bundle antes de escrever. Redigir em Markdown, dialeto PMA. **PORTÃO:** toda tese empregada tem de ter fundamento depositado neste bundle; jurisprudência fora dele só por citação indireta, e enunciado sumular não se cita de memória.

## Etapa 5 — Compilação

Compilar com `md2docx`, que roda os lints de remissões, anti-IA e citações e valida o timbrado do `.docx`. **PORTÃO:** lint reprovado não se contorna com `--skip-lint`.

## Etapa 6 — Conferência final

Valor da causa igual ao demonstrativo. Denominação do executado igual à da consulta cadastral. Datas da peça iguais às dos carimbos. Lista de documentos da inicial completa, com procuração e custas.
