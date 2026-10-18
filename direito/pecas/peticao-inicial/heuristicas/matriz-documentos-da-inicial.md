---
type: heuristica
title: Matriz de documentos e roteiro de intake da inicial — o que pedir ao cliente antes de escrever
description: A inicial é a única peça do pipeline sem instrumento de coleta (contestação e réplica geram roteiro de entrevista a partir da peça adversária). Esta heurística deriva do art. 320, do mapa probatório e da causa de emenda mais frequente (gratuidade e documento faltante) a lista do que o cliente traz, com criticidade e o fundamento de cada item, e o roteiro de perguntas que vira a cronologia. Instancia-se na pasta do caso como checklist presente | pendente | dispensado, e alimenta o rol `documentos:` do frontmatter.
tags: [peticao-inicial, intake, documentos, art-320, gratuidade, emenda, lgpd]
timestamp: '2026-09-08'
status: vigente
autor: escritorio
peca: peticao-inicial
fundamentos:
  - /peticao-inicial/jurisprudencia/cpc-arts-319-321-330-331-334.md
  - /peticao-inicial/jurisprudencia/cpc-arts-396-400.md
  - /peticao-inicial/jurisprudencia/resp-1988687-rj-tema-1178-gratuidade.md
---

# Matriz de documentos e roteiro de intake da inicial

O art. 320 diz que a inicial "será instruída com os documentos indispensáveis à propositura da
ação", e o art. 321 dá quinze dias para emendar o que faltou. A mineração dos despachos de emenda
do escritório no DJEN (09/09/2026, 80 processos, comunicações desde 2025) encontrou doze
despachos de emenda: **gratuidade em nove, documento faltante em oito** (comprovante de endereço
em nome próprio, extratos de todas as contas, comprovante de rendimentos dos últimos três meses),
valor da causa em dois, qualificação em dois. Quase tudo isso é coleta, não técnica: o documento
existia e não foi pedido ao cliente antes de protocolar.

Esta matriz é **transversal**: vale para qualquer inicial. O bundle temático acrescenta a sua
(exemplo: [matriz de fraude em consignado](../../../bancario/emprestimo-nao-realizado/playbooks/matriz-documentos-fraude-consignado.md);
[matriz de golpe bancário](../../../bancario/golpes/heuristicas/matriz-documentos-golpe-bancario.md)).

## Regra de derivação

1. **O que o art. 320 sempre exige** está na Parte A, para toda inicial.
2. **Cada fato "a produzir" do mapa probatório** (`ANALISE.md`, seção 3) vira uma pergunta ao
   cliente com o documento esperado (Parte B). Se o documento está com o réu, vira pedido de
   exibição do art. 397 na seção de provas, não item de coleta.
3. **Gratuidade** só coleta quando pedida, e na forma que a faixa da ADC 80 exige
   (`perfil/definicoes.md` §2 e [pedido pós-ADC 80](../../gratuidade/heuristicas/pedido-de-gratuidade-pos-adc-80.md)).
4. **Minimização (LGPD):** documento sem tese, heurística ou exigência processual que o lastreie
   não entra na matriz, e não se pede ao cliente.

## Parte A — o que toda inicial junta (art. 320)

| Documento | Criticidade | Por quê |
|---|---|---|
| Procuração | bloqueante | representação (CPC 104); subscritoras de `perfil/advogados.json` |
| Documento de identidade com CPF | bloqueante | qualificação do art. 319, II; idade ≥ 60 aciona prioridade |
| Comprovante de residência **em nome do autor**, recente | bloqueante | qualificação (domicílio e residência) e competência; em nome de terceiro é a causa mais comum de emenda por documento faltante (mineração de 09/09/2026); se for de terceiro, declaração do titular do imóvel junto |
| E-mail do autor confirmado | bloqueante | art. 319, II exige; sem ele o `lint-inicial` reprova |
| Estado civil e existência de união estável | bloqueante | art. 319, II; pergunta direta ao cliente, não se presume |
| Instrumento da relação jurídica (contrato, proposta, cédula, fatura, print da contratação) | alta | causa de pedir; se o autor nega o contrato, a ausência vira exibição do art. 397 |
| Comprovantes de pagamento ou de desembolso (extrato, recibo, boleto pago) | bloqueante quando há número na peça | todo `R$` da peça sai de um documento (ficha numérica); número sem documento não entra |
| Protocolos de reclamação administrativa (número, data, meio, resposta) | alta | narrativa da tentativa prévia e decisão de autocomposição (art. 319, VII); resposta negativa do réu fundamenta o desinteresse |
| Documento que prova cada fato **comprovado** do mapa probatório | bloqueante | fato sem `Doc. N` é fato frágil ou a produzir, e a peça o narra como tal |

## Parte B — gerada do mapa probatório (por caso)

Para cada linha da `ANALISE.md`, seção 3, com estado *frágil* ou *a produzir*, e para cada item
da lista **A esclarecer** da seção 1 (o que só morava ali escapava da matriz: retrofit de
15/10/2026):

| Pergunta ao cliente | Documento esperado | Se não existir |
|---|---|---|
| "Você tem …?" (o que robustece o fato frágil: testemunha com nome e contato, gravação, e-mail, print com data e origem) | o que o cliente indicar | fato continua frágil e a peça o narra como relato |
| "Quem tem …?" (o que prova o fato a produzir) | se o autor: junta; se terceiro: ofício (art. 319, VI, com o meio nomeado); se o réu: exibição (art. 397, I a III) | o pedido de prova vai para a seção VII com o meio nomeado |

O roteiro é curto: uma pergunta por fato, com o documento esperado ao lado. Mais de dez
perguntas é sinal de cronologia mal feita, não de caso complexo.

## Parte C — gratuidade (só quando pedida)

| Faixa (ADC 80, ações ajuizadas após a ata) | Coleta |
|---|---|
| Renda até R$ 5.000,00 | comprovante de renda (contracheque, extrato do benefício, DIRPF ou declaração de isenção); declaração do art. 99, § 3º, na própria peça basta |
| Renda acima de R$ 5.000,00 | além do comprovante de renda: extratos de **todas** as contas dos últimos três meses (o juízo confere pelo Registrato), DIRPF completa, despesas fixas que comprometem a renda (saúde, educação, financiamento) com comprovante |

Nove dos doze despachos de emenda minerados em 09/09/2026 pediam exatamente isso: extratos de
todas as contas e rendimentos dos últimos três meses. Coletar antes é a diferença entre um
protocolo e três.

## Instanciação na pasta do caso

Seção 7 (**Documentos**) da `clientes/<caso>/ANALISE.md`, o único arquivo de estado do caso
(decisão de 01/10/2026: não se cria `DOCUMENTOS.md`), uma linha por item:

```markdown
| Doc. | Descrição | Estado | Arquivo | Fato que prova |
|---|---|---|---|---|
| 1 | Procuração | presente | Doc-01_procuracao.pdf | — |
| 2 | Comprovante de residência em nome próprio | pendente (pedido em 08/09) | — | qualificação |
| 3 | Extrato Banco A, mar/2025 | presente | Doc-03_extrato-a.pdf | transações 1 a 3 |
| — | Print da tela de limite no dia do fato | pendente | — | fato frágil (Parte B) |
```

Os itens `presente` viram o rol `documentos:` do frontmatter da peça (`n`, `descricao`,
`arquivo`), conferido por `checar-docs.js`; o `lint-inicial` reprova peça que cita `Doc. N` sem o
rol. Item **com número** é citado na peça: `pendente` nele é motivo para não protocolar, não para
placeholder. Item **sem número** (`—`) é prova sugerida pela Parte B e fica *a decidir*: juntar,
dispensar com motivo ou deixar para a instrução. `node scripts/caso.js <caso>` mostra os dois
grupos separados.

## Retroalimentação

Toda emenda por documento faltante volta para esta matriz: o documento pedido pelo juízo entra
na Parte A ou na matriz do tema, com a contagem. O script
`skills/pesquisa-djen/scripts/minerar-emendas.js` do workspace refaz a contagem quando a titular
quiser conferir se a matriz está funcionando.
