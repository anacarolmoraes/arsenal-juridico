# Log

## 2026-08-02

- **Ingestão** — Migração final do acervo local `direito_bancario/emprestimo_nao_realizado/`
  (Fase 4 do PRD de versionamento do `pma-workspace`):
  - `raw/res-bacen-4753-2019.pdf` — texto oficial da Resolução CMN 4.753/2019 (estava em
    `golpes/legislacao_principal/` no acervo antigo). Página derivada do art. 2º ganhou o
    campo `raw:`. **Pendência Etapa 0:** par `.md` + sidecar.
  - Cadeia-fonte do caso A (TJRO, Apel. 7004672-78.2021.8.22.0010) depositada em
    `raw/cadeia-tjro-7004672-*` — **fora do git** (regra dura 10, dado pessoal de terceiro),
    pendente de anonimização. Fecha a auditabilidade do
    `casos_decididos/caso-a-consignado-fraudulento.md`.
  - Criado `raw/index.md` (catálogo).
  - Não migrados: `jurisprudencia_stj/EMENTA_*` (subconjuntos redundantes dos inteiros
    teores já depositados) e `estrategias/estrategia1.md` (já destilado em
    `playbooks/`+`heuristicas/` na criação do bundle, schema §11); `marly/` é camada C1.

## 2026-07-07

- **Lint** — **Auditoria das skills jurídicas (6 pinadas) com correções aplicadas na origem (`D:\WORK\advocacia\skills`) e no bundle:**
  1. `legal-orchestrator` 4.0.0 → **4.1.0**: eliminada contradição interna do Estágio 3/4 (a tabela mandava tratar MÉDIO/BAIXO no Estágio 4, o cabeçalho do Estágio 4 exigia CRÍTICA/ALTA); adicionada **revalidação obrigatória** pós-humanizer (Estágio 5 alterava texto depois da validação adversarial sem nova checagem); nota de autossuficiência do modo jurídico quando a skill `humanizer` não estiver disponível.
  2. `legal-consistency-validator` 2.1.0 → **2.2.0**: criado o **mapeamento fixo severidade → veredito** (nenhuma fraqueza = APROVADO; só MÉDIO/BAIXO = APROVADO COM RESSALVAS; qualquer CRÍTICO/ALTO = REPROVADO) — antes o veredito era indefinido para textos só com fraquezas médias.
  3. `peca-pma-builder` → **1.1.0**: `pQuote()` corrigido para cumprir a tipografia-pma Módulo 6.1 — Montserrat **Light** 11 pt (era regular), **sem itálico** (era itálico), recuo **3 cm** (era 2 cm + 1 cm à direita). Verificado por execução: .docx de teste gerado e XML inspecionado (`w:left="1701"`, `w:i w:val="false"`, fonte "Montserrat Light", `sz 22`). SKILL.md atualizado (exemplo e tabela de API).
  4. `tipografia-pma` → **1.1.0**: campo `version` criado; caminhos absolutos `D:\WORK\...` removidos do texto (modelo canônico agora referenciado só por caminho relativo `assets/PETICAO_MODELO.docx` — a fronteira do repositório é a fronteira do compartilhamento).
  5. **Varredura de vazamento**: `legal-writer` do bundle ainda continha o prenome real de um cliente nas referências às peças-ouro (a anonimização de 2026-07-06 foi parcial — apenas um dos dois nomes havia sido trocado por "CLIENTE-B"). Substituído por **CLIENTE-A** nas 3 ocorrências. Divergência intencional com a origem registrada no `skills-lock.json`. Histórico git expurgado via filter-branch na mesma data (varredura pós-expurgo limpa; única ocorrência remanescente do prefixo é "Alexandre de Moraes", ministro relator citado em `raw/` — legítima).
  - `skills-lock.json` atualizado (versões novas + divergência intencional do legal-writer documentada). Pendência de lint do versionamento (2026-07-05) resolvida — versionado na origem.

- **Atualização** — **Matriz validada pelo titular → `vigente`** (bundle v0.4.0): criticidades confirmadas como propostas (protocolos administrativos e hipossuficiência permanecem `alta`). Conhecimento novo do titular incorporado: seção **Comprovação reforçada de hipossuficiência (condicional)** — juízes vêm exigindo documentação além da declaração (extratos de todos os relacionamentos bancários/conferíveis pelo **Registrato**/BCB, declaração de IR, conta de energia baixa renda, comprovante de auxílio governamental, contracheques); coleta condicional ao pedido de gratuidade, não padrão (minimização). Evolução da lista de documentos: na medida do uso (ciclo de encerramento de casos).
- **Schema** — **Tipo novo `matriz-documentos`** (bundle v0.3.0): criada `playbooks/matriz-documentos-fraude-consignado.md` — o que coletar do cliente no atendimento, com criticidade e fundamento (cada item lastreado em tese/heurística/exigência processual do bundle; regra de minimização LGPD: documento sem lastro não se coleta). Origem: schema da camada C1 v0.2 (`c1/SCHEMA_CAMADA_C1.md` no repo KnowledgeOperatingSystem), validado com o primeiro caso real estruturado — os 9 itens da matriz conferidos contra a coleta real da pasta do cliente no Drive. Status `em_teste` — **aguarda validação de criticidades pelo titular**.

## 2026-07-05

- **Atualização** — **Ciclo de melhoria pós-H1 (bundle v0.2.0):** (1) raw/ reconvertido com paginação — o EAREsp 600.663 agora tem o **inteiro teor** (16 p., e-STJ Fl.1339–1354); acórdãos ganharam seção **Trechos-chave** com transcrições literais localizadas por folha e-STJ; corrigida a modulação para o texto literal do item 23 ("**cobrados** após a publicação", não "pagos"). (2) Legislação com texto literal + seção **Remissões** (inclui CDC 14, § 3º, II — a defesa típica dos bancos — e a nuance do CPC 334, § 4º, I). (3) Novos: tese `solidariedade-correspondente-bancario` (lacuna detectada pelo H1), páginas CDC 7º § ún./34, CPC 98-99/300/319-VII, Res. CNJ 345/2020, heurísticas `sugerir-multa-diaria-na-tutela` (vigente) e `pedir-audiencia-conciliacao` (**em_teste** — aguarda titular), tipo novo `perfil-orgao-julgador` com `perfis/1a-camara-civel-tjro.md`, e `escritorio.md` (fonte única de subscrição). (4) Playbooks com **Regras de citação e verificabilidade** (literal em bloco + granularidade máxima + cadeia de remissões) e **matriz de cobertura** como portão da apelação. (5) Workflows com entregáveis formais: relatório de fontes (URL + página/folha + trecho + nível de confiança) e checklist pré-protocolo.
  - Pendências novas: capturar Res. CMN 3.954/2011 (correspondentes); URI canônica da Res. CNJ 345; endereço profissional em `escritorio.md`; tipo `perfil-orgao-julgador` a formalizar no schema v0.4 junto com a D12 (ortogonalidade peça × matéria).

- **Lint** — **Teste H1 nº 1: Q7 confirmado pelo titular** ("protocolaria com ≤15 min de revisão") — H1 formalmente aprovada. Feedback de calibragem do titular registrado como pendências de melhoria: (a) citar trechos literais de julgados e legislação na peça (facilita a revisão humana); (b) relatório de fontes apartado com endereço oficial + página do trecho citado; (c) profundidade de citação legislativa: artigo/parágrafo/inciso/alínea + cadeia de remissões (artigo que cita artigo, inclusive de outra lei, com a lei identificada).
- **Lint** — **Teste H1 nº 1 (agente limpo, caso piloto): APROVADO.** Eliminatórios 3/3 (nenhuma jurisprudência inventada — Súmula 297 e caso TJRO citados indiretamente e com origem rastreável; nenhum vazamento; pedidos essenciais completos, incluindo exibição de cautelas e depósito judicial). Qualidade 6/6 verificados (roteou sozinho via atividades.md; narrativa com via administrativa e valor intacto; impugnação expressa da assinatura; fundamentação completa; números consistentes — 60×R$47=R$2.820, dobro R$5.640, causa R$17.767,01; .docx gerado pela skill). Q7 (revisão ≤15min) pendente de avaliação do titular. Duração: ~13,5min; ~134k tokens.
  - **Lacuna de bundle detectada pelo teste:** não há tese de solidariedade do correspondente bancário (cadeia de fornecimento, CDC) — o agente, corretamente, não incluiu a Ponto Amigo como corré por falta de fundamento no bundle, mas a peça real do escritório a incluiu. Criar a tese.
  - **Divergência estratégica a decidir pelo titular:** agente manifestou desinteresse na autocomposição (art. 319, VII, CPC); a peça real pediu audiência de conciliação. Se houver preferência do escritório, virar heurística.
  - **Menores:** multa diária deixada ao arbítrio do juízo (peça real sugeriu R$1.000/dia — candidata a heurística); legislação processual geral (CPC 98/99, 300, 319 VII; Res. CNJ 345/2020) citada fora do bundle e devidamente sinalizada — avaliar criar páginas.

- **Schema** — Adotada a Etapa 0 da ingestão (schema v0.3, decisão D11): conversão PDF→md pelo `pdfmd` com escalonamento de OCR e portão de qualidade determinístico (`ingest-prep.py` + sidecars `.quality.json`). Rodado sobre `raw/`: earesp-600663-rs (100, aprovado), resp-1199782-pr (90, aprovado — artefatos de assinatura PJe), resp-1846649-ma (100, aprovado). Trabalho futuro registrado na decisão: markitdown para formatos não-PDF; docling/marker se tabelas degradarem.

- **Ingestão** — Migração inicial do acervo `direito_bancario/emprestimo_nao_realizado` conforme `SCHEMA_BUNDLE_PILOTO.md` v0.2 (seção 11): 3 acórdãos STJ para `raw/` + 9 páginas de jurisprudência, 4 teses, 3 heurísticas e 2 playbooks extraídos de `estrategia1.md`, 1 caso decidido anonimizado, 2 workflows, 6 skills pinadas.
- **Lint** — Varredura de vazamento executada sobre o bundle na migração: caso decidido reescrito de forma anonimizada (fonte original em C1 continha nome, CPF, RG, telefone, endereço, nº de benefício e nº de processo — nenhum migrado). Pendências registradas abaixo.

### Pendências de lint

- Confirmar URIs canônicas (`resource`) das páginas de jurisprudência nos portais oficiais (STJ/Planalto/BCB) — preenchidas com portais de consulta, faltam deep links.
- Capturar PDFs oficiais para `raw/`: Súmula 479, dispositivos CDC/CPC e Res. BACEN 4.753/2019 (páginas criadas sem `raw:`).
- ~~Skills `tipografia-pma` e `peca-pma-builder` sem campo `version` no SKILL.md — pinadas por data de cópia no `skills-lock.json`; versionar na origem.~~ — **resolvido (2026-07-07):** ambas versionadas como 1.1.0 na origem e no bundle.
- ~~`skills/peca-pma-builder/SKILL.md` usa número de processo real como exemplo de código~~ — **resolvido (2026-07-06):** número e nomes de clientes substituídos por fictícios na fonte canônica (`D:\WORK\advocacia\skills`) e no bundle; **histórico git reescrito** (filter-branch) e varredura confirmou zero ocorrências em todos os commits. Pré-requisito de push cumprido.
