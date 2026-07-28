---
type: escritorio-config
title: Dados do escritório para peças
description: Subscritoras, contatos e preferências fixas do escritório — fonte única para qualificação de peças (substitui a pesca de exemplos nas skills).
tags: [escritorio, subscritoras, configuracao]
timestamp: '2026-07-21'
status: vigente
autor: escritorio
---

# Dados do escritório (PMA — Paulo Moraes Advocacia)

**Regra para o agente:** todo dado de subscrição/contato em peça vem DESTE arquivo — nunca de exemplos embutidos em skills. Em distribuição externa do bundle, este arquivo é excluído ou substituído pelo equivalente do consumidor. Replicado a partir de `direito/bancario/emprestimo-nao-realizado/escritorio.md` (dado do escritório, não do tema — pendência de schema v0.5: convenção de link entre bundles evitaria essa duplicação).

## Subscritoras (confirmar a cada peça quem assina)

- **ANA CAROLINA RIBEIRO DE MORAES PAULO** — OAB/TO 6573
- **FLAVIA PAULO DOS SANTOS OLIVEIRA RIBEIRO** — OAB/TO 6951

## Contatos para intimações

- E-mail: contato@paulomoraesadvocacia.com.br
- Telefones/WhatsApp: (63) 98489-2582 e (63) 98105-2171
- Endereço profissional: [PREENCHER — não consta das fontes migradas]

## Preferências fixas

- Habilitação e intimação exclusivamente em nome das advogadas subscritoras.
- Opção pelo Juízo 100% Digital quando a comarca suportar (Res. CNJ 345/2020 — página ainda não ingerida neste bundle; ver `direito/bancario/emprestimo-nao-realizado/jurisprudencia/res-cnj-345-2020.md`).
- Padrão visual: skill `tipografia-pma` / `peca-pma-builder` (Montserrat 12pt, banner e logo).
