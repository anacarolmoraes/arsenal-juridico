---
type: heuristica
title: Estrutura AI-first de peça processual
description: Como estruturar peças para leitura primária por IA de triagem de gabinete — BLUF, títulos autodescritivos, jurisprudência transcrita com fonte adjacente, seções autossuficientes, TUDO em prosa natural (sem rótulos meta-textuais visíveis). Transversal a todas as peças.
tags: [estrutura, redacao, ai-first, triagem, humanizacao]
timestamp: '2026-07-16'
status: vigente
autor: escritorio
supersede_nota: "Revisão 2026-07-16 (decisão do titular): regras 1, 3 e 4 reescritas — rótulos meta-textuais visíveis, antes prescritos, agora são o próprio sinal de escrita por IA que se quer evitar. A versão 2026-07-09 (com 'Caso em exame.', 'Conclusão do capítulo:' etc. como rótulos em negrito) está superada; peças novas NÃO usam essa forma."
---

# Estrutura AI-first de peça processual

Premissa: quem lê a peça primeiro nos tribunais é, cada vez mais, uma IA de triagem que resume para o assessor humano. Estrutura previsível reduz alucinação do resumo e garante que a conclusão da parte chegue intacta ao gabinete. **Mas a estrutura é invisível**: ela organiza onde a informação mora no texto, não estampa rótulos anunciando cada peça de informação — um rótulo em negrito ("Conclusão do capítulo:", "Impugnação:") é, para o leitor humano (juiz, assessor, cliente), o sinal mais óbvio de que a peça foi escrita por IA, o que esta mesma heurística existe para evitar em outra camada (ver `humanizer-forense`). Validada em execução real de AREsp em 2026-07-08/09; revisada em 2026-07-16 após a peça passar a "parecer robótica" na leitura humana (réplica de um caso real). Compatível com o resumo obrigatório do [RISTJ 343-A](/recurso-especial/jurisprudencia/ristj-art-343a.md) (Emenda 53/2026) para petições ao STJ — o 343-A exige que a petição **contenha** resumo dos fundamentos/pedidos/decisões/dispositivos, não que esse resumo venha sob campos rotulados.

## As sete regras

1. **Síntese de abertura em prosa**, cobrindo o mesmo conteúdo do padrão de ementa CNJ/STJ (caso / questão em discussão / razões / pedido / dispositivos legais invocados), mas **sem os rótulos desse padrão estampados no texto** — os parágrafos abrem diretamente com os fatos, a tese, os pedidos, na ordem em que um advogado humano os apresentaria. No STJ, o mesmo texto cumpre o RISTJ 343-A (o item "dispositivos invocados" é o mais esquecido) — o dever é de conteúdo, não de rótulo.
2. **Títulos autodescritivos que enunciam a conclusão** ("A Súmula X não se aplica ao capítulo Y porque Z"), não rótulos vazios ("Do Direito"). Título funciona como índice no *chunking*: cada pedaço fatiado carrega seu contexto. Isto vale para os títulos de capítulo (nível de sumário) — não para frases dentro do corpo.
3. **Conclusão nas primeiras linhas de cada capítulo** (BLUF — *bottom line up front*): o parágrafo inicial já entrega o resultado pretendido e as 2-3 razões, em prosa corrida — **sem o rótulo** "Conclusão do capítulo:" anunciando isso. Modelos e assessores dão mais peso ao início da seção; o peso vem da posição da informação, não do anúncio dela.
4. **Sequência idêntica em todos os capítulos, dissolvida em prosa** — todo capítulo de impugnação percorre a mesma lógica (o que a decisão/contestação disse → onde a peça anterior já havia suscitado o ponto → a resposta → a jurisprudência que a sustenta), mas cada transição usa conectivo natural, não um rótulo fixo copiado e colado. Tabela de equivalência (rótulo antigo → prosa):

   | Rótulo antigo (NÃO USAR) | Prosa equivalente |
   |---|---|
   | "Caso em exame." / síntese com campos rotulados | Parágrafo abre direto com os fatos |
   | "Conclusão do capítulo:" | Último (ou primeiro) parágrafo do capítulo enuncia a conclusão como frase própria, variada a cada capítulo |
   | "Fundamento impugnado (transcrição literal):" | "A sentença assentou que:" / "Consta da contestação:" / "Diz o julgado:" (variar) + a transcrição |
   | "Impugnação:" | Parágrafo seguinte à transcrição ataca direto, sem anúncio |
   | "Jurisprudência pertinente (transcrição):" | A frase anterior já anuncia a ementa com dois-pontos: "Nesse sentido decidiu o TJ-TO:" / "A 2ª Seção do STJ pacificou:" |

   O parsing previsível continua existindo — mas é estrutural (mesma sequência lógica, mesma posição), não lexical (mesmas palavras em negrito repetidas).
5. **Jurisprudência TRANSCRITA, não só citada**, com identificação completa (número, órgão, relator, data de julgamento/DJe) **colada à citação**, nunca em nota distante. A fonte dentro do contexto é a principal defesa contra alucinação de julgado no resumo. Isto não muda: transcrição + fonte adjacente são conteúdo, não rótulo.
6. **Seções autossuficientes**: proibido "conforme demonstrado acima" — cada capítulo repete em uma linha a premissa de que depende. Resiste a leitura fatiada.
7. **Evitar o que quebra extração de PDF**: tabelas complexas no corpo, excesso de negrito/caixa alta, imagens com texto. (Tabelas vão bem em relatórios internos; no corpo da peça, prosa — sem rótulos e sem excesso de negrito.)

## Armadilhas conhecidas

- **Renumerar capítulos sem reconferir remissões**: a síntese que aponta "(Capítulo III)" quando a impugnação está no IV mina a confiabilidade da peça inteira. Após qualquer renumeração, reconferir TODAS as remissões cruzadas (item de checklist nos playbooks).
- **Citar norma de memória ou de resumo**: alínea trocada em citação de regimento passa despercebida até o gabinete. Toda norma citada: conferir letra por letra contra a página do bundle ou fonte oficial.
- **Datas de julgado**: "DJe" e "data de julgamento" não se confundem — conferir qual é qual antes de transcrever a identificação.

## Relação com as outras camadas

Esta heurística trata da **estrutura lógica**. As demais camadas são independentes e complementares:

- **Superfície da prosa:** a estrutura AI-first não exige travessões, paralelismos negativos, perguntas retóricas nem frases-clone — esses são cacoetes de modelo de linguagem, removíveis sem tocar no esqueleto. Ferramenta: skill do escritório `humanizer-forense` (tabela de substituições + lint quantitativo `lint-ia.js`), etapa obrigatória de validação nos workflows de peça.
- **Tipografia** (fonte, margens, timbrado): padrão visual do escritório.

## Ver também

- [Citar e transcrever como o STJ](citar-e-transcrever-como-o-stj.md) — a forma oficial da referência de julgado, da transcrição com fonte adjacente e dos números, transcrita do Manual de Padronização de Textos do STJ (2024).
- [Como o STJ escreve a ementa](ementa-do-stj-anatomia.md) — a ordem *instituto, ramo, fato, entendimento* que o gabinete lê o dia inteiro e o vocabulário controlado com que a triagem indexa.
