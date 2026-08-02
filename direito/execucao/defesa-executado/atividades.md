---
type: router
title: Roteador de atividades — defesa do executado
description: Mapeia cada situação de defesa do executado (bloqueio SISBAJUD, penhora, prazo de embargos, bem de família, EPE) para o conhecimento e a peça correspondentes.
tags: [roteador, defesa-executado, execucao]
timestamp: '2026-08-01'
status: em_teste
autor: escritorio
---

# Roteador de atividades — defesa do executado

## Cliente teve valores bloqueados (SISBAJUD)

- **Gatilhos:** "conta bloqueada", "bloqueio SISBAJUD", "penhora on-line", "dinheiro preso na conta", "teimosinha"
- **URGÊNCIA:** prazo de **5 dias** da intimação (art. 854, §3º); silêncio converte em penhora e, pós-Tema 1.235, preclui a impenhorabilidade dos 40 SM
- **Conhecimento obrigatório:** [playbook SISBAJUD](playbooks/playbook-impugnacao-bloqueio-sisbajud.md), [heurística da primeira manifestação](heuristicas/arguir-impenhorabilidade-na-primeira-manifestacao.md), [checklist de prova](heuristicas/provar-a-origem-e-o-fim-do-valor-bloqueado.md), [tese 40 SM](teses/reserva-ate-40sm-impenhoravel-em-qualquer-aplicacao.md), [tese salário](teses/salario-impenhoravel-mitigacao-so-excepcional.md)
- **Entrada mínima:** data da intimação, extratos dos últimos meses, origem do valor (salário/reserva), valor da dívida × valor bloqueado

## Cliente foi citado em execução (título extrajudicial)

- **Gatilhos:** "fui citado numa execução", "recebi mandado para pagar em 3 dias", "prazo para embargos"
- **Conhecimento obrigatório:** [playbook de embargos](playbooks/playbook-embargos-a-execucao.md), [heurística de escolha do meio](heuristicas/escolher-meio-de-defesa-pela-fase-da-execucao.md), [teses/](teses/index.md)
- **Decisão prévia com o cliente:** embargar × moratória do art. 916 (parcelamento) — são excludentes
- **Entrada mínima:** cópia do título e da inicial executiva, data de juntada do AR/mandado, matérias de defesa disponíveis, bens em risco

## Penhora recaiu sobre a casa do cliente

- **Gatilhos:** "penhoraram minha casa", "bem de família", "leilão do imóvel"
- **Conhecimento obrigatório:** [tese bem de família](teses/bem-de-familia-ordem-publica-alegavel-ate-arrematacao.md), [checklist de prova](heuristicas/provar-a-origem-e-o-fim-do-valor-bloqueado.md), modelo real anonimizado em `raw/peticao-terceiro-bem-de-familia-tjsp.md`
- **Via:** simples petição nos autos (arts. 518 e 917, §1º), a qualquer tempo até a arrematação; checar exceções do art. 3º da Lei 8.009/90 antes de prometer resultado

## Prazo de embargos perdido / vício evidente

- **Gatilhos:** "perdi o prazo", "execução prescrita", "nunca fui citado", "sócio incluído sem desconsideração", "título nulo"
- **Conhecimento obrigatório:** [heurística EPE](heuristicas/epe-so-com-prova-pre-constituida.md), [heurística de escolha do meio](heuristicas/escolher-meio-de-defesa-pela-fase-da-execucao.md)
- **Portão:** só protocolar EPE com prova pré-constituída; senão avaliar ação autônoma

## Execução antiga, parada há anos

- **Gatilhos:** "essa execução é de 2015", "está parada há anos", "prescreveu?", "prescrição intercorrente"
- **Conhecimento obrigatório:** [tese da prescrição intercorrente](teses/prescricao-intercorrente-corre-da-primeira-tentativa-infrutifera.md), [art. 921 na redação da Lei 14.195/2021](jurisprudencia/cpc-art-921-prescricao-intercorrente.md)
- **Entrada mínima:** data da **primeira** certidão negativa de citação ou de busca de bens, e a lista datada de todos os atos posteriores — separando o que alcançou o devedor ou o patrimônio do que foi mera petição
- **Base conferida:** o art. 921 está transcrito e `vigente` no acervo, conferido contra o texto compilado — pode ser citado. O que **não** está coberto é jurisprudência posterior a 2021 sobre o marco inicial e sobre direito intertemporal

## Penhora de trator/caminhão/ferramenta ou imóvel rural

- **Gatilhos:** "penhoraram meu instrumento de trabalho", "penhoraram o sítio/chácara"
- **Conhecimento obrigatório:** [tese pequena propriedade rural](teses/pequena-propriedade-rural-impenhoravel-mesmo-hipotecada.md), [checklist de prova](heuristicas/provar-a-origem-e-o-fim-do-valor-bloqueado.md)

## Composição peça × matéria

A peça final (embargos, impugnação, agravo da decisão) compila pelo fluxo padrão do workspace: `perfil/definicoes.md` → este bundle → `direito/pecas/<tipo>` → `md2docx` com os três lints. Toda página deste bundle está `em_teste` — citar exige conferência oficial prévia ou `cita_em_teste: sim` declarado.
