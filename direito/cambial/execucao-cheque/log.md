# Log — bundle Execução de Cheque

## 2026-07-28 (terceira rodada)

**Ingestão** — REsp 1.556.834/SP, Segunda Seção, Rel. Min. Luis Felipe Salomão, julgado em 22/06/2016, DJe de 10/08/2016, sob o rito dos repetitivos. Inteiro teor fornecido pela titular e depositado em `raw/resp-1556834-sp.pdf`, com transcrição por `pdfmd` ao lado. Página derivada: `jurisprudencia/resp-1556834-sp-termo-inicial-juros-e-correcao.md`, `status: vigente`. Primeiro acórdão do bundle. `bundle_version` para 0.3.0.

**Tese firmada:** "Em qualquer ação utilizada pelo portador para cobrança de cheque, a correção monetária incide a partir da data de emissão estampada na cártula, e os juros de mora a contar da primeira apresentação à instituição financeira sacada ou câmara de compensação."

**Pendência resolvida:** o termo inicial da correção monetária na data de emissão era pendência declarada desde a primeira rodada, e a página do art. 52 registrava que não podia ser citado em peça. Passa a poder, com inteiro teor depositado.

**Cruzamento com o conhecimento existente:** o precedente **reforça** as três teses do bundle e não contradiz nenhuma. Reforço adicional colhido do voto: a contagem da prescrição (6 meses da expiração do prazo de apresentação, de 30 ou 60 dias), o prazo quinquenal da monitória pela Súmula 503/STJ, e a ineficácia cambiária da pós-datação extracartular (REsp 1.423.464/SC). A heurística sobre súmulas de monitória ganhou fundamento direto: o próprio voto emprega a Súmula 503 como prazo, nunca como encargo.

**Delimitação registrada na página:** o precedente fixa **termo inicial**, não taxa. Havendo juros convencionados, a taxa é a da convenção; não havendo, é a do art. 406 do Código Civil.

**Conferência no painel de repetitivos, na mesma sessão:** a titular consultou o portal do STJ e confirmou tratar-se do **Tema Repetitivo 942**, ramo Direito Civil, Segunda Seção, **trânsito em julgado em 04/10/2016**, sem embargos de declaração, afetado em 20/11/2015, com processos destacados de ofício pelo relator e origem no TJSP. A pendência aberta horas antes, sobre o número do tema não constar do inteiro teor, nasceu e morreu no mesmo dia: o precedente passa a ser citável como Tema 942/STJ.

## 2026-07-28 (segunda rodada)

**Ingestão** — tabela oficial de motivos de devolução de cheque, capturada de
`https://www.bcb.gov.br/meubc/faqs/p/motivos-de-devolucao-de-cheques` (página do Banco Central, atualizada em 11/10/2023).
A página é aplicação de página única e não entrega conteúdo por requisição simples; foi renderizada com Playwright e depositada
em `raw/` como PDF e como transcrição do texto renderizado. Página derivada: `jurisprudencia/motivos-de-devolucao-de-cheque-bcb.md`, `status: vigente`.

**Pendência 2 da rodada anterior, resolvida.** Os códigos numéricos do carimbo passam a ter fonte oficial no bundle, e a peça
volta a poder nomear o motivo pelo código. A página da Carta-Circular nº 1.256/1985 foi atualizada para remeter à tabela; ela
permanece `em_teste` apenas quanto à sua vigência atual.

**Três correções que a ingestão produziu no conhecimento já escrito:**

1. **Reapresentação.** A regra anterior, tirada da carta-circular de 1985, dizia apenas que não se reapresenta mais de uma vez.
   A tabela é mais precisa e mais restritiva: nova apresentação de cheque devolvido pelos motivos 12, 13, 14, 43, 44, 45 e 72 é
   **remessa nula** (motivo 49), devolvível a qualquer tempo. A janela útil de reapresentação existe uma única vez, e depois do motivo 11.
2. **Erro de preenchimento.** O motivo 31 enumera os defeitos que o próprio banco devolve: sem data de emissão, **mês grafado
   numericamente**, ausência de assinatura, valor por extenso ausente ou incompleto. O mês em números não constava do checklist e passou a constar.
3. **Beneficiário e integridade.** Motivo 48 (cheque acima de R$ 100,00 sem identificação do beneficiário), 33 (divergência de
   endosso) e 35 (fraude, rasura ou adulteração) entraram nos blocos 3 e 6 do checklist.

**Confirmação colateral:** o motivo 44 descreve o cheque prescrito como "apresentado após decorridos 6 meses da expiração do prazo
de apresentação", o que confirma, pela ótica operacional bancária, a contagem do art. 59 da Lei do Cheque já registrada nas teses.

## 2026-07-28

**Ingestão** — criação do bundle (`bundle_version: 0.1.0`), domínio `direito/cambial/`.

Fontes oficiais depositadas em `raw/`:

- `lei-7357-1985.htm` e `lei-7357-1985.md` — texto integral da Lei nº 7.357/1985 capturado de `https://www.planalto.gov.br/ccivil_03/leis/l7357.htm` em 28/07/2026. Conversão determinística do HTML para texto, sem OCR.
- `carta-circular-bcb-1256-1985.pdf` e `.md` — Carta-Circular BCB nº 1.256, capturada de `https://normativos.bcb.gov.br/Lists/Normativos/Attachments/39021/C_Circ_1256_v1_O.pdf`. Conversão por `pdfmd --ocr auto`.

Páginas derivadas: 5 de legislação sobre a Lei do Cheque (`vigente`, transcrições conferidas contra o depósito), 1 sobre a carta-circular (`em_teste`), 3 teses, 3 heurísticas, 1 playbook, 1 workflow, 1 roteador.

**Correção de metadado na ingestão:** o arquivo do Banco Central foi baixado sob nome que sugeria 1988; o documento é datado de **23 de julho de 1985**, e os arquivos em `raw/` foram renomeados para refletir a data correta.

**Pendências declaradas nesta rodada:**

1. Vigência atual da Carta-Circular nº 1.256/1985 não conferida contra o Banco Central. A página fica `em_teste` até a conferência.
2. ~~A numeração dos motivos de devolução impressa nos carimbos atuais não consta da carta-circular ingerida.~~ **Resolvida na segunda rodada do mesmo dia**, com a ingestão da tabela oficial do Banco Central.
3. Nenhum acórdão ingerido. Enunciados do STJ sobre monitória de cheque e sobre termo inicial da correção monetária permanecem fora do bundle e não podem ser citados em peça.
4. Sem `casos_decididos/`: só depois de desfecho, e sempre anonimizado. Sem `escritorio.md`, que dois dos quatro bundles anteriores também não têm.

**Origem do pedido:** demanda da titular durante a preparação de uma execução real, com a determinação de que toda execução de cheque passe a incluir checagem do correto preenchimento da cártula. A determinação virou o portão obrigatório em `heuristicas/conferir-preenchimento-do-cheque-antes-de-executar.md`, referenciado pelo roteador, pelo playbook e pela etapa 2 do workflow.

**Achado incorporado como heurística:** notificação extrajudicial do escritório fundamentava juros de 1% ao mês e correção pelo INPC em enunciados sumulares cujo objeto é o prazo da ação monitória. O erro não migrou para a peça e gerou `heuristicas/nao-usar-sumulas-de-monitoria-para-fundamentar-encargos.md`.
