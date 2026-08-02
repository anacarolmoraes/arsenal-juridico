# Catálogo do `raw/` — peças (transversal)

Duas naturezas convivem aqui, com regimes opostos de circulação.

## Códigos e leis — fonte transversal do acervo, circulam

Texto de lei **não é obra protegida** (Lei 9.610/98, art. 8º, IV): entra no git e viaja em qualquer pacote.

Este é o lugar onde o **código integral** mora **uma vez**. Bundles que citam artigos isolados não recebem cópia do código: recebem um **recorte** gerado por script, com cabeçalho de proveniência.

| Arquivo | Papel |
|---|---|
| `cpc-l13105-compilada.html` | **fonte oficial canônica.** Texto compilado do CPC, em `cp1252`. Estava desde 2026-07-06 em `recurso-especial/raw/`; movido para cá em 2026-08-01, quando passou a servir a todo o acervo. 14 páginas o citam no campo `raw:`. |
| `cpc-l13105-compilada.md` | **é esta que o `recortar-artigo.py` lê.** Conversão do HTML ao lado, feita em 2026-08-01. Limpa e completa. |
| `cpc-l13105-compilada-2026-08-01.pdf` | PDF oficial do Planalto (168 p.), impresso pela titular em 2026-08-01. Guardado como artefato oficial. **Sem par `.md`, de propósito** — ver o aviso abaixo. |

**Cobertura:** o depósito incorpora alterações até a **Lei nº 15.109, de 2025** (visível no art. 82). A **Lei nº 15.479, de 2026** aparece apenas como "Vide" na capa do PDF, **sem nota de alteração em nenhum artigo** — não mudou o texto do Código.

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

Cada um tem seu `*.quality.json` — o sidecar da Etapa 0. **Ler o veredito antes do `.md`**: `reprovado` não se lê.
