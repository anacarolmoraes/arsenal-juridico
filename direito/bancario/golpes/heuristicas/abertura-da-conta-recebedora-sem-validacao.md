---
type: heuristica
title: Atacar a abertura da conta recebedora — checklist regulatório (Res. CMN 4.753, Res. BCB 96/2021, BC Protege+)
description: Contra o banco recebedor, a pergunta não é "quem abriu a conta" e sim "como o banco validou que quem abriu era o titular". Jornada de abertura reconstruída pelas normas do BCB — contas de depósito (Res. CMN 4.753/2019), contas de pagamento (Res. BCB 96/2021, art. 4º) e, desde 1º/12/2025, consulta prévia ao BC Protege+ (Res. CMN 5.218/2025 + IN BCB 661/2025). Encerrar a conta depois não apaga a falha da abertura.
tags: [golpe-pix, banco-recebedor, kyc, onboarding, res-cmn-4753, res-bcb-96, bc-protege, instituicao-de-pagamento, exibicao-de-documentos, peticao-inicial]
timestamp: '2026-10-20'
status: em_teste
autor: escritorio
peca: peticao-inicial
momento: [inicial, replica]
casos_origem: []
fundamentos:
  - /jurisprudencia/apciv-1017912-tjsp-conta-fraudulenta-kyc.md
  - /jurisprudencia/apciv-1026252-tjsp-mercado-pago-origem-bradesco-recebedor.md
  - /jurisprudencia/apciv-1007466-tjsp-osasco-mercado-pago-bradesco-dano-moral.md
  - /jurisprudencia/ri-0046473-tjpe-falso-advogado-recebedor-nubank.md
  - /jurisprudencia/res-bcb-96-2021-art-4-conta-de-pagamento.md
  - /jurisprudencia/bc-protege-consulta-previa-res-cmn-5218-in-bcb-661.md
---

# Atacar a abertura da conta recebedora

**Regra:** contra a instituição que recebeu o Pix, a causa de pedir é a abertura da conta usada no golpe, não o golpe. Exige-se a demonstração da **jornada de abertura** e confronta-se com o dever regulatório de identificar, qualificar e validar o titular.

## Por que favorece a vítima

Desloca o processo da conduta da vítima para o *onboarding* do recebedor, onde a vítima não teve participação nenhuma. Conta aberta sem validação é defeito do serviço do recebedor, que responde mesmo que o banco pagador seja absolvido pelo perfil. O TJSP já condena nessa linha ([ApCiv 1017912](/jurisprudencia/apciv-1017912-tjsp-conta-fraudulenta-kyc.md), [ApCiv 1026252](/jurisprudencia/apciv-1026252-tjsp-mercado-pago-origem-bradesco-recebedor.md), [ApCiv 1007466](/jurisprudencia/apciv-1007466-tjsp-osasco-mercado-pago-bradesco-dano-moral.md)): o recebedor que não prova as cautelas da Res. 4.753 responde solidariamente.

## O checklist regulatório

| Norma | Alcance | O que pedir |
|---|---|---|
| Res. CMN 4.753/2019 ([art. 2º](../../emprestimo-nao-realizado/jurisprudencia/res-bacen-4753-2019-art-2.md)) | contas de depósito em banco | procedimentos de identificação, qualificação e validação, confronto com bases públicas/privadas |
| [Res. BCB 96/2021, art. 4º](/jurisprudencia/res-bcb-96-2021-art-4-conta-de-pagamento.md) | contas de pagamento (fintechs, carteiras) | os mesmos controles; é a norma que fecha a saída "não somos banco" |
| [Res. CMN 5.218/2025 + IN BCB 661/2025](/jurisprudencia/bc-protege-consulta-previa-res-cmn-5218-in-bcb-661.md) | contas abertas a partir de **1º/12/2025** | prova da consulta prévia ao **BC Protege+**, seu resultado e eventual manifestação contrária; a regulamentação manda guardar o comprovante por 10 anos |

Pedido de exibição individualizado (art. 397): proposta de abertura, documentos usados, selfie e biometria com prova de vida, dados cadastrais informados, IP, dispositivo, *user agent*, geolocalização, logs da jornada, score antifraude, resultado da consulta ao Protege+, data e hora de cada evento.

## Sinais de conta de passagem (narrativa da inicial)

Conta aberta há dias; dinheiro entra e sai em minutos; pulverização para outras contas; divergência entre os dados cadastrais e os do suposto titular; outra conta já existente no mesmo CPF; telefone e e-mail que não eram do titular. Tudo isso o recebedor sabia ou devia saber.

## Dois lances da contestação a aproveitar na réplica

- "Identificamos uso indevido e encerramos a conta": confissão de que a conta servia à fraude. Encerrar depois não apaga a falha da abertura.
- "O empréstimo foi contratado em outra instituição": não afasta a responsabilidade de quem permitiu a abertura. Individualizar ([individualizar a falha de cada ré](individualizar-a-falha-de-cada-re.md)).

## Quando NÃO usar

Conta recebedora antiga, de titular real com histórico, usada como "laranja" ocasional: a falha não é de abertura, é de monitoramento (eixo do perfil e do MED). Golpe anterior a 1º/12/2025: não invocar o Protege+.

## Fontes

- **Depositadas em 20/10/2026 e conferidas contra o checklist acima:** Res. BCB 96/2021 consolidada (o art. 4º é o dever de validar; o 4º-A, a consulta ao Protege+ só para conta **pré-paga**; guarda da prova por dez anos no § 4º), Res. CMN 5.218/2025 e IN BCB 661/2025 (a IN, art. 6º, dá o conteúdo da prova da consulta: é a lista do pedido de exibição). Páginas `vigente` linkadas na tabela.
- **TJPE RI 0046473-94.2024.8.17.8201** capturado: [página](/jurisprudencia/ri-0046473-tjpe-falso-advogado-recebedor-nubank.md). A condenação do Nubank recebedor apoiou-se exatamente no lance de réplica acima (a contestação confessou o uso indevido e o encerramento da conta).
- A capturar: TJSP ApCiv 1081556-32.2022.8.26.0100 (conta aberta sem cumprir a Res. 4.753; R$ 4.900 + R$ 5.000), citado em triagem de perfil público (@jessicaabreuadv); Res. BCB 475/2025 (cria o sistema).
