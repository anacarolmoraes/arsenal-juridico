---
type: router
title: Roteador de atividades
description: Mapeia cada atividade executável deste bundle para seu workflow, skills e conhecimento obrigatório.
tags: [roteador, execucao]
timestamp: '2026-07-21'
status: em_teste
autor: escritorio
---

# Roteador de atividades

Agente: localize a atividade pelos gatilhos, depois siga o workflow indicado **na ordem**, lendo antes o conhecimento obrigatório. Se a entrada mínima estiver incompleta, entreviste o usuário antes de executar.

Dois portões obrigatórios antes de **qualquer** atividade:

1. **Data do contrato original** — determina se o regime é o da Lei do Distrato (contratos a partir de 28/12/2018, art. 32-A da Lei 6.766/79) ou o regime anterior do STJ (Súmula 543, Tema 577, retenção escalonada 10-25%).
2. **Tribunal em que o processo tramita (ou tramitará)** — o IRDR-0009560-46.2017.827.0000/TJTO é vinculante **apenas na jurisdição do TJTO** (art. 985, I, CPC), e foi ele que gerou a suspensão dos processos de rescisão de lote no TO. **Se o caso for do TJTO**, o IRDR é o eixo (aplicar ou afastar por *distinguishing*). **Se for de outro tribunal**, não citar o IRDR como vinculante — sustentar a tese diretamente pelos precedentes do STJ e pela lei; o incidente serve, no máximo, como reforço persuasivo.

## Peticionar rescisão de compromisso de compra e venda de imóvel

- **Gatilhos:** "rescisão de contrato de imóvel", "distrato de lote", "cliente quer desistir do lote", "devolução de parcelas pagas"
- **Workflow:** /workflows/peticao-inicial-rescisao-imovel.md
- **Skills (ordem):** pre-peticionamento → legal-orchestrator (legal-writer, tipografia-pma, legal-consistency-validator) → peca-pma-builder
- **Conhecimento obrigatório antes de redigir:** /playbooks/playbook-peticao-inicial-rescisao-imovel.md, /teses/index.md, /jurisprudencia/irdr-0009560-46-2017-tjto.md
- **Entrada mínima:** data do contrato original, valor e percentual pago, natureza do empreendimento (lote × apartamento), motivo do desinteresse na manutenção do contrato

## Contestar ação de resolução/reintegração de posse movida por loteadora

- **Gatilhos:** "fui notificado para desocupar o lote", "loteadora está pedindo a rescisão", "reintegração de posse de lote", "recebi citação de ação de resolução contratual"
- **Workflow:** /workflows/contestacao-notificacao-viciada.md
- **Skills (ordem):** pre-peticionamento → legal-orchestrator (legal-writer, tipografia-pma, legal-consistency-validator) → peca-pma-builder
- **Conhecimento obrigatório antes de redigir:** /playbooks/playbook-contestacao-notificacao-viciada.md, /heuristicas/verificar-vicio-formal-de-notificacao-extrajudicial.md
- **Entrada mínima:** cópia da notificação extrajudicial recebida (ou certidão de diligência), contrato, histórico de pagamentos, houve cessão de direitos

## Agravar de decisão que mantém suspensão por IRDR já exaurido

- **Gatilhos:** "processo suspenso por causa do IRDR", "juiz não decide porque está aguardando o STJ", "levantar suspensão do processo"
- **Workflow:** /workflows/agravo-levantamento-suspensao-irdr.md
- **Skills (ordem):** legal-orchestrator (legal-writer, tipografia-pma, legal-consistency-validator) → peca-pma-builder
- **Conhecimento obrigatório antes de redigir:** /playbooks/playbook-agravo-levantamento-suspensao-irdr.md, /jurisprudencia/resp-2035848-to-acordao-nao-conhecimento.md, /jurisprudencia/resp-2035848-to-edcl-rejeitados.md
- **Entrada mínima:** decisão agravada (texto integral do fundamento da suspensão), data da suspensão, se há alguma hipótese de distinguishing aplicável

## Elaborar cumprimento de sentença com retenção percentual

- **Gatilhos:** "sentença transitou, preciso calcular a devolução", "cumprimento de sentença de rescisão de imóvel", "memória de cálculo de retenção"
- **Workflow:** /workflows/cumprimento-sentenca-retencao-percentual.md
- **Skills (ordem):** legal-orchestrator (legal-writer, tipografia-pma, legal-consistency-validator) → peca-pma-builder
- **Conhecimento obrigatório antes de redigir:** /playbooks/playbook-cumprimento-sentenca-retencao-percentual.md, /teses/vedacao-bis-in-idem-retencao-global-e-encargos-moratorios.md
- **Entrada mínima:** sentença/acórdão transitado com o percentual e índices fixados, extrato de pagamentos, memória de cálculo da parte contrária (se houver)
