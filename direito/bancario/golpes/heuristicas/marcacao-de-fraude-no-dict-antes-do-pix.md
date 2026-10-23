---
type: heuristica
title: Perguntar se a chave recebedora já tinha marcação de fraude no DICT antes do Pix
description: Chave Pix ou CPF/CNPJ do recebedor com marcação de fraude anterior à operação significa que o banco pagador tinha a informação de risco disponível e deixou passar sem alerta, limite, autenticação reforçada ou bloqueio cautelar (regulamento do Pix, arts. 39 e 39-B). A data da marcação decide. Pedido de exibição a ambos os bancos, na inicial.
tags: [golpe-pix, dict, marcacao-de-fraude, notificacao-de-infracao, regulamento-pix, bloqueio-cautelar, exibicao-de-documentos, peticao-inicial, audiencia]
timestamp: '2026-10-20'
status: em_teste
autor: escritorio
peca: peticao-inicial
momento: [inicial, audiencia]
casos_origem: []
fundamentos:
  - /jurisprudencia/apciv-1026252-tjsp-mercado-pago-origem-bradesco-recebedor.md
  - /jurisprudencia/apciv-1007466-tjsp-osasco-mercado-pago-bradesco-dano-moral.md
---

# Marcação de fraude no DICT antes do Pix

**Regra:** antes de aceitar "culpa exclusiva do cliente", o banco responde a uma pergunta: a chave Pix ou o CPF/CNPJ do recebedor já tinha marcação de fraude quando o Pix foi feito?

## Por que favorece a vítima

O DICT (Diretório de Identificadores de Contas Transacionais) guarda, associada à chave e ao usuário, a informação de fundada suspeita de fraude, e essa informação é compartilhada com os participantes quando a chave é consultada. Se a marcação era anterior, o pagador tinha o dado antes de processar a transação. O regulamento do Pix manda rejeitar a transação em caso de fundada suspeita (art. 39) e admite bloqueio cautelar (art. 39-B); os arts. 88 e 89 exigem mecanismos robustos de prevenção. Os quatro artigos estão transcritos nos votos da [ApCiv 1026252](/jurisprudencia/apciv-1026252-tjsp-mercado-pago-origem-bradesco-recebedor.md) (pp. 10–13) e da [ApCiv 1007466](/jurisprudencia/apciv-1007466-tjsp-osasco-mercado-pago-bradesco-dano-moral.md) (pp. 14–16): citar por aí.

Com a marcação anterior provada, a discussão deixa de ser "o sistema era seguro" e passa a ser "o que o banco fez com a informação que tinha": alerta ao pagador, limite, análise adicional, autenticação reforçada, bloqueio. Nada feito é falha concreta, não presunção.

## O que pedir (art. 397, individualizado)

A ambos os bancos: existência de marcação de fraude na chave e no CPF/CNPJ recebedor; data e hora da marcação; notificação de infração relacionada; registros do DICT consultados na operação; alertas de risco gerados; providências de cada instituição; registros do MED. Não pedir "documentos sobre a fraude".

Para IP, dispositivo e horário de acesso ao aplicativo, cumular o pedido do art. 22 do Marco Civil ([Lei 12.965, arts. 10, 13, 15 e 22](../../emprestimo-nao-realizado/jurisprudencia/lei-12965-2014-arts-10-13-15-22.md)), que é a resposta ao "sigilo" do banco; os registros de acesso só ficam guardados 6 meses.

A vítima pode trazer o seu lado desde já: relatório do Registrato (chaves e contas no seu CPF), já previsto na [matriz de documentos](matriz-documentos-golpe-bancario.md).

## Audiência

Ao preposto: "a chave recebedora foi consultada no DICT antes da operação? com que resultado?". Ver [inquirir o preposto](inquirir-o-preposto-do-banco.md).

## Quando NÃO usar

Marcação posterior ao Pix (feita a partir da própria notificação da vítima): não prova conhecimento prévio; serve só à cronologia do MED. Não afirmar na peça que havia marcação sem o documento: o pedido é de exibição, a afirmação vem depois.

## Fontes a depositar antes de promover a `vigente`

- Regulamento do Pix (anexo à Res. BCB 1/2020) e o manual do DICT sobre marcação de fraude e notificação de infração: texto oficial em `raw/`.
- Origem: triagem de perfil público (@jessicaabreuadv, post Dc1g4LCoEfw, 03/09/2026) e `raw/notas-estrategicas-fraudes-bancarias.md` (relatório do DICT).
