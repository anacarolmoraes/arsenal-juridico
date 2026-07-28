# Log — cobranca-honorarios

## 2026-07-21

**Ingestão.** Primeira carga de conhecimento do bundle, a pedido do titular ("consuma a fonte de direito civil e de processo civil que fala sobre honorários advocatícios, execução de honorários e execução de título executivo extrajudicial").

- Fonte primária tentada: `WebFetch` a `planalto.gov.br` (CPC, Lei 13.105/2015) para conferir texto vigente dos arts. 85, 784, 523-527 e 771-776 — **falhou 3x com `ECONNRESET`**, sem acesso à internet nesta sessão do agente.
- Fonte secundária consultada: doutrina já presente em `direito/pecas/raw/` (`manual-dpc-scarpinella-2024.md`, `manual-dpc-montans-2024.md`, `iuris-dpc-vol4-2025.md`, `pratica-processo-civil-gediel-2016.md`) — 478 ocorrências de "honorári*" localizadas; extração seletiva sobre natureza alimentar (art. 85, §14), rol do art. 784 (títulos executivos extrajudiciais) e execução de honorários sucumbenciais. Conteúdo **reescrito em linguagem própria** (nunca reproduzido literalmente da obra), conforme regra 6.6 do schema — ementas/dispositivos citados apontam a fonte oficial (lei), não o manual.
- Criadas 6 páginas em `jurisprudencia/` (5 `status: em_teste`, pendentes de conferência oficial; 1 `status: vigente` — art. 82, §3º, CPC, já conferido em uso real anterior do escritório, ver `honorarios-dispensa-custas-lei-15109` na memória do agente) e 3 páginas em `teses/`.
- **Não encontrado nos 4 manuais**: conteúdo específico do Estatuto da OAB (Lei 8.906/94, arts. 22 a 26) — são manuais de processo civil geral, não do estatuto da advocacia. Página `jurisprudencia/oab-lei8906-arts-22-a-26.md` criada a partir de conhecimento consolidado do agente, sem cruzamento com fonte local; prioridade alta para verificação.

**Pendências (para próxima sessão com acesso à internet, ou depósito de PDF pelo titular):**
1. Depositar em `raw/` os PDFs oficiais: CPC (Lei 13.105/2015) e Estatuto da OAB (Lei 8.906/94) — rodar `ingest-prep.py` (Etapa 0) e só então promover as páginas de `em_teste` para `vigente` com `resource`/`verificado_em` reais.
2. `clientes/cobranca_honorarios/estrategias/estrategias1.md` (projeto principal, C1) tem apenas a citação solta "RESP 1573573 (sobre honorários)", sem conteúdo — localizar o acórdão e, se pertinente ao tema, ingerir como `jurisprudencia/` (tipo `acordao`).
3. Jurisprudência do STJ sobre termo inicial da prescrição do art. 25 da Lei 8.906/94 — não localizada nas fontes atuais.
4. Texto integral da Lei 15.109/2025 — hoje só há o art. 82, §3º, CPC, registrado (via memória do escritório, não via ingestão formal deste bundle).
5. `README.md` e `atividades.md` do bundle — pendentes até existir workflow/peça real associada (petição de cobrança ou execução).
