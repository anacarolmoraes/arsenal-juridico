---
type: heuristica
title: Impugnar a cadeia de autenticação da contratação digital, elo por elo, não o PDF
description: Quando o banco alega contratação digital, a impugnação deixa de ser "o autor não reconhece o contrato" e passa a ser "quais elementos objetivos demonstram que foi o autor": autoria, dispositivo, localização, autenticação, consentimento, rastreabilidade. Cada elo que o banco não traz é ônus não cumprido (art. 373, II; Tema 1061). Na inicial, negativa e pedido de exibição; na réplica, elo por elo contra o que veio.
tags: [contratacao-digital, cadeia-de-autenticacao, ip, geolocalizacao, dispositivo, logs, trilha-de-auditoria, onus-da-prova, exibicao-de-documentos, replica]
timestamp: '2026-10-20'
status: em_teste
autor: escritorio
peca: replica
momento: [inicial, replica]
casos_origem: []
fundamentos:
  - /teses/onus-prova-assinatura-impugnada.md
  - /jurisprudencia/cpc-art-429-ii.md
  - /jurisprudencia/res-bacen-4753-2019-art-2.md
  - /jurisprudencia/lei-12965-2014-arts-10-13-15-22.md
---

# Impugnar a cadeia de autenticação, elo por elo

**Regra:** contrato digital se impugna pela cadeia que o produziu. A pergunta da réplica é uma só: *quais elementos objetivos demonstram que foi o autor quem realizou esta contratação?* Depois, divide-se em seis.

| Elo | O que o banco tem de mostrar | Se não mostra |
|---|---|---|
| **autoria** | quem realizou a operação | negativa do autor permanece incontroversa |
| **dispositivo** | modelo, identificador, se era aparelho habitual | contratação de aparelho desconhecido |
| **localização** | IP e geolocalização no momento | cliente em uma cidade, contratação em outra |
| **autenticação** | método (biometria com prova de vida, token, SMS, senha) e telefone/e-mail que recebeu o código | "autenticado" sem dizer como |
| **consentimento** | aceite eletrônico, versão do instrumento aceita, envio do contrato ao cliente | sem ciência das condições não há vontade |
| **rastreabilidade** | logs, data e hora de cada evento, trilha de auditoria, hash e carimbo de tempo | documento sem história |

## Por que favorece a vítima

O banco raramente tem a cadeia completa; costuma ter o PDF, uma selfie e telas do próprio sistema, que são prova unilateral. Impugnada a assinatura (aqui, a autenticação), o ônus da autenticidade é dele ([tese](/teses/onus-prova-assinatura-impugnada.md); [art. 429, II](/jurisprudencia/cpc-art-429-ii.md)), e o dever de validar a identidade é regulatório ([Res. 4.753, art. 2º](/jurisprudencia/res-bacen-4753-2019-art-2.md)). Cada elo ausente é um fundamento autônomo da nulidade.

## Momento

- **Inicial:** negativa expressa da contratação ([impugnar a assinatura já na inicial](impugnar-assinatura-na-inicial.md)) e pedido de exibição por categoria (art. 397, I: "registros de autenticação, dispositivo, IP e geolocalização da contratação de DD/MM"). A recusa gera presunção (art. 400) sobre a contestação que vier. Quando o banco opõe sigilo ou LGPD aos registros de IP e dispositivo, cumular o pedido do **art. 22 do Marco Civil** ([arts. 10, 13, 15 e 22](/jurisprudencia/lei-12965-2014-arts-10-13-15-22.md)): indícios, utilidade e período, em três linhas; a guarda dos registros de acesso é de só 6 meses, então pedir cedo.
- **Réplica:** elo por elo contra o que o banco juntou. Impugnação genérica ("impugna todos os documentos") não produz efeito e deixa fato incontroverso. Ver [conferir a contestação documento por documento](conferir-a-contestacao-documento-por-documento.md) e [hash, biometria e selfie](hash-biometria-e-selfie-nao-provam-autoria.md).
- **Audiência:** "qual registro identifica o dispositivo usado nesta contratação?" ([inquirir o preposto](../../golpes/heuristicas/inquirir-o-preposto-do-banco.md)).

Vale igual para conta aberta em nome da vítima ([abertura sem validação](../../golpes/heuristicas/abertura-da-conta-recebedora-sem-validacao.md)).

## Quando NÃO usar

Contratação presencial com assinatura manuscrita: aí a via é a perícia grafotécnica, não a cadeia. Banco que de fato junta a cadeia completa e coerente: não insistir; mudar para o consentimento informado (o que o cliente entendeu que contratava) ou para o perfil.

## Fontes a depositar antes de promover a `vigente`

Acórdãos citados em triagem de perfil público (@jessicaabreuadv, jul–set/2026), a capturar e conferir: TJPB 0806156-49.2022.8.15.0731 (número lido por OCR; telas sistêmicas insuficientes, Tema 1061); TJBA 8044044-81.2022.8.05.0001 (biometria sem prova de vida; dobro; dano moral R$ 10 mil); TJSP 1022245-39.2024.8.26.0004 (Mercado Pago, selfie diferente da CNH, sem logs).
