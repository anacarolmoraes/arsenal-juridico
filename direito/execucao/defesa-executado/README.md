# Bundle de Competência — Defesa do Executado

Este bundle carrega o conhecimento para **defender quem sofre uma execução civil**: escolher o instrumento certo para a fase do processo (impugnação ao bloqueio SISBAJUD em 5 dias, embargos à execução, impugnação ao cumprimento de sentença, exceção de pré-executividade, petição simples de bem de família), montar a prova da impenhorabilidade e não cair nas preclusões que o Tema 1.235/STJ criou em 2024.

## Prompt de instalação

```
Aqui está um bundle de competência: direito/execucao/defesa-executado.
Leia o README, configure-o e me diga o que você consegue executar com ele.
```

## Setup para o agente

1. Ler o [index.md](index.md) para conhecer o tema e o [atividades.md](atividades.md) para despachar o pedido.
2. Rodar a verificação estrutural a partir da raiz do acervo: `python lint-bundle.py direito/execucao/defesa-executado`.
3. Saber o que existe em `raw/` pelo [catálogo](raw/index.md) — os arquivos `metodo-mma-*` são obra comercial de terceiro e podem não existir na sua máquina (ficam fora do git); o conhecimento reescrito está nas páginas do bundle.

## Como executar

Entre sempre pelo [atividades.md](atividades.md). Navegue por revelação progressiva: índice → página → `raw/` só se precisar da fonte.

**O relógio manda.** A pergunta inaugural de qualquer caso é "quando o cliente foi intimado e de quê?" — o prazo mais curto e mais destrutivo do tema é o de **5 dias** do art. 854, §3º (bloqueio SISBAJUD), porque o silêncio converte o bloqueio em penhora e preclui a impenhorabilidade dos 40 SM (Tema 1.235/STJ).

**Nunca cite o que não está conferido.** Este bundle é semente (v0.1.0): **todas as páginas estão `em_teste`** — os julgados vieram de material de estudo de terceiro, não de inteiro teor conferido. Antes de citar em peça: conferir na fonte oficial, depositar em `raw/` e promover a página; ou declarar `cita_em_teste: sim` no frontmatter da peça. O `lint-citacoes` bloqueia o caminho descuidado.

**Duas armadilhas que este bundle existe para evitar:** deixar passar os 5 dias do bloqueio confiando na velha jurisprudência de que "impenhorabilidade se alega a qualquer tempo" (morreu para o art. 833, X em 02/10/2024); e protocolar exceção de pré-executividade de matéria que exige dilação probatória — a via certa era embargos, e o incidente infundado custa litigância de má-fé.

## Contrato de uso

Consumidores não modificam o bundle. Produtores seguem o schema do acervo: fonte oficial em `raw/` antes de promover página a `vigente`, `status` declarado em toda página, superação só com confirmação da titular.

O bundle **não contém dados de cliente**. A única peça de caso real (`raw/peticao-terceiro-bem-de-familia-tjsp.md`) é de processo de terceiro e foi anonimizada conforme a regra dura 10 do workspace; o PDF original não circula.

## Versão

`bundle_version: 0.1.0` — semente de 2026-08-01. Histórico e pendências no [log.md](log.md).
