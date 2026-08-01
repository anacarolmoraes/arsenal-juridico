---
type: playbook
title: Playbook — impugnação ao bloqueio SISBAJUD (art. 854, §3º)
description: Como montar, em 5 dias, a manifestação do executado contra a indisponibilidade de ativos financeiros — qualificação da verba, prova pré-constituída, pedidos e recurso cabível.
tags: [sisbajud, impugnacao, bloqueio, art-854, impenhorabilidade]
timestamp: '2026-08-01'
status: em_teste
autor: escritorio
peca: impugnacao-incidental
teses:
  - /teses/reserva-ate-40sm-impenhoravel-em-qualquer-aplicacao.md
  - /teses/salario-impenhoravel-mitigacao-so-excepcional.md
skills: [peca-pma-builder, humanizer-forense]
---

# Playbook — impugnação ao bloqueio SISBAJUD

**Janela:** 5 dias da intimação do bloqueio (art. 854, §§2º-3º). Silêncio = conversão automática em penhora (§5º) e, depois do Tema 1.235/STJ, preclusão da impenhorabilidade do art. 833, X. Este playbook é para a fase **antes** da conversão; bloqueio já convertido → impugnação à penhora (525, §11 / 917, §1º) ou EPE, conforme o caso.

## Passo 0 — triagem (mesmo dia da intimação)

1. De onde veio o dinheiro bloqueado? (salário/benefício × reserva × receita avulsa) — define a tese.
2. Quanto foi bloqueado × quanto é a dívida? (excesso de indisponibilidade é a segunda matéria legal — art. 854, §3º, II; e o §1º manda o juiz cancelar excesso até de ofício).
3. Há vício anterior aproveitável (citação nula, desconsideração sem incidente, prescrição intercorrente)? A primeira manifestação é o momento de arguir tudo.
4. Pessoa jurídica? Teses dos 40 SM e do salário não servem; o eixo vira função social da empresa/capital de giro e folha.

## Estrutura da petição (dialeto PMA, estrutura AI-first invisível)

1. **BLUF:** o valor bloqueado é [salário/reserva] e portanto impenhorável; pedido de cancelamento em 24 h (art. 854, §4º).
2. **Síntese do necessário:** execução, valor, data do bloqueio, intimação.
3. **Qualificação da verba** com a prova anexada — checklist por perfil na [heurística de prova](/heuristicas/provar-a-origem-e-o-fim-do-valor-bloqueado.md). Sem prova, não protocolar: alegação nua equivale a silêncio.
4. **Matérias cumuladas** (se houver): excesso de indisponibilidade com demonstrativo próprio; vícios processuais; prescrição intercorrente.
5. **Pedidos:** cancelamento da indisponibilidade (854, §4º — cumprimento pela instituição em 24 h); subsidiário de liberação parcial (percentual que preserve o mínimo existencial); se houver negócio processual ou contrato, destinação de percentual aos honorários do patrono só com base contratual expressa.

## Portões

- Rodar `lint-ia` antes de compilar; peça citando páginas `em_teste` deste bundle exige conferência da fonte oficial ou `cita_em_teste: sim` no frontmatter (portão do `lint-citacoes`).
- Conferir prazos no eproc/DJEN — a intimação do 854, §2º pode vir na pessoa do advogado.

## Depois da decisão

- Acolhida → cancelamento; atenção: a penhora anterior interrompida pode reabrir discussão de prescrição intercorrente.
- Rejeitada → converte em penhora; recurso: **agravo de instrumento** (art. 1.015, p.u.). A rejeição não gera honorários (decisão interlocutória), mas transita e faz coisa julgada material sobre a questão decidida.
