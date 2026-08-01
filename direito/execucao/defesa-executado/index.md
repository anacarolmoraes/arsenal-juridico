---
okf_version: "0.1"
bundle_version: "0.1.0"
---

# Defesa do Executado — Bundle de Competência (Execução Civil)

Defesa de quem está no polo passivo de execução de título extrajudicial ou cumprimento de sentença: qual instrumento usar em cada fase (embargos, impugnação, exceção de pré-executividade, impugnações específicas), o que alegar (impenhorabilidades, vícios do título e do procedimento, excesso) e como provar. Agentes: leiam o [atividades.md](atividades.md) para executar.

## Seções

- [README.md](README.md) — onboarding do agente consumidor
- [atividades.md](atividades.md) — roteador: atividade → conhecimento obrigatório
- [jurisprudencia/](jurisprudencia/index.md) — os dois repetitivos que redesenharam o tema em 2024
- [teses/](teses/index.md) — impenhorabilidades (40 SM, salário, bem de família, pequena propriedade rural) e **prescrição intercorrente na redação da Lei 14.195/2021**
- [heuristicas/](heuristicas/index.md) — regras de decisão: quando arguir, por qual via, com que prova
- [playbooks/](playbooks/index.md) — impugnação ao bloqueio SISBAJUD e embargos à execução
- [raw/](raw/index.md) — fontes depositadas (curso de terceiro fora do git; ProAfR oficial do Tema 1.235; petição de terceiro anonimizada)
- [log.md](log.md) — histórico

## O tema num parágrafo

A defesa do executado se decide em duas perguntas: **em que fase a execução está** e **a alegação depende de prova a produzir**. Quem tem prova pré-constituída ou matéria de ofício se defende por petição simples (exceção de pré-executividade, impugnação ao bloqueio, impugnação à penhora); quem precisa instruir vai de embargos (15 dias úteis da juntada da citação, individuais por executado) ou de impugnação ao cumprimento de sentença (15 dias automáticos após o prazo de pagamento, matérias taxativas do art. 525, §1º). O terreno mudou em 2024: a Corte Especial fixou no **Tema 1.235** que a impenhorabilidade da reserva de até 40 salários mínimos **não é matéria de ordem pública e preclui** se não arguida na primeira oportunidade — o prazo de 5 dias do art. 854, §3º virou o momento mais importante da defesa patrimonial. Escapam da preclusão o bem de família da Lei 8.009/90 (ordem pública, alegável até a arrematação) e as nulidades do art. 803. Em qualquer via, impenhorabilidade se prova com documento anexado à primeira petição — a alegação nua equivale a silêncio.

**v0.1.0 (2026-08-01).** Semente extraída do curso "Método MMA" (obra de terceiro em `raw/`, fora do git), do acórdão oficial de afetação do Tema 1.235 e de uma petição real anonimizada de bem de família. **Todas as páginas estão `em_teste`**: nenhum inteiro teor de mérito foi conferido contra fonte oficial ainda — pendências declaradas no [log.md](log.md). Antes de citar em peça: conferir no tribunal e depositar em `raw/` (regra dura 4; o `lint-citacoes` bloqueia).

## Fronteiras

- Execução **movida pelo cliente** (lado credor) não é aqui: cheque está em [direito/cambial/execucao-cheque/](../../cambial/execucao-cheque/index.md); honorários em [direito/cobranca-honorarios/](../../cobranca-honorarios/index.md).
- Técnica de peça recursal (agravo de instrumento, apelação) é do transversal [direito/pecas/](../../pecas/index.md).
