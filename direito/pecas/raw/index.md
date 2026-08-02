# Catálogo do `raw/` — peças (transversal)

Duas naturezas convivem aqui, com regimes opostos de circulação.

## Códigos e leis — fonte transversal do acervo, circulam

Texto de lei **não é obra protegida** (Lei 9.610/98, art. 8º, IV): entra no git e viaja em qualquer pacote.

Este é o lugar onde o **código integral** mora **uma vez**. Bundles que citam artigos isolados não recebem cópia do código: recebem um **recorte** gerado por script, com cabeçalho de proveniência.

| Arquivo | Estado |
|---|---|
| `cpc-l13105-compilada.html` | **depositado** — texto compilado oficial do CPC, em `cp1252`. Estava desde 2026-07-06 em `recurso-especial/raw/`; movido para cá em 2026-08-01, quando passou a servir a todo o acervo. 14 páginas o citam no campo `raw:`. |
| `cpc-l13105-compilada.md` | **depositado** — conversão em texto do HTML ao lado, gerada em 2026-08-01. É a fonte que o `recortar-artigo.py` lê. |

**Cobertura do depósito:** a compilação incorpora alterações até a **Lei nº 14.976**. Alteração posterior a essa **não** está refletida — conferir antes de citar dispositivo sensível, e substituir o par de arquivos quando houver versão mais nova.

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

**Nunca editar recorte à mão.** Veio errado, corrige-se o script ou o depósito e regera-se — recorte editado deixa de refletir a fonte e derrota o `lint-citacoes`.

### Fila de recortes

Feitos:

- `direito/execucao/defesa-executado/raw/cpc-art-921.md` — art. 921 (prescrição intercorrente, redação da Lei 14.195/2021). Página derivada promovida a `vigente` em 2026-08-01.

Páginas `em_teste` que ainda esperam recorte:

- `direito/execucao/defesa-executado` — arts. 833, 834, 854, 525, 917.
- `direito/execucao/credor` — arts. 381 a 383, 495, 523, 524, 534, 535, 784, 798, 799, 828, 835, 844, 910.

## Obras comerciais de terceiros — não circulam

Manuais e livros de direito processual civil usados como fonte de estudo. Ficam **fora do git** (`.gitignore` §1) e na máquina de quem depositou; só o conhecimento reescrito nas páginas circula.

- `iuris-dpc-vol4-2025.{pdf,md}`
- `manual-dpc-montans-2024.{pdf,md}`
- `manual-dpc-scarpinella-2024.{pdf,md}`
- `pratica-processo-civil-gediel-2016.{pdf,md}`

Cada um tem seu `*.quality.json` — o sidecar da Etapa 0. **Ler o veredito antes do `.md`**: `reprovado` não se lê.
