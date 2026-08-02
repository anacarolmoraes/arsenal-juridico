# Log

## 2026-08-02

- **Ingestão** — Migração final do acervo local `direito_bancario/golpes/` (Fase 4 do PRD de
  versionamento do `pma-workspace`). Entradas:
  - **REsp 2.222.059/SP** (3ª Turma, Rel. Min. Cueva, j. 08/10/2025) — inteiro teor oficial
    depositado em `raw/resp-2222059-sp.{md,pdf}` (versionado; varredura limpa) e página
    derivada `vigente` em `jurisprudencia/`. Era o precedente-mestre da skill
    `analise-perfil` do motor e ainda não estava no acervo.
  - `raw/notas-jurisprudencia-stj-fraude-bancaria.md` — nota de pesquisa pré-existente
    (resumo do REsp 2.222.059 + Súmula 479); depositada como material de trabalho, não fonte.
  - `raw/notas-estrategicas-fraudes-bancarias.md` — notas estratégicas do acervo antigo
    (nomenclatura da ação, checklist pré-processual, relatório DICT, Marco Civil para IP,
    tese "ato primário × ato secundário"). **Pendência:** destilar em `heuristicas/`
    (granularidade §4 — hoje viola a regra de 1 documento = 1 conhecimento; por isso está em
    `raw/`, não em `heuristicas/`).
  - A Res. BACEN 4.753/2019 que estava em `golpes/legislacao_principal/` foi depositada no
    bundle irmão `emprestimo-nao-realizado/raw/` (a página derivada do art. 2º mora lá).
  - Criado `raw/index.md` (catálogo — a pasta não tinha índice).
  - Não migrados: `casos_decididos/*.md` locais (versões pré-anonimização das cadeias já
    reconvertidas aqui — superadas) e as pastas de caso do escritório (camada C1 → Drive).

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
