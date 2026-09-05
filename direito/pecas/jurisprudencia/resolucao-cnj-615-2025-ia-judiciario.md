---
type: legislacao
title: Resolução CNJ 615/2025 — governança de inteligência artificial no Judiciário
description: Vedações absolutas (perfilamento para prever crime ou avaliar credibilidade de testemunho), categorização de risco por finalidade (Anexo), dever de supervisão humana com poder de modificação e a faculdade — não o dever — de revelar o uso de IA no texto da decisão.
tags: [inteligencia-artificial, cnj-615, governanca-ia, sinapses, supervisao-humana, vieses]
timestamp: '2026-09-04'
status: vigente
autor: ingerido
resource: https://atos.cnj.jus.br/atos/atos (Resolução CNJ 615/2025; confirmar URI canônica — não localizada no PDF depositado)
orgao: Conselho Nacional de Justiça
data_publicacao: '2025-03-11'
data_vigencia: '2025-07-09'
raw: /raw/resolucao-cnj-615-2025-ia-judiciario.md
verificado_em: '2026-09-04'
---

# Resolução CNJ 615/2025 — governança de IA no Judiciário

Revoga a Res. CNJ 332/2020 (art. 46). Entrou em vigor **120 dias após a publicação** de 11/03/2025 (art. 47) — **9/07/2025**. Convertida do PDF oficial pelo `pdfmd`; conversão limpa (0 ligadura quebrada, 0 duplicata por OCR de imagem).

## O artigo que mais importa para peça: o que é vedado (art. 10)

São **vedados** ao Poder Judiciário, por risco excessivo aos direitos fundamentais ou à independência do magistrado:

> I - que não possibilitem a revisão humana dos resultados [...] ou que gerem dependência absoluta do usuário em relação ao resultado proposto, sem possibilidade de alteração ou revisão;
> II - que valorem traços da personalidade [...] para fins de avaliar ou prever o cometimento de crimes ou a probabilidade de reiteração delitiva [...] bem como para fins preditivos [...] em matéria trabalhista a partir da formulação de perfis pessoais;
> III - que classifiquem ou ranqueiem pessoas naturais, com base no seu comportamento ou situação social ou ainda em atributos da sua personalidade, **para a avaliação da plausibilidade de seus direitos, méritos judiciais ou testemunhos**; e
> IV - a identificação e a autenticação de padrões biométricos para o reconhecimento de emoções.

O inciso III é o de maior valor argumentativo direto: se um sistema de IA usado por um órgão do Judiciário **atribuir score de credibilidade a uma testemunha** ou ranquear partes por "perfil", isso é vedação absoluta, não mero risco a mitigar — e o §2º do art. 10 manda **descontinuar** a solução assim que constatado.

## Categorização de risco (Anexo) — o que a solução tinha que fazer antes de ser usada

O Anexo separa **alto risco (AR)** de **baixo risco (BR)**. Duas entradas de alto risco tocam diretamente a atividade de peticionar:

> AR2 - aferição da adequação dos meios de prova e a sua valoração nos processos de jurisdição contenciosa, sejam documentais, testemunhais, periciais ou de outras naturezas, especialmente quando tais avaliações possam influenciar diretamente a decisão judicial;
>
> AR4 - formulação de juízos conclusivos sobre a aplicação da norma jurídica ou precedentes a um conjunto determinado de fatos concretos, inclusive para a quantificação ou a qualificação de danos [...]

Solução de alto risco exige avaliação de impacto algorítmico e auditoria contínua (art. 9º, §1º; art. 11, §1º) e cadastro no Sinapses **antes do início do desenvolvimento** (art. 24, §4º).

Do lado de baixo risco, o que a Resolução expressamente **autoriza** como uso rotineiro do gabinete:

> BR4 - produção de textos de apoio para facilitar a confecção de atos judiciais, **desde que a supervisão e a versão final do documento sejam realizadas pelo magistrado** e com base em suas instruções, especialmente as decisões acerca das preliminares e questões de mérito;
>
> BR3 - fornecimento aos magistrados de subsídios [...] **desde que não haja substituição da avaliação humana** e que a solução não realize valorações de cunho moral sobre provas ou sobre perfis e condutas de pessoas.

**O corte entre BR4/BR3 e AR2/AR4 é a substituição do juízo humano**, não o uso de IA em si. Minuta de decisão redigida com apoio de IA e revisada pelo magistrado é BR4 (lícito, rotineiro); decisão em que a IA "valorou a prova" ou "aplicou a norma aos fatos" sem esse exame próprio migra para AR2/AR4 (alto risco, com deveres de auditoria que, se descumpridos, são falha regulatória arguível).

## O dever de supervisão humana (art. 34) e o que ele NÃO exige

> Art. 34. Os sistemas computacionais [...] deverão exigir a supervisão humana e permitir a modificação pelo magistrado competente de qualquer produto gerado pela inteligência artificial, sempre que cabível [...]

Este artigo, lido com o art. 93, IX, da Constituição (toda decisão fundamentada) e o art. 489, §1º, do CPC (o que não é fundamentação), é a base para arguir que uma decisão que **reproduz output de IA sem exame próprio identificável** carece de fundamentação — não porque usou IA (lícito), mas porque não houve o juízo humano que o art. 34 exige que permaneça possível e efetivo.

## A informação ao usuário externo é regrada — e tem um limite que decepciona

> Art. 33. Os usuários externos deverão ser informados [...] sobre a utilização de sistemas baseados em IA nos serviços que lhes forem prestados [...]
> § 3º A comunicação sobre o eventual uso da IA **no texto de decisões judiciais será uma faculdade de seu signatário** [...]

**Não existe dever de o juiz revelar, no corpo da decisão, que usou IA para redigi-la.** A transparência exigida é sistêmica (cadastro público no Sinapses, art. 24-25; avisos gerais sobre os sistemas em uso, art. 33 §§1º-2º e 4º) — não é uma declaração caso a caso. **Não arguir nulidade por "a decisão não revelou o uso de IA"**: essa alegação não tem apoio na própria norma que a estabeleceria.

## Como usar

1. **Antes de alegar nulidade por decisão "gerada por IA"**, verificar se o caso é de mera redação assistida (BR4, lícita) ou se há indício de que a IA valorou prova ou aplicou a norma aos fatos sem exame próprio do magistrado (art. 34 c/c art. 93, IX, CF e art. 489, §1º, CPC) — a segunda hipótese é a que sustenta arguição.
2. **Perfilamento de testemunha ou parte por IA é vedação absoluta** (art. 10, III), não questão de grau de risco. Se detectado, é fundamento autônomo, mais forte que a via da fundamentação.
3. **Não alegar falta de aviso sobre uso de IA na decisão** como nulidade — é faculdade do signatário (art. 33, §3º).
4. **Consultar o Sinapses** (catálogo público de soluções de IA no Judiciário, art. 24-25) quando houver suspeita fundada de uso de sistema de alto risco sem o registro devido — a ausência de cadastro é, em si, descumprimento regulatório a apontar.

## Limite desta página

Esta é a leitura da norma para uso em peça; não há, no acervo, levantamento de qual tribunal já implantou qual sistema, nem jurisprudência aplicando esta Resolução (vigente desde 9/07/2025, recente demais para precedente consolidado). Ver também a heurística irmã: [decisão com apoio de IA — o que arguir e o que não arguir](../heuristicas/decisao-com-apoio-de-ia-o-que-arguir.md).
