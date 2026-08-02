---
type: router
title: Roteador de atividades — execução de cheque
description: Mapeia os pedidos mais comuns sobre cheque devolvido para o workflow, o conhecimento obrigatório e a entrada mínima exigida.
tags: [roteador, cheque, execucao]
timestamp: '2026-07-28'
status: vigente
autor: escritorio
---

# Roteador de atividades — execução de cheque

## Executar cheque devolvido

- **Gatilhos:** "execução de cheque", "cheque sem fundos", "cheque devolvido", "cobrar cheque", "ação de execução de título extrajudicial fundada em cheque"
- **Workflow:** [/workflows/workflow-execucao-cheque.md](workflows/workflow-execucao-cheque.md)
- **Portão inaugural, sem exceção:** [/heuristicas/conferir-preenchimento-do-cheque-antes-de-executar.md](heuristicas/conferir-preenchimento-do-cheque-antes-de-executar.md). A conferência da cártula precede a redação; sem ela, não se escreve a peça.
- **Conhecimento obrigatório antes de redigir:** [/playbooks/playbook-execucao-cheque.md](playbooks/playbook-execucao-cheque.md), [/teses/index.md](teses/index.md), [/jurisprudencia/index.md](jurisprudencia/index.md)
- **Entrada mínima exigida:** imagem legível do cheque em frente e verso, consulta cadastral do emitente, qualificação do cliente, informação sobre cobrança extrajudicial anterior. Faltando a imagem do verso, entrevistar antes de executar: sem carimbo de devolução não há prova da recusa.

## Avaliar se ainda cabe execução

- **Gatilhos:** "o cheque prescreveu", "ainda dá para executar", "cheque antigo", "qual o prazo do cheque"
- **Conhecimento:** [/teses/janela-de-seis-meses-e-as-vias-remanescentes.md](teses/janela-de-seis-meses-e-as-vias-remanescentes.md), [/jurisprudencia/lei-7357-1985-art-59-62-prescricao.md](jurisprudencia/lei-7357-1985-art-59-62-prescricao.md)
- **Cálculo:** data de emissão da cártula, mais 30 dias se o lugar de emissão coincide com a praça de pagamento ou 60 se não coincide, mais seis meses.
- **Saída:** dentro da janela, seguir para a atividade de execução; fora dela, analisar ação de enriquecimento (art. 61), ação causal (art. 62) e monitória, esta com requisitos ainda não ingeridos no bundle.

## Definir juros e correção na cobrança de cheque

- **Gatilhos:** "quanto atualizar o cheque", "juros do cheque", "demonstrativo do débito"
- **Conhecimento:** [/teses/juros-desde-a-apresentacao-e-taxa-legal-do-art-406.md](teses/juros-desde-a-apresentacao-e-taxa-legal-do-art-406.md), [/jurisprudencia/lei-7357-1985-art-52-encargos.md](jurisprudencia/lei-7357-1985-art-52-encargos.md), [/heuristicas/nao-usar-sumulas-de-monitoria-para-fundamentar-encargos.md](heuristicas/nao-usar-sumulas-de-monitoria-para-fundamentar-encargos.md)
- **Regra rápida:** juros da primeira apresentação, à taxa legal do art. 406 do Código Civil; correção pelo IPCA; 1% ao mês apenas com convenção escrita.

## Decidir se reapresenta o cheque

- **Gatilhos:** "deposito de novo", "reapresentar o cheque", "vale a pena depositar outra vez"
- **Conhecimento:** [/heuristicas/reapresentar-antes-de-ajuizar-a-execucao.md](heuristicas/reapresentar-antes-de-ajuizar-a-execucao.md), [/jurisprudencia/carta-circular-bcb-1256-1985.md](jurisprudencia/carta-circular-bcb-1256-1985.md)
- **Regra rápida:** uma única reapresentação, após dois dias úteis, se a primeira recusa foi por falta de fundos e a data-limite da execução não estiver próxima.
