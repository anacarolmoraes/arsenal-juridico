# Bundle de Competência — Audiências (transversal)

Este bundle carrega a técnica de audiência independentemente da matéria: preparar o ato, saber qual fato está controvertido e de quem é o ônus de prová-lo, escolher a forma da pergunta conforme a testemunha, sobreviver às regras próprias do Juizado Especial e registrar o que precisa ser registrado quando o ato corre por videoconferência.

## Prompt de instalação

```
Aqui está um bundle de competência: direito/audiencias.
Leia o README, configure-o e me diga o que você consegue executar com ele.
```

## Setup para o agente

1. Ler o [index.md](index.md) — em especial o **aviso de maturidade** — e o [atividades.md](atividades.md) para despachar o pedido.
2. Rodar a verificação estrutural a partir da raiz do acervo: `python lint-bundle.py direito/audiencias`.
3. Consultar o [catálogo do raw](raw/index.md) antes de procurar fonte: os arquivos `curso-audiencias-*` são obra comercial de terceiro e podem não existir na sua máquina (ficam fora do git).

## Como executar

Entre pelo [atividades.md](atividades.md). O caminho útil quase sempre começa na [tabela de pontos controvertidos](heuristicas/tabela-de-pontos-controvertidos.md): sem ela, o resto do bundle não tem em que se apoiar.

**Este bundle sabe menos do que parece, e diz onde.** A fonte é material promocional de 2020 que entrega o diagnóstico e retém o tratamento. Cada página termina com uma seção de **lacuna declarada** apontando o que a fonte não cobre — ordem dos atos, pena de confissão, contradita e acareação, preclusão do saneamento, sistema recursal do Juizado, segredo de justiça em família. Quando a pergunta cair numa dessas lacunas, a resposta correta é dizer que o bundle não cobre e buscar fora, nunca completar de memória.

**Vigência era o problema real aqui, e o eixo de videoconferência foi reancorado em 2026-08-02** na [Resolução CNJ 354/2020](jurisprudencia/resolucao-cnj-354-2020-videoconferencia.md), depositada e transcrita — a única página `vigente` do bundle. O que a fonte do curso dizia sobre videoconferência só vale conferido contra ela. Falta o ato regulamentar do tribunal local (art. 13). O resto do bundle segue `em_teste` e sem citação conferida.

**Matéria penal está quarentenada.** Há material de audiência de custódia em `raw/` que **não foi derivado**: este bundle é de técnica cível.

## Contrato de uso

Consumidores não modificam o bundle. Produtores seguem o schema do acervo. O bundle **não contém dados de cliente**: a única peça de caso real é uma decisão judicial de processo de terceiro, anonimizada conforme a regra dura 10, com o código de acesso ao inteiro teor suprimido.

## Versão

`bundle_version: 0.1.0` — semente de 2026-08-01. Histórico e pendências no [log.md](log.md).
