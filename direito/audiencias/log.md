# Log — audiências

## 2026-08-02 — reancoragem normativa da videoconferência

**Resolvida a pendência de vigência nº 1, que era a que mais bloqueava o bundle.** Depositada a **Resolução CNJ 354/2020** (`raw/resolucao-cnj-354-2020-videoconferencia.pdf` + `.md`, texto compilado até a Res. 679/2026) e derivada a página `jurisprudencia/resolucao-cnj-354-2020-videoconferencia.md`, **`vigente`**, com 14 transcrições conferidas contra o depósito. É a primeira pasta `jurisprudencia/` e a primeira página `vigente` deste bundle.

O que a reancoragem mudou de substantivo na heurística de videoconferência — não foi troca de citação, foi ganho de conteúdo:

1. **A incomunicabilidade ganhou base própria e atual:** art. 7º, II — testemunhas inquiridas "cada uma de per si, de modo que umas não saibam nem ouçam os depoimentos umas das outras". Não é mais preciso invocar norma emergencial para impugnar oitiva de testemunhas do adversário no mesmo ambiente.
2. **A gravação é obrigação do juízo** (art. 7º, IV), com juntada aos autos ou depósito em repositório oficial. A gravação própria continua como seguro, mas o pedido do arquivo oficial passou a ser o caminho principal.
3. **O vocabulário mudou e importa na petição:** o art. 2º separa **videoconferência** (ato dentro de unidade judiciária) de **telepresencial** (a partir de ambiente externo). Pedir "videoconferência" para depor de casa é pedir outra coisa.
4. **O arranjo que a heurística defendia tem previsão expressa:** art. 4º manda ouvir testemunha, ofendido e perito residentes fora da sede **por videoconferência na sede do foro do domicílio** — dentro de unidade judiciária. É o que se requer quando o adversário quer ouvir de casa a testemunha que mora longe.
5. **Armadilha que a fonte não tinha:** art. 5º, § 3º — é ônus de quem requereu comparecer presencialmente em caso de indeferimento **ou de falta de análise** do pedido. Não existe deferimento tácito.
6. **Violência doméstica inverte a regra:** art. 3º-A (incluído pela Res. 679/2026) exige oitiva **presencial** da vítima como regra, telepresencial só em caráter excepcional e com anuência expressa manifestada na intimação.

**Portão de qualidade novo, criado nesta ingestão.** A conversão de PDF perde o ordinal sobrescrito (`Art. 1º` vira `Art. 1`), e a conferência acusou 8 falsas divergências por causa disso. O `depositar-lei.py` passou a **avisar** quando artigos de 1 a 9 aparecem sem indicador de ordinal, e a rotina de conferência normaliza o ordinal antes de comparar. Depois da normalização: 14 transcrições, **0 divergências**.

**Pendências que sobram no eixo de videoconferência:**

1. **Ato regulamentar do tribunal local** — o art. 13 atribui aos tribunais regulamentar a aplicação. Nenhum está depositado; o do TJTO precisa ser conferido antes de peticionar.
2. **Res. CNJ 341/2020**, referida nos arts. 2º e 12 (participação em unidade judiciária diversa), não depositada.
3. Os arts. 8º a 11 (citação e intimação por meio eletrônico) foram depositados e **não derivados** — são de outro eixo.

**Depositados também** os recortes da Lei 9.099/95 (arts. 9º, 20 e 55), que fechavam a lacuna de conteúdo nº 5 do dia anterior no plano do texto legal. **Ainda sem página derivada:** depósito não é página, e a lacuna só se fecha quando a transcrição for escrita e conferida.

## 2026-08-01

**Ingestão** — Semente v0.1.0, criada a partir de `consumir/EXECUCOES_CREDOR`, cuja pasta misturava três assuntos (execução pelo credor, audiências e justiça gratuita). Decisão da titular na mesma data: separar audiências em bundle transversal próprio; justiça gratuita **não consumir agora** (já é definição canônica em `perfil/definicoes.md`, e ingerir a aula criaria segunda fonte da mesma regra).

- `raw/`: 12 arquivos do curso "Semana da Audiência Sem Medo" (Prof. José de Andrade Neto, juiz do TJMS — obra comercial, fora do git) e 1 decisão judicial de processo de terceiro, **anonimizada** (partes viraram rótulo de papel; **código de acesso ao eSAJ suprimido** — era credencial de acesso ao inteiro teor, não chave de citação; número do processo e nome do magistrado mantidos). Varredura de vazamento limpa. Links de convite de WhatsApp e quiz com token removidos na ingestão.
- Páginas derivadas, todas `em_teste`: 5 heurísticas (tabela de pontos controvertidos, matriz de perguntas a testemunha, armadilhas do Juizado, videoconferência, correspondente/dativo) e 1 playbook (preparação de audiência).

**Avaliação honesta da fonte.** É material promocional: entrega o diagnóstico e retém o tratamento no curso pago. Três técnicas de inquirição são apenas nomeadas; a maioria dos "10 maiores medos" e das "situações inesperadas" enuncia o problema sem resolver. O bundle registra isso em vez de disfarçar.

**Lacunas de conteúdo (a fonte não cobre — completar de fora):**

1. Ordem dos atos da audiência (art. 361); pena de confissão (art. 385, *caput* e §1º).
2. Prova testemunhal em bloco (arts. 450-463): contradita (art. 457), testemunha impedida ou suspeita (art. 447), acareação, perguntas formuladas diretamente pelo advogado (art. 459).
3. Protesto/consignação em ata (art. 367, §1º).
4. Art. 357, §1º (esclarecimento e ajuste do saneamento em 5 dias) e §3º (saneamento compartilhado) — **e a preclusão que se segue**.
5. Juizado: arts. 9º, 20 e 55 da Lei 9.099/95 e o sistema recursal, inclusive a inexistência de agravo contra interlocutória.
6. Família: art. 695, segredo de justiça (art. 189, II), participação do MP, depoimento especial de criança e adolescente (Lei 13.431/2017).
7. Responsabilidade civil do advogado correspondente.

**Pendências de vigência (bloqueiam uso em peça):**

1. **Videoconferência** — reancorar: a fonte usa Res. CNJ 314/2020 (art. 6º, §3º) e Recomendação 62, **exauridas**. Conferir Res. CNJ 354/2020, o regime atual do CNJ e o ato do tribunal local.
2. **Res. CNJ 213/2015** (custódia) sofreu alterações após 2020 — relevante só quando houver bundle penal.
3. Enunciados FONAJE 35 e 141 citados a partir do material — conferir texto e vigência na fonte oficial. Observação: há um arquivo `ENUNCIADOS_FONAJE_juizados_especiais.md` em `consumir/`, candidato natural a depósito em `raw/` deste bundle.

**Fora de escopo declarado:** `raw/curso-audiencias-custodia-penal.md` — matéria penal, depositada e **não derivada**.
