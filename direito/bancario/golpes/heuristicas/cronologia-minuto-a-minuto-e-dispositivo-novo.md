---
type: heuristica
title: Cronologia minuto a minuto do golpe e dois parâmetros de perfil que faltavam — dispositivo novo e cadastro alterado
description: A seção de fatos da inicial traz a sequência com hora (ligação → link → app → Pix 1 → Pix 2 → percepção → aviso), cada linha com Doc., e o relatório de perfil acrescenta aos seis parâmetros do REsp 2.222.059 dois sinais que o banco vê antes de liberar: dispositivo nunca usado e alteração recente de cadastro (telefone, e-mail, limite, chave). Velocidade e novidade são o retrato da fraude.
tags: [golpe-pix, cronologia, perfil-de-consumo, dispositivo, analise-perfil, peticao-inicial, atendimento]
timestamp: '2026-10-20'
status: em_teste
autor: escritorio
peca: peticao-inicial
momento: [atendimento, inicial, replica]
casos_origem: []
fundamentos:
  - /jurisprudencia/resp-2222059-sp-falsa-central-perfil-consumo.md
  - /jurisprudencia/apciv-1007466-tjsp-osasco-mercado-pago-bradesco-dano-moral.md
---

# Cronologia minuto a minuto e dispositivo novo

**Regra:** o relato "fui enganado" não entra na peça; entra a sequência com hora. E o relatório de perfil (skill `analise-perfil` do motor) confere, além de valor, horário, frequência, destinatário, canal e geolocalização, **o dispositivo** e **as alterações de cadastro** nos dias anteriores.

## A cronologia

Colhida na primeira reunião (ver [matriz de documentos](matriz-documentos-golpe-bancario.md)), com o cliente reconstruindo do começo:

```
10h12  ligação de número que exibia o nome do banco      (Doc. 3, print)
10h18  clique no link / instalação do app de acesso       (Doc. 3)
10h25  acesso ao aplicativo em aparelho ___               (log a exibir)
10h31  Pix 1, R$ ___, chave ___, conta ___ no banco ___   (Doc. 4)
10h34  Pix 2 ...                                          (Doc. 5)
10h50  percepção da fraude
11h03  comunicação ao banco, protocolo ___                (Doc. 6)
```

Ela faz três serviços: fixa a atipicidade (minutos, não dias), liga narrativa a documento e transação ([ficha numérica](matriz-documentos-golpe-bancario.md)), e abre a janela do [MED](med-e-conduta-do-banco-apos-o-aviso.md). Contradição entre relato, BO e extrato aparece aqui, antes do protocolo, e não na contestação. Empréstimo e Pix em sequência são um fato só ([empréstimo seguido de Pix](emprestimo-seguido-de-pix-e-um-fato-so.md)).

## Os dois parâmetros novos

| Sinal | Por que o banco devia ter reagido |
|---|---|
| **dispositivo nunca usado** (aparelho novo, acesso remoto, *device ID* desconhecido) | é o primeiro dado que o sistema antifraude recebe; operação de valor alto em aparelho novo pede fricção (confirmação por outro canal, limite, prazo) |
| **alteração recente de cadastro** (telefone, e-mail, limite diário, chave Pix criada minutos antes) | preparação do golpe visível ao banco; chave criada e usada no mesmo dia aparece no Registrato |

A 12ª Câmara do TJSP reconhece perfil desviado sem laudo quando há valor alto e sequência ([ApCiv 1007466](/jurisprudencia/apciv-1007466-tjsp-osasco-mercado-pago-bradesco-dano-moral.md)); o dispositivo e o cadastro só reforçam. Quando o banco não os traz, pedido de exibição (logs de acesso, *device ID*, IP, histórico de alterações cadastrais).

## Quando NÃO usar

Golpe em etapas de dias (falso advogado com várias "custas"): a cronologia se faz por dia, e a atipicidade se mede pela soma e pela repetição de destinatário novo, não pela velocidade.

## Origem

Triagem de perfil público (@jessicaabreuadv, posts Ddl5lalIP2h, DdmRnysoEve, Dc1IgiooAf7, set/2026). Pendência no motor: acrescentar os dois parâmetros à skill `analise-perfil`.
