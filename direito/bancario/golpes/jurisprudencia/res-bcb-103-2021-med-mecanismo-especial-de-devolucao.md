---
type: legislacao
title: Resolução BCB 103/2021 — Mecanismo Especial de Devolução (MED) do Pix, na redação original
description: Cria o MED no regulamento do Pix (anexo à Res. BCB 1/2020). Fundada suspeita de fraude → o banco do pagador abre notificação de infração e pede a devolução pelo DICT → aceita a notificação, bloqueio imediato do valor (ou do saldo) na conta recebedora → devolução. Prazo de 90 dias da transação; depende de saldo; o recebedor responde pelo prejuízo se rejeitar a notificação sem justo motivo. É o roteiro da causa de pedir "o que o banco fez depois de avisado". Texto ORIGINAL de 2021; as alterações posteriores do MED não estão no acervo.
tags: [golpe-pix, med, mecanismo-especial-de-devolucao, regulamento-pix, dict, notificacao-de-infracao, bloqueio-cautelar, res-bcb-103, exibicao-de-documentos]
timestamp: '2026-10-20'
status: em_teste
autor: ingerido
resource: https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolução BCB&numero=103
orgao: Banco Central do Brasil (Diretoria Colegiada)
data_publicacao: '2021-06-08'
data_vigencia: '2021-11-16'
raw: /raw/res-bcb-103-2021-med.md
verificado_em: '2026-10-20'
---

# Resolução BCB 103/2021 — o MED do Pix

> **Por que `em_teste`.** O texto depositado é o **da própria Res. BCB 103/2021**, que alterou o
> regulamento do Pix em 2021 (vigor em 1º/11/2021, efeitos a partir de 16/11/2021). O
> regulamento foi alterado depois disso e o acervo **não tem o texto consolidado** do anexo à Res.
> BCB 1/2020. Transcrição abaixo é fiel à Res. 103; **se o dispositivo ainda vige com essa
> redação, não foi conferido.** Antes de citar em peça: depositar o regulamento consolidado (Exibe
> Normativo, Res. BCB 1/2020) e conferir os arts. 41-A a 41-I e 78-F a 78-J.

Exposição de motivos: [Voto 119/2021-BCB](/raw/voto-bcb-119-2021-med.md) — o MED existe para
"aumentar ainda mais a segurança para os usuários do Pix, que teriam ampliada a possibilidade de
reaver fundos transacionados a partir de uma fraude" (item 4).

## O mecanismo (redação de 2021)

> O Mecanismo Especial de Devolução é o conjunto de regras e de procedimentos operacionais destinado a viabilizar a devolução de um Pix nos casos em que exista fundada suspeita do uso do arranjo para a prática de fraude
> (Resolução BCB 103/2021, art. 1º, que inclui o art. 41-B no regulamento do Pix)

Fluxo, na fraude ocorrida fora dos sistemas do recebedor:

1. O banco do pagador, por iniciativa própria ou a pedido do cliente, abre **notificação de
   infração** (art. 78-F) e **solicitação de devolução** (art. 78-I) pelo DICT.
2. O banco do recebedor analisa e aceita ou rejeita a notificação (art. 78-G). Só a aceita fica
   armazenada no DICT (art. 78-G, parágrafo único).
3. Com a aceitação, bloqueio imediato:

   > implicarão o bloqueio imediato, na conta transacional do usuário recebedor, dos valores cuja devolução é solicitada, ou, sendo menor, do valor correspondente ao saldo nela disponível.
   > (Resolução BCB 103/2021, art. 41-D, II, do regulamento do Pix)

4. Prazos de bloqueio e de devolução: remetidos ao Manual Operacional do DICT (art. 41-E), **não
   depositado**.
5. O recebedor é comunicado (art. 41-F) e pode pedir o cancelamento da devolução em 30 dias
   (art. 41-G).

## Prazo e saldo

Toda devolução "pressupõem a existência de recursos suficientes na conta transacional do usuário
recebedor" e:

> deverão ser iniciadas em até 90 (noventa) dias contados da data em que houver sido realizada a transação original.
> (Resolução BCB 103/2021, art. 41-A, II, do regulamento do Pix)

**É por isso que a hora importa.** O MED só devolve o que ainda está na conta; a janela entre o
aviso e a saída do dinheiro é a medida da falha do banco que demorou. Ver
[MED e conduta pós-aviso](../heuristicas/med-e-conduta-do-banco-apos-o-aviso.md): na
[ApCiv 1007466](apciv-1007466-tjsp-osasco-mercado-pago-bradesco-dano-moral.md) o MED foi acionado
e falhou por falta de saldo.

## Quem responde

> o participante prestador de serviço de pagamento do usuário recebedor responderá pelos eventuais prejuízos causados pela não devolução dos recursos quando:
> I - rejeitar, sem justo motivo, a notificação de infração de que trata o art. 78, quando vinculada a uma solicitação de devolução;
> (Resolução BCB 103/2021, art. 41-I, do regulamento do Pix)

O inciso II do art. 41-I responsabiliza também o recebedor que recusa a devolução por falta da
autorização contratual do cliente (art. 41-C, § 2º). Contra o banco recebedor, os dois incisos
são causa de pedir regulatória própria, além da abertura da conta.

## Fora do MED

O MED não cobre "controvérsias relacionadas a aspectos do negócio jurídico subjacente" nem
transações em que o dinheiro foi a "terceiro de boa-fé" (art. 41-B, parágrafo único). Golpe de
falsa venda em que o recebedor é um lojista real que entregou a mercadoria a outra pessoa: o MED
não é o caminho.

## Aplicação

- **Inicial:** cronologia com hora (Pix → aviso → abertura do MED → bloqueio → saída do dinheiro) e pedido de exibição da notificação de infração, da solicitação de devolução, da resposta do recebedor e do registro do bloqueio.
- **Réplica:** "acionamos o mecanismo de contestação" (defesa do BB no [RI 0046473](ri-0046473-tjpe-falso-advogado-recebedor-nubank.md)) não basta; exigir data e hora de cada etapa e o motivo da não devolução.
- **Contra o recebedor:** rejeição da notificação sem justo motivo atrai o art. 41-I, I.

## Pendências

- Regulamento do Pix consolidado (anexo à Res. BCB 1/2020) e Manual Operacional do DICT: depositar e conferir a redação vigente; promover esta página a `vigente` só depois.
