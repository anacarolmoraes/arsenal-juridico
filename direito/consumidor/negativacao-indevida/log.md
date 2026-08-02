# Log do bundle — negativacao-indevida

## 2026-07-31 — mudança de domínio (v0.2.0): bancário → consumidor

**Decisão da titular.** O bundle nasceu em `direito/bancario/` porque o caso de origem era
bancário. É o endereço errado: negativação indevida acontece em telefonia, energia, varejo,
ensino e plataformas com o mesmo regime, porque a fonte é a mesma — o art. 43 do CDC. O banco é
um fornecedor entre outros, não a matéria.

Movido para `direito/consumidor/negativacao-indevida/`. **Todo caso de negativação indevida
consulta este bundle**, qualquer que seja o setor, e busca no bundle da relação de origem o que
for específico dela.

Consequências aplicadas:

- `heuristicas/ler-documentos-do-banco-pelo-que-negam.md` → `ler-documentos-do-fornecedor-pelo-que-negam.md`, com a tabela de documentos reescrita em termos de fornecedor (comprovante de entrega em vez de AR de cartão; histórico de faturas ao lado do extrato de conta).
- `heuristicas/reconstruir-saldo-na-data-da-negativacao.md` → `reconstruir-debito-na-data-da-negativacao.md`: "saldo devedor" é vocabulário de conta corrente; o teste é o mesmo contra histórico de faturas.
- Links relativos ao bundle `emprestimo-nao-realizado` corrigidos de `../../` para `../../../bancario/`, porque a profundidade mudou.
- Ressalva acrescentada no `index.md`: a Súmula 479/STJ é redigida para instituições financeiras e **não se estende por analogia direta** a outros fornecedores — fora do setor bancário, o caminho é a lógica de risco do empreendimento do art. 14 do CDC.
- Pendência nova: o acervo não tem caso de negativação fora do setor bancário. As heurísticas estão generalizadas, mas seus exemplos não — a primeira negativação de telefonia ou varejo deve confirmá-las ou corrigi-las.

Acrescentada à heurística de leitura de documentos a cautela contra **afirmar o que um manuscrito
ambíguo diz**: no caso de origem, duas peças anteriores do escritório leram a mesma data
manuscrita de formas diferentes, e ambas provavelmente erradas.

## 2026-07-31 — criação (v0.1.0, semente)

Extraído do caso Diego (embargos de declaração em apelação, TJTO, 1ª Câmara Cível). O bundle
`emprestimo-nao-realizado` cobria a fraude na contratação, mas nada cobria a **negativação em si**:
art. 43 do CDC, Súmula 385, notificação prévia e baixa após quitação ficavam órfãos, e as teses
foram montadas do zero na peça.

**Criado:**

- `jurisprudencia/sumula-385-stj.md` — `vigente`. Conferida contra o compêndio oficial de súmulas
  do STJ já depositado no acervo (`/pecas/recurso-especial/raw/SumulasSTJ_oficial.md`, linhas
  30499-30514); extrato verbatim com procedência declarada em `raw/sumula-385-stj.md`.
- `jurisprudencia/resp-1061134-rs.md` — `em_teste`. Repetitivo da notificação prévia.
- `jurisprudencia/cdc-art-43.md` — `em_teste`, **sem texto literal**.
- duas heurísticas, `vigente`.

**Duas decisões que valem registro:**

1. **A página do art. 43 nasceu sem o texto do art. 43.** O Planalto esteve inacessível na
   criação e o CDC não está depositado em nenhum `raw/` do acervo. Transcrever de memória
   produziria verificação circular: a peça citaria o dispositivo, o `lint-citacoes` conferiria a
   citação contra a página, e a página seria a própria invenção. A página entrega o mapa
   (qual parágrafo sustenta qual tese) e declara a lacuna.
2. **O número do Tema do REsp 1.061.134/RS não foi afirmado.** As peças do escritório divergem
   entre si ("Tema 59" e "Temas 37, 38, 40, 41" no mesmo parágrafo das razões de apelação).
   Fixou-se citar o precedente pelo número do REsp até a conferência.

**Efeito colateral útil:** ao criar a página `em_teste` do REsp 1.061.134/RS, o `lint-citacoes`
passou a acusar a peça dos embargos com exit 3. Antes dava verde, porque o único candidato era a
própria apelação do caso, que não tem campo `status`. Era falso-verde: o escritório citava um
repetitivo não conferido e o portão não sabia.

**Pendências de Etapa 0:** depositar o inteiro teor do REsp 1.061.134/RS e confirmar o número do
Tema; depositar a transcrição oficial do art. 43 do CDC. Sem `teses/`, `playbooks/` e
`casos_decididos/` — o caso de origem não transitou em julgado.
