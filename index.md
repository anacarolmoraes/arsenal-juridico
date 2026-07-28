---
type: router
title: Roteador global de bundles
description: Índice de nível superior do segundo cérebro — domínios, subáreas e bundles; o agente entra aqui, escolhe o bundle e navega pelo index.md dele.
tags: [roteador, segundo-cerebro]
timestamp: '2026-07-05'
status: vigente
autor: escritorio
---

# Roteador global de bundles

Agente: topo do segundo cérebro (D6). Escolha pela **matéria**; para técnica de **peça** jurídica use o transversal `direito/pecas/` (D12) quando existir; para procedimentos operacionais do escritório, `direito/escritorio/`. Dentro de cada bundle: `index.md` para conhecer, `atividades.md` para executar.

Regras de organização: domínio = topo; subárea = um bundle até crescer (divisão em temas é proposta pelo lint, confirmada pelo titular); máximo 3 níveis; sobreposição entre áreas resolve-se por link, não por hierarquia; a fronteira do repositório é a fronteira do compartilhamento.

## Direito

- [direito/bancario/emprestimo-nao-realizado/](direito/bancario/emprestimo-nao-realizado/index.md) — fraude em consignado não contratado: teses, jurisprudência com vigência, playbooks executáveis, skills e workflows. **Piloto, H1 aprovado.**
- [direito/bancario/golpes/](direito/bancario/golpes/index.md) — golpes por engenharia social (falsa central, PIX): cadeias de litígio, **contra-ataques** e perfis de órgãos julgadores.
- [direito/pecas/](direito/pecas/index.md) — **transversal (D12)**: técnica de peça independente de matéria. **Fluxos completos (5): REsp** (anti-284, 343-A), **AREsp** (anti-182), **AgInt** (três papéis; penal 5 dias), **EDcl** (dois papéis; penal 2 dias) e **Apelação** (anti-preclusão do 1.009 §1º; causa madura); em estoque: agravo de instrumento, inicial, contestação e réplica. Raw com 4 obras de DPC (Etapa 0, regra 6.6).
- [direito/cobranca-honorarios/](direito/cobranca-honorarios/index.md) — cobrança/execução de honorários advocatícios: título executivo do contrato escrito, natureza alimentar, dispensa de custas (Lei 15.109/2025). **Semente (2026-07-21)**: só `jurisprudencia/` e `teses/`, maioria `status: em_teste` — Etapa 0 formal (raw/ + conferência oficial) pendente.
- [direito/imobiliario/](direito/imobiliario/index.md) — rescisão de compromisso de compra e venda de lote urbano: IRDR-TO com ciclo recursal no STJ já mapeado, teses de retenção/restituição/fruição, 4 workflows executáveis (inicial, contestação, agravo de suspensão, cumprimento de sentença). **v0.2.0 (2026-07-22)**, acervo `rescisao_contrato_imovel` — jurisprudência do STJ e IRDR-TO **verificada contra fonte oficial** (`status: vigente`); restam `em_teste` só as 2 leis (transcrição do Planalto pendente) e 3 acórdãos do TJTO. Atenção: o IRDR-TO vincula **apenas na jurisdição do TJTO**.

**Planejados no domínio** (criar quando o primeiro conteúdo exigir):
novos: `direito/escritorio/` (atendimento, checklist de documentos por caso, organização de pastas C1, honorários) · `direito/bancario/juros-abusivos/` · `direito/consumidor/` · `direito/lgpd/` (acervo: direito_digital) · `direito/familia/`

## Demais domínios (planejados)

- `dev-sistemas/` — decisões de arquitetura, padrões, lições de projetos com IA/Python.
- `auditoria/` — controle externo e auditoria de TI: normativos, matrizes de risco, achados-padrão, procedimentos. *(Primeiro teste da hipótese H2 — o schema generaliza para além do direito.)*
- `marketing/juridico/` (compliance OAB como heurísticas) e `marketing/comercial/` (landing pages, funis).
- `conteudo/` — YouTube/Instagram: roteiros, ganchos validados, calendário editorial.

## Regras da raiz

- Um bundle = um repositório git próprio; esta raiz versiona só o roteador.
- Camada C1 (casos concretos, dados de cliente) **nunca** entra aqui — vive em `D:\WORK\...` e referencia os bundles.
- Reorganizações desta raiz: gatilho declarado → lint propõe → titular confirma → agente move.
- Pendência de schema (v0.5): convenção de links **entre** bundles (os links absolutos atuais são intra-bundle).
