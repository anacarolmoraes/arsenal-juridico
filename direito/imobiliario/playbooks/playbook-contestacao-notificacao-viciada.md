---
type: playbook
title: Playbook — contestação a ação de resolução/reintegração de posse por notificação viciada
description: Estrutura da defesa do comprador contra ação de resolução contratual c/c reintegração de posse movida pela loteadora, centrada no vício formal da notificação extrajudicial e na ilegitimidade por cessão de direitos.
tags: [contestacao, notificacao-extrajudicial, reintegracao-de-posse, defesa]
timestamp: '2026-08-01'
status: em_teste
autor: escritorio
peca: contestacao
teses:
  - /teses/notificacao-previa-invalida-obsta-rescisao-por-loteadora.md
  - /teses/benfeitorias-boa-fe-anteriores-a-mora-sao-indenizaveis.md
skills: [pre-peticionamento, legal-orchestrator, peca-pma-builder]
---

# Playbook — Contestação por notificação viciada

## Antes de redigir

Confirme com o cliente/dossiê: (a) a certidão/comprovante de diligência da notificação extrajudicial — meio utilizado, endereço, quem assinou o recebimento, prazo de purga e conteúdo (ver [heurística de checklist](/heuristicas/verificar-vicio-formal-de-notificacao-extrajudicial.md)); (b) houve cessão de direitos aquisitivos a terceiro antes do ajuizamento — checar risco de ilegitimidade passiva ou necessidade de intervenção de terceiro ([heurística](/heuristicas/checar-cessao-de-direitos-antes-de-definir-legitimidade.md)); (c) valores efetivamente pagos e impugnação de eventuais divergências apontadas pela loteadora; (d) benfeitorias erigidas no lote — cronologia em relação à mora alegada, regularidade perante o Município; (e) data do contrato original, para determinar o regime de retenção aplicável em caso de mérito subsidiário; (f) **os encargos do contrato**: juros compostos/capitalizados cobrados por loteadora (que não é instituição financeira) esbarram na Lei de Usura — encargo ilegal descaracteriza a culpa do comprador pela mora (arts. 394, 396 e 389, CC) e mina a própria pretensão resolutória; (g) **percentual do preço já pago** — pagamento substancial abre a defesa de adimplemento substancial (boa-fé objetiva) contra a resolução; (h) o valor da causa da inicial adversária — deve ser o valor do contrato (art. 292, II, CPC; ver `perfil/definicoes.md` do motor) e a correção força complemento de custas (art. 292, § 3º); (i) o foro — relação de consumo permite arguir incompetência quando a ação não foi proposta no domicílio do comprador (art. 101, I, CDC c/c art. 64, CPC; contestar desde logo, art. 340, CPC).

## Estrutura da peça

1. **Preliminares (nesta ordem):**
   - Incorreção do valor da causa, quando a loteadora atribuiu valor menor que o do contrato (art. 292, II e § 3º, CPC) — acessória, mas força complemento de custas e sinaliza rigor;
   - Incompetência do foro, se a ação não foi proposta no domicílio do comprador-consumidor (art. 101, I, CDC c/c arts. 64 e 340, CPC);
   - Ilegitimidade passiva, se houve cessão de direitos não considerada pela loteadora na petição inicial — pela via do art. 338, CPC (intimação da autora para substituir o réu, com as consequências do art. 485, VI, se não o fizer);
   - Falta de interesse de agir / inépcia, por ausência de constituição regular em mora — vício formal da notificação ([tese central desta defesa](/teses/notificacao-previa-invalida-obsta-rescisao-por-loteadora.md)).
2. **Mérito (subsidiário, caso as preliminares não sejam acolhidas):**
   - Descaracterização da culpa pela mora, quando o inadimplemento decorreu de encargo ilegal cobrado pela loteadora (juros capitalizados sem amparo — Lei de Usura; arts. 394, 396 e 389, CC): sem culpa do comprador, não há resolução por inadimplemento dele;
   - Adimplemento substancial, quando parcela expressiva do preço foi paga — a boa-fé objetiva veda a resolução e remete o credor à via da cobrança do saldo;
   - Impugnação específica dos valores/percentuais de retenção pretendidos pela loteadora, com o cálculo correto conforme o regime aplicável ([tese](/teses/retencao-escalonada-regime-anterior-10-a-25-por-cento.md) ou art. 32-A conforme a data do contrato);
   - Vedação de cumulação de cláusula penal compensatória com perdas e danos ([tese](/teses/vedacao-bis-in-idem-retencao-global-e-encargos-moratorios.md)) e de perda total das parcelas (art. 53, CDC);
   - Pedido de indenização por benfeitorias de boa-fé erigidas antes da mora, com **direito de retenção** do imóvel até o pagamento (art. 1.219, CC) ([tese](/teses/benfeitorias-boa-fe-anteriores-a-mora-sao-indenizaveis.md));
   - Impugnação de pedido de fruição sem prova de proveito econômico ([tese](/teses/fruicao-exige-prova-de-proveito-economico-efetivo.md));
   - Combate à tutela provisória de reintegração: irreversibilidade prática (art. 300, § 3º, CPC) e ausência de periculum — o imóvel não desaparece até a sentença.
3. **Pedidos:** improcedência (preliminar) ou, subsidiariamente, procedência parcial com os ajustes de mérito acima. **Reconvenção** (art. 343, CPC), quando a instrução comportar: (i) declaração de resolução por culpa da loteadora (encargo ilegal), com devolução integral das parcelas, juros desde cada desembolso; (ii) indenização por benfeitorias com retenção até o pagamento. Restituição em parcela única ([tese](/teses/restituicao-imediata-parcela-unica-nao-parcelada.md)).

## Erros a evitar

- Aceitar tacitamente a mora sem antes checar a certidão de diligência da notificação — é o ponto de maior retorno da defesa quando presente o vício.
- Omitir a preliminar de ilegitimidade quando há cessão de direitos não regularizada, mesmo que pareça "só" uma questão formal — evita disputa possessória paralela e intervenção de terceiros no meio do processo.
- Discutir só o mérito quando a preliminar de notificação viciada, se acolhida, já resolve o processo inteiro a favor do réu.
- Citar a jurisprudência dos modelos do Scavone ([`/raw/modelos-scavone/`](/raw/modelos-scavone/index.md)) sem conferir: as ementas de lá são de TJSP e STJ antigos (1998–2015) e **não passaram por verificação oficial** — usar o `radar-jurisprudencia` para buscar precedente atual e depositar em `jurisprudencia/` antes de citar. O modelo dá o argumento; o precedente vem do acervo.
- Invocar adimplemento substancial sem dosar: a tese perdeu força no STJ para alienação fiduciária e exige percentual realmente expressivo — usar como reforço da boa-fé objetiva, não como tese única.
