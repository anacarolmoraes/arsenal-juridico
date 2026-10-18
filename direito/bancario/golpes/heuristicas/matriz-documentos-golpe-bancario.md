---
type: heuristica
title: Matriz de documentos — golpe bancário (falsa central, Pix induzido, empréstimo contratado pelo golpista)
description: O que coletar do cliente no atendimento de golpe bancário e por quê, com criticidade e o fundamento de cada item; complementa a matriz transversal da inicial. O centro é o extrato integral do período, porque a tese do defeito do serviço depende de mostrar a atipicidade das operações contra o perfil de uso, e a ficha numérica só aceita transação com fonte.
tags: [atendimento, coleta, documentos, golpe, falsa-central, pix, lgpd]
timestamp: '2026-09-08'
status: em_teste
autor: escritorio
peca: peticao-inicial
fundamentos:
  - /jurisprudencia/resp-2222059-sp-falsa-central-perfil-consumo.md
---

# Matriz de documentos — golpe bancário

Complementa a [matriz transversal da inicial](../../../pecas/peticao-inicial/heuristicas/matriz-documentos-da-inicial.md),
que traz o que o art. 320 sempre exige e a coleta da gratuidade. Aqui, só o que é da matéria.
`em_teste` até a titular conferir contra os casos da pasta.

**Regra de minimização (LGPD):** só se coleta o que esta matriz justifica.

## A matriz

| Documento | Criticidade | Por quê (fundamento no bundle) |
|---|---|---|
| Extrato **integral** da conta de origem, de 90 dias antes do golpe até hoje | bloqueante | perfil de uso (valores médios, destinatários habituais, horários) × operações do golpe: é a atipicidade que o [REsp 2.222.059/SP](/jurisprudencia/resp-2222059-sp-falsa-central-perfil-consumo.md) usa para afirmar o defeito do serviço; sem o antes, não há "fora do perfil" |
| Comprovante de cada transação do golpe (Pix, TED, saque, compra), com hora e destinatário | bloqueante | cada `R$` da peça sai daqui (ficha `ficha-golpe-bancario`); dupla contagem entre conta de origem e conta intermediária só se detecta com os dois documentos |
| Extrato ou comprovante da conta intermediária, quando o golpe passou por conta do próprio autor em outro banco | alta | a mesma transferência aparece duas vezes; [contra-ataque quantum](/contra-ataques/quantum-comprovado-extratos-vs-saldo.md) |
| Contrato, cédula ou tela do empréstimo contratado durante o golpe (ou a negativa do banco em fornecer) | alta | base do pedido declaratório e da repetição em dobro (só sobre o que o banco **cobrou**); se o banco não fornece, exibição do art. 397 |
| Registro do atendimento fraudulento: número que ligou, horário, prints de mensagens, e-mail ou SMS com link | alta | nomeia a alavanca de engenharia social ([transversal LGPD](../../../lgpd/heuristicas/engenharia-social-as-alavancas.md)): consumidor induzido, não descuidado; número que exibia o nome do banco é indício de vazamento de dado |
| Registrato (Banco Central): relatório de chaves Pix, relatório de contas e relacionamentos (CCS) e SCR, emitidos pelo próprio cliente | alta | a data e a hora de criação de chave e de abertura de conta no CPF da vítima provam a conta intermediária (chave criada minutos antes do crédito); o CCS revela contas que o cliente esqueceu de mencionar e que o réu vai explorar; o SCR mostra a dívida derivada do golpe |
| Boletim de ocorrência | média | fato frágil vira relato documentado; não prova o golpe, mas fixa a data e a versão do autor |
| Protocolos junto ao banco: contestação da operação, pedido de MED (Mecanismo Especial de Devolução), resposta recebida | bloqueante | tentativa administrativa e decisão sobre autocomposição; a negativa fundamenta o desinteresse (art. 319, VII); a devolução parcial via MED entra como estorno na ficha |
| Comprovante de negativação (consulta Serasa/SPC/Boa Vista com data) | bloqueante se há negativação | dano moral *in re ipsa* da inscrição indevida e pedido de tutela para baixa; a data fixa o termo da correção |
| Comprovante de que o valor subtraído era verba alimentar (contracheque, extrato do benefício) | média | segunda fase do método bifásico: circunstância que eleva, com `Doc. N` |
| Prints de perfil ou anúncios do golpista, quando houver | baixa | indício para ofício ao banco de destino (identificação do beneficiário); não substitui o ofício |

## O que não pedir

- Senha, token ou foto de cartão: nunca; a peça não precisa e a guarda expõe o cliente.
- Extratos de contas que não participaram do golpe, salvo para gratuidade acima da faixa
  (matriz transversal, Parte C).

## Instanciação

Na seção 7 (**Documentos**) da `clientes/<caso>/ANALISE.md`, com estado `presente | pendente |
dispensado (motivo)`, no formato da matriz transversal (não se cria `DOCUMENTOS.md`); os
`presente` viram o rol `documentos:` do frontmatter. As transações viram a ficha numérica da
`ficha-golpe-bancario` (`dados_caso.json`), que é rastro de trabalho e mora em `tmp/<caso>/`,
nunca na pasta do cliente, uma linha por transação com `fonte: Doc. N, p. X`.
