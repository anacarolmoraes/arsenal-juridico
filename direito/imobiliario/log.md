# Log — imobiliario (rescisão contratual)

## 2026-08-02

**Ingestão da migração final do acervo local (v0.3.0 → v0.4.0).** Fase 4 do PRD de
versionamento do `pma-workspace` — sobras de `rescisao_contrato_imovel/` conferidas e
migradas:

- **`playbooks/modelo-peticao-levantamento-suspensao-irdr.md`** (`vigente`, versionado) —
  modelo genérico do escritório da petição intercorrente de levantamento de suspensão por
  IRDR, promovido de `genericas/`. Duas adaptações na promoção: assinatura vira referência
  ao `perfil/advogados.json` do motor, e o "Tema 557" da voz própria da peça foi corrigido
  para **Tema 577** (o typo é do TJTO na redação das teses; as transcrições literais o
  preservam, com nota de alerta no cabeçalho do modelo).
- Depósitos novos em `raw/`, **fora do git** até anonimização/conversão (regra dura 10):
  `resp-2035848-to-decisao-nao-afetacao.md` (decisão da Comissão Gestora de Precedentes,
  Min. Assusete Magalhães, 01/06/2023 — fecha a cadeia documental da desafetação);
  `resp-2035848-to-certidao-desafetacao.pdf` (certidão da retirada do rito qualificado —
  **sem par `.md`**, Etapa 0 pendente); e 5 documentos `antes-lei-*` do TJTO (acórdãos de
  agravo, sentença e compilação de ementas sobre inaplicabilidade do IRDR a contratos
  anteriores — fontes de argumentação do modelo acima).
- `raw/artigo-zufelato-irdr.{md,pdf}` — artigo doutrinário de terceiro (obra intelectual,
  Lei 9.610/98): **fora do git**, mesma regra do Scavone; só conhecimento reescrito circula.
- **Não migram** (camada C1 → Drive): `francineia/`, `joao_victor/`, `rodrigo_chaves/`,
  `cumprimento_sentenca/patrick/`, contrarrazões e apelação avulsas da raiz, e os
  `modelos_argumentacao/` com peça de cliente identificável (conferir antes de qualquer
  reaproveitamento). Os modelos de cumprimento (`CUMPR_SENTENCA_MODELO.docx` + planilha de
  upload) foram copiados para `material_padrao_escritorio/` no motor — casa canônica.

## 2026-08-01

**Ingestão dos modelos Scavone (v0.2.0 → v0.3.0).** Execução das Fases A e B do plano
`planos/2026-08-01_plano-consumo-scavone-imobiliario.md` (motor).

- **raw/modelos-scavone/**: 94 modelos de petição do material que acompanha SCAVONE JR.,
  *Direito Imobiliário — Teoria e Prática*, depositados como par `.rtf` (original imutável)
  e `.md` (conversão striprtf, aviso de obra de terceiro no topo de cada arquivo). 3 arquivos
  curtos (< 800 chars) conferidos à vista — são documentos genuinamente curtos, não erro de
  conversão. Catálogo por tema em `raw/modelos-scavone/index.md`. **Regra de fronteira
  (corrigida na mesma data):** obra comercial **não entra no git** (`.gitignore` §1, mesma
  regra dos manuais de DPC) — os arquivos vivem só na máquina de quem depositou; **o
  catálogo é o que circula**. A primeira versão desta ingestão havia rastreado os arquivos;
  os commits locais foram reescritos antes de qualquer push.
- **Fase B — conhecimento reescrito da anatomia dos modelos 3.10.x** (lado credor da mesma
  relação deste bundle) nas páginas existentes:
  - `heuristicas/verificar-vicio-formal-de-notificacao-extrajudicial.md` — checklist ampliado
    (itens 5-7): prazo de purga por regime (art. 32 Lei 6.766/79 × art. 1º DL 745/69 ×
    art. 1º V-VI Lei 4.864/65), conteúdo mínimo da notificação, e o fallback da notificação
    judicial (arts. 726-729 CPC) quando a diligência é frustrada.
  - `teses/notificacao-previa-invalida-obsta-rescisao-por-loteadora.md` — novo contra-argumento:
    diligência frustrada não supre a mora; a via correta era a notificação judicial, que a
    loteadora não usou.
  - `playbooks/playbook-contestacao-notificacao-viciada.md` — preliminares ampliadas (valor da
    causa art. 292 II/§3º; incompetência art. 101 I CDC; mecânica do art. 338 CPC na
    ilegitimidade), mérito ampliado (descaracterização da culpa da mora por encargo ilegal;
    adimplemento substancial; retenção por benfeitorias art. 1.219 CC; combate à tutela pelo
    art. 300 §3º) e reconvenção para inverter a culpa da resolução. Novo alerta: **as ementas
    citadas nos modelos Scavone (1998-2015) não passaram por verificação — buscar precedente
    atual via radar-jurisprudencia antes de citar.**
- **Livro-fonte depositado** (`raw/scavone-direito-imobiliario-9ed-2015.{pdf,md}`, fora
  do git como acima): OCR concluído no mesmo dia (5,4 MB de texto). **Achado da
  validação: é a 9ª edição, de 2015** — anterior à Lei 13.786/2018, à Lei 14.382/2022
  (SERP) e à Lei 14.711/2023 (Marco Legal das Garantias). Aviso com dupla trava (edição
  + ruído de OCR) no topo do `.md` e no `raw/index.md`; sumário aproximado por Livro
  anotado no catálogo dos modelos. O livro **não** é fonte de transcrição literal: lei e
  julgado se conferem na fonte oficial.
- **Manifesto de distribuição criado na raiz do acervo** (`distribuicao.json` +
  `empacotar.py`), formalizando as duas camadas: camada 1 = `.gitignore` (obra de
  terceiro e PDF de processo alheio nunca entram no git); camada 2 = manifesto (o que é
  rastreado mas não sai em pacote externo: `escritorio.md`, peças anonimizadas da cadeia
  golpe, o próprio manifesto). `python empacotar.py --verificar` é portão obrigatório
  antes de qualquer pacote; o modo padrão gera o zip distribuível em `dist/`.
- **Escopo:** os demais temas dos modelos (possessórias, locação/despejo, usucapião,
  condomínio, incorporação, alienação fiduciária/leilão) permanecem fora do escopo deste
  bundle. Decisão registrada: quando chegar o primeiro caso de um tema novo, promover
  `direito/imobiliario/` → `direito/imobiliario/rescisao-lote/` e criar o bundle irmão
  (Fase C do plano — aprovada pela titular em 2026-08-01, execução sob demanda).

## 2026-07-22

**Verificação oficial + resolução de pendências (v0.1.0 → v0.2.0).** Sessão dedicada a fechar as pendências de lint da ingestão.

- **Jurisprudência STJ verificada contra fonte oficial e promovida a `status: vigente`** (7 REsp + Súmula 543):
  - Súmula 543/STJ — 2ª Seção, j. 26/08/2015, DJe 31/08/2015; enunciado literal inserido.
  - REsp 1.798.374/DF — Mauro Campbell, Corte Especial, 18/05/2022 (Inf. 737).
  - REsp 1.846.109/SP — Nancy Andrighi, 3ª Turma, 10/12/2019, DJe 13/12/2019 (Inf. 662); *ratio* precisada (distinguishing do art. 1.037 §§9-13 → agravo de instrumento).
  - REsp 1.745.407/SP — Marco Aurélio Bellizze, 3ª Turma, 11/05/2021, DJe 14/05/2021 (Inf. 696).
  - REsp 1.635.428/SC — Luis Felipe Salomão, 2ª Seção, questão de ordem 2019 (Temas 970/971); empregado só quanto à tese da irretroatividade (mérito é atraso na entrega, distinto do objeto do tema — anotado).
  - REsp 1.723.519/SP — **Maria Isabel Gallotti, 2ª Seção, 28/08/2019** (o acervo estava correto; a hipótese "Bellizze" das buscas foi descartada); retenção 25% p/ contratos pré-2018 (EAg 1.138.183/PE).
  - REsp 1.879.554/SC — Francisco Falcão, 2ª Turma, DJe 31/08/2020; matéria administrativa/previdenciária, *ratio* processual geral; acrescida cautela sobre corrente divergente (3ª Turma, 12/05/2021).
- **Correção relevante — Tema 557 → 577.** O repetitivo do REsp 1.300.418/SC é o **Tema 577** (confirmado na base de repetitivos do STJ e no próprio acórdão do REsp 2.035.848/TO, linha 88). A Tese 07 do IRDR-TO o cita, por **erro material**, como "557" — o bundle havia propagado o typo. Arquivo renomeado (`resp-1300418-tema-557.md` → `-577.md`), tese oficial literal inserida, e todas as remissões próprias corrigidas (jurisprudencia/index, teses/index, tese de restituição, REsp 1.635.428, Súmula 543, Lei 13.786). O "557" foi preservado apenas dentro das transcrições verbatim da decisão do TJTO, com `[sic — 577]`.
- **IRDR-0009560-46.2017.827.0000/TJTO** — data de fixação das teses confirmada: **28/02/2019** (Evento 318; instaurado em 2017), Rel. Des. Ronaldo Eurípedes, remetido ao STJ em 21/10/2022. `status: vigente`. **Âmbito territorial** documentado em bloco destacado na página, no roteador `atividades.md` (novo portão obrigatório) e nos índices: o IRDR vincula **apenas na jurisdição do TJTO** (art. 985, I, CPC) e a suspensão que gerou é fenômeno interno do TO — fora do TO, sustentar a tese direto pelos precedentes do STJ, sem citá-lo como vinculante. (Ponto trazido pelo titular nesta sessão.)
- **Legislação (arts. 32 e 32-A da Lei 6.766/79)** — conteúdo estruturado e conferido contra fontes secundárias (STJ Inf. 696; base de repetitivos; doutrina) inserido: incisos I-V do 32-A com percentuais (0,75% fruição; 10% cláusula penal), §1º (12 parcelas + carências) e §2º. **Permanecem `em_teste`**: a transcrição byte-a-byte não pôde ser feita porque `planalto.gov.br` recusou conexão (ECONNRESET) e os espelhos bloquearam a leitura automática — conferência literal final segue pendente para sessão com acesso ao Planalto.
- **3 acórdãos do TJTO** (IPTU 0011158-73.2023; benfeitorias 0009733-61.2021; lote×apto 0032228-40.2019) — **não localizados em fonte pública aberta** (jurisprudência do TJTO não indexada nas buscas web disponíveis); mantidos `em_teste`, com nota de verificação — dependem do depósito do inteiro teor (pendência que se soma à ingestão dos PDFs originais do TJTO, item 5 abaixo).
- **Workflows completados (2 de 2 faltantes):** `contestacao-notificacao-viciada.md` e `cumprimento-sentenca-retencao-percentual.md` redigidos no padrão dos existentes (etapas + portões), religados no `atividades.md` e no `workflows/index.md`. As 4 atividades passam a ter workflow dedicado.
- **Índices atualizados:** `jurisprudencia/index.md` (novo estado de vigência + correção do tema), `index.md` do bundle (bump **v0.2.0**), roteador global `D:\GITHUB\bundles\index.md` (entrada refrescada para v0.2.0/ativo).

### Pendências remanescentes (para o titular / próxima sessão)

1. **Anonimização do `casos_decididos/caso-a-...` + ritual de encerramento (schema 7.2)** — segue com o titular (não tocado nesta sessão).
2. **Transcrição byte-a-byte dos arts. 32 e 32-A** contra o Planalto — bloqueada por rede nesta sessão.
3. **Inteiro teor dos 3 acórdãos do TJTO** e dos originais do IRDR/EDcl do TJTO — depósito de PDF pelo titular.
4. **Casos A/B/C (em andamento, C1)** — encerramento quando houver sentença/acórdão.

## 2026-07-21

**Ingestão.** Criação do bundle piloto `direito/imobiliario/`, a pedido do titular, aproveitando o acervo `D:\WORK\advocacia\rescisao_contrato_imovel\` (4 casos reais do escritório, referidos aqui só como Caso A, Caso B e Caso C — nomes reais permanecem exclusivamente em C1, `D:\WORK\advocacia\...`: Casos A e B seguem em andamento e não geraram página; Caso C também em andamento; o quarto caso, com desfecho transitado, gerou `casos_decididos/`). Espelha a estrutura do piloto `direito/bancario/emprestimo-nao-realizado/` (schema `SCHEMA_BUNDLE_PILOTO.md`).

- **raw/**: só as 2 fontes públicas de terceiro (Laguna Empreendimentos, não cliente do escritório) já convertidas na origem — acórdão do REsp 2.035.848/TO (não conhecimento, 06/11/2025) e EDcl rejeitados (02/03/2026). Renomeados na cópia para refletir o conteúdo real (o catálogo inicial havia rotulado incorretamente o primeiro arquivo como "despacho de desafetação" — é, na verdade, o próprio acórdão de não conhecimento; a decisão de desafetação de 2023 da Min. Assusete Magalhães é mencionada dentro desse acórdão, mas não existe como arquivo próprio nesta ingestão).
- **jurisprudencia/**: 14 páginas — 2 com `raw/` (`autor: ingerido`), 12 sem PDF oficial ainda (`autor: escritorio`, `status: em_teste`), extraídas das peças do próprio escritório. Curadoria de ~40 citações do acervo para ~14 páginas — priorizados os precedentes que sustentam as teses centrais; os demais (~25 acórdãos TJTO/TJSP/TJMG/TJCE citados nas peças) ficaram de fora desta rodada.
- **teses/**: 11 páginas (o catálogo inicial identificou ~17 candidatas; consolidadas por sobreposição e pela regra de granularidade do schema).
- **heuristicas/**: 6 páginas.
- **playbooks/**: 4 páginas (inicial, contestação, agravo de levantamento de suspensão, cumprimento de sentença).
- **casos_decididos/**: 1 página — anonimizada a partir da sentença e do acórdão já lidos (autor real, incorporadora ré, comarca reduzida a nível de comarca — não bairro/distrito — vara e número de processo omitidos, datas em mês/ano). **Rascunhada sem o ritual de encerramento completo (schema 7.2)** — decisão do titular, registrada na sessão de ingestão, de priorizar a criação do bundle e completar o ritual (4 perguntas: desfecho, teses acatadas/rejeitadas, o que faria diferente, lição para o próximo caso) numa sessão futura.
- **workflows/**: 2 de 4 atividades têm workflow dedicado (inicial e agravo); contestação e cumprimento de sentença usam o playbook diretamente por ora.
- **skills/**: as 6 skills pinadas foram copiadas sem alteração de `direito/bancario/emprestimo-nao-realizado/skills/` (mesmo pipeline de redação do escritório).
- **escritorio.md**: replicado de `direito/bancario/emprestimo-nao-realizado/escritorio.md` (dado do escritório, não do tema).

### Pendências de lint

1. **Validação da anonimização do `casos_decididos/caso-a-loteamento-retencao-18-por-cento.md` pelo titular** — prioridade alta, antes de considerar a página `status: vigente`.
2. **Ritual de encerramento completo (schema 7.2)** para o mesmo caso, quando houver tempo — enriquecer as lições com a perspectiva do titular (o que faria diferente, teses rejeitadas e por quê).
3. **Verificação oficial das ~12 páginas de `jurisprudencia/` sem `raw/`**: confirmar número exato, relator, data e ementa integral contra a fonte oficial do STJ (`scon.stj.jus.br`) e do TJTO (`tjto.jus.br`) — sem acesso à internet nesta sessão (mesmo obstáculo já registrado no bundle `cobranca-honorarios` em 2026-07-21), pendência para próxima sessão com `WebFetch` funcional ou depósito de PDF pelo titular.
4. **Texto integral do art. 32 e art. 32-A da Lei 6.766/79** (redação dada pela Lei 13.786/2018) — hoje as páginas de legislação têm apenas os trechos citados nas peças do acervo, não o dispositivo completo conferido contra o Planalto.
5. **Acórdão original do IRDR-0009560-46.2017.827.0000/TJTO e dos embargos de declaração do próprio TJTO** (não os do STJ) — não estão em `raw/` desta ingestão; a página-síntese do incidente foi construída a partir das transcrições reproduzidas dentro do acórdão do STJ. Depositar os PDFs originais do TJTO quando disponíveis.
6. **Casos A, B e C (em andamento, C1) não geraram `casos_decididos/`** por falta de desfecho — considerar o encerramento quando houver sentença/acórdão, especialmente o do caso com o agravo de levantamento de suspensão, que é o mais avançado estrategicamente.
7. **Seleção curada de jurisprudência de outros TJs** (TJSP, TJMG, TJCE) usada nas tutelas de urgência de suspensão de parcelas vincendas — não ingerida nesta rodada; considerar se o volume justificar sua própria seção.
8. `README.md`/`índice raiz` do roteador global (`D:\GITHUB\bundles\index.md`) a atualizar, movendo esta entrada de "planejado" para "ativo" (próxima etapa desta mesma sessão).
