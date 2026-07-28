---
type: playbook
title: Playbook — petição inicial de fraude em empréstimo consignado
description: Estrutura, checklist e fundamentação obrigatória da inicial de declaratória de inexistência c/c danos morais e materiais por empréstimo consignado não contratado.
tags: [peticao-inicial, fraude, consignado, declaratoria-inexistencia]
timestamp: '2026-07-05'
status: vigente
autor: escritorio
peca: peticao-inicial
teses:
  - /teses/onus-prova-assinatura-impugnada.md
  - /teses/responsabilidade-objetiva-fortuito-interno.md
  - /teses/devolucao-em-dobro-boa-fe-objetiva.md
  - /teses/dever-verificacao-identidade-res-4753.md
skills: [pre-peticionamento, legal-orchestrator, peca-pma-builder]
---

# Playbook — Petição inicial de fraude em consignado

## Antes de redigir

Confirme com o cliente/dossiê: (a) como descobriu o desconto; (b) tentativa administrativa prévia (data, meio, resultado — ver [heurística](/heuristicas/comprovar-tentativa-administrativa-previa.md)); (c) destino do valor creditado (ver [heurística](/heuristicas/demonstrar-nao-utilizacao-do-valor.md)); (d) perfil do cliente (idoso → prioridade do art. 71 do Estatuto da Pessoa Idosa; hipossuficiência → justiça gratuita); (e) datas e valores de **todos** os descontos; (f) **houve correspondente bancário na contratação?** — se sim, decidir a inclusão como corréu pela [tese da solidariedade](/teses/solidariedade-correspondente-bancario.md); (g) dados de subscrição e contatos **sempre** de [/escritorio.md](/escritorio.md); (h) consultar [/perfis/](/perfis/index.md) do órgão julgador provável para calibrar pedidos.

## Regras de citação e verificabilidade (calibragem do titular, 2026-07-05)

1. **Fundamento central = transcrição literal em bloco**, extraída da seção "Trechos-chave" da página de jurisprudência (ou do `raw/` paginado) — nunca de memória. Fundamentos acessórios podem ser citação indireta.
2. **Legislação na granularidade máxima**: artigo, parágrafo, inciso e alínea, com a lei identificada (ex.: "art. 42, parágrafo único, da Lei 8.078/1990"). Se o dispositivo remete a outro artigo — inclusive de outra lei — citar a cadeia completa, usando a seção "Remissões" das páginas (ex.: Tema 1061 → "CPC, arts. 6º, 369 e 429, II").
3. **Toda citação da peça entra no relatório de fontes** (entregável obrigatório do workflow) com URL oficial, localização no `raw/` (página / folha e-STJ) e nível de confiança.

## Estrutura da peça

1. **Preliminares de tramitação:** justiça gratuita (com declaração anexa); prioridade de tramitação se ≥ 60 anos.
2. **Narrativa fática — cirúrgica e detalhada:** cliente não tinha intenção de contratar e desconhece a contratação, dito desde o primeiro parágrafo; tentativa administrativa relatada com detalhes; destino do valor (não utilizado / depositado em juízo / jamais recebido); **impugnação expressa da assinatura** (ver [heurística](/heuristicas/impugnar-assinatura-na-inicial.md)) — essa alegação será reafirmada na impugnação à contestação para forçar a perícia.
3. **Fundamentação jurídica (bloco obrigatório):**
   - Inversão do ônus da prova — CDC art. 6º, VIII;
   - Responsabilidade objetiva e fortuito interno — CDC art. 14 + Súmula 479 + Tema 466 ([tese](/teses/responsabilidade-objetiva-fortuito-interno.md));
   - Ônus da prova da assinatura — CPC art. 429, II + Tema 1061 ([tese central](/teses/onus-prova-assinatura-impugnada.md));
   - Violação do dever de verificação — Res. 4.753/2019, art. 2º, com os indícios concretos do caso ([tese](/teses/dever-verificacao-identidade-res-4753.md));
   - Boa-fé objetiva, informação e transparência — CDC arts. 6º, III, e 51, IV.
4. **Pedidos (todos, nesta lógica):**
   - Tutela de urgência: suspensão imediata dos descontos no benefício, com sugestão de multa diária ([heurística](/heuristicas/sugerir-multa-diaria-na-tutela.md));
   - Opção sobre audiência de conciliação ([heurística em teste](/heuristicas/pedir-audiencia-conciliacao.md) — atenção ao art. 334, § 4º, I: desinteresse só do autor não cancela a audiência);
   - Declaração de inexistência da relação jurídica contratual;
   - Danos morais (desconto indevido em verba alimentar de aposentado configura dano moral — precedente no [caso de referência](/casos_decididos/caso-a-consignado-fraudulento.md));
   - Danos materiais: restituição **em dobro** dos descontos (condicional — [tese](/teses/devolucao-em-dobro-boa-fe-objetiva.md), atenção à modulação);
   - Exibição de documentos: contrato, histórico da operação, ficha cadastral e comprovação das cautelas de verificação;
   - Se houver valor intocado: consignação/depósito judicial do montante.

## Erros a evitar

- Pedir o dobro incondicionalmente sem checar datas dos descontos (modulação do EAREsp 600.663/RS).
- Esquecer a impugnação expressa da assinatura — sem ela não há Tema 1061 nem preliminar futura.
- Narrativa genérica de "fraude" sem os indícios concretos de negligência do banco (documento antigo, praça distante, canal incompatível).
- Inconsistência entre valor da causa, valores dos descontos e pedido de dano material — é o ponto mais atacado em contestação.
