# Catálogo do `raw/` — LGPD

Duas fontes, com regimes de circulação opostos.

## Obra da própria titular — circula na equipe, não sai em pacote externo

| Arquivo | O que é |
|---|---|
| `cartilha-seguranca-informacao-pma-2021.md` | **Cartilha de introdução à proteção de dados pessoais e a conceitos iniciais de segurança da informação**, maio de 2021, elaborada por Ana Carolina Ribeiro de Moraes Paulo (advogada e cientista da computação, certificada pela EXIN em segurança da informação e em proteção de dados). Cobre conceitos da LGPD (tratamento, dado pessoal, dado sensível, titular), o rol de direitos do titular, a tríade confidencialidade/disponibilidade/integridade e o catálogo de **engenharia social** — a parte que virou [página derivada](../heuristicas/engenharia-social-as-alavancas.md). Material autoral e identificado do escritório: registrado em `distribuicao.json` como exclusão de camada 2. **Datado:** anuncia sanções "a partir de 1º/08/2021" e não reflete a atuação posterior da ANPD. |

## Obra de terceiro — **fora do git**

| Arquivo | O que é |
|---|---|
| `lgpd-cartorios-infografico.{pdf,md}` | Coluna "Ponto de Vista" de **Joelson Sell**, uma página, sobre adequação de cartórios à LGPD. Publicação de terceiro (Lei 9.610/98) — fica na máquina de quem depositou. Conversão por OCR (`tesseract`), texto em duas colunas que o extrator entrelaçou: **legível, mas fora de ordem em vários pontos** — não citar sem conferir no PDF. Aponta o art. 23, § 4º, da LGPD (notários e registradores: política transparente e encarregado nomeado) e os Provimentos CNJ **74/2018** e **50/2015** como referência de padrões mínimos de TI. **Nada disso foi conferido em fonte oficial.** Sem página derivada: a matéria é de serventia extrajudicial, tangencial à prática do escritório. |

## Etapa 0 — cumprida em 2026-09-13

**A Lei 13.709/2018 está depositada** no transversal [`direito/pecas/raw/`](../../pecas/raw/index.md), como
`lgpd-l13709-2018-compilada.{html,md}` (texto do Planalto via `depositar-lei.py`, cp1252, 64 artigos, cobertura até a
Lei 15.352, sem trecho revogado). Recorte por artigo para cá com `recortar-artigo.py <art> direito/lgpd --codigo
direito/pecas/raw/lgpd-l13709-2018-compilada.md --rotulo LGPD`. Aviso do depósito: um artigo de 1 a 9 vem sem indicador
ordinal no HTML oficial; a página que o transcrever declara a normalização.
