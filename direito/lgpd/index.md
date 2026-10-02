---
okf_version: "0.1"
bundle_version: "0.1.0"
---

# LGPD — Bundle de Competência

Proteção de dados pessoais e segurança da informação: conceitos operacionais da Lei 13.709/2018, direitos do titular e — o que hoje sustenta o bundle — as **alavancas de engenharia social**, que ligam esta matéria à litigância de golpes bancários.

## Estado: semente fraca, e declarada

Este é o bundle mais magro do acervo, e o index diz por quê antes que alguém se apoie nele.

A **Lei 13.709/2018 está depositada desde 2026-09-13** no transversal `direito/pecas/raw/lgpd-l13709-2018-compilada.md` (cobertura até a Lei 15.352). O literal existe; o que falta é derivar: a única página é `em_teste` e a matéria jurídica propriamente dita — bases legais, hipóteses de tratamento, sanções, incidentes — **ainda não está coberta**. Quando um caso puxar um artigo, recortar com `recortar-artigo.py <art> direito/lgpd --codigo direito/pecas/raw/lgpd-l13709-2018-compilada.md --rotulo LGPD` e escrever a página.

O que existe de sólido é lateral e vale por si: o catálogo das alavancas psicológicas da engenharia social, que a prática do escritório usa em outro bundle.

## Seções

- [heuristicas/](heuristicas/index.md) — regras de decisão prática
- [raw/](raw/index.md) — fontes, com a fronteira de distribuição de cada uma
- [log.md](log.md) — histórico de ingestões

**Ainda não criadas:** `README.md`, `atividades.md`, `jurisprudencia/`, `teses/`, `playbooks/`, `workflows/`, `skills/`.

## Onde este bundle é usado hoje

Em [`bancario/golpes/`](../bancario/golpes/index.md). A tese central de lá é que operação fora do perfil de consumo é defeito do serviço (REsp 2.222.059/SP), e o contra-ataque recorrente da instituição financeira é atribuir culpa exclusiva à vítima. Nomear a alavanca que o golpista acionou — urgência, medo, confiança, dever legal — desloca a conversa de "o consumidor foi descuidado" para "o consumidor foi induzido", que é o terreno em que a tese ganha.

## Pendências

- ~~Depositar a Lei 13.709/2018~~ — feito em 2026-09-13 (transversal). Próximo passo: páginas de legislação para os artigos que a prática usar (candidatos: art. 42, responsabilidade do controlador; art. 46, segurança; art. 23, § 4º, notários e registradores, citado pela fonte de cartórios).
- Provimento CNJ 74/2018 e Provimento CNJ 50/2015, citados pela fonte de cartórios, **não conferidos** em fonte oficial.
- A cartilha-fonte é de **maio de 2021** e traz marcos já vencidos (aplicação de sanções "a partir de 1º/08/2021"); a atuação sancionatória da ANPD desde então não está refletida.
