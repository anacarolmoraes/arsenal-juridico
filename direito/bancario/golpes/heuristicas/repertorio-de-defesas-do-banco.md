---
type: heuristica
title: Repertório de defesas do banco em ação de golpe — tese defensiva típica, resposta e página do acervo
description: A contestação-padrão do banco (tradicional ou instituição de pagamento) em ação de fraude por engenharia social repete as mesmas dez teses. Esta página as lista na formulação em que aparecem, diz o eixo em que a réplica as responde, aponta a página do acervo que sustenta a resposta e marca lacuna onde o acervo ainda não cobre. Esqueleto de 2026-09-05; coluna de resposta e estado a conferir pela titular.
tags: [replica, repertorio, defesas-tipicas, golpe, banco, instituicao-de-pagamento, culpa-exclusiva, perfil-de-consumo]
timestamp: '2026-09-05'
status: em_teste
autor: escritorio
fundamentos:
  - /jurisprudencia/resp-2222059-sp-falsa-central-perfil-consumo.md
  - /contra-ataques/culpa-concorrente-vs-dever-vigilancia.md
  - /contra-ataques/quantum-comprovado-extratos-vs-saldo.md
---

# Repertório de defesas do banco em ação de golpe

Formato e regras: [heurística transversal do repertório](../../../pecas/replica/heuristicas/repertorio-de-defesas-tipicas.md) (bundle `pecas`). A tabela de réplica consome esta página no eixo 4 (tese jurídica) e no eixo 2 (fato novo).

**Como ler:** a coluna "o réu alega" está na formulação da contestação-padrão. "Coberto" quer dizer que a página apontada sustenta a resposta com fonte conferida; "parcial" quer dizer que a página existe mas não fecha a tese inteira; "lacuna" quer dizer que a resposta ainda não tem página e, pela regra dura 3, não vai para a peça até ter.

| # | O réu alega | Eixo | O que se responde | Página do acervo | Estado |
|---|---|---|---|---|---|
| 1 | "Culpa exclusiva do consumidor, que forneceu senha e dados a terceiro" (CDC, art. 14, § 3º, II) | fato novo | A excludente exige culpa **exclusiva**; o defeito do serviço de segurança concorre sempre que o sistema deixa passar operação destoante do perfil. Nomear a alavanca de engenharia social do caso reclassifica o consumidor de descuidado para induzido. O ônus da excludente é do banco (art. 373, II; CDC, art. 14, § 3º). | [REsp 2.222.059/SP](../jurisprudencia/resp-2222059-sp-falsa-central-perfil-consumo.md) · [culpa concorrente × dever de vigilância](../contra-ataques/culpa-concorrente-vs-dever-vigilancia.md) · [alavancas de engenharia social](../../../lgpd/heuristicas/engenharia-social-as-alavancas.md) | coberto |
| 2 | "As operações foram autenticadas com senha pessoal, biometria facial e dispositivo cadastrado" | fato novo / documento | Autenticação legítima não sanea operação atípica: o dever de vigilância é sobre o padrão da operação, não sobre a credencial. Pedir a exibição do relatório antifraude e do histórico de operações (arts. 396 a 400), que o banco invoca e não junta. | [culpa concorrente × dever de vigilância](../contra-ataques/culpa-concorrente-vs-dever-vigilancia.md) · [REsp 2.222.059/SP](../jurisprudencia/resp-2222059-sp-falsa-central-perfil-consumo.md) | coberto |
| 3 | "As operações estavam dentro do perfil de consumo do cliente" | fato novo | Os seis parâmetros objetivos do REsp 2.222.059 (valor, horário, frequência, destinatário, canal, geolocalização) se conferem no extrato do próprio autor; o relatório de perfil é a prova. A afirmação do banco costuma vir sem documento: estado "invocado e não juntado", exibição. | [REsp 2.222.059/SP](../jurisprudencia/resp-2222059-sp-falsa-central-perfil-consumo.md) | coberto |
| 4 | "Ilegitimidade passiva: somos instituição de pagamento, não banco" | preliminar | Instituições de pagamento respondem como as bancárias pela segurança do serviço. Preliminar que é mérito travestido. | [REsp 2.222.059/SP](../jurisprudencia/resp-2222059-sp-falsa-central-perfil-consumo.md) | coberto |
| 5 | "Fato de terceiro, fortuito externo: o golpista é o responsável" | tese jurídica | Fraude praticada por terceiro no âmbito da operação bancária é fortuito interno. A resposta canônica é a Súmula 479 do STJ, cuja página mora no bundle irmão; demonstrar o fortuito interno pelo [ato primário](ato-primario-e-ato-secundario.md), não só citar. | [Súmula 479/STJ](../../emprestimo-nao-realizado/jurisprudencia/sumula-479-stj.md) · [ato primário × ato secundário](ato-primario-e-ato-secundario.md) | parcial (súmula coberta; heurística `em_teste`) |
| 6 | "O MED foi acionado e o valor não foi recuperado; o banco não recebeu nenhum valor" | tese jurídica | O mecanismo de devolução é dever regulatório, não excludente; não receber o valor não afasta o defeito do serviço. Inverter: quando o MED foi aberto, o que foi feito entre o aviso e a saída do dinheiro, e que documento prova. | [MED e conduta do banco depois do aviso](med-e-conduta-do-banco-apos-o-aviso.md) (`em_teste`; Res. BCB 103/2021 ainda a depositar) | parcial |
| 7 | "A transferência foi para conta do próprio autor em outro banco; não há fraude" | tese jurídica | A conta intermediária é etapa do golpe, não prova de voluntariedade; a atipicidade se mede pela cadeia inteira de operações no mesmo dia. | [REsp 2.222.059/SP](../jurisprudencia/resp-2222059-sp-falsa-central-perfil-consumo.md) (atipicidade da cadeia) | parcial |
| 8 | "Mero dissabor; ausência de dano moral" | tese jurídica | Negativação e privação de valores essenciais configuram dano in re ipsa; mas o acervo tem precedente **desfavorável** neste ponto (TJRS negou danos morais) e não tem o favorável. Não citar de memória. | [ApCiv 5005364/RS](../jurisprudencia/apciv-5005364-tjrs-falsa-central.md) (desfavorável) · [perfil 12ª Câmara TJRS](../perfis/12a-camara-civel-tjrs.md) | **lacuna** (precedente favorável) |
| 9 | "O valor pleiteado não corresponde ao subtraído; parte foi estornada" | documento | O quantum se prova pelos extratos, operação a operação, não pelo saldo; estorno parcial se deduz, não se presume. | [quantum provado por extratos × saldo](../contra-ataques/quantum-comprovado-extratos-vs-saldo.md) | coberto |
| 10 | "Impugna-se a gratuidade: o autor movimentou valores altos" | preliminar | Movimentação da conta fraudada não é renda; resposta no repertório transversal. | [repertório do banco contra a gratuidade](../../../pecas/gratuidade/heuristicas/repertorio-do-banco-contra-a-gratuidade.md) | coberto |

## Notas de frequência e prioridade

- As teses 1, 2 e 3 aparecem juntas em toda contestação de banco digital e são uma só tese em três formulações: "o consumidor autorizou". A resposta é uma só também, o padrão da operação contra o perfil, e por isso o relatório de perfil de consumo (skill `analise-perfil` do motor) é o documento central da réplica neste tema.
- As lacunas 5 e 6 são as de maior frequência e devem ser as primeiras ingestões do bundle: Súmula 479 com fonte oficial e uma página sobre o MED.
- Esta página não registra caso, número de processo nem nome. O que ela sabe veio da titular e das páginas do acervo apontadas.
