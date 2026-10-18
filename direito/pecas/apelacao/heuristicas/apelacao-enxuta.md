---
type: heuristica
title: Apelação enxuta — o que sai da peça porque o tribunal já tem, e o que fica porque a lei exige no ato
description: Vista do gabinete, a apelação longa perde o leitor humano e dilui o resumo que a IA de triagem produz. Sai o que já está nos autos (qualificação, capítulo de fatos, tópico de tempestividade e competência, sentença transcrita inteira); fica o que a lei exige provado no ato (preparo, feriado local) e o que o recurso precisa para ser conhecido (trecho atacado, impugnação específica). Partes como apelante e apelado; dispositivo federal no título do capítulo quando houver direito federal, preparando o REsp.
tags: [apelacao, extensao, concisao, ai-first, prequestionamento, titulo-tese, cabimento]
timestamp: '2026-10-18'
verificado_em: '2026-10-18'
status: em_teste
autor: escritorio
peca: apelacao
fundamentos:
  - /apelacao/jurisprudencia/cpc-arts-1009-1010.md
  - /apelacao/heuristicas/extensao-e-profundidade-do-devolutivo.md
---

# Apelação enxuta

**Por que `em_teste`:** regras de redação vindas de prática de gabinete (Osvaci Venâncio Jr.,
ex-assessor de TJ, posts de 17/07, 18/08 e 20/08/2026: `instagram.com/p/Da6RPXNIKNG/`,
`DcMpF_oo46_/`, `DcRzB5oIxkO/`), cruzadas com o playbook e com o `perfil/voz-forense.md` do motor.
Nenhuma delas é norma; duas colidem de frente com o que o escritório já decidiu e estão resolvidas
abaixo a favor da decisão do escritório. Promover depois de a titular ler duas apelações escritas
assim.

## O que o leitor do gabinete já tem

O relator e o assessor leem a sentença antes das razões, e o sistema confere prazo e preparo. Tudo o
que repete isso ocupa espaço e, para a IA que resume a peça, dilui a tese. Sai da apelação:

| Sai | Por quê | O que fica no lugar |
|---|---|---|
| **Qualificação repetida** das partes | Já estão qualificadas desde a inicial (o art. 1.010, I, se cumpre com nome e papel) | Preâmbulo com nome e papel; depois, só **apelante** e **apelado(a)** |
| **Capítulo autônomo "Dos fatos"** | Reconta o que a sentença já contou e obriga o leitor a procurar onde o fato importa | Cada fato entra no capítulo de mérito que depende dele, ao lado do fundamento da sentença que ataca; a síntese situa o caso em um parágrafo |
| **Tópico de tempestividade e de competência** | O sistema confere a data; a distribuição define a competência | Uma frase no cabimento, com o que a lei exige **provado no ato**: preparo (1.007) e feriado local (1.003, § 6º), por documento |
| **Sentença transcrita inteira** ou em blocos longos | Está nos autos, o assessor vai ao original e não confia na cópia | Só o **trecho atacado**, curto, no início do capítulo que o impugna, seguido da impugnação |
| **"Autor", "ré", "demandante"** | Troca o leitor de polo a cada parágrafo | **Apelante** e **apelado(a)**; o papel na origem só quando a confusão de polos exigir (adesivo, litisconsórcio) |

O que **não** sai, porque é condição do conhecimento ou do prequestionamento: a impugnação
específica de cada fundamento da sentença (dialeticidade,
[extensão e profundidade](/apelacao/heuristicas/extensao-e-profundidade-do-devolutivo.md)), as
interlocutórias não agraváveis em preliminar (1.009, § 1º), a posição sobre causa madura e os
dispositivos que o futuro REsp vai exigir.

## Duas colisões resolvidas

1. **"Nada de tópico sobre tempestividade" × portão 2 do playbook.** O post trata de prazo; o
   portão trata de **preparo e feriado local**, que a lei manda comprovar no ato e cuja falta é
   deserção, não intempestividade. Resolução: sem tópico próprio, mas o cabimento tem **uma frase**
   que declara a data da intimação, a data da interposição, o comprovante de preparo (Doc.) e, se
   houver, o feriado local (Doc.). É o portão em uma frase, não a supressão do portão.
2. **"Títulos-frase" × §8.10 do `voz-forense.md`.** O post recomenda título em frase finita ("O
   apelado deve indenizar o apelante"). O escritório decidiu em 15/10/2026 pelo **título-síntese
   nominal** ("Da responsabilidade do apelado pelos danos morais"), com frase finita só quando a
   precisão jurídica exigir. Prevalece o §8.10. O que se aproveita do post é o acréscimo do
   **dispositivo federal entre parênteses** no título do capítulo que discute direito federal:
   "Da restituição em parcela única (art. 53 do CDC e Súmula 543/STJ)". Serve ao prequestionamento
   e sinaliza ao gabinete que a tese tem caminho acima.

## O que o post confirma do playbook

- **Síntese no início**, com o primeiro parágrafo dizendo contra quais capítulos da sentença se
  recorre e os seguintes resumindo as teses: é a síntese estratégica do playbook, lida pelo humano no
  primeiro parágrafo e pela IA nos seguintes.
- **Primeiro parágrafo de cada capítulo diz o que se pretende** ("O apelado deve ser condenado a…,
  porque…"), nunca abre pelo dispositivo ("Segundo o art. 186…"): é o BLUF da heurística AI-first.
- **Apelação com cara de apelação.** Pode-se rediscutir a matéria; não se pode parecer que se
  rediscute. O capítulo que reedita a inicial ou a contestação, sem o trecho da sentença no início,
  é lido como rediscussão e perde atenção.
- **Um tópico por preliminar e por capítulo impugnado**, nem mais nem menos: espelho 1:1 da
  [tabela de capítulos](/apelacao/heuristicas/tabela-capitulos-interlocutorias.md).

## Extensão

Não há teto de páginas para apelação no `lint-extensao` (só EDcl e contrarrazões a EDcl). A decisão
de extensão é da titular, registrada no `<PECA>.estrutura.md` e, quando fixada, em
`orcamento_paginas:` no frontmatter da peça, para ficar no documento. Regra de revisão que vale sem
teto: na releitura, tentar tirar uma palavra de cada frase, uma frase de cada parágrafo e um
parágrafo de cada capítulo; o conectivo de abertura ("todavia", "desse modo", "portanto") é o
primeiro candidato.

## Portão

Antes de compilar: há capítulo "Dos fatos"? Há tópico de tempestividade ou competência? Há bloco da
sentença maior que o trecho atacado? Aparecem "autor" ou "ré" depois do preâmbulo? Algum capítulo
de direito federal está sem o dispositivo no título? Cada "sim" é um corte antes do `humanizer-forense`.

## Remissões

[playbook da apelação](/apelacao/playbooks/playbook-apelacao.md) ·
[tabela de capítulos e interlocutórias](/apelacao/heuristicas/tabela-capitulos-interlocutorias.md) ·
[extensão e profundidade do devolutivo](/apelacao/heuristicas/extensao-e-profundidade-do-devolutivo.md) ·
[estrutura AI-first](/heuristicas/estrutura-ai-first.md) ·
[CPC, arts. 1.009 e 1.010](/apelacao/jurisprudencia/cpc-arts-1009-1010.md)
