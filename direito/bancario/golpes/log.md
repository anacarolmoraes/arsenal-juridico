# Log

## 2026-10-20

- **Ingestão (20/10)** — **API do DICT, v2.12.1, "Consultar Vínculo"** (BCB): recorte da documentação
  oficial fornecida pela titular (HTML Redoc), depositado em `raw/dict-api-2-12-1-consultar-vinculo.md`
  + página `vigente`. Prova que o participante pagador recebe `CreationDate`/`KeyOwnershipDate` da
  chave de destino antes de liquidar. Fecha a ressalva MÉDIA da validação da inicial do caso de golpe
  (IV.1, idade da chave vista pelo pagador).

## 2026-10-19

- **Ingestão** — **ApCiv 1026252-80.2024.8.26.0196** (TJSP, 12ª CDPriv., Rel. Alexandre David
  Malfatti, j. 24/11/2025), a pedido da titular, a partir da triagem CJSG de 18/10/2026 (caso de
  golpe do falso advogado; 319 acórdãos, relatório em `tmp/radar-tjsp/welson/` do motor).
  Mercado Pago como instituição **de origem** e Bradesco como **recebedor**, ambos condenados;
  regulamento do Pix (arts. 39, 88, 89, 39-B) e Res. 4.753 (arts. 2º e 4º) transcritos no voto.
  Raw pseudonimizado (autora PJ e beneficiário → rótulo) + página `vigente`.
  - **Ressalva registrada na página:** a p. 8 do voto traz trecho de modelo de outro caso
    (celular subtraído, cartão de débito), incompatível com os fatos das pp. 5–6; não transcrever.
    Ementa nomeia "MERCADOPAGO.COM REPRESENTAÇÕES LTDA"; relatório, "MERCADO PAGO INSTITUIÇÃO
    DE PAGAMENTO LTDA".
- **Ingestão** — **ApCiv 1007466-06.2025.8.26.0405** (TJSP, 12ª CDPriv., Rel. Malfatti, j.
  17/12/2025, origem 1ª Vara Cível de Osasco), a pedido da titular. Falso funcionário, três Pix
  sequenciais; Mercado Pago (origem) e Bradesco (recebedor) solidários; dano moral R$ 5 mil;
  restituição simples; juros da citação. Raw pseudonimizado (autora → rótulo) + página `vigente`.
  - **Achados:** (i) a 12ª Câmara reconhece perfil desviado sem laudo (valor elevado + sequência);
    (ii) nega o art. 42 para o principal do Pix: a tese do dobro deve ficar restrita a encargos
    cobrados; (iii) juros da citação por relação contratual, contra a Súmula 54 de outras câmaras.
- **Ingestão** — **ApCiv 1004155-48.2025.8.26.0068** (TJSP, 17ª CDPriv., Rel. designado Irineu
  Fava, maioria em julgamento estendido, j. 28/07/2026). Falso advogado; o banco que não prova a
  compatibilidade da operação com o perfil (ônus do saneador, art. 373, II) responde pelo
  prejuízo integral; dano moral negado. Raw pseudonimizado + página `vigente`. Entra na inicial
  do caso de golpe (IV.1) como contraponto ao precedente de Osasco que exigiu do autor a prova da
  atipicidade.
  - **Pendências novas:** os demais acórdãos da triagem de 18/10/2026 (relatório
    `tmp/radar-tjsp/welson/TRIAGEM-RELATORIO.md` do motor; inteiros teores de 20840716, 20037894,
    20884353, 21034123, 19336426, 20856691, 20378185 e 20806766 já na biblioteca
    `jurisprudencia-tjsp/`): depositar os que a titular escolher. Precedentes do STJ citados nos
    votos e ainda sem página: AREsp 2.843.388/RJ, REsp 2.179.133/SP, AgInt nos EDcl no REsp
    2.029.860/MG.

## 2026-10-15

- **Ingestão (3ª leva)** — sete julgados capturados a partir das citações do REsp 2.052.228 e da
  ApCiv 1003610. Leitura e depósito feitos por um agente por julgado; conferência independente
  depois: 43 transcrições literais OK, resíduo de nomes e OAB vazio, varredura de injeção limpa.
  - STJ: **REsp 1.995.458/SP** (motoboy; tese integral está no voto-vista do Min. Cueva, a ementa
    ficou com "concorrência de causas" — atenção ao citar), **REsp 2.015.732/SP** (motoboy, dano
    moral R$ 3 mil), **REsp 1.875.164/MG** (inversão *ope legis* do art. 14, § 3º; caso de escola,
    tese transversal — candidato a migrar para um bundle de consumidor quando existir).
  - TJSP: **ApCiv 1001051** (falso advogado, idosa, culpa concorrente afastada, sem dano moral),
    **1002595** (falso advogado + empréstimo, dobro, dano moral R$ 5 mil, juros do evento),
    **1003655** (falso advogado + empréstimo pelo app, contrato nulo), **1001183** (acesso remoto,
    sem dano moral).
  - **Achados:** (i) dano moral é o ponto instável — 16ª Câmara deu R$ 10 mil (1003610) e negou
    (1001183); 19ª negou; 20ª deu R$ 5 mil; (ii) termo dos juros diverge entre câmaras contra o
    banco do correntista (citação × evento danoso); (iii) nenhum julgado aplicou redução por culpa
    concorrente.
  - **Pendências novas:** REsp 1.633.785/SP (precedente do banco, cartão com chip e senha) para
    contra-ataque; EAREsp 600.663/RS; REsp 1.197.929/PR; REsp 2.124.423/SP; "REsp 21.666/RJ"
    citado na 1001183 (número suspeito); p. 22 do REsp 2.015.732 perdeu uma linha na conversão.

- **Ingestão** — dois acórdãos do **TJSP** (chegaram em `consumir/` como "acórdãos do STJ sobre o
  golpe do falso advogado"; não são do STJ):
  - **ApCiv 1003610-33.2025.8.26.0664** (16ª CDPriv., Rel. Marcelo Ielo Amaro, j. 13/11/2025) —
    primeiro acórdão do acervo sobre o **golpe do falso advogado**. Raw pseudonimizado + página
    `vigente` (`apciv-1003610-tjsp-falso-advogado-perfil`).
  - **ApCiv 1017912-17.2022.8.26.0068** (Núcleo 4.0 Turma IV, Rel. Paulo Sergio Mangerona,
    j. 18/02/2025) — **não é falso advogado** (falsa venda de veículo por WhatsApp); entrou pela
    tese do banco recebedor × KYC (Res. 4.753/2019). Raw pseudonimizado + página `vigente`.
  - Pseudonimização: autor e beneficiário das transferências → rótulo; magistrados, réus PJ e
    número do processo mantidos. PDFs não depositados. Varredura de resíduo de nomes limpa.
- **Ingestão** — **REsp 2.052.228/DF** (3ª T., Rel. Min. Nancy Andrighi, j. 12/09/2023): inteiro
    teor oficial pseudonimizado em `raw/resp-2052228-df.md` + página `vigente`. Fecha a pendência
    de 05/07/2026. Citados no voto e ainda fora do acervo: REsp 1.197.929/PR (Tema 466),
    REsp 1.995.458/SP, REsp 2.015.732/SP, AgInt no AREsp 2.201.401/RJ (golpe do motoboy),
    REsp 1.875.164/MG (art. 14, § 3º).
- **Enunciado 14 do TJSP** — texto fornecido pela titular; idêntico ao transcrito na ApCiv 1003610.
    Página `em_teste` até depositar a publicação oficial (órgão e data).
  - **Pendências:** órgão e data oficiais do Enunciado 14 do TJSP; quatro acórdãos do TJSP sobre
    falso advogado citados na ApCiv 1003610 (lista na página); URI canônica do e-SAJ; p. 3 da
    ApCiv 1017912 com frases fora de ordem na conversão.

## 2026-08-02

- **Ingestão** — Migração final do acervo local `direito_bancario/golpes/` (Fase 4 do PRD de
  versionamento do `pma-workspace`). Entradas:
  - **REsp 2.222.059/SP** (3ª Turma, Rel. Min. Cueva, j. 08/10/2025) — inteiro teor oficial
    depositado em `raw/resp-2222059-sp.{md,pdf}` (versionado; varredura limpa) e página
    derivada `vigente` em `jurisprudencia/`. Era o precedente-mestre da skill
    `analise-perfil` do motor e ainda não estava no acervo.
  - `raw/notas-jurisprudencia-stj-fraude-bancaria.md` — nota de pesquisa pré-existente
    (resumo do REsp 2.222.059 + Súmula 479); depositada como material de trabalho, não fonte.
  - `raw/notas-estrategicas-fraudes-bancarias.md` — notas estratégicas do acervo antigo
    (nomenclatura da ação, checklist pré-processual, relatório DICT, Marco Civil para IP,
    tese "ato primário × ato secundário"). **Pendência:** destilar em `heuristicas/`
    (granularidade §4 — hoje viola a regra de 1 documento = 1 conhecimento; por isso está em
    `raw/`, não em `heuristicas/`).
  - A Res. BACEN 4.753/2019 que estava em `golpes/legislacao_principal/` foi depositada no
    bundle irmão `emprestimo-nao-realizado/raw/` (a página derivada do art. 2º mora lá).
  - Criado `raw/index.md` (catálogo — a pasta não tinha índice).
  - Não migrados: `casos_decididos/*.md` locais (versões pré-anonimização das cadeias já
    reconvertidas aqui — superadas) e as pastas de caso do escritório (camada C1 → Drive).

## 2026-07-05

- **Ingestão** — **Cadeia golpeA ingerida (ritual 7.5, primeira execução real).** Derivados: 1 caso-decidido (`origem: terceiro`), 2 contra-ataques (`sentenca->tj`: um argumentativo — culpa concorrente × dever de vigilância; um **probatório** — quantum provado por extratos × saldo), 1 página de jurisprudência citável (ApCiv 5005364-95.2023.8.21.0034/RS) e o perfil da 12ª CC do TJRS. Contra-ataques com `confianca_fonte: derivado-do-voto` (razões de apelação ausentes da cadeia — caminho degradado exercitado conforme planejado). Varredura de vazamento limpa (nomes de pessoas naturais do processo excluídos das páginas derivadas, regra 6.5).
  - Conversão: sentença que estava com 11 bytes na origem converteu com score 90 via escalonamento para tesseract; acórdão score 75 (colunas da ementa intercaladas — tese de julgamento marcada como "recomposta, conferir na fonte"). Pendências: URI canônica eproc; data de julgamento do acórdão a confirmar; capturar STJ REsp 2.052.228, Súmula 568 e TJRS ApCiv 5004251-64.2019.8.21.2001 (citadas no voto); avaliar docling/marker para PDFs em colunas (gatilho da D11 possivelmente atingido).

- **Ingestão** — Bundle criado (schema v0.4, D13). Cadeias copiadas de `direito_bancario/golpes/casos_decididos` para `raw/` com reconversão pelo portão de qualidade (a conversão legada tinha `sentenca_golpeA.md` com 11 bytes — falha silenciosa desde maio — e acórdão com colunas embaralhadas).

### Matriz de completude das cadeias

| Cadeia | inicial | contestação | sentença | razões de apelação | acórdão TJ | REsp | Situação |
|---|---|---|---|---|---|---|---|
| golpeA (ApCiv 5005364-95.2023.8.21.0034/RS) | ✔ | ✘ | ✔ | ✘ (derivar do voto) | ✔ | — | ingerida (contra-ataques `derivado-do-voto`) |
| golpeB | ✔ | ✘ | ✔ | ✘ | ✘ **sem acórdão** | — | pendente — cadeia sem desfecho; localizar acórdão |
| golpeC | ✔ | ✘ | ✘ **sem sentença** | ✘ | ✔ | — | pendente — localizar sentença e razões |
