---
type: heuristica
title: Tabela de impugnação especificada e checklist de preliminares da contestação
description: Antes de redigir a contestação, varrer a inicial fato a fato (por episódio, não por frase) e decidir, para cada um, a postura do réu e a prova que a sustenta (art. 341); medir a exposição de cada pedido; dar postura a cada documento do autor (art. 436); percorrer as treze preliminares do art. 337 e as posturas acessórias e registrar "cabe" ou "não cabe e por quê"; e gerar, da própria inicial, o roteiro de entrevista do réu. Fato sem linha é fato incontroverso; preliminar sem decisão registrada é preliminar esquecida.
tags: [contestacao, impugnacao-especificada, preliminares, checklist, reconvencao]
timestamp: '2026-09-04'
status: vigente
autor: escritorio
peca: contestacao
---

# Tabela de impugnação especificada e checklist de preliminares

A contestação tem um risco que nenhuma outra peça tem na mesma medida: **o que ela não diz vira verdade** ([art. 341](/contestacao/jurisprudencia/cpc-arts-335-346.md)). A réplica que cala sobre uma preliminar sofre no saneamento; a contestação que cala sobre um fato perde o fato. Por isso a análise da contestação não é "ler a inicial e achar fragilidades". É inventariar cada alegação de fato do autor e decidir o que o réu diz sobre ela, com que prova.

A tabela serve a dois propósitos, na ordem: **inventário** (nenhum fato da inicial fica sem linha) e **arquitetura** (cada linha aponta a seção da peça que a absorve). Ela é a seção 5 da `ANALISE.md` do caso quando a peça é contestação.

**Lado:** antes de qualquer linha, a `ANALISE.md` declara `lado: consumidor` (padrão do escritório) ou `lado: fornecedor`. O lado decide quem pede e quem enfrenta a inversão do ônus (CDC, art. 6º, VIII) e se o acervo tem páginas para as defesas do réu; para `fornecedor`, esperar lacunas e dizê-las.

**Escopo:** procedimento comum do CPC. No Juizado Especial a defesa segue outro regime (Lei 9.099: contestação na audiência, art. 30; pedido contraposto em vez de reconvenção, art. 31) e este fluxo não a cobre.

## Parte 0 — Roteiro de entrevista do réu, gerado da inicial

A versão do réu não se colhe com formulário genérico ("o que aconteceu?"). Colhe-se com perguntas extraídas da inicial: lida a inicial e listados os fatos (Parte 1, colunas 1 a 4, preenchidas só com o lado do autor), cada fato vira uma pergunta ao cliente, com o documento que se espera dele. O roteiro sai antes da reunião e volta dela preenchido; as respostas alimentam as colunas 5 a 7.

| # do fato | Pergunta ao cliente (fechada, sobre o fato, não sobre a tese) | Documento esperado (contrato, extrato, e-mail, log, protocolo, foto) | Resposta | Documento entregue |
|---|---|---|---|---|
| 1 | | | | |

Regras: pergunta por fato, na ordem cronológica, em linguagem do cliente; perguntar também o que a inicial **não** diz e o réu saberia (relação anterior entre as partes, tratativas, pagamentos parciais, notificações); registrar "não sabe" e "não tem o documento" como respostas, porque viram "falta saber" e protesto por provas. Roteiro e respostas são camada C1.

## Parte 1 — Tabela de impugnação especificada

Varrer a inicial **inteira**, parágrafo a parágrafo, extraindo toda alegação de fato (não os argumentos de direito, que não se presumem verdadeiros). Cada fato ganha uma linha, mesmo o que parece irrelevante: a relevância se decide na coluna de postura, não na triagem.

| # | Fato alegado (literal + parágrafo/folha da inicial) | Prova do autor (Doc. e o que ele prova de fato) | Estado da prova do autor | Versão do réu | Prova do réu (Doc. N) | Postura | Seção da contestação |
|---|---|---|---|---|---|---|---|
| 1 | | | comprovado / frágil / sem prova | | | nega / admite / admite com ressalva / fato novo | |

**Granularidade.** Fato é **episódio** (a contratação, a entrega, o pagamento de tal parcela, a negativação), não frase. Uma inicial de trinta páginas rende de dez a vinte linhas, não sessenta; tabela de sessenta linhas é tabela preenchida para acabar, e o juiz não lê fato por frase. Fatos irrelevantes para qualquer pedido e que o réu não contesta (qualificação, foro, existência da relação) vão **em bloco, numa linha só**, postura "admite", seção "síntese". O que não se comprime é fato que sustenta pedido: esse tem linha própria.

**Colunas que decidem:**

- **Estado da prova do autor.** *Comprovado*: documento que prova o fato, não só o menciona. *Frágil*: declaração da própria parte, print sem metadado, documento de terceiro sem assinatura, boletim de ocorrência (que prova a comunicação, não o fato). *Sem prova*: alegação nua. A coluna existe para separar o que se nega com prova própria do que se nega apontando o vazio do autor.
- **Versão do réu.** O que o cliente diz que aconteceu, com a fonte (reunião, e-mail, sistema). Contestação não se escreve só apontando lacuna alheia; o réu conta a própria história. Linha sem versão do réu é linha que ainda não foi perguntada ao cliente.
- **Postura.** *Nega*: o fato não ocorreu ou ocorreu de outro modo (defesa direta). *Admite*: o fato é verdadeiro e não convém negá-lo (negar fato provado custa credibilidade em toda a peça). *Admite com ressalva*: verdadeiro, mas incompleto ou sem a consequência pretendida; a ressalva tem de **remover a consequência jurídica** com fato, documento ou norma, senão é reconhecimento sem refutação, a pior das posturas ([refutar ou omitir](/heuristicas/refutar-ou-omitir.md)). *Fato novo*: o réu aceita o fato e opõe outro, impeditivo, modificativo ou extintivo (defesa indireta, [art. 350](/replica/jurisprudencia/cpc-arts-350-352.md) na perspectiva do autor). **Fato novo desloca o ônus da prova para o réu** (art. 373, II): só se declara com Doc. do réu na coluna anterior, ou com o meio de prova nomeado no protesto.
- **Seção.** Toda linha desemboca numa seção da peça. Linha "admite" sem consequência pode ir para a síntese dos fatos incontroversos, que é seção também.

**Regras de preenchimento:**

- **Nenhum fato sem linha.** O portão é este. Fato da inicial ausente da tabela é fato que a contestação vai deixar passar por incontroverso.
- **Fato ≠ argumento.** "O réu descumpriu o contrato" é conclusão; "o réu não entregou o bem em 30/05" é fato. A tabela recebe o segundo.
- **Coluna de prova aponta folha ou parágrafo, nunca "vide autos".**
- **Contradição interna do autor é linha própria:** quando dois fatos da inicial se excluem, ou o fato contradiz o documento que o autor mesmo juntou, registrar como fato e como postura "nega", com a prova sendo o próprio documento do autor. É a impugnação mais barata e mais forte que existe.
- **Fato que o réu não sabe** (nem a pasta nem o cliente respondem) vai para "falta saber" do `<PECA>.estrutura.md`. Não se nega o que não se sabe, nem se admite por silêncio.

### 1-B — Pedidos do autor e exposição

A contestação responde a pedidos, não só a fatos, e a titular decide acordo, reconvenção e peso da peça pelo risco, não pela indignação. Cada pedido da inicial ganha uma linha:

| Pedido (letra da inicial) | Valor pedido | Fatos que o sustentam (# da Parte 1) | Probabilidade de condenação (alta / média / baixa) e por quê | Exposição ponderada | Resposta principal | Resposta subsidiária (redução, compensação, dedução do já pago, limitação de juros e termo inicial) |
|---|---|---|---|---|---|---|
| a | | | | | | |

Regras: probabilidade se justifica pelo estado da prova (Parte 1, coluna 4) e pela tese do bundle temático, não por impressão; pedido sem valor (obrigação de fazer, declaratório) recebe o custo de cumprir; a soma da coluna de exposição é o número que abre a conversa com o cliente sobre acordo. Toda linha tem resposta subsidiária, mesmo quando a principal é forte: compensação e dedução do já pago não se presumem, pedem-se.

### 1-C — Documentos do autor e postura (art. 436)

A Parte 1 é por fato; a impugnação de documento é por documento, e silêncio tende a valer aceitação.

| Doc. do autor | O que o autor diz que ele prova | Postura (admite / impugna admissibilidade / impugna autenticidade / argui falsidade, art. 430 / impugna o conteúdo) | Argumento específico (genérico não produz efeito, art. 436, parágrafo único) |
|---|---|---|---|
| | | | |

## Parte 2 — Checklist das preliminares (art. 337) e prejudiciais

Percorrer **todas**, mesmo as óbvias, e registrar a decisão. "Não cabe" com motivo é decisão; linha em branco é esquecimento.

| Inciso | Preliminar | Cabe? | Por quê / prova | Preclui se calada? |
|---|---|---|---|---|
| I | Inexistência ou nulidade da citação | | | não (§ 5º), mas comparecer sem arguir supre o vício (art. 239, § 1º) |
| II | Incompetência absoluta | | | não |
| II | Incompetência **relativa** | | | **sim** (§ 5º). Com audiência de conciliação designada, antecipar por petição avulsa (art. 340, § 3º chega tarde) |
| III | Incorreção do valor da causa | | conferir contra o art. 292 e o regime do bundle temático | não, mas a correção é aqui |
| IV | Inépcia da inicial (art. 330, §§ 1º e 2º) | | | não |
| V | Perempção (art. 486, § 3º) | | | não |
| VI | Litispendência | | identidade de partes, causa de pedir e pedido (§ 2º) | não |
| VII | Coisa julgada | | idem, com trânsito | não |
| VIII | Conexão ou continência (arts. 54 a 56) | | | não |
| IX | Incapacidade, defeito de representação, falta de autorização | | procuração, atos constitutivos, art. 73 | não |
| X | Convenção de arbitragem | | cláusula no contrato dos autos | **sim** (§ 6º): calar é renunciar ao juízo arbitral |
| XI | Ilegitimidade (ativa ou passiva) ou falta de interesse | | se passiva e o réu conhece o legitimado, **indicá-lo** (art. 339) | não |
| XII | Falta de caução (arts. 83, 559, 641 § 2º) | | | não |
| XIII | Indevida concessão de gratuidade ao autor | | prova de capacidade (art. 100) | não, mas o momento é este |
| — | Justificativa por não confirmar citação eletrônica (art. 246, § 1º-B) | | | multa do § 1º-C se omitida |

**Prejudiciais de mérito** (não são preliminares; vão depois delas e antes do mérito, porque extinguem a pretensão com resolução de mérito, art. 487, II):

| Prejudicial | Cabe? | Termo inicial, prazo, norma, data-limite | Causa de interrupção ou suspensão alegável pelo autor |
|---|---|---|---|
| Prescrição | | | |
| Decadência | | | |

## Parte 3 — Posturas acessórias do réu

Cada uma é decisão da titular, registrada com "sim", "não" ou "não cabe e por quê":

| Postura | Norma | Decisão | Motivo |
|---|---|---|---|
| Reconvenção (na mesma peça; autônoma, sobrevive à desistência) | art. 343 | | pretensão própria conexa com a ação ou com a defesa? Se sim, é uma inicial embutida: causa de pedir própria, pedido certo, **valor da causa pelo art. 292** (regra de `perfil/definicoes.md`, § 1), custas ou gratuidade (art. 319) |
| Denunciação da lide | art. 125 | | |
| Chamamento ao processo | art. 130 | | |
| Arguição de falsidade de documento do autor | art. 430 | | argumentação específica, nunca genérica (art. 436, parágrafo único) |
| Exibição de documento em poder do autor ou de terceiro | arts. 397 e 401 | | |
| **Depoimento pessoal do autor** | art. 385 | | a prova mais barata e mais esquecida da defesa: qual fato o autor não sustenta pessoalmente sob pena de confissão (art. 385, § 1º)? |
| Gratuidade de justiça para o próprio réu | art. 99 | | |
| Reconhecimento parcial do pedido | art. 487, III, "a" | | reduz honorários (art. 90, § 4º) quando o fato é indefensável |
| Desinteresse na autocomposição | art. 334, § 5º | | decisão de caso, não padrão |
| Especificação de provas | art. 336 | | documental vai junto (art. 434); o resto, nomeado |

## Depois de preencher

1. Toda linha da Parte 1 tem seção. Todo pedido da 1-B tem resposta principal e subsidiária. Todo documento da 1-C tem postura. Toda "cabe" da Parte 2 e todo "sim" da Parte 3 tem seção.
2. Os "admite" formam o bloco de fatos incontroversos da síntese: dizê-los antes que o autor os use.
3. Os "fato novo" com prova do réu são as seções mais fortes da peça; os "fato novo" sem prova vão para o protesto por provas com o meio nomeado, ou saem.
4. Os "nega" cuja única prova é o vazio do autor se agrupam num capítulo de ônus da prova (art. 373, I), sem inflar cada um em seção própria; réu consumidor pede ali a inversão (CDC, art. 6º, VIII) e a exibição do que só o fornecedor tem.
4-bis. A tabela **não vira prosa linha a linha**. O capítulo de impugnação agrupa as linhas em três a cinco blocos temáticos, com a versão do réu como fio; "o autor alega" e "não procede" no máximo uma vez cada no capítulo (playbook, capítulo V).
4-ter. Todo `Doc. N` do réu que a tabela cita vai para o frontmatter da peça em `documentos:` (n, descrição, arquivo) e passa pelo `checar-docs.js` antes da compilação.
5. A soma da exposição (1-B) e os "não sabe" do roteiro (Parte 0) vão para a titular antes da estrutura: são as duas informações que mudam a decisão de acordo e de reconvenção.
6. A tabela vai para a `ANALISE.md` do caso (camada C1) e o `<PECA>.estrutura.md` a espelha seção por seção.
