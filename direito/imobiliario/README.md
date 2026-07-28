# Bundle de Competência — Rescisão Contratual de Imóvel (Direito Imobiliário)

Este é um **bundle de competência**: um pacote de conhecimento jurídico + skills + workflows que um agente de IA pode **executar**, não apenas consultar. Cobre o tema *rescisão de compromisso de compra e venda de lote urbano*: teses com fundamentos rastreáveis, o precedente vinculante local (IRDR-TO) com o ciclo recursal já mapeado, playbooks de petição inicial, contestação, agravo e cumprimento de sentença, heurísticas validadas em caso real do escritório, e o pipeline de skills que redige a peça no padrão PMA. Formato: [Open Knowledge Format (OKF)](https://github.com/GoogleCloudPlatform/knowledge-catalog) estendido.

## Como usar

Cole isto no seu agente (Claude Code, Cursor, Codex, Gemini CLI, …):

```
Aqui está um bundle de competência: <caminho-ou-url-deste-repositório>
Leia o README, configure-o e me diga o que você consegue EXECUTAR com ele.
```

## Instruções de setup para o agente

1. **O que é isto:** uma pasta de arquivos markdown com frontmatter YAML, navegada por `index.md` — sem banco de dados, sem embeddings.
2. **Para executar uma atividade:** leia **primeiro** o `atividades.md` — ele mapeia cada atividade para o workflow, as skills e o conhecimento obrigatório. Siga o workflow literalmente, respeitando seus portões de validação.
3. **Para responder perguntas:** navegue por progressive disclosure (índice → página → `raw/` só se necessário). Cite fontes pelo campo `resource`/`raw` do frontmatter. **Jamais cite jurisprudência que não esteja neste bundle** — se faltar, use citação indireta e diga que faltou.
4. **Filtre por `status: vigente`** por padrão. Desde a verificação de 2026-07-22 (v0.2.0), a jurisprudência do STJ e o IRDR-TO estão `vigente`; seguem `em_teste` apenas as 2 páginas de legislação (transcrição literal do Planalto pendente) e os 3 acórdãos do TJTO (não indexados publicamente) — sinalizar essa condição ao usuário sempre que empregar uma dessas páginas.
5. **Precedente central:** antes de qualquer peça do tema, ler `jurisprudencia/irdr-0009560-46-2017-tjto.md` — praticamente toda ação de rescisão de loteamento no foro local passa por ele, seja para aplicá-lo, seja para afastá-lo por *distinguishing*.

## Contrato de uso

- **Consumidores não modificam o bundle.** Produção e manutenção seguem o schema em `D:\GITHUB\KnowledgeOperatingSystem\piloto\SCHEMA_BUNDLE_PILOTO.md`.
- Este bundle **não contém dados de clientes**: o único `casos_decididos/` é anonimizado (nomes, CPF e número de processo removidos), e nenhum PDF/DOCX de petição, contestação ou sentença de cliente entra em `raw/` — só as duas decisões do STJ sobre o IRDR (processo de terceiro, público).
- A vigência da jurisprudência é revalidada por lint periódico; a data da última checagem está no campo `verificado_em` de cada página.

## O que há dentro

- `index.md` — sumário (comece aqui) · `atividades.md` — roteador de execução · `log.md` — histórico
- `jurisprudencia/` `teses/` `heuristicas/` `playbooks/` `casos_decididos/` — conhecimento
- `workflows/` — sequências executáveis (2 de 4 atividades) · `skills/` — pipeline de redação (formato Agent Skills, copiado de `direito/bancario/emprestimo-nao-realizado`)
- `raw/` — os 2 pares de fontes públicas do STJ sobre o IRDR (imutáveis)

Versão: ver `bundle_version` no `index.md`. Licença: uso interno do escritório PMA (não publicado).
