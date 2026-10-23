# raw/ — fontes brutas imutáveis

Depósito de fonte: nada aqui se edita. Páginas de `jurisprudencia/` derivam daqui e apontam
para cá.

## Versionado (circula para a equipe)

- [cdc-art-6.md](cdc-art-6.md) · [cdc-art-7.md](cdc-art-7.md) · [cdc-art-14.md](cdc-art-14.md) · [cdc-art-34.md](cdc-art-34.md) · [cdc-art-42.md](cdc-art-42.md) — recortes do CDC gerados por `recortar-artigo.py` em 2026-09-13 a partir do depósito transversal `direito/pecas/raw/cdc-l8078-1990-compilado.md` (cobertura até a Lei 14.181). Fonte das cinco páginas de legislação do CDC deste bundle, cujas transcrições foram conferidas contra os recortes.
- [cpc-art-300.md](cpc-art-300.md) · [cpc-art-319.md](cpc-art-319.md) · [cpc-art-429.md](cpc-art-429.md) · [cpc-arts-98-99.md](cpc-arts-98-99.md) — recortes do CPC compilado transversal (`direito/pecas/raw/cpc-l13105-compilada.md`, cobertura até a Lei 15.484), gerados em 2026-09-13. Fonte das quatro páginas de legislação do CPC deste bundle; transcrições conferidas. A página dos arts. 98-99 também transcreve o art. 5º, LXXIV, da Constituição, que não tem depósito no acervo.
- [sumula-479-stj.md](sumula-479-stj.md) (+ `.pdf`) — verbete oficial da Súmula 479/STJ (2ª Seção, j. 27/06/2012, DJe 01/08/2012), com enunciado, referência legislativa e precedentes, extraído do SCON. Fonte pública; depositado em 29/08/2026. O repetitivo que a originou é o REsp 1.199.782/PR, acima.
- [resp-1846649-ma.md](resp-1846649-ma.md) (+ `.pdf`, `.quality.json`) — REsp 1.846.649/MA: ônus da prova da autenticidade de assinatura impugnada é do banco.
- [earesp-600663-rs.md](earesp-600663-rs.md) (+ `.pdf`, `.quality.json`) — EDcl nos EAREsp 600.663/RS: devolução em dobro, boa-fé objetiva (par do EAREsp 676.608/RS, depositado no bundle `juros-abusivos`).
- [resp-1199782-pr.md](resp-1199782-pr.md) (+ `.pdf`, `.quality.json`) — REsp 1.199.782/PR (repetitivo): responsabilidade objetiva do banco por fraudes de terceiros (base da Súmula 479).
- `res-bacen-4753-2019.pdf` — Resolução CMN 4.753/2019 (texto oficial). **Pendência Etapa 0:** gerar o par `.md` + sidecar via `ingest-prep.py`; a página derivada do art. 2º já existe em `jurisprudencia/`.

## Fora do git (`.gitignore` §2 — regra dura 10; ficam na máquina de quem depositou)

Cadeia de litígio de terceiro (TJRO, Apel. 7004672-78.2021.8.22.0010 — fraude em consignado;
é a cadeia-fonte do `casos_decididos/caso-a-consignado-fraudulento.md`), com dado pessoal,
pendente de anonimização:

- `cadeia-tjro-7004672-inicial.{md,pdf}` — petição inicial.
- `cadeia-tjro-7004672-sentenca.{md,pdf}` — sentença.
- `cadeia-tjro-7004672-acordao-tj.{md,pdf}` — acórdão da 1ª Câmara Cível do TJRO.

## Legislação

- `lei-12965-2014-marco-civil.md` — Lei 12.965/2014 (Marco Civil da Internet), texto oficial consolidado do Planalto, convertido de HTML em 20/10/2026. Página derivada: `jurisprudencia/lei-12965-2014-arts-10-13-15-22.md`.
