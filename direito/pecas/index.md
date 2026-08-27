---
okf_version: "0.1"
bundle_version: "0.6.0"
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
- [sucumbencia/](sucumbencia/index.md) — núcleo transversal: decaimento mínimo, bases autônomas e vedação à redução indireta dos honorários abaixo do piso do art. 85, § 2º

## Peças em estoque (fluxo próprio na fila)

- [agravo-de-instrumento/](agravo-de-instrumento/index.md) · [peticao-inicial/](peticao-inicial/index.md) · [contestacao/](contestacao/index.md)

## Seções

- [atividades.md](atividades.md) — roteador: atividade → peça → recursos
- [heuristicas/estrutura-ai-first.md](heuristicas/estrutura-ai-first.md) — **transversal**: estrutura de peça para leitura primária por IA de triagem (BLUF, títulos-conclusão, jurisprudência transcrita, RISTJ 343-A) — TUDO em prosa natural, sem rótulos meta-textuais visíveis (rev. 2026-07-16)
- [log.md](log.md) — histórico de ingestões, lints e alterações
- [`raw/`](raw/index.md) (raiz) — **onde o CPC integral mora, para todo o acervo**, ao lado das obras de terceiros transversais às peças; `recurso-especial/raw/` — fontes específicas do REsp

## Regras deste bundle

1. Conhecimento de peça **não cita matéria**: exemplos usam placeholders ("tese X", "art. Y da lei Z"). A matéria vem do bundle temático na composição.
2. `raw/` mistura dois regimes: **obras comerciais** (manual REsp Perfeito, livros de DPC) são uso interno e não circulam; **texto de lei circula** — não é obra protegida (Lei 9.610/98, art. 8º, IV). Ver o [catálogo](raw/index.md).
3. **Código integral mora aqui uma vez, para todo o acervo.** Bundle que cita artigo isolado recebe recorte gerado por `python recortar-artigo.py <artigo> <bundle>`, nunca cópia do código.
4. Jurisprudência citada aponta fonte oficial (STJ/STF), nunca a obra de terceiro.
5. Antes de ler qualquer `.md` de `raw/`, ler o sidecar `.quality.json` (Etapa 0): `reprovado` não se lê.
