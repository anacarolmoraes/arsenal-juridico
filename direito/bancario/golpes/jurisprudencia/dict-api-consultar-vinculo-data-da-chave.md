---
type: legislacao
title: API do DICT (BCB, v2.12.1) — a consulta de vínculo devolve ao participante pagador a data de criação da chave Pix (CreationDate, KeyOwnershipDate)
description: Documentação oficial da API do Diretório de Identificadores de Contas Transacionais (DICT) do Banco Central. A operação "Consultar Vínculo" (GET /entries/{Key}), feita pelo participante pagador antes de liquidar um Pix e identificada pelo CPF do pagador e pelo EndToEndId do pagamento, devolve, entre os dados da chave de destino, CreationDate (data de criação do vínculo) e KeyOwnershipDate (data de posse da chave), além de contadores antifraude opcionais. Base para afirmar que o banco do pagador sabia, no instante da liquidação, que a chave de destino tinha minutos de vida.
tags: [legislacao, bcb, dict, pix, chave-pix, consulta-de-vinculo, creationdate, antifraude, perfil-de-consumo, golpe-pix]
timestamp: '2026-10-20'
status: vigente
autor: ingerido
resource: https://www.bcb.gov.br/estabilidadefinanceira/pagamentosinstantaneos (documentação Redoc da API DICT 2.12.1; arquivo HTML fornecido pela titular em 20/10/2026)
orgao: Banco Central do Brasil (Departamento de TI; suporte.ti@bcb.gov.br)
raw: /raw/dict-api-2-12-1-consultar-vinculo.md
verificado_em: '2026-10-20'
---

# API do DICT — Consultar Vínculo e a data da chave

## O que a fonte diz

A documentação da API do DICT, versão 2.12.1, descreve a operação **Consultar Vínculo**
(`GET /entries/{Key}`) assim:

> Obtém um vínculo contendo os detalhes de conta transacional associados a uma chave de endereçamento.
> — `raw/dict-api-2-12-1-consultar-vinculo.md`

A requisição leva, no cabeçalho, o participante requisitante (`PI-RequestingParticipant`), o
**CPF ou CNPJ do pagador** (`PI-PayerId`, "Identificador do pagador que originou a requisição") e o
**identificador fim-a-fim do pagamento** (`PI-EndToEndId`, "Identificador fim-a-fim do pagamento
associado a essa requisição. Corresponde ao campo EndToEndId na mensagem pacs.008"). O parâmetro
opcional `IncludeStatistics` inclui "dados antifraude na resposta".

A resposta (`GetEntryResponse`, exemplo da própria documentação) traz, dentro de `Entry`, além da
chave, da conta e do titular, os campos:

> `<CreationDate>` 2019-11-18T03:00:00Z `</CreationDate>`
> `<KeyOwnershipDate>` 2019-11-18T03:00:00Z `</KeyOwnershipDate>`
> `<OpenClaimCreationDate>` 2019-11-19T03:00:00Z `</OpenClaimCreationDate>`
> — `raw/dict-api-2-12-1-consultar-vinculo.md` (exemplo de resposta 200)

## Aplicação no tema

- **O banco do pagador conhece a idade da chave de destino antes de liquidar.** A consulta ao
  DICT é feita pelo participante pagador, vinculada ao pagador e ao pagamento concreto, e devolve a
  data de criação do vínculo. Numa peça de golpe em que a chave da conta de destino foi criada
  minutos antes do Pix, isso transforma "chave recém-criada" de fato conhecido só pela vítima em
  **sinal que o sistema antifraude do pagador recebeu e ignorou**. Combina com o item 9 do
  [REsp 2.222.059/SP](resp-2222059-sp-falsa-central-perfil-consumo.md) (meio e sequência das
  operações) e com o art. 39-B, § 1º, II, do regulamento do Pix ("o tempo decorrido desde a abertura
  da conta transacional pelo usuário recebedor" como critério de suspeita, transcrito na
  [ApCiv 1026252](apciv-1026252-tjsp-mercado-pago-origem-bradesco-recebedor.md), p. 12).
- **Pedido de exibição:** o registro da consulta de vínculo feita para cada Pix (com `EndToEndId`,
  horário e resposta recebida, inclusive `CreationDate` e estatísticas antifraude, se solicitadas).
  É documento que o participante gera por dever operacional e que prova o que ele sabia no instante
  da liquidação.
- **Limite:** a documentação prova que o dado é devolvido; não prova que o banco o consultou com
  `IncludeStatistics` nem que o leu. Por isso a peça afirma o que a API devolve e pede o registro
  da consulta, em vez de afirmar o que o banco "viu".

## Observações

- Depositado a pedido da titular em 20/10/2026 para sustentar afirmação da inicial do caso de golpe
  do falso advogado (IV.1). Antes disso a peça enunciava o fato sem fonte no acervo (ressalva da
  validação de 20/10/2026, 12h30).
- Só a seção "Consultar Vínculo" foi depositada em raw; o arquivo completo (1,5 MB, Redoc) ficou
  fora do acervo. Versão 2.12.1; a API tem changelog próprio e os campos podem mudar em versão
  *major*.
