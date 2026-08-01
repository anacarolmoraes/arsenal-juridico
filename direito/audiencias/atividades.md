---
type: router
title: Roteador de atividades — audiências
description: Mapeia cada situação de audiência (designação, instrução, Juizado, videoconferência, diligência como correspondente) para o conhecimento correspondente.
tags: [roteador, audiencia]
timestamp: '2026-08-01'
status: em_teste
autor: escritorio
---

# Roteador de atividades — audiências

## Foi designada audiência de instrução

- **Gatilhos:** "designaram audiência", "audiência de instrução", "vou ter audiência semana que vem", "preciso preparar audiência"
- **Conhecimento obrigatório:** [playbook de preparação](playbooks/playbook-preparacao-de-audiencia.md), [tabela de pontos controvertidos](heuristicas/tabela-de-pontos-controvertidos.md), [matriz de perguntas](heuristicas/inquirir-testemunha-pela-matriz-de-perguntas.md)
- **Entrada mínima:** inicial, contestação, réplica, decisão de saneamento (se houver), rol de testemunhas, data do ato

## Chegou a contestação

- **Gatilhos:** "juntaram a contestação", "vou fazer a réplica", "o que é fato novo aqui"
- **Conhecimento obrigatório:** [tabela de pontos controvertidos](heuristicas/tabela-de-pontos-controvertidos.md)
- **Por quê agora:** fato novo não impugnado na réplica vira incontroverso; a tabela é o que evita descobrir isso na audiência

## A audiência é no Juizado Especial

- **Gatilhos:** "audiência no juizado", "JEC", "conciliação no juizado", "preposto"
- **Conhecimento obrigatório:** [armadilhas do Juizado](heuristicas/armadilhas-do-juizado-especial.md) + o playbook
- **Portão:** conferir quem tem de comparecer pessoalmente e se a documentação de representação está juntada **antes** do ato

## A audiência é por videoconferência

- **Gatilhos:** "audiência virtual", "videoconferência", "por Teams/Webex", "testemunha não tem internet"
- **Conhecimento obrigatório:** [registrar o incidente na hora](heuristicas/videoconferencia-registrar-o-incidente-na-hora.md)
- **Portão de vigência:** a âncora normativa da fonte está exaurida — conferir Res. CNJ 354/2020 e o ato do tribunal local antes de sustentar a tese em petição

## Vou atuar por conta de outro escritório, ou fui nomeado dativo

- **Gatilhos:** "correspondente", "diligência em outra comarca", "fui nomeado dativo", "posso recusar a nomeação"
- **Conhecimento obrigatório:** [correspondente e dativo](heuristicas/atuar-como-correspondente-ou-dativo.md)

## Audiência de custódia

Não é deste bundle. Há material depositado em [raw/](raw/index.md), **não derivado**: é matéria penal e este bundle é de técnica cível. Tratar como pendência até existir bundle penal.
