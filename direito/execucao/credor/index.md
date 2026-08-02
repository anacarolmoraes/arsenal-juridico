---
okf_version: "0.1"
bundle_version: "0.3.0"
---

# Execução pelo Credor — Bundle de Competência (Execução Civil)

Como fazer o crédito virar dinheiro: qualificar o título, montar o requerimento sem errar o cálculo, encontrar patrimônio quando as consultas voltam negativas, alcançar o bem que está em nome de terceiro e manter a execução andando para que ela não morra no arquivo. Agentes: leiam o [atividades.md](atividades.md) para executar.

## Seções

- [README.md](README.md) — onboarding do agente consumidor
- [atividades.md](atividades.md) — roteador: situação → conhecimento obrigatório
- [jurisprudencia/](jurisprudencia/index.md) — a base legal da ação probatória, duas súmulas de admissibilidade e o precedente da penhora de restituição de IR
- [teses/](teses/index.md) — ação probatória autônoma para revelar patrimônio, penhora da restituição de IR, honorários do beneficiário, MS no Juizado
- [heuristicas/](heuristicas/index.md) — seis regras de decisão sobre busca, prevenção e movimento do processo
- [playbooks/](playbooks/index.md) — título extrajudicial, cumprimento de sentença e Fazenda Pública
- [raw/](raw/index.md) — curso de terceiro, fora do git, com o inventário de erros já mapeados
- [log.md](log.md) — histórico e pendências

## O tema num parágrafo

A execução se perde por inércia, não por falta de direito, e desde 2021 ela se perde mais rápido do que o credor imagina: pela Lei 14.195/2021, o prazo da prescrição intercorrente corre da **ciência da primeira tentativa infrutífera** de localizar devedor ou bens, sem depender de despacho algum, e **só citação, intimação ou constrição efetivas o interrompem** — petição protocolada não interrompe nada. No Juizado é pior ainda, porque o art. 53, §4º, manda extinguir de imediato quando não há devedor nem bens. Contra isso, três movimentos. **Prevenir**, antes de o bem sumir: certidão de admissão da execução averbada nos registros, hipoteca judiciária constituída com a simples apresentação de cópia da sentença no cartório, penhora averbada pelo próprio exequente — nenhum impede a venda, todos a tornam presumidamente fraudulenta. **Procurar** com prioridade para o que tem chance de se efetivar, pedindo os sistemas um a um e lendo a declaração de renda pelo que só ela mostra: o aluguel de imóvel que não está no nome dele, o empréstimo que ele fez a terceiro, a compra que ele escriturou e nunca registrou. E, quando o bem aparece na mão do executado mas no nome de outro, **constituir a prova fora da execução**, pela ação probatória autônoma do art. 381, §5º, que dá contraditório onde o procedimento executivo não tem instrução.

**v0.3.0 (2026-08-02).** Semente extraída de um curso de terceiro de 2020, ainda quase toda `em_teste`. **Quatro exceções `vigente`, com transcrição conferida contra o depósito:** o [REsp 2.192.857/DF](jurisprudencia/resp-2192857-df-penhora-restituicao-ir.md) e a [tese da penhora da restituição de IR](teses/restituicao-de-ir-e-penhoravel-onus-do-executado.md), o [CC, arts. 389 e 406](jurisprudencia/cc-arts-389-406-juros-e-correcao.md) (juros e correção, que era lacuna bloqueante) e a [Res. CNJ 115/2010, art. 5º](jurisprudencia/resolucao-cnj-115-2010-honorarios-no-precatorio.md) (honorários no precatório — leia a pendência de vigência dela). Fora delas, **nenhuma citação foi conferida contra fonte oficial** — checar o status na própria página antes de citar.

## Aviso de maturidade

A fonte é boa em estratégia e ruim em atualidade. Três consequências, declaradas em cada página:

1. **Nomenclatura de sistemas vencida.** O material é de meados de 2020 e desconhece a repetição automatizada de ordens de bloqueio e metade das centrais hoje disponíveis. As categorias de busca valem; os nomes, listas e links não.
2. **Erros de citação mapeados.** Nove erros de numeração de artigo e atribuição de tribunal estão inventariados no [catálogo do raw](raw/index.md). Nenhum foi reproduzido nas páginas, mas quem for ao material original precisa saber que existem.
3. **Lacunas bloqueantes.** Prescrição intercorrente (art. 921) **não aparece uma vez** no material — em curso dirigido ao credor, e pior: ele ensina como boa uma tática que a **Lei 14.195/2021** esvaziou, porque requerimento pendente não interrompe o prazo. A norma passou a existir no acervo em 2026-08-01, no [bundle irmão](../defesa-executado/jurisprudencia/cpc-art-921-prescricao-intercorrente.md), ainda `em_teste`. Também faltam a inscrição em cadastro de inadimplentes (art. 782, §3º), o protesto da decisão (art. 517), a penhora eletrônica (art. 854) e **qualquer critério de juros e correção** — o art. 406 do Código Civil, alterado pela Lei 14.905/2024, atinge diretamente todo demonstrativo montado a partir daqui.

## Fronteiras

O lado passivo é o bundle irmão [defesa do executado](../defesa-executado/index.md) — consultar sempre antes de peticionar, para antecipar a impenhorabilidade que virá. Execução de cheque tem bundle próprio em [direito/cambial/](../../cambial/execucao-cheque/index.md) e cobrança de honorários em [direito/cobranca-honorarios/](../../cobranca-honorarios/index.md). Técnica de audiência é do transversal [direito/audiencias/](../../audiencias/index.md).
