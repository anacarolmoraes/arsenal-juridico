---
type: playbook
title: Playbook — pedido de cumprimento de sentença, obrigação de pagar
description: Do teste de liquidez ao início da penhora, com as duas armadilhas que decidem o caso — a intimação por carta quando o pedido é feito depois de um ano e o fato de que o processo não anda sozinho.
tags: [cumprimento-de-sentenca, art-523, art-524, liquidacao, multa-de-10]
timestamp: '2026-08-01'
status: em_teste
autor: escritorio
peca: requerimento-de-cumprimento-de-sentenca
teses:
  - /teses/derrubar-suspensao-de-honorarios-do-beneficiario.md
skills: [peca-pma-builder, humanizer-forense]
---

# Playbook — pedido de cumprimento de sentença (obrigação de pagar)

## Passo 1 — há título executivo judicial?

Rol do art. 515: decisões civis que reconheçam exigibilidade de obrigação; homologação de autocomposição judicial ou **extrajudicial de qualquer natureza**; formal e certidão de partilha, quanto a inventariante, herdeiros e sucessores; crédito de auxiliar da justiça aprovado por decisão; sentença penal condenatória transitada em julgado; sentença arbitral; sentença estrangeira homologada; decisão interlocutória estrangeira após exequatur.

Vale lembrar o art. 519: as regras do cumprimento e da liquidação aplicam-se, no que couber, **às decisões que concedem tutela provisória**.

## Passo 2 — a sentença é líquida?

Se a apuração depender **apenas de cálculo aritmético**, promove-se desde logo o cumprimento (art. 509, §2º) — não há fase de liquidação. Havendo parte líquida e parte ilíquida, executa-se a líquida e, **em autos apartados**, liquida-se a ilíquida (§1º).

O teste que decide a modalidade: **há fato novo a alegar e provar?** Se sim — despesas médicas posteriores à sentença, por exemplo — é liquidação **pelo procedimento comum**, com 15 dias para contestação e revelia quanto à matéria de fato. Se não há fato novo, mas a conta exige técnica — recálculo de juros e índices de um contrato revisado —, é **arbitramento**, em que o juiz intima as partes a apresentar pareceres e documentos e, não decidindo de plano, nomeia perito.

Liquidação é fase, não processo: não se distribui, não se recolhem custas e, em regra, não gera honorários — salvo quando assumir nítido cunho litigioso. Não exige trânsito em julgado: pode correr na pendência de recurso, em autos apartados no juízo de origem (art. 512). Contra a decisão que a resolve, agravo de instrumento.

**Vedação central (art. 509, §4º):** na liquidação é proibido rediscutir a lide ou modificar a sentença.

## Passo 3 — competência

Art. 516: o tribunal nas causas de competência originária; o juízo que decidiu em primeiro grau; o juízo cível competente, para sentença penal, arbitral ou estrangeira. O parágrafo único permite ao exequente **optar** pelo juízo do atual domicílio do executado, do local dos bens ou do local de cumprimento da obrigação, com remessa dos autos — faculdade pouco usada e que pode encurtar muito a execução quando o devedor mudou de comarca.

## Passo 4 — qual rito

Alimentos, art. 528. Fazenda Pública, art. 534 — [playbook próprio](/playbooks/playbook-cumprimento-contra-a-fazenda-publica.md). Nem um nem outro, rito comum do art. 523. Fazer ou não fazer, art. 536; entregar coisa, art. 538.

## Passo 5 — prevenir antes de requerer

Buscar bens pelos meios que independem de ordem judicial e, sobretudo, considerar a **hipoteca judiciária do art. 495**, que se constitui pela simples apresentação de cópia da sentença no registro imobiliário — ver [averbar antes que o bem suma](/heuristicas/averbar-antes-que-o-bem-suma.md).

## Passo 6 — o requerimento (art. 524)

Demonstrativo discriminado e atualizado do crédito, contendo: nome e CPF/CNPJ de exequente e executado; índice de correção adotado; juros aplicados e respectivas taxas; termo inicial e final de juros e correção; periodicidade da capitalização, se houver; descontos obrigatórios; e indicação de bens penhoráveis, sempre que possível.

**O cálculo é responsabilidade sua, e errado ele custa caro.** A lei prevê que, se o valor aparentemente exceder os limites da condenação, a execução se inicia pelo valor pretendido mas a penhora se faz pelo que o juiz entender adequado (§1º), podendo o juízo valer-se de contabilista (§2º). Na prática isso raramente acontece: o juiz não corrige a conta do credor. Demonstrativo inflado vira impugnação por excesso acolhida, com sucumbência contra quem executou.

## Passo 7 — o procedimento, e as duas armadilhas

O juiz manda intimar o executado para pagar em **15 dias**, sob pena de multa de 10% e honorários de 10% (art. 523, §1º).

**Armadilha 1 — a forma da intimação (art. 513, §2º):** pelo Diário, na pessoa do advogado constituído; por carta com AR quando representado pela Defensoria ou **sem procurador constituído**; por meio eletrônico na hipótese do art. 246, §1º; por edital, se citado por edital e revel na fase de conhecimento. **E o §4º:** requerimento formulado **depois de um ano do trânsito em julgado** exige intimação **na pessoa do devedor, por carta com AR** — não mais pelo Diário. Errar isso é anular a intimação e recomeçar.

**Armadilha 2 — o processo não anda sozinho.** Esgotado o prazo de pagamento voluntário, é o credor quem tem de peticionar requerendo o prosseguimento com a penhora. Ninguém faz isso por ele, e o tempo parado é tempo correndo contra o crédito ([manter a execução em movimento](/heuristicas/manter-a-execucao-em-movimento.md)).

Não pagando, aplicam-se subsidiariamente as regras da execução de título extrajudicial: penhora na ordem do art. 835, formalização, depósito, intimação e **averbação pelo exequente**.

**Depósito para discutir não afasta a multa.** O executado que deposita o valor da condenação e custas sem pagar não se livra da multa de 10% nem dos honorários.

## Correção importante à fonte

O material que originou este bundle afirma, em três arquivos, que "até este momento não há imposição de honorários advocatícios" no despacho que manda intimar. **Isso descreve a praxe do despacho, não o direito.** O art. 523, §1º, prevê multa de 10% **e** honorários de 10% incidindo com o decurso do prazo — 20% de acréscimo. Quem usar aquele material como checklist deixa de pedir os honorários. Pedir sempre, expressamente.

A fonte também **omite o art. 523, §2º**: no pagamento parcial, multa e honorários incidem sobre o restante.

## O que esperar da defesa

Impugnação independe de penhora, em 15 dias contados automaticamente do fim do prazo de pagamento, com matéria restrita ao rol do art. 525, §1º. Ela **não suspende** por si: o efeito suspensivo exige garantia do juízo, fundamentos relevantes e risco de dano grave (art. 525, §6º — a fonte cita "art. 526, §6º", erro a não reproduzir).

O parcelamento do art. 916 **não se aplica** ao cumprimento de sentença (§7º). Um dos arquivos da fonte comete esse erro; os outros dois, não.

No Juizado, a multa de 10% se aplica ainda que o total ultrapasse a alçada, mas o [Enunciado 97 do FONAJE](../jurisprudencia/enunciado-97-fonaje-civel-multa-523-honorarios.md) afasta os honorários — conferido em 2026-09-04 contra o compilado oficial, redação vigente (nova redação do XXXVIII Encontro).

## Lacunas declaradas

Base de cálculo dos 10%, honorários da fase de execução e recursais (art. 85, §§1º e 11), pagamento parcial (art. 523, §2º), impenhorabilidades (arts. 833 e 834) e penhora eletrônica (art. 854) — nada disso está na fonte.

**A lacuna de juros e correção foi fechada em 2026-08-02:** ver [CC, arts. 389 e 406](/jurisprudencia/cc-arts-389-406-juros-e-correcao.md), com texto conferido — juros pela **taxa legal** (Selic deduzido o IPCA), correção pelo **IPCA** na falta de convenção. **Não usar "1% ao mês"** no demonstrativo.
