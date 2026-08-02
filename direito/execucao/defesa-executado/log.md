# Log — defesa do executado

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
