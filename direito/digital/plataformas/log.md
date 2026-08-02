# Log — digital/plataformas

## 2026-08-02

**Ingestão.** Semente v0.1.0 do bundle, criada na migração do acervo local
`direito_digital/` (Fase 4 do PRD de versionamento e modularização do `pma-workspace`).
3 cadeias de litígio de terceiros depositadas em `raw/` (18 arquivos, todos fora do git —
regra dura 10), 3 páginas derivadas em `jurisprudencia/` (todas `em_teste`).

- **Decisão de arquitetura:** o roteador planejava `direito/lgpd/` como destino do acervo
  `direito_digital`, mas o conteúdo real é litígio criador × plataforma (desmonetização,
  bloqueio de conta) — nada de LGPD. Criado `direito/digital/plataformas/`; `direito/lgpd/`
  continua planejado, vazio, para quando houver conteúdo próprio de proteção de dados.
- A pasta de origem também continha o caso do escritório no tema (desmonetização de canal
  no YouTube) — camada C1, **não migra**; segue no workspace até ir para o Drive.
- Eixo do tema conforme prática do escritório: a tese vencedora é a de que **a plataforma
  não provou a infração concreta** (ônus da ré), não a discussão abstrata dos termos de uso.

**Pendências:**
1. Etapa 0 formal (ingest-prep.py + sidecar) para os 9 documentos.
2. Anonimizar as cadeias (regra dura 10) para versionar os `.md` — prioridade para os 3
   acórdãos/decisões, que são o material citável.
3. Capturar o acórdão de agravo transcrito na decisão do TJPI (paradigma de tutela).
4. Página de legislação: Marco Civil da Internet (arts. 7º e 8º) via
   `recortar-artigo.py` quando o código integral for depositado em `direito/pecas/raw/`.
5. Ritual 7.2 (encerramento) quando o caso do escritório no tema tiver desfecho — alimenta
   `casos_decididos/` e o placar das teses.
