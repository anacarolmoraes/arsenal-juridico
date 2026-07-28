---
type: workflow
title: Workflow — contestação a ação de resolução/reintegração por notificação viciada
description: Da citação recebida ao .docx protocolável, com portão de checagem do vício formal da notificação extrajudicial e da cessão de direitos antes de qualquer discussão de mérito.
tags: [contestacao, notificacao-extrajudicial, reintegracao-de-posse, defesa]
timestamp: '2026-07-22'
status: em_teste
autor: escritorio
skills: [pre-peticionamento, legal-orchestrator, peca-pma-builder]
playbook: /playbooks/playbook-contestacao-notificacao-viciada.md
---

# Workflow — contestação por notificação viciada

## Etapa 1 — Coleta e portões de regime

Entrada mínima: cópia da notificação extrajudicial recebida (ou certidão de diligência), contrato, histórico de pagamentos, e a informação sobre eventual cessão de direitos. Confirmar os **dois portões de regime** do roteador antes de seguir: (i) **data do contrato original** — define se o mérito subsidiário segue o art. 32-A (pós-28/12/2018) ou o regime anterior do STJ (Súmula 543, Tema 577, retenção 10-25%); (ii) **tribunal** — se o processo tramita no TJTO, o IRDR é o pano de fundo (aplicar/afastar); fora do TO, sustentar a defesa de mérito diretamente pelos precedentes do STJ, sem citar o IRDR como vinculante. PORTÃO: sem a certidão/comprovante da notificação, não é possível avaliar o vício central — entrevistar antes de seguir.

## Etapa 2 — Portão do vício formal da notificação

Rodar o [checklist de vício formal da notificação extrajudicial](/heuristicas/verificar-vicio-formal-de-notificacao-extrajudicial.md) contra os meios válidos fixados no [REsp 1.745.407/SP](/jurisprudencia/resp-1745407-sp.md) (Oficial do RI; Oficial de RTD; ou AR assinado pelo próprio devedor). PORTÃO: identificado o vício (endereço errado, ausência de assinatura do próprio devedor, meio inidôneo), ele é a **preliminar principal** — sem constituição regular em mora, falta pressuposto para a resolução/reintegração ([tese](/teses/notificacao-previa-invalida-obsta-rescisao-por-loteadora.md)).

## Etapa 3 — Portão da cessão de direitos

Checar [cessão de direitos antes de definir legitimidade](/heuristicas/checar-cessao-de-direitos-antes-de-definir-legitimidade.md). PORTÃO: havendo cessão não regularizada, incluir a preliminar de ilegitimidade passiva — omiti-la abre disputa possessória paralela e intervenção de terceiros no curso do processo.

## Etapa 4 — Redação e validação (skill: legal-orchestrator)

Pipeline completo (writer → tipografia → validator), montando a peça na ordem do [playbook](/playbooks/playbook-contestacao-notificacao-viciada.md): preliminares (ilegitimidade → ausência de mora regular) e, subsidiariamente, mérito (impugnação dos percentuais de retenção conforme o regime; indenização por benfeitorias de boa-fé anteriores à mora; impugnação de fruição sem prova de proveito econômico).

## Etapa 5 — Entrega (skill: peca-pma-builder)

Gerar .docx no padrão PMA. Saída: contestação + eventual reconvenção de benfeitorias + lista de anexos + relatório de fontes.
