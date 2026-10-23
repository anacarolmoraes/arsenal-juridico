---
type: legislacao
title: BC Protege+ — consulta prévia obrigatória antes de abrir conta (Res. CMN 5.218/2025, Res. BCB 476/2025, IN BCB 661/2025), desde 1º/12/2025
description: Desde 1º/12/2025, banco e instituição de pagamento têm de consultar o BC Protege+ antes de abrir conta de depósito à vista, poupança ou conta de pagamento pré-paga, e antes de incluir titular ou representante. Abrir contra restrição registrada só em situação excepcional, com decisão documentada e fundamentada; prova da consulta (CPF, produto, instituição, data e hora, resposta, código) guardada por dez anos; sistema fora do ar não autoriza abrir a conta. Contra o recebedor de golpe, é pedido de exibição objetivo e, se a vítima do uso do nome tinha a proteção ativada, falha documental.
tags: [golpe-pix, banco-recebedor, bc-protege, onboarding, kyc, res-cmn-5218, res-cmn-4753, res-bcb-96, in-bcb-661, conta-laranja, identidade-falsa, exibicao-de-documentos]
timestamp: '2026-10-20'
status: vigente
autor: ingerido
resource: https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolução CMN&numero=5218 ; https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Instrução Normativa BCB&numero=661
orgao: Conselho Monetário Nacional / Banco Central do Brasil
data_publicacao: '2025-05-26'
data_vigencia: '2025-12-01'
raw: /raw/res-cmn-5218-2025-bc-protege.md
verificado_em: '2026-10-20'
---

# BC Protege+ — consulta prévia antes de abrir conta

Três normas, um regime, vigente desde **1º/12/2025**:

| Norma | O que faz | Depósito |
|---|---|---|
| Res. CMN 5.218/2025 | inclui o art. 2º-A na Res. CMN 4.753/2019 (conta de depósito à vista e poupança) | [`raw/res-cmn-5218-2025-bc-protege.md`](/raw/res-cmn-5218-2025-bc-protege.md) |
| Res. BCB 476/2025 | inclui o art. 4º-A na Res. BCB 96/2021 (conta de pagamento pré-paga) | texto consolidado na [Res. BCB 96](res-bcb-96-2021-art-4-conta-de-pagamento.md) |
| IN BCB 661/2025 | procedimentos operacionais: o que se consulta, o que se guarda, o que fazer com o sistema fora do ar | [`raw/in-bcb-661-2025-bc-protege.md`](/raw/in-bcb-661-2025-bc-protege.md) |

O sistema em si foi criado pela Res. BCB 475/2025, **não depositada**. Exposição de motivos:
[Voto 24/2025-CMN](/raw/voto-cmn-24-2025-bc-protege.md) (encaminha o Voto 63/2025-BCB). FAQ do
BCB, impresso em 20/10/2026: [`raw/bc-protege-faq-bcb.md`](/raw/bc-protege-faq-bcb.md) (não é
norma; serve para explicar o serviço e orientar o cliente).

## O dever: consultar antes de abrir

> devem consultar o sistema de que trata a Resolução BCB nº 475, de 26 de maio de 2025, previamente à abertura de contas de depósitos à vista e de poupança e à alteração de titulares ou de seus representantes.
> (Resolução CMN 4.753/2019, art. 2º-A, caput, incluído pela Resolução CMN 5.218/2025)

Abrir mesmo com restrição registrada exige decisão "documentada e fundamentada, sendo aplicável
somente em situações excepcionais" (art. 2º-A, § 1º), e a decisão "é de exclusiva
responsabilidade da instituição" (§ 3º).

## A prova que o banco tem de ter

> As instituições devem manter à disposição do Banco Central do Brasil por no mínimo dez anos a documentação comprobatória referente à realização da consulta ao sistema de que trata o *caput*
> (Resolução CMN 4.753/2019, art. 2º-A, § 4º, incluído pela Resolução CMN 5.218/2025)

A IN BCB 661/2025 (art. 6º) diz o que essa documentação contém: a estrutura da consulta (CPF ou
CNPJ consultado; produto, se abertura de conta ou inclusão de titular ou representante;
identificação da instituição; data e hora) e a resposta ("status da permissão para contratação,
se 'sim - permitido' ou 'não - não permitido'", código da consulta, identificação da
requisição). **É a lista do pedido de exibição**, item por item.

## Sistema fora do ar não é desculpa

> Eventual indisponibilidade temporária do BC Protege +, seja por motivo de instabilidade ou manutenção programada, não caracterizará situação excepcional para a abertura da conta ou alteração de titular ou representante
> (Instrução Normativa BCB 661/2025, art. 10)

A instituição deve "postergar a conclusão do processo até o restabelecimento do sistema"
(art. 10, parte final). Conta aberta sem consulta registrada não tem justificativa técnica.

## Pessoa jurídica

A consulta alcança o CNPJ **e** o CPF de todos os titulares e representantes (IN 661, art. 3º,
§ 1º). Golpe com conta recebedora de empresa recém-aberta: pedir a consulta de cada CPF.

## Aplicação

1. **Contra o recebedor**, em conta aberta a partir de 1º/12/2025: pedir a exibição da prova da
   consulta (art. 2º-A, § 4º; IN 661, art. 6º) junto com a jornada de abertura — ver
   [abertura da conta recebedora](../heuristicas/abertura-da-conta-recebedora-sem-validacao.md).
   Consulta inexistente é violação objetiva; consulta com "não - não permitido" seguida de
   abertura sem a decisão fundamentada do § 1º é falha documental grave.
2. **Cliente cujo nome foi usado para abrir a conta-laranja** (vítima de identidade falsa): com
   a proteção ativada, a abertura contra a restrição é o fato central. O FAQ do BCB orienta a gerar
   o "Histórico de ativações" para provar que a proteção estava ativa, e o "Histórico de
   Consultas" mostra qual instituição consultou e quando (FAQ, itens 12 e 14).
3. **Orientação preventiva ao cliente** (pós-golpe ou em atendimento): ativar o Protege+ no Meu
   BC, com conta gov.br prata ou ouro e verificação em duas etapas (FAQ, item 5).

## Limites

- **Alcance:** conta de depósito à vista, poupança e conta de pagamento **pré-paga**, e inclusão de titular ou representante. Não alcança empréstimo, cartão ou conta pós-paga; conta exclusiva de salário ou benefício está fora (FAQ, item 3).
- **Golpe anterior a 1º/12/2025:** não invocar. Usar só o dever geral de validação (Res. CMN 4.753, art. 2º; Res. BCB 96, art. 4º).
- A proteção é **facultativa** para o cidadão: sem restrição registrada, a consulta retorna "permitido" e o argumento volta para a qualidade da validação de identidade, não para o Protege+.
- O FAQ é material de divulgação, datado por item (impresso em 20/10/2026); não é fonte normativa.
