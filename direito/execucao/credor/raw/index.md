# Catálogo do `raw/` — execução pelo credor

Duas origens distintas, com regimes distintos de circulação.

## Fonte oficial (circula no git)

- `resp-2192857-df-penhora-restituicao-ir.md` — inteiro teor do **REsp 2.192.857/DF** (STJ, 3ª Turma, rel. Min. Moura Ribeiro, DJEN/CNJ 20/03/2025), convertido do PDF oficial pelo `pdfmd` em 2026-08-02. **Anonimizado** pela regra dura 10: partes e advogados viraram rótulo de papel; ministros, número do processo, datas, ementa, relatório e voto mantidos. O **PDF** fica fora do git (traz os nomes), em `advocacia/consumir/RESP-2192857-2025-03-20.pdf`. Lastro da página [REsp 2.192.857/DF](../jurisprudencia/resp-2192857-df-penhora-restituicao-ir.md).

- `resolucao-cnj-115-2010-precatorios.pdf` e `.md` — **Resolução CNJ 115/2010** (gestão de precatórios), texto compilado do portal de atos do CNJ, com a redação das Resoluções 123/2010 e 145/2012. 46 artigos, convertido pelo `pdfmd` em 2026-08-02; integridade conferida. Mesma ressalva do ordinal sobrescrito. **Compilação que para em 2012 e sem nota de revogação: conferir vigência no portal do CNJ antes de peticionar.** Lastro da página [art. 5º — honorários no precatório](../jurisprudencia/resolucao-cnj-115-2010-honorarios-no-precatorio.md).
- `cpc-arts-381-383.md`, `cpc-art-495.md`, `cpc-arts-523-524.md`, `cpc-arts-534-535.md`, `cpc-art-784.md`, `cpc-arts-798-799.md`, `cpc-art-828.md`, `cpc-art-835.md`, `cpc-art-844.md`, `cpc-art-910.md` — recortes do CPC; `cc-art-406.md`, `cc-art-389.md`, `cc-arts-167-168.md` — recortes do Código Civil; `lei-9099-arts-52-53.md` — recorte da Lei 9.099/95. Todos gerados por `recortar-artigo.py` a partir dos depósitos transversais em `direito/pecas/raw/`. **Não editar à mão: regerar.**
- `lei-12016-2009-mandado-de-seguranca.md` e `.html` — lei do mandado de segurança, matéria específica deste bundle (base da tese do MS na Turma Recursal), depositada por `depositar-lei.py`.

## Obra comercial de terceiro (fora do git)

Depositado em 2026-08-01, vindo de `consumir/EXECUCOES_CREDOR`: curso "Semana da Execução de Sucesso" / "Expert em Execução", do Prof. José de Andrade Neto, juiz de direito do TJMS. Fora do git (`.gitignore` §1); só o conhecimento reescrito nas páginas do bundle circula. Dois dos arquivos eram **protegidos por senha** e foram decifrados na ingestão.

## Procedimento

- `curso-execucao-procedimento-titulo-extrajudicial.md` e `curso-execucao-passo-a-passo-extrajudicial.md` — mesmo conteúdo; o segundo acrescenta os passos de qualificação do título, competência, busca prévia e inicial.
- `curso-execucao-procedimento-pedido-cumprimento.md`, `curso-execucao-passo-a-passo-cumprimento.md` e `curso-execucao-cumprimento-sentenca-segredos.md` — ~80% coincidentes. **O terceiro (40 páginas, era protegido por senha) é o único com a estratégia de busca de bens em cinco passos**; o segundo é o único com o roteiro de sete etapas até a inicial.
- `curso-execucao-liquidacao-de-sentenca.md` — modalidades e o teste prático que decide entre arbitramento e procedimento comum.
- `curso-execucao-execucao-provisoria.md` — art. 520, caução e as quatro hipóteses de dispensa do art. 521.
- `curso-execucao-execucao-contra-terceiro-titulo.md` — título truncado no original; **o tema real é execução contra a Fazenda Pública**. Precatório, RPV e honorários em requisitório. É o arquivo mais desatualizado do lote (anterior às EC 113 e 114/2021) e o mais degradado por OCR.
- `curso-execucao-semana-aulas-1-2-3.md`, `curso-execucao-semana-fixacao-aulas-1-2.md`, `curso-execucao-semana-fixacao-aula-4.md`, `curso-execucao-live1-porque-estudar.md` — método PPCR (prevenção, procura, coerção, recuperação), averbação premonitória em detalhe e o bloco de simulação.

## Busca de bens e constrição

- `curso-execucao-roteiro-busca-de-bens.md` — 27 páginas, era protegido por senha. Roteiro em cinco passos e as onze buscas alternativas.
- `curso-execucao-sistema-infojud.md` — **o melhor arquivo do lote**: como ler cada campo da declaração de renda e qual pedido cada achado autoriza.
- `curso-execucao-penhorar-dinheiro-em-bancos.md` — apesar do nome, é monotemático sobre **fintechs**: quais respondem à ordem judicial de bloqueio e quais não.
- `curso-execucao-provar-bem-do-executado.md` — a ação probatória autônoma; base da tese central do bundle.
- `curso-execucao-avaliacao-do-bem-penhorado.md` — arts. 870 a 875, quem avalia, como impugnar, nova avaliação.
- `curso-execucao-astreintes.md` — o mais completo em jurisprudência: Súmula 410/STJ, cumprimento provisório da multa, parâmetros de revisão, teto.
- `curso-execucao-receber-honorarios.md` — apesar do nome, trata **só** de honorários contra beneficiário da gratuidade.
- `curso-execucao-5-passos-fundamentais.md` — título truncado; é "5 passos para garantir o recebimento de um crédito".

## Modelos de peça

- `curso-execucao-modelo-agravo.md` — agravo contra indeferimento de diligência de busca.
- `curso-execucao-modelo-mandado-seguranca.md` — MS na Turma Recursal, mesma matéria no Juizado.

**Não copiar nenhum dos dois.** Só o esqueleto argumentativo foi aproveitado, nas páginas de tese. Erros confirmados nos modelos: "art. 1.03, §5º" no lugar de 1.003; "art. 475" para regras de experiência comum, que é o art. 375; menção a sistema de bloqueio já extinto; a palavra *mandamus* dentro do agravo (contaminação de copy-paste entre os dois modelos); remissões cruzadas a parágrafo errado; numeração romana pulando item; citação com "colacionar trecho da jurisprudência" por preencher; e, no MS, confusão entre direito de ação e razoável duração do processo, pedido de "citação" da autoridade coatora onde a lei exige notificação, e ausência de requerimento de ingresso da pessoa jurídica de direito público. Os dois modelos também **se contradizem entre si** sobre a necessidade de esgotar a via administrativa.

## Avisos permanentes

**Datação.** Meados de 2020, exatamente na virada do sistema de bloqueio de ativos: um dos arquivos documenta a mudança e todos os outros continuam usando o nome antigo. O material **desconhece** a repetição automatizada de ordens, a central de indisponibilidade de bens, a ferramenta de análise patrimonial do CNJ, o cadastro de clientes do sistema financeiro, a central notarial e o sistema de semoventes. As categorias de busca continuam válidas; **nomes de sistema, listas de empresas e links precisam ser refeitos** antes de virar checklist operacional — várias das empresas citadas encerraram atividades ou foram incorporadas.

**Erros de citação já mapeados** (não reproduzir): texto do art. 836, §1º, atribuído ao art. 835, §1º; parágrafos do art. 382 atribuídos ao art. 383, em dois arquivos; art. 525, §6º citado como art. 526, §6º; parcelamento do art. 916 aplicado ao cumprimento de sentença, do qual é expressamente excluído; um repetitivo do STJ atribuído ao STF; decisões do CADE fundadas em lei revogada; cédula de crédito bancário fundada em medida provisória superada.

**Afirmação enganosa a corrigir sempre:** três arquivos dizem que "até este momento não há imposição de honorários advocatícios" no cumprimento de sentença. Isso descreve a praxe do despacho, não o art. 523, §1º, que prevê multa de 10% **e** honorários de 10%.

**Conteúdo retido.** É funil de vendas e interrompe nos pontos mais valiosos: como penhorar crédito em intermediadora de pagamento, "mais 15 tipos de pedidos alternativos", "mais de 12 sistemas" — todos anunciados e não entregues.

**Higiene.** Links de grupo de WhatsApp, canais de Telegram e funis comerciais foram removidos na ingestão. Nenhum dado pessoal de cliente, CPF ou número de processo de terceiro foi encontrado: as partes dos exemplos são fictícias e os números citados são de julgados públicos.
