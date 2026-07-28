# Log

## 2026-07-05

- **Ingestão** — **Cadeia golpeA ingerida (ritual 7.5, primeira execução real).** Derivados: 1 caso-decidido (`origem: terceiro`), 2 contra-ataques (`sentenca->tj`: um argumentativo — culpa concorrente × dever de vigilância; um **probatório** — quantum provado por extratos × saldo), 1 página de jurisprudência citável (ApCiv 5005364-95.2023.8.21.0034/RS) e o perfil da 12ª CC do TJRS. Contra-ataques com `confianca_fonte: derivado-do-voto` (razões de apelação ausentes da cadeia — caminho degradado exercitado conforme planejado). Varredura de vazamento limpa (nomes de pessoas naturais do processo excluídos das páginas derivadas, regra 6.5).
  - Conversão: sentença que estava com 11 bytes na origem converteu com score 90 via escalonamento para tesseract; acórdão score 75 (colunas da ementa intercaladas — tese de julgamento marcada como "recomposta, conferir na fonte"). Pendências: URI canônica eproc; data de julgamento do acórdão a confirmar; capturar STJ REsp 2.052.228, Súmula 568 e TJRS ApCiv 5004251-64.2019.8.21.2001 (citadas no voto); avaliar docling/marker para PDFs em colunas (gatilho da D11 possivelmente atingido).

- **Ingestão** — Bundle criado (schema v0.4, D13). Cadeias copiadas de `direito_bancario/golpes/casos_decididos` para `raw/` com reconversão pelo portão de qualidade (a conversão legada tinha `sentenca_golpeA.md` com 11 bytes — falha silenciosa desde maio — e acórdão com colunas embaralhadas).

### Matriz de completude das cadeias

| Cadeia | inicial | contestação | sentença | razões de apelação | acórdão TJ | REsp | Situação |
|---|---|---|---|---|---|---|---|
| golpeA (ApCiv 5005364-95.2023.8.21.0034/RS) | ✔ | ✘ | ✔ | ✘ (derivar do voto) | ✔ | — | ingerida (contra-ataques `derivado-do-voto`) |
| golpeB | ✔ | ✘ | ✔ | ✘ | ✘ **sem acórdão** | — | pendente — cadeia sem desfecho; localizar acórdão |
| golpeC | ✔ | ✘ | ✘ **sem sentença** | ✘ | ✔ | — | pendente — localizar sentença e razões |
