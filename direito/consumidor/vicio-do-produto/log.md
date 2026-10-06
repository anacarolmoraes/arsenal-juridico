# Log do bundle — vicio-do-produto

## 2026-10-02 — REsp 1.744.595/MG (contratos coligados)

Depositado a partir de `consumir/` (`stj_dje_20210901_0_29990720.pdf`), convertido com `pdfmd --no-tables --page-breaks` e anonimizado (consumidora, quatro advogados e o número do contrato de financiamento). Decisão monocrática de Sanseverino (3ª T., 26/08/2021), página `vigente`, principal e **parcialmente contrária**: reconhece a coligação entre compra de móveis planejados e financiamento assinado na loja com preposto do Santander, resolve o financiamento e condena o banco a devolver o que recebeu; mas mantém a ilegitimidade do banco quanto ao dano moral, por falta de solidariedade entre coligados sem falha própria. Reúne cinco precedentes das duas Turmas (REsp 1.127.403/SP, REsp 1.406.245/SP, AgInt no REsp 1.519.556/SP, AgInt no AREsp 829.380/RJ, REsp 1.379.839/SP), nenhum depositado.

Preenche a lacuna declarada por um caso em contrarrazões (concessionária de usados + banco de varejo): o acervo não tinha jurisprudência sobre o art. 54-F. Tese nova `financiamento-coligado-cai-com-a-compra` (`em_teste`, um fundamento). A decisão é posterior à Lei 14.181/2021 e não cita o art. 54-F; a tese usa a lei como fundamento principal e o julgado como confirmação. Conferido o texto do art. 54-F no CDC compilado de `pecas/raw/` (inciso II: crédito oferecido no local da venda; § 2º: rescisão do contrato não cumprido contra o fornecedor do crédito).

**Flanco registrado:** condenação solidária do banco de varejo por dano moral não resiste nesta linha da 3ª Turma sem conduta própria do banco (cobrança após ciência, negativação, recusa de suspender).

## 2026-10-01 (noite, 2) — quatro julgados do prazo e do reparo tardio

Depositados a partir de `consumir/` e anonimizados: REsp 2.101.225/BA (`vigente`), REsp 2.103.427/GO (`vigente`, **contrário**, 3×2), AgInt no AREsp 2.197.121/RO (`vigente`, contrário no resultado por Súmula 7) e a **decisão monocrática** no REsp 1.697.426/MG (`vigente`).

Achados:

- O PDF baixado como "AgInt nos EDcl no REsp 1.697.426/MG" é a monocrática de 01/09/2020 que deu provimento ao REsp; o acórdão colegiado de 13/12/2021, que os contrários citam, continua faltando. Depósito renomeado para não induzir citação errada.
- Duas cópias do AgInt no AREsp 2.197.121 com hashes diferentes e o mesmo código de controle: mesmo documento.
- Anonimização: a consumidora do REsp 2.103.427 aparece só pelo primeiro nome no voto-vencedor (9 vezes), e a do 1.960.115 tem uma terceira grafia ("MARA ELISABETH") na ementa do acórdão estadual transcrito. O script passou a aceitar padrão por arquivo; ambos corrigidos.

A tese `prazo-de-30-dias-global-e-escolha-do-consumidor` foi reescrita: termo inicial na primeira manifestação do vício, conserto tardio não apaga o direito (1.697.426), placar 4×3 e resposta aos três contrários. O padrão comum dos contrários é restituição integral pedida anos depois do reparo, ou linha do tempo não provada na origem.

## 2026-10-01 (noite) — REsp 1.982.739/MT

Depositado a partir de `consumir/` (`RESP-1982739-2022-03-21.pdf`), anonimizado (consumidor e três advogados; uma inscrição com letra final, "MT014146O", escapava ao padrão e o script foi ajustado). Página `vigente`, principal. Dois usos: (i) **critério de cálculo** quando o veículo foi vendido, valor de um novo na data da venda menos o valor recebido (item 7), mais favorável que o do REsp 1.828.296/PA; a tese `venda-do-bem-converte-em-perdas-e-danos` ganhou a tabela com os dois critérios; (ii) **comerciante solidário "sem qualquer distinção"** no vício do produto e no fato do serviço (item 4), agora o primeiro fundamento da tese `solidariedade-da-cadeia-no-vicio-do-produto`. Sai da lista de pendências do `index.md`.

## 2026-10-01 — criação (v0.1.0, semente)

O roteador global listava "vício do produto" como planejado em `direito/consumidor/`. O gatilho foi uma sentença em ação de veículo zero com vício que excluiu a concessionária pelo art. 13 do CDC (fato do produto) num caso que é de vício (art. 18). O caso concreto fica na camada C1; aqui entra só a jurisprudência pública e as teses em termos gerais.

Seis decisões do STJ depositadas a partir de `consumir/`, convertidas com `pdfmd --no-tables --page-breaks` e anonimizadas:

- AgInt nos EDcl no REsp 1.960.115/PR (`vigente`, principal): prazo global, solidariedade, substituição.
- REsp 1.684.132/CE (`vigente`, principal): trintídio corrido, devolução do preço, concessionária solidária.
- AgInt no AREsp 1.703.445/MG (`vigente`, similar): solidariedade, Súmula 83.
- AgInt no REsp 1.828.296/PA (`vigente`, principal): venda no curso da ação, perdas e danos com abatimento.
- AgInt no AREsp 2.329.940/MG (`vigente`, **contrário**): restituição integral desproporcional com excesso de 6 dias e 3 anos de uso.
- AREsp 3.214.920/PB (`vigente`, similar, **peso limitado**): conversão de ofício pelo art. 499 mantida por Súmula 7; matéria diversa (gravações de rádio).

Três teses `em_teste`: solidariedade da cadeia (art. 18 × art. 13), prazo global e escolha do consumidor (com resposta ao contrário), venda do bem converte em perdas e danos.

**Achado da anonimização:** o nome do advogado que fez a sustentação oral aparece no acórdão do REsp 1.684.132/CE fora do cabeçalho ("Dr. ..., pela parte RECORRIDA"). O padrão entrou no script de anonimização.

**Fora do bundle, de propósito:** AREsp 2.983.084/AL (usucapião entre familiares), que veio na mesma leva de `consumir/` sem relação com o tema; AgInt no AREsp 1.881.823/MS, já consumido em 29/09/2026 para `execucao/credor`.

**Pendências:** ver `index.md` (recorte do art. 18 do CDC; cinco julgados citados e não depositados).
