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

O esqueleto é o **único do escritório**, em `direito/pecas/peticao-inicial/playbooks/playbook-peticao-inicial.md` (bundle transversal de peças): síntese da lide em BLUF, fatos com `Doc. N`, preliminares de tramitação, tutela, direito por tese, danos, provas com meio nomeado, autocomposição, pedidos, valor da causa. Aqui fica só o que é da matéria:

**Variáveis do esqueleto neste tema:** preliminares = gratuidade (enxuta, pessoa natural) e prioridade se ≥ 60 anos; **tutela logo após os fatos** (o desconto em curso é o destaque e o juízo decide no despacho inicial); capítulo de danos = sim; competência = só se houver cláusula de eleição no contrato impugnado (o autor nega o contrato, então em regra não há); autocomposição = decisão por caso ([heurística em teste](/heuristicas/pedir-audiencia-conciliacao.md) — atenção ao art. 334, § 4º, I: desinteresse só do autor não cancela a audiência).

**O que a narrativa fática deste tema exige:** cliente não tinha intenção de contratar e desconhece a contratação, dito desde o primeiro parágrafo; tentativa administrativa relatada com detalhes; destino do valor (não utilizado / depositado em juízo / jamais recebido); **impugnação expressa da assinatura** (ver [heurística](/heuristicas/impugnar-assinatura-na-inicial.md)) — essa alegação será reafirmada na impugnação à contestação para forçar a perícia. Assinatura impugnada é fato **a produzir** por perícia no mapa probatório, o que afasta o Juizado.

**Fundamentação (um capítulo por tese, na ordem):**
- Inversão do ônus da prova — CDC art. 6º, VIII;
- Responsabilidade objetiva e fortuito interno — CDC art. 14 + Súmula 479 + Tema 466 ([tese](/teses/responsabilidade-objetiva-fortuito-interno.md));
- Ônus da prova da assinatura — CPC art. 429, II + Tema 1061 ([tese central](/teses/onus-prova-assinatura-impugnada.md));
- Violação do dever de verificação — Res. 4.753/2019, art. 2º, com os indícios concretos do caso ([tese](/teses/dever-verificacao-identidade-res-4753.md));
- Boa-fé objetiva, informação e transparência — CDC arts. 6º, III, e 51, IV.

**Provas e pedidos próprios do tema:**
- Tutela de urgência: suspensão imediata dos descontos no benefício, com sugestão de multa diária ([heurística](/heuristicas/sugerir-multa-diaria-na-tutela.md));
- Declaração de inexistência da relação jurídica contratual;
- Danos morais (desconto indevido em verba alimentar de aposentado configura dano moral — precedente no [caso de referência](/casos_decididos/caso-a-consignado-fraudulento.md));
- Danos materiais: restituição **em dobro** dos descontos (condicional — [tese](/teses/devolucao-em-dobro-boa-fe-objetiva.md), atenção à modulação);
- Exibição de documentos com os três incisos do art. 397 preenchidos por categoria: contrato, histórico da operação, ficha cadastral e comprovação das cautelas de verificação; a recusa gera a presunção do art. 400 (acórdão do TJSP sobre exibição depositado no bundle `bancario/juros-abusivos`, `jurisprudencia/apelacao-1027749-tjsp-exibicao-art-400.md`);
- Se houver valor intocado: consignação/depósito judicial do montante.

## Erros a evitar

- Pedir o dobro incondicionalmente sem checar datas dos descontos (modulação do EAREsp 600.663/RS).
- Esquecer a impugnação expressa da assinatura — sem ela não há Tema 1061 nem preliminar futura.
- Narrativa genérica de "fraude" sem os indícios concretos de negligência do banco (documento antigo, praça distante, canal incompatível).
- Inconsistência entre valor da causa, valores dos descontos e pedido de dano material — é o ponto mais atacado em contestação.
