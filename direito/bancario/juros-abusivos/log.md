# Log — juros-abusivos

## 2026-08-02

**Ingestão.** Semente v0.1.0 do bundle, criada na migração do acervo local
`direito_bancario/juros_abusivos/` (Fase 4 do PRD de versionamento e modularização do
`pma-workspace`). 7 documentos depositados em `raw/` (1 versionado + 6 fora do git por
conterem dado pessoal de terceiro — regra dura 10), 4 páginas derivadas em `jurisprudencia/`
(1 `vigente`, 3 `em_teste`).

- O EAREsp 676.608/RS foi identificado pelo registro 2015/0049776-9 e confirmado por fonte
  já depositada no acervo: os EDcl no EAREsp 600.663/RS
  (`emprestimo-nao-realizado/raw/earesp-600663-rs.md`) citam textualmente "EDcl no EAREsp
  676.608/RS, Rel. Min. Og Fernandes, Corte Especial".
- A decisão do STJ sobre honorários por apreciação equitativa que estava na mesma pasta de
  origem (AREsp 2.706.690/SP) pertence à matéria de honorários e foi ingerida no bundle
  `cobranca-honorarios`, não aqui.
- O caso local `maria_helena/` é camada C1: **não migra**; segue no workspace até ir para o
  Drive do escritório.

**Pendências:**
1. Etapa 0 formal (ingest-prep.py + sidecar) para todos os depósitos.
2. Anonimizar (regra dura 10) os 3 acórdãos do TJSP e, se valerem o esforço, as 2 petições
   iniciais — só então versioná-los.
3. Conferir trânsito em julgado das 3 apelações do TJSP antes de promover a `vigente`.
4. Criar páginas próprias: Tema 972/STJ (redação oficial), Súmula 530/STJ, REsp
   1.061.530/RS (Tema 27).
5. Teses e heurísticas: a pasta de origem não tinha `estrategias/` — destilar do uso real
   quando o primeiro caso do escritório fechar (ritual 7.2).
