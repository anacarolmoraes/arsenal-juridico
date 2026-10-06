---
okf_version: "0.1"
bundle_version: "0.1.0"
---

# Vício do Produto — Bundle de Competência (Direito do Consumidor)

Produto que não funciona como deveria: carro zero que volta à oficina, eletrodoméstico que para, bem que perde valor pelo defeito. O regime é o do **art. 18 do CDC**: prazo de trinta dias para o fornecedor sanar e, vencido, escolha do consumidor entre substituição, restituição do preço ou abatimento, com **todos os fornecedores da cadeia solidários**.

## O tema num parágrafo

O fornecedor tenta três saídas, e cada uma tem resposta própria. Primeira, fatiar o prazo: cada retorno à oficina reabriria os trinta dias, e cada fornecedor teria o seu. O STJ conta o prazo de forma corrida e global. Segunda, empurrar a responsabilidade para o outro: a concessionária diz que o defeito é de fábrica e invoca o art. 13. O art. 13 é do fato do produto (acidente de consumo); no vício, a solidariedade é do art. 18. Terceira, a proporcionalidade: consertado o carro, devolver o preço seria excessivo. A regra do STJ é a contrária (o conserto tardio não apaga o direito), mas há dois precedentes de exceção, um da 3ª Turma por 3×2 e um da 4ª, ambos com restituição integral pedida anos depois do reparo. Distinguem-se pelo tempo, pelo pedido (perdas e danos, não preço integral) e pela extensão do excesso.

## Seções

- [jurisprudencia/](jurisprudencia/index.md): doze decisões do STJ (três contrárias, uma parcialmente contrária sobre financiamento coligado), inteiro teor depositado e anonimizado
- [teses/](teses/index.md): quatro teses de trabalho (`em_teste`)
- [raw/](raw/index.md): depósitos
- [log.md](log.md): histórico

## Fronteiras

- **Fato do produto** (acidente, dano à segurança, arts. 12 a 17) não mora aqui; quando chegar o primeiro caso, semear página própria.
- **Serviço** da concessionária (demora no reparo, recusa de carro reserva) é art. 14 e 20; cabe nas peças deste bundle como fundamento acumulado, mas sem página própria ainda.
- **Financiamento coligado** (art. 54-F do CDC): mora aqui enquanto o gatilho for compra com vício ou sem entrega; o banco de varejo entra pela [tese de coligação](teses/financiamento-coligado-cai-com-a-compra.md), não pela solidariedade do art. 18.
- **Negativação** decorrente do caso: [consumidor/negativacao-indevida](../negativacao-indevida/index.md).
- Técnica de peça: [direito/pecas/](../../pecas/index.md); honorários e sucumbência: `direito/pecas/sucumbencia/`.

## Pendências

1. **Etapa 0 da lei**: o art. 18 do CDC não tem recorte neste bundle. O CDC compilado está em `direito/pecas/raw/`; gerar recorte (`recortar-artigo.py 18`) antes de transcrever o artigo em peça.
2. **Julgado citado e não depositado**: o acórdão colegiado AgInt nos EDcl no REsp 1.697.426/MG (Cueva, 3ª T., 13/12/2021). Só a monocrática de 2020 que ele manteve está no acervo.
3. Sem `heuristicas/`, `playbooks/` e `casos_decididos/`: o caso de origem está em fase de recurso.
4. **Coligação com um só julgado, monocrático.** Depositar REsp 1.127.403/SP e REsp 1.406.245/SP (4ª T.) e procurar acórdão colegiado que aplique o art. 54-F; recortar o art. 54-F do CDC compilado.
