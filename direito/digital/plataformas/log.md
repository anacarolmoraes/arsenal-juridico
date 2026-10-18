# Log — digital/plataformas

## 2026-10-18

**Ingestão (v0.2.0).** Dois acórdãos do TJSP vindos de `consumir/` do motor, baixados do
CJSG/e-SAJ pela skill `buscar-jurisprudencia-tjsp` na pesquisa de um caso de conta de Instagram
desabilitada. São processos de terceiros; entraram pseudonimizados (regra dura 6: nome da autora,
nome e ID da conta, município da candidatura e @ do perfil viraram rótulo). PDF não depositado.

- ApCiv 1149661-90.2024.8.26.0100 (30ª CDPriv, 14/07/2025): conta de anúncios de candidata;
  CDC por vulnerabilidade, art. 51, IV, dano moral de R$ 10 mil, Súmula 326. `vigente`.
- ApCiv 1051450-82.2025.8.26.0100 (23ª CDPriv, 22/06/2026): restrição de funcionalidades de
  perfil profissional no Instagram; documento juntado após a sentença precluso; lucros cessantes
  negados sem prova mínima (liquidação não prova o *an debeatur*); dano moral de R$ 10 mil;
  sucumbência mínima do autor. `vigente`.
- Repertório de defesas: linhas 3 (parcial) e 7 saíram de lacuna; linhas 9 (prova tardia) e 10
  (reativação no curso do processo) novas; linha 6 ganhou o contraponto dos lucros cessantes.
- `segmentar-acordao.py`: o TJSP não usa cabeçalho "EMENTA". Na 1149661 o raw saiu
  `nao_segmentado`; na 1051450 o segmentador marcou a ementa do próprio acórdão como voz alheia,
  e o sidecar foi descartado para não bloquear a citação dela. As ementas alheias transcritas nos
  votos estão listadas nas páginas, com número, para citar pela fonte certa.

**Pendências:** ingerir o AgRg no AREsp 837.871/SP (finalismo mitigado) se a peça for citar o STJ;
conferir trânsito da ApCiv 1051450; ensinar o segmentador a reconhecer a ementa do TJSP (bloco
entre a autuação do voto e o relatório).

## 2026-08-02

**Ingestão.** Semente v0.1.0 do bundle, criada na migração do acervo local
`direito_digital/` (Fase 4 do PRD de versionamento e modularização do `pma-workspace`).
3 cadeias de litígio de terceiros depositadas em `raw/` (18 arquivos, todos fora do git —
regra dura 10), 3 páginas derivadas em `jurisprudencia/` (todas `em_teste`).

- **Decisão de arquitetura:** o roteador planejava `direito/lgpd/` como destino do acervo
  `direito_digital`, mas o conteúdo real é litígio criador × plataforma (desmonetização,
  bloqueio de conta) — nada de LGPD. Criado `direito/digital/plataformas/`; `direito/lgpd/`
  continua planejado, vazio, para quando houver conteúdo próprio de proteção de dados.
- A pasta de origem também continha o caso do escritório no tema (desmonetização de canal
  no YouTube) — camada C1, **não migra**; segue no workspace até ir para o Drive.
- Eixo do tema conforme prática do escritório: a tese vencedora é a de que **a plataforma
  não provou a infração concreta** (ônus da ré), não a discussão abstrata dos termos de uso.

**Pendências:**
1. Etapa 0 formal (ingest-prep.py + sidecar) para os 9 documentos.
2. Anonimizar as cadeias (regra dura 10) para versionar os `.md` — prioridade para os 3
   acórdãos/decisões, que são o material citável.
3. Capturar o acórdão de agravo transcrito na decisão do TJPI (paradigma de tutela).
4. Página de legislação: Marco Civil da Internet (arts. 7º e 8º) via
   `recortar-artigo.py` quando o código integral for depositado em `direito/pecas/raw/`.
5. Ritual 7.2 (encerramento) quando o caso do escritório no tema tiver desfecho — alimenta
   `casos_decididos/` e o placar das teses.
