# Log — execução pelo credor

## 2026-08-02 (terceira entrada) — Res. CNJ 115/2010 e uma citação errada do playbook

**Depositada a Resolução CNJ 115/2010** (`raw/resolucao-cnj-115-2010-precatorios.pdf` + `.md`, 46 artigos, compilada com as Resoluções 123/2010 e 145/2012) e derivada a página `jurisprudencia/resolucao-cnj-115-2010-honorarios-no-precatorio.md`, **`vigente`**, com as duas transcrições conferidas.

**Achado que corrige o acervo:** o playbook da Fazenda situava o destaque de honorários contratuais "a partir do art. 20" da Resolução, seguindo o material do curso. **Está no art. 5º, §§ 2º e 3º**, com o complemento do inciso XI. A substância que o playbook descrevia estava certa — o prazo é preclusivo e o contrato tem de estar nos autos **antes da apresentação do precatório ao tribunal**; feito o destaque, o advogado é **beneficiário do precatório** (§ 3º) —, mas a citação estava errada e teria ido errada para a peça. O playbook foi corrigido e agora aponta para a página.

**Caveat que ficou declarado na página, e é sério:** o depósito é compilação que **para em 2012** e **não traz nota de revogação**. Não confirmei se houve ato posterior do CNJ sobre gestão de precatórios, nem o efeito das **EC 113/2021 e 114/2021** sobre o procedimento. A regra do destaque é operacional e ancorada no art. 22, § 4º, do Estatuto da Advocacia, então sobrevive — mas a vigência da Resolução precisa ser conferida no portal do CNJ antes de peticionar. **Isso não fecha a lacuna nº 7** (regime de precatórios pós-2021), que continua sendo a maior deste bundle.

**Nota de método:** a conversão do PDF perde o ordinal sobrescrito; o `depositar-lei.py` passou a avisar quando artigos de 1 a 9 aparecem sem o indicador, e a conferência normaliza o ordinal antes de comparar.

## 2026-08-02 (segunda entrada)

**Ingestão** — Fechada a lacuna que era **bloqueante** deste bundle: juros e correção monetária. Depositados os recortes do **CC, arts. 389 e 406** e derivada a página `jurisprudencia/cc-arts-389-406-juros-e-correcao.md`, **`vigente`**, com as seis transcrições conferidas contra o depósito.

O que muda na prática: juros legais pela **taxa legal do art. 406** — Selic deduzido o IPCA —, correção pelo **IPCA** na falta de convenção (art. 389, p.u.), e resultado negativo conta como zero. O **"1% ao mês"** que a fonte de 2020 repete deixou de ter base legal com a Lei 14.905/2024, salvo onde a própria lei o fixa (parcelamento do art. 916). Os dois playbooks foram corrigidos.

Também depositados: **Lei 12.016/2009** (mandado de segurança, base da tese do MS na Turma Recursal) e os recortes de **CC arts. 167-168** (simulação) e **Lei 9.099, arts. 52-53** (a extinção imediata do § 4º).

**Pendência que permanece e é a mais importante deste bloco:** o **direito intertemporal da Lei 14.905/2024** — que critério vale para o período anterior à produção de efeitos, e como se compõe o cálculo que atravessa a virada. Aparece em todo caso real e não está no acervo. Também não estão o ato do CMN e a divulgação do BCB de que fala o § 2º.

## 2026-08-02 — v0.2.0: primeira página `vigente` do bundle

**Promoção vinda da camada de consumo.** Primeiro item promovido da `kb-youtube/jose-andrade-neto` (canal `@JoseAndradeneto`), pelo portão da Fase 6: **REsp 2.192.857/DF** — penhorabilidade da restituição de imposto de renda.

- `raw/resp-2192857-df-penhora-restituicao-ir.md` — inteiro teor conferido e depositado (STJ, 3ª Turma, rel. Min. Moura Ribeiro, sessão virtual de 11 a 17/03/2025, DJEN/CNJ 20/03/2025, processo 2025/0018524-0). Convertido do PDF oficial pelo `pdfmd`; **anonimizado** pela regra dura 10 (partes e advogados viraram rótulo; ministros, número, datas e todo o raciocínio mantidos). Varredura de vazamento limpa. O PDF fica fora do git, em `advocacia/consumir/`.
- Páginas novas, ambas `vigente`: [jurisprudencia/resp-2192857-df-penhora-restituicao-ir.md](jurisprudencia/resp-2192857-df-penhora-restituicao-ir.md) e [teses/restituicao-de-ir-e-penhoravel-onus-do-executado.md](teses/restituicao-de-ir-e-penhoravel-onus-do-executado.md). São as **primeiras páginas do bundle com citação conferida em fonte oficial** — o resto segue `em_teste`.
- Roteador ganhou a entrada "Achei restituição de imposto de renda a receber".

**A leitura do inteiro teor desmentiu a fonte da pista, e isso ficou registrado nas páginas.** O canal de YouTube apresentava o julgado como abertura de exceção jurisprudencial. Não é: o voto aplica a **Súmula 568** sobre jurisprudência já firmada e remonta ao **REsp 1.150.738/MG** (Nancy Andrighi, 2010). Além disso, o recurso foi provido **só** quanto à multa do art. 1.026, §2º — quanto à penhora, incidiu a **Súmula 7**. Citar como leading case seria frágil, e a página diz isso em voz alta.

**Ganho substantivo que a pista não trazia:** o acórdão de origem (TJDFT), transcrito e endossado pelo STJ, fixa que **a natureza alimentar da restituição não se presume** — o IR não incide só sobre salário (art. 43 do CTN) e cabe **ao executado** demonstrar a origem. É o melhor argumento do exequente na matéria e virou o segundo degrau da tese.

**Supre parcialmente a lacuna 5 do log de 2026-08-01** (arts. 833 e 834 ausentes): agora há tratamento conferido do art. 833, IV, ao menos quanto à restituição de IR. As demais impenhorabilidades continuam ausentes.

**Pendências abertas por esta ingestão:**

1. **Sem parâmetro numérico** do percentual que satisfaz a "dignidade do devedor e de sua família" — os julgados remetem ao caso concreto. Registrar em `casos_origem` quando houver decisão do escritório.
2. **Página espelho no bundle irmão** [defesa do executado](../defesa-executado/index.md) não existe: quem defender executado nessa matéria não tem página própria e terá de partir do "limite desta tese".
3. **URI canônica do acórdão** no STJ não registrada (`resource` aponta só para o portal) — o depósito supre para fins de conferência.

## 2026-08-02 — recortes do CPC

**Ingestão** — Depositados dez recortes do CPC, gerados por `recortar-artigo.py` a partir do depósito transversal e conferidos um a um: `cpc-arts-381-383` (produção antecipada de prova, base da tese central), `cpc-art-495` (hipoteca judiciária), `cpc-arts-523-524` (cumprimento e demonstrativo), `cpc-arts-534-535` (Fazenda Pública), `cpc-art-784` (rol dos títulos), `cpc-arts-798-799` (requisitos da inicial executiva), `cpc-art-828` (averbação premonitória), `cpc-art-835` (ordem da penhora), `cpc-art-844` (averbação da penhora) e `cpc-art-910` (extrajudicial contra a Fazenda).

Conferência: fronteira de artigo, ruído zero, e completude verificada onde a conversão do PDF havia corrompido no dia anterior — as **sete alíneas do art. 798** estão presentes.

**Depósito não é página.** A página `cpc-arts-381-383-producao-antecipada-de-prova.md` agora tem raw local e pode ser promovida quando a transcrição for escrita e conferida; os outros nove recortes esperam página derivada. Até lá, teses e playbooks que se apoiam neles seguem `em_teste`.

**Não cobertos pela fila e citados com destaque pelos playbooks:** art. 916 (moratória legal), art. 774, V (ato atentatório) e art. 98, §§ 2º e 3º (gratuidade, na tese de honorários).

## 2026-08-01

**Ingestão** — Semente v0.1.0, criada a partir de `consumir/EXECUCOES_CREDOR`. A pasta misturava três assuntos; audiências foi para o bundle transversal [direito/audiencias/](../../audiencias/index.md) e justiça gratuita ficou fora por decisão da titular (já é definição canônica em `perfil/definicoes.md`).

- `raw/`: 22 arquivos do curso "Semana da Execução de Sucesso" / "Expert em Execução" (Prof. José de Andrade Neto, juiz do TJMS) — obra comercial, fora do git. **Dois estavam protegidos por senha** (a senha era o último termo do nome do arquivo) e foram decifrados na ingestão: o roteiro de busca de bens, de 27 páginas, e o de cumprimento de sentença, de 40 — os dois arquivos mais densos do lote. Varredura de vazamento limpa; links de captação removidos.
- Páginas derivadas, todas `em_teste`: 3 de jurisprudência/legislação, 3 teses, 6 heurísticas, 3 playbooks.

**Avaliação da fonte.** Boa em estratégia, vencida em atualidade e imprecisa em citação. É material de meados de 2020, apanhado na virada do sistema de bloqueio de ativos: um arquivo documenta a mudança e os outros onze seguem usando o nome antigo. Também é funil comercial — retém conteúdo nos pontos mais valiosos ("mais 15 tipos de pedido", "mais de 12 sistemas", como penhorar crédito em intermediadora de pagamento).

**Erros de citação da fonte, mapeados e não reproduzidos** (inventário completo em `raw/index.md`): texto do art. 836, §1º atribuído ao art. 835, §1º; parágrafos do art. 382 atribuídos ao art. 383, em dois arquivos distintos; art. 525, §6º citado como art. 526, §6º; parcelamento do art. 916 aplicado ao cumprimento de sentença, do qual é expressamente excluído; repetitivo do STJ atribuído ao STF; "art. 1.03, §5º" e "art. 475" nos modelos de peça; decisões do CADE fundadas em lei revogada; cédula de crédito bancário fundada em MP superada.

**Afirmação enganosa corrigida no playbook:** três arquivos afirmam que "até este momento não há imposição de honorários advocatícios" no cumprimento de sentença — descreve a praxe do despacho, não o art. 523, §1º.

**Pendências de conferência (bloqueiam promoção a `vigente`):**

1. Texto vigente dos arts. 381 a 383, 495, 523, 524, 534, 535, 784, 798, 799, 828, 835, 844 e 910 — **o depósito do CPC já existe** em `direito/pecas/raw/` desde 2026-08-01, então isto virou trabalho mecânico: rodar o recorte de cada faixa e conferir. **Não depositar o CPC aqui:** o código integral mora uma vez em `direito/pecas/raw/` e este bundle recebe recortes — `python recortar-artigo.py 381-383 direito/execucao/credor`, e assim por diante. Procedimento no [catálogo do raw transversal](../../pecas/raw/index.md).
2. Súmulas 317 e 376 do STJ — conferir enunciado literal no repositório oficial.
3. Precedentes citados sem relator, turma ou data confiáveis: o da desnecessidade de esgotamento para deferir consulta aos sistemas; o da inexistência de quebra de sigilo na consulta fiscal; o da reiteração de bloqueio após tempo razoável; os dois sobre prova indiciária de simulação; e o do sequestro por descumprimento do prazo da requisição de pequeno valor.

**Lacunas bloqueantes (a fonte não cobre — completar de fora antes de orientar caso real):**

1. ~~**Prescrição intercorrente — art. 921.**~~ **Parcialmente suprida em 2026-08-01:** a norma foi para o bundle irmão (`defesa-executado/jurisprudencia/cpc-art-921-prescricao-intercorrente.md`), por ser matéria de defesa, e a heurística deste bundle foi **corrigida** — a **Lei 14.195/2021** deslocou o termo inicial para a primeira tentativa infrutífera e restringiu a interrupção a citação, intimação ou constrição efetivas (§ 4º-A), o que **esvazia a tática de encadear requerimentos** que o material de 2020 ensina. Continua pendente a transcrição oficial do artigo e a jurisprudência posterior a 2021.
2. **Art. 406 do Código Civil e critério de correção monetária.** Nenhum arquivo diz qual taxa ou índice aplicar, embora exija que o demonstrativo os declare. A alteração pela Lei 14.905/2024 atinge todo cálculo montado a partir daqui.
3. **Art. 782, §§3º a 5º** (inscrição em cadastro de inadimplentes) e **art. 517** (protesto da decisão) — duas medidas de pressão baratas, ausentes.
4. **Art. 854** — penhora de dinheiro por meio eletrônico, com os prazos de 24 horas e 5 dias. Ausente.
5. **Arts. 833 e 834** — impenhorabilidades. Ausentes; supridas pelo bundle irmão [defesa do executado](../defesa-executado/index.md).
6. **Art. 830, §§1º a 3º** — o rito do arresto executivo que a própria fonte manda requerer; só o caput é citado.
7. **EC 113/2021 e EC 114/2021** e alterações posteriores ao regime de precatórios — todo o playbook da Fazenda é regime pré-2021.
8. **Arts. 133 a 137** (incidente de desconsideração), **art. 792** (fraude à execução) e ação pauliana — nomeados como rótulos, nunca procedimentalizados. Só a simulação recebeu tratamento completo.
9. **Art. 523, §2º** — pagamento parcial faz multa e honorários incidirem sobre o restante.
10. Leilão, arrematação e preço vil (arts. 880 a 903) — só remissão de bloco.

**Nomenclatura a atualizar antes de qualquer checklist operacional:** nomes de sistemas de busca, listas de administradoras, corretoras e programas de fidelidade — várias empresas citadas encerraram atividades ou foram incorporadas desde 2020.
