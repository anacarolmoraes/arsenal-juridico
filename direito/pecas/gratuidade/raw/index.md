# Catálogo do `raw/` — gratuidade

| Arquivo | Papel |
|---|---|
| `stf-adc-80-agr-2023-admissibilidade.{pdf,md,quality.json}` + `.md.estrutura.json` | **STF, ADC 80 AgR/DF, Plenário, j. 18/10/2023** (33 p.). Inteiro teor público do STF, sem parte privada: PDF e `.md` circulam. Depositado em 05/09/2026 de `consumir/` do workspace. Conversão pelo `pdfmd` **com `--no-tables`** e com a supressão automática da camada de texto duplicada (272 blocos, `duplicate_layer` no manifesto) — sem as duas correções, cada parágrafo saía em dobro e a prosa justificada virava tabela. Sidecar por `score_markdown` (75, aprovado; penalidade `muitos_artefatos` = os 33 rodapés de autenticação). Sidecar de voz pelo `segmentar-acordao.py`: 8 blocos citados sem atribuição rastreável (cabeçalhos em caixa alta e ementas coladas nos votos) — conferir antes de citar qualquer trecho entre aspas. |
| `cpc-arts-98-102.md` | Recorte do CPC compilado (`direito/pecas/raw/`), gerado por `recortar-artigo.py 98-102`. Não editar; regerar. |
| `cpc-art-1072.md` | Recorte do CPC compilado, `recortar-artigo.py 1072`. A lista de dispositivos revogados sai em linhas curtas; a página derivada lê o inciso inteiro. |

**Falta:** acórdão de mérito da ADC 80 (j. 03/09/2026), não publicado na data do depósito. A
página `jurisprudencia/stf-adc-80-merito-2026.md` fica `em_teste` até ele chegar aqui.
