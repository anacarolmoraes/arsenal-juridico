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

## Redigir Apelação

1. **Inventário primeiro:** [tabela de capítulos e interlocutórias](apelacao/heuristicas/tabela-capitulos-interlocutorias.md) — interlocutória não agravável fora do apelo é preclusão definitiva (1.009, §1º).
2. Leitura obrigatória: [/apelacao/playbooks/playbook-apelacao.md](apelacao/playbooks/playbook-apelacao.md)
3. Execute: [/apelacao/workflows/apelacao.md](apelacao/workflows/apelacao.md) — a geração usa a skill local `apelacao-cirurgica`.

## Redigir Réplica

1. **Portão de cabimento primeiro:** [tabela de alegações e resposta](replica/heuristicas/tabela-alegacoes-resposta.md) — se toda alegação da contestação for mero mérito direto (sem preliminar, fato novo ou documento), a réplica é dispensável.
2. Leitura obrigatória: [/replica/playbooks/playbook-replica.md](replica/playbooks/playbook-replica.md) — atenção à regra de ouro contra inovar a causa de pedir (CPC, art. 329, II).
3. Execute: [/replica/workflows/replica.md](replica/workflows/replica.md)

## Redigir Contestação

1. **Versão do réu com prova, antes de analisar a inicial;** depois a [tabela de impugnação especificada](contestacao/heuristicas/tabela-impugnacao-especificada.md) — nenhum fato da inicial sem linha (art. 341), nenhum inciso do art. 337 sem decisão (relativa e arbitragem precluem).
2. Leitura obrigatória: [/contestacao/playbooks/playbook-contestacao.md](contestacao/playbooks/playbook-contestacao.md) — defesa direta mantém o ônus no autor; fato novo traz o ônus para o réu (art. 373, II).
3. Execute: [/contestacao/workflows/contestacao.md](contestacao/workflows/contestacao.md)

## Demais peças (estoque — fluxo na fila)

Agravo de Instrumento · Petição Inicial: cada uma tem "o essencial em 5 linhas" e fontes mapeadas no seu `index.md`. Para redigir uma delas hoje, use o essencial + o bundle temático + as skills do escritório, e registre no log o que faltou — isso prioriza a fila.
