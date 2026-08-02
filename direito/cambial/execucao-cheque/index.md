---
okf_version: "0.1"
bundle_version: "0.3.0"
---

# Execução de Cheque — Bundle de Competência (Direito Cambial)

Cobrança judicial de cheque devolvido: o que torna o papel um título executivo, como se prova a recusa, em que janela se executa, quais encargos se pedem e como se monta a inicial de execução no padrão do escritório PMA. Agentes: leiam o [atividades.md](atividades.md) para executar.

## Seções

- [README.md](README.md) — onboarding do agente consumidor: setup, regras de citação e contrato de uso
- [atividades.md](atividades.md) — roteador: atividade → workflow → conhecimento obrigatório
- [jurisprudencia/](jurisprudencia/index.md) — Lei do Cheque por blocos temáticos e a norma do BCB sobre devolução, com status de vigência
- [teses/](teses/index.md) — teses do tema, com fundamentos e contra-argumentos esperados
- [heuristicas/](heuristicas/index.md) — regras de decisão, entre elas o portão de conferência da cártula
- [playbooks/](playbooks/index.md) — como construir a inicial de execução
- [workflows/](workflows/index.md) — sequência executável com portões
- [log.md](log.md) — histórico de ingestões, lints e alterações

## O tema num parágrafo

O cliente tem em mãos um cheque que o banco devolveu. Três perguntas decidem tudo o que vem depois. A primeira é se o papel preenche os requisitos do art. 1º da Lei nº 7.357/1985: faltando qualquer dos insupríveis, não há título executivo, e a execução ajuizada sobre ele é extinta com honorários contra o exequente. A segunda é quando a janela executiva se fecha: seis meses contados da expiração do prazo de apresentação, que é de 30 dias na mesma praça e 60 em praça diversa, tudo a partir da data de emissão estampada na cártula. A terceira é o que se pede além do principal: juros legais desde o dia da apresentação (art. 52, II), à taxa legal do art. 406 do Código Civil na redação da Lei nº 14.905/2024, e correção monetária, sem repetir a fórmula de "1% ao mês mais INPC" que circula em notificações extrajudiciais e não encontra base legal sem convenção entre as partes. Contra o emitente, a execução independe de protesto: o carimbo de devolução do verso é a declaração do sacado que produz os efeitos dele (art. 47, § 1º).

**v0.3.0 (2026-07-28).** Fontes oficiais depositadas em `raw/`: texto integral da Lei nº 7.357/1985 capturado do Planalto, a Carta-Circular BCB nº 1.256/1985, a tabela de motivos de devolução do Banco Central e o inteiro teor do **REsp 1.556.834/SP, Tema 942/STJ**, repetitivo da Segunda Seção transitado em julgado, que fixou os termos iniciais de juros e correção. Todas as páginas derivadas estão `vigente`, com transcrição conferida contra o depósito, salvo a da carta-circular, `em_teste` porque a vigência atual daquela norma de 1985 não foi conferida. Continuam fora do bundle, e portanto não citáveis, a Súmula 531/STJ e o Tema 564/STJ.
