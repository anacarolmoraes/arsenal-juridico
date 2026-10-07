# Catálogo do `raw/` — defesa do executado

Depositado em 2026-08-01, vindo de `consumir/EXECUCOES_DEFESA_EXECUTADO`. Três regimes de circulação:

| Regime | Arquivos | Regra |
|---|---|---|
| **Obra comercial** (curso "Método MMA", Prof. José Andrade) | `metodo-mma-*` | fora do git (`.gitignore` §1); ficam só na máquina de quem depositou; conhecimento reescrito circula nas páginas do bundle |
| **Documento oficial do STJ** | `proafr-resp-2061973-pr-tema-1235-stj.*` | rastreado e circula na equipe |
| **Petição de processo de terceiro** | `peticao-terceiro-bem-de-familia-tjsp.*` | PDF fora do git; `.md` anonimizado (regra dura 10) circula na equipe, mas não em pacote externo |

## Arquivos

- `metodo-mma-cpl1-aula1-o-que-e-o-metodo.{pdf,md}` — apresentação do método (Meios de defesa × Matérias de defesa × Aplicação prática). OCR ruidoso; valor de mineração baixo — o framework já está reescrito nas heurísticas.
- `metodo-mma-cpl1-aula2-linha-do-tempo-execucao.{pdf,md}` — as 9 fases da execução de título extrajudicial (art. 784 → extinção) com a defesa cabível em cada uma (tradicional / específica / excepcional). Fonte da heurística de escolha do meio de defesa.
- `metodo-mma-cpl1-aula3-desbloqueio-sisbajud.{pdf,md}` — procedimento do art. 854, impenhorabilidade do salário (833, IV e §2º) e da reserva de 40 SM (833, X), com dezenas de ementas transcritas (STJ e TJs) e cláusulas de negócio processual p/ honorários. Fonte do playbook de impugnação ao bloqueio.
- `metodo-mma-cpl2-aula2-impenhorabilidade-de-bens.{pdf,md}` — art. 833 inciso a inciso, bem de família (Lei 8.009/90, legal e convencional), pequena propriedade rural, com ementas transcritas. Fonte das teses de impenhorabilidade.
- `metodo-mma-cpl2-aula2-meios-de-defesa.{pdf,md}` — embargos à execução (prazo, PI, efeito suspensivo), impugnação ao cumprimento de sentença (rol do 525 §1º) e exceção de pré-executividade (procedimento, recursos, honorários). Fonte do playbook de embargos.
- `metodo-mma-epe-mapa-mental.{pdf,md}` — mapa mental "Tudo sobre a Exceção de Pré-Executividade": matérias arguíveis, momento, recursos, EPE em execução fiscal e trabalhista.
- `proafr-resp-2061973-pr-tema-1235-stj.{pdf,md}` — **oficial**: acórdão de afetação (ProAfR) do REsp 2.061.973/PR ao Tema 1.235/STJ, Corte Especial, Rel. Min. Nancy Andrighi, sessão virtual encerrada 27/02/2024. É a afetação, **não** o acórdão de mérito (julgado em 02/10/2024 — inteiro teor pendente de depósito).
- `resp-1340553-rs-temas-566-571-prescricao-intercorrente-fiscal.md` — **oficial, recorte**: ementa integral (teses 4.1 a 4.5 e subitens) do repetitivo dos **Temas 566 a 571** mais a ementa integral dos **EDcl** que alteraram o item 3. Depositado em 2026-08-02. É **recorte, não inteiro teor**: o acórdão tem 175 páginas e os EDcl 17; o que se cita é a ementa, reproduzida aqui verbatim. Os PDFs e os `.md` completos (`.integral.md`), índices e manifestos do `pdfmd` ficam ao lado, fora do git: `resp-1340553-rs-temas-566-571-prescricao-intercorrente-fiscal.*` e `edcl-resp-1340553-rs-temas-566-571-prescricao-intercorrente-fiscal.*`. Recorrida (microempresa) anonimizada; Fazenda Nacional mantida por ser ente público.
- `resp-2188970-pr-prescricao-intercorrente-execucao-civel.md` — **oficial, inteiro teor, ANONIMIZADO**: REsp 2.188.970/PR (Quarta Turma, rel. Min. João Otávio de Noronha, j. 18/03/2025), 13 páginas. As duas partes recorridas já vêm reduzidas a iniciais pelo próprio STJ na publicação; **procurador do Estado e advogado do recorrido** (nomes completos, com OAB) viraram rótulo pela regra dura 10. Mantidos: Estado do Paraná (ente público), ministro (ato público), número do processo, ementa, relatório e voto integrais. Convertido pelo `pdfmd` (OCR — texto nativo do PDF vinha corrompido) em 2026-09-04; conversão limpa, 0 ligadura partida. Lastro da página [REsp 2.188.970/PR](../jurisprudencia/resp-2188970-pr-prescricao-intercorrente-execucao-civel.md).
- `resp-2188970-pr-prescricao-intercorrente-execucao-civel.integral.md` e `.pdf` — conversão crua (com os nomes) e PDF oficial, fora do git ao lado do `.md` anonimizado.
- **Depósitos de 2026-10-07**, vindos de `consumir/` do motor. Inteiro teor oficial **ANONIMIZADO** (partes privadas, advogados e procurador viram rótulo; ficam ministros, entes públicos, números de processo e de origem). PDF, `.integral.md`, `.index.md` e `.pdfmd.json` (com os nomes) ficam ao lado, fora do git. Cada um é lastro da página homônima em `jurisprudencia/`:
  - `agint-resp-2231082-to-prescricao-intercorrente-penhora-irrisoria.md` — AgInt no REsp 2.231.082/TO, 1ª Turma, 2026.
  - `resp-1986517-pr-diligencias-infrutiferas-nao-interrompem.md` — REsp 1.986.517/PR, monocrática, 2022.
  - `eresp-97328-pr-execucao-fiscal-paralisada-prescricao.md` — EREsp 97.328/PR, 1ª Seção, 1998. **PDF digitalizado, OCR ruidoso**: cinco trechos corrigidos contra a imagem e marcados `CORRECAO DECLARADA n`; o resto é OCR bruto, não transcrever sem conferir a página.
  - `resp-1102554-mg-arquivamento-baixo-valor-prescricao-intercorrente.md` — REsp 1.102.554/MG, repetitivo, 1ª Seção, 2009.
  - `eresp-1874222-df-salario-penhora-relativizacao-excepcional.md` — EREsp 1.874.222/DF, Corte Especial, 2023: **só ementa e acórdão** (2 p.); voto do relator e notas taquigráficas não depositados.
  - `eresp-1874222-df-voto-vogal-nao-conhecimento.md` — voto-vogal vencido no mesmo EREsp (não conhecimento); o documento não identifica o ministro. Não é voz da Corte.
  - `aresp-2711567-sp-garantia-infima-embargos-execucao-fiscal.md` — AREsp 2.711.567/SP, monocrática, 2024.
  - `resp-1954382-sp-honorarios-nao-sao-prestacao-alimenticia.md` — REsp 1.954.382/SP, repetitivo da Corte Especial, 2024, **inteiro teor completo (112 p.)** com votos-vista e vencidos; partes, advogados e advogados dos *amici curiae* (CFOAB, MDA) viraram rótulo. Lastro da página do repetitivo (arquivo `resp-1954380-...`). DJe não consta do documento.
- `peticao-terceiro-bem-de-familia-tjsp.md` — petição real (anonimizada) de arguição de impenhorabilidade de bem de família por simples petição (art. 518 c/c 917, §1º) em cumprimento de sentença no TJSP, com checklist probatório concreto (contas de consumo, habite-se, certidão negativa de outros imóveis, ata notarial com vizinho). Elo único de cadeia — sem decisão; não vira `caso-decidido`.

## Legislação depositada

- `lei-6830-1980-execucao-fiscal.{html,md}` — **Lei de Execução Fiscal**, texto compilado do Planalto (cobertura: até a Lei nº 14.689/2023). Depositada em 2026-08-02 para **fechar a fronteira** da prescrição intercorrente: o regime do art. 40 é oposto ao do art. 921 do CPC no termo inicial. Traz também o art. 16, § 1º, pelo qual embargos na execução fiscal **exigem garantia** — o inverso do art. 914.
  **Atenção:** o HTML da LEF usa riscado para a redação superada. A conversão preserva os **6 trechos revogados** com o rótulo `[REVOGADO — NAO CITAR]`; sem isso, o art. 16, II apareceria em duas versões e a antiga poderia ser citada. Conferir o rótulo antes de transcrever.
  *Não há bundle de execução fiscal; se vier a existir, este depósito migra para lá.*
- `lei-10522-2002-cadin-arquivamento-baixo-valor.{html,md}` — **Lei 10.522/2002** (CADIN, parcelamento federal, arquivamento de execução fiscal de baixo valor), texto compilado do Planalto, cobertura até a **Lei 14.973**. Depositada em 2026-10-07 por `depositar-lei.py` para lastrear o [REsp 1.102.554/MG](../jurisprudencia/resp-1102554-mg-arquivamento-baixo-valor-prescricao-intercorrente.md): o art. 20, na redação da Lei 13.874/2019, delega o valor de arquivamento a ato do PGFN. O revogado aparece como "(Revogado)", sem riscado. **Armadilha de busca:** vários cabeçalhos saem partidos entre linhas ("Art." numa linha, "26." na seguinte); grep por `^Art\. 26` falha. Em 2026-10-07 o script contou 41 cabeçalhos, mas o texto vai do art. 1º ao 40, com os artigos de letra.
- `cpc-art-921.md`, `cpc-arts-833-834.md`, `cpc-art-854.md`, `cpc-art-525.md`, `cpc-art-917.md` — recortes do CPC gerados por `recortar-artigo.py` a partir do depósito transversal em `direito/pecas/raw/`. **Não editar à mão: regerar.**

## Aviso permanente

Ementa ou tese lida nos `.md` do curso **não é fonte conferida**: número, órgão e data podem vir com erro de OCR ou de digitação do autor do slide. Antes de citar em peça, conferir no tribunal e depositar o inteiro teor aqui (regra dura 4 + lint-citacoes).
