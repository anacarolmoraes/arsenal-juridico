# raw/ — fontes brutas imutáveis

Depósito de fonte: nada aqui se edita. Páginas derivadas apontam para cá.

## Versionado (circula para a equipe)

- [resp-2222059-sp.md](resp-2222059-sp.md) (+ `.pdf`) — inteiro teor oficial do REsp 2.222.059/SP (3ª Turma, Rel. Min. Ricardo Villas Bôas Cueva, j. 08/10/2025): responsabilidade de instituição de pagamento por operações fora do perfil de consumo. Página derivada em `jurisprudencia/`.
- [notas-jurisprudencia-stj-fraude-bancaria.md](notas-jurisprudencia-stj-fraude-bancaria.md) — nota de pesquisa (resumo do REsp 2.222.059, Súmula 479 e correlatos). Material de trabalho, **não é fonte** — citar sempre pelo inteiro teor.
- [notas-estrategicas-fraudes-bancarias.md](notas-estrategicas-fraudes-bancarias.md) — notas estratégicas do acervo antigo, texto gerado por IA com rodapés que não apontam para fonte nenhuma: **material de trabalho, não fonte**. Destilado em 20/10/2026: ato primário × secundário e nomenclatura → `heuristicas/ato-primario-e-ato-secundario.md`; relatório do DICT → `heuristicas/marcacao-de-fraude-no-dict-antes-do-pix.md`; Marco Civil para IP → `emprestimo-nao-realizado/jurisprudencia/lei-12965-2014-arts-10-13-15-22.md`; Res. 4.753 e monitoramento atípico já tinham página. Sem resíduo.
- `cadeia-golpea-*.md`, `cadeia-golpeb-*.md`, `cadeia-golpec-*.md` (+ `.quality.json`) — cadeias de litígio de terceiros, **anonimizadas em 28/07/2026** (regra dura 10): os `.md` circulam.
- [resp-2052228-df.md](resp-2052228-df.md) — inteiro teor oficial do REsp 2.052.228/DF (3ª Turma, Rel. Min. Nancy Andrighi, j. 12/09/2023, DJe 15/09/2023). **Pseudonimizado** em 15/10/2026 (recorrentes, advogados, nº do contrato); PDF não depositado.
- [apciv-1003610-tjsp-falso-advogado.md](apciv-1003610-tjsp-falso-advogado.md) — inteiro teor do TJSP, ApCiv 1003610-33.2025.8.26.0664 (16ª CDPriv., j. 13/11/2025), golpe do falso advogado. **Pseudonimizado** em 15/10/2026 (autor e beneficiário); PDF não depositado.
- [apciv-1017912-tjsp-conta-fraudulenta-kyc.md](apciv-1017912-tjsp-conta-fraudulenta-kyc.md) — inteiro teor do TJSP, ApCiv 1017912-17.2022.8.26.0068 (Núcleo 4.0 Turma IV, j. 18/02/2025), banco recebedor e KYC. **Pseudonimizado** em 15/10/2026; PDF não depositado.
- `resp-1995458-sp.md`, `resp-2015732-sp.md`, `resp-1875164-mg.md` — inteiros teores oficiais do STJ, **pseudonimizados** em 15/10/2026 (partes, advogados, OAB); PDFs não depositados.
- `apciv-1001051-tjsp.md`, `apciv-1001183-tjsp.md`, `apciv-1002595-tjsp.md`, `apciv-1003655-tjsp.md` — acórdãos do TJSP sobre falso advogado e acesso remoto, **pseudonimizados** em 15/10/2026; PDFs não depositados.

- [ri-0046473-tjpe-falso-advogado-recebedor-nubank.md](ri-0046473-tjpe-falso-advogado-recebedor-nubank.md) — inteiro teor do TJPE, RI 0046473-94.2024.8.17.8201 (2ª Turma Recursal da Capital, proclamação 12/05/2026), falso advogado, recebedor × pagador. Veio em .docx do PJe, num parágrafo só: quebras inseridas só nos marcos estruturais, sem paginação. **Pseudonimizado** em 20/10/2026 (autor → `[AUTOR]`); .docx não depositado.

## Normas do BCB e do CMN (texto oficial; circulam)

Impressas do Exibe Normativo do BCB em 20/10/2026 e convertidas pelo `pdfmd`. Cada `.md` tem um **`.higiene.diff`** ao lado: a higiene foi determinística e só tirou resíduo do site (banner de cookies, inclusive o que caía no meio de artigo; menu "expand_less"; links "Siga o BC"; rodapé e cabeçalho de impressão; tabelas de texto espelhado) e o caractere invisível U+200B que o HTML do BCB espalha nos títulos — o alerta de injeção do `pdfmd` era só isso. Os blocos `> **OCR da imagem**` são OCR de captura de página embutida no PDF e duplicam o texto nativo; ficaram. Links para `*_assets/` apontam para imagens não depositadas (logotipo e capturas do site).

- `res-bcb-96-2021-contas-de-pagamento.{pdf,md}` — **Res. BCB 96/2021**, contas de pagamento, **versão vigente atualizada em 24/11/2025** (com Res. BCB 365/2023, 476/2025 e 518/2025). Página: [res-bcb-96-2021-art-4-conta-de-pagamento](../jurisprudencia/res-bcb-96-2021-art-4-conta-de-pagamento.md).
- `res-cmn-5218-2025-bc-protege.{pdf,md}` — **Res. CMN 5.218/2025** (art. 2º-A na Res. 4.753: consulta ao BC Protege+), vigor 1º/12/2025. Página: [bc-protege-consulta-previa](../jurisprudencia/bc-protege-consulta-previa-res-cmn-5218-in-bcb-661.md).
- `in-bcb-661-2025-bc-protege.{pdf,md}` — **IN BCB 661/2025**, procedimentos do BC Protege+ (prova da consulta, art. 6º; indisponibilidade, art. 10). Mesma página.
- `res-bcb-103-2021-med.{pdf,md}` — **Res. BCB 103/2021**, cria o MED no regulamento do Pix. **Texto da resolução alteradora, não o regulamento consolidado**: o MED mudou depois. Página `em_teste`: [res-bcb-103-2021-med](../jurisprudencia/res-bcb-103-2021-med-mecanismo-especial-de-devolucao.md). A p. 2 do PDF tem art. 78-H a 78-I lidos como tabela, com erro de digitação da fonte ("partciipante", "iniciatvia"): não transcrever dali sem conferir no PDF.
- `bc-protege-faq-bcb.{pdf,md}` — FAQ do BC Protege+ (bcb.gov.br/meubc/faqs/s/bc-protege), impresso em 20/10/2026, itens datados de 01/12/2025 a 17/08/2026. **Divulgação, não norma.**
- Exposições de motivos (fonte interpretativa, sem página derivada): `voto-bcb-107-2021-contas-de-pagamento.{pdf,md}` (Res. BCB 96); `voto-bcb-119-2021-med.{pdf,md}` (Res. BCB 103); `voto-cmn-24-2025-bc-protege.md` (Res. CMN 5.218; encaminha o Voto 63/2025-BCB). **O PDF do Voto CMN 24 não foi depositado**: a folha de rosto do e-BC traz o CPF do servidor que autenticou a cópia; no `.md` o número virou `[CPF]` (diff ao lado).
- **Não depositados, ainda pendentes:** Res. BCB 475/2025 (cria o BC Protege+), Res. BCB 476/2025 em separado (o texto está consolidado na Res. 96), regulamento do Pix consolidado (anexo à Res. BCB 1/2020) e Manual Operacional do DICT.

## Fora do git (`.gitignore` §2; ficam na máquina de quem depositou)

- `cadeia-golpea-*.pdf`, `cadeia-golpeb-*.pdf`, `cadeia-golpec-*.pdf` — PDFs originais das cadeias (binário não se redige com segurança).
