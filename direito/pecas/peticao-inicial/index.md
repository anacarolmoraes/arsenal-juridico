# Petição Inicial — fluxo completo

**Fluxo de criação próprio construído em 2026-09-04** (fontes: CPC compilado, CDC e Lei 9.099 em `raw/`; técnica extraída do encadeamento canônico do `legal-writer` e dos playbooks de inicial dos bundles bancário e imobiliário, que agora apontam para cá). O pipeline do workspace (`legal-orchestrator`: `ANALISE.md` → `<PECA>.estrutura.md` aprovada → redação → validação → compilação) executa; este bundle é a técnica que o orienta.

## O essencial em 5 linhas

Requisitos do CPC 319 (juízo, qualificação completa, fatos e fundamentos, pedido com especificações, valor da causa, provas, opção pela audiência de conciliação — inciso VII) + documentos indispensáveis (320). Pedido certo e determinado (322/324; interpretação pelo conjunto da postulação, 322 §2º), cumulação nos moldes do 327. Valor da causa segue o 292 (soma dos pedidos — e a inconsistência numérica é o erro mais atacável). Faltando requisito sanável: **emenda em 15 dias com indicação precisa do que corrigir** (321) antes de indeferir (330); improcedência liminar nas hipóteses do 332 (retratação em 5 dias, §3º). Desinteresse na autocomposição declara-se na inicial (319, VII c/c 334, §5º).

## Fluxo

- **Playbook:** [playbooks/playbook-peticao-inicial.md](playbooks/playbook-peticao-inicial.md) — portões, decisões de abertura, esqueleto único com cinco variáveis, mapa probatório na peça, ataques previstos, checklist
- **Workflow:** [workflows/peticao-inicial.md](workflows/peticao-inicial.md) — etapas executáveis espelhando os estágios do `legal-orchestrator`
- **Heurística:** [heuristicas/competencia-e-foro-na-inicial.md](heuristicas/competencia-e-foro-na-inicial.md) — quando escrever o capítulo de competência e o que a Lei 14.879/2024 exige de quem escolhe foro
- **Heurística:** [heuristicas/juizado-ou-vara-comum.md](heuristicas/juizado-ou-vara-comum.md) — a decisão de abertura: teto, perícia, custas, honorários, acesso ao STJ
- **Heurística:** [heuristicas/tutela-provisoria-na-inicial.md](heuristicas/tutela-provisoria-na-inicial.md) — urgência × evidência × antecedente, irreversibilidade e caução, posição do capítulo
- **Heurística:** [heuristicas/exibicao-de-documentos-a-partir-do-mapa-probatorio.md](heuristicas/exibicao-de-documentos-a-partir-do-mapa-probatorio.md) — fato "a produzir" com prova em poder do réu vira pedido do art. 397 na inicial
- **Heurística:** [heuristicas/emenda-da-inicial.md](heuristicas/emenda-da-inicial.md) — responder ao art. 321, atacar o indeferimento, e devolver a causa da emenda ao checklist
- **Heurística:** [heuristicas/juros-e-correcao-na-inicial.md](heuristicas/juros-e-correcao-na-inicial.md) — IPCA e taxa legal (Lei 14.905/2024), termo inicial pela natureza da responsabilidade (Súmulas 54, 43 e 362), regra do escritório de direito intertemporal
- **Heurística:** [heuristicas/quantificar-dano-moral-metodo-bifasico.md](heuristicas/quantificar-dano-moral-metodo-bifasico.md) — grupo de casos do tribunal competente + circunstâncias com prova; o valor pedido sai da conta e vai para o 292, V

## Páginas

- [jurisprudencia/resp-1152541-rs-metodo-bifasico.md](jurisprudencia/resp-1152541-rs-metodo-bifasico.md) — REsp 1.152.541/RS, Terceira Turma, 2011: as duas fases do arbitramento (ementa e voto, inteiro teor em `raw/`)
- [jurisprudencia/resp-1988687-rj-tema-1178-gratuidade.md](jurisprudencia/resp-1988687-rj-tema-1178-gratuidade.md) — Tema 1.178, Corte Especial, 2025: gratuidade da pessoa natural não se indefere de plano por critério objetivo (inteiro teor em `raw/`)
- [jurisprudencia/sumula-54-stj.md](jurisprudencia/sumula-54-stj.md) · [jurisprudencia/sumula-43-stj.md](jurisprudencia/sumula-43-stj.md) · [jurisprudencia/sumula-362-stj.md](jurisprudencia/sumula-362-stj.md) — termos iniciais de juros e correção
- [jurisprudencia/cc-arts-389-405-406.md](jurisprudencia/cc-arts-389-405-406.md) — IPCA, citação e taxa legal na redação da Lei 14.905/2024 (literal)

- [jurisprudencia/cpc-arts-319-321-330-331-334.md](jurisprudencia/cpc-arts-319-321-330-331-334.md) — requisitos, documentos, emenda, indeferimento e inépcia, apelação com retratação, opção pela autocomposição (literal)
- [jurisprudencia/cpc-arts-46-53-63.md](jurisprudencia/cpc-arts-46-53-63.md) — foro do réu, foros especiais, eleição de foro pós-Lei 14.879/2024 (literal)
- [jurisprudencia/cdc-art-101-i.md](jurisprudencia/cdc-art-101-i.md) — foro do domicílio do consumidor (literal)
- [jurisprudencia/cpc-arts-300-304-311.md](jurisprudencia/cpc-arts-300-304-311.md) — tutela de urgência, antecedente com estabilização, evidência (literal)
- [jurisprudencia/cpc-arts-396-400.md](jurisprudencia/cpc-arts-396-400.md) — exibição de documento em poder da parte, presunção de veracidade (literal)
- [jurisprudencia/lei-9099-arts-3-9-54-55.md](jurisprudencia/lei-9099-arts-3-9-54-55.md) — competência do Juizado, assistência, custas e honorários (literal)
- Composição com a matéria: [bancário, fraude em consignado](../../bancario/emprestimo-nao-realizado/playbooks/playbook-peticao-inicial-fraude-consignado.md) · [imobiliário, rescisão de lote](../../imobiliario/playbooks/playbook-peticao-inicial-rescisao-imovel.md)
- Cadeia: contestação → [réplica](../replica/index.md) → sentença → [apelação](../apelacao/index.md)

## Pendências (PRD `planos/2026-09-04_prd-fluxo-peticao-inicial.md` do workspace)

- **F3 concluída em 05/09/2026:** a titular depositou as três súmulas, o REsp 1.152.541/RS e o acórdão do Tema 1.178; páginas acima. Os PDFs individuais das súmulas reprovam no sidecar por serem tabelas de precedentes; as páginas apontam `raw:` para a compilação oficial já aprovada em `/recurso-especial/raw/`.
- **F4, dado próprio:** mineração dos despachos de emenda da fila do DJEN → contagem por causa no checklist abaixo; perfis de juízo das varas mais frequentes.

## Checklist de saída (Estágio 6 do `legal-orchestrator` aponta para cá)

Conferir na peça pronta, antes do `.docx`. Definição canônica (valor da causa, gratuidade, assinatura, endereçamento) mora em `perfil/definicoes.md` do workspace; aqui só o requisito legal e onde ele costuma falhar.

**Art. 319 — requisitos**

- [ ] I — Juízo a que é dirigida, no padrão do `definicoes.md` §5 (vara em branco se ainda não distribuída).
- [ ] II — Qualificação de autor e réu: nome, estado civil, existência de união estável, profissão, CPF/CNPJ, e-mail, domicílio e residência. Telefone não é requisito e o escritório não o inclui (§5). Réu sem dado completo: requerer as diligências do §1º, não deixar em branco.
- [ ] III — Fato e fundamentos jurídicos, cada fato ancorado no `Doc. N` que o prova (mapa probatório da `ANALISE.md`); fato "a produzir" não é afirmado como provado.
- [ ] IV — Pedido certo e determinado (322/324), um a um, com valor quando quantificável; cumulação conforme o 327. Juros, correção e honorários estão compreendidos no principal (322 §1º), mas pedi-los expressamente evita discussão.
- [ ] V — Valor da causa pelo 292, coerente com a soma dos pedidos e com a regra do `definicoes.md` §1. Divergência entre valor da causa e pedidos é o defeito mais atacado.
- [ ] VI — Provas: além do protesto genérico, o meio nomeado para cada fato "a produzir" (testemunha, perícia, exibição, ofício).
- [ ] VII — Opção pela audiência de conciliação ou mediação declarada (desinteresse só na inicial, 334 §5º).

**Art. 320 — documentos indispensáveis**

- [ ] Procuração, comprovante de residência, documento de identidade, contrato/instrumento da relação, comprovantes de pagamento, e o documento que prova cada fato do mapa probatório. Falta sanável gera emenda (321); é tempo perdido.
- [ ] Gratuidade: declaração e prova conforme `definicoes.md` §2 — e, para ação ajuizada depois da ata da ADC 80 (09/2026), a forma A ou B pela faixa de salário de R$ 5.000,00 ([heurística](../gratuidade/heuristicas/pedido-de-gratuidade-pos-adc-80.md)).

**Encargos**

- [ ] Correção monetária pelo IPCA (CC 389, p.ú.) e juros pela taxa legal (CC 406, com a redação da Lei 14.905/2024), salvo índice contratual válido. "Correção pela Selic" é erro comum de prompt genérico: a Selic é a base da taxa legal de juros, não índice de correção.
- [ ] Termo inicial dos juros conforme a natureza da responsabilidade (contratual: citação, CC 405; extracontratual: evento danoso, Súmula 54) e da correção (dano material: prejuízo, Súmula 43; dano moral: arbitramento, Súmula 362). Regra intertemporal da Lei 14.905/2024 em [juros e correção na inicial](heuristicas/juros-e-correcao-na-inicial.md).
- [ ] Dano moral com valor básico do grupo de casos e circunstâncias provadas ([método bifásico](heuristicas/quantificar-dano-moral-metodo-bifasico.md)); valor no 292, V.

**Tutela provisória, se pedida**

- [ ] Urgência (300) com o perigo concreto descrito, ou evidência (311) com a hipótese do inciso indicada. Citar o artigo sem descrever o fato é o que faz o pedido ser indeferido de plano.

**Requerimentos finais e forma**

- [ ] Citação do réu; intimações em nome exclusivo da advogada subscritora (272 §5º); Juízo 100% Digital se a comarca oferecer.
- [ ] Capítulo I "DA SÍNTESE DA LIDE" em BLUF; títulos-tese; sem rótulo meta-textual (`definicoes.md` §5; AGENTS.md §5).
- [ ] Assinatura conforme `definicoes.md` §4.
- [ ] Nenhum placeholder (`[VERIFICAR]`, `[NOME]`): o que falta volta como "falta saber" da estrutura, não vai para o texto.

## Fontes a explorar (restantes)

- Scarpinella 2024 (`/raw/manual-dpc-scarpinella-2024.md`, aprovado): caps. 2–3 do procedimento comum (linhas ~7382 e ~7491) + quadro (~7896) — para a F2 seguinte (pedido genérico, cumulação do 327, improcedência liminar do 332).
- Prática Gediel 2016 — conferir sidecar antes de usar.
