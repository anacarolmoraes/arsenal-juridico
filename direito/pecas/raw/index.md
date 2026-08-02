# Catálogo do `raw/` — peças (transversal)

Duas naturezas convivem aqui, com regimes opostos de circulação.

## Códigos e leis — fonte transversal do acervo, circulam

Texto de lei **não é obra protegida** (Lei 9.610/98, art. 8º, IV): entra no git e viaja em qualquer pacote.

Este é o lugar onde o **código integral** mora **uma vez**. Bundles que citam artigos isolados não recebem cópia do código: recebem um **recorte** gerado por script, com cabeçalho de proveniência.

| Arquivo | Estado |
|---|---|
| `cpc-lei-13105-2015-compilado.{pdf,md}` | **pendente de depósito** — ver procedimento abaixo |

### Por que recorte, e não cópia

O `lint-citacoes` confere a transcrição contra um arquivo **do próprio bundle**, e o `E4` do `lint-bundle` exige depósito para promover página a `vigente`. Copiar o CPC inteiro em cada `raw/` resolveria os dois, ao custo de duplicar megabytes e de criar várias fontes canônicas do mesmo texto — exatamente o defeito que a regra de não repetir definição existe para evitar. O recorte satisfaz o lint sem duplicar o código.

### Procedimento de depósito e recorte

1. A titular baixa o PDF oficial do código e deposita em `consumir/`.
2. Converter com o `pdfmd` do `adv_env` (`PYTHONUTF8=1`, `--ocr auto --lang por`) e **conferir a saída**: procurar um artigo conhecido e ver se veio íntegro. Texto de Planalto costuma ter camada de texto; se sair magro, é sinal de PDF de imagem e o OCR precisa ser forçado.
3. Depositar o par `.pdf` + `.md` aqui, com nome que declare a versão: `cpc-lei-13105-2015-compilado.{pdf,md}`. Registrar no `log.md` deste bundle a **data da consolidação** do texto baixado — é ela que diz até que alteração legislativa o depósito cobre.
4. Para cada bundle que cite artigos, gerar o recorte a partir da raiz do acervo:

   ```
   python recortar-artigo.py 921 direito/execucao/defesa-executado
   python recortar-artigo.py 381-383 direito/execucao/credor
   ```

   Saída: `<bundle>/raw/cpc-art-921.md`, `<bundle>/raw/cpc-arts-381-383.md`.
5. **Conferir o recorte à vista** antes de transcrever em página derivada, e só então promover a página a `vigente` preenchendo `verificado_em`.

**Nunca editar recorte à mão.** Veio errado, corrige-se o script ou o depósito e regera-se — recorte editado deixa de refletir a fonte e derrota o `lint-citacoes`.

### Fila de recortes já necessária

Páginas `em_teste` que esperam depósito para virar `vigente`:

- `direito/execucao/defesa-executado` — **art. 921** (prescrição intercorrente, redação da Lei 14.195/2021), arts. 833, 834, 854, 525, 917.
- `direito/execucao/credor` — arts. 381 a 383, 495, 523, 524, 534, 535, 784, 798, 799, 828, 835, 844, 910.

## Obras comerciais de terceiros — não circulam

Manuais e livros de direito processual civil usados como fonte de estudo. Ficam **fora do git** (`.gitignore` §1) e na máquina de quem depositou; só o conhecimento reescrito nas páginas circula.

- `iuris-dpc-vol4-2025.{pdf,md}`
- `manual-dpc-montans-2024.{pdf,md}`
- `manual-dpc-scarpinella-2024.{pdf,md}`
- `pratica-processo-civil-gediel-2016.{pdf,md}`

Cada um tem seu `*.quality.json` — o sidecar da Etapa 0. **Ler o veredito antes do `.md`**: `reprovado` não se lê.
