# Apelação — fluxo completo

**Fluxo de criação próprio construído em 2026-07-09** (fontes: Scarpinella 2024 §4 e IURIS vol. 4, raws aprovados — ver log do bundle). O `legal-orchestrator` executa a geração (Estágio 0.5 aponta para o workflow deste bundle); este fluxo é a técnica generalizada que o orienta.

## O essencial em 5 linhas

Cabe contra **sentença** (CPC 1.009, incl. capítulos com matéria do rol do agravo — §3º); 15 dias úteis, **preparo e feriado local comprovados no ato**. Carrega três cargas: as **interlocutórias não agraváveis** (§1º — preliminar do apelo ou contrarrazões, sob pena de preclusão definitiva), as nulidades (*error in procedendo* → decretação) e o mérito (*error in judicando* → reforma) — confundir os dois últimos autoriza não conhecimento (932, III). Efeito suspensivo é a regra (1.012), com as exceções do §1º (tutela provisória na sentença, alimentos etc. → eficácia imediata; pedido *ope judicis* nos §§3º–4º). Causa madura (1.013, §3º) é **dever** do tribunal — a peça declara posição expressa. Sobe sem juízo de admissibilidade na origem (1.010, §3º), salvo efeito regressivo.

## Fluxo

- **Playbook:** [playbooks/playbook-apelacao.md](playbooks/playbook-apelacao.md) — portões, as três cargas, devolutividade estratégica, estrutura canônica PMA, checklist
- **Workflow:** [workflows/apelacao.md](workflows/apelacao.md) — etapas executáveis com portões
- **Heurística:** [heuristicas/tabela-capitulos-interlocutorias.md](heuristicas/tabela-capitulos-interlocutorias.md) — portão anti-preclusão (inventário de capítulos + varredura de interlocutórias) e decisão de recorrer capítulo a capítulo: prejuízo, chance, ganho, risco e rota (apelo próprio / aguardar e aderir / contrarrazões / transitar) (rev. 2026-10-18)
- **Heurística:** [heuristicas/nulidade-teste-do-processo-alternativo.md](heuristicas/nulidade-teste-do-processo-alternativo.md) — preliminar de nulidade só com a cadeia completa (norma → violação → consequência → prejuízo → providência); o prejuízo se demonstra pelo processo que teria acontecido sem o vício (`em_teste`, 2026-10-18)
- **Heurística:** [heuristicas/relator-prevento-pelo-primeiro-recurso.md](heuristicas/relator-prevento-pelo-primeiro-recurso.md) — com agravo anterior, o relator da apelação é conhecido (930, parágrafo único): pesquisar as decisões dele no tema e devolver à coluna "chance" da tabela; vedado o "teste de relatoria" (recurso sem interesse só para revelar o relator) (`em_teste`, 2026-10-18)
- **Heurística:** [heuristicas/apelacao-enxuta.md](heuristicas/apelacao-enxuta.md) — o que sai porque o gabinete já tem (qualificação, capítulo de fatos, tópico de tempestividade, sentença transcrita inteira) e o que fica porque a lei exige no ato (preparo, feriado local); apelante/apelado; dispositivo federal no título-síntese; colisões com o portão 2 e com o §8.10 resolvidas (`em_teste`, 2026-10-18)
- **Heurística:** [heuristicas/intimacao-nula-arguir-no-proprio-ato.md](heuristicas/intimacao-nula-arguir-no-proprio-ato.md) — intimação viciada (272, §§ 2º e 5º) não se resolve com pedido de devolução de prazo: prazo pelo pior cenário, ato completo e nulidade em capítulo preliminar do próprio ato (§ 8º); ponto cego do monitor do DJEN, que busca pela OAB (`em_teste`, 2026-10-18)
- **Heurística (sucumbência):** [/sucumbencia/heuristicas/honorarios-na-apelacao-do-vencido-pedir-ou-calar.md](../sucumbencia/heuristicas/honorarios-na-apelacao-do-vencido-pedir-ou-calar.md) — honorários contra o cliente fora do art. 85, § 2º: fixação fora da lei → calar e guardar EDcl/REsp; percentual baixo dentro da faixa → pedir, condicional e neutro; Temas 1.059 e 1.076 (`em_teste`, acórdãos não depositados)
- **Heurística:** [heuristicas/extensao-e-profundidade-do-devolutivo.md](heuristicas/extensao-e-profundidade-do-devolutivo.md) — o que sobe sem se pedir (1.013, §§1º-2º) e por que ainda assim se articula todo fundamento: dialeticidade e matéria-prima dos embargos (`em_teste`)

## Páginas

- [jurisprudencia/cpc-arts-1009-1010.md](jurisprudencia/cpc-arts-1009-1010.md) — cabimento, resgate das interlocutórias, subida direta (literal)
- [jurisprudencia/cpc-arts-1012-1014.md](jurisprudencia/cpc-arts-1012-1014.md) — efeitos, causa madura, questões novas (literal)
- [jurisprudencia/cpc-art-272.md](jurisprudencia/cpc-art-272.md) — intimação pela publicação; nulidade por falta do nome do advogado (§ 2º) ou desrespeito a intimação exclusiva (§ 5º); arguição em preliminar do próprio ato (§ 8º) e a exceção do § 9º (literal; recorte em `raw/`)
- [jurisprudencia/cpc-art-930.md](jurisprudencia/cpc-art-930.md) — distribuição pelo regimento; prevenção do relator pelo primeiro recurso (literal; recorte em `raw/`)
- [jurisprudencia/ritjto-arts-78-79-distribuicao-prevencao.md](jurisprudencia/ritjto-arts-78-79-distribuicao-prevencao.md) — RITJTO: prevenção pelo "mesmo fato" (§ 8º), relator vencido (§ 9º), desaparecimento da prevenção (§ 12), vacância (art. 79); cala sobre recurso não conhecido (literal; recortes em `raw/`)
- [jurisprudencia/cpc-arts-277-278-282-283-nulidades.md](jurisprudencia/cpc-arts-277-278-282-283-nulidades.md) — instrumentalidade das formas, preclusão da nulidade, prejuízo como condição da invalidação, aproveitamento dos atos (literal; recortes em `raw/`)
- Cadeia recursal: [/embargos-declaracao/](../embargos-declaracao/index.md) (prequestionar) → [/recurso-especial/](../recurso-especial/index.md) → [/agravo-em-resp/](../agravo-em-resp/index.md) / [/agravo-interno/](../agravo-interno/index.md)
