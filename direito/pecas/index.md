---
okf_version: "0.1"
bundle_version: "0.9.0"
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
- [contestacao/](contestacao/index.md) — tabela de impugnação especificada (art. 341: fato sem linha é fato incontroverso), checklist das treze preliminares com decisão registrada (relativa e arbitragem precluem), defesa direta × indireta e o ônus da prova, reconvenção na mesma peça
- [gratuidade/](gratuidade/index.md) — núcleo transversal (semeado 05/09/2026): CPC 98-102 literal, art. 1.072, III (Lei 1.060/50 revogada), **ADC 80** (admissibilidade `vigente` com inteiro teor; mérito de 03/09/2026 `em_teste`: presunção até R$ 5.000,00 de salário, todos os ramos, só ações novas), heurística do pedido em duas formas pela faixa de salário e o repertório do banco contra a gratuidade com refutação item a item
- [sucumbencia/](sucumbencia/index.md) — núcleo transversal: decaimento mínimo, bases autônomas e vedação à redução indireta dos honorários abaixo do piso do art. 85, § 2º
- [peticao-inicial/](peticao-inicial/index.md) — decisões de abertura (rito, foro, tutela, autocomposição), esqueleto único com cinco variáveis, mapa probatório e exibição do art. 397, checklist de saída do 319/320, emenda

## Peças em estoque (fluxo próprio na fila)

- [agravo-de-instrumento/](agravo-de-instrumento/index.md)

## Seções

- [atividades.md](atividades.md) — roteador: atividade → peça → recursos
- [heuristicas/estrutura-ai-first.md](heuristicas/estrutura-ai-first.md) — **transversal**: estrutura de peça para leitura primária por IA de triagem (BLUF, títulos-conclusão, jurisprudência transcrita, RISTJ 343-A) — TUDO em prosa natural, sem rótulos meta-textuais visíveis (rev. 2026-07-16)
- [jurisprudencia/](jurisprudencia/index.md) — legislação e normas transversais a toda peça (hoje: Resolução CNJ 615/2025, governança de IA no Judiciário)
- [heuristicas/refutar-ou-omitir.md](heuristicas/refutar-ou-omitir.md) — **transversal**: argumento do adversário ou é refutado ou não aparece; reconhecer sem refutar ("embora se possa argumentar...") é a postura menos persuasiva das três, abaixo de ignorar; refutar é atacar plausibilidade, raciocínio ou prova, não "pesar mais"; a ordem não tem efeito medido. Base: meta-análise de O'Keefe (1999), em `raw/`
- [heuristicas/citar-e-transcrever-como-o-stj.md](heuristicas/citar-e-transcrever-como-o-stj.md) — **transversal**: a gramática oficial do STJ para referência de julgado (`AgInt no AREsp n. 1.414.332/SP, relatora Ministra..., Segunda Turma, julgado em 4/3/2024, DJe de 7/3/2024`), `n.` e não `nº`, súmula, artigo, transcrição com fonte entre parênteses, cargo flexionado, quantia por extenso. Fonte: Manual de Padronização de Textos do STJ, 3ª ed., 2024, em `raw/`
- [heuristicas/siglas-classes-processuais-stj.md](heuristicas/siglas-classes-processuais-stj.md) — lista oficial das siglas de classe (item 2.13 do manual) e regras de maiúscula, plural e encadeamento; referência para ampliar o detector do `lint-citacoes`
- [heuristicas/ementa-do-stj-anatomia.md](heuristicas/ementa-do-stj-anatomia.md) — como o STJ constrói a ementa e as dez orientações do manual; consequência: ementa não transcreve julgado nem cita precedente, e a ordem dos itens é o mapa do voto
- [heuristicas/linguagem-simples-como-o-stj-escreve.md](heuristicas/linguagem-simples-como-o-stj-escreve.md) — os princípios de linguagem simples que o próprio STJ segue (ordem direta, voz ativa, palavra frequente, uma ideia por frase), transcritos da cartilha da Ouvidoria do STJ
- [heuristicas/decisao-com-apoio-de-ia-o-que-arguir.md](heuristicas/decisao-com-apoio-de-ia-o-que-arguir.md) — o que arguir (falta de exame próprio; perfilamento de testemunha, vedação absoluta) e o que não arguir (uso de IA em si não é nulidade; ausência de aviso no texto da decisão não é dever) diante de decisão com apoio de IA
- [log.md](log.md) — histórico de ingestões, lints e alterações
- [`raw/`](raw/index.md) (raiz) — **onde o CPC integral mora, para todo o acervo**, ao lado das obras de terceiros transversais às peças; `recurso-especial/raw/` — fontes específicas do REsp

## Regras deste bundle

1. Conhecimento de peça **não cita matéria**: exemplos usam placeholders ("tese X", "art. Y da lei Z"). A matéria vem do bundle temático na composição.
2. `raw/` mistura dois regimes: **obras comerciais** (manual REsp Perfeito, livros de DPC) são uso interno e não circulam; **texto de lei circula** — não é obra protegida (Lei 9.610/98, art. 8º, IV). Ver o [catálogo](raw/index.md).
3. **Código integral mora aqui uma vez, para todo o acervo.** Bundle que cita artigo isolado recebe recorte gerado por `python recortar-artigo.py <artigo> <bundle>`, nunca cópia do código.
4. Jurisprudência citada aponta fonte oficial (STJ/STF), nunca a obra de terceiro.
5. Antes de ler qualquer `.md` de `raw/`, ler o sidecar `.quality.json` (Etapa 0): `reprovado` não se lê.
