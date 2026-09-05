---
type: playbook
title: Playbook — Petição inicial
description: Como construir uma petição inicial no padrão do escritório, independente da matéria — decisões de abertura (rito, foro, tutela, autocomposição), esqueleto único com cinco variáveis declaradas, requisitos do art. 319 por seção, mapa probatório e exibição, pedidos e valor da causa, checklist de saída. Técnica pura; a matéria vem do bundle temático.
tags: [peticao-inicial, esqueleto, art-319, tutela, mapa-probatorio, checklist]
timestamp: '2026-09-04'
status: vigente
autor: escritorio
peca: peticao-inicial
fundamentos:
  - /peticao-inicial/jurisprudencia/cpc-arts-319-321-330-331-334.md
  - /peticao-inicial/jurisprudencia/cpc-arts-300-304-311.md
  - /peticao-inicial/jurisprudencia/cpc-arts-46-53-63.md
  - /peticao-inicial/jurisprudencia/cpc-arts-396-400.md
skills: [legal-orchestrator, legal-writer, legal-consistency-validator, humanizer-forense, peca-pma-builder]
---

# Playbook — Petição inicial

A inicial é a peça que o escritório mais produz e a que fixa tudo o que vem depois: causa de pedir que não se pode inovar (329, II), pedidos que limitam a sentença, valor da causa que dita custas e alçada. O que se decide mal aqui se paga na réplica, na apelação e no REsp. Por isso o esqueleto é um só, as decisões de abertura são declaradas, e a prosa só começa depois que a titular aprovou a estrutura.

Este playbook é **técnica de peça**: não cita matéria. Regime, teses, precedentes e documentos típicos vêm do bundle temático (`direito/<tema>/playbooks/playbook-peticao-inicial-<tema>.md`), que aponta para cá e guarda só o que é da matéria.

## Portões (parar se falhar)

1. **Inventário completo?** Pasta local + Drive + acervo (Estágio 0 do `legal-orchestrator`). Sem contrato, extrato ou documento que sustente os números, não se redige com placeholder.
2. **`ANALISE.md` do caso escrita?** Cronologia com prescrição, teses candidatas do bundle com regime/responsabilidade/ônus, mapa probatório em três estados, ataques previstos. É de onde saem as decisões de abertura abaixo.
3. **Estrutura aprovada?** `<PECA>.estrutura.md` com `aprovada: sim` da titular antes de qualquer prosa (Estágio 0.5). Peça com template segue sem parar e lista só os desvios.
4. **Pretensão prescrita fora dos pedidos?** A cronologia diz. Pretensão prescrita que vira pedido é a primeira coisa que a contestação levanta.

## Decisões de abertura (registradas na `ANALISE.md`, seção 2)

| Decisão | Opções | Onde está a técnica |
|---|---|---|
| Rito | Juizado Especial × vara comum | [juizado ou vara comum](/peticao-inicial/heuristicas/juizado-ou-vara-comum.md) |
| Foro | Domicílio do réu (46) × foro especial (53) × domicílio do consumidor (CDC 101, I); cláusula de eleição a afastar? | [competência e foro](/peticao-inicial/heuristicas/competencia-e-foro-na-inicial.md) |
| Tutela | Nenhuma × urgência (300) × evidência (311) × antecedente (303); posição no esqueleto | [tutela provisória na inicial](/peticao-inicial/heuristicas/tutela-provisoria-na-inicial.md) |
| Autocomposição | Interesse × desinteresse (319, VII; 334, § 5º) | [CPC 334, §§ 4º e 5º](/peticao-inicial/jurisprudencia/cpc-arts-319-321-330-331-334.md) |
| Regime, responsabilidade, ônus | CDC × CC; contratual × extracontratual; 373 × inversão | bundle temático |

## Esqueleto único (cinco variáveis, o resto é fixo)

Ordem canônica do escritório, com as regras da [heurística AI-first](/heuristicas/estrutura-ai-first.md): BLUF, títulos que são teses, jurisprudência transcrita com fonte adjacente, sem rótulo meta-textual visível. Forma (endereçamento, capítulo I, qualificação, assinatura, valor da causa, gratuidade) mora em `perfil/definicoes.md` do workspace; aqui só a arquitetura.

| # | Seção | Fixa ou variável | O que precisa conter | 319 |
|---|---|---|---|---|
| 0 | Endereçamento · qualificação do autor · título da ação · "em face de" e qualificação do réu | fixa | Padrão do §5 das definições; qualificação do inciso II (com e-mail, sem telefone); réu com dado faltante → diligências do § 1º | I, II |
| I | **Da síntese da lide** | fixa | BLUF em um parágrafo denso: quem, o que houve, o número central, o que se pede; antecipa em uma frase a objeção previsível. Abre pelo argumento em destaque da estrutura | III |
| II | **Dos fatos** | fixa | Cronologia da `ANALISE.md`, cada fato com o `Doc. N`; fato *frágil* narrado como o que é; fato *a produzir* anunciado como o que se demonstrará. Conectivo de cronologia ou consequência entre parágrafos | III, VI |
| III | **Preliminares de tramitação** | **variável** | Só as que afirmam algo: gratuidade (pessoa natural, enxuta, §2; presunção relativa e vedação ao indeferimento de plano por critério objetivo, [Tema 1.178](/peticao-inicial/jurisprudencia/resp-1988687-rj-tema-1178-gratuidade.md)), prioridade (idoso), competência e foro (só nas três hipóteses da heurística), rito quando o valor caberia no Juizado | — |
| IV | **Da tutela provisória** | **variável (posição)** | Aqui, logo após os fatos, quando o perigo é o destaque e o juízo decide no despacho inicial. Perigo em reais, meses e impacto; reversibilidade; caução ou dispensa; o artigo no fim | — |
| V | **Do direito** | fixa | Um capítulo por tese escolhida, título-tese, na ordem: fato concreto → o que significa → norma → consequência. Abre pelo regime e pelo ônus decididos na análise. Jurisprudência **transcrita** da página do bundle, fonte colada; sem página, a peça diz que o acervo não cobre | III |
| IV' | **Da tutela provisória** | **variável (posição)** | Aqui, depois do direito, quando a probabilidade depende da tese desenvolvida | — |
| VI | **Dos danos** | **variável** | Só quando há pedido indenizatório. Material itemizado com documento por item; moral pelo [método bifásico](/peticao-inicial/heuristicas/quantificar-dano-moral-metodo-bifasico.md): grupo de casos do tribunal e circunstâncias com prova (perda objetiva, impacto, esforço para resolver, necessidade de litigar), nunca adjetivo. Encargos por verba, com índice, taxa e termo inicial ([juros e correção](/peticao-inicial/heuristicas/juros-e-correcao-na-inicial.md)) | III, IV |
| VII | **Das provas** | fixa | Protesto **com meio nomeado** por fato *a produzir* (testemunha, perícia, ofício); pedido de exibição do art. 397 por documento em poder do réu, três incisos preenchidos | VI |
| VIII | **Da autocomposição** | fixa (conteúdo variável) | Dois períodos: interesse ou desinteresse, conforme a decisão de abertura | VII |
| IX | **Dos pedidos** | fixa | Alíneas, nesta ordem: preliminares de tramitação · tutela · citação · mérito por capítulo, na ordem dos capítulos · subsidiários · inversão do ônus · exibição · custas e honorários. Pedido certo e determinado (322/324); juros, correção e honorários expressos, embora implícitos (322, § 1º) | IV |
| X | **Do valor da causa** | fixa | Pelo inciso do 292 que o objeto da ação atrai (`definicoes.md` §1); coerente com todos os números da peça | V |
| XI | **Fecho** | fixa | Requerimentos finais (intimação exclusiva, 272, § 5º; Juízo 100% Digital se houver); local com data certificada; assinatura do §4 | — |

As cinco variáveis: preliminares (quais), posição da tutela, capítulo de danos (sim ou não), competência (sim ou não), gratuidade (sim ou não). Se a matéria pedir mais de cinco variações, são dois esqueletos, e o segundo mora no bundle temático.

## Mapa probatório na peça

Cada fato da `ANALISE.md` tem um de três estados, e o estado dita o verbo na seção II e o destino na seção VII:

| Estado | Na narrativa | Na seção de provas |
|---|---|---|
| **Comprovado** | Afirmado, com `Doc. N` | Nada além do documento já juntado (320) |
| **Frágil** | Narrado como relato ou indício ("segundo relata", "o print de fl. X indica") | Meio que o robustece (testemunha, ofício), nomeado |
| **A produzir** | Anunciado como o que se demonstrará | Meio nomeado; se a prova está com o réu, pedido de exibição do 397 ([heurística](/peticao-inicial/heuristicas/exibicao-de-documentos-a-partir-do-mapa-probatorio.md)) |

Fato de tese sem prova comprovada nem a produzir é fato que a tese não pode afirmar. Se a tese depende dele, a tese muda.

## Ataques previstos

A `ANALISE.md`, seção 4, lista os três melhores argumentos do réu. A estrutura diz em qual seção cada um é neutralizado, ou por que não se enfrenta (enfrentar objeção que o réu talvez não levante entrega o piso). Na peça, o ataque se responde na seção prevista, em prosa, sem rótulo ("Impugnação:", "Contra-argumento:").

## Depois do protocolo

- **Despacho inicial:** tutela deferida ou não; emenda (321) responde-se em 15 dias pela [heurística de emenda](/peticao-inicial/heuristicas/emenda-da-inicial.md); indeferimento (330) ataca-se por apelação com retratação (331).
- **Retroalimentação:** toda emenda recebida entra no `log.md` deste bundle com a causa em uma linha; causa repetida vira item do checklist com contagem. Decisão que aplique tese do bundle vira `casos_decididos/` no bundle temático.
- **Cadeia:** contestação → [réplica](/replica/index.md) (sem inovar a causa de pedir, 329, II) → sentença → [apelação](/apelacao/index.md).

## Checklist antes de protocolar

O [checklist de saída](/peticao-inicial/index.md) do bundle (319 I–VII, 320, encargos, tutela, requerimentos, forma) é o que o Estágio 6 do `legal-orchestrator` confere. Além dele, quatro testes que o checklist não cobre:

| # | Teste |
|---|---|
| 1 | A síntese da lide abre pelo argumento em destaque aprovado na estrutura, e não por um resumo cronológico? |
| 2 | Cada capítulo do direito corresponde a uma alínea dos pedidos, na mesma ordem, e nenhuma alínea pede o que nenhum capítulo fundamentou? |
| 3 | Nenhum fato *frágil* ou *a produzir* aparece na peça como incontroverso? |
| 4 | Os três ataques previstos foram respondidos onde a estrutura mandou, ou a decisão de não responder está registrada? |
