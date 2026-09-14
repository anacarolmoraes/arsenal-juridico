# Log

## 2026-09-13 (consumo de `consumir/`: Caderno Scalabrin e EDcl no REsp 1.573.573)

- **`raw/caderno-scalabrin-atualizacao-dpc-2025-2026.{pdf,md}`** — 54 p., pdfmd sem `--strict` (nenhuma página exigiu conferência). Circula no git porque o autor licencia a redistribuição com citação da fonte (rodapé de cada página). Catalogado em `raw/index.md` com mapa por parte e lista do que serve a cada bundle. Sem página derivada: é síntese didática, não fonte oficial.
- **`sucumbencia/raw/edcl-agint-resp-1573573-rj-honorarios-recursais.{md,pdf,integral.md,estrutura.json}`** — EDcl no AgInt no REsp 1.573.573/RJ (3ª T., Bellizze, j. 04/04/2017, DJe 08/05/2017), 68 p., `--no-tables`. `.md` anonimizado (pessoas físicas e advogados; ficam ministros, a pessoa jurídica e o número); PDF e `.integral.md` fora do git (`.gitignore` §2). Página nova `sucumbencia/jurisprudencia/edcl-agint-resp-1573573-rj-honorarios-recursais.md`, `vigente`, com `tese:` (ementa, item I: seis requisitos cumulativos dos honorários recursais do art. 85, § 11), item II (critérios de cálculo) e voto-vogal da Min. Nancy Andrighi. **Portão de voz:** o `segmentar-acordao.py` não marcou as dezenas de ementas transcritas no voto (p. 6-62) porque a conversão não preservou aspas/itálico; a página avisa que só a ementa é transcrição segura sem conferência de autoria. Vinha anotado como pendência do `cobranca-honorarios` desde 21/07; é sucumbência, não cobrança, e mora aqui.

## 2026-09-13 (LINDB depositada no transversal)

`raw/lindb-dl4657-1942-compilada.{htm,md}` via `depositar-lei.py` (cp1252, 30 artigos, cobertura até a Lei 13.655, sem `<strike>`), a pedido da titular, para servir ao art. 6º (irretroatividade) do bundle imobiliário e a qualquer tese intertemporal. Sem página derivada por ora; recorte por artigo pelo `recortar-artigo.py --codigo`. Na mesma sessão, o bundle imobiliário recebeu o Tema 1.002/STJ (ver o log de lá).

## 2026-09-08/09 (petição inicial: intake, F4.1 minerada, perfis de 1º grau, ferramentas do workspace)

**Disparo:** notas graduadas em `sugestoes_peticao_inicial.md` do workspace (08/09), a partir do achado de que o pipeline da inicial nunca rodou em caso real (nenhuma `ANALISE.md`, `.estrutura.md` ou `tipo: inicial` em `clientes/`). Implementadas as notas ≥ 5, exceto o dry-run em inicial real, que é operação da titular. **No acervo:** (1) heurística transversal [matriz de documentos e roteiro de intake](peticao-inicial/heuristicas/matriz-documentos-da-inicial.md), Parte A (320), Parte B derivada do mapa probatório (uma pergunta por fato frágil ou a produzir; documento com o réu vira exibição do 397), Parte C gratuidade pela faixa da ADC 80; instanciada em `clientes/<caso>/DOCUMENTOS.md` e alimentando o rol `documentos:`; (2) [matriz de golpe bancário](../bancario/golpes/heuristicas/matriz-documentos-golpe-bancario.md) (`em_teste`): extrato integral para o perfil de uso, comprovante por transação, conta intermediária, MED, negativação; (3) **F4.1 executada em primeira passada**: o script `minerar-emendas.js` buscou o texto das comunicações dos 80 processos da fila do DJEN (desde 2025) e achou 12 despachos de emenda, gratuidade 9 e documento faltante 8 (comprovante de endereço em nome próprio, extratos de todas as contas, rendimentos de três meses), competência ou rito 6, valor da causa 2, qualificação 2; a contagem entrou no checklist de saída do index (320 e gratuidade) e na matriz; (4) [perfis/](peticao-inicial/perfis/index.md) de 1º grau com template e a contagem de órgãos da fila (Núcleos de Justiça 4.0 do TJTO concentram o volume; SJU de Palmas 21 processos; 2ª Vara Cível de Porto Nacional 6; 1ª Vara Cível de Palmas 4), nenhum perfil escrito; (5) workflow Etapa 0 com intake, `caso.json` e perfis; index com links. **No workspace:** skill `ficha-golpe-bancario` (dano material por transação com fonte, dupla contagem, dobro só sobre o que o réu cobrou e condicionado a 30/03/2021, encargos por verba com a cisão da Lei 14.905/2024, dano moral bifásico com mediana do grupo, valor da causa 292 V e VI, teto do Juizado; `--conferir PECA.md` acusa todo `R$` sem origem na ficha); `TEMPLATE_INICIAL_GOLPE_BANCARIO.md` (esqueleto único com as variáveis do tema, `estrutura: template`, rol de documentos, passa no `lint-inicial` v1 e v2); `radar-jurisprudencia/scripts/grupo-de-casos.js` (valores de dano moral por regex, candidatos a depósito); `orgaos-frequentes.js`; `caso.schema.json` + `qualificacao.js` (preâmbulo do 319, II, com concordância e preposição do estado); orchestrator 4.11.0 (intake e perfis no Estágio 0), validator 2.11.0 (ficha como gabarito do valor da causa). **Portões** (estrutura aprovada exigida pelo `md2docx` salvo `estrutura: template`; `lint-inicial` v2 com bloqueio de valor da causa divergente, `Doc. N` sem rol e "correção pela Selic", e avisos de 272 §5º, tutela sem número, alíneas e forma da gratuidade) ficaram em `planos/patch-manutencao-2026-09-08-inicial.js`, ensaiados em cópia (16/16 e 21/21), à espera de sessão `PMA_MANUTENCAO=1`. **Pendente e prioritário:** rodar o fluxo numa inicial real de golpe e anotar aqui o atrito.

## 2026-09-05 (réplica, segunda rodada: prova do réu, pedidos não combatidos, exibição, repertórios, saneamento)

**Cinco acréscimos ao fluxo de réplica, decididos pela titular depois de nota de custo-benefício** (itens com nota 7 ou mais; ficaram de fora ranking de impacto das teses, lint de cobertura por palavra-chave, jurisprudência do próprio juízo via DJEN e depoimento pessoal sobre a confissão). (1) **Estado da prova do réu** como coluna da Parte 1 da tabela (comprovado, frágil, sem prova, invocado e não juntado), espelho da coluna que a tabela da contestação tem para a prova do autor; regra nova no playbook: afirmação sem prova se responde pelo ônus, não pelo mérito. (2) **Pedidos da inicial × resposta da defesa** (Parte 2-B): pedido não combatido é incontroverso e vai para requerimento de julgamento antecipado parcial (art. 356, I, execução imediata pelo § 2º); página literal nova `cpc-arts-355-357` com aplicação. (3) **Documento invocado e não juntado** como quarto tipo da Parte 3: exibição pelos arts. 396 a 400, recusa inadmissível pelo art. 399, II (o réu aludiu ao documento para constituir prova), presunção do art. 400; aponta a página `peticao-inicial/jurisprudencia/cpc-arts-396-400`, já existente. (4) **Repertório de defesas típicas**: heurística transversal em `replica/heuristicas/` com formato e regras (tese como o réu a escreve → resposta → página do acervo → estado coberto/parcial/lacuna; fonte permitida é a titular e o acervo, nunca a pasta do cliente), e três esqueletos `em_teste` nos bundles temáticos: `bancario/golpes/heuristicas/repertorio-de-defesas-do-banco` (10 teses; lacunas Súmula 479, MED, dano moral favorável), `imobiliario/heuristicas/repertorio-de-defesas-da-loteadora` (13 teses; lacunas taxa de associação, anuência tácita na cessão, acórdão originário do IRDR), `digital/plataformas/heuristicas/repertorio-de-defesas-da-plataforma` (8 teses; lacunas Marco Civil, CDC e serviço gratuito, ilegitimidade da filial, dano moral). Pastas `heuristicas/` criadas em `golpes` e `plataformas`. (5) **Depois da réplica**: prazo comum de 5 dias do art. 357, § 1º anotado na cronologia na entrega (Etapa 5), e Etapa 6 nova, página de caso decidido no bundle temático com três respostas obrigatórias (incontroversos fixados? confissão acolhida? pedido não combatido julgado?), que realimenta o repertório. Checklist do playbook de 11 para 13 itens; checklist de saída do index de 8 para 10. No workspace: orchestrator e validator ajustados; lint de reedição da inicial (sobreposição réplica × inicial) **rascunhado fora dos portões** porque a sessão não é de manutenção; instalação pendente da titular.

## 2026-09-05 (réplica: cinco eixos, incontrovérsia, confissão, prazos paralelos)

**Fluxo de réplica ampliado (playbook, workflow, heurística, página nova), disparado pela comparação com o prompt "Réplica à Contestação Cível" do repositório Skills Jurídicas com IA (RSA Advocacia) e com as réplicas reais do escritório.** O prompt genérico perdia para o nosso fluxo em tudo que é portão (cabimento, prazo contado da decisão, art. 329, II, posturas do art. 436, art. 352), mas apontava quatro vãos que as peças protocoladas confirmavam: (1) **art. 341 ao contrário**: o bundle não cobrava do réu o fato que ele silenciou; a réplica do caso de rescisão de lote tinha capítulo de incontrovérsia feito sem apoio do fluxo. Agora é a Parte 2 da tabela e o capítulo III do playbook, com pedido de fixação no saneamento (art. 357, II) e antecipação das exceções do art. 341, I a III. (2) **Confissão e contradição da defesa**: onde o escritório mais ganha (tela de sistema que confessa o cancelamento, oficina que confessa os trinta dias, laudo que omite o que soma a diferença) não tinha etapa. Parte 3 da tabela + página literal `cpc-arts-389-395-408` (confissão, indivisibilidade e cisão do 395, documento particular do 408). (3) **Posturas acessórias com relógio próprio**: reconvenção (contestação à reconvenção em 15 dias, art. 343, § 1º; sem ela, revelia do autor), impugnação à gratuidade (art. 100, resposta no repertório do bundle `gratuidade`), agravo do réu contra a tutela, arguição de falsidade (art. 430). Parte 4 da tabela, portão 3 do playbook, Etapa 0 do workflow. (4) **Tese jurídica da defesa como quinto eixo**: a tabela tinha quatro eixos e mandava ignorar "mero mérito", mas a réplica de dezesseis capítulos do caso de rescisão respondia quase só a teses jurídicas da ré (IRDR, Lei 13.786, fruição), não a fatos novos. A prática contradizia o playbook. O eixo 5 passa a ser "negativa pura" (o único que não aciona réplica) e o eixo 4 "tese jurídica" recebe resposta do bundle temático; o playbook explicita que argumento de direito novo não é inovação (art. 322, § 2º), só fato e pedido são. Também: Parte 0 (roteiro de entrevista do autor gerado da contestação, espelho do da contestação), estrutura em sete capítulos com ordem III/IV/V declarada na estrutura, checklist de 8 para 11 itens, checklist de saída no index para o Estágio 6 do orchestrator. No workspace: orchestrator 4.9.0 (seção 6 da `ANALISE.md` e espelho da contestação no `estrutura.md`), validator 2.9.0 (bloco "Em réplica"), writer 3.6.0 (incontrovérsia e confissão em prosa). Do prompt da RSA **não** se importou: tom "combativo", pedidos em letras, impugnação de documento sem a técnica do parágrafo único do art. 436.

## 2026-09-05 (gratuidade: ADC 80 e sub-bundle transversal)

**Ingestão — STF, ADC 80 AgR/DF (Plenário, 18/10/2023), trazido pela titular em `consumir/`, + sub-bundle `gratuidade/` (v0.1.0).** O acórdão é só admissibilidade (legitimidade da CONSIF, controvérsia relevante em norma processual); o **mérito foi julgado em 03/09/2026** e ainda não tem acórdão publicado — página `stf-adc-80-merito-2026` criada `em_teste` a partir de seis fontes secundárias (presunção relativa até R$ 5.000,00 de salário; inconstitucionalidade do critério de 40% do RGPS e da Súmula 463, I, TST; todos os ramos salvo Juizados; só ações ajuizadas após a ata). Páginas: `stf-adc-80-agr-2023-admissibilidade` (`vigente`, inteiro teor no git — PDF público sem parte privada — com **vozes separadas**: ementa do Tribunal, repertório da CONSIF relatado, voto vencido de Fachin, pareceres), `cpc-arts-98-102` e `cpc-art-1072` (recortes pelo `recortar-artigo.py`). Heurísticas: `pedido-de-gratuidade-pos-adc-80` (portão da data + forma A/B pela faixa de salário) e `repertorio-do-banco-contra-a-gratuidade` (cinco argumentos da CONSIF com refutação; responde à pendência "impugnação à gratuidade sem fonte patrimonial" de 05/09). Tema 1.178 continua em `peticao-inicial/` e é referenciado, não duplicado.

**Ferramenta — dois defeitos do `pdfmd` expostos por PDF do STF, corrigidos no motor (`vendor/pdfmd`) do workspace:** (1) o "Inteiro Teor" do STF traz cada página **duas vezes** no fluxo de conteúdo (mesmo texto, mesmas coordenadas) e a extração nativa saía com todo parágrafo em dobro; o motor agora suprime o bloco repetido no mesmo lugar e o registra no manifesto (`suppressed_repeated`, `kind: duplicate_layer` — 272 blocos neste acórdão); (2) a prosa justificada era lida como tabela (uma palavra por célula) pelos dois detectores; opção nova `--no-tables` desliga ambos. Resultado: 1.503 → 705 linhas, 0 tabelas espúrias. Também fixados `OPENBLAS_NUM_THREADS=1`/`OMP_NUM_THREADS=1` nos wrappers, sem os quais a conversão morria por alocação de memória. Teste unitário no `tests/test_fidelity.py` (13/13). **Achado para o portão:** o `lint-citacoes` não reconhece `ADC` (nem ADO, Rcl, MS) como identificador de precedente — citação da ADC 80 saía como `FONTE_SEM_ID` e não era conferida. **Corrigido em sessão de manutenção no mesmo dia:** classes ADC/ADO/Rcl/MS incluídas e, para controle concentrado (ADI/ADC/ADO/ADPF), casamento por regex própria de número curto, como Súmula e Tema; teste com três citações (ementa da ADC 80, voto vencido, CPC) → 3 `VERIFICADA`; `npm test` 12/12.

## 2026-09-05 (terceiro relógio e transcrição da inicial)

**Contestação, dois fechamentos.** (1) **Terceiro relógio:** desinteresse na audiência de conciliação já designada é petição avulsa até dez dias antes (art. 334, § 5º); só o de ambas as partes cancela a audiência (§ 4º, I) e a ausência injustificada é ato atentatório (§ 8º). Entrou no playbook (portão 1 e checklist), no workflow (Etapa 0, agora com três relógios) e na heurística (Parte 3); o `legal-orchestrator` passa a registrar a decisão sobre conciliar em toda inicial e contestação. (2) **Transcrição da inicial × `lint-citacoes`:** testado com inicial sintética na pasta do caso. Bloco `>` sem atribuição bloqueia; atribuição sem identificador é aviso e não verifica; atribuição com o número CNJ dos autos faz o lint achar o `.md` da inicial e conferir a literalidade (exata = verificada; recorte = aviso de suspeita). Convenção fixada no playbook (capítulo V) e na heurística: `(Petição inicial, autos <CNJ>, p. X)`. Nenhum portão foi alterado.

## 2026-09-05 (lado, reconvenção, documentos, prosa da impugnação)

**Contestação, quatro ajustes decididos pela titular.** (1) **Lado:** o escritório defende por padrão o consumidor como réu; `lado: consumidor | fornecedor` passa a ser declarado na `ANALISE.md` no Estágio 0, e o capítulo de ônus da prova segue o lado (consumidor pede a inversão do art. 6º, VIII, do CDC e a exibição do que só o fornecedor tem; fornecedor a enfrenta). Para fornecedor, o acervo tende a não cobrir as defesas e a peça o diz. (2) **Reconvenção** tratada como inicial embutida: causa de pedir própria, pedido certo, valor da causa pelo art. 292 (regra canônica do escritório), custas ou gratuidade, conexão declarada; validator marca CRÍTICO a reconvenção sem esses requisitos. (3) **Documentos:** rol declarado no frontmatter da peça (`documentos:`) e script `checar-docs.js` no validator do motor, que confere citado × rol × arquivo e imprime o rol para o fim da peça (art. 434). (4) **Prosa da impugnação:** o capítulo V é o que mais sai em cadência de tabela; playbook, legal-writer e humanizer-forense ganharam a mesma regra (três a cinco blocos temáticos, versão do réu como fio, "o autor alega" e "não procede" no máximo uma vez cada). Pendências apontadas e não tratadas: terceiro relógio (desinteresse na audiência, dez dias antes), impugnação à gratuidade do autor sem fonte patrimonial, citação da inicial em bloco × lint-citacoes (a testar), prazo de contestação fora da fila do DJEN.

## 2026-09-05 (F3 da petição inicial: fontes depositadas pela titular)

**Ingestão — cinco depósitos em `peticao-inicial/raw/`** (vindos de `consumir/` do workspace): Súmulas 43, 54 e 362 (páginas individuais do site do STJ), inteiro teor do REsp 1.152.541/RS (29 p., score 100) e do REsp 1.988.687/RJ, Tema 1.178 (120 p., score 90). Conversão pelo `pdfmd`, sidecars pelo `ingest-prep`. As três súmulas **reprovam no sidecar (score 45)** por serem tabelas de precedentes com poucos caracteres de prosa; o enunciado é texto nativo e foi conferido, e as páginas apontam `raw:` para a compilação oficial já aprovada em `/recurso-especial/raw/SumulasSTJ_oficial.pdf`, mantendo os PDFs individuais como fonte secundária.

- Páginas novas: `sumula-43-stj`, `sumula-54-stj`, `sumula-362-stj` (tipo súmula), `resp-1152541-rs-metodo-bifasico` e `resp-1988687-rj-tema-1178-gratuidade` (tipo acórdão, com `tese:`, trechos-chave literais com página do PDF), `cc-arts-389-405-406` (literal, Lei 14.905/2024).
- Heurísticas novas: `juros-e-correcao-na-inicial` (tabela verba × índice × termo inicial; **regra do escritório de direito intertemporal, decisão da titular em 05/09/2026:** depois da vigência da Lei 14.905/2024 aplica-se a lei quando não há sentença ou acórdão, ou quando a decisão não estipulou outro índice) e `quantificar-dano-moral-metodo-bifasico` (as duas fases na inicial; valor no 292, V).
- Checklist de saída e playbook atualizados para apontar as duas heurísticas. Pendências do PRD reduzidas a F4 (mineração das emendas, perfis de juízo) e F5 (portões).

## 2026-09-05 (continuação)

**Ingestão — O'Keefe (1999), meta-análise sobre argumentos contrários, + heurística transversal `refutar-ou-omitir`.** Artigo trazido pela titular em `consumir/`; convertido com `pdfmd --ocr auto` (22 p., OCR em duas colunas com ordem de leitura ambígua em todas as páginas; sidecar gerado pelo `score_markdown` do `ingest-prep.py`, nota registrada). Depositado em `raw/` como obra de terceiro, no `.gitignore`. Achados aproveitados, do resumo e dos resultados (legíveis): refutar o argumento contrário é mais persuasivo e mais crível do que ignorá-lo; **reconhecer sem refutar é pior do que ignorar**; a ordem (refutar antes, depois ou entrelaçado) não tem efeito; escolaridade e posição inicial do leitor não moderam. Não aproveitados: tamanhos de efeito, modelo de elaboração, achados sobre publicidade. Consequências no acervo e no motor: heurística nova em `heuristicas/`, definição de "admite com ressalva" endurecida no playbook da contestação (a ressalva remove a consequência, ou é reconhecimento sem refutação), fraqueza ALTO no `legal-consistency-validator` para argumento contrário mencionado sem refutação, e proibição das fórmulas de reconhecimento sem refutação no `legal-writer`.

## 2026-09-05

**Contestação, ajustes após avaliação de prompt externo (`02-contestacao-civel.md`, RSA).** O prompt foi rejeitado (procedimento sumário inexistente, pedido contraposto confundido com o art. 343, prazo "da citação" ignorando os três termos do 335, súmulas sem acervo), mas rendeu quatro ideias incorporadas à heurística e ao playbook: **exposição por pedido** (1-B: valor, probabilidade justificada pela prova, resposta principal e subsidiária com compensação e dedução do já pago), **depoimento pessoal do autor** como postura nomeada (art. 385), **roteiro de entrevista do réu gerado da inicial** (Parte 0, no lugar do formulário genérico) e pedidos subsidiários explícitos. Da revisão própria: **dois relógios** na Etapa 0 (contestação × agravo da liminar já deferida, art. 1.003, § 5º), **granularidade por episódio** (dez a vinte linhas, não sessenta), **postura por documento do autor** (1-C, art. 436) e **escopo declarado** (procedimento comum; Juizado Especial fora, Lei 9.099, arts. 30 e 31). Fluxo ainda não testado em caso real, por decisão da titular.

## 2026-09-04 (fluxo da petição inicial)

**Fluxo próprio da petição inicial construído (F1 e F2 do PRD `planos/2026-09-04_prd-fluxo-peticao-inicial.md` do workspace).** Sai da fila de estoque; resta só o agravo de instrumento. Sem fonte nova: tudo transcrito do CPC, CDC e Lei 9.099 já em `raw/`.

- `peticao-inicial/playbooks/playbook-peticao-inicial.md` — esqueleto único extraído do "Encadeamento Canônico — Inicial PMA" do `legal-writer` e das seções "Estrutura da peça" dos playbooks de inicial dos bundles `bancario/emprestimo-nao-realizado` e `imobiliario`, que agora apontam para cá e guardam só o que é da matéria. Cinco variáveis declaradas (preliminares, posição da tutela, danos, competência, gratuidade).
- `peticao-inicial/workflows/peticao-inicial.md` — etapas espelhando os estágios do `legal-orchestrator` (`ANALISE.md` → estrutura aprovada → redação → validação → compilação → pós-despacho).
- Cinco heurísticas: competência e foro (Lei 14.879/2024, art. 63 §§ 1º e 5º), juizado × vara comum, tutela provisória (300/303-304/311, posição do capítulo), exibição a partir do mapa probatório (397 com categoria, 400), emenda (321/330/331 e retroalimentação do checklist).
- Seis páginas de legislação (literal, `raw:` resolvido): CPC 319-321/330/331/334 §§4º-5º; 46/53/63; 300-304/311; 396-400; CDC 101, I; Lei 9.099 arts. 3º/9º/54/55.
- `index.md` do bundle promovido a "fluxo completo"; `atividades.md` ganhou "Redigir Petição Inicial"; checklist de saída do 319/320 (04/09) mantido no `index.md` da peça.
- **Pendências registradas no `index.md`:** F3 (Súmulas 43/54/362 + Lei 14.905; método bifásico; Tema 1.178) depende de depósito da titular; F4 (mineração das emendas na fila do DJEN; perfis de juízo). A página `apelacao-1027749-tjsp-exibicao-art-400.md` (bundle `bancario/juros-abusivos`) continua órfã: o playbook de consignado a menciona sem link porque está em outro bundle; quem a liga é o playbook de inicial de `juros-abusivos`, quando existir.

## 2026-09-04 (fluxo de contestação)

**Fluxo novo: Contestação (bundle v0.9.0).** Gatilho: avaliação, pedida pela titular, de um roteiro de seis prompts para contestação (entenda a inicial → fragilidades → fatos × provas → estratégia → ataque à própria defesa → redija). Veredito: setenta por cento já existia no orchestrator (ANALISE.md e validator); o que faltava era a **inversão de perspectiva do art. 341**: a análise do escritório mapeava os fatos da própria tese, e a contestação exige mapear os fatos da inicial do outro, um a um, com a postura do réu e a prova. Fontes: Scarpinella 2024 §5.1 a §5.3 (linhas ~7654 a 7860 do raw aprovado) e quadro do capítulo (~7928), CPC compilado. Entregues: página literal `cpc-arts-335-346` (o capítulo inteiro; o 337 comentado continua na página da réplica), heurística `tabela-impugnacao-especificada` em três partes (fato a fato da inicial com estado da prova do autor, versão do réu, prova do réu e postura nega/admite/ressalva/fato novo; checklist dos treze incisos do 337 com coluna "preclui se calada"; posturas acessórias como decisão da titular), playbook (portões, defesa direta × indireta e o que cada uma faz com o art. 373, estrutura em onze capítulos condicionais, seis armadilhas, checklist de dez itens) e workflow espelhando os estágios do orchestrator. Rejeitado do roteiro original: redigir "exclusivamente das análises anteriores" (o redator lê o documento, não o resumo; lição de 2026-08-04), placeholder [VERIFICAR] (o portão é parar e pedir) e ordem fragilidades-antes-de-provas. Lado do motor: orchestrator ganhou a seção 5 da ANALISE.md e o bloco de contestação no Estágio 0.5; validator ganhou a checagem do art. 341 e a lente do autor. Estoques restantes na fila: agravo de instrumento, petição inicial.

## 2026-09-04 (continuação)

**Ingestão — três fontes menores + um julgado que fecha pendência de direito intertemporal, bundle v0.8.0.** Quatro depósitos
na mesma leva de saneamento de `consumir/`:

1. **Cartilha de linguagem simples da Ouvidoria do STJ** → `raw/paralembrar-linguagem-simples-stj.{pdf,md}` +
   heurística [`heuristicas/linguagem-simples-como-o-stj-escreve.md`](heuristicas/linguagem-simples-como-o-stj-escreve.md).
   Confirma, na voz do próprio Tribunal, exigências que o `humanizer-forense` já perseguia por conta própria (voz
   ativa, frase curta, sem "vai/irá").
2. **Resolução CNJ 615/2025** (governança de IA no Judiciário) → `raw/resolucao-cnj-615-2025-ia-judiciario.{pdf,md}`,
   página [`jurisprudencia/resolucao-cnj-615-2025-ia-judiciario.md`](jurisprudencia/resolucao-cnj-615-2025-ia-judiciario.md)
   e heurística [`heuristicas/decisao-com-apoio-de-ia-o-que-arguir.md`](heuristicas/decisao-com-apoio-de-ia-o-que-arguir.md).
   **Achado central:** o art. 10, III, veda de forma absoluta — não como questão de grau de risco — que sistema de
   IA "classifique ou ranqueie pessoas [...] para a avaliação da plausibilidade de seus [...] testemunhos"; e o
   art. 33, § 3º, torna a revelação do uso de IA **no texto da decisão** uma faculdade do signatário, não um
   dever — argumento que a titular não deve tentar ("a decisão não revelou uso de IA" não é nulidade).
3. **Manual de Práticas Cartorárias do TJSP (2016)** → `raw/manual-praticas-cartorarias-tjsp-2016.{pdf,md}`, 340
   páginas, CPC artigo por artigo com sugestão de minuta e observação. Convertido por OCR (PDF com texto nativo
   corrompido — mesmo padrão de `resp_2188970` e do manual de padronização). **Quatro páginas de fluxograma
   (332, 337-339) ficam sinalizadas `reading_order_ambiguous`**: são diagramas de caixa-e-seta (tutela
   provisória, penhora, avaliação, expropriação), não texto linear — a transcrição dessas páginas não presta para
   prosa, mas o procedimento que ilustram já está descrito nos artigos vizinhos. Depósito de referência; sem
   página derivada ainda (340 páginas de uma fonte de 2016 não justificam derivação exaustiva sem um caso
   concreto puxando um artigo específico — e o texto pode estar superado por emenda posterior, como o próprio
   art. 921).

Registro à parte, em `execucao/defesa-executado`: o **REsp 2.188.970/PR** (Quarta Turma, j. 18/03/2025) fecha a
pendência de direito intertemporal da tese de prescrição intercorrente — como aplicar o art. 921, § 4º
(Lei 14.195/2021) a execução que atravessa CPC/1973, CPC/2015 original e o regime atual. **Achado de método,
não só de conteúdo:** o voto transcreve o acórdão do TJPR dizendo que os Temas 566-571 (fiscais) são
"igualmente aplicáveis às execuções cíveis" — é a voz do TJPR, não do STJ, e o próprio STJ rejeita esse
fundamento duas linhas depois. Ver a página, que documenta a armadilha de atribuição em detalhe.

## 2026-09-04

**Ingestão — Manual de Padronização de Textos do STJ, 3ª ed. (2024) → bundle v0.7.0.** Estava convertido
desde 02/08 na caixa de entrada da titular e só tinha sido lido para o PRD de leitura semântica; não havia
cópia no acervo. Depositado em `raw/manual-padronizacao-textos-stj-3ed-2024.{pdf,md}` como fonte
transversal (é obra institucional do Tribunal, com autorização expressa de reprodução — circula, como o
RISTJ). Higiene antes do depósito: **675 blocos de OCR de imagem duplicado** removidos pelo
`reparar-ligaduras.py --remover-ocr-de-imagem`; ligaduras partidas, zero; páginas com `review_required`, zero.
Índice, manifesto e imagens do pdfmd ficam ao lado, fora do git pela regra §4.

**Triagem do que o manual rende.** Das três partes, a segunda (atos administrativos: ofício, portaria,
edital) não gera conduta para peça. Da primeira e da terceira saíram **três heurísticas transversais**,
todas `vigente` porque transcrevem regra do próprio Tribunal, com a página PDF de cada uma:

- [`heuristicas/citar-e-transcrever-como-o-stj.md`](heuristicas/citar-e-transcrever-como-o-stj.md) — a
  fórmula oficial de referência de julgado (classe encadeada com *no/nos/na*, `n.` e não `nº`, ponto de
  milhar, UF após barra, relator ou relatora flexionado, órgão por extenso, datas sem zero), súmula em
  quatro usos, artigo (ordinal até nove), transcrição com fonte entre parênteses antes do ponto
  (procedimento da Presidência), folhas, cargos, quantia com extenso, latim em itálico, e a lista de
  palavras que o manual manda evitar (*inobstante, vez que, no que pertine, o mesmo*).
- [`heuristicas/siglas-classes-processuais-stj.md`](heuristicas/siglas-classes-processuais-stj.md) — os
  78 pares sigla → classe do item 2.13, íntegros e na ordem do original, mais as regras de plural,
  maiúscula e encadeamento.
- [`heuristicas/ementa-do-stj-anatomia.md`](heuristicas/ementa-do-stj-anatomia.md) — as três partes e as
  dez orientações do verbete *ementa*. O achado que muda a leitura de acórdão: **a ementa do STJ não
  transcreve julgado nem súmula e não referencia precedente** (orientações 3 e 5). Texto de outro tribunal
  atribuído "à ementa" está, por construção, no relatório ou no voto — é a razão institucional do portão de
  voz do `lint-citacoes` (PRD de 02/08). A ordem dos itens da ementa é a ordem dos fundamentos no voto
  (orientação 4), o que dá um mapa para localizar o trecho que sustenta cada tese.

**Pendências que ficam:**

1. O `lint-citacoes` (`skills/peca-pma-builder/scripts/lint-citacoes.js`, `CLASSES_SUPERIOR`) reconhece
   11 siglas; a lista oficial tem 78. Ampliar o detector a partir da página de siglas é tarefa do motor,
   não do acervo. Ao menos RMS, RHC, CC, Rcl, MS, SLS, EDcl, PUIL e SIRDR aparecem em peça do escritório.
2. O Vocabulário Jurídico do STJ (orientação 10 da ementa) não está depositado; o manual só dá dois
   exemplos. O PRD de leitura semântica já prevê uma versão mínima.
3. O padrão de ementa estruturada por campos que a `estrutura-ai-first` chama de "padrão CNJ/STJ" não
   consta desta edição do manual e segue sem fonte oficial em `raw/`.
4. Da mesma pasta de origem, o Manual de Organização 2026 e o manual revogado ficam de fora por decisão
   do PRD de 02/08 (só o cap. 5 interessava, e já foi lido).

## 2026-08-29

**Ingestão — tese de doutorado sobre objeto dos recursos (Buril, USP 2019).** Depositada em
`raw/tese-buril-objeto-dos-recursos-2019.{pdf,md}` e posta **fora do git** antes de qualquer commit
(obra intelectual de terceiro; acesso público na biblioteca digital da USP não é licença para
redistribuir num repositório compartilhado). Conversão pdfmd: **420/420 páginas, 0 aviso, 0
`review_required`**, 1 página por OCR.

**Triagem honesta do que a obra rende.** É tese teórica e propositiva: dos cinco capítulos, dois são
história do efeito devolutivo (direito romano, visigótico, canônico, lusitano, Regulamento 737 aos
CPCs de 39 e 73) e um é direito comparado (Itália, Portugal, Espanha, Inglaterra, EUA, Argentina,
Peru). Isso não gera conduta. O que gera está no Capítulo III, e virou **uma** heurística:
[`apelacao/heuristicas/extensao-e-profundidade-do-devolutivo.md`](apelacao/heuristicas/extensao-e-profundidade-do-devolutivo.md).

O achado aproveitável é a **função residual da causa de pedir recursal**. Sendo a profundidade do
efeito devolutivo automática (art. 1.013, §§ 1º e 2º), o tribunal pode julgar por fundamento que a
apelação não articulou — mas a fundamentação recursal segue fazendo duas coisas: sustenta a
**dialeticidade** (admissibilidade, art. 932, III) e **obriga o tribunal a responder**. Como é a
resposta devida e não dada que abre os embargos, e são os embargos que constroem o prequestionamento,
a regra prática que fica é: *na apelação se articula tudo não pela devolução, mas para construir o
registro do REsp*. A página amarra isso à assimetria com a Súmula 283/STF, já coberta pela
`recurso-especial/heuristicas/tabela-de-fundamentos` — a omissão inofensiva na apelação é fatal no
especial.

Nasce **`em_teste`**, e a página diz por quê: a descrição do art. 1.013 é pacífica, mas o encadeamento
acrescentado vem de fonte única e sem conferência contra jurisprudência do TJTO e do STJ. As
proposições do autor que **não são direito posto** estão isoladas em seção própria (crítica ao
"gigantismo"; profundidade como regra exclusiva da apelação; realocação da dialeticidade;
irrelevância da causa de pedir recursal), para que ninguém as cite como lei.

**Falso positivo do `reparar-ligaduras.py`, e um cego do script.** O reparo automático propôs 3 formas
(4 substituições) e uma delas era **espúria**: `plaintiff presented → plaintiffpresented`, em citação
de doutrina estadunidense — adotar em bloco teria corrompido o texto. Descartado o `.reparado.md`;
aplicadas à mão só as duas válidas. Na conferência apareceu um ponto que o script **não** enxerga: ele
só reconhece a forma ASCII (`fi eld`), e o PDF trazia também o **caractere** de ligadura tipográfica
U+FB01 — 6 ocorrências, todas em citação em inglês, duas partidas por espaço e quatro íntegras
(`specific`, `find`, `field`, `find`), que passariam incólumes e quebrariam qualquer busca por
"field"/"find". Normalizadas à mão; conferido que não restou U+FB00/FB02/FB03/FB04. Tudo registrado em
`raw/tese-buril-objeto-dos-recursos-2019.ligaduras.md`. **Lição que fica: volume baixo de propostas
não significa reparo seguro — significa que o que sobra tem alta chance de ser falso positivo.**

**Armadilha para quem for recortar desta fonte:** 333 das 420 páginas trazem bloco `> OCR da imagem`
duplicando o texto nativo (mesma classe já catalogada no `raw/index.md`), e a versão do OCR é a pior
(`TIMG`, `perícial`, `sámula`). Registrado no catálogo.

**Ingestão — Imersão "Relevância na Prática": 16 arquivos triados, 13 depositados.** Material de curso
pago trazido pela titular (`consumir/material_pratica_relevancia_STJ`). Triagem por hash antes de
qualquer conversão: `Emr_55_2026_STJ.pdf` é **byte-idêntico** ao `raw/ristj-er55.pdf` já depositado em
08-26; a ER-53 e a Lei 15.484 do curso são outras impressões de normas já ingeridas — as três
descartadas sem conversão. Os 13 restantes foram convertidos pelo pdfmd (sem `--strict`; nenhum aviso
pendente) e os 3 `.docx` por extração direta do `word/document.xml`.

**Pendências fechadas nesta rodada** (todas abertas em 08-18 ou 08-26):

- **(a) Literal da CF, art. 105, §§ 2º-3º.** A `cf-art-105-iii` carregava paráfrase deliberada, porque o Planalto é inacessível do sandbox e a regra pós-caso-AREsp proíbe transcrever de memória. A **EC 125/2022** veio no material, foi depositada (`ec-125-2022-relevancia.{pdf,md}`) e a paráfrase deu lugar ao texto conferido. Página nova [`ec-125-2022`](recurso-especial/jurisprudencia/ec-125-2022.md) registra o que a emenda decidiu e por que o art. 2º dela **não** é o marco de transição (é o art. 4º da Lei 15.484) — sobrevive dele a faculdade de **atualizar o valor da causa**, leitura que Koehler e Bonizzi (RePro 333/2022) confirmam.
- **(b) Ato regulamentar do art. 343-A.** A página do 343-A pedia "acompanhar o ato regulamentar da Presidência" desde 07/2026. Ele existe: **IN STJ/GP 42/2026**, DJe de 20/08/2026. Depositada e derivada em [`instrucao-normativa-stj-gp-42-2026`](recurso-especial/jurisprudencia/instrucao-normativa-stj-gp-42-2026.md). **Muda a prática:** o resumo deixa de ser seção do preâmbulo e vira **campo estruturado do sistema**, preenchido **no ato da interposição no juízo a quo** (art. 3º, §§ 4º-5º); cinco campos, o quinto exclusivo do REsp e destinado à relevância; 3.000 caracteres recomendados por campo; inexatidão deliberada pode ser tratada como ato atentatório à dignidade da justiça, com comunicação à OAB (art. 4º, p.ú.); vício é sanável em 10 dias por certidão automatizada (art. 5º). **Ainda não é exigível** — o art. 12 condiciona a portaria da Presidência, com gatilhos separados para o sistema do STJ e para cada tribunal de origem. Não se aplica à Terceira Seção. *Monitorar as portarias, e a habilitação do TJTO.*
- **(c) Página do procedimento do Capítulo II-A.** O recorte existia desde 08-26 sem análise. Escrita [`ristj-cap-ii-a-relevancia`](recurso-especial/jurisprudencia/ristj-cap-ii-a-relevancia.md), conferida artigo a artigo contra o recorte oficial, não contra a doutrina: duas técnicas (255-C), quóruns (2/3 para rejeitar; maioria absoluta para competência), plenário virtual, suspensão nacional de 6+6 meses (255-N), temas **negativos** com agravo interno e AREsp incabível (255-M, § 4º), *fast track* de reafirmação (255-S) e a presunção do art. 255-AE, § 3º (mérito julgado sem deliberação sobre relevância presume-se caso concreto — logo, sem eficácia expansiva).
- **(d) Reconsolidação do RISTJ.** O log de 08-26 registrava que `ristj-er53.md` ficaria parcialmente superado "sem reconsolidação disponível ainda". O material trouxe o **RISTJ consolidado até a ER-55** (edição do Gabinete do Diretor da Revista, ER-55 de 21/08/2026, DJe 26/08/2026, 515 p.), depositado como `raw/ristj-consolidado-er55` (transversal, ao lado do `ristj-er53`, que fica como registro histórico).

**RISTJ consolidado até a ER-55 — depósito, reparo e regeração dos recortes.** O volume (515 p.,
edição do Gabinete do Diretor da Revista, DJe 26/08/2026) foi convertido com o pdfmd: **515/515
páginas, 0 aviso, 0 `review_required`**, 10 páginas por OCR. Passou pelo `reparar-ligaduras.py` —
**192 formas** de palavra partida, todas conferidas contra falso positivo (`ex officio` é latim e ficou
como está); uma correção manual fora do alcance do script: o extrator devolveu `Aperfi çoamento` no
art. 331-A e a junção daria `Aperfiçoamento`, errado de todo modo — corrigido para **`Aperfeiçoamento`**,
grafia que o próprio documento usa nas outras 52 ocorrências. O `.diff` fica depositado para conferência.

Com a fonte nova, os quatro recortes do RISTJ no `recurso-especial` que a ER-55 tornou obsoletos
(arts. **34, 104-A, 121-A e 255** — todos na lista de artigos alterados) foram regerados. Duas
armadilhas do consolidado apareceram e estão documentadas no cabeçalho de cada recorte e no
`raw/index.md` transversal: (1) a **duplicata por OCR de imagem** faz o recorte automático começar pela
versão pior do texto (`Art.255.0O recurso especial...`); (2) o volume traz um **apêndice com todas as
emendas históricas**, em que `Art. 255...` reaparece dezenas de vezes com reticências, fora do corpo do
Regimento. Além disso, o corte pelo fim varreu os 33 artigos do Capítulo II-A para dentro do recorte do
art. 255 — a mesma limitação do script já registrada em 08-26 (não percorre sequência com sufixo de
letra). Resultado: os quatro recortes foram limpos à mão, cada um com a limpeza declarada no cabeçalho,
e conferidos — um artigo por arquivo, com o texto pós-ER-55 e as marcas "(Redação dada/Incluído pela
Emenda Regimental n. 55, de 2026)". `ristj-er53` e `ristj-er55` ficam como registro histórico; **para
citar em peça, a fonte agora é `ristj-consolidado-er55.md`**.


**Descoberta que não estava em nenhuma fonte do acervo: a presunção não dispensa o tópico.** O
art. 255-J, parágrafo único, do RISTJ exige a demonstração da relevância "**inclusive nas hipóteses de
presunção**", sob pena de inadmissão na origem ou não conhecimento. O playbook antes recomendava
"invocá-la E fundamentar subsidiariamente" — conduta que por acaso satisfaz a regra, mas por prudência,
não por conhecê-la. Agora é portão explícito. Junto vem o risco do art. 255-K, § 2º: no inciso III
(500 salários mínimos), o STJ pode rever **de ofício** o valor da causa e negar a relevância se ele não
corresponder aos arts. 291-293 do CPC — invocar o piso sem conferir a fixação do valor é tiro pela
culatra. Ambos viraram a heurística
[`relevancia-presumida-como-enquadrar`](recurso-especial/heuristicas/relevancia-presumida-como-enquadrar.md),
que cobre as seis hipóteses uma a uma. Conferido que o documento de método solto na raiz
("Modelo Mental, Método e Estrutura para LLM", 817 linhas) **não menciona presunção** em nenhuma linha —
a heurística preenche lacuna, não duplica.

**Heurística nova a partir de conferência que contrariou a fonte.** O artigo do JOTA (29/07/2026,
anterior à ER-55) projetava que o tema de relevância carregaria os mesmos efeitos do repetitivo, e lista
arts. 311, 332, 496, § 4º, e 521 ao lado do 927 e do 932. Conferido contra a
`lei-15484-2026-alteracoes-cpc`: a lei alterou **927 (III-A)** e **932 (IV/V, b)**, mas **não** tocou nos
arts. 311, 332, 496 e 521, que seguem falando apenas em recursos repetitivos. A heurística
[`efeitos-do-tema-de-relevancia-fora-do-resp`](recurso-especial/heuristicas/efeitos-do-tema-de-relevancia-fora-do-resp.md)
separa os dois grupos e marca o segundo como **construção pela via do 927, III-A** — tese fundamentável,
nunca premissa. Interessa fora do REsp: tema negativo muda a estratégia já na inicial.

**Fluxos atualizados.** Playbook (portão 9, item 2 do resumo reescrito para o regime da IN 42, item 3
com remissão à heurística, 3 erros novos a evitar); mapa de rotas (tema negativo → agravo interno com
âncora regimental; rejeição pela Turma exige colegiado); `atuacao-no-stj-pos-protocolo` ganhou seção do
**Plenário Virtual da Relevância** — 7 dias corridos, acompanhamento em tempo real, e o comunicado do STJ
de 25/08/2026 que moveu início e encerramento das sessões virtuais para as **11h30** (não retroage a
pautas já publicadas). A sustentação oral por vídeo no virtual está marcada como **interpretação
doutrinária, não texto regimental**: o art. 255-S não a prevê, e a tese é de Salomão, Bellizze, Gajardoni
e Marchiori — que redigiram a emenda, o que dá peso, mas não converte em norma.

**Distribuição.** As 6 obras doutrinárias e os 3 modelos do curso são obra de terceiro e entraram no
`.gitignore` (`doutrina-relevancia-*`, `curso-relevancia-*`) **antes** de qualquer commit — o excerto do
livro coordenado por Campbell Marques traz vedação expressa de reprodução. Circula o catálogo novo
[`recurso-especial/raw/index.md`](recurso-especial/raw/index.md), que registra o que cada fonte rendeu.
Os modelos do curso contêm nome de parte e número de autos de processo de terceiro: anotado no catálogo
que não se reaproveita o texto sem limpar. Nenhuma linha dos modelos foi transcrita nas páginas — o que
foi para o acervo é conhecimento reescrito.

Na mesma passagem, uma regra que já era prática virou texto no `.gitignore`: **subprodutos do pdfmd
(`*_assets/`, `*.pdfmd.json`, `*.index.md`) não são versionados.** Zero deles existia no repositório, mas
nada impedia que entrassem por descuido — e a pasta de imagens do RISTJ consolidado sozinha tem
**127 MB**. Circula o par canônico `.pdf` + `.md` (e o `.quality.json`, que segue versionado); quem
precisar das imagens reconverte a partir do PDF, que está depositado.

**Ressalvas de fonte.** (1) O dia do mês na epígrafe da IN 42 está rasurado no PDF oficial e o OCR
devolve lixo; o que se conferiu é a publicação no DJe de 20/08/2026 — declarado na página. (2) Vargas
(e-book RPGMJ) e o capítulo de Fuga (2023) ficaram **sem página derivada**: o primeiro é teórico-
institucional sem consequência operacional, o segundo defende alteração legislativa que a Lei 15.484 em
boa parte realizou. Depositados e catalogados para consulta.

## 2026-08-26

**Ingestão — núcleo transversal de sucumbência (v0.5.0 → v0.6.0).** Criado `sucumbencia/` com duas teses `em_teste`: decaimento mínimo quando o pedido principal é acolhido e a divergência se limita à quantificação; e impossibilidade de o rateio de verba única reduzir indiretamente os honorários abaixo do piso do art. 85, § 2º. Fundamentos: TJGO Ap. 5412926-72.2023.8.09.0051 (`em_teste`) e TJSP Ap. 1096878-68.2017.8.26.0100 (`vigente`). As três fontes desta rodada foram depositadas como recortes `.md` anonimizados em `raw/jurisprudencia/`, sem PDFs e sem dados das partes. O precedente do TJSP teve inteiro teor e metadados conferidos no e-SAJ em 26/08/2026; os precedentes do STJ que ele cita permanecem pendentes de ingestão individual.

**Ingestão — Emenda Regimental n. 55 (o lado RISTJ da relevância, pendência "d" de 08-18).** Depositados `raw/ristj-er55.{pdf,md}` (conversão pdfmd limpa: 0 ligadura quebrada, 0 duplicata por OCR de imagem; as 3 páginas com anotação de PDF são brasão e logotipo do BDJur, sem conteúdo normativo, conferidas visualmente). A ER-55, de 21/08/2026, em vigor **3/9/2026**, insere no RISTJ o **Capítulo II-A** inteiro (arts. 255-A a 255-AE — procedimento completo da relevância: seleção do recurso representativo, deliberação, rejeição/reconhecimento por 2/3, reafirmação de jurisprudência, distinção e superação de tema) e altera pontualmente, de forma fragmentária, os arts. 2º, 11, 12, 21-E, 34, 44, 104-A, 121-A, 162, 173, 177, 184-A, 185, 187, 253 e 255 — o `ristj-er53.md` fica parcialmente superado nesses artigos a partir da vigência, sem reconsolidação disponível. Gerado recorte manual `recurso-especial/raw/ristj-arts-255A-255AE-capitulo-iia.md` (o `recortar-artigo.py` não percorre sequência de artigos com sufixo de letra dentro do mesmo capítulo; removida 1 duplicata de tabela truncada no § 1º do art. 255-AE, mantida a versão em parágrafo, idêntica). Ainda sem página derivada — fica pronto para quando alguém escrever a análise do procedimento.

**Bug corrigido no `recortar-artigo.py` (mesma classe do bug do `depositar-lei.py` corrigido em 08-18: corrupção silenciosa por heurística que não previa o caso novo).** `variantes()` calculava o separador de milhar sobre a string inteira do artigo, inclusive o sufixo de letra: pedir o recorte de `1035-A` produzia `103.5-A` em vez de `1.035-A`, e o artigo não era encontrado. Não aparecera antes porque os únicos artigos com sufixo de letra já recortados (104-A, 121-A) têm 3 dígitos, abaixo do limiar de separador de milhar. Corrigido para separar o sufixo antes do cálculo e recolocá-lo depois; comportamento inalterado para todo recorte já existente. Ao usar o script corrigido para `cpc-art-1035-A.md`, o corte automático pelo fim ("próximo artigo numérico") varreu as alterações fragmentárias seguintes da mesma lei (arts. 927, 932...) para dentro do recorte — cortado manualmente; o arquivo final não foi mantido porque duplicava a página já `vigente` (`jurisprudencia/cpc-art-1035a.md`, ingerida em 08-18) — ver nota abaixo.

**Reorganização — `lei-15484-2026-relevancia-resp.{html,md}` movido de `recurso-especial/raw/` para `raw/` (transversal), sem sufixo `-resp`.** Ao depositar a ER-55 acima, ficou claro que a Lei 15.484/2026 — já ingerida em 08-15/18 — se encaixa no mesmo critério que já vale para `ristj-er53` e `cpc-l13105-compilada`: altera CPC transversal (927, 932, 979, 988, 998, 1.030, 1.039, 1.042), não é exclusiva do REsp. Conteúdo do `.md` inalterado; só o caminho mudou. As duas páginas que citavam o depósito antigo (`jurisprudencia/cpc-art-1035a.md` e `.../lei-15484-2026-alteracoes-cpc.md`) tiveram o campo `raw:` atualizado para `/raw/lei-15484-2026-relevancia.md`. Depositado também `raw/lei-15484-2026-relevancia.pdf` (PDF oficial do DOU, baixado nesta rodada) como artefato de referência, sem substituir o `.md` canônico — mesmo critério do `cpc-l13105-compilada-2026-08-01.pdf`.

## 2026-08-18

**Lei 15.484/2026 absorvida no fluxo do REsp** — resolvidas as pendências (a), (b) e (c) de 08-15:
- (a) Páginas literais novas a partir do depósito da lei: `cpc-art-1035a` (texto integral do artigo + regra de transição do art. 4º; espaços do "*caput*" normalizados com declaração, conforme nota de fonte de 08-15) e `lei-15484-2026-alteracoes-cpc` (trechos NR literais de 927 III-A, 932 IV-b/V-b, 979 §3º, 988 V/§§4º-5º, 998 p.ú., 1.030 I-c/II/V-a, 1.039 p.ú., 1.042 caput/§2º, art. 5º — cada um com o efeito no fluxo). `cpc-art-1030` ganhou seção de alteração (o literal antigo permanece, com aviso de que o compilado transversal não reflete a lei). `cf-art-105-iii` ganhou seção sobre os §§2º-3º (EC 125/2022) em **paráfrase deliberada** — o literal constitucional não está depositado no bundle e a regra pós-caso-AREsp proíbe transcrever de memória.
- (b) Fluxo atualizado: playbook agora tem **9 portões** (novo portão 9: relevância — presunções, tema já decidido muda a rota) e **9 itens na estrutura da peça** (novo item 3: tópico de relevância após o resumo 343-A — atenção: itens 4-9 renumerados; sem remissões numéricas externas quebradas, conferido por grep); erro novo em "Erros a evitar" (omitir o tópico / AREsp contra inadmissão por relevância); workflow com relevância no parecer de viabilidade (Etapa 1), na sequência de redação (Etapa 3) e como portão 3 da validação (Etapa 4, itens seguintes renumerados 4-7).
- (c) Mapa de rotas: grupo do AgInt agora inclui o 1.030, I, c (relevância negada/conformidade — novo 1.042 bloqueia o AREsp); armadilhas novas — 1.039 p.ú. (sobrestados automaticamente inadmitidos quando negada a relevância no afetado: monitorar o TEMA, não a intimação) e irrecorribilidade do não conhecimento por irrelevância (1.035-A caput). Nota de vigilância na página das alterações: convivência da reclamação do 988, V com a Rcl 36.476/SP fica para a emenda regimental.
- **Método de redação do tópico conectado:** encontrado na raiz de `direito/pecas/` o documento solto "Relevância da Questão Federal no Recurso Especial — Modelo Mental, Método e Estrutura para LLM" (817 linhas: relevância ≠ mérito; fórmula; estrutura de capítulo em 7 seções; heurística QRETI; algoritmo operacional). Referenciado no item 3 da estrutura do playbook, no lugar em que a peça o exige. Está fora do bundle, sem frontmatter e sem indexação — **promoção formal (playbook do bundle + kebab-case + frontmatter) é decisão da titular**.
- **Pendências que ficam:** (d) emenda regimental do STJ (art. 6º da lei) — acompanhar; depósito do literal da CF 105 §§2º-3º (EC 125/2022) para destravar transcrição em peça (Planalto inacessível do sandbox); revisar o fluxo do AREsp (bundle `agravo-em-resp`) frente ao novo 1.042 §2º — fora do escopo desta entrada; triagem do documento de relevância da raiz (promover ao bundle ou manter solto).

**Reconversão do manual REsp Perfeito + colheita dos capítulos restantes (bundle recurso-especial)** — o `.md` do manual (convertido em 06/07, fora do git por regra 6.6) não existia mais ao lado do PDF; reconvertido com o pdfmd atual (278/278 p., manifesto auditável, 306 assets, sidecar **aprovado score 90**; único aviso: `ocr_low_confidence` na p. 1, resolvido por conferência visual — é a capa, arte gráfica sem conteúdo). Aprendizado operacional: o modo `--strict` bloqueia a escrita com aviso pendente — conferir a página indicada e reconverter sem `--strict` deixa o aviso documentado no manifesto. Higiene: pasta órfã de staging removida; `.gitignore` ganhou `manual_resp_perfeito_assets/` (o padrão `manual_resp_perfeito.*` não cobria o diretório de imagens da obra).

**Capítulos do manual sem correspondência no bundle, agora colhidos** (caps. 4, 10, 20-22, 24-25, 27-32, 39 — os caps. 26/33/37/38 já viviam nos fluxos de AgInt/AREsp/EDcl desde 07-08):
- Páginas de legislação novas: `cpc-art-942` (ampliação do colegiado — rejulga TUDO, vício é error in procedendo que exige EDcl antes do REsp; recorte literal no raw/), `cpc-art-1032` (fungibilidade só para questão exclusivamente constitucional mal rotulada — nunca REsp misto), `cpc-arts-1043-1044` (EDv), `sumula-5-stj` (irmã contratual da Súmula 7).
- Heurísticas novas: `dissidio-cotejo-e-paradigmas` (3 fases, rol de paradigmas vedados, 4 vias de prova, prejudicialidade a×c), `quantum-e-honorarios-excecao-sumula-7` (método bifásico do REsp 1.152.541; aritmética do art. 85 §2º na peça; alínea c nunca serve para valor), `preclusao-consumativa-e-unirrecorribilidade` (protocolo é ato único; AgInt-espelho), `efeito-suspensivo-a-quem-pedir` (3 fases do 1.029 §5º + teratologia antes da admissibilidade).
- Playbooks novos: `playbook-embargos-de-divergencia` (portões, Súmulas 158/168/315/316/420, competência interna, interrupção do RE — 1.044 §1º) e `atuacao-no-stj-pos-protocolo` (contrarrazões sem pedido de reforma + prequestionamento do recorrido; despacho; memoriais; sustentação oral RISTJ 158-160).
- Complementos: `sumula-456-stf` (limites do direito à espécie — RISTJ 255 §5º, fatos novos/CPC 493, cassação × julgamento), `sumula-7-stj` (remissões às exceções), playbook do REsp (6 erros novos a evitar) e mapa de rotas (seção pós-julgamento → EDv).

**Ressalva de fonte:** jurisprudência do manual (2018–2021) transcrita via OCR ~90% — toda página nova carrega o aviso de conferir inteiro teor antes de citar (portão de voz); grafia divergente "arts. 884/944 × 844/994 do CC" no modelo de quantum sinalizada na heurística. **Pendência que segue de 08-15:** absorver a Lei 15.484/2026 no fluxo (tópico de relevância obrigatório a partir de 03/09/2026) — os textos novos não a antecipam.

**Ingestão — Lei 15.484/2026 (regime de relevância do REsp)** — depositada em `recurso-especial/raw/` (`lei-15484-2026-relevancia-resp`, HTML oficial do DOU/Imprensa Nacional, UTF-8, sem `<strike>`). A lei regulamenta o art. 105, § 2º, da CF: cria o **art. 1.035-A do CPC** (não conhecimento do REsp sem relevância da questão federal; **tópico específico e fundamentado obrigatório na petição, sob pena de inadmissão — § 2º/§ 3º**; presunções do art. 105, § 3º, da CF; rejeição só por 2/3 do órgão julgador; suspensão nacional de processos por 6+6 meses) e altera **927 (III-A), 932 (IV/V, b), 979 (§ 3º), 988 (V, §§ 4º-5º), 998 (p.u.), 1.030 (I, c; II; V, a), 1.039 (p.u.) e 1.042 (caput e § 2º)**. **Vigência: 3 de setembro de 2026** (art. 7º, vacatio de 30 dias; contagem LC 95, art. 8º, § 1º); pelo art. 4º, o tópico de relevância só é exigível em recurso contra **acórdão publicado após a vigência**. Art. 6º delega ao RISTJ a regulamentação — **acompanhar emenda regimental** (compõe com o 343-A já ingerido).

**Bug corrigido no `depositar-lei.py` (corrupção silenciosa, a mesma classe que o script existe para impedir):** a lista `ACENTUADAS` da detecção de encoding continha `"artigo"` e `"penhora"` — palavras **sem acento** —, então o `latin-1` (que decodifica qualquer byte sem erro) vencia em arquivo UTF-8 que mencionasse "artigo", e o primeiro depósito desta lei saiu em mojibake (`relevÃ¢ncia`). A lista agora só tem palavras acentuadas; HTML do Planalto (cp1252) continua vencendo na primeira tentativa, e o UTF-8 do DOU cai corretamente na terceira. Redepositado limpo (`fonte=utf-8`, resíduo nenhum). Regra que fica: **fonte do DOU/Imprensa Nacional é UTF-8; a do Planalto é cp1252** — a detecção agora distingue as duas.

**Nota de fonte para páginas derivadas:** o HTML do DOU cola o itálico sem espaços (`o<em>caput</em>deste`), então o raw traz `ocaputdeste` (§ 1º) e `docaput` (§ 6º) no art. 1.035-A — fiel à fonte; quem transcrever deve declarar a normalização dos espaços.

**Pendências novas:** (a) página literal do art. 1.035-A (+ recortes das alterações em 927/932/979/988/998/1.030/1.039/1.042) — o CPC compilado transversal (`raw/cpc-l13105-compilada`) **não reflete** a Lei 15.484; (b) revisar o fluxo do REsp (playbook/checklist/workflow): o tópico de relevância vira item obrigatório da peça a partir de 03/09/2026, ao lado do resumo do RISTJ 343-A; (c) o mapa de rotas pós-inadmissão precisa absorver o novo 1.042 (inadmissão fundada em relevância não comporta agravo) e o 1.030, I, c; (d) acompanhar a emenda regimental do STJ (art. 6º).

## 2026-08-02 (segunda entrada)

**Ingestão** — Depositados dois códigos/leis transversais, via `depositar-lei.py`: o **Código Civil** (`cc-l10406-2002-compilada`, cobertura até a Lei 15.068, 2.046 artigos) e a **Lei 9.099/1995** (`lei-9099-1995-juizados`, cobertura até a Lei 14.245, 13 trechos revogados marcados). Ambos aqui porque servem a dois ou mais bundles — o CC é citado por cambial, execução/credor e imobiliário; a Lei 9.099 por execução/credor e audiências.

**Ferramenta nova: `depositar-lei.py`** na raiz do acervo. Faz a Etapa 0 de texto de lei e recusa o depósito quando não consegue decidir o encoding. Encapsula as duas armadilhas que já corromperam depósito aqui: HTML do Planalto é `cp1252`, e a redação superada vem em `<strike>` e precisa sair rotulada.

**Dois bugs corrigidos no `recortar-artigo.py`, ambos silenciosos:**

1. **Separador de milhar.** O padrão não reconhecia `Art. 1.003.` — ou seja, **nenhum artigo acima de 999 podia ser recortado**, o que incluía todos os artigos de recurso deste bundle (1.003, 1.009, 1.022, 1.030, 1.036-1.041). O mesmo defeito fazia o contador de artigos do depositador ler "Art. 1.911" como artigo 1, e foi o que me levou a suspeitar erradamente que o CC estivesse truncado.
2. **Ordinal e travessão.** Artigos de 1 a 9 se escrevem `Art. 9º`, e leis mais antigas usam `Art. 40 - `. O padrão exigia ponto, então falhava nos dois casos. Agora aceita ponto, ordinal e travessão, mantendo o `A` maiúsculo como discriminador contra remissões em minúsculo.

Regressão exercitada nas três formas de cabeçalho e nos artigos que já funcionavam.

## 2026-08-01

**Schema** — O CPC compilado deixou de morar dentro de `recurso-especial/raw/` e passou a ser **fonte transversal do acervo**, em `raw/` na raiz deste bundle. Motivo: 14 páginas de quatro fluxos diferentes já o citavam, e os bundles de execução passaram a precisar dele. O campo `raw:` das 14 páginas foi corrigido de `/recurso-especial/raw/...` para `/raw/...`. *(Entradas anteriores deste log citam o caminho antigo — registro histórico, não corrigido.)*

Gerada a conversão em texto (`cpc-l13105-compilada.md`) a partir do HTML, que é `cp1252`. É a fonte que o `recortar-artigo.py` lê para produzir recortes por artigo nos bundles consumidores.

**Conferência de atualidade e de qualidade, na mesma data.** A titular forneceu o PDF oficial do Planalto impresso em 2026-08-01. Ele foi convertido com o `pdfmd` e comparado ao depósito **artigo por artigo**: 994 artigos nas duas fontes, 35 divergências, **nenhuma de direito**. Duas conclusões:

1. **O depósito está atual.** Incorpora alterações até a **Lei nº 15.109, de 2025** (art. 82). A **Lei nº 15.479, de 2026** consta apenas como "Vide" na capa do PDF, sem nota de alteração em artigo algum.
2. **A conversão do PDF foi rejeitada** e não entrou no acervo. Ela truncava o art. 525 de 4.082 para 479 caracteres — perdendo o rol do § 1º —, deslocava parágrafos para artigos alheios (93, 529, 662, 913), apagava alíneas em 12 artigos e colava palavras hifenizadas em 16 (`salariosminimos`, `observandose`). O PDF ficou depositado como artefato oficial, **sem par `.md`**, com o aviso no [catálogo](raw/index.md). **Regra que fica: para texto de lei, a fonte é o HTML do Planalto, não o PDF.**

O `recortar-artigo.py` foi endurecido no mesmo movimento: o cabeçalho de artigo passou a ser reconhecido por `Art. N.` com maiúscula e ponto — o que distingue o artigo das remissões em minúsculo e funciona mesmo quando a conversão cola o cabeçalho do capítulo na mesma linha.


## 2026-07-16 (dissolução dos rótulos meta-textuais + fluxo novo: Réplica, v0.5.0)

- **Heurística `estrutura-ai-first` revisada (regras 1, 3 e 4 reescritas)** — decisão do titular, disparada por leitura humana de uma réplica real (caso real, fora deste bundle) que "parecia escrita por IA". Rótulos meta-textuais visíveis ("Caso em exame.", "Conclusão do capítulo:", "Fundamento impugnado (transcrição literal):", "Impugnação:", "Jurisprudência pertinente (transcrições):") deixam de ser prescrição e passam a ser o próprio sinal de escrita por IA que a heurística existia para evitar em outra camada. A estrutura (BLUF, título-tese, transcrição+fonte adjacente, seções autossuficientes) permanece — só que dissolvida em prosa, sem anúncio. Tabela de equivalência rótulo→prosa incluída na heurística. Propagado às referências em `agravo-em-resp/workflows`, `apelacao/workflows`, `embargos-declaracao/playbooks` e `workflows` (estes últimos tinham estrutura própria de rótulos fixos por vício, também dissolvida) e ao `pecas/index.md`. `recurso-especial/` e `agravo-interno/` conferidos — sem menção a rótulos fixos, nada a corrigir. Coerente com a skill do escritório `humanizer-forense`, revisada no mesmo sentido em `skills/` do workspace na mesma data.
- **Fluxo novo: Réplica** — sai do estoque (fluxo próprio não construído desde 2026-07-08) para fluxo completo. Fontes: Scarpinella 2024 §9.1–9.2 (linhas ~8140–8170 do raw, providências preliminares dos arts. 347–353) e §9.4.5 sobre impugnação documental (arts. 436–437); CPC compilado (arts. 329, 337, 344, 348–352, 436–437) conferido letra por letra contra `recurso-especial/raw/cpc-l13105-compilada.html`. Entregues: playbook (portão de cabimento — só há réplica útil diante de preliminar do 337, fato novo do 350 ou documento novo do 437; regra de ouro contra inovar causa de pedir, ancorada no art. 329, II — aditamento após a citação exige consentimento do réu, que a réplica não tem como obter; estrutura por tipo de resposta), heurística `tabela-alegacoes-resposta` (portão de redação: cada preliminar/fato novo/documento da contestação → réplica → item da tabela, espelho da tabela de fundamentos do AREsp e da tabela de capítulos da apelação); workflow (rota e prazo → mapa de alegações → composição com matéria → redação → validação → entrega); páginas literais `cpc-art-337`, `cpc-arts-350-352`, `cpc-arts-436-437`.

## 2026-07-13 (banca revisora, v0.4.2)

- **Skill nova do escritório `banca-revisora` + primeira execução real (AREsp)** — decisão do titular: peças de tribunal superior passam por banca simulada antes do protocolo. Desenho: 5 assentos com ISOLAMENTO DE CONTEXTO (assessor às cegas; adversário só com o material da parte contrária; relator com equities; processualista = legal-consistency-validator orquestrada; estrategista com tudo + objetivo real), revisão cruzada anônima, portão de evidência (achado sem trecho+fonte = descartado), parecer CONFIRMADO/PLAUSÍVEL com laço de retroalimentação obrigatório. Integrada como item condicional na Etapa 4 dos 5 workflows. A skill `conselheiros` (LLM Council genérico) foi renomeada para SKILL.md (não era descoberta) e reposicionada para decisões ESTRATÉGICAS de litígio.
- **Resultado da 1ª banca (4 CONFIRMADOS, todos corrigidos):** (C1, o mais grave) reescrita de desrobotização converteu concessão condicional do REsp em admissão afirmativa de motivação de blindagem — "mudança de modalidade é mudança de mérito" virou o invariante nº 6 da humanizer-forense; (C2) faltava pedido subsidiário de provimento parcial por capítulo — item 10 novo no checklist do playbook AREsp; (C3) tese construída sobre citação seletiva de ementa (item 6 sem os vizinhos 3 e 7) — regra anti-citação-seletiva nova na heurística tabela-fundamentos; (C4) elemento citado na síntese sem destino em capítulo (multa) — item 11 novo no checklist. Evidência do desenho: o defeito mais grave foi introduzido por uma etapa de melhoria anterior (desrobotização) e só a lente estratégica o viu — nenhum lint ou revisão single-lens o teria pego.
- **Pendência nova:** página literal do `cpc-art-1030` no bundle do REsp (recomendação do assento processualista — hoje a conferência do inciso V se apoia em nota derivada).

## 2026-07-09 (tarde — desrobotização, v0.4.1)

- **Camada de desrobotização nos 5 workflows** — decisão do titular: peças não podem ter "cara de IA" na superfície, mantendo a estrutura AI-first. Skill nova do escritório `humanizer-forense` (fork forense da humanizer, base Wikipedia "Signs of AI writing"): tabela de substituições pt-BR forense (travessões, paralelismos negativos, perguntas retóricas, frases-clone, registro inflado), lista de falsos positivos do gênero (passiva, conectivos, "Primeiro./Segundo."), invariantes (transcrições, rótulos, citações) e lint quantitativo (`lint-ia.js`). Integrada como item de validação nos workflows de REsp, AREsp, AgInt, EDcl e apelação; heurística `estrutura-ai-first` ganhou a seção "camadas" (esqueleto × superfície). Primeira aplicação real (AREsp): travessões 52→3, "e não" contrastivo 3→1, perguntas retóricas 7→0, frases-clone 0, sem alteração de conteúdo jurídico.

## 2026-07-09 (regimento consolidado + ferramenta)

- **Lint de vigência: Regimento do STJ consolidado (30/06/2026) ingerido e conferido** — novo raw `Regimento_interno_atualizado_30062026.pdf` (454 p., Etapa 0 **aprovado score 75**, mesmas penalidades de artefatos do anterior). Conferência dos 5 pontos que o bundle deriva: **arts. 253, 255, 258, 259 e 343-A idênticos às páginas** (343-A com nota "Incluído pela Emenda 53" no corpo); **21-E §§2º/2º-A da Emenda 53 incorporados no corpo principal** (a descrição da página `ristj-arts-258-259` foi re-conferida contra o raw da própria Emenda 53 e está correta: relatoria do Presidente em sessão virtual da Seção; oposição → voto desconsiderado e redistribuição). **Nenhuma emenda posterior à 53** no consolidado. As 4 páginas derivadas agora apontam `raw:` para o consolidado, `verificado_em: 2026-07-09`. Atenção de leitura: o consolidado traz **anexo de versões históricas** — ocorrências duplicadas dos artigos adiante da linha ~5400 do .md são texto revogado. O raw anterior (`Regimento_interno_atualizado.*`) permanece como histórico; fonte canônica é o consolidado.
- **Bug de ferramenta (pendência de correção, causa raiz CONFIRMADA): a detecção "scanned PDF" do modo `--ocr auto` do pdfmd é não determinística** — o mesmo arquivo com camada de texto ora converte em segundos, ora é classificado como escaneado e escala para Tesseract (que falha/trava em livros de 700–1800 p.). Foi isso que derrubou todos os lotes do `ingest-prep.py` (que passa `--ocr auto`): montans/gediel 07-08, regimento novo 2× em 07-09, montans/gediel de novo em 07-09 (episódio final com "Using Tesseract OCR" nos dois, capturado no output). **Contorno validado: converter sem `--ocr auto`** quando o PDF tem camada de texto (conferível via PyMuPDF `get_text()` numa página do miolo) — montans (1.788 p.) e gediel (759 p.) converteram em segundos e pontuaram **aprovado 100**; sidecars gerados pela `score_markdown` do próprio script, com `modo_ocr` e nota fiéis. Correção do pdfmd a fazer (engine em `D:\GITHUB\pdfmd`): investigar a amostragem da detecção auto; no `ingest-prep.py`: tentar modo sem OCR antes do auto e capturar stderr no sidecar; sincronizar com a cópia do bundle piloto.
- **Etapa 0 dos 4 livros CONCLUÍDA — 4/4 aprovados score 100** (resolve as pendências (a) e (b) de 07-08): `iuris-dpc-vol4-2025` (530 p.), `manual-dpc-scarpinella-2024` (1.586 p.), `manual-dpc-montans-2024` (1.788 p. — não era PDF protegido, era o bug acima), `pratica-processo-civil-gediel-2016` (759 p.). Todos com `--page-breaks`; os dois últimos sem OCR (texto nativo).

## 2026-07-09 (continuação — bundle v0.4.0)

- **Fluxo novo: Embargos de Declaração** — fontes: manual REsp Perfeito cap. 37 (linhas 6240–6784 do raw), IURIS §8.6 (~9316–9339), Scarpinella §7 e §7.7 (~17946–18061). Entregues: playbook pelos **dois papéis** (corretivo × prequestionador/Súmula 98) com anatomia operacional dos 4 vícios (contradição é interna — EREsp 40.468; precedente externo não é vício — EDcl no AgRg no HC 548.222), o **prequestionador eficaz em 4 elementos** (suscitação+folha / silêncio / dispositivo / inciso), regime de interrupção (sem indicação de vício = sem interrupção), conversão em AgInt (1.024 §3º), complementação de razões (§4º) e multa; workflow com gatilho de reabertura de prazo em C1; heurística `tabela-vicios-prequestionamento` (portão omissão × inovação); página `cpc-arts-1023-1026` literal. **Armadilha de prazo penal destacada: EDcl = 2 DIAS (CPP 619)** — espelho das armadilhas do AgInt (5 dias) e do AREsp (corridos).
- **Fluxo novo: Apelação** — fontes: Scarpinella §4 (~17698–17810), IURIS (princípios/preparo/efeitos ~8556–8864). Entregues: playbook das **três cargas** (interlocutórias não agraváveis do 1.009 §1º — preclusão definitiva se caladas; *error in procedendo* → nulidade; *in judicando* → reforma; confusão = 932 III), devolutividade estratégica (profundidade §§1º–2º como arma de contrarrazões; causa madura §3º como DEVER — posição expressa na peça), efeito suspensivo e exceções do 1.012 §1º (decisão no dia da intimação), estrutura canônica PMA (Síntese→Cabimento→Preliminares→Mérito→Pedidos, integrada à skill local `apelacao-cirurgica` e à heurística AI-first); workflow com inventário como parecer ao titular; heurística `tabela-capitulos-interlocutorias` (duas partes: capítulos da sentença + varredura completa de interlocutórias); páginas `cpc-arts-1009-1010` e `cpc-arts-1012-1014` literais.
- Estoques restantes na fila: agravo de instrumento, petição inicial, contestação, réplica (ordem: decisão do titular).

## 2026-07-09

- **Primeira execução real do fluxo AREsp (v0.3.0 → v0.3.1)** — o playbook/workflow do AREsp foi executado de ponta a ponta em caso real (inadmissão TJTO por Súmulas 7 e 83, art. 1.030, V; rota única AREsp confirmada pelo mapa de rotas). Duas falhas de execução detectadas e convertidas em portões: (a) **citação de norma a partir de resumo** — alínea da autuação como REsp citada errada ("c" em vez de "d" do RISTJ 253, p.u., II); playbook agora destaca a alínea e o checklist ganhou o item de conferência letra por letra; (b) **peça do caso não lida integralmente** (petição de EDcl inferida em vez de lida) — Etapa 1 do workflow ganhou portão de leitura integral obrigatória. Terceira lição (de revisão externa independente): **remissões cruzadas quebram em renumeração** — item novo no checklist (nº 8) e na Etapa 4 do workflow.
- **Heurística transversal nova: [heuristicas/estrutura-ai-first.md](heuristicas/estrutura-ai-first.md)** — estrutura de peça para leitura primária por IA de triagem (síntese padrão ementa CNJ/STJ cumprindo o RISTJ 343-A, títulos-conclusão, BLUF por capítulo, rótulos fixos, jurisprudência transcrita com fonte adjacente, seções autossuficientes). Decisão do titular de 2026-07-08. Playbook do AREsp atualizado: estrutura da peça agora inclui o resumo do 343-A como item 2 (o playbook referenciava o 343-A só no fluxo do REsp — corrigido o vão para o AREsp) e checklist estendido (itens 7–9).
- **Validação de jurisprudência na fonte**: AREsp 2.425.931/SP confirmado (Rel. Min. João Otávio de Noronha, 4ª T., j. 15/04/2024, DJe 18/04/2024); REsp 1.960.026/SP confirmado em substância, mas a data circulante "DJe 11/10/2022" é a de **julgamento** (armadilha registrada na heurística). SCON bloqueado por Cloudflare para automação — verificação automatizada de julgados permanece pendência (skill futura).

## 2026-07-08

- **Ingestão** — **4 livros de processo civil para `raw/` da raiz** (obras comerciais de terceiros, regra 6.6: uso interno, conhecimento reescrito, obra não distribuível). Etapa 0: `iuris-dpc-vol4-2025.pdf` (530 p., **score 100, aprovado**), `manual-dpc-scarpinella-2024.pdf` (1.586 p., **score 100, aprovado**), `manual-dpc-montans-2024.pdf` (1.788 p., **REPROVADO — conversão falhou em todos os modos de OCR**; suspeita de PDF protegido — pendência de revisão humana, .md não gerado, não lido), `pratica-processo-civil-gediel-2016.pdf` (em conversão ao fechar esta entrada — sidecar pendente; conferir antes de usar).
- **Fluxo novo: AREsp (bundle v0.3.0)** — decisão do titular de 2026-07-08 destrava a construção. Fontes: manual REsp Perfeito cap. 33 (linhas 5950–6240 do raw), IURIS vol. 4 §§8.7.5–8.7.7 (linhas ~9540–9615), RISTJ 253, páginas existentes. Entregues: playbook (portões; autópsia da inadmissão com tabela óbice→resposta técnica; incindibilidade/EAREsp 746.775; preclusão consumativa/AgInt no AREsp 1.581.737; divergência sobre sustentação oral no §5º; checklist anti-182), heurística `tabela-fundamentos-inadmissao` (portão de redação, espelho da anti-283) e workflow (rota e prazo no dia da intimação → autópsia → composição com matéria → redação → validação → entrega).
- **Fluxo novo: Agravo Interno (bundle v0.3.0)** — fontes: manual caps. 26/38 (linhas 1266–1310 e 6785–7176 do raw), IURIS §8.5 (linhas ~9291–9315), RISTJ 258-259/21-E. Entregues: playbook organizado pelos **três papéis** (esgotamento/Súmula 281 + Tema 434; distinguishing do 1.030 §2º + Rcl 36.476; monocrática no STJ/Súmula 568) com regime da multa (não automática — AgInt no AREsp 1.411.025; atraída por falta de impugnação específica — AgInt nos EAREsp 802.877), impugnação parcial admitida (AgInt nos EREsp 1.424.404 — contraste com AREsp), vedação *per relationem* e exceção, sustentação oral do 937 §3º; e workflow. **Armadilha de prazo penal (5 dias, RISTJ 258) destacada em playbook, workflow e index.**
- **Estoques novos (6 peças)** — `apelacao/`, `agravo-de-instrumento/`, `embargos-declaracao/`, `peticao-inicial/`, `contestacao/`, `replica/`: cada um com "essencial em 5 linhas" (CPC, granularidade máxima) e fontes mapeadas com localização nos raws aprovados (Scarpinella: iniciais ~7382, contestação ~7641, apelação ~17698, AI ~17811, EDcl ~17946; manual REsp cap. 37 ~6240–6784 para EDcl). Prioridade de construção dos fluxos: decisão do titular.
- **Pendências novas:** ~~(a) Montans reprovado~~ e ~~(b) sidecar do Gediel~~ — **resolvidos (2026-07-09): 4/4 aprovados score 100 (era o bug do --ocr auto, ver entrada de 09/07)**; (c) fluxos das 6 peças em estoque — ordem a definir pelo titular; (d) Tema 988/STJ (taxatividade mitigada do AI) — criar página com texto literal da tese ao construir o fluxo do AI; (e) divergência STJ sobre sustentação oral no AREsp (§5º do 1.042) — acompanhar; jurisprudência dos playbooks novos citada do manual/IURIS (2016–2024) → revalidar no lint mensal.

## 2026-07-07

- **Lint** — **Vigência das súmulas STJ conferida contra fonte oficial** (bundle v0.2.0): baixada a compilação oficial `SumulasSTJ.pdf` (stj.jus.br/docs_internet, Etapa 0 score 100) para `raw/`; as **16 súmulas STJ** do bundle conferidas enunciado a enunciado — 16/16 corretas (418 confirmada CANCELADA pela Corte Especial em 01/07/2016, anotação oficial incorporada à página; 320 vigente na compilação mas superada pelo CPC 941 §3º, status mantido com justificativa). `resource` das súmulas STJ agora aponta o PDF oficial (deep link canônico resolvido); `verificado_em: 2026-07-07`. STF: deep link por súmula indisponível (portal reorganizado; SCON bot-blocked) — `resource` mantido na página-índice viva; conferência literal STF permanece pendência de lint.
- **Superação detectada** — o arquivo depositado como "resolucao_STJ_1" contém na verdade a **Resolução STJ/GP n. 2/2017**, que revogou as res. anteriores (1/2014, 1/2016) citadas pelo manual-fonte. Arquivos renomeados em raw/ (`resolucao_STJ_GP_2_2017.*`), página derivada criada com nota de vigência, e as 3 referências no bundle corrigidas.
- **Ingestão** — Derivados do Regimento (444 p.): `ristj-art-255` (REsp no STJ: dissídio §1º, repositórios §3º c/ Emenda 49/2026, poderes do relator §4º, preliminar de cabimento §5º), `ristj-art-253` (AREsp no STJ → agravo-em-resp), `ristj-arts-258-259` (→ agravo-interno; **achado prático: agravo regimental em matéria penal no STJ tem prazo de 5 DIAS**, não 15). `res-stj-gp-2-2017` (custas/porte: GRU Cobrança exclusiva, campos obrigatórios, isenções, prorrogação por indisponibilidade >60min).
- **Pendências remanescentes:** conferência literal das súmulas STF contra fonte oficial; ato regulamentar da Presidência do STJ que detalhará o art. 343-A; jurisprudência do manual (2018–2021) citada nas seções de aplicação — revalidar no lint mensal.

## 2026-07-06

- **Ingestão** — Fundação do bundle (D12: primeira ingestão de conhecimento de peça puro). Fontes na Etapa 0 (todas aprovadas): `manual_resp_perfeito.pdf` (278 p., score 100 — obra comercial de terceiro, regra 6.6 do schema aplicada: conhecimento reescrito, obra não distribuível), `EMENDA_REGIMENTAL_53_30_junho_2026.pdf` (5 p., score 100), `Regimento_interno_atualizado.pdf` (444 p., score 75, penalidade muitos_artefatos), `resolucao_STJ_1.pdf` (6 p., score 100), + CPC compilado capturado do Planalto (HTML em `raw/`). Estrutura aprovada pelo titular: pastas por peça; só REsp com fluxo executável; AREsp/AgInt nascem como estoque de conhecimento; menções cruzadas viram mapa de rotas pós-inadmissão.
- **Achado de vigência** — O manual (jurisprudência 2018–2021) **não conhece** a Emenda Regimental 53 (30/06/2026): novo art. 343-A do RISTJ exige resumo dos fundamentos/pedidos/decisões/dispositivos em toda petição recursal ao STJ. Incorporado ao playbook.
- **Pendências de ingestão:** derivar do Regimento (444 p.) os artigos pertinentes (255–257-F, 21-E, 343-A consolidado); Resolução STJ 1/2014 (porte de remessa); deep links oficiais das súmulas; jurisprudência do manual com `verificado_em` vazio → lint deve checar vigência (2018–2021 → hoje).
