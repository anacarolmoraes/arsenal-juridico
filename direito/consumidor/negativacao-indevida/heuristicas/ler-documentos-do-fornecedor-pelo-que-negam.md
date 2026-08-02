---
type: heuristica
title: Ler os documentos do fornecedor pelo que eles negam
description: O acervo que o fornecedor junta para provar a contratação frequentemente prova o contrário. Ler cada documento procurando o que ele desmente, e separar prova de USO do serviço de prova de ORIGEM do vínculo.
tags: [estrategia-processual, prova, contestacao, negativacao, consumidor]
timestamp: '2026-07-31'
status: vigente
autor: escritorio
fundamentos:
  - /jurisprudencia/sumula-385-stj.md
---

# Ler os documentos do fornecedor pelo que eles negam

**Regra:** não tratar o acervo da contestação como bloco adversário a ser genericamente impugnado. Abrir documento por documento perguntando **o que este papel desmente**, e classificar cada um em duas pilhas: prova do **uso** do serviço e prova da **origem** do vínculo. O fornecedor quase sempre enche a primeira e deixa a segunda vazia, e a decisão desfavorável costuma nascer de o julgador tratar as duas como a mesma coisa.

**Efeito buscado:** deslocar o ônus sem depender de perícia. Documento produzido pelo réu que contradiz a tese do réu é prova contra ele, não prova a ser afastada — e dispensa a instrução que o julgamento antecipado costuma negar.

**Onde olhar, em ordem:**

| Documento | O que costuma desmentir |
|---|---|
| Comprovante de entrega (AR, protocolo de instalação, canhoto) | **nome do recebedor** diverso do titular; campo de motivo assinalado como entrega em caixa postal ou a terceiro; endereço diverso do declarado; data incompatível com a contratação |
| Tela de cadastro ou de abertura | status final registrando que **não houve oferta ou adesão** do produto que o fornecedor diz ter contratado; campos de qualificação em branco ("não informado"), sinal de preenchimento por terceiro; divergência de estado civil, filiação ou endereço |
| Consulta de cadastro juntada para acionar a Súmula 385 | "nada consta" no campo pertinente; apontamentos **posteriores** à negativação impugnada; ausência de anotação do próprio réu, que confessa a baixa |
| Extrato de conta ou histórico de faturas | ver [reconstruir o débito na data da negativação](reconstruir-debito-na-data-da-negativacao.md) |
| A própria contestação | confissões em prosa: admissão de que houve inscrição, de que houve quitação, de que o nome foi retirado |

**Armadilha operacional, e é a mais cara:** esses documentos costumam ser **imagens embutidas no PDF**. Conversor de PDF para texto não as transcreve, e o `.md` resultante não avisa que elas existem — o silêncio é indistinguível de "o documento é só prosa". No workspace PMA, converter com `node skills/pdfmd/scripts/converter-caso.js`, que exporta as imagens e escreve no topo do `.md` quantas são e em que páginas se concentram. Sem isso, a leitura do texto convertido conclui que a contestação não tem prova nenhuma e perde a prova que ganha o caso.

**Cautela que o mesmo caso ensinou:** ler a imagem em resolução baixa e afirmar o que ela diz é tão perigoso quanto não lê-la. Campo manuscrito de formulário (data, hora, assinatura) é ambíguo com frequência, e tese construída sobre leitura errada de manuscrito entrega ao adversário uma refutação de um parágrafo que contamina os pontos bons do mesmo capítulo. Sustentar-se no que o documento diz **sem ambiguidade** e deixar o resto de fora.

**Origem:** caso Diego (TJTO, 2026), negativação por conta e cartão bancários. O comprovante de entrega do cartão registrava recebedor de nome diverso e entrega em caixa postal; a tela de abertura do próprio fornecedor encerrava a solicitação com "cliente sem oferta de cartao disponivel"; a consulta juntada para sustentar a Súmula 385 registrava "nada consta". As três estavam em imagens embutidas, invisíveis no texto convertido. A data manuscrita do mesmo comprovante, ao contrário, era ambígua, e duas peças anteriores do escritório afirmaram datas diferentes e provavelmente erradas a partir dela.

**Quando NÃO usar:** quando o fornecedor junta contrato assinado e o cliente não nega a assinatura. Aí a pilha "origem" está preenchida, a leitura adversarial dos periféricos vira ruído, e a tese é vício de consentimento — não inexistência do vínculo. Ver [impugnar a assinatura já na inicial](../../../bancario/emprestimo-nao-realizado/heuristicas/impugnar-assinatura-na-inicial.md).
