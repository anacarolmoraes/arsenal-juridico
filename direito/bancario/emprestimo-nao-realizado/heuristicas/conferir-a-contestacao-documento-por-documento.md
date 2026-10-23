---
type: heuristica
title: Conferir a contestação documento por documento — número, valor, data, conta, horário, assinatura
description: Antes de escrever a réplica, cada documento do banco é confrontado com o contrato discutido e com os demais documentos dele mesmo. Inconsistências típicas — vários contratos com o mesmo horário e a mesma assinatura; assinatura em folha avulsa; "contratação digital" provada com contrato físico; CCB de valor estranho às operações; selfie diferente do documento; cadastro divergente; parcelas pagas por terceiro; TED sem liquidação. Cada uma vira impugnação específica; a genérica deixa fato incontroverso.
tags: [replica, contestacao, impugnacao-especifica, ted, contrato, assinatura, conferencia]
timestamp: '2026-10-20'
status: em_teste
autor: escritorio
peca: replica
momento: [replica]
casos_origem: []
fundamentos:
  - /teses/onus-prova-assinatura-impugnada.md
---

# Conferir a contestação documento por documento

**Regra:** a réplica não repete a inicial; desmonta a contestação. Para cada documento do banco: *o que ele prova, o que não prova, e bate com os outros?*

## A conferência

| Confrontar | Com | Inconsistência típica |
|---|---|---|
| número, data, valor, parcelas, modalidade do contrato juntado | contrato discutido na inicial e nos extratos | documento de outra operação |
| horário de assinatura de cada contrato | os demais contratos | quatro contratos às 10h32, mesma assinatura: como se formalizaram no mesmo instante? |
| folha de assinatura | o instrumento | assinatura apartada, sem identificador que a ligue a este contrato |
| forma de contratação alegada | formato do documento | "digital" na contestação, contrato físico nos autos: qual é o registro da contratação? |
| selfie | foto do documento e dados cadastrais | rosto ou dados que não correspondem |
| comprovante de TED/Pix | valor do contrato, titularidade da conta, data, extrato | ordem de transferência sem liquidação; conta de terceiro; valor diverso |
| parcelas pagas | quem pagou | pagamento por terceiro não prova regularidade: é compatível com o fraudador mantendo aparência |

## O TED exige impugnação própria

Comprovante de crédito não impugnado especificamente vira fato incontroverso e sustenta improcedência mesmo com contrato frágil. Perguntas: o valor corresponde ao contrato? a conta é do autor? a data é compatível? o documento mostra liquidação ou só ordem? o crédito aparece no extrato? houve estorno ou saída imediata? Se recebeu, qual é a controvérsia sobre esse valor ([compensação só com proveito](compensacao-so-com-proveito-economico.md))?

## Checklist antes de fechar a réplica

Impugnei o contrato especificamente? A forma exigida para este consumidor foi observada? Confrontei o TED com número, valor e data? Titularidade da conta de destino conferida? Pedi prova complementar onde o comprovante não demonstra liquidação? Enfrentei o recebimento, se provado, e expliquei por que não resolve a validade? Requeri as provas com fundamento? Rebati a prescrição pela qualificação da causa de pedir ([prazo decenal](qualificar-a-causa-de-pedir-como-nulidade-prazo-decenal.md))?

## Quando NÃO usar

Não listar inconsistência que não existe; a impugnação tem de ser verdadeira e ancorada na folha. Inconsistência isolada não prova fraude: ela exige esclarecimento e prova técnica individualizada, e é assim que se escreve.

## Origem e pendência

Triagem de perfil público (@jessicaabreuadv, posts DdEDRbCoCv_, DcdpCPcoKws, Dcd2zEHoJVy, DceEjRuoKgq, DdRI6E_IIhG, ago–set/2026). Acórdãos a capturar: TJSP 1022245-39.2024.8.26.0004 (CCB de R$ 2.339 contra operações de R$ 1.000 e R$ 5.922); TJPB 0806156-49.2022.8.15.0731 (parcelas pagas por terceiro); TJMS 0858838-50.2024.8.12.0001 (tela de TED não prova crédito; cartão não entregue). Pendência no motor: script de conferência da contestação contra a `ANALISE.md`, no molde do `conferir-decisao.js`.
