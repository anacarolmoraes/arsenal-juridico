# Log — imobiliario (rescisão contratual)

## 2026-10-18 — repertório de embargos da loteadora (v0.6.1 → v0.6.2)

**Página nova** `heuristicas/repertorio-de-embargos-da-loteadora.md`, `em_teste`, por ordem da titular. Motivo: em outubro de 2026 o escritório respondeu a uma série de embargos de declaração da mesma banca adversa, todos pelo mesmo modelo, e cada contrarrazão nasceu do zero; o fluxo de `pecas/embargos-declaracao` está escrito para EDcl próprios e não tinha mapa dos embargos adversos. A página lista dezessete alegações na formulação em que aparecem, a resposta, a página do acervo, se o item conta para a multa do art. 1.026, § 2º (critério extraído das decisões da titular na série), o que não afirmar (encerramento do ciclo recursal do IRDR, objeto do Tema 1.465, composição do valor pago com cessão, páginas `em_teste` de IPTU) e o que fica reservado para a apelação. **Fonte declarada:** a experiência da titular na série; nenhum dado de caso (nome, número, evento, valor, data) entra na página. A regra transversal do repertório proíbe a pasta de cliente como fonte; aqui a titular ordenou a escrita e confere linha a linha antes de promover.

**Lacunas abertas:** fonte do agravo interno pendente no STJ contra a negativa de seguimento do RE no IRDR; Tema 1.465; Tema 938 (corretagem); página do art. 31, § 1º, da Lei 6.766/79; encargos fiscais na compensação do IPTU; enunciado da tese de IPTU que favorece a ré. Índice de `heuristicas/`, repertório transversal (`pecas/replica/heuristicas/repertorio-de-defesas-tipicas.md`) e índice de `pecas/embargos-declaracao` apontam para a página.

## 2026-10-18 — sub-bundle `usucapiao/` aberto

**Decisão de arquitetura.** O plano de 01/08 (Fase C, aprovada) mandava promover este bundle a `imobiliario/rescisao-lote/` e criar o irmão `usucapiao/`. **Não promovido**: 101 arquivos em `clientes/` do motor declaram `bundle: direito/imobiliario` e quebrariam. O tema novo entrou como **sub-bundle** (`imobiliario/usucapiao/`), no molde de `pecas/sucumbencia/`: caminho `/absoluto` resolve da raiz deste bundle (`/usucapiao/raw/...`), log aqui. A promoção continua possível quando a titular quiser pagar a migração dos `bundle:`.

**Conteúdo.** A titular mandou abrir o tema para o PDF que estava em `consumir/` desde 30/09 (`STJ_202502495907_tipo_integra_379956716.pdf`). É o **AREsp 2.983.084/AL** (4ª T., Raul Araújo, j. 09/06/2026, DJEN 06/07/2026, unânime): descendente que ocupa imóvel de ascendente, integrante de herança indivisa, tem posse por tolerância e não usucape; a usucapião entre herdeiros é "caso especial, e não a regra"; não pode contornar a legítima. Depósito pseudonimizado em `usucapiao/raw/` (partes, interessados, a falecida, seis advogados com OAB e o endereço; o PDF e o `.integral.md` fora do git, regra nova no `.gitignore`); página `vigente` em `usucapiao/jurisprudencia/`; tese `em_teste` `usucapiao-entre-familiares-exige-ruptura-da-tolerancia` com os dois lados (defesa dos herdeiros e ônus de quem pede); recortes do CC, arts. 1.203, 1.208, 1.238, 1.784 e 1.791. **Pendências** no `usucapiao/index.md`: depositar REsp 1.631.859/SP e REsp 668.131/PR (favoráveis ao herdeiro, citados como exceção) e AgInt no AREsp 2.859.266/SP; sem TJTO; modalidades além da extraordinária não cobertas.

## 2026-10-01

**Divergência entre Turmas pós-Lei 13.786 e fim do ciclo recursal do IRDR-TO.** Cinco depósitos vindos de `consumir/`, convertidos com `pdfmd --no-tables --page-breaks` e anonimizados (partes pessoas físicas e advogados; ficam magistrados, pessoas jurídicas, Defensoria, servidores da sessão e números). PDF e `.integral.md` fora do git (`.gitignore`, bloco de 01/10/2026).

- `jurisprudencia/resp-2104086-sp.md` (`vigente`): REsp 2.104.086/SP, 4ª Turma, Gallotti, 07/10/2025, maioria, vencido Buzzi. **Precedente contrário**: fruição e cláusula penal de 10% do valor do contrato dedutíveis em lote não edificado pós-2018. A página registra as quatro portas de distinção com página do PDF (item 4 da ementa, só dedução; p. 13, comprador apto a construir; p. 15, loteamento de lazer; p. 13, valor sopesado) e os limites (R$ 6.549,10 pagos, p. 12; dissídio com paradigmas pré-lei, p. 7; arts. 413 e 884 do CC não prequestionados, p. 20).
- `jurisprudencia/proafr-resp-2255370-ma-tema-1464.md` (`vigente`): afetação do **Tema 1.464** (2ª Seção, Cueva, 30/06/2026, DJEN 04/08/2026). Sem tese; suspende só REsp e AREsp. A questão afetada é percentual e base da retenção; a página adverte para não dizer que o tema decide a fruição.
- `jurisprudencia/tjgo-agint-ac-5277023-94-2025-retencao-10-pago.md` (`em_teste`): TJGO, 7ª Câmara, Proto de Oliveira, 21/09/2026, unânime. Fica `em_teste` porque o depósito é cópia de anexo sem código de autenticidade; promover depois de conferir no portal do TJGO. **Achado na anonimização**: o cabeçalho de impressão do navegador (com URL assinada do Google Storage) vinha na mesma linha do texto das páginas 31 a 33; a primeira passada apagou a linha inteira e, com ela, os itens 5 a 15 da ementa. Corrigido: só o cabeçalho sai.
- `jurisprudencia/resp-2035848-to-re-negativa-seguimento.md` (`vigente`): Vice-Presidência do STJ, Salomão, 30/07/2026, nega seguimento ao RE da loteadora (Temas 339 e 181/STF) e julga **prejudicado o efeito suspensivo**. A página adverte: trânsito em julgado não certificado.
- `jurisprudencia/irdr-0009560-46-2017-tjto-voto-relator-ev433.md` (`vigente`, `natureza: similar`, `fonte_da_tese: voto`): voto do relator Ronaldo Eurípedes, 05/09/2019, questão de ordem denegada pelo art. 980, parágrafo único. **É voto, não acórdão**: o relator ficou vencido no mérito em 19/11/2020, e o acórdão da maioria silencia sobre a questão de ordem.

Arestas: tese `cdc-prevalece-lei-distrato-contratos-pos-2018` ganha a seção "Divergência entre as Turmas (desde 2025) e Tema 1.464", dois fundamentos e o campo `contrarios:`; repertório da loteadora, linhas 2, 3 e 8 atualizadas e **linha 16 nova** (suspensão pelo Tema 1.464); heurística `atacar-premissa-fatica-exaurida-da-suspensao` ganha o RE e o segundo flanco (art. 980). Índices de `jurisprudencia/` e `raw/` atualizados.

**Não depositados, citados nas páginas como pendentes de conferência:** AgInt nos EDcl no AREsp 3.115.278/SP (Antonio Carlos Ferreira, 25/09/2026), AgInt no REsp 2.083.289/SP e REsp 2.087.740/SP (Humberto Martins, 3ª T., junho de 2026), EAREsp 3.037.983/GO (decisão de 01/09/2026), TJGO 2ª Câmara 5271612-11.2025 (suspensão pelo Tema 1.464 indeferida).

## 2026-09-13

**REsp 1.635.428/SC depositado.** Inteiro teor (70 p., `--no-tables`, segmentado) em `raw/`, anonimizado quanto ao recorrente pessoa física e aos advogados, PDF e `.integral.md` fora do git. Página `resp-1635428-sc` reescrita: `raw:`, `tese:` (Tema 970, `natureza: similar`, porque o bundle usa só a questão de ordem), transcrição literal da proposta aprovada (p. PDF 20) e do registro no voto de mérito (p. PDF 37), datas corrigidas (questão de ordem 27/03/2019; mérito 22/05/2019; DJe 25/06/2019). Fecha o E4 do bundle; os E6 das outras dez páginas continuam.

**Consumo de `consumir/REVISIONAL/`.** Sentença da 5ª Vara Cível de Palmas (0019510-40.2017.8.27.2729, 30/10/2018) e a inicial de outro escritório que a provocou, ambas sobre capitalização de juros e dupla correção em contrato de lote contra a G10, depositadas em `raw/` **anonimizadas** (regra dura 6: autora, cedente e advogados viraram rótulo; ficam o juiz, a loteadora e o número; PDF e `.integral.md` fora do git). Catalogadas em `raw/index.md` com o dispositivo resumido. Sem página derivada: tema revisional está fora do escopo ativo do bundle; o valor é o precedente local de que loteadora não integra o SFN e não capitaliza juros (Súmulas 539/541 não a alcançam), útil quando a loteadora inflar o saldo devedor na rescisão. Fecha o último item da auditoria de `consumir/` de 04/09/2026 fora do Caderno Scalabrin (que foi para `direito/pecas/raw/`).

**Páginas de legislação do art. 67-A da Lei 4.591/64 e do art. 1.358-B do CC (v0.6.0 → v0.6.1).** Fecha a pendência aberta na ingestão do Tema 1.002 (abaixo). `jurisprudencia/lei-4591-64-art-67-a.md`, `vigente`, `raw:` apontando para o depósito integral da Lei 4.591/64 já existente em `raw/`: transcrição do caput, incisos e §§ 1º a 14 gerada por script a partir do depósito (marcação "Incluído pela Lei 13.786" mantida só no caput; soft hyphen do Planalto em "admitindo-se" trocado por hífen comum, declarado na página), com leitura dos 25% do pago (inciso II), dos 50% condicionados a patrimônio de afetação provado (§ 5º), da fruição só pelo período de disponibilização (§ 2º) e da parcela única em 180 dias (§ 6º). `jurisprudencia/cc-art-1358-b-multipropriedade.md`, `vigente`, `raw: /raw/cc-art-1358-B.md`: recorte novo gerado por `recortar-artigo.py --codigo direito/pecas/raw/cc-l10406-2002-compilada.md --rotulo CC` e **aparado à mão** (o script varreu 1.358-C a U, limitação já conhecida de sufixo de letra; cabeçalho do recorte declara o aparo). A página registra que a remissão é supletiva e subsidiária, que nomeia o CDC ao lado da Lei 4.591/64 e que o Capítulo VII-A não regula a resolução da compra da fração por inadimplemento do preço (o 1.358-S trata de despesas condominiais). Repertório da loteadora, linha 15: estado `parcial` → `completa`, com o distinguishing de que o art. 67-A pressupõe incorporador. Tese `cdc-prevalece-lei-distrato-contratos-pos-2018`, item 7: aponta para as páginas. `raw/index.md` passa a listar os três depósitos de lei (6.766, 13.786, 4.591) e o recorte, que estavam fora do índice. `jurisprudencia/index.md`, seção Legislação, ganha as duas entradas.

**Ingestão do Tema 1.002/STJ (v0.5.0 → v0.6.0).** Depositado em `raw/` o inteiro teor do REsp 1.740.911/DF (2ª Seção, Rel. p/ acórdão Min. Maria Isabel Gallotti, j. 14/08/2019, DJe 22/08/2019), PDF público do STJ vindo de `consumir/`, convertido com `--no-tables` e segmentado por vozes (`segmentar-acordao.py`: 33 blocos citados sem atribuição, todos dentro do voto vencido). Página nova `jurisprudencia/resp-1740911-df-tema-1002.md`, `vigente`: a tese limita os juros do trânsito em julgado aos contratos **anteriores** à Lei 13.786/2018, e o voto vencedor (p. PDF 43) manda contar da citação nos contratos regidos pela lei nova; correção desde cada desembolso (p. PDF 42). Motivo: contestação de multipropriedade (contrato de 2023) invocou o Tema por dentro de ementa alheia. Repertório da loteadora ganhou as linhas 14 (Tema 1.002) e 15 (art. 67-A com afetação em multipropriedade); tese `cdc-prevalece-lei-distrato-contratos-pos-2018` ganhou os itens 6 (juros) e 7 (multipropriedade). **Pendências abertas:** página de legislação do art. 67-A da Lei 4.591/64 e do art. 1.358-B do CC (os textos já estão depositados: `raw/lei-4591-...` e `direito/pecas/raw/cc-...`); Lei 4.591/64 e Código Civil não foram redepositados (HTMLs novos em `consumir/` do motor, decisão da titular de manter os depósitos atuais). LINDB depositada no transversal `direito/pecas/raw/`.

## 2026-09-04

**Depósito fora de escopo, sem página derivada.** `raw/checklist-documentacao-compra-imovel-sp.md`, um checklist de due diligence para **compra** de imóvel (matrícula, certidões do vendedor PF/PJ, praxe de São Paulo), vindo de `consumir/`. Mesmo critério de escopo já registrado abaixo para os demais temas dos modelos Scavone: este bundle é rescisão de contrato já firmado, não aquisição. Fica catalogado para quando chegar o primeiro caso de aquisição imobiliária.

## 2026-08-26

**Ingestão — retenção de 10% sem prejuízo comprovado (v0.4.0 → v0.5.0).** Ingeridos os acórdãos TJGO Ap. 5412926-72.2023.8.09.0051 (`em_teste`) e TJSP Ap. 1006338-51.2024.8.26.0577 (`vigente`, inteiro teor conferido no e-SAJ). As fontes textuais anonimizadas vivem uma única vez em `direito/pecas/raw/jurisprudencia/`; os PDFs e os dados das partes não entraram no acervo. Os dois julgados tratam 25% como teto condicionado às circunstâncias e à prova de despesas, criando tensão expressa com o emprego mecânico do escalonamento do regime anterior. O conflito foi registrado na tese de retenção, sem promover o TJGO antes da conferência oficial.

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
