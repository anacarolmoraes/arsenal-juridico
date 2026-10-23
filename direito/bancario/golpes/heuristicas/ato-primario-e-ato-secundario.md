---
type: heuristica
title: Ato primário × ato secundário — a falha do banco precede e causa o Pix da vítima
description: Em golpe por engenharia social, a fraude não começa no Pix; começa na falha do banco que o tornou possível (conta recebedora aberta sem validação, dado da vítima que só o banco tinha, autenticação que não barrou dispositivo ou operação atípica). O Pix da vítima é ato secundário, induzido pelo primário. Demonstrado o ato primário, a conduta da vítima não é causa exclusiva, qualquer que seja o valor. É a resposta direta ao REsp 2.209.868 e ao Enunciado 14 do TJSP.
tags: [golpe-pix, falsa-central, falso-advogado, culpa-exclusiva, nexo-causal, ato-primario, fortuito-interno, peticao-inicial]
timestamp: '2026-10-20'
status: em_teste
autor: escritorio
peca: peticao-inicial
momento: [inicial, replica, alegacoes-finais]
casos_origem: []
fundamentos:
  - /jurisprudencia/resp-2222059-sp-falsa-central-perfil-consumo.md
  - /jurisprudencia/apciv-1026252-tjsp-mercado-pago-origem-bradesco-recebedor.md
  - /contra-ataques/culpa-concorrente-vs-dever-vigilancia.md
---

# Ato primário × ato secundário

**Regra:** a narrativa fática da inicial começa pela falha do banco (ato primário) e só depois chega ao Pix (ato secundário). O leitor tem de ver que, sem o primário, o secundário não existiria.

## O que é cada um

| Ato primário (do banco) | Ato secundário (da vítima) |
|---|---|
| conta recebedora aberta sem validação ([abertura sem validação](abertura-da-conta-recebedora-sem-validacao.md)) | transferir para essa conta |
| dado da vítima (saldo, limite, número do cartão, contrato em curso) que só o banco ou parceiro tinha e que o golpista usou para parecer o banco | acreditar que falava com o banco |
| dispositivo novo, chave Pix criada minutos antes, cadastro alterado na véspera, sem fricção adicional | operar no app |
| chave recebedora já marcada no DICT e Pix liberado sem alerta ([marcação no DICT](marcacao-de-fraude-no-dict-antes-do-pix.md)) | confirmar a transação |
| nada feito depois do aviso ([MED](med-e-conduta-do-banco-apos-o-aviso.md)) | — |

## Por que favorece a vítima

O STJ absolve o banco quando a operação cabe no perfil e nenhuma falha é demonstrada. No [REsp 2.209.868/SP](/jurisprudencia/resp-2209868-sp.md) (3ª Turma, j. 16/06/2026, `em_teste`) a Turma nem reviu o mérito: a origem tinha fixado culpa exclusiva e ausência de falha, e a Súmula 7 barrou o recurso. A lição é processual: **a tese se ganha ou se perde nos fatos provados em primeiro grau**; se a sentença disser "não houve falha", o STJ não corrige. Daí o ato primário ter de estar provado desde a inicial, com documento, e não alegado em recurso. Mesma lógica do [REsp 2.222.059](/jurisprudencia/resp-2222059-sp-falsa-central-perfil-consumo.md), que exige o defeito demonstrado. A excludente do art. 14, § 3º, II, exige culpa **exclusiva**: basta um ato primário provado para que a causa seja concorrente no mínimo, e a jurisprudência do bundle vai além, tratando a vítima enganada como não determinante ([ApCiv 1026252](/jurisprudencia/apciv-1026252-tjsp-mercado-pago-origem-bradesco-recebedor.md); [contra-ataque](/contra-ataques/culpa-concorrente-vs-dever-vigilancia.md)). "Independentemente do valor transferido": a tese não depende de a operação ser grande.

Nomear a alavanca de engenharia social ([transversal LGPD](../../../lgpd/heuristicas/engenharia-social-as-alavancas.md)) fecha o raciocínio: o secundário foi induzido, não escolhido.

## Como escrever

**Nomear o caso pela falha, não pelo apelido do golpe.** "Golpe do WhatsApp", "golpe do Pix" e "golpe da falsa central" chegam ao gabinete com o viés de que a culpa é da vítima, porque é assim que o nome circula. O título da peça, o título-tese e a primeira frase dos fatos nomeiam o ato primário: "conta aberta sem validação de identidade e usada para receber transferências de terceiros", "operações liberadas de dispositivo desconhecido sem confirmação". O apelido do golpe aparece depois, como contexto. Não é mudar o nome da peça para enganar o juiz; é descrever o fato pela causa.

Seção de fatos em duas partes, sem rótulo visível: primeiro a falha (com `Doc.`), depois a cronologia do golpe ([cronologia minuto a minuto](cronologia-minuto-a-minuto-e-dispositivo-novo.md)). O título-tese do capítulo de mérito liga os dois ("A conta que recebeu o Pix foi aberta sem validação; sem ela o golpe não existiria"). A culpa concorrente subsidiária **não** entra na inicial: entra na réplica ou nas alegações finais só se o banco provar contribuição da vítima.

## Quando NÃO usar

Quando não há ato primário provável: golpista que obteve os dados da própria vítima por outro meio, conta recebedora regular e antiga, operação dentro do perfil e nenhuma omissão pós-aviso. Nesse caso a peça não deve ser proposta com a tese de defeito; avaliar.

## Fontes a depositar antes de promover a `vigente`

- [REsp 2.209.868/SP](/jurisprudencia/resp-2209868-sp.md) já depositado (20/10/2026, `em_teste`): conferir o voto e registrar a distinção (Súmula 7; culpa exclusiva fixada na origem) na página dele. Esta heurística responde à tese 5 do [repertório de defesas](repertorio-de-defesas-do-banco.md).
- A tese está esboçada em `raw/notas-estrategicas-fraudes-bancarias.md` (acervo antigo, pendência do log de 02/08/2026) e reaparece em triagem de perfil público (@jessicaabreuadv, posts Da0ABvNFn7_ e Da5gDjdOysC, jul/2026), que não a define: a definição acima é do escritório.
