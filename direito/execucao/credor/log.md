# Log — execução pelo credor

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
