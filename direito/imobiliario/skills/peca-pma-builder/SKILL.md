---
name: peca-pma-builder
version: 1.1.0
description: |
  Biblioteca Node compartilhada para geração de peças jurídicas .docx no padrão PMA.
  Fornece helpers reutilizáveis (p, pMixed, pQuote, titulo, subtitulo, assinatura, etc.)
  e um builder único que aplica cabeçalho com banner, rodapé com logo + paginação,
  margens 3 cm, Montserrat 12 pt, entrelinha 1,3 — tudo conforme tipografia-pma.
  Substitui a duplicação de helpers em scripts gerar_*.js individuais.
  Use sempre que precisar gerar ou regerar um .docx de peça processual via Node.
---

# peca-pma-builder — Biblioteca de Geração de Peças .docx (Padrão PMA)

## Quando usar
- Geração ou regeneração de **qualquer** .docx de peça jurídica via Node (apelação, inicial, contestação, recurso, manifestação, embargos, parecer).
- Substitui a prática anterior de redefinir helpers `p()`, `pMixed()`, `titulo()`, etc. em cada script.
- **Proibido** copiar helpers desta skill para scripts locais. Sempre importar daqui.

## Por que existe
Antes desta skill, cada caso (caso A, caso B, caso C) tinha seu próprio `gerar_*.js` com ~100 linhas de boilerplate duplicado. Mudança visual exigia editar 4+ arquivos. Pior: nenhum dos scripts injetava o banner (cabeçalho) e a logo (rodapé) exigidos pela tipografia-pma Módulo 2.

## Como usar

```js
const PMA = require('d:/WORK/advocacia/skills/peca-pma-builder'); // ajuste ao caminho onde esta skill está instalada
const { p, pMixed, pQuote, pCentered, titulo, subtitulo,
        endereco, quebra, pageBreak, assinatura, buildDoc } = PMA;

const conteudo = [
  ...endereco([
    'AO JUÍZO DA 3ª VARA CÍVEL DA',
    'COMARCA DE PALMAS, ESTADO DO TOCANTINS',
  ]),
  quebra(),
  pMixed([{ text: 'Processo nº ', bold: true }, { text: '0000000-00.0000.8.27.2729', bold: true }]),
  quebra(),
  // ... corpo
  titulo('I.', 'Síntese Estratégica'),
  p('Texto da síntese...'),
  pQuote('Citação literal da sentença em bloco — Montserrat Light 11 pt, recuo 3 cm, sem itálico.'),
  subtitulo('I.1.', 'Subseção'),
  pMixed([{ text: 'Texto com ', }, { text: 'negrito inline', bold: true }, { text: '.' }]),
  // ... pedidos
  ...assinatura(
    [
      { nome: 'ANA CAROLINA RIBEIRO DE MORAES PAULO', oab: 'OAB/TO 6573' },
      { nome: 'FLAVIA PAULO OLIVEIRA',                 oab: 'OAB/TO 6951' },
    ],
    { localData: 'Palmas — TO, 20 de maio de 2026.' }
  ),
];

await buildDoc({
  titulo: 'Apelação Cível — Maria Exemplo da Silva',
  processo: '0000000-00.0000.8.27.2729',
  conteudo,
  outPath: './APELACAO_EXEMPLO.docx',
});
```

## API

### Helpers de parágrafo
| Função | Uso |
|---|---|
| `p(text, opts?)` | Parágrafo simples (justificado, Montserrat 12pt). `opts`: `bold`, `italics`, `alignment`, `spaceAfter`, `indent`, `size`. |
| `pMixed(runs, opts?)` | Parágrafo com runs mistos (negrito/itálico inline). `runs` = array de strings ou `{text, bold?, italics?, size?}`. |
| `pQuote(text, opts?)` | Citação em bloco (recuo 3 cm, Montserrat Light 11 pt, sem aspas e sem itálico — tipografia-pma Módulo 6.1). `opts`: `left`, `right` (em DXA). |
| `pCentered(text, opts?)` | Parágrafo centralizado (default bold). `opts`: `bold`, `italics`, `before`, `after`. |
| `titulo(num, texto)` | Seção principal — MAIÚSCULO + bold (ex: `titulo('I.', 'Dos Fatos')`). |
| `subtitulo(num, texto)` | Subseção — caixa mista + bold (ex: `subtitulo('I.1.', 'Cronologia')`). |
| `endereco(linhas)` | Array de linhas em bold à esquerda (cabeçalho do endereçamento ao juízo). |
| `quebra(spaceAfter?)` | Linha em branco. |
| `pageBreak()` | Quebra de página explícita. |
| `assinatura(adv, opts?)` | Bloco de assinatura. `adv` = `[{nome, oab}]`. `opts.localData` = linha "Cidade — UF, data." à direita acima das assinaturas. |

### Builder
```js
await buildDoc({
  titulo: 'metadado do .docx',
  processo: 'número do processo (vai em description)',
  conteudo: [Paragraph, Paragraph, ...],   // array de parágrafos
  outPath: 'caminho/arquivo.docx',          // obrigatório
  creator: 'PMA Advocacia',                 // opcional
  bannerPath: 'caminho/banner.png',         // opcional — default: assets/banner.png da skill
  logoPath: 'caminho/logo.png',             // opcional — default: assets/logo.png da skill
});
```

O `buildDoc` aplica automaticamente:
- A4 (11906 × 16838 twips)
- Margens 3 cm (1701 twips) topo/base/laterais
- Montserrat 12 pt como fonte padrão do documento
- Header: banner centralizado (tipografia-pma Módulo 2)
- Footer: logo à direita + paginação "Página X de Y" centralizada

## Assets
- `assets/banner.png` — cabeçalho institucional PMA (proporção ~13:1)
- `assets/logo.png` — logo PMA para rodapé (proporção ~2:1)

Ambos extraídos de `PETICAO_MODELO.docx` (tipografia-pma) — não editar sem coordenar com a tipografia-pma.

## Dependência externa
`docx` (npm global). Path padrão: `C:\Users\anamo\AppData\Roaming\npm\node_modules`. Pode ser sobrescrito via env var `NPM_GLOBAL_NODE_MODULES`.

## Limites (FORA DO ESCOPO)
- **Não** redige conteúdo jurídico — isso é tarefa do `legal-writer`/`legal-orchestrator` ou de skill específica (`apelacao-cirurgica`).
- **Não** valida consistência argumentativa — isso é `legal-consistency-validator`.
- **Não** decide layout visual avançado (tabelas complexas, gráficos, visual law) — para isso, estender este builder ou usar a skill `docx` diretamente.
