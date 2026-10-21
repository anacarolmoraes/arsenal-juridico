> **Fonte oficial.** Recorte da documentação da API do DICT (Diretório de Identificadores de Contas Transacionais), Banco Central do Brasil, versão **2.12.1**, seção "Consultar Vínculo" (operação GET /entries/{Key}), extraído em 20/10/2026 do arquivo HTML baixado pela titular de https://www.bcb.gov.br/estabilidadefinanceira/pagamentosinstantaneos (Redoc). Texto convertido de HTML para texto plano, sem edição; marcação do Redoc removida. Só esta seção foi depositada (o documento completo tem 1,5 MB).

# API DICT 2.12.1 — Consultar Vínculo (GET /entries/{Key})

</ CreateEntryResponse > Consultar Vínculo Obtém um vínculo contendo os detalhes de conta transacional associados a uma chave de endereçamento.</p>
<h3 id="limitação-de-requisições">Limitação de requisições</h3>
<p>A consulta a chaves está sujeita à política de limitação (<em>rate-limiting</em>) de requisições.
A limitação funciona com base em cabeçalhos enviados na requisição. Os cabeçalhos de requisição são obrigatórios
para todos os tipos de chaves.</p>
<p>O parâmetro <code>PI-PayerId</code> é o identificador do usuário final e é usado para aplicar as políticas de
limitação com escopo de usuário. Deve ser preenchido com o CPF ou CNPJ (apenas dígitos), a depender
do tipo da entidade titular da conta pagadora.</p>
<h3 id="cache">Cache</h3>
<p>Consultas a vínculos podem ter suas respostas <em>cacheadas</em> no PSP, devendo seguir as
diretivas contidas no header <a href="https://tools.ietf.org/html/rfc7234#section-5.2"><code>Cache-Control</code></a>.</p>
<p><em>Importante</em>: Para fazer uso de cache, clientes HTTP geralmente precisam ser configurados. Não
é comum que tenham essa funcionalidade habilitada por padrão.</p>
<h3 id="estatísticas">Estatísticas</h3>
<p>Através do parâmetro opcional <code>IncludeStatistics</code>, é possível indicar se as informações de contadores antifraude
devem ou não ser incluídas na resposta.</p>
Obtém um vínculo contendo os detalhes de conta transacional associados a uma chave de endereçamento.
Limitação de requisições
A consulta a chaves está sujeita à política de limitação ( rate-limiting ) de requisições.
A limitação funciona com base em cabeçalhos enviados na requisição. Os cabeçalhos de requisição são obrigatórios
para todos os tipos de chaves.
O parâmetro PI-PayerId é o identificador do usuário final e é usado para aplicar as políticas de
limitação com escopo de usuário. Deve ser preenchido com o CPF ou CNPJ (apenas dígitos), a depender
do tipo da entidade titular da conta pagadora.
Cache
Consultas a vínculos podem ter suas respostas cacheadas no PSP, devendo seguir as
diretivas contidas no header Cache-Control .
Importante : Para fazer uso de cache, clientes HTTP geralmente precisam ser configurados. Não
é comum que tenham essa funcionalidade habilitada por padrão.
Estatísticas
Através do parâmetro opcional IncludeStatistics , é possível indicar se as informações de contadores antifraude
devem ou não ser incluídas na resposta.
path Parameters Key required string ( Key ) <= 77 characters Example: 12345678901 query Parameters IncludeStatistics boolean Default: false Incluir dados antifraude na resposta.</p>
Incluir dados antifraude na resposta.
header Parameters PI-RequestingParticipant required string ^(?i)[a-z0-9]{8} Example: 12345678 Identificador único do requisitante, podendo ser:</p>
<ul>
<li>ISPB do participante (direto ou indireto) que faz a requisição <strong>OU</strong></li>
<li>8 primeiros dígitos do CNPJ para Iniciadores de Pagamento</li>
</ul>
Identificador único do requisitante, podendo ser:
ISPB do participante (direto ou indireto) que faz a requisição OU
8 primeiros dígitos do CNPJ para Iniciadores de Pagamento
PI-PayerId required string ^([0-9]{11}|[0-9]{14})$ Identificador do pagador que originou a requisição. Usado para <em>rate-limiting</em>.</p>
Identificador do pagador que originou a requisição. Usado para rate-limiting .
PI-EndToEndId required string Identificador fim-a-fim do pagamento associado a essa requisição. Corresponde ao campo <code>EndToEndId</code> na mensagem pacs.008. Usado para <em>rate-limiting</em>.</p>
Identificador fim-a-fim do pagamento associado a essa requisição. Corresponde ao campo EndToEndId na mensagem pacs.008. Usado para rate-limiting .
Responses 200 OK</p>
OK
400 Bad Request</p>
Bad Request
404 Not found</p>
Not found
429 Rate-Limited</p>
Rate-Limited
get /entries/{Key} Homologação</p>
Homologação
https://dict-h.pi.rsfn.net.br:16522/api/v2 /entries/{Key} Produção</p>
Produção
https://dict.pi.rsfn.net.br:16422/api/v2 /entries/{Key} Response samples 200 400 404 429 Content type application/xml Example entry-include-statistics entry entry-include-statistics Copy <?xml version="1.0" encoding="UTF-8" ?>
< GetEntryResponse >
< Signature > </ Signature >
< ResponseTime > 2020-01-10T10:00:00Z </ ResponseTime >
< CorrelationId > a9f13566e19f5ca51329479a5bae60c5 </ CorrelationId >
< Entry >
< Key > 11122233300 </ Key >
< KeyType > CPF </ KeyType >
< Account >
< Participant > 12345678 </ Participant >
< Branch > 0001 </ Branch >
< AccountNumber > 0007654321 </ AccountNumber >
< AccountType > CACC </ AccountType >
< OpeningDate > 2010-01-10T03:00:00Z </ OpeningDate >
</ Account >
< Owner >
< Type > NATURAL_PERSON </ Type >
< TaxIdNumber > 11122233300 </ TaxIdNumber >
< Name > João Silva </ Name >
</ Owner >
< CreationDate > 2019-11-18T03:00:00Z </ CreationDate >
< KeyOwnershipDate > 2019-11-18T03:00:00Z </ KeyOwnershipDate >
< OpenClaimCreationDate > 2019-11-19T03:00:00Z </ OpenClaimCreationDate >
</ Entry >
< OwnerStatistics >
< Spi >
< Watermark > 2023-01-01T10:00:00.000Z </ Watermark >
< Settlements d90 = " 0 " m12 = " 0 " m60 = " 0 " />
</ Spi >
