---
okf_version: "0.1"
bundle_version: "0.6.2"
---

# Rescisão Contratual de Imóvel — Bundle de Competência (Direito Imobiliário)

Rescisão de compromisso de compra e venda de lote urbano: conhecimento executável para redigir, fundamentar e validar peças no padrão do escritório PMA, com foco especial no incidente de resolução de demandas repetitivas do TJTO sobre o tema (ciclo recursal já encerrado no STJ). Agentes: leiam o [README.md](README.md) para setup e o [atividades.md](atividades.md) para executar.

## Seções

- [atividades.md](atividades.md) — roteador: atividade → workflow → skills → conhecimento
- [jurisprudencia/](jurisprudencia/index.md) — IRDR-TO, acórdãos do STJ e legislação do tema, com status de vigência
- [teses/](teses/index.md) — teses do tema, com fundamentos, contra-argumentos e placar
- [heuristicas/](heuristicas/index.md) — regras de decisão estratégica com origem rastreável
- [playbooks/](playbooks/index.md) — como construir cada tipo de peça
- [casos_decididos/](casos_decididos/index.md) — precedentes anonimizados com desfecho e lições
- [escritorio.md](escritorio.md) — subscritoras, contatos e preferências fixas (fonte única para qualificação de peças)
- [workflows/](workflows/index.md) — sequências executáveis de skills com portões de validação
- [raw/](raw/index.md) — fontes brutas imutáveis: acórdãos oficiais e os 94 modelos Scavone (uso interno, não distribuir)
- [skills/](skills/skills-lock.json) — pipeline de redação: pre-peticionamento, legal-orchestrator, legal-writer, tipografia-pma, legal-consistency-validator, peca-pma-builder
- [log.md](log.md) — histórico de ingestões, lints e alterações

**Sub-bundle** (desde 18/10/2026): [usucapiao/](usucapiao/index.md) — usucapião, aberta pela usucapião entre familiares e herdeiros (AREsp 2.983.084/AL, 4ª Turma, 2026: posse por tolerância familiar não gera animus domini). Não herda as teses de rescisão de lote; registra-se neste `log.md`.

## O tema num parágrafo

Comprador de lote urbano deseja (ou é forçado a) rescindir o compromisso de compra e venda — seja porque desistiu, seja porque a loteadora move ação de resolução/reintegração de posse. A espinha dorsal da atuação: determinar se o contrato é anterior ou posterior a 28/12/2018 (marco da Lei 13.786/2018, "Lei do Distrato" — se anterior, aplica-se o regime do STJ: retenção escalonada de 10-25%, restituição imediata em parcela única, fruição condicionada a prova de proveito econômico); verificar vícios na notificação extrajudicial que embasa a mora; e, sobretudo, atacar suspensões processuais baseadas no IRDR nº 0009560-46.2017.827.0000/TJTO cujo ciclo recursal no STJ **já se encerrou** (REsp 2.035.848/TO não conhecido em 06/11/2025; embargos de declaração rejeitados em 02/03/2026).

**v0.3.0 — ingestão dos modelos Scavone (2026-08-01):** 94 modelos de petição e o livro (9ª
ed., 2015, OCR) do material de SCAVONE JR., *Direito Imobiliário — Teoria e Prática*,
depositados na máquina da titular e **catalogados** em
[`raw/modelos-scavone/`](raw/modelos-scavone/index.md) por tema (posse, compromisso de compra
e venda, locação/despejo, condomínio, usucapião, incorporação, alienação fiduciária/leilão,
execução). **A obra em si está fora do git** (`.gitignore` §1, Lei 9.610/98) — o catálogo é o
que circula. A anatomia dos modelos `3.10.x` foi reescrita no playbook de contestação e na
heurística/tese de notificação. Os demais temas dos modelos estão **fora do escopo deste
bundle** — semear bundle irmão quando chegar o primeiro caso (plano
`2026-08-01_plano-consumo-scavone-imobiliario.md` no motor).

**v0.2.0 — verificação oficial (2026-07-22)**, migrado do acervo interno `D:\WORK\advocacia\rescisao_contrato_imovel\`. A jurisprudência do STJ (7 REsp + Súmula 543) e o IRDR-TO foram conferidos contra fonte oficial e estão `status: vigente`; permanecem `em_teste` os cinco acórdãos de tribunais locais (3 TJTO, TJGO, TJMT), que dependem do inteiro teor. Correção da rodada: o repetitivo do REsp 1.300.418/SC é o **Tema 577** (o IRDR-TO o cita, por erro material, como "557"). **O IRDR-TO vincula apenas na jurisdição do TJTO** (art. 985, I, CPC). Ver `log.md`.

**Regra do IRDR-TO (desde 29/08/2026):** só as Teses 4, 7 e 8 têm fonte direta depositada (acórdão dos EDcl de 19/11/2020, em `raw/`); as demais são paráfrase e não se transcrevem como citação literal em peça enquanto o acórdão originário de 28/02/2019 não for depositado.
