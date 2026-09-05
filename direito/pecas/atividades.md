---
type: router
title: Roteador de atividades — peças
description: Mapeia cada atividade de peça para o fluxo, o conhecimento obrigatório e o ponto de composição com o bundle de matéria.
timestamp: '2026-07-06'
status: vigente
autor: escritorio
---

# Atividades

## Redigir Recurso Especial

1. **Componha com a matéria:** teses, jurisprudência de mérito e perfil do tribunal vêm do bundle temático do caso (ex.: `direito/bancario/emprestimo-nao-realizado`). Este bundle dá a **técnica**.
2. Leitura obrigatória: [/recurso-especial/playbooks/playbook-recurso-especial.md](recurso-especial/playbooks/playbook-recurso-especial.md)
3. Execute: [/recurso-especial/workflows/recurso-especial.md](recurso-especial/workflows/recurso-especial.md)

## REsp inadmitido na origem — qual recurso?

→ [/recurso-especial/playbooks/mapa-rotas-pos-inadmissao.md](recurso-especial/playbooks/mapa-rotas-pos-inadmissao.md) (AREsp × AgInt × ambos)

## Redigir Agravo em REsp (AREsp)

1. **Componha com a matéria** quando algum óbice exigir mérito (ex.: distinção para Súmula 83) — bundle temático do caso.
2. Leitura obrigatória: [/agravo-em-resp/playbooks/playbook-agravo-em-resp.md](agravo-em-resp/playbooks/playbook-agravo-em-resp.md)
3. Execute: [/agravo-em-resp/workflows/agravo-em-resp.md](agravo-em-resp/workflows/agravo-em-resp.md) — começando pela [tabela de fundamentos da inadmissão](agravo-em-resp/heuristicas/tabela-fundamentos-inadmissao.md) (portão de redação).

## Redigir Agravo Interno

1. **Classifique o papel** (esgotamento de instância / distinguishing do 1.030 §2º / monocrática no STJ) — muda a peça inteira.
2. Leitura obrigatória: [/agravo-interno/playbooks/playbook-agravo-interno.md](agravo-interno/playbooks/playbook-agravo-interno.md) — atenção à armadilha do prazo penal (5 dias, RISTJ 258).
3. Execute: [/agravo-interno/workflows/agravo-interno.md](agravo-interno/workflows/agravo-interno.md)

## Opor Embargos de Declaração

1. **Declare o papel** (corretivo × prequestionador) e confira o prazo: **5 dias úteis cível / 2 dias penal (CPP 619)**.
2. Leitura obrigatória: [/embargos-declaracao/playbooks/playbook-embargos-declaracao.md](embargos-declaracao/playbooks/playbook-embargos-declaracao.md)
3. Execute: [/embargos-declaracao/workflows/embargos-declaracao.md](embargos-declaracao/workflows/embargos-declaracao.md) — começando pela [tabela de vícios](embargos-declaracao/heuristicas/tabela-vicios-prequestionamento.md) (portão: omissão × inovação).

## Pedir ou defender a gratuidade da justiça (qualquer peça)

1. **Portão da data:** ação ajuizada antes ou depois da ata da ADC 80 (09/2026)? Depois: a faixa de salário (R$ 5.000,00) escolhe a forma do pedido.
2. Leitura obrigatória: [/gratuidade/heuristicas/pedido-de-gratuidade-pos-adc-80.md](gratuidade/heuristicas/pedido-de-gratuidade-pos-adc-80.md); forma canônica em `perfil/definicoes.md` §2 do workspace.
3. Impugnação do banco (réplica) ou impugnação nossa (contestação): [/gratuidade/heuristicas/repertorio-do-banco-contra-a-gratuidade.md](gratuidade/heuristicas/repertorio-do-banco-contra-a-gratuidade.md).
4. Indeferimento: agravo do art. 101, sem preparo; Tema 1.178 em [/peticao-inicial/jurisprudencia/resp-1988687-rj-tema-1178-gratuidade.md](peticao-inicial/jurisprudencia/resp-1988687-rj-tema-1178-gratuidade.md); acórdão que cita a Lei 1.060/50 → [/gratuidade/jurisprudencia/cpc-art-1072.md](gratuidade/jurisprudencia/cpc-art-1072.md).

## Redigir Apelação

1. **Inventário primeiro:** [tabela de capítulos e interlocutórias](apelacao/heuristicas/tabela-capitulos-interlocutorias.md) — interlocutória não agravável fora do apelo é preclusão definitiva (1.009, §1º).
2. Leitura obrigatória: [/apelacao/playbooks/playbook-apelacao.md](apelacao/playbooks/playbook-apelacao.md)
3. Execute: [/apelacao/workflows/apelacao.md](apelacao/workflows/apelacao.md) — a geração usa a skill local `apelacao-cirurgica`.

## Redigir Réplica

1. **Mapa da contestação primeiro:** [tabela de alegações e resposta](replica/heuristicas/tabela-alegacoes-resposta.md), Partes 0 a 4 — cinco eixos (preliminar, fato novo, documento, tese jurídica, negativa pura) com o estado da prova do réu, fatos da inicial que a defesa silenciou (art. 341) e pedidos que não combateu (art. 356, I), confissões, documentos do réu contra ele e documentos invocados sem juntar (arts. 389 a 395, 408 e 396 a 400), posturas com prazo próprio (reconvenção, art. 343, § 1º). Só negativa pura e nada colhido: a réplica é dispensável. Antes de responder tese ou fato novo, o [repertório de defesas típicas](replica/heuristicas/repertorio-de-defesas-tipicas.md) do bundle temático.
2. Leitura obrigatória: [/replica/playbooks/playbook-replica.md](replica/playbooks/playbook-replica.md) — regra de ouro contra inovar fato ou pedido (CPC, art. 329, II); argumento de direito novo contra a tese da defesa é permitido.
3. Execute: [/replica/workflows/replica.md](replica/workflows/replica.md)

## Redigir Contestação

1. **Versão do réu com prova, antes de analisar a inicial;** depois a [tabela de impugnação especificada](contestacao/heuristicas/tabela-impugnacao-especificada.md) — nenhum fato da inicial sem linha (art. 341), nenhum inciso do art. 337 sem decisão (relativa e arbitragem precluem).
2. Leitura obrigatória: [/contestacao/playbooks/playbook-contestacao.md](contestacao/playbooks/playbook-contestacao.md) — defesa direta mantém o ônus no autor; fato novo traz o ônus para o réu (art. 373, II).
3. Execute: [/contestacao/workflows/contestacao.md](contestacao/workflows/contestacao.md)

## Redigir Petição Inicial

1. **Decisões de abertura primeiro:** rito ([juizado ou vara comum](peticao-inicial/heuristicas/juizado-ou-vara-comum.md)), foro ([competência e foro](peticao-inicial/heuristicas/competencia-e-foro-na-inicial.md)), tutela ([tutela provisória](peticao-inicial/heuristicas/tutela-provisoria-na-inicial.md)), autocomposição — registradas na `ANALISE.md` do caso.
2. Leitura obrigatória: [/peticao-inicial/playbooks/playbook-peticao-inicial.md](peticao-inicial/playbooks/playbook-peticao-inicial.md) — esqueleto único; a matéria vem do playbook de inicial do bundle temático.
3. Execute: [/peticao-inicial/workflows/peticao-inicial.md](peticao-inicial/workflows/peticao-inicial.md) — espelha o `legal-orchestrator`; estrutura aprovada pela titular antes da prosa.

## Demais peças (estoque — fluxo na fila)

Agravo de Instrumento: tem "o essencial em 5 linhas" e fontes mapeadas no seu `index.md`. Para redigi-lo hoje, use o essencial + o bundle temático + as skills do escritório, e registre no log o que faltou — isso prioriza a fila.
