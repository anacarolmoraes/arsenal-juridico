# Catálogo do `raw/` — audiências

Depositado em 2026-08-01, vindo de `consumir/EXECUCOES_CREDOR` (a pasta misturava três assuntos; este é o corpo de audiências). Dois regimes:

| Regime | Arquivos | Regra |
|---|---|---|
| **Obra comercial** — curso "Semana da Audiência Sem Medo" / Audiências Online, Prof. José de Andrade Neto (juiz de direito do TJMS) | `curso-audiencias-*` | fora do git (`.gitignore` §1); só o conhecimento reescrito circula |
| **Decisão judicial de processo de terceiro** | `decisao-negocio-processual-videoconferencia-tjms.*` | PDF fora do git; `.md` anonimizado (regra dura 10) circula na equipe, não em pacote externo |
| **Ato normativo oficial** | `resolucao-cnj-354-2020-videoconferencia.*`, `lei-9099-art-*.md` | circula no git; texto de lei é público |

## Ato normativo oficial (circula no git)

- `resolucao-cnj-354-2020-videoconferencia.pdf` e `.md` — **Resolução CNJ 354/2020**, texto compilado do portal de atos do CNJ, já com as Resoluções 481/2022, 508/2023 e **679/2026**. 14 artigos, convertido pelo `pdfmd` em 2026-08-02; integridade conferida (nenhum artigo faltando na sequência, ruído de cabeçalho zero). **Ressalva da conversão:** o PDF grafa o ordinal como sobrescrito e a conversão o perde — o depósito mostra `Art. 1` e `§ 1 o` onde a norma escreve `Art. 1º`; o `depositar-lei.py` agora avisa quando isso acontece. Lastro da página [Resolução CNJ 354/2020](../jurisprudencia/resolucao-cnj-354-2020-videoconferencia.md).
- `lei-9099-art-9.md`, `lei-9099-art-20.md`, `lei-9099-art-55.md` — recortes gerados por `recortar-artigo.py` a partir do depósito transversal da Lei 9.099/95 em `direito/pecas/raw/`. **Não editar à mão: regerar.** Ainda sem página derivada.
- `enunciados-fonaje-juizados-especiais.md` — compilação oficial do **Fórum Nacional de Juizados Especiais (FONAJE)**, depositada em 2026-09-04, vinda de `consumir/`. **Três séries independentes, cada uma numerada a partir de 1**: Cível (177 enunciados), Fazenda Pública (17) e Criminal (133) — o mesmo número identifica enunciados diferentes em séries diferentes; sempre citar com a série ("Enunciado 35 do FONAJE, série Cível"). Conferido: 3 enunciados já citados pelos bundles do escritório (35, 97 e 141, todos Cível) tiveram o texto conferido letra por letra contra este depósito, com páginas próprias em [`jurisprudencia/`](../jurisprudencia/index.md) (e uma em `execucao/credor`, ver o `raw/` de lá). Os demais 324 enunciados **não têm página derivada** — consultar sob demanda com `ler-pdfmd.js` quando um caso citar outro número.

## Arquivos

- `curso-audiencias-pontos-controvertidos.md` — **o melhor do lote**: a tabela que cruza inicial, contestação e réplica com os arts. 373 e 374. Fonte da [heurística da tabela](/heuristicas/tabela-de-pontos-controvertidos.md).
- `curso-audiencias-perguntas-a-testemunha.md` — as cinco matrizes de pergunta e as regras de conduta; traz também uma lista de "sinais de mentira" sem validade científica, descartada na derivação.
- `curso-audiencias-perigos-juizado-especial.md` — dez perigos do rito da Lei 9.099/95.
- `curso-audiencias-semana-aula-4.md` e `curso-audiencias-perigos-videoconferencia.md` — regime da videoconferência, ancorado em normas de 2020 hoje exauridas.
- `curso-audiencias-perigos-familia.md` — dez perigos, essencialmente comportamentais; rito ancorado nos arts. 693 e 731 do CPC e no art. 13 da Lei 5.478/68.
- `curso-audiencias-advogado-correspondente.md` e `curso-audiencias-advogado-dativo.md` — atuação por conta de outro. (O cabeçalho interno do arquivo de correspondente está trocado e diz "dativo": artefato do material, o corpo é de correspondente.)
- `curso-audiencias-sem-experiencia-pratica.md` — os passos de preparação; base do [playbook](/playbooks/playbook-preparacao-de-audiencia.md).
- `curso-audiencias-situacoes-inesperadas.md` e `curso-audiencias-10-maiores-medos.md` — casuística de sala de audiência; **a maior parte só enuncia o problema sem dar a solução**.
- `curso-audiencias-custodia-penal.md` — **MATÉRIA PENAL, não derivada neste bundle.** Audiência de custódia (CPP art. 310, Res. CNJ 213/2015, prazo de 24 h). Fica depositado para quando houver bundle penal; não confundir com o escopo cível.
- `decisao-negocio-processual-videoconferencia-tjms.md` — decisão de 10/06/2020 da 14ª Vara Cível de Campo Grande/MS (proc. 0806036-51.2019.8.12.0001), assinada pelo próprio autor do curso, propondo às partes negócio jurídico processual (art. 190) para instrução por videoconferência, com sete cláusulas — a sétima é renúncia prévia ao direito de alegar nulidade por quebra de incomunicabilidade. Anonimizada; código de acesso ao eSAJ suprimido.

## Avisos permanentes

**Vigência.** Todo o eixo de videoconferência do curso nasce do regime emergencial da Covid-19 e se apoia na Res. CNJ 314/2020 e na Recomendação 62 — **exauridas**. **Resolvido em 2026-08-02 quanto à norma do CNJ:** a âncora vigente é a Res. CNJ 354/2020, depositada aqui e transcrita em [jurisprudencia/](../jurisprudencia/resolucao-cnj-354-2020-videoconferencia.md). Continua faltando o **ato do tribunal local** (art. 13 da Resolução) e a **Res. CNJ 341/2020**, referida nos arts. 2º e 12. Nenhum número ou prazo dos arquivos de curso vai para peça sem conferir contra a Resolução depositada.

**Natureza do material.** São mapas mentais de lives promocionais: entregam o diagnóstico e retêm boa parte do tratamento no curso pago. Três técnicas de inquirição só são nomeadas; a maioria dos "10 medos" e das "situações inesperadas" fica sem resposta. O acervo registra isso para que ninguém espere do material o que ele não tem.

**Higiene.** Links de convite de grupos de WhatsApp e o quiz com token de sessão foram removidos na ingestão: não têm valor jurídico e são rastreadores de acesso a espaços privados de terceiros. A autoria do professor foi mantida — é obra de terceiro e a atribuição é devida.
