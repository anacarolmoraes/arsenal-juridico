---
type: workflow
title: Workflow — cumprimento de sentença de rescisão com retenção percentual
description: Da sentença/acórdão transitado ao .docx protocolável, com portão de montagem da memória de cálculo própria e de checagem do bis in idem entre retenção global e encargos moratórios.
tags: [cumprimento-de-sentenca, memoria-de-calculo, retencao-percentual]
timestamp: '2026-07-22'
status: em_teste
autor: escritorio
skills: [legal-orchestrator, peca-pma-builder]
playbook: /playbooks/playbook-cumprimento-sentenca-retencao-percentual.md
---

# Workflow — cumprimento de sentença com retenção percentual

## Etapa 1 — Coleta dos parâmetros da decisão transitada

Entrada mínima: sentença/acórdão transitado com o percentual e os índices fixados, extrato de pagamentos, e a memória de cálculo da parte contrária (se houver). Extrair da decisão, sem inferir: percentual de retenção e **base de cálculo exata** (valor atualizado do contrato × valor efetivamente pago); índice de correção; termo inicial de juros (em regra, o trânsito em julgado); determinação ou não de dedução de IPTU e respectivo período. PORTÃO: se a base de cálculo ou o índice não estiverem inequívocos na decisão, resolver a dúvida antes de calcular — não arbitrar.

## Etapa 2 — Memória de cálculo própria

Montar a memória discriminada conforme o [playbook](/playbooks/playbook-cumprimento-sentenca-retencao-percentual.md): total pago; retenção (percentual × base); saldo a restituir; **correção mês a mês desde o desembolso de cada parcela** (não sobre o total de uma vez); juros desde o trânsito; dedução de IPTU do período de posse, se determinada. Para contratos anteriores a 28/12/2018, a restituição do saldo é em **parcela única** ([Súmula 543 / Tema 577](/teses/restituicao-imediata-parcela-unica-nao-parcelada.md)), não parcelada em 12 meses.

## Etapa 3 — Portão do bis in idem

Se houver memória de cálculo da parte contrária, revisá-la item a item contra a [vedação de bis in idem entre retenção global e encargos moratórios](/teses/vedacao-bis-in-idem-retencao-global-e-encargos-moratorios.md). PORTÃO: identificada a cumulação indevida (encargos moratórios cobrados de forma autônoma além da retenção percentual), termo inicial incorreto, fruição não determinada na sentença, ou IPTU de período anterior à posse — cada um vira ponto específico de impugnação, não observação genérica.

## Etapa 4 — Redação e validação (skill: legal-orchestrator)

Pipeline completo (writer → tipografia → validator). Pedido: homologação do cálculo próprio ou, na divergência, perícia contábil, com destaque para os vícios da Etapa 3.

## Etapa 5 — Entrega (skill: peca-pma-builder)

Gerar .docx no padrão PMA. Saída: petição de cumprimento + memória de cálculo (planilha/anexo) + relatório de fontes.
