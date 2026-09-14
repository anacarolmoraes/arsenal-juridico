# Log — cobranca-honorarios

## 2026-09-13

**Etapa 0 cumprida e páginas promovidas (v0.1.0 → v0.2.0).** Consumo de `consumir/` do workspace a pedido da titular.

- **Lei 15.109/2025** depositada integral em `raw/` (`depositar-lei.py`, cp1252, 3 artigos). Página `cpc-art-82-par3` ganha `raw:` e `verificado_em`. Fecha a pendência 4 de 21/07.
- **Estatuto da OAB**: o depósito já existia desde 02/08 (cobertura Lei 15.472), mas a página `oab-lei8906-arts-22-a-26` seguia `em_teste` com `raw: pendente-deposito-titular`. Reescrita com transcrição literal dos arts. 22 (caput, §§ 2º, 3º, 4º, 9º), 23, 24 (caput, §§ 1º, 4º a 7º), 25, 25-A e 26, e promovida a `vigente`. **Duas correções de conteúdo:** (a) o "art. 26 como regra residual de contagem da prescrição" **não existe** na lei; o art. 26 trata do substabelecido com reserva de poderes. Era conhecimento não conferido. (b) Entram o § 9º do art. 22 (Lei 15.472/2026: natureza alimentar e privilégio trabalhista para **todas** as espécies de honorários, inclusive convencionados) e os §§ 5º a 7º do art. 24 (Lei 14.365/2022: distrato não é renúncia; honorários proporcionais). A tese `natureza-alimentar-privilegio` ainda não aponta para o § 9º: fazer na próxima revisão da tese. A cópia nova de `L8906.html` em `consumir/` tem a mesma cobertura do depósito e não foi redepositada.
- **CPC**: recortes gerados do compilado transversal para os arts. 85, 784, 523-527, 771-776 e **827-829** (este último porque o prazo de 3 dias e a redução dos honorários pela metade, que a página dos arts. 771-776 atribuía às disposições gerais, estão nos arts. 829 e 827, § 1º). As quatro páginas ganham bloco "Texto" com transcrição gerada do recorte, `raw:` e `status: vigente`. Correção na página do art. 784: a Lei 14.620/2023 incluiu o § 4º (assinatura eletrônica dispensa testemunhas), não alterou o inciso IV. Fecha a pendência 1 de 21/07.
- **REsp 1.504.969/SP** (3ª Turma, Rel. Villas Bôas Cueva) depositado em `raw/` como relatório e voto anonimizados (PDF e `.integral.md` fora do git), segmentado (`segmentar-acordao.py`: 6 blocos citados, 2 sem atribuição), página `vigente` com `tese:` extraída do voto. O depósito não traz ementa nem data de julgamento; conferir no STJ antes de citar com data. **Fecha em parte a pendência 3 de 21/07** (termo inicial da prescrição do art. 25): o STJ diz que o art. 25 e o art. 206, § 5º, II, do CC valem só para a relação advogado-cliente, e que fora dela o prazo é o decenal do art. 205 contado pela *actio nata* do recebimento. Segue em aberto um julgado do STJ sobre os incisos do art. 25 na cobrança contra o cliente.
- **REsp 1.573.573/RJ** (pendência 2 de 21/07): localizado e depositado. É o EDcl no AgInt que fixa os requisitos dos **honorários recursais** do art. 85, § 11, matéria de sucumbência e não de cobrança de honorários; foi para `direito/pecas/sucumbencia/` (raw + página). Pendência fechada por redistribuição.
- `index.md` do bundle passa a listar `raw/` e registra que a réplica de honorários de 10/09/2026 é a primeira peça real do tema.

**Pendências que ficam:** (3) julgado do STJ sobre o termo inicial do art. 25 na relação com o cliente; (5) `README.md` e `atividades.md`; AREsp 2.706.690 continua `em_teste`; tese `natureza-alimentar-privilegio` sem o art. 22, § 9º.

## 2026-08-02

**Ingestão.** Migração da Fase 4 do PRD de versionamento do `pma-workspace`:

- **AREsp 2.706.690/SP** (decisão monocrática, Min. Noronha, DJEN 06/05/2025) — honorários
  por apreciação equitativa devem observar a tabela da OAB ou o piso de 10% do art. 85, §2º,
  o que for maior (art. 85, §8º-A). Inteiro teor depositado em `raw/aresp-2706690-sp.{md,pdf}`
  (cópia certificada, veio juntada como paradigma em autos do TJSP) e página `em_teste` em
  `jurisprudencia/` — conferir se houve agravo interno antes de promover.
  O documento estava no acervo local `direito_bancario/juros_abusivos/` (matéria é daqui).
- Criado `raw/index.md` (catálogo).
- Sobre a pendência 2 de 21/07 (`estrategias1.md` com a citação solta "RESP 1573573"): o
  arquivo tem 34 bytes, é só o apontamento — **não migra**; a pendência de localizar o REsp
  1.573.573 e avaliar ingestão permanece aberta.

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
