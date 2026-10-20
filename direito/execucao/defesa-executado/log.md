# Log — defesa do executado

## 2026-10-20 — Tema 1.230/STJ julgado (REsp 1.894.973/PR), bundle v0.5.0

**Origem:** `consumir/` do motor trouxe `STJ_202002358023_tipo_91_298480684.pdf`, que é **o voto original do relator** (32 p., assinado 08/09/2026), com tese em duas partes e critérios percentuais. **Não foi depositado:** o portal de repetitivos do STJ e o acórdão oficial (SCON, 65 p., DJEN 21/09/2026, baixado pelo radar-jurisprudencia-stj) mostram que a segunda parte ficou vencida. Depositado o acórdão oficial em `raw/`, pseudonimizado.

- **Tese fixada** (por maioria; recurso desprovido por unanimidade): mitigação excepcional para dívida não alimentar, (a) frustrados outros meios e (b) comprovado que a constrição não compromete a subsistência digna, **cabendo ao devedor o ônus probatório**. Redação do voto-vista do Min. João Otávio de Noronha, acolhida pelo relator em aditamento. Vencidos na redação: Nancy Andrighi, Og Fernandes, Mauro Campbell Marques.
- **Vencido:** mínimo existencial sempre impenhorável; teto de 35% a 45% entre o mínimo e 50 SM (analogia à Lei 10.820/2003); graduação pela essencialidade do crédito. O voto-vista recusou percentual na tese, mas mandou usar a fundamentação como baliza do exame concreto.
- **O texto corrigiu a [tese do salário](teses/salario-impenhoravel-mitigacao-so-excepcional.md):** ela dizia que o ônus de demonstrar a preservação do mínimo existencial era "do juízo/exequente". Agora é do devedor; ao juiz fica o controle dos requisitos (aditamento, p. PDF 62). Reescritas a tese e o índice de teses (que dizia "honorários não penhoram salário", em desacordo com o EREsp 1.874.222). Atualizada a página do EREsp 1.874.222/DF (Fronteiras).
- **Pseudonimização:** o `depositar.js` deixou escapar três advogados (nome seguido de "E OUTRO(S)" ou com espaço duplo) e quatro nomes da certidão de sustentação oral, e trocou "Defensoria Pública do Estado do Rio de Janeiro" por `[ADVOGADO 13]`. Corrigido à mão; sidecar de voz regenerado.

**Pendências novas:**

1. **EDcl** juntados em 12/10/2026 (petição 1085269/2026), vista publicada em 19/10/2026. Página `em_teste` até a titular promover; conferir o julgamento dos EDcl antes de citar.
2. Votos de Nancy Andrighi e Og Fernandes (vencidos na redação) não lidos.
3. O bundle `execucao/credor` não tem tese de penhora de salário; o Tema 1.230 o favorece (ônus do devedor).

## 2026-10-07 — seis decisões do STJ (prescrição intercorrente, salário, garantia na LEF), bundle v0.4.0

**Origem:** `consumir/` do motor. Depositados em `raw/` (inteiro teor anonimizado; PDF e conversão crua fora do git) e derivadas seis páginas `vigente` em `jurisprudencia/`, com as transcrições conferidas literalmente contra o depósito:

- **EREsp 97.328/PR** (1ª Seção, 1998): execução fiscal paralisada mais de cinco anos prescreve. PDF digitalizado; cinco correções de OCR declaradas no depósito. **Achado:** o REsp 1.340.553 trata este EREsp como *leading case* da Súmula 314 e da contagem automática, mas havia penhora e a suspensão do art. 40 não foi discutida (Herman Benjamin contesta a leitura). Para contar prazo, citar a tese 4.1 do repetitivo, não o EREsp.
- **REsp 1.102.554/MG** (repetitivo, 1ª Seção, 2009): arquivamento por baixo valor (art. 20 da Lei 10.522/2002) não impede a prescrição intercorrente; prazo da decisão de arquivamento. **Achado:** a ementa do REsp 1.230.558/PE (transcrita no REsp 1.340.553) diz que este repetitivo exigiu oitiva prévia da Fazenda; o acórdão diz que isso não foi objeto do recurso.
- **AgInt no REsp 2.231.082/TO** (1ª Turma, 2026): execução fiscal do Estado do Tocantins; prescrição mantida por Súmula 283/STF. A regra de que bloqueio irrisório não interrompe é do TJTO, não do STJ; a tese 4.3 dos Temas 566-571 ("ainda que parcial") pesa contra ela.
- **REsp 1.986.517/PR** (monocrática, 2022): diligências infrutíferas não suspendem nem interrompem. Reforça a [tese de prescrição intercorrente](teses/prescricao-intercorrente-corre-da-primeira-tentativa-infrutifera.md).
- **EREsp 1.874.222/DF** (Corte Especial, 2023, mérito 8 x 5): fecha a pendência nº 4 de 2026-08-01. **O texto corrigiu a [tese do salário](teses/salario-impenhoravel-mitigacao-so-excepcional.md):** a ementa não fixa percentual (o "20–30%" era prática de tribunal); a mitigação independe da natureza da dívida, então afastar o § 2º não fecha a penhora. Tese segue `em_teste`.
- **AREsp 2.711.567/SP** (monocrática, 2024): só negou omissão; a garantia ínfima para o art. 16, § 1º, da LEF é voz do TRF3. Ligado ao playbook de embargos.

Também atualizadas, com edição mínima: a página da LEF art. 40, a do REsp 1.954.380/SP e o playbook de embargos.

**Segunda leva do mesmo dia:**

- **Lei 10.522/2002** depositada em `raw/` (cobertura até a Lei 14.973/2024) — fecha a pendência 2 abaixo. O art. 20, na redação da Lei 13.874/2019, não fixa mais valor (remete a ato do PGFN); a página do REsp 1.102.554 dizia R$ 10.000 e foi corrigida.
- **REsp 1.954.382/SP** (repetitivo, Corte Especial, 05/06/2024, 7 x 5): inteiro teor depositado; a página `resp-1954380-...` passou de `em_teste` a **`vigente`**. **O texto corrigiu a página:** a tese fala só da verba *sucumbencial* (não "sucumbenciais ou contratuais"); a definição de prestação alimentícia é do REsp 1.815.055/SP, não do repetitivo; o relator ressalva que a mitigação excepcional segue possível para qualquer credor e, no aditamento, alcança os 40 SM do inciso X. Atualizadas a tese do salário, a página do EREsp 1.874.222 e, no bundle `cobranca-honorarios`, a tese `natureza-alimentar-privilegio`. Pendentes: DJe e trânsito, acórdão do REsp 1.954.380/SP, número do Tema (1.153 aparece só no voto-vogal da Min. Nancy Andrighi), autor do voto-vogal das p. 102-105.

**Pendências novas:**

1. Número do Tema do REsp 1.102.554/MG — não está no documento nem no acervo.
2. Lei 10.522/2002 (art. 20, valor de alçada) não depositada.
3. Acórdão do TJTO da origem do AgInt 2.231.082 (5000360-60.2009.8.27.2731), que contém a tese da penhora irrisória: depositar antes de citar.
4. EREsp 1.874.222/DF: voto do relator e notas taquigráficas; identificar o autor do voto-vogal e renomear o depósito.
5. EREsp 97.328/PR: trechos não conferidos na imagem (p. 4, voto vencido p. 9–10, ementas p. 6–7).
6. "RESP 106574" (Min. Eliana Calmon) citado pelo TRF3 no AREsp 2.711.567: número possivelmente truncado; não citar sem depósito.

## 2026-09-04 — REsp 2.188.970/PR: direito intertemporal da Lei 14.195/2021 em execução civil, bundle v0.3.0

**Depositado o inteiro teor do REsp 2.188.970/PR** (Quarta Turma, rel. Min. João Otávio de Noronha, j. 18/03/2025) em `raw/resp-2188970-pr-prescricao-intercorrente-execucao-civel.md` (anonimizado — procurador do Estado e advogado do recorrido viraram rótulo; PDF oficial e `.integral.md` com os nomes ficam fora do git, mesmo padrão do REsp 1.340.553/RS) e derivada a página `jurisprudencia/resp-2188970-pr-prescricao-intercorrente-execucao-civel.md`, **`vigente`**. Conversão pelo `pdfmd` com OCR (o texto nativo do PDF vinha corrompido, mesmo padrão já visto no PDF da resolução CNJ e no manual do STJ); conferido, 0 ligadura partida.

**Fecha uma das duas pendências da [tese de prescrição intercorrente](teses/prescricao-intercorrente-corre-da-primeira-tentativa-infrutifera.md):** agora há precedente conferido sobre o **direito intertemporal** da Lei 14.195/2021. O caso é execução civil (título extrajudicial) ajuizada em 1996, atravessando CPC/1973, CPC/2015 original e o CPC/2015 pós-2021 — o STJ segmenta a linha do tempo em três períodos e reforma o TJPR por aplicar retroativamente a regra automática de 2021 a uma suspensão de 2011-2012.

**Achado de método, não só de conteúdo — e um exemplo real da armadilha de voz que o portão de citações existe para bloquear.** O voto transcreve o acórdão do TJPR (fl. 641) dizendo que os Temas 566-571 (fiscais, REsp 1.340.553/RS) são "igualmente aplicáveis às execuções cíveis". **É a voz do TJPR, dentro de uma transcrição — não uma tese do STJ.** O próprio STJ rejeita esse fundamento duas linhas depois, decidindo por um caminho mais estreito (direito intertemporal do art. 921, §4º, dentro do próprio CPC). A página documenta a armadilha em detalhe, com aviso explícito para não citar o acórdão como "o STJ estende os Temas fiscais às execuções cíveis".

## 2026-08-02 (quarta entrada) — Temas 566 a 571 conferidos: a pendência que travava a execução fiscal caiu

**Ingestão** — Depositado o recorte oficial do **REsp 1.340.553/RS** (Temas 566 a 571) e dos seus **embargos de declaração**, e derivada a página `jurisprudencia/resp-1340553-rs-temas-566-571-prescricao-intercorrente-fiscal.md`, **`vigente`**. 1ª Seção, rel. Min. Mauro Campbell Marques, j. 12/09/2018, DJe 16/10/2018, **trânsito em julgado 14/05/2019**.

**Fecha a pendência nº 1 que a página da LEF declarava** desde 2026-08-02 de manhã — a que dizia, com todas as letras, que "o STJ interpretou o art. 40 em recurso repetitivo [...] nada disso está conferido no acervo — é a pendência que impede a defesa em execução fiscal de ser construída aqui". A pendência foi escrita de manhã e fechada à tarde, com os PDFs que a titular baixou.

**Origem da pista:** camada de consumo (KB do canal @JoseAndradeneto), que citava "Temas 566 e 567" a partir de legenda automática de YouTube. A pista estava certa quanto à existência e ao número; **estava incompleta quanto à extensão** — são seis temas, não dois, todos do mesmo paradigma.

**Três coisas que só a leitura do inteiro teor entregou:**

1. **Os EDcl alteraram a ementa.** Foram parcialmente acolhidos, sem efeitos infringentes, para **retirar do item 3 a expressão "pelo oficial de justiça"**, e esclareceram que a não localização do devedor ou de bens se constata "por quaisquer dos meios válidos admitidos pela lei processual". Muita fonte secundária ainda reproduz a redação original — quem a usa dá ao adversário o argumento de que o termo inicial dependeria de diligência de oficial de justiça. Depositar só o acórdão principal teria deixado esse defeito no acervo.
2. **A "retroatividade" da tese 4.3** é o contra-argumento mais forte da Fazenda e não aparece em resumo nenhum: requerimento feito dentro do prazo que **depois** se revele frutífero interrompe a prescrição **retroativamente, na data do protocolo**. Fechar a conta sem varrer os requerimentos pendentes é errar a favor do adversário.
3. **A Súmula 314/STJ** está transcrita e reafirmada no item 2 da própria ementa — o que fecha também a segunda metade da pendência ("há súmula sobre o tema"), sem precisar de fonte separada.

**Um erro de método registrado para não se repetir:** a primeira consulta às fichas dos seis temas no site do STJ, feita sem cruzar com a ementa, devolveu teses trocadas entre os temas 569, 570 e 571 e grafou "efetiva **construção** patrimonial" onde o acórdão diz "efetiva **constrição** patrimonial". A tabela tema → tese da página nova foi montada cruzando a **questão submetida a julgamento** de cada ficha com o bloco de teses do acórdão. Ficha de site é índice, não fonte.

**Pendência de segundo grau, nova:** **RE 636.562/SC** (STF, repercussão geral) discute a constitucionalidade do prazo de 1 ano de suspensão do art. 40. O próprio relator do repetitivo registrou que o julgado "poderá a ele ser adaptado, caso se entenda pela retirada desse prazo inicial de 1 (um) ano". Conferir o desfecho antes de usar a contagem em peça.

**Escopo inalterado:** continua **não havendo bundle de execução fiscal**. O que esta entrada acrescenta é lastro jurisprudencial para a **prescrição intercorrente** fiscal e para a fronteira com o art. 921 do CPC — não o rito da LEF (competência, CDA, garantia, ordem do art. 11).

## 2026-08-02 (terceira entrada)

**Ingestão** — Depositada a **Lei 8.009/1990** e derivada a página `jurisprudencia/lei-8009-1990-bem-de-familia.md`, **`vigente`**, com dez transcrições conferidas. Também depositada a **Lei 8.629/1993** (conceito de módulo fiscal, para a tese da pequena propriedade rural) e os recortes do **CC art. 1.911** (cláusula de inalienabilidade) e da **Lei 8.629, art. 4º**.

**O rótulo de revogado provou seu valor no primeiro uso.** Na Lei 8.009 ele revelou que o **inciso I do art. 3º está revogado pela LC 150/2015** — dívida com empregado doméstico deixou de excepcionar a impenhorabilidade — e que o **inciso III foi alterado pela Lei 13.144/2015**, ganhando a ressalva dos direitos do coproprietário em união estável ou conjugal. Sem a marcação, a redação velha estaria no acervo como se fosse vigente, e é justamente o rol que o exequente tenta encaixar.

A conferência da página foi feita contra a fonte **com os trechos revogados removidos**, para garantir que nenhuma transcrição viesse de texto morto.

**A tese do bem de família segue `em_teste`, e agora por um motivo mais preciso:** a base legal está fechada e conferida; o que falta é o inteiro teor dos precedentes e das Súmulas 364, 449 e 486, que é onde a tese realmente se apoia.

## 2026-08-02 (segunda entrada)

**Ingestão** — Depositada a **Lei 6.830/1980 (LEF)**, a partir do HTML oficial do Planalto fornecido pela titular. Derivada a página `jurisprudencia/lei-6830-1980-art-40-prescricao-intercorrente-fiscal.md`, **`vigente`**, com transcrição conferida palavra a palavra contra o depósito.

**Por que uma lei fiscal entra num bundle de execução comum.** Para fechar uma fronteira que estava declarada como pendência e agora tem texto: o art. 40 da LEF é **oposto** ao art. 921 do CPC no ponto que decide. No CPC o prazo **corre** desde a ciência da primeira tentativa infrutífera; na LEF ele **não corre** enquanto não localizado devedor ou bens, e o marco do § 4º é a decisão que ordenou o arquivamento. Quem invoca o art. 921 em execução fiscal entrega ao juízo o argumento de que aplicou norma errada. A página traz a comparação lado a lado dos dois regimes.

**Achado de método, que vale para todo depósito futuro de lei.** O HTML da LEF usa `<strike>` para a redação superada — 6 trechos. A primeira conversão achatou a marcação e passou a apresentar **texto revogado como se fosse vigente**: o art. 16, II aparecia em duas versões. Refeita a conversão, os trechos agora saem rotulados `[REVOGADO — NAO CITAR]`. O CPC compilado foi verificado e **não** tem riscado, então aquele depósito está a salvo.

**Nota de transcrição registrada na página:** o Planalto grafa os parágrafos inseridos por leis posteriores com o ordinal como letra (`§ 4o`). A transcrição normaliza para `§ 4º`; conferência palavra a palavra acusou divergência zero fora desse sinal.

**Pendência que permanece, e é a que importa:** a **jurisprudência do STJ sobre o art. 40** não está no acervo. Sem ela, a página serve para marcar fronteira, não para construir defesa em execução fiscal — que segue sem bundle.


## 2026-08-02

**Ingestão** — Depositados os recortes do CPC que faltavam: `cpc-arts-833-834` (impenhorabilidade), `cpc-art-854` (penhora eletrônica e o prazo de 5 dias), `cpc-art-525` (impugnação) e `cpc-art-917` (matérias dos embargos). Gerados por `recortar-artigo.py` a partir do depósito transversal e **conferidos um a um**: fronteira de artigo, ausência de ruído de conversão, completude de incisos, alíneas e parágrafos.

Conferência dirigida aos dois pontos em que a conversão do PDF do Planalto havia falhado no dia anterior: o **rol I a VII do art. 525, §1º** está completo, e as **alíneas do art. 798** sobreviveram — confirmando que o depósito vindo do HTML é a fonte correta.

**Isto ainda não promove página nenhuma.** Depósito não é página: falta escrever as páginas `legislacao` derivadas desses quatro recortes. Até que existam, as quatro teses de impenhorabilidade seguem `em_teste`.

## 2026-08-01 (segunda entrada)

**Ingestão** — Prescrição intercorrente entrou no bundle, por decisão de arquitetura da titular: é **matéria de defesa**, e não ganha bundle próprio.

- `jurisprudencia/cpc-art-921-prescricao-intercorrente.md` — descreve o regime na redação da **Lei 14.195/2021** (nova redação dos §§ 4º e 5º; acréscimo dos §§ 4º-A, 6º e 7º). **Sem transcrição depositada:** o Planalto estava inacessível na sessão de ingestão. A página descreve a arquitetura da norma e proíbe citação literal até o depósito.
- `teses/prescricao-intercorrente-corre-da-primeira-tentativa-infrutifera.md` — como montar a alegação: datar a primeira frustração, qualificar cada ato posterior como interruptivo ou não, somar, e pedir a oitiva prévia do § 5º.

**Decisão de arquitetura registrada.** Não se criou `direito/execucao/prescricao-intercorrente/`. Três razões: bundle é matéria, não instituto; a regra do roteador global manda resolver sobreposição por link, não por hierarquia; e o `lint-bundle.py` descarta bundles aninhados mantendo o mais externo, de modo que uma camada-mãe em `direito/execucao/` engoliria `credor/` e `defesa-executado/`. O bundle do credor guarda só a conduta inversa e aponta para cá.

**Gatilho declarado para revisão futura.** Há três institutos bilaterais no domínio — prescrição intercorrente, fraude à execução e impenhorabilidade. Quando os três tiverem páginas próprias nos dois lados, propor à titular a criação de `direito/execucao/comum/` como terceiro irmão, migrando a camada de norma e deixando em cada lado apenas a tática. Antes disso, não fragmentar.

**Pendências novas (bloqueantes para citação):**

1. ~~Depositar o CPC e recortar o art. 921.~~ **FEITO em 2026-08-01.** Achado do dia: o CPC compilado **já estava no acervo desde julho**, dentro de `direito/pecas/recurso-especial/raw/`. Foi movido para `direito/pecas/raw/` (fonte transversal), convertido para texto, e o recorte do art. 921 gerado em `raw/cpc-art-921.md` por `recortar-artigo.py`. A transcrição foi conferida letra por letra e a página promoveu a **`vigente`** — a primeira do bundle. *(O PDF que a titular depositou em `consumir/cpc_01082026.pdf` estava com 0 byte, mas era desnecessário.)*

   **O texto real corrigiu três imprecisões da descrição anterior:** a suspensão do § 4º ocorre **uma única vez**; o § 4º-A, além de restringir a interrupção, **protege o credor diligente** (o prazo não corre pelo tempo dos atos, se ele cumpriu os prazos); e o § 5º autoriza expressamente o reconhecimento **de ofício**, com extinção **sem ônus para as partes**. O § 7º estende o regime ao cumprimento de sentença. A heurística do bundle do credor foi corrigida no mesmo movimento.
2. Conferir o dispositivo da Lei 14.195/2021 que promoveu a alteração.

   **Adendo do mesmo dia:** a titular forneceu o PDF oficial do Planalto impresso em 2026-08-01. Comparado ao depósito artigo por artigo, **o art. 921 é idêntico** — a transcrição `vigente` está confirmada contra duas fontes independentes, e a Lei nº 15.479/2026 não alterou o Código. A conversão do PDF, porém, foi **rejeitada** por corromper outros artigos (o 525 perdeu o rol do § 1º); detalhes no [catálogo do raw transversal](../../pecas/raw/index.md).
3. Levantar jurisprudência **posterior a 2021** sobre a fixação da "ciência da primeira tentativa infrutífera" e sobre **direito intertemporal** (execuções em curso quando a lei entrou em vigor) — os dois pontos mais disputados e ambos ausentes do acervo.
4. Não transportar a tese para **execução fiscal**, que tem regime próprio (Lei 6.830/80 e súmula específica do STJ), também ausente do acervo.

## 2026-08-01

**Ingestão** — Semente v0.1.0 do bundle, criada a partir de `consumir/EXECUCOES_DEFESA_EXECUTADO` (workspace da titular):

- `raw/`: 6 arquivos do curso "Método MMA" (Prof. José Andrade — obra comercial, fora do git, `.gitignore` §1), acórdão oficial de **afetação** do Tema 1.235/STJ (ProAfR no REsp 2.061.973/PR) e petição real de bem de família de processo de terceiro (TJSP), **anonimizada** conforme regra dura 10 (varredura de vazamento limpa; PDF fora do git).
- Páginas derivadas, todas `em_teste`: 2 de jurisprudência (Tema 1.235; repetitivo REsp 1.954.380/SP), 4 teses (40 SM, bem de família, salário, pequena propriedade rural), 4 heurísticas (primeira manifestação, escolha do meio pela fase, checklist probatório, EPE), 2 playbooks (impugnação SISBAJUD, embargos à execução).
- Manifesto de distribuição atualizado na raiz (`.gitignore` + `distribuicao.json`): `metodo-mma-*` e o PDF da petição nunca rastreados; `.md` anonimizado e catálogo circulam na equipe mas não em pacote externo.

**Pendências de conferência (bloqueiam promoção a `vigente`):**

1. **Tema 1.235/STJ** — baixar o inteiro teor do acórdão de MÉRITO (REsp 2.061.973/PR, Corte Especial, j. 02/10/2024, DJe 07/10/2024) e conferir a tese literal; a afetação já está em `raw/`.
2. **Tema 1.285/STJ** (REsps 2.015.693 e 2.020.425 — 40 SM em conta-corrente/fundos/papel-moeda) — estava com voto-vista pendente à época da fonte; conferir se foi julgado e qual a tese.
3. **REsp 1.954.380/SP e 1.954.382/SP** (honorários × §2º do 833) — confirmar número do Tema repetitivo, texto da tese e trânsito.
4. **EREsp 1.874.222/DF** (mitigação da impenhorabilidade do salário) — inteiro teor.
5. **REsp 1.913.234/MT** (ônus da prova na pequena propriedade rural) e **ARE 1.038.507 RG/STF** (número da tese de repercussão geral) — inteiro teor.
6. **Bem de família**: REsp 1.639.337/MG, EAREsp 2.141.032/GO (Info 840) e Súmulas 364, 449 e 486/STJ — conferência e depósito.
7. Rol do art. 833 e Lei 8.009/90 — depositar texto vigente do Planalto em `raw/` (mesmo padrão da Lei do Cheque no bundle de execução de cheque).

**Fora de escopo declarado:** material de `consumir/EXECUCOES_CREDOR` (lado exequente) — candidato a bundle irmão `direito/execucao/credor/` quando a titular pedir.
