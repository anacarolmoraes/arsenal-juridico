---
type: heuristica
title: Repertório de defesas típicas — como cada bundle temático mapeia a contestação-padrão do réu à resposta do acervo
description: A contestação do banco, da loteadora e da plataforma é formulário; a resposta do escritório a cada tese dela já foi escrita em réplicas reais, mas mora na peça do cliente, onde ninguém reaproveita. Esta heurística define o formato da página "repertório de defesas" que cada bundle temático mantém (tese defensiva → resposta → página do acervo → lacuna declarada), quem a escreve (a titular, a partir da experiência, nunca por ingestão da pasta do cliente) e como a tabela de réplica a consome no eixo 4.
tags: [replica, repertorio, defesas-tipicas, tese-juridica, transversal]
timestamp: '2026-09-05'
status: vigente
autor: escritorio
peca: replica
---

# Repertório de defesas típicas

A réplica é a peça mais repetitiva do escritório, porque a peça que ela responde é a mais repetitiva do adversário. Banco digital, loteadora e plataforma contestam por modelo: as mesmas cinco a dez teses, na mesma ordem, com os mesmos documentos. Cada uma dessas teses o escritório já respondeu, com jurisprudência transcrita e conferida, em réplica protocolada. O problema é onde essa resposta mora: na peça do cliente, camada C1, que não pode virar fonte do acervo (AGENTS.md, regra 5) e que ninguém abre na réplica seguinte. O resultado é que cada réplica nasce do zero.

O repertório resolve isso sem violar a regra: a **titular** escreve, a partir do que sabe, uma página por bundle temático que lista a tese defensiva recorrente e a resposta, apontando a página do acervo que a sustenta. Nenhum dado de cliente entra; entra o conhecimento de como se responde.

## Formato da página

Uma página em `heuristicas/` do bundle temático (`bancario/golpes`, `imobiliario`, `digital/plataformas`), `type: heuristica`, `autor: escritorio`, com esta tabela:

| # | O réu alega (tese defensiva, na formulação típica) | Eixo na réplica | O que se responde | Página do acervo que sustenta | Estado |
|---|---|---|---|---|---|
| 1 | | fato novo / tese jurídica / preliminar / documento | | `/bundle/teses/...` ou `/bundle/jurisprudencia/...` | coberto / parcial / **lacuna** |

**Regras da página:**

- **A tese defensiva se escreve como o réu a escreve**, na formulação da contestação-padrão ("a operação foi realizada com senha pessoal e dispositivo cadastrado"), não na nossa paráfrase. Quem lê a contestação nova reconhece a linha na hora.
- **A resposta é a heurística, não a peça.** Duas a quatro frases: o que desmonta a tese (norma, precedente, fato que costuma existir nos autos) e o que não funciona (o argumento que já perdeu). A prosa da réplica sai do bundle e da peça concreta, não desta página.
- **A página do acervo é obrigatória ou o estado é "lacuna".** Resposta sem página é o que a regra dura 3 proíbe de ir para a peça. A coluna de estado é o mapa do que falta ingerir no bundle: cada "lacuna" é uma tarefa de acervo com prioridade dada pela frequência da tese.
- **Frequência e resultado, quando conhecidos.** Uma nota ao fim da tabela ("teses 1, 3 e 5 aparecem em toda contestação de banco digital; a 3 foi rejeitada em duas sentenças do escritório") orienta a ordem de ataque. Sem número de processo, sem nome: só o padrão.
- **Fonte permitida:** a memória da titular, os acórdãos e leis já no acervo, a página de caso decidido que a titular escreveu. **Fonte proibida:** a pasta de qualquer cliente. A regra 5 não tem exceção para "só a tese, sem o nome".
- **Status:** a página nasce `em_teste` (a titular ainda não conferiu cada linha contra o acervo) e vira `vigente` quando toda linha "coberto" tiver a página apontada conferida. Como a página não é citada na peça, o `em_teste` não trava o `md2docx`; trava só a confiança.

## Como a réplica a consome

Na Parte 1 da [tabela de alegações](/replica/heuristicas/tabela-alegacoes-resposta.md), cada linha do eixo 4 (tese jurídica) e do eixo 2 (fato novo) confere primeiro se a alegação está no repertório do bundle. Se está e o estado é "coberto", a coluna "página do bundle que sustenta" já vem preenchida e a Etapa 2 do workflow encurta. Se o estado é "lacuna", a lacuna vai para a estrutura da peça como tal, e a titular decide se ingere agora ou declara na peça que o acervo não cobre. Se a tese não está no repertório, a réplica a responde pelo bundle e, ao fim do caso, a titular acrescenta a linha: é assim que a página cresce.

## Repertórios existentes

- [Banco digital, golpe e fraude](../../../bancario/golpes/heuristicas/repertorio-de-defesas-do-banco.md) (bundle `bancario/golpes`)
- [Loteadora, rescisão de lote](../../../imobiliario/heuristicas/repertorio-de-defesas-da-loteadora.md) (bundle `imobiliario`)
- [Plataforma digital, desmonetização e bloqueio](../../../digital/plataformas/heuristicas/repertorio-de-defesas-da-plataforma.md) (bundle `digital/plataformas`)
- [Banco contra a gratuidade](/gratuidade/heuristicas/repertorio-do-banco-contra-a-gratuidade.md) (transversal, já `vigente`; é o modelo de que os outros partem)

Os três primeiros nasceram em 2026-09-05 como **esqueleto**: as teses defensivas listadas são as que qualquer advogado da área reconhece na contestação-padrão, e a coluna de página aponta o que o acervo já tem. As linhas de resposta e a coluna de estado são da titular; até ela passar por elas, a página vale como mapa de lacunas, não como repertório.
