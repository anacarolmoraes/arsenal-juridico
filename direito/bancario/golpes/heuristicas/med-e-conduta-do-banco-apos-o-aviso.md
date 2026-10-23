---
type: heuristica
title: O que o banco fez depois de avisado — MED e janela até a saída do dinheiro como causa de pedir autônoma
description: Em golpe Pix, mesmo quando a vítima autorizou a transferência, o banco responde pelo que deixou de fazer depois da comunicação da fraude — abertura do MED, bloqueio, recuperação, comunicação com o recebedor. A omissão pós-aviso é só do banco e neutraliza a culpa exclusiva. Entra na inicial, com cronologia e pedido de exibição individualizado.
tags: [golpe-pix, med, resolucao-bcb-103, culpa-exclusiva, cronologia, exibicao-de-documentos, peticao-inicial, audiencia]
timestamp: '2026-10-20'
status: em_teste
autor: escritorio
peca: peticao-inicial
momento: [inicial, audiencia]
casos_origem: []
fundamentos:
  - /jurisprudencia/apciv-1007466-tjsp-osasco-mercado-pago-bradesco-dano-moral.md
  - /jurisprudencia/resp-2222059-sp-falsa-central-perfil-consumo.md
  - /jurisprudencia/res-bcb-103-2021-med-mecanismo-especial-de-devolucao.md
---

# O que o banco fez depois de avisado (MED)

**Regra:** toda ação de golpe Pix leva, como causa de pedir própria e separada da atipicidade da operação, a conduta do banco entre o aviso da fraude e a saída definitiva do dinheiro da conta recebedora. A pergunta da peça não é só "quem apertou o botão"; é **quanto tempo o banco levou para agir depois que soube, e o que fez**.

## Por que favorece a vítima

A defesa-padrão ("o próprio cliente autorizou") responde ao ato da vítima e cala sobre o que veio depois. O Mecanismo Especial de Devolução (MED) é dever regulatório da instituição pagadora; não abri-lo, abri-lo tarde ou não comprovar a tentativa de bloqueio é falha do serviço que nenhuma culpa da vítima explica. É o ponto em que o REsp 2.222.059 (defeito do serviço demonstrado) se alcança mesmo quando a operação cabia no perfil.

Na [ApCiv 1007466](/jurisprudencia/apciv-1007466-tjsp-osasco-mercado-pago-bradesco-dano-moral.md) o MED foi acionado e falhou por falta de saldo na conta recebedora (p. 5): a janela já tinha fechado. É exatamente o intervalo que esta heurística manda medir.

## Como escrever (inicial)

1. **Cronologia com hora**, uma linha por evento: Pix → percepção da fraude → primeira comunicação ao banco (canal e protocolo) → resposta → abertura do MED (se houve) → bloqueio/recuperação → saída do dinheiro da conta recebedora. Cada linha com `Doc. N`.
2. **Comparação** do que o cliente pediu com o que o banco respondeu, e quando. Resposta genérica ou silêncio entram como fato.
3. **Pedido de exibição individualizado** (art. 397, I a III), nunca "documentos do MED": data e hora da abertura do MED; protocolo; notificação de infração; comunicações entre instituição pagadora e recebedora; resultado da análise; registro de bloqueio; valores localizados e recuperados; cronologia interna das providências. A recusa gera a presunção do art. 400 — por isso o pedido vai na inicial, não na réplica (ver [exibição a partir do mapa probatório](../../../pecas/peticao-inicial/heuristicas/exibicao-de-documentos-a-partir-do-mapa-probatorio.md)).

## Audiência

Ao preposto: "que horas o banco foi comunicado?", "que horas o MED foi aberto?", "que documento comprova isso?". "Não sei" fica registrado; "o banco tem" abre a pergunta "por que não juntou?" (ver [inquirir o preposto](inquirir-o-preposto-do-banco.md)).

## Quando NÃO usar

Vítima que só comunicou o banco dias depois, quando o dinheiro já tinha saído: a janela não existiu e a heurística vira argumento contra. Nesse caso a peça fica na atipicidade e na conta recebedora ([abertura sem validação](abertura-da-conta-recebedora-sem-validacao.md)).

## Fontes a depositar antes de promover a `vigente`

- Resolução BCB 103/2021 (MED) — **depositada em 20/10/2026**, mas só o texto da resolução alteradora de 2021: [página `em_teste`](/jurisprudencia/res-bcb-103-2021-med-mecanismo-especial-de-devolucao.md) com o fluxo (notificação de infração → bloqueio imediato → devolução), o prazo de 90 dias, a dependência de saldo e a responsabilidade do recebedor que rejeita sem justo motivo (art. 41-I). Falta o regulamento do Pix consolidado e o Manual Operacional do DICT (prazos do bloqueio) para conferir a redação vigente.
- Acórdão que reconheceu falha pela não instauração do MED com Pix autorizado pela vítima: citado sem número em triagem de perfil público (@jessicaabreuadv, post DdQ7PbMIKSg, 14/09/2026). Localizar no CJSG por "MED" + "fortuito interno".
- Origem desta página: triagem de 17–20/10/2026 (`novas_ideias/APANHADO_instagram_2026-10-17.md` do motor). Nenhuma transcrição aqui é citável em peça.
