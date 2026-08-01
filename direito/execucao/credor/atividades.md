---
type: router
title: Roteador de atividades — execução pelo credor
description: Mapeia cada situação do exequente (ajuizar, requerer cumprimento, buscar bens, achar bem em nome de terceiro, executar contra a Fazenda) para o conhecimento correspondente.
tags: [roteador, execucao, credor]
timestamp: '2026-08-01'
status: em_teste
autor: escritorio
---

# Roteador de atividades — execução pelo credor

## Cliente tem título extrajudicial e quer executar

- **Gatilhos:** "vou executar", "tenho um contrato/nota promissória/cheque não pago", "execução de título extrajudicial"
- **Conhecimento obrigatório:** [playbook do extrajudicial](playbooks/playbook-execucao-de-titulo-extrajudicial.md), [averbar antes que o bem suma](heuristicas/averbar-antes-que-o-bem-suma.md), [pedir os sistemas um a um](heuristicas/pedir-os-sistemas-um-a-um.md)
- **Portão inaugural:** qualificar o documento como título (rol do art. 784 + certeza, liquidez e exigibilidade) **antes** de qualquer redação
- **Decisão consciente:** Justiça Comum × Juizado — no Juizado, não achar bens significa extinção imediata
- **Entrada mínima:** o título, o cálculo do débito, o que já se sabe sobre o patrimônio do devedor

## Ganhamos a ação e o réu não pagou

- **Gatilhos:** "transitou em julgado", "vou entrar com cumprimento de sentença", "o réu não pagou"
- **Conhecimento obrigatório:** [playbook do cumprimento](playbooks/playbook-pedido-de-cumprimento-de-sentenca.md)
- **Portões:** a sentença é líquida? o pedido está sendo feito **mais de um ano** depois do trânsito (muda a forma de intimação)? o demonstrativo do art. 524 tem os sete itens?
- **Lembrete:** pedir expressamente multa **e** honorários de 10% — a fonte induz a esquecer os honorários

## As consultas voltaram todas negativas

- **Gatilhos:** "não achei bens", "vou ser intimado para indicar bens", "execução parada"
- **Conhecimento obrigatório:** [pedir os sistemas um a um](heuristicas/pedir-os-sistemas-um-a-um.md), [ler a declaração de renda](heuristicas/ler-a-declaracao-de-renda-como-mapa-de-bens.md), [documentar a recusa administrativa](heuristicas/documentar-a-recusa-administrativa-antes-de-pedir-ao-juiz.md), [perseguir constrição efetiva](heuristicas/manter-a-execucao-em-movimento.md)
- **URGÊNCIA:** a primeira tentativa infrutífera já disparou o prazo da prescrição intercorrente — e requerimento pendente **não** o interrompe. Manter os autos em movimento protege contra o arquivamento; só citação, intimação ou constrição efetivas protegem o crédito

## A execução está parada há muito tempo

- **Gatilhos:** "essa execução é antiga", "vale a pena continuar?", "o executado alegou prescrição intercorrente"
- **Conhecimento obrigatório:** [perseguir constrição efetiva](heuristicas/manter-a-execucao-em-movimento.md) e, no bundle irmão, a [tese do executado](../defesa-executado/teses/prescricao-intercorrente-corre-da-primeira-tentativa-infrutifera.md) — ler o que virá contra você
- **Diagnóstico antes de investir:** medir o intervalo entre a primeira tentativa infrutífera e o último ato **interruptivo** (citação, intimação ou constrição efetivas). Petições não contam desde a Lei 14.195/2021

## O devedor tem bens, mas nada está no nome dele

- **Gatilhos:** "o carro é dele mas está no nome da sogra", "mora no imóvel mas não é o dono", "laranja", "passou tudo para os filhos"
- **Conhecimento obrigatório:** [ação probatória autônoma](teses/acao-probatoria-autonoma-para-revelar-patrimonio.md), [simulação por indícios](heuristicas/provar-simulacao-por-indicios-em-acao-autonoma.md)
- **Primeira pergunta:** o negócio existiu e só não vale contra o credor (fraude) ou foi aparente (simulação)? A resposta muda a ação e o polo passivo

## O juiz indeferiu a diligência de busca

- **Gatilhos:** "o juiz negou o ofício", "mandou eu mesmo buscar a informação"
- **Justiça Comum:** agravo de instrumento (art. 1.015, parágrafo único)
- **Juizado:** [mandado de segurança na Turma Recursal](teses/ms-na-turma-recursal-contra-indeferimento-de-busca.md)

## O devedor é ente público

- **Gatilhos:** "executar o município", "precatório", "RPV", "a Fazenda foi condenada"
- **Conhecimento obrigatório:** [playbook da Fazenda](playbooks/playbook-cumprimento-contra-a-fazenda-publica.md)
- **Portão de vigência:** a fonte é anterior às emendas constitucionais de 2021 — reconferir todo prazo e valor
- **Não perder:** o contrato de honorários tem de estar nos autos **antes** de o requisitório ir ao tribunal

## Ganhei honorários mas o vencido é beneficiário da gratuidade

- **Gatilhos:** "a sentença suspendeu os honorários", "beneficiário da justiça gratuita", "não vou receber"
- **Conhecimento obrigatório:** [derrubar a suspensão de exigibilidade](teses/derrubar-suspensao-de-honorarios-do-beneficiario.md)
- **Relógio:** cinco anos do trânsito em julgado, e depois extingue

## Composição peça × matéria

A peça sai pelo fluxo padrão do workspace: `perfil/definicoes.md` → este bundle → `direito/pecas/<tipo>` → `md2docx` com os três lints. Toda página aqui está `em_teste`: citar exige conferência oficial prévia ou `cita_em_teste: sim` declarado no frontmatter.
