# raw/ — fontes brutas imutáveis

Depósito de fonte: nada aqui se edita. Páginas de `jurisprudencia/` derivam daqui e apontam
para cá. **Etapa 0 formal (ingest-prep.py + sidecar de qualidade) pendente** para todos os
depósitos.

## Fora do git (`.gitignore` §2 — regra dura 10; ficam na máquina de quem depositou)

Três cadeias de litígio de terceiros, com dado pessoal, pendentes de anonimização:

**Cadeia 1145073-74.2023.8.26.0100 (TJSP — desmonetização de canal no YouTube):**
- `cadeia-1145073-inicial.{md,pdf}` — petição inicial (tutela antecedente do art. 303 do CPC; contém CPF, RG, endereço e e-mail do autor).
- `cadeia-1145073-sentenca.{md,pdf}` — sentença de procedência (reativação + lucros cessantes).
- `cadeia-1145073-acordao-tj.{md,pdf}` — acórdão da 33ª CDPriv negando provimento à apelação da plataforma.

**Cadeia 1056045-32.2022.8.26.0100 (TJSP — bloqueio de monetização de página no Facebook):**
- `cadeia-1056045-inicial.{md,pdf}` — petição inicial.
- `cadeia-1056045-interlocutoria.{md,pdf}` — decisão interlocutória da cadeia.
- `cadeia-1056045-sentenca.{md,pdf}` — sentença de procedência.
- `cadeia-1056045-acordao-tj.{md,pdf}` — acórdão da 26ª CDPriv negando provimento à apelação da plataforma.

**Cadeia 0809064-72.2026.8.18.0176 (TJPI — reativação de conta de Instagram, Juizado):**
- `cadeia-0809064-inicial.{md,pdf}` — petição inicial (Juizado Especial; contém CPF e endereço da autora).
- `cadeia-0809064-tutela-deferida.{md,pdf}` — decisão-carta deferindo a tutela de urgência.

## No git (pseudonimizados, regra dura 6)

Acórdãos de terceiros baixados do CJSG/e-SAJ (18/10/2026). Nome da parte autora e identificador
da conta trocados por rótulo; PDF não depositado (fica em `jurisprudencia-tjsp/` do workspace).

- `apelacao-1149661-tjsp-bloqueio-conta-candidata-facebook.md` — ApCiv 1149661-90.2024.8.26.0100, 30ª CDPriv, 14/07/2025. Sidecar `.estrutura.json` com `nao_segmentado: true`.
- `apelacao-1051450-tjsp-restricao-funcionalidades-instagram.md` — ApCiv 1051450-82.2025.8.26.0100, 23ª CDPriv, 22/06/2026. Sem sidecar: o segmentador tomava a ementa do próprio acórdão por voz alheia.
- `apelacao-1064147-tjsp-instagram-fraude-enganacao-onus-re.md` — ApCiv 1064147-38.2025.8.26.0100, 28ª CDPriv, 25/03/2026. Sem sidecar (mesmo motivo da 1051450).
- `agravo-2249428-tjsp-tutela-reativacao-perfis-instagram.md` — AI 2249428-59.2025.8.26.0000, 11ª CDPriv, 19/02/2026. Sem sidecar.
- `apelacao-1031722-tjsp-instagram-fraude-enganacao-dever-informacao.md` — ApCiv 1031722-55.2025.8.26.0100, 27ª CDPriv, 13/04/2026. Sem sidecar.
- `agravo-2159834-tjsp-meta-alega-exclusao-permanente.md` — AI 2159834-97.2026.8.26.0000, 31ª CDPriv, 17/08/2026. Sem sidecar; parte e perfil de terceiro em precedente transcrito também pseudonimizados.
