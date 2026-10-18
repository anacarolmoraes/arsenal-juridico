---
type: heuristica
title: Ler a sentença contra os autos antes de apelar — cinco passagens, uma tabela e um script
description: A apelação não começa pela sentença, começa pela comparação entre o que a sentença diz e o que os autos mostram. Cinco passagens em ordem (decompor; comparar com as peças; cruzar fundamento e prova; procurar vícios sem presumir erro; defender a sentença como se fosse o apelado), com saída na tabela de capítulos e no mapa de vícios dos EDcl. O script conferir-decisao.js faz a parte mecânica: toda data, valor, percentual, cláusula, documento e nome que a decisão afirma e nenhum documento do caso contém.
tags: [apelacao, sentenca, inventario, error-in-judicando, error-in-procedendo, embargos-declaracao, prova, conferencia]
timestamp: '2026-10-18'
verificado_em: '2026-10-18'
status: em_teste
autor: escritorio
peca: apelacao
fundamentos:
  - /apelacao/heuristicas/tabela-capitulos-interlocutorias.md
  - /apelacao/heuristicas/nulidade-teste-do-processo-alternativo.md
  - /embargos-declaracao/heuristicas/tabela-vicios-prequestionamento.md
---

# Ler a sentença contra os autos

**Por que `em_teste`:** o método vem de prática de prompts (Túlio Silveira, 10/2026,
`instagram.com/p/DeM2G8yBB5a/` e carrosséis vizinhos) reorganizada para o fluxo do escritório; o
script é novo (`scripts/conferir-decisao.js`, 18/10/2026, com teste) e rodou em um caso real. Promover
depois de duas apelações em que a Etapa 1 tenha sido feita assim.

## O erro que o método evita

A reação natural à sentença desfavorável é ler o dispositivo, achar os pontos ruins e "recorrer da
sentença". A apelação que sai daí reedita a inicial. O que o tribunal lê é rediscussão, e o que o
assessor procura, a impugnação específica do fundamento, não está lá.

Dois casos recentes do escritório mostram o outro lado do mesmo erro: uma sentença fixou o IPTU com
texto copiado de outro processo (Maria de Jesus x DF, 10/2026) e outra escreveu 75% onde o pedido
era 25% (Divino x Buena Vista, 10/2026). Nos dois, o defeito estava em uma linha que ninguém conferiu
contra os autos no dia da intimação. Erro de fato e erro material são matéria de EDcl, com prazo de
cinco dias, e são também o melhor flanco da apelação quando o EDcl não os resolve.

## As cinco passagens

Nesta ordem, cada uma com a anterior terminada, e **sem procurar erro antes da quarta**:

1. **Decompor a sentença.** Capítulos do dispositivo, pedido a que cada um responde, resultado para o
   cliente, fundamentos usados em cada capítulo, fatos que a sentença deu por provados, provas que
   valorizou e as que mencionou sem valorar. É a Parte A da
   [tabela de capítulos](/apelacao/heuristicas/tabela-capitulos-interlocutorias.md), colunas
   "capítulo" e "fundamentos a atacar". Ainda não se critica nada.
2. **Comparar com as peças.** Para cada capítulo desfavorável, o que a inicial, a contestação, a
   réplica e as alegações finais alegaram sobre ele, e o que a sentença fez com cada alegação:
   acolheu, rejeitou, enfrentou em parte, **não enfrentou**. Argumento relevante não enfrentado é
   omissão do art. 489, § 1º, IV (EDcl) e, mantida, nulidade por falta de fundamentação na apelação,
   com o [teste do processo alternativo](/apelacao/heuristicas/nulidade-teste-do-processo-alternativo.md)
   a dizer o que esse argumento mudaria.
3. **Cruzar fundamento e prova.** Para cada conclusão de fato da sentença, qual documento ou
   depoimento a sustenta, com evento e página, e qual aponta em sentido contrário ou foi
   **desconsiderado**. Prova desconsiderada é *error in judicando* (reforma) e é também o que
   decide a posição sobre causa madura: processo instruído com prova ignorada pede julgamento
   direto pelo tribunal (1.013, § 3º), não anulação.
4. **Procurar vícios, sem presumir que existam.** Omissão, contradição entre fundamentação e
   dispositivo, obscuridade, erro material, premissa de fato errada, aplicação de norma a fato que
   os autos não mostram. Cada achado vai para o
   [mapa de vícios dos EDcl](/embargos-declaracao/heuristicas/tabela-vicios-prequestionamento.md),
   com a decisão de embargar ou de levar direto à apelação. Aqui entra o script, abaixo.
5. **Defender a sentença.** Escrever, em meia página, as contrarrazões que o apelado vai apresentar:
   que fundamento da sentença resiste, que prova o sustenta, que precedente da Câmara o confirma. A
   apelação tem de responder a essa meia página antes de ser escrita; o que não tiver resposta sai
   da tabela como "não impugnar" ou vira pedido subsidiário.

A saída das cinco passagens é a tabela de capítulos completa (Parte A com as colunas de decisão), o
mapa de vícios quando houver EDcl e, na `ANALISE.md`, a seção de decisões da titular. Só então se
desenha a estrutura da peça.

## O script

```powershell
node scripts\conferir-decisao.js <caso> sentenca.md
node scripts\conferir-decisao.js <caso> sentenca.md --tudo      # lista também o que bateu
node scripts\conferir-decisao.js <caso> sentenca.md --json
```

Extrai da decisão convertida pelo `pdfmd` toda **data, valor em reais, percentual, cláusula,
documento ou evento, número CNJ e nome próprio**, e procura cada um nos demais `.md` da pasta do
caso (`ANALISE.md`, inicial, contestação, contrato, extratos convertidos; ignora `.index.md`,
`.validacao.md`, `.estrutura.md`). O que não aparece em nenhum deles sai como "sem correspondência":
candidato a erro de fato, erro material ou texto de outro processo. Âncoras dentro de citação de
precedente (perto de "julgado em", "DJe", "Rel.", nome de classe) são separadas, porque data de
julgado e nome de ministro não são fatos do caso. Exit 1 quando há âncora do caso sem
correspondência.

Três limites, para não confiar demais: **(a)** só vê o que foi convertido; PDF sem `.md` irmão é
invisível, e a primeira causa de "sem correspondência" é documento não convertido; **(b)** nomes
próprios são heurística de maiúsculas, com filtro de termos institucionais, e pedem leitura; **(c)**
âncora encontrada não significa fato correto, só que o número existe em algum documento, e o que
importa é se existe **no documento certo**. O script substitui a parte mecânica da quarta passagem,
não as outras quatro.

## Portão

Antes do parecer de estratégia recursal (Etapa 1 do workflow): as cinco passagens foram feitas
nesta ordem, com a Parte A da tabela e, havendo vício, o mapa dos EDcl preenchidos? O script rodou
e cada âncora sem correspondência foi conferida no PDF original, com o resultado anotado (erro
confirmado e onde; ou falso positivo e por quê)? A meia página de defesa da sentença existe e cada
capítulo que vai à peça responde a ela?

## Remissões

[tabela de capítulos e interlocutórias](/apelacao/heuristicas/tabela-capitulos-interlocutorias.md) ·
[teste do processo alternativo](/apelacao/heuristicas/nulidade-teste-do-processo-alternativo.md) ·
[mapa de vícios dos EDcl](/embargos-declaracao/heuristicas/tabela-vicios-prequestionamento.md) ·
[extensão e profundidade do devolutivo](/apelacao/heuristicas/extensao-e-profundidade-do-devolutivo.md) ·
[playbook da apelação](/apelacao/playbooks/playbook-apelacao.md)
