# Bundle de Competência — Empréstimo Não Realizado (Direito Bancário)

Este é um **bundle de competência**: um pacote de conhecimento jurídico + skills + workflows que um agente de IA pode **executar**, não apenas consultar. Cobre o tema *fraude em empréstimo consignado não contratado*: teses com fundamentos rastreáveis até os acórdãos oficiais do STJ, playbooks de petição inicial e apelação, heurísticas estratégicas validadas em caso real, e o pipeline de skills que redige a peça no padrão do escritório PMA. Formato: [Open Knowledge Format (OKF)](https://github.com/GoogleCloudPlatform/knowledge-catalog) estendido.

## Como usar

Cole isto no seu agente (Claude Code, Cursor, Codex, Gemini CLI, …):

```
Aqui está um bundle de competência: <caminho-ou-url-deste-repositório>
Leia o README, configure-o e me diga o que você consegue EXECUTAR com ele.
```

## Instruções de setup para o agente

1. **O que é isto:** uma pasta de arquivos markdown com frontmatter YAML, navegada por `index.md` — sem banco de dados, sem embeddings. Inclui a CLI sem dependências `okf-cli.py` (Python stdlib; origem: bundle `cole-medin-ai-coding`).
2. **Verifique o setup:** `python okf-cli.py index` deve imprimir o sumário. Confirme que a pasta `skills/` contém as 6 skills listadas em `skills/skills-lock.json`.
3. **Para executar uma atividade:** leia **primeiro** o `atividades.md` — ele mapeia cada atividade para o workflow, as skills e o conhecimento obrigatório. Siga o workflow literalmente, respeitando seus portões de validação.
4. **Para responder perguntas:** navegue por progressive disclosure (índice → página → `raw/` só se necessário). Cite fontes pelo campo `resource` do frontmatter. **Jamais cite jurisprudência que não esteja neste bundle** — se faltar, use citação indireta e diga que faltou.
5. **Filtre por `status: vigente`** por padrão; documentos `superada` existem só como histórico.

## Contrato de uso

- **Consumidores não modificam o bundle.** Produção e manutenção seguem o schema em `KnowledgeOperatingSystem/piloto/SCHEMA_BUNDLE_PILOTO.md`.
- Este bundle **não contém dados de clientes**: casos decididos são anonimizados e fontes brutas de casos permanecem fora do pacote.
- A vigência da jurisprudência é revalidada por lint periódico; a data da última checagem está no campo `verificado_em` de cada página.

## O que há dentro

- `index.md` — sumário (comece aqui) · `atividades.md` — roteador de execução · `log.md` — histórico
- `jurisprudencia/` `teses/` `heuristicas/` `playbooks/` `casos_decididos/` — conhecimento
- `workflows/` — sequências executáveis · `skills/` — pipeline de redação (formato Agent Skills)
- `raw/` — PDFs oficiais imutáveis

Versão: ver `bundle_version` no `index.md`. Licença: uso interno do escritório PMA (não publicado).
