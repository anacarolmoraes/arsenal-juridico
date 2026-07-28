---
okf_version: "0.1"
bundle_version: "0.1.0"
---

# Cobrança de Honorários Advocatícios — Bundle de Competência

Direito civil e processual civil aplicável à cobrança e execução de honorários advocatícios: natureza jurídica, título executivo do contrato escrito, rito de cumprimento de sentença (honorários fixados judicialmente) e de execução de título extrajudicial (honorários contratuais), privilégios e prescrição.

## Seções

- [jurisprudencia/](jurisprudencia/index.md) — dispositivos legais (CPC, Estatuto da OAB) com comentário e status de vigência
- [teses/](teses/index.md) — teses aplicáveis, com fundamento e contra-argumentos
- [log.md](log.md) — histórico de ingestões

**Ainda não criadas** (a fazer quando houver primeiro caso/peça real alimentando o bundle, conforme SCHEMA_BUNDLE_PILOTO §11): `README.md`, `atividades.md`, `playbooks/`, `workflows/`, `heuristicas/`, `casos_decididos/`, `perfis/`, `raw/`, `skills/`.

## O tema num parágrafo

Honorários advocatícios têm dupla fonte de exigibilidade: fixação judicial de sucumbência (CPC, art. 85), cobrada pelo rito de cumprimento de sentença; e contrato escrito de honorários, título executivo extrajudicial por força do art. 24, caput, da Lei 8.906/94 (Estatuto da OAB), cobrado pelo rito de execução de título extrajudicial. Em ambos os casos a verba tem natureza alimentar (CPC, art. 85, §14), com impenhorabilidade limitada e privilégio em concurso de credores. A pretensão de cobrança prescreve em 5 anos (Lei 8.906/94, art. 25). Desde a Lei 15.109/2025, o advogado credor é dispensado de adiantar custas e preparo nessas ações (CPC, art. 82, §3º).

## Nota de proveniência (2026-07-21)

Conteúdo derivado de conhecimento consolidado sobre CPC e Estatuto da OAB, cruzado com a doutrina já ingerida no bundle transversal `direito/pecas/raw/` (4 manuais de DPC). **Etapa 0 formal da ingestão (SCHEMA_BUNDLE_PILOTO §7.1) não foi cumprida**: não há PDF oficial depositado em `raw/` desta pasta, e a tentativa de conferência do texto vigente via `WebFetch` a planalto.gov.br falhou por ausência de rede nesta sessão (`ECONNRESET`). Por isso a maioria das páginas de `jurisprudencia/` está com `status: em_teste`, não `vigente` — ver `log.md` para o que falta.
