---
type: heuristica
title: Argumento do adversário — refutar ou omitir, nunca reconhecer sem refutar
description: Regra transversal para toda peça que responde a argumento contrário (contestação, réplica, apelação, contrarrazões, memoriais) e para a inicial que antecipa defesa. Mencionar o argumento do adversário e não o desmontar é pior do que silenciar; refutar é atacar a plausibilidade, o raciocínio ou a prova do argumento contrário, e não dizer que os próprios pesam mais. A ordem em que a refutação aparece não tem efeito medido. Base empírica: meta-análise de O'Keefe (1999) sobre mensagens de um e de dois lados.
tags: [transversal, refutacao, argumento-contrario, contestacao, replica, apelacao, persuasao]
timestamp: '2026-09-05'
status: vigente
autor: escritorio
fonte: /raw/artigo_how_to_handle_opposing_arguments.md
---

# Argumento do adversário: refutar ou omitir

Toda peça que responde a outra escolhe, para cada argumento do adversário, uma de três posturas. **Ignorar**: não mencionar. **Reconhecer sem refutar**: mencionar e seguir adiante, em geral com a fórmula "embora se possa argumentar que..., o fato é que..." ou "ainda que assim não fosse, os fundamentos aqui expostos prevalecem". **Refutar**: mencionar e desmontar.

A meta-análise de O'Keefe (1999, Communication Yearbook 22, mais de cem estimativas de efeito, com casos judiciais simulados entre os temas) mediu as três em temas não publicitários e chegou a um resultado que a intuição forense costuma inverter:

1. **Refutar é a postura mais persuasiva e a que mais eleva a credibilidade de quem escreve.** Supera ignorar.
2. **Reconhecer sem refutar é a postura menos persuasiva das três.** Fica abaixo de ignorar. O leitor recebe o argumento contrário validado pela própria voz do redator e não recebe resposta.
3. **A ordem não importa.** Refutar antes dos argumentos próprios, depois deles ou entrelaçado não mudou o resultado. O conselho de "não abrir pelo argumento do adversário" não se confirmou.
4. **Escolaridade e posição inicial do leitor não moderam o efeito.** Refutar funciona igual para leitor favorável, neutro ou hostil.

Ressalvas honestas: os efeitos medidos são pequenos, o público dos experimentos é leigo, e o juiz não é o consumidor do experimento. Isso não enfraquece a regra; muda o quadro a favor dela. O juiz lê a peça do adversário de qualquer modo, então em juízo a opção "ignorar" é quase sempre ilusória, e o que sobra é a escolha entre refutar e reconhecer sem refutar. A meta-análise diz qual das duas custa.

## A regra

**Argumento do adversário ou é refutado ou não aparece na peça.** Não existe terceira via. "Não enfrentado porque não agrega" é decisão legítima (a peça de um lado). "Mencionado e deixado em pé" não é decisão: é a postura que perde para as outras duas.

## O que conta como refutar

Refutar é atacar **a plausibilidade** do argumento contrário (ele não descreve o que aconteceu), **o raciocínio** dele (a conclusão não decorre da premissa) ou **a prova** dele (o documento não prova o que se diz que prova, ou há documento em contrário). Refutação vem com fato, documento ou norma, no mesmo parágrafo em que o argumento é mencionado.

Não conta como refutar:

- "Os fundamentos aqui expostos superam qualquer alegação em contrário." Isso é pesar, não refutar.
- "Ainda que assim não fosse, ..." sem antes ter dito por que não é assim. A subsidiariedade é legítima depois da refutação, nunca no lugar dela.
- Transcrever a tese do adversário e responder com jurisprudência genérica que não toca no ponto.
- Adjetivar ("a alegação é absurda", "beira a litigância de má-fé") sem desmontar.

## Onde a regra morde em cada peça

- **Contestação.** O art. 341 já obriga a impugnar cada fato; a regra acrescenta a qualidade da impugnação. A postura "admite com ressalva" da [tabela de impugnação](/contestacao/heuristicas/tabela-impugnacao-especificada.md) só vale quando a ressalva **remove a consequência jurídica** do fato admitido. "É verdade que o réu atrasou, mas..." seguido de nada que afaste a mora é reconhecimento sem refutação, que aqui soma o pior dos dois mundos: o fato fica incontroverso e o redator o validou.
- **Réplica e contrarrazões.** A peça inteira é resposta, então toda preliminar, fato novo ou razão recursal que apareça na réplica tem de sair desmontada. O que não se sabe desmontar não se transcreve "para registro": a [tabela de alegações](/replica/heuristicas/tabela-alegacoes-resposta.md) já manda reavaliar com a titular; a alternativa é o silêncio, não a menção.
- **Apelação e memoriais.** O fundamento da sentença que se ataca é o argumento do adversário. Fundamento mencionado no relatório e não atacado nas razões é reconhecimento sem refutação, e o tribunal o lê como concordância.
- **Inicial.** A antecipação de defesa (o "ataque previsto" da `ANALISE.md`) entra na peça **só com refutação pronta**. Defesa prevista que não se sabe refutar fica fora da inicial; não entra como "ainda que se alegue". A seção que afasta a tese da "transferência para a própria conta" nas iniciais de golpe bancário é o modelo certo: nomeia a defesa e a desmonta com fato e precedente.

## Consequências para o pipeline do escritório

- O `<PECA>.estrutura.md` (Estágio 0.5) já prevê, para cada ataque, "seção X" ou "não enfrentado porque". A segunda opção significa **ausente da peça**, não "mencionado de passagem".
- O `legal-consistency-validator` registra como fraqueza ALTO o argumento contrário mencionado sem refutação no mesmo trecho.
- O `legal-writer` não usa as fórmulas de reconhecimento sem refutação ("embora se possa argumentar", "ainda que se sustente", "não se desconhece que") a menos que o período seguinte desmonte o que foi reconhecido.
- Ordem não é critério: a posição do capítulo que refuta se decide pelo BLUF e pela leitura do juiz, não por medo de dar palco ao adversário.

## Fonte

O'Keefe, D. J. (1999). How to handle opposing arguments in persuasive messages: a meta-analytic review of the effects of one-sided and two-sided messages. *Communication Yearbook*, 22, 209-249. Depositado em `raw/` como obra de terceiro (uso interno); o OCR em duas colunas não permite transcrição literal, e esta página é conhecimento reescrito, não citação.
