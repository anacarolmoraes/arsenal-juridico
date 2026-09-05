# Réplica — fluxo completo

**Fluxo de criação próprio construído em 2026-07-16 e ampliado em 2026-09-05** (fontes: Scarpinella 2024 §9.1-9.2 e §9.4.5, CPC compilado, prática do escritório em réplicas reais; ver log do bundle).

## O essencial em 5 linhas

Não é recurso: é a manifestação do autor nas **providências preliminares** (CPC, arts. 347 a 353), em 15 dias, aberta quando a contestação traz **fato impeditivo, modificativo ou extintivo** (art. 350) ou **preliminares** do art. 337 (art. 351); documento novo da contestação abre a vista do art. 437, §1º junto. Nesses limites, não é espaço para inovar fato ou pedido (art. 329, II), mas argumento de direito novo contra a **tese jurídica da defesa** é permitido e costuma ser o grosso da peça. A réplica também **colhe**: o fato da inicial que a defesa silenciou é incontroverso (art. 341), o pedido que ela não combateu é caso de julgamento parcial (art. 356, I), o fato que ela admitiu ou o documento dela provou é prova do autor (arts. 389 a 395 e 408), e o documento que ela invocou sem juntar vira exibição com presunção (arts. 396 a 400). Toda afirmação do réu se responde primeiro pelo estado da prova dele, depois pelo mérito. Reconvenção abre prazo próprio de contestação (art. 343, § 1º); o saneamento abre cinco dias para ajuste (art. 357, § 1º). Sem preliminar, fato novo, documento, tese ou colheita, a réplica é dispensável: não a transformar em memorial antecipado.

## Fluxo

- **Playbook:** [playbooks/playbook-replica.md](playbooks/playbook-replica.md) — portões de cabimento, prazo paralelo e repertório, os cinco eixos e o estado da prova do réu, a defesa como prova do autor, regra de ouro anti-inovação, estrutura da peça, o que fica armado para depois, checklist de 13 itens
- **Workflow:** [workflows/replica.md](workflows/replica.md) — etapas executáveis com portões, da intimação ao caso decidido
- **Heurística:** [heuristicas/tabela-alegacoes-resposta.md](heuristicas/tabela-alegacoes-resposta.md) — Partes 0 a 4: roteiro de entrevista do autor, eixos com estado da prova do réu, espelho do art. 341 (fatos e pedidos), confissões e documentos invocados sem prova, posturas acessórias com prazo. É a seção 6 da `ANALISE.md` do caso
- **Heurística transversal:** [heuristicas/repertorio-de-defesas-tipicas.md](heuristicas/repertorio-de-defesas-tipicas.md) — formato e regras da página "repertório de defesas" que cada bundle temático mantém (contestação-padrão → resposta → página do acervo → lacuna); aponta os três repertórios existentes (banco, loteadora, plataforma)

## Páginas

- [jurisprudencia/cpc-art-337.md](jurisprudencia/cpc-art-337.md) — as treze preliminares e a resposta técnica por bloco (literal)
- [jurisprudencia/cpc-arts-350-352.md](jurisprudencia/cpc-arts-350-352.md) — fato novo, oitiva sobre preliminares, saneamento de vícios (literal)
- [jurisprudencia/cpc-arts-436-437.md](jurisprudencia/cpc-arts-436-437.md) — impugnação de documentos, as quatro posturas do art. 436 (literal)
- [jurisprudencia/cpc-arts-389-395-408.md](jurisprudencia/cpc-arts-389-395-408.md) — confissão, indivisibilidade e cisão, documento particular contra o signatário (literal)
- [jurisprudencia/cpc-arts-355-357.md](jurisprudencia/cpc-arts-355-357.md) — julgamento antecipado, julgamento parcial do pedido incontroverso, saneamento e o prazo de 5 dias do § 1º (literal)
- Art. 341 (incontrovérsia) e art. 343 (reconvenção): [/contestacao/jurisprudencia/cpc-arts-335-346.md](../contestacao/jurisprudencia/cpc-arts-335-346.md) · exibição de documentos, arts. 396 a 400: [/peticao-inicial/jurisprudencia/cpc-arts-396-400.md](../peticao-inicial/jurisprudencia/cpc-arts-396-400.md) · impugnação à gratuidade: [/gratuidade/](../gratuidade/index.md)
- Sequência processual: providências preliminares → julgamento conforme o estado do processo (arts. 355 a 357) → fase instrutória

## Checklist de saída (Estágio 6 do orchestrator aponta para aqui)

1. Toda preliminar do art. 337 e a impugnação à gratuidade, se houver, com resposta individual.
2. Fatos silenciados ou impugnados só por negativa geral listados com folha e pedido de fixação no saneamento.
3. Pedidos não combatidos com requerimento de julgamento antecipado parcial (art. 356, I e § 2º).
4. Confissões e documentos do réu contra ele transcritos pela folha da contestação; cisão do art. 395 declarada quando há fato novo junto.
5. Documento invocado e não juntado com pedido de exibição (arts. 396 a 400) e presunção do art. 400 requerida.
6. Fato novo do art. 350 com o estado da prova do réu anotado antes da resposta e com a prova ou especificação de prova do autor.
7. Tese jurídica da defesa conferida no repertório do tema e respondida com página do bundle temático, ou lacuna declarada.
8. Postura do art. 436 para cada documento relevante da contestação.
9. Nenhum fato constitutivo ou pedido novo (art. 329, II).
10. Especificação de provas fato a fato; reconvenção, agravo e falsidade com prazo próprio na `cronologia.md`; nota para os cinco dias do art. 357, § 1º.
