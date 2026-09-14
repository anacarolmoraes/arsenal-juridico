---
type: workflow
title: Workflow — Contestação
description: Sequência executável com portões para redigir uma contestação, compondo técnica (este bundle) com matéria (bundle temático) e espelhando os estágios do legal-orchestrator do escritório.
tags: [contestacao, workflow]
timestamp: '2026-09-04'
status: vigente
autor: escritorio
skills: [legal-orchestrator, legal-writer, legal-consistency-validator, humanizer-forense, peca-pma-builder]
playbook: /contestacao/playbooks/playbook-contestacao.md
---

# Workflow — Contestação

**Escopo:** procedimento comum. Juizado Especial (Lei 9.099, arts. 30 e 31) não é coberto por este workflow; parar e sinalizar.

## Etapa 0 — Três relógios (no dia da citação)

1. **Contestação:** identificar o inciso do [art. 335](/contestacao/jurisprudencia/cpc-arts-335-346.md) que rege o termo inicial (audiência frustrada; protocolo do pedido de cancelamento; art. 231 conforme o modo de citação) e anotar a data fatal em `cronologia.md` do caso (C1). Litisconsórcio passivo: §§ 1º e 2º. A conta dos três relógios sai de `node skills/pesquisa-djen/scripts/prazo-citacao.js --citacao <data> --modo <correio|oficial|escrivao|edital|eletronica|carta> --tribunal <sigla> [--audiencia <data>] [--liminar | --liminar-djen <data>]`; `--cronologia` imprime as linhas para a `cronologia.md` e `--gravar` põe a citação na fila do DJEN (`PENDENTES.md`), que não a enxerga sozinha porque citação em processo novo não é intimação. A data continua sendo conferida no eproc.
2. **Agravo contra a liminar, se houver tutela deferida:** quinze dias da intimação da decisão (art. 1.003, § 5º; art. 1.015, I), que em geral vence antes da contestação. Anotar a data e levar à titular a decisão de agravar na mesma reunião. Pedido de reconsideração não suspende esse prazo.
3. **Desinteresse na audiência de conciliação, se designada:** petição avulsa até dez dias antes da audiência (art. 334, § 5º). Perguntar à titular se quer conciliar, com a exposição da Etapa 2 em mãos se já houver; registrar a decisão na `ANALISE.md`. Se a pasta não diz se a audiência foi designada, perguntar antes de contar.
4. Se houver incompetência relativa ou convenção de arbitragem a alegar **e** audiência de conciliação designada, decidir agora a petição avulsa (armadilha do art. 340, § 3º, no playbook).

## Etapa 1 — Inventário (Estágio 0 do orchestrator)

0. **Declarar o lado** na `ANALISE.md`: `lado: consumidor` (padrão) ou `lado: fornecedor`. Fornecedor é exceção declarada pela titular e avisa que o acervo pode não cobrir as defesas.
1. **Inicial e todos os anexos do autor**, lidos integralmente, PDF convertido antes.
2. **Roteiro de entrevista gerado da inicial** ([heurística](/contestacao/heuristicas/tabela-impugnacao-especificada.md), Parte 0): cada fato da inicial vira pergunta fechada ao cliente com o documento esperado; perguntar também o que a inicial não diz e o réu saberia. O roteiro é camada C1.
3. **Versão do réu com prova**, colhida com o roteiro. "Não sabe" e "não tem o documento" são respostas válidas e viram "falta saber" e protesto por provas. Portão: sem versão do réu não há Etapa 2.
4. **Pasta local e Drive do escritório** pelo nome do cliente e pelo número do processo.
5. **Bundle temático** (`index.md`, `jurisprudencia/`, `teses/`, `heuristicas/`, `casos_decididos/`): as defesas típicas do réu daquela matéria vivem lá, não aqui.

## Etapa 2 — Tabela de impugnação e checklist (portão de arquitetura)

Preencher a [tabela de impugnação especificada](/contestacao/heuristicas/tabela-impugnacao-especificada.md), Partes 1 (fato por episódio), 1-B (exposição por pedido, com resposta principal e subsidiária), 1-C (postura por documento do autor), 2 e 3, como seção 5 da `ANALISE.md` do caso. **Portões:** nenhum fato da inicial sem linha; nenhum pedido sem exposição estimada; nenhum documento do autor sem postura; nenhum inciso do art. 337 sem decisão; posturas acessórias decididas pela titular. **Antes da Etapa 3, levar à titular a soma da exposição e os "não sabe" do roteiro**: são o que decide acordo, reconvenção e peso da peça. A tabela decide também o eixo probatório de cada linha (defesa direta mantém o ônus no autor; fato novo traz o ônus para o réu, art. 373, II), e é aqui que a peça ganha ou perde. Prescrição e decadência (Parte 2, prejudiciais): a escolha da regra e do termo inicial é da titular com página no bundle; a aritmética (interrupção única do art. 202, suspensão da Lei 14.010/2020, retroação da citação à propositura, art. 240, § 1º) sai de `node skills/legal-consistency-validator/scripts/prescricao.js --termo <data> --regra <chave> --distribuicao <data>` (`--regras` lista as chaves; `--md` rascunha o parágrafo da prejudicial).

## Etapa 3 — Estrutura aprovada (Estágio 0.5 do orchestrator)

`<PECA>.estrutura.md` espelhando a tabela: cada linha "nega", "admite com ressalva" e "fato novo" aponta a seção que a absorve; cada "cabe" do checklist vira subseção de preliminar ou prejudicial; "admite" vai para a síntese. Destaque, peso e o que fica de fora, conforme o playbook. Contestação é peça argumentativa livre: **parar e aguardar a aprovação da titular** antes de qualquer prosa.

## Etapa 4 — Composição com a matéria e redação (Estágio 1)

Estrutura do playbook (I. Síntese → II. Preliminares → III. Prejudiciais → IV. Fatos na versão do réu → V. Impugnação especificada → VI. Fatos novos → VII. Mérito → VIII. Pedidos do autor um a um → IX. Reconvenção → X. Provas → XI. Pedidos), capítulos presentes só quando acionados. Regras [AI-first](/heuristicas/estrutura-ai-first.md): BLUF, títulos-tese, jurisprudência transcrita com fonte adjacente, sem rótulos meta-textuais. A prosa vem dos documentos, não do resumo deles: o redator lê o contrato, não a linha da tabela sobre o contrato. **Portão:** tese sem página no bundle temático → sinalizar lacuna à titular, nunca inventar.

## Etapa 5 — Validação (portões bloqueantes)

1. Checklist do playbook (14 itens), todos "sim".
2. Tabela da Etapa 2 espelhada 1:1 na peça: fato ↔ seção, preliminar "cabe" ↔ subseção, pedido do autor ↔ resposta. Havendo reconvenção: causa de pedir própria, pedido certo, valor da causa pelo art. 292 e custas ou gratuidade (requisitos do art. 319).
2-bis. `node skills/legal-consistency-validator/scripts/checar-docs.js <PECA>.md` limpo: todo `Doc. N` citado no rol do frontmatter (`documentos:`), todo item do rol citado, arquivo na pasta. `--rol` imprime o rol para o fim da peça.
3. Citações normativas conferidas letra por letra contra a página do bundle ou a fonte oficial.
4. skill `legal-consistency-validator` sobre a peça, com a `ANALISE.md` e o `<PECA>.estrutura.md` como gabarito; em contestação o validator assume o advogado do autor.
4-bis. **Espelho reverso:** dentro do validator (Fase 5), preencher contra a nossa contestação a [tabela de alegações e resposta](/replica/heuristicas/tabela-alegacoes-resposta.md), Partes 2 a 4, como faria o advogado do autor: fato da inicial silenciado (2-A), pedido não combatido (2-B), confissão, documento nosso contra nós, contradição com o BO ou a notificação, documento invocado sem juntar (Parte 3), postura acessória sem requisito (Parte 4). A tabela preenchida fica no `<PECA>.validacao.md` e é o gabarito para conferir a réplica real quando ela chegar.
5. skill `humanizer-forense` sobre a prosa própria, sem tocar transcrições, **começando pelo capítulo de impugnação especificada**: é o que mais sai em cadência de tabela ("o autor alega X; não procede"). Meta do playbook: três a cinco blocos temáticos, versão do réu como fio, "o autor alega" e "não procede" no máximo uma vez cada.
6. **Banca (a pedido da titular ou caso de alto valor):** skill `banca-revisora`, lente do autor: cada fato recebeu impugnação específica ou ficou incontroverso por omissão?

## Etapa 6 — Entrega

`peca-pma-builder` (md2docx com portões) + relatório de fontes + tabela de impugnação anexada ao dossiê do caso (C1). Agendar em `cronologia.md`: réplica do autor (arts. 350 e 351, 15 dias, se houver preliminar, fato novo ou documento) e saneamento (art. 357), onde a especificação de provas da Etapa 4 e a questão do ônus serão decididas.
