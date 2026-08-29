# Catálogo do `raw/` — peças (transversal)

Duas naturezas convivem aqui, com regimes opostos de circulação.

## Jurisprudência transversal anonimizada

- [TJGO, Ap. 5412926-72.2023 — retenção e sucumbência mínima](jurisprudencia/tjgo-ap-5412926-72-2023-retencao-sucumbencia.md) — fonte única para as derivações imobiliária e processual; nomes das partes removidos.
- [TJSP, Ap. 1006338-51.2024 — retenção de 10%](jurisprudencia/tjsp-ap-1006338-51-2024-retencao.md) — lote não edificado e ausência de despesas comprovadas; nomes das partes removidos.
- [TJSP, Ap. 1096878-68.2017 — rateio dos honorários](jurisprudencia/tjsp-ap-1096878-68-2017-honorarios-rateio.md) — redução indireta abaixo do piso do art. 85, § 2º; cópia recebida já ocultava as partes.

Somente os recortes `.md` anonimizados integram o acervo. Os PDFs permanecem na camada local da titular e não são distribuídos.

## Códigos e leis — fonte transversal do acervo, circulam

Texto de lei **não é obra protegida** (Lei 9.610/98, art. 8º, IV): entra no git e viaja em qualquer pacote.

Este é o lugar onde o **código integral** mora **uma vez**. Bundles que citam artigos isolados não recebem cópia do código: recebem um **recorte** gerado por script, com cabeçalho de proveniência.

| Arquivo | Papel |
|---|---|
| `cpc-l13105-compilada.html` | **fonte oficial canônica.** Texto compilado do CPC, em `cp1252`. Estava desde 2026-07-06 em `recurso-especial/raw/`; movido para cá em 2026-08-01, quando passou a servir a todo o acervo. 14 páginas o citam no campo `raw:`. |
| `cpc-l13105-compilada.md` | **é esta que o `recortar-artigo.py` lê.** Conversão do HTML ao lado, feita em 2026-08-01. Limpa e completa. |
| `cpc-l13105-compilada-2026-08-01.pdf` | PDF oficial do Planalto (168 p.), impresso pela titular em 2026-08-01. Guardado como artefato oficial. **Sem par `.md`, de propósito** — ver o aviso abaixo. |

**Depositados também em 2026-08-02, pelo `depositar-lei.py`:**

| Arquivo | Papel |
|---|---|
| `cc-l10406-2002-compilada.{html,md}` | **Código Civil**, transversal — citado por cambial, execução/credor e imobiliário. 2.046 artigos; cobertura até a Lei 15.068; 1 trecho revogado marcado. |
| `lei-9099-1995-juizados.{html,md}` | **Lei 9.099/1995**, transversal — citada por execução/credor e audiências. Cobertura até a Lei 14.245; **13 trechos revogados marcados**. |
| `cdc-l8078-1990-compilado.{html,md}` | **Código de Defesa do Consumidor**, transversal — citado por bancário/empréstimo-não-realizado, bancário/golpes, consumidor/negativação-indevida e imobiliário. 119 artigos; cobertura até a Lei 14.181; sem trecho revogado. Era a lacuna mais antiga do acervo. |

**Depositado em 2026-08-02 — norma de tribunal, não lei federal:**

| Arquivo | Papel |
|---|---|
| `ristj-er53.{pdf,md}` | **Regimento Interno do STJ**, transversal a toda peça dirigida ao Tribunal. Cobertura até a **Emenda Regimental n. 53**. O `.md` é a conversão pdfmd do PDF oficial, já passada pelo `reparar-ligaduras.py` — ver o aviso abaixo. Recortes gerados para `recurso-especial`, `agravo-interno` e `embargos-declaracao`. |
| `ristj-er53.ligaduras.diff` | as 793 junções de palavra partida, agrupadas em 177 formas distintas, para conferência. Toda linha é palavra do português que estava rachada (`confi rmando → confirmando`); nenhuma junção espúria. |

**Depositado em 2026-08-26 — Emenda Regimental n. 55 (regime de relevância do REsp, lado RISTJ):**

| Arquivo | Papel |
|---|---|
| `ristj-er55.{pdf,md}` | **Emenda Regimental n. 55, de 21 de agosto de 2026**, em vigor a partir de **3/9/2026**. NÃO é o Regimento consolidado — é o texto da própria emenda (19 pp.), com trechos alterados marcados "(NR)" e reticências no que não mudou. Insere o **Capítulo II-A** inteiro (arts. 255-A a 255-AE, texto integral e novo — regulamenta o regime de relevância da questão de direito federal infraconstitucional) e renumera o antigo Capítulo II-A para II-B e o antigo II-B para II-C. Também altera pontualmente, mas de forma **fragmentária** (só o trecho que mudou, não o artigo inteiro), os arts. 2º, 11, 12, 21-E, 34, 44, 104-A, 121-A, 162, 173, 177, 184-A, 185, 187, 253 e 255. Conversão pdfmd limpa (0 ligadura quebrada, 0 duplicata por OCR de imagem); as 3 páginas com anotação de PDF (1, 8, 15) foram conferidas visualmente — são o brasão da República e o logotipo do BDJur, sem conteúdo normativo. É o item "(d) acompanhar emenda regimental" que ficou pendente na ingestão da Lei 15.484/2026 (log de 2026-08-18). |

**Depositado em 2026-08-29 — RISTJ consolidado até a ER-55 (fecha a pendência aberta em 08-26):**

| Arquivo | Papel |
|---|---|
| `ristj-consolidado-er55.{pdf,md}` | **Regimento Interno consolidado**, "edição revista, ampliada e atualizada até a Emenda Regimental n. 55, de 21 de agosto de 2026" (DJe 26/08/2026), organizada pelo Gabinete do Diretor da Revista — 515 páginas. É a **fonte canônica do RISTJ a partir de agora**: traz cada artigo em sua redação pós-ER-55, com as marcas "(Incluído/Redação dada pela Emenda Regimental n. 55, de 2026)", e não em forma fragmentária como a emenda avulsa. Conversão pdfmd: 515/515 páginas, **0 aviso**, 0 página com `review_required`, 10 páginas por OCR. Veio no material da Imersão "Relevância na Prática". |
| `ristj-consolidado-er55.ligaduras.diff` | as junções de palavra partida agrupadas em **192 formas** distintas (`fi nal → final`, `confl itos → conflitos`), para conferência. Todas conferidas: nenhuma junção espúria. **`ex officio` é latim e está correto.** Uma correção manual à parte: o extrator devolveu `Aperfi çoamento` no art. 331-A, e a junção automática produziria `Aperfiçoamento` — grafia errada de qualquer modo; corrigido à mão para **`Aperfeiçoamento`** (2 ocorrências), que é como o próprio documento grafa nas outras 52 vezes. |

**⚠️ Duas armadilhas deste consolidado, para quem for recortar dele:**

1. **Duplicata por OCR de imagem** — o mesmo problema já catalogado abaixo: em cada página cujo texto também é imagem, a transcrição do OCR aparece antes do texto nativo. O recorte automático começa pela versão do OCR, que é a pior (`Art.255.0O recurso especial...`).
2. **Apêndice das emendas históricas** — o volume reproduz, ao fim, todas as emendas regimentais anteriores. Por isso `Art. 255...` reaparece dezenas de vezes com reticências, em contextos que não são o corpo do Regimento. Recorte gerado sem cuidado pega a ocorrência errada.

Por causa disso, os recortes regerados em 2026-08-29 (arts. 34, 104-A, 121-A e 255, no `recurso-especial`) passaram por **limpeza manual declarada no cabeçalho de cada um**: removidos os blocos de OCR, os marcadores de página, as imagens e os cabeçalhos correntes; para o art. 255, extração manual da ocorrência do corpo, porque o corte automático varreu os 33 artigos do Capítulo II-A para dentro do recorte (o script não percorre sequência com sufixo de letra — mesma limitação já registrada em 08-26).

**`ristj-er53.md` e `ristj-er55.md` permanecem depositados como registro histórico** — o primeiro é a consolidação anterior, o segundo é o texto da emenda tal como publicada. Para **citar em peça**, usar o `ristj-consolidado-er55.md`.

**Recorte já gerado**, em `direito/pecas/recurso-especial/raw/` (texto integral e novo, sem o problema de fragmentação acima):

| Recorte | Origem | Observação |
|---|---|---|
| `ristj-arts-255A-255AE-capitulo-iia.md` | `ristj-er55.md` | **Recorte manual**, não gerado pelo script — ele não percorre uma sequência de artigos com sufixo de letra (255-A ... 255-AE) dentro do mesmo capítulo. Removida 1 duplicata de tabela truncada (§ 1º do art. 255-AE), mantida a versão em parágrafo. Ainda não citado por nenhuma página derivada — fica pronto para quando alguém escrever a página de RISTJ sobre o procedimento da relevância. |

**Sobre a Lei n. 15.484/2026 (o lado CPC do mesmo regime, art. 1.035-A):** já estava depositada — em `recurso-especial/raw/`, via `depositar-lei.py`, HTML do DOU — desde 2026-08-15/18 (ver log deste diretório-pai, entradas de 08-15 e 08-18), com duas páginas `vigente` (`recurso-especial/jurisprudencia/cpc-art-1035a.md` e `.../lei-15484-2026-alteracoes-cpc.md`). Em 2026-08-26, ao depositar a ER-55 acima, o par `{html,md}` foi **movido para cá** (`lei-15484-2026-relevancia.{html,md}`, sem o sufixo `-resp`) — a lei altera o CPC transversal (arts. 927, 932, 979, 988, 998, 1.030, 1.039, 1.042), mesmo critério que já vale para `ristj-er53` e `cpc-l13105-compilada`; as duas páginas `vigente` tiveram o campo `raw:` atualizado para o novo caminho, texto inalterado. Também depositado `lei-15484-2026-relevancia.pdf` (PDF oficial do DOU) como artefato de referência — **sem alterar o `.md` canônico**, que continua sendo a conversão do HTML (mesmo critério do `cpc-l13105-compilada-2026-08-01.pdf`). **`cpc-l13105-compilada.md` fica PARCIALMENTE SUPERADO** nos oito artigos acima a partir de 3/9/2026, pelo mesmo motivo fragmentário do RISTJ.

### ⚠️ Conversão de PDF pode conter o texto DUAS vezes — e o recorte pega a pior

Descoberto em 2026-08-02, no depósito do RISTJ. Quando a página do PDF traz o texto também como imagem, o `--ocr-images` do pdfmd emite a transcrição da imagem num blockquote **antes** do texto nativo da mesma página. O arquivo passa a ter cada artigo duas vezes:

```
> **OCR da imagem; confiança média 91.1%:**
> ... Art.255.0 recurso especial ... S$ 1º ... óabeas corpus ...

**Art. 255. ** O recurso especial ... § 1º ... habeas corpus ...
```

O `recortar-artigo.py` recorta a **primeira** ocorrência: o recorte do art. 255 saiu com `Art.255.0`, `S$ 1º` e `óabeas corpus` — e recorte é exatamente o que a peça transcreve. Eram **429 blocos** assim, 754 mil caracteres de duplicata degradada.

**Regra que fica:** antes de depositar conversão de PDF, contar `OCR da imagem` no `.md`. Havendo ocorrência, remover com `python reparar-ligaduras.py <arquivo> --remover-ocr-de-imagem`. Páginas cujo texto só existe por OCR (`method=tesseract`) não são afetadas — ali o OCR é o corpo da página, não um blockquote duplicado.

Mesma família das duas armadilhas já catalogadas (o `<strike>` do Planalto e o truncamento do PDF do CPC): **a conversão parece boa e o defeito só aparece artigo por artigo.**

**Cobertura:** o depósito do CPC incorpora alterações até a **Lei nº 15.109, de 2025** (visível no art. 82). A **Lei nº 15.479, de 2026** aparece apenas como "Vide" na capa do PDF, **sem nota de alteração em nenhum artigo** — não mudou o texto do Código.

### ⚠️ Não converter o PDF do Planalto com o pdfmd para uso como fonte literal

Tentado e **rejeitado em conferência** em 2026-08-01. A conversão do PDF pareceu boa (612 mil caracteres, 994 artigos, mesma contagem do HTML), mas a comparação artigo por artigo contra o HTML expôs 35 divergências, e nenhuma era alteração legislativa:

- **Truncamento grave.** O art. 525 saiu com **479 caracteres contra 4.082** — perdeu o § 1º inteiro, que é o rol das matérias da impugnação ao cumprimento de sentença. O artigo pulava do *caput* para o § 5º.
- **Fragmentos deslocados.** Parágrafos apareceram em artigos aos quais não pertencem (93, 529, 662, 913), **sem nota de alteração** e com marcação de tabela vazando no meio do texto — efeito do layout de duas colunas do PDF.
- **Alíneas perdidas.** Em 12 artigos (22, 53, 152, 313, 487, 620, 653, 742, 798, 932, 967, 984) as letras `a)`, `b)`, `c)` desapareceram.
- **Hífens comidos.** Em 16 artigos, palavras compostas colaram: `salariosminimos`, `observandose`, `subrogatorias`, `aplicandose`. Isso sozinho já derrota o `lint-citacoes`, cuja normalização não reinsere espaço.
- Além disso, o `pdfmd` injeta cabeçalho e rodapé de página (data, título, URL, `139/168`) **no meio dos artigos, às vezes na mesma linha do texto legal**.

**Regra que fica:** para texto de lei, a fonte é o **HTML do Planalto**, não o PDF. O PDF serve como artefato oficial e para conferência visual. Se algum dia for preciso converter um PDF de lei, a conversão só entra no acervo depois de comparação artigo por artigo contra uma fonte limpa.

### Por que recorte, e não cópia

O `lint-citacoes` confere a transcrição contra um arquivo **do próprio bundle**, e o `E4` do `lint-bundle` exige depósito para promover página a `vigente`. Copiar o CPC inteiro em cada `raw/` resolveria os dois, ao custo de duplicar megabytes e de criar várias fontes canônicas do mesmo texto — exatamente o defeito que a regra de não repetir definição existe para evitar. O recorte satisfaz o lint sem duplicar o código.

### Procedimento de depósito e recorte

1. **Antes de baixar nada, conferir se o código já está aqui.** Foi o erro de 2026-08-01: o CPC estava no acervo desde julho, dentro de `recurso-especial/raw/`, e quase se refez o trabalho.
2. Havendo versão mais nova, depositar a fonte oficial (HTML do Planalto ou PDF) e convertê-la. **HTML do Planalto é `cp1252`, não UTF-8** — decodificar errado corrompe todo acento silenciosamente. PDF converte-se com o `pdfmd` do `adv_env` (`PYTHONUTF8=1`, `--ocr auto --lang por`).
3. **Conferir a saída** procurando artigos conhecidos, e registrar no `log.md` deste bundle **até que lei alteradora** a compilação cobre — é isso que diz a validade do depósito.
4. Para cada bundle que cite artigos, gerar o recorte a partir da raiz do acervo:

   ```
   python recortar-artigo.py 921 direito/execucao/defesa-executado
   python recortar-artigo.py 381-383 direito/execucao/credor
   ```

   Saída: `<bundle>/raw/cpc-art-921.md`, `<bundle>/raw/cpc-arts-381-383.md`.
5. **Conferir o recorte à vista** antes de transcrever em página derivada, e só então promover a página a `vigente` preenchendo `verificado_em`.

### ⚠️ Conferir se o HTML usa riscado para texto revogado

Descoberto em 2026-08-02, ao depositar a Lei 6.830/1980 em `direito/execucao/defesa-executado/raw/`: o Planalto marca a **redação superada com `<strike>`**, e a conversão automática achata a marcação. O resultado é texto **revogado apresentado como vigente** — na LEF, o art. 16, II aparecia em duas versões, e nada indicava qual valia.

Regra para todo depósito de lei: **antes de converter, contar as tags `<strike>` no HTML.** Havendo, a conversão precisa preservá-las com rótulo explícito (`[REVOGADO — NAO CITAR]`). O CPC compilado foi verificado e não tem nenhuma, por isso aquele depósito é seguro.

Outra armadilha da mesma família: o Planalto grafa o ordinal como letra nos parágrafos inseridos por leis posteriores (`§ 4o`, não `§ 4º`). A transcrição pode normalizar, mas a **nota de normalização vai na página**, para que a conferência futura não acuse divergência falsa.

**Nunca editar recorte à mão.** Veio errado, corrige-se o script ou o depósito e regera-se — recorte editado deixa de refletir a fonte e derrota o `lint-citacoes`.

### Fila de recortes

**Depositados em 2026-08-01, todos conferidos** (fronteira de artigo, ausência de ruído, completude de incisos, alíneas e parágrafos):

| Bundle | Recorte | Artigos |
|---|---|---|
| defesa-executado | `cpc-art-921.md` | 921 — prescrição intercorrente. **Página derivada `vigente`.** |
| defesa-executado | `cpc-arts-833-834.md` | impenhorabilidade e seus limites |
| defesa-executado | `cpc-art-854.md` | penhora de dinheiro por meio eletrônico (o prazo de 5 dias) |
| defesa-executado | `cpc-art-525.md` | impugnação ao cumprimento de sentença |
| defesa-executado | `cpc-art-917.md` | matérias dos embargos à execução |
| credor | `cpc-arts-381-383.md` | produção antecipada de prova |
| credor | `cpc-art-495.md` | hipoteca judiciária |
| credor | `cpc-arts-523-524.md` | cumprimento de sentença e demonstrativo |
| credor | `cpc-arts-534-535.md` | cumprimento contra a Fazenda e impugnação |
| credor | `cpc-art-784.md` | rol dos títulos executivos extrajudiciais |
| credor | `cpc-arts-798-799.md` | requisitos da inicial executiva |
| credor | `cpc-art-828.md` | averbação premonitória |
| credor | `cpc-art-835.md` | ordem de preferência da penhora |
| credor | `cpc-art-844.md` | averbação da penhora pelo exequente |
| credor | `cpc-art-910.md` | execução de título extrajudicial contra a Fazenda |

**O que os recortes ainda não fazem.** Depósito não é página. Só o art. 921 tem página derivada com transcrição conferida; os outros treze recortes estão em `raw/` esperando que se escreva a página `legislacao` correspondente, que é o que permite citá-los em peça pelo `resource` e o que o `lint-citacoes` confere. Enquanto isso, as teses e playbooks que se apoiam nesses artigos seguem `em_teste`.

**Candidatos que a fila não previu** e que os bundles citam com destaque: art. 916 (moratória legal, no playbook do extrajudicial), art. 774, V (ato atentatório, na heurística de movimento) e art. 98, §§ 2º e 3º (gratuidade, na tese de honorários).

## Obras comerciais de terceiros — não circulam

Manuais e livros de direito processual civil usados como fonte de estudo. Ficam **fora do git** (`.gitignore` §1) e na máquina de quem depositou; só o conhecimento reescrito nas páginas circula.

- `iuris-dpc-vol4-2025.{pdf,md}`
- `manual-dpc-montans-2024.{pdf,md}`
- `manual-dpc-scarpinella-2024.{pdf,md}`
- `pratica-processo-civil-gediel-2016.{pdf,md}`
- `tese-buril-objeto-dos-recursos-2019.{pdf,md}` — **tese de doutorado**, não manual: Lucas Buril de Macêdo Barros, *Objeto dos recursos cíveis: crítica ao efeito devolutivo como categoria central da Teoria Geral dos Recursos* (USP, orientação de Cruz e Tucci, 420 f.). Consumida em 2026-08-29. Predominantemente **teórica e propositiva** — boa parte é história do instituto (direito romano ao CPC/73) e direito comparado (Itália, Portugal, Espanha, Inglaterra, EUA, Argentina, Peru). O que rendeu página é o Capítulo III: a distinção extensão × profundidade e a **função residual da causa de pedir recursal** (só dialeticidade e dever de resposta) → [`apelacao/heuristicas/extensao-e-profundidade-do-devolutivo.md`](../apelacao/heuristicas/extensao-e-profundidade-do-devolutivo.md), que nasce `em_teste` por vir de fonte única. Conversão: 420/420 p., 0 aviso. **Cuidado ao recortar:** 333 das 420 páginas trazem bloco de OCR de imagem duplicando o texto nativo — mesmo problema catalogado abaixo. Ver `tese-buril-objeto-dos-recursos-2019.ligaduras.md`.

Cada um tem seu `*.quality.json` — o sidecar da Etapa 0. **Ler o veredito antes do `.md`**: `reprovado` não se lê.
