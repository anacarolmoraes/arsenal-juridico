---
okf_version: "0.1"
bundle_version: "0.1.0"
---

# Juros Abusivos — Bundle de Competência

Revisão de contrato bancário por abusividade de encargos: juros remuneratórios acima da
taxa média do BACEN, venda casada de seguro prestamista (Tema 972/STJ), exibição do
contrato pelo banco (art. 400 do CPC), repetição do indébito em dobro (EAREsp 676.608/RS)
e dano moral por onerosidade excessiva.

## Seções

- [jurisprudencia/](jurisprudencia/index.md) — precedentes com comentário e status de vigência
- [raw/](raw/index.md) — fontes brutas depositadas (parte fora do git — ver catálogo)
- [log.md](log.md) — histórico de ingestões

**Ainda não criadas** (a fazer quando houver primeiro caso/peça real alimentando o bundle,
conforme SCHEMA_BUNDLE_PILOTO §11): `README.md`, `atividades.md`, `teses/`, `playbooks/`,
`workflows/`, `heuristicas/`, `casos_decididos/`, `perfis/`, `skills/`.

## O tema num parágrafo

A revisional de juros parte de dois pilares probatórios: a taxa efetivamente contratada e a
taxa média de mercado do BACEN para a mesma modalidade e época. Se o banco não exibe o
contrato pedido na inicial, o art. 400 do CPC autoriza presumir verdadeira a abusividade
alegada e aplicar a média de mercado (TJSP, Apel. 1027749-03.2022.8.26.0196). Reconhecida a
cobrança acima da média, a repetição do indébito é em dobro quando a cobrança contraria a
boa-fé objetiva, sem exigência de má-fé subjetiva (EAREsp 676.608/RS, Corte Especial, com
modulação para cobranças posteriores a 30/03/2021). Juros muito acima da média contra
consumidor hipossuficiente também sustentam dano moral (TJSP, Apel. 1006093-51.2025.8.26.0077,
taxa de 524% a.a., indenização de R$ 10.000,00). Seguro prestamista embutido sem liberdade
real de escolha da seguradora é venda casada — Tema 972/STJ (TJSP, Apel.
1014306-74.2025.8.26.0003). Os casos do escritório no tema ficam na camada C1 e não entram
aqui.

## Nota de proveniência (2026-08-02)

Semente extraída na migração do acervo local `direito_bancario/juros_abusivos/` (Fase 4 do
PRD de versionamento). Os acórdãos do TJSP e as petições iniciais são **documentos de
processo de terceiro**: os depósitos em `raw/` com dado pessoal ficam **fora do git**
(`.gitignore` §2; regra dura 10 do AGENTS.md) até serem anonimizados — o que circula são as
páginas derivadas, que citam por número e tribunal. O inteiro teor do EAREsp 676.608/RS
(cópia oficial certificada) está depositado e versionado.
