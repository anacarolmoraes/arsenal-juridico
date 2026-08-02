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
- `resp-1340553-rs-temas-566-571-prescricao-intercorrente-fiscal.md` — **oficial, recorte**: ementa integral (teses 4.1 a 4.5 e subitens) do repetitivo dos **Temas 566 a 571** mais a ementa integral dos **EDcl** que alteraram o item 3. Depositado em 2026-08-02. É **recorte, não inteiro teor**: o acórdão tem 175 páginas e os EDcl 17; o que se cita é a ementa, reproduzida aqui verbatim. Os `.md` completos, índices e manifestos do `pdfmd` ficam em `advocacia/consumir/RESP_1340553.*` e `EDRESP_1340553.*`, fora do git. Recorrida (microempresa) anonimizada; Fazenda Nacional mantida por ser ente público.
- `peticao-terceiro-bem-de-familia-tjsp.md` — petição real (anonimizada) de arguição de impenhorabilidade de bem de família por simples petição (art. 518 c/c 917, §1º) em cumprimento de sentença no TJSP, com checklist probatório concreto (contas de consumo, habite-se, certidão negativa de outros imóveis, ata notarial com vizinho). Elo único de cadeia — sem decisão; não vira `caso-decidido`.

## Legislação depositada

- `lei-6830-1980-execucao-fiscal.{html,md}` — **Lei de Execução Fiscal**, texto compilado do Planalto (cobertura: até a Lei nº 14.689/2023). Depositada em 2026-08-02 para **fechar a fronteira** da prescrição intercorrente: o regime do art. 40 é oposto ao do art. 921 do CPC no termo inicial. Traz também o art. 16, § 1º, pelo qual embargos na execução fiscal **exigem garantia** — o inverso do art. 914.
  **Atenção:** o HTML da LEF usa riscado para a redação superada. A conversão preserva os **6 trechos revogados** com o rótulo `[REVOGADO — NAO CITAR]`; sem isso, o art. 16, II apareceria em duas versões e a antiga poderia ser citada. Conferir o rótulo antes de transcrever.
  *Não há bundle de execução fiscal; se vier a existir, este depósito migra para lá.*
- `cpc-art-921.md`, `cpc-arts-833-834.md`, `cpc-art-854.md`, `cpc-art-525.md`, `cpc-art-917.md` — recortes do CPC gerados por `recortar-artigo.py` a partir do depósito transversal em `direito/pecas/raw/`. **Não editar à mão: regerar.**

## Aviso permanente

Ementa ou tese lida nos `.md` do curso **não é fonte conferida**: número, órgão e data podem vir com erro de OCR ou de digitação do autor do slide. Antes de citar em peça, conferir no tribunal e depositar o inteiro teor aqui (regra dura 4 + lint-citacoes).
