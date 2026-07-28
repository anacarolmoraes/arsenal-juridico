---
okf_version: "0.1"
bundle_version: "0.5.0"
---

# Peças Processuais — Bundle Transversal (D12)

Conhecimento de **peça** (como construir cada recurso/petição, independente da matéria). Os bundles temáticos (`direito/bancario/...`) fornecem a dimensão de **matéria**; o roteador compõe: *atividade = peça × matéria*.

## Peças com fluxo completo (executável)

- [recurso-especial/](recurso-especial/index.md) — playbook, workflow, admissibilidade, prequestionamento, súmulas obstativas
- [agravo-em-resp/](agravo-em-resp/index.md) — playbook anti-182, tabela de fundamentos da inadmissão, workflow
- [agravo-interno/](agravo-interno/index.md) — os três papéis, regime da multa, armadilha do prazo penal (5 dias no STJ), workflow
- [embargos-declaracao/](embargos-declaracao/index.md) — os dois papéis (corretivo/prequestionador), anatomia dos 4 vícios, armadilha do prazo penal (2 dias, CPP 619), tabela de vícios
- [apelacao/](apelacao/index.md) — as três cargas, portão anti-preclusão (1.009 §1º), causa madura como decisão expressa, estrutura canônica PMA
- [replica/](replica/index.md) — portão de cabimento (dispensável se só mérito direto), os quatro eixos de resposta (preliminares, fato novo, documentos), regra de ouro anti-inovação (art. 329, II)

## Peças em estoque (fluxo próprio na fila)

- [agravo-de-instrumento/](agravo-de-instrumento/index.md) · [peticao-inicial/](peticao-inicial/index.md) · [contestacao/](contestacao/index.md)

## Seções

- [atividades.md](atividades.md) — roteador: atividade → peça → recursos
- [heuristicas/estrutura-ai-first.md](heuristicas/estrutura-ai-first.md) — **transversal**: estrutura de peça para leitura primária por IA de triagem (BLUF, títulos-conclusão, jurisprudência transcrita, RISTJ 343-A) — TUDO em prosa natural, sem rótulos meta-textuais visíveis (rev. 2026-07-16)
- [log.md](log.md) — histórico de ingestões, lints e alterações
- `raw/` (raiz) — obras de terceiros transversais às peças (livros de processo civil); `recurso-especial/raw/` — fontes específicas do REsp

## Regras deste bundle

1. Conhecimento de peça **não cita matéria**: exemplos usam placeholders ("tese X", "art. Y da lei Z"). A matéria vem do bundle temático na composição.
2. `raw/` contém obras comerciais de terceiros (manual REsp Perfeito; livros de DPC) e normas oficiais — **uso interno; excluído de qualquer distribuição** (schema do bundle, seção 6.6).
3. Jurisprudência citada aponta fonte oficial (STJ/STF), nunca a obra de terceiro.
4. Antes de ler qualquer `.md` de `raw/`, ler o sidecar `.quality.json` (Etapa 0): `reprovado` não se lê.
