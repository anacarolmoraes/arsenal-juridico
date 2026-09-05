---
type: heuristica
title: Como o STJ escreve a ementa — anatomia e dez orientações
description: Cabeçalho em maiúsculas sem verbo, fundamentos numerados na ordem do voto, dispositivo ao fim; ementa não transcreve julgado nem súmula, não cita precedente e usa só o vocabulário controlado do Tribunal. Transcrito do verbete "ementa" do Manual de Padronização de Textos do STJ (3ª ed., 2024). Muda como se lê um acórdão e como se escreve a síntese de uma peça.
tags: [ementa, redacao, stj, leitura-de-acordao, vocabulario, padronizacao]
timestamp: '2026-09-04'
status: vigente
orgao: STJ
raw: /raw/manual-padronizacao-textos-stj-3ed-2024.pdf
verificado_em: '2026-09-04'
autor: ingerido
---

# Como o STJ escreve a ementa

O verbete *ementa* do Manual de Padronização de Textos do STJ (3ª ed., 2024, p. PDF 295-298) descreve a ementa que o Tribunal escreve. O manual adverte que "as informações a seguir apresentadas não são regras, mas orientações", alinhadas às *Diretrizes para a Elaboração de Ementas* do CNJ (2021). Para o escritório o valor é duplo: saber **ler** a ementa de um acórdão do STJ sabendo o que ela contém por construção, e escrever a síntese de abertura da peça de modo que o gabinete a reconheça.

## As três partes (p. PDF 295-296)

1. **Cabeçalho (verbetação)**, em maiúsculas, com o resumo do voto em palavras-chave, na ordem `INSTITUTO JURÍDICO. RAMO DO DIREITO. FATO. ENTENDIMENTO. FATO. ENTENDIMENTO.` Sem verbo: "em vez de NÃO CABE ANÁLISE DE MÉRITO, diz-se ANÁLISE DE MÉRITO. DESCABIMENTO".
2. **Fundamentação**, em períodos numerados (cardinal ou romano maiúsculo, seguido de ponto), correspondendo aos motivos que levaram à conclusão do voto.
3. **Dispositivo**, a conclusão do voto, numerado ou não.

## As dez orientações sobre a fundamentação (p. PDF 296-297)

O manual as enumera assim:

1. Períodos introduzidos por numeração cardinal ou romana maiúscula (`I.`, `II.`).
2. Períodos concisos e precisos, correspondentes aos fundamentos; "todos os fundamentos (não explicações) devem estar nesta parte da ementa".
3. "Não se podem fazer transcrições em ementa, seja de outro julgado, seja de súmula" (com apoio em Ruy Rosado de Aguiar, *Ementas e sua técnica*, 2008, e nas orientações do CNJ).
4. "A ordem dos fundamentos listados deve ser respeitada no desenvolvimento do voto": o primeiro item da ementa é o primeiro fundamento do voto.
5. "Não se usam referências a precedentes na ementa. Basta, se for imprescindível, o uso de 'Precedentes'".
6. Quanto mais genérica a afirmação, melhor para a busca: apresentar teses aplicáveis a casos semelhantes.
7. Uniformidade de tempo verbal, em regra o presente do indicativo.
8. Sem negrito, itálico (salvo estrangeirismo) ou sublinhado.
9. Sem formas vagas entre um item e outro ("anterior", "já citada"); repete-se o termo específico.
10. Sem sinônimos fora do **Vocabulário Jurídico do STJ**: "'petição inicial' não se confunde com 'portal' ou com 'peça vestibular', da mesma maneira que 'embargos de declaração' não pode ser substituído, em ementas, por 'aclaratórios'".

## O que isso muda na leitura de um acórdão

- **Ementa que transcreve outra ementa não é ementa do STJ.** Pela orientação 3, o bloco entre aspas que reproduz julgado ou súmula está no relatório ou no voto, não na ementa. Quando uma citação atribuída "à ementa do REsp X" contém texto de outro tribunal, a atribuição está errada por construção. É a mesma armadilha que o portão de voz do `lint-citacoes` já bloqueia; esta orientação é a razão institucional dela.
- **"Precedentes" sem número é o normal, não um defeito.** Pela orientação 5, a ementa não lista os julgados em que se apoia. Quem precisa dos paradigmas vai ao voto.
- **A ordem da ementa é o mapa do voto.** Pela orientação 4, o item *n* da ementa corresponde ao *n*-ésimo fundamento desenvolvido. Para localizar no inteiro teor o trecho que sustenta uma tese, conta-se a posição dela na ementa.
- **Busca com o termo canônico.** Pela orientação 10, o STJ não escreve "aclaratórios" nem "peça vestibular" em ementa. Consulta ao `radar-jurisprudencia` com esses termos perde resultado; usa-se *embargos de declaração*, *petição inicial*.
- **Cabeçalho sem verbo, tese no presente.** "DESCABIMENTO", "IMPOSSIBILIDADE", "NECESSIDADE" no cabeçalho são a conclusão; a tese propriamente dita está nos itens numerados, no presente do indicativo.

## O que isso muda na peça

A [estrutura AI-first](estrutura-ai-first.md) pede uma síntese de abertura em prosa, sem rótulos, cobrindo caso, questão, razões, pedido e dispositivos. Esta página não a altera. Acrescenta duas coisas:

1. O gabinete lê ementas o dia inteiro na ordem *instituto, ramo, fato, entendimento* e com um fundamento por item. Uma síntese que siga a mesma ordem lógica, mesmo em prosa, é lida mais depressa.
2. O vocabulário da síntese e dos títulos deve ser o do Vocabulário Jurídico do STJ, porque é com ele que a triagem do Tribunal indexa e busca. O manual dá dois exemplos (petição inicial, embargos de declaração); o vocabulário completo não está depositado no acervo.

## Exemplo do manual (p. PDF 297-298)

O manual fecha o verbete com duas ementas-modelo. A segunda, curta, mostra as três partes:

> AGRAVO INTERNO NO AGRAVO EM RECURSO ESPECIAL. PROCESSUAL CIVIL E ADMINISTRATIVO. INTEMPESTIVIDADE DO AGRAVO INTERNO.
> 1. Não se conhece de agravo interno interposto em momento posterior a certidão de trânsito em julgado da decisão monocrática que não conheceu do agravo em recurso especial.
> 2. Agravo interno não conhecido.
> (AgInt no AREsp n. 1.414.332/SP, relatora Ministra Maria Novaes, Segunda Turma, julgado em 4/3/2024, DJe de 7/3/2024.)

Os nomes de ministros nos exemplos do manual são ilustrativos. A fórmula de referência ao fim é a oficial, detalhada em [citar e transcrever como o STJ](citar-e-transcrever-como-o-stj.md).

## Limite desta página

O manual descreve o modelo clássico de ementa do STJ (cabeçalho, fundamentos, dispositivo). O padrão de ementa estruturada por campos que a heurística AI-first menciona como "padrão CNJ/STJ" não consta desta edição do manual e não está depositado no acervo. Enquanto não estiver, esta página é a única fonte oficial sobre ementa em `raw/`.
