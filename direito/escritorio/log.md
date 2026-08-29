# Log

## 2026-08-29

**Criação do bundle (v0.1.0).** Semente a partir de `consumir/ESCRITORIO/`, que estava parado desde
01/08/2026. O bundle já constava do roteador da raiz como planejado — *atendimento, checklist de
documentos por caso, organização de pastas C1, honorários* —, e nasce cobrindo só a parte institucional;
o resto entra quando houver material.

**Depositados** dois documentos da própria sociedade, ambos versão 1.0 de 2021: Regimento Interno e
Política de Privacidade. **Não são obra de terceiro** — logo, são rastreados e circulam na equipe. Mas
identificam a sociedade (razão social, endereço, encarregada de dados, regras de conduta), e por isso
foram registrados em `distribuicao.json` como **exclusão de camada 2**: não saem em pacote externo. É a
primeira vez que o acervo hospeda material institucional, e a fronteira precisou ser declarada antes do
conteúdo entrar.

**Uma página derivada:**
[`heuristicas/compromissos-da-politica-de-privacidade`](heuristicas/compromissos-da-politica-de-privacidade.md).
A premissa é que **política publicada é promessa oponível** — vale contra o escritório independentemente
do mínimo legal. A página consolida a tabela de prazos de retenção (5 anos do fim do ano de encerramento
do caso; 5 anos mínimos mesmo com pedido de exclusão; 6 meses para dado automatizado e para CCTV; 1 ano
para evento e boletim), o canal da encarregada e a ressalva de recusa quando o pedido do titular afeta
terceiro — que numa banca não é cláusula de estilo, porque o dado do cliente costuma ser dado do
adversário ou de testemunha.

Dois pontos que a leitura levantou e que a política não resolve sozinha: (1) o prazo de cinco anos corre
do **fim do ano** do encerramento, não da data — errar isso para menos descumpre a promessa publicada;
(2) a promessa de "nunca enviar mensagem com link para download" vale também para a comunicação de
rotina, e quebrá-la treina o cliente a confiar no formato que o golpista usa — cruzado com a heurística
de engenharia social do bundle [`lgpd`](../lgpd/index.md), criado na mesma rodada.

**Sem página derivada:** o Regimento Interno. Está depositado e catalogado; derivar dele exige decisão
sobre o que é norma da casa e o que já mora em `perfil/definicoes.md` no motor — e essa fronteira
importa, porque o motor é distribuível e este bundle não é.

**Pendências registradas no index:** ambos os documentos são de 2021 e nunca foram revisados; a Política
não fixa prazo de resposta ao titular nem trata de incidente de segurança; não há cópia da versão
efetivamente publicada depositada para conferência — se divergir, vale a publicada.
