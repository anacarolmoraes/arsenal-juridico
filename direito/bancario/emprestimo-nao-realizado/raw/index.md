# raw/ — fontes brutas imutáveis

Depósito de fonte: nada aqui se edita. Páginas de `jurisprudencia/` derivam daqui e apontam
para cá.

## Versionado (circula para a equipe)

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
