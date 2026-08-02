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
- [direito/bancario/golpes/](direito/bancario/golpes/index.md) — golpes por engenharia social (falsa central, PIX): cadeias de litígio, **contra-ataques** e perfis de órgãos julgadores. Desde 2026-08-02 inclui o **REsp 2.222.059/SP** (`vigente`, inteiro teor depositado) — operações fora do perfil de consumo são defeito do serviço; é o precedente-mestre da skill `analise-perfil` do motor.
- [direito/bancario/juros-abusivos/](direito/bancario/juros-abusivos/index.md) — revisional de contrato bancário: juros acima da média do BACEN, exibição do contrato (art. 400 do CPC), repetição em dobro (**EAREsp 676.608/RS**, `vigente`), dano moral por onerosidade excessiva e seguro prestamista (Tema 972). **Semente v0.1.0 (2026-08-02)**, da migração do acervo local: 3 acórdãos TJSP `em_teste` com raw fora do git (anonimização pendente).
- [direito/digital/plataformas/](direito/digital/plataformas/index.md) — criador de conteúdo × plataforma (YouTube, Facebook, Instagram): desmonetização e bloqueio de conta sem infração demonstrada — o eixo é o **ônus da plataforma** de provar a violação concreta. **Semente v0.1.0 (2026-08-02)**: 3 cadeias de terceiros depositadas (raw fora do git), 3 páginas `em_teste`. A skill de peça (`desmonetizacao-plataforma`) mora no motor.
- [direito/consumidor/negativacao-indevida/](direito/consumidor/negativacao-indevida/index.md) — inscrição em cadastro de inadimplentes por dívida não reconhecida, **de qualquer fornecedor** (banco, telefonia, energia, varejo, ensino, plataforma): exatidão do valor inscrito (art. 43, § 1º), notificação prévia (§ 2º) e baixa após a quitação (§ 3º), cada uma autônoma. **Todo caso de negativação passa por aqui**; a fraude na **formação** do vínculo fica em `emprestimo-nao-realizado`. **Semente v0.2.0 (2026-07-31)**, extraída de um caso bancário; só `jurisprudencia/` e `heuristicas/`, com 2 de 3 páginas `em_teste` e Etapa 0 pendente.
- [direito/pecas/](direito/pecas/index.md) — **transversal (D12)**: técnica de peça independente de matéria. **Fluxos completos (5): REsp** (anti-284, 343-A), **AREsp** (anti-182), **AgInt** (três papéis; penal 5 dias), **EDcl** (dois papéis; penal 2 dias) e **Apelação** (anti-preclusão do 1.009 §1º; causa madura); em estoque: agravo de instrumento, inicial, contestação e réplica. Raw com 4 obras de DPC (Etapa 0, regra 6.6).
- [direito/cambial/execucao-cheque/](direito/cambial/execucao-cheque/index.md) — cobrança judicial de cheque devolvido: requisitos do título, dispensa do protesto, janela de seis meses, encargos pela taxa legal. **v0.2.0 (2026-07-28)**, com Lei nº 7.357/1985, Carta-Circular BCB nº 1.256/1985 e a tabela oficial de motivos de devolução do Banco Central depositadas em `raw/`; sem jurisprudência ingerida. **Portão obrigatório:** toda execução de cheque começa pela conferência do preenchimento da cártula.
- [direito/execucao/credor/](direito/execucao/credor/index.md) — o lado ativo: qualificar o título, montar o requerimento, procurar patrimônio em sequência, alcançar o bem em nome de terceiro (**ação probatória autônoma do art. 381, §5º** é a tese central) e impedir que a execução morra no arquivo. Inclui Fazenda Pública (precatório/RPV). **v0.2.0 (2026-08-02)**, semente de curso de terceiro de 2020: nomenclatura de sistemas vencida e **prescrição intercorrente ausente da fonte** — pendências no log. Quase tudo `em_teste`, com **duas exceções `vigente`**: o REsp 2.192.857/DF (penhora da restituição de IR, inteiro teor depositado) e a tese que o emprega — primeira promoção vinda da camada de consumo `kb-youtube`.
- [direito/audiencias/](direito/audiencias/index.md) — **transversal**: técnica de audiência independente de matéria — tabela de pontos controvertidos, matriz de perguntas a testemunha, armadilhas do Juizado, videoconferência, correspondente e dativo. **Semente v0.1.0 (2026-08-01)** e o bundle mais fraco do acervo, de propósito: a fonte é material promocional que entrega o diagnóstico e retém o tratamento; cada página declara a lacuna. Matéria penal (custódia) depositada em `raw/` e **não derivada**.
- [direito/execucao/defesa-executado/](direito/execucao/defesa-executado/index.md) — defesa de quem sofre execução ou cumprimento de sentença: escolha do instrumento pela fase (impugnação ao bloqueio SISBAJUD em **5 dias**, embargos, impugnação, EPE, petição de bem de família), teses de impenhorabilidade e checklists probatórios. Eixo: **Tema 1.235/STJ (2024)** — impenhorabilidade dos 40 SM não é ordem pública e **preclui**. **Semente v0.1.0 (2026-08-01)**, extraída de curso de terceiro (raw fora do git): todas as páginas `em_teste`, conferência oficial pendente. O lado **credor** é o irmão [`execucao/credor/`](direito/execucao/credor/index.md) (cheque fica em `cambial/`; honorários em `cobranca-honorarios/`). **Prescrição intercorrente mora aqui**, por ser matéria de defesa — ver a decisão de arquitetura no log.
- [direito/cobranca-honorarios/](direito/cobranca-honorarios/index.md) — cobrança/execução de honorários advocatícios: título executivo do contrato escrito, natureza alimentar, dispensa de custas (Lei 15.109/2025). **Semente (2026-07-21)**: só `jurisprudencia/` e `teses/`, maioria `status: em_teste` — Etapa 0 formal (raw/ + conferência oficial) pendente.
- [direito/imobiliario/](direito/imobiliario/index.md) — rescisão de compromisso de compra e venda de lote urbano: IRDR-TO com ciclo recursal no STJ já mapeado, teses de retenção/restituição/fruição, 4 workflows executáveis (inicial, contestação, agravo de suspensão, cumprimento de sentença). **v0.3.0 (2026-08-01)**: + 94 modelos Scavone catalogados em `raw/modelos-scavone/` (obra de terceiro, uso interno — cobre também possessórias, locação, usucapião, condomínio, incorporação, temas ainda **sem bundle**; semear irmão quando chegar caso). Jurisprudência do STJ e IRDR-TO **verificada contra fonte oficial** (`status: vigente`). Em 2026-08-02 as **2 leis foram depositadas e transcritas** (Lei 6.766/1979 e o art. 32-A da Lei do Distrato), fechando a pendência aberta em julho — e a transcrição corrigiu três leituras de fonte secundária, entre elas a do § 2º do art. 32-A e a atribuição do Cartório de Títulos e Documentos ao art. 33 em vez do 49. Restam `em_teste` 3 acórdãos do TJTO. Atenção: o IRDR-TO vincula **apenas na jurisdição do TJTO**.

**Planejados no domínio** (criar quando o primeiro conteúdo exigir):
novos: `direito/escritorio/` (atendimento, checklist de documentos por caso, organização de pastas C1, honorários) · `direito/cambial/` demais títulos (nota promissória, duplicata) · `direito/consumidor/` demais temas (cobrança indevida, vício do produto, serviço não contratado) · `direito/lgpd/` (o acervo `direito_digital` migrou para `digital/plataformas` em 2026-08-02 — lgpd segue planejado, vazio) · `direito/familia/`

## Demais domínios (planejados)

- `dev-sistemas/` — decisões de arquitetura, padrões, lições de projetos com IA/Python.
- `auditoria/` — controle externo e auditoria de TI: normativos, matrizes de risco, achados-padrão, procedimentos. *(Primeiro teste da hipótese H2 — o schema generaliza para além do direito.)*
- `marketing/juridico/` (compliance OAB como heurísticas) e `marketing/comercial/` (landing pages, funis).
- `conteudo/` — YouTube/Instagram: roteiros, ganchos validados, calendário editorial.

## Regras da raiz

- Um bundle = um repositório git próprio; esta raiz versiona só o roteador.
- Camada C1 (casos concretos, dados de cliente) **nunca** entra aqui — vive em `D:\WORK\...` e referencia os bundles.
- **Distribuição em duas camadas** ([distribuicao.json](distribuicao.json)): obra comercial de terceiro e PDF de processo alheio **nunca entram no git** (`.gitignore` §§1-2 — ficam na máquina de quem depositou; os catálogos circulam); pacote para fora da equipe **só** via `python empacotar.py` (o `--verificar` é portão). Nunca tornar este repositório público nem espelhá-lo.
- Reorganizações desta raiz: gatilho declarado → lint propõe → titular confirma → agente move.
- **Código integral mora uma vez, em [`direito/pecas/raw/`](direito/pecas/raw/index.md)** (transversal). Bundle que cita artigo isolado recebe um **recorte** gerado por `python recortar-artigo.py <artigo> <bundle>` — o `lint-citacoes` confere transcrição dentro do bundle e o `E4` exige depósito local, mas duplicar o código em cada `raw/` criaria várias fontes canônicas do mesmo texto.
- Pendência de schema (v0.5): convenção de links **entre** bundles (os links absolutos atuais são intra-bundle).
