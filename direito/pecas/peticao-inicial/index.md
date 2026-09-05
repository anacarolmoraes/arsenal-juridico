# Petição Inicial — estoque de conhecimento

**Fluxo de criação próprio: não construído** (fila do log, 2026-07-08). Atenção: o escritório **já opera** iniciais reais pelo bundle temático (`direito/bancario/emprestimo-nao-realizado` — teste H1 aprovado) e pelo encadeamento canônico PMA da skill `legal-writer`. O fluxo transversal, quando construído, generaliza essa experiência para qualquer matéria.

## O essencial em 5 linhas

Requisitos do CPC 319 (juízo, qualificação completa, fatos e fundamentos, pedido com especificações, valor da causa, provas, opção pela audiência de conciliação — inciso VII) + documentos indispensáveis (320). Pedido certo e determinado (322/324; interpretação pelo conjunto da postulação, 322 §2º), cumulação nos moldes do 327. Valor da causa segue o 292 (soma dos pedidos — e a inconsistência numérica é o erro mais atacável). Faltando requisito sanável: **emenda em 15 dias com indicação precisa do que corrigir** (321) antes de indeferir (330); improcedência liminar nas hipóteses do 332 (retratação em 5 dias, §3º). Desinteresse na autocomposição declara-se na inicial (319, VII c/c 334, §5º).

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
- [ ] Gratuidade: declaração e prova conforme `definicoes.md` §2.

**Encargos**

- [ ] Correção monetária pelo IPCA (CC 389, p.ú.) e juros pela taxa legal (CC 406, com a redação da Lei 14.905/2024), salvo índice contratual válido. "Correção pela Selic" é erro comum de prompt genérico: a Selic é a base da taxa legal de juros, não índice de correção.
- [ ] Termo inicial dos juros conforme a natureza da obrigação (contratual: mora; extracontratual: evento danoso — matéria de bundle temático, não deste checklist).

**Tutela provisória, se pedida**

- [ ] Urgência (300) com o perigo concreto descrito, ou evidência (311) com a hipótese do inciso indicada. Citar o artigo sem descrever o fato é o que faz o pedido ser indeferido de plano.

**Requerimentos finais e forma**

- [ ] Citação do réu; intimações em nome exclusivo da advogada subscritora (272 §5º); Juízo 100% Digital se a comarca oferecer.
- [ ] Capítulo I "DA SÍNTESE DA LIDE" em BLUF; títulos-tese; sem rótulo meta-textual (`definicoes.md` §5; AGENTS.md §5).
- [ ] Assinatura conforme `definicoes.md` §4.
- [ ] Nenhum placeholder (`[VERIFICAR]`, `[NOME]`): o que falta volta como "falta saber" da estrutura, não vai para o texto.

## Fontes a explorar na construção do fluxo

- Scarpinella 2024 (`/raw/manual-dpc-scarpinella-2024.md`, aprovado): caps. 2–3 do procedimento comum (linhas ~7382 e ~7491) + quadro (~7896).
- Bundle piloto: playbooks e caso decidido de inicial real (composição peça × matéria já testada — H1).
- Skill `legal-writer` (encadeamento canônico PMA de inicial cível) — a técnica de peça generalizável migra para cá; o estilo fica na skill.
- Prática Gediel 2016 — conferir sidecar antes de usar.
