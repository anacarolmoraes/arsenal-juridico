---
type: playbook
title: Playbook — apelação contra improcedência em fraude de consignado
description: Estrutura da apelação para reverter sentença de improcedência, com preliminar de cerceamento de defesa pela ausência de perícia grafotécnica e mérito subsidiário.
tags: [apelacao, fraude, consignado, cerceamento-de-defesa]
timestamp: '2026-07-05'
status: vigente
autor: escritorio
peca: apelacao
teses:
  - /teses/onus-prova-assinatura-impugnada.md
  - /teses/responsabilidade-objetiva-fortuito-interno.md
  - /teses/dever-verificacao-identidade-res-4753.md
skills: [legal-orchestrator, peca-pma-builder]
---

# Playbook — Apelação (sentença de improcedência)

## Antes de redigir

Verifique nos autos: a impugnação da assinatura foi feita na inicial **e** reafirmada na impugnação à contestação? Houve perícia grafotécnica? O que o banco juntou além do contrato (histórico, ficha cadastral)? Esses três fatos definem a força da preliminar.

## Estrutura da peça

1. **PRELIMINAR — Nulidade por cerceamento de defesa (o ponto mais forte):**
   - Impugnação expressa da assinatura na inicial e na réplica → ônus da prova da autenticidade era do banco (CPC art. 429, II + Tema 1061, [tese central](/teses/onus-prova-assinatura-impugnada.md));
   - O banco não produziu a perícia; o juízo julgou improcedente sem determiná-la → *error in procedendo*: o consumidor foi punido pela inércia probatória que era do banco;
   - Pedido: anular a sentença e devolver à origem para perícia grafotécnica.
2. **MÉRITO 1 — Falha de verificação (Res. 4.753/2019, art. 2º):** os indícios concretos do caso (documento emitido há décadas, contratação em praça distante do domicílio) demonstram que o banco não se cercou das cautelas exigíveis; limitou-se a juntar o contrato sem histórico da operação nem ficha cadastral ([tese](/teses/dever-verificacao-identidade-res-4753.md)).
3. **MÉRITO 2 — Ausência de vontade:** valor não utilizado / depositado em juízo comprova que o consumidor não tinha ciência nem intenção de contratar ([heurística](/heuristicas/demonstrar-nao-utilizacao-do-valor.md)).
4. **MÉRITO 3 — Responsabilidade objetiva:** fortuito interno (Súmula 479 + Tema 466 + CDC art. 14); o banco não se exime sem provar a lisura da contratação ([tese](/teses/responsabilidade-objetiva-fortuito-interno.md)).
5. **PEDIDOS (cirúrgicos, em cascata):**
   - Acolher a preliminar: anular a sentença e devolver à origem para perícia;
   - Subsidiariamente (causa madura, CPC art. 1.013, § 3º): reformar integralmente — inexistência da relação, danos morais, restituição em dobro;
   - Destinação do valor depositado em juízo (levantamento/devolução ao banco);
   - Honorários recursais.

## Portão obrigatório — Matriz de cobertura da sentença

Peça responsiva rebate **todos** os fundamentos do ato atacado. Antes de finalizar:

1. Extrair da sentença **cada fundamento autônomo** de improcedência (lista numerada).
2. Montar a matriz *fundamento → seção da apelação que o impugna*.
3. **Nenhuma linha pode ficar vazia** — fundamento não impugnado preclui (e em eventual REsp faltará prequestionamento). Se um fundamento não tiver resposta boa, diga isso ao titular em vez de fingir cobertura.
4. A matriz integra o relatório de fontes como anexo.

## Regras de citação e verificabilidade (calibragem do titular, 2026-07-05)

1. **Fundamento central = transcrição literal em bloco**, extraída da seção "Trechos-chave" da página de jurisprudência (ou do `raw/` paginado) — nunca de memória.
2. **Legislação na granularidade máxima** (artigo/parágrafo/inciso/alínea + lei identificada) e cadeia de remissões completa, via seção "Remissões" das páginas.
3. **Toda citação entra no relatório de fontes** com URL oficial, localização no `raw/` (página / folha e-STJ) e nível de confiança.

## Erros a evitar

- Começar pelo mérito: a preliminar de cerceamento é a via de menor resistência — o tribunal anula sem precisar reexaminar prova.
- Pedir só a anulação sem o subsidiário de causa madura — se o tribunal quiser julgar desde logo, a peça precisa ter dado o caminho.
- Repetir a inicial: a apelação ataca os fundamentos **da sentença**, um a um (a matriz de cobertura acima é a prova disso).
- Ignorar o [perfil do órgão julgador](/perfis/index.md) ao calibrar pedidos de quantum.
