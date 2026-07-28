// peca-pma-builder/index.js
// Helpers reutilizáveis para geração de peças jurídicas no padrão PMA.
// Aplica o padrão da tipografia-pma: Montserrat 12pt, margens 3cm, entrelinha 1,3 (312 DXA),
// banner no cabeçalho centralizado, logo + paginação no rodapé.
//
// Uso típico:
//   const PMA = require('d:/WORK/advocacia/skills/peca-pma-builder');
//   const { p, pMixed, pQuote, titulo, subtitulo, pageBreak, buildDoc } = PMA;
//   const conteudo = [ titulo('I.', 'Síntese'), p('texto...'), ... ];
//   buildDoc({ titulo: '...', processo: '...', conteudo, outPath: 'APELACAO.docx' });

const path = require('path');
const fs = require('fs');

// Carrega docx do diretório global do npm (Windows padrão; ajustar se necessário)
const globalNodeModules = process.env.NPM_GLOBAL_NODE_MODULES
  || 'C:\\Users\\anamo\\AppData\\Roaming\\npm\\node_modules';
const docx = require(path.join(globalNodeModules, 'docx'));
const {
  Document, Packer, Paragraph, TextRun, AlignmentType, ImageRun,
  PageNumber, Footer, Header, HeightRule, BorderStyle,
} = docx;

// ─── Constantes do padrão PMA ────────────────────────────────────────────────
const FONT = 'Montserrat';
const FONT_LIGHT = 'Montserrat Light'; // uso exclusivo em citações em bloco (tipografia-pma Módulo 6)
const SIZE_BODY = 24;      // 12pt em half-points
const SIZE_QUOTE = 22;     // 11pt
const SIZE_FOOTER = 20;    // 10pt
const LINE = 312;          // 1,3 entrelinhas em 240ths
const SPACE_AFTER = 240;   // 12pt
const MARGIN_3CM = 1701;   // 3cm em twips
// Distância do header/footer até a borda da página — valores do PETICAO_MODELO.docx.
// SEM isso, o docx-js aplica o default do Word (708 twips ≈ 1,25cm) e o banner/logo
// ficam recuados para dentro, descolados das bordas — não parecem o papel timbrado.
const HEADER_DIST = 135;   // ~0,24cm (banner colado ao topo, como no modelo)
const FOOTER_DIST = 45;    // ~0,08cm (rodapé colado à base, como no modelo)

// Dimensões EMU canônicas (tipografia-pma Módulo 2) → convertidas para px @ 96 DPI
// banner.png  → cx=7560000 cy=567000  → 794 × 59 px
// logo.png    → cx=1921387 cy=828184  → 202 × 87 px
const BANNER_PX = { w: 794, h: 59 };
const LOGO_PX = { w: 202, h: 87 };

// Assets default (banner + logo) — copiados de PETICAO_MODELO.docx
const ASSETS_DIR = path.join(__dirname, 'assets');
const DEFAULT_BANNER = path.join(ASSETS_DIR, 'banner.png');
const DEFAULT_LOGO = path.join(ASSETS_DIR, 'logo.png');

// ─── Helpers de parágrafo ────────────────────────────────────────────────────

function p(text, opts = {}) {
  const runOpts = {
    text,
    font: FONT,
    size: opts.size || SIZE_BODY,
    bold: opts.bold || false,
    italics: opts.italics || false,
  };
  return new Paragraph({
    alignment: opts.alignment || AlignmentType.JUSTIFIED,
    spacing: { line: LINE, after: opts.spaceAfter !== undefined ? opts.spaceAfter : SPACE_AFTER },
    indent: opts.indent || undefined,
    children: opts.runs || [new TextRun(runOpts)],
  });
}

// Parágrafo com múltiplos runs (suporta bold/italics inline).
// Cada run: string (texto puro) ou { text, bold?, italics?, size? }.
function pMixed(runs, opts = {}) {
  const trs = runs.map(r => {
    if (typeof r === 'string') return new TextRun({ text: r, font: FONT, size: SIZE_BODY });
    return new TextRun({
      text: r.text, font: FONT, size: r.size || SIZE_BODY,
      bold: !!r.bold, italics: !!r.italics,
    });
  });
  return new Paragraph({
    alignment: opts.alignment || AlignmentType.JUSTIFIED,
    spacing: { line: LINE, after: opts.spaceAfter !== undefined ? opts.spaceAfter : SPACE_AFTER },
    indent: opts.indent || undefined,
    children: trs,
  });
}

// Citação em bloco (tipografia-pma Módulo 6.1): recuo 3 cm à esquerda,
// Montserrat Light 11 pt, sem aspas e sem itálico — o recuo já sinaliza a citação.
function pQuote(text, opts = {}) {
  return new Paragraph({
    alignment: AlignmentType.JUSTIFIED,
    spacing: { line: LINE, before: 120, after: 240 },
    indent: { left: opts.left || MARGIN_3CM, right: opts.right || 0 },
    children: [new TextRun({ text, font: FONT_LIGHT, size: SIZE_QUOTE, italics: false })],
  });
}

// Título de seção principal (I., II., III.) — MAIÚSCULO + bold + alinhado à esquerda.
function titulo(numeracao, texto) {
  return new Paragraph({
    alignment: AlignmentType.LEFT,
    spacing: { line: LINE, before: 360, after: 240 },
    children: [new TextRun({
      text: `${numeracao} ${texto.toUpperCase()}`,
      font: FONT, size: SIZE_BODY, bold: true,
    })],
  });
}

// Subtítulo (I.1., I.2.) — caixa mista + bold.
function subtitulo(numeracao, texto) {
  return new Paragraph({
    alignment: AlignmentType.LEFT,
    spacing: { line: LINE, before: 240, after: 180 },
    children: [new TextRun({
      text: `${numeracao} ${texto}`,
      font: FONT, size: SIZE_BODY, bold: true,
    })],
  });
}

// Parágrafo centralizado (uso: título "APELAÇÃO CÍVEL", "RAZÕES DE APELAÇÃO").
function pCentered(text, opts = {}) {
  return new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { line: LINE, before: opts.before || 240, after: opts.after || 240 },
    children: [new TextRun({
      text, font: FONT, size: SIZE_BODY,
      bold: opts.bold !== false, italics: !!opts.italics,
    })],
  });
}

// Bloco de endereçamento ao juízo (várias linhas em negrito à esquerda).
function endereco(linhas) {
  return linhas.map(l =>
    new Paragraph({
      alignment: AlignmentType.LEFT,
      spacing: { line: LINE, after: 0 },
      children: [new TextRun({ text: l, font: FONT, size: SIZE_BODY, bold: true })],
    })
  );
}

// Espaço em branco (parágrafo vazio).
function quebra(spaceAfter = 120) {
  return new Paragraph({
    children: [new TextRun({ text: '', font: FONT, size: SIZE_BODY })],
    spacing: { line: LINE, after: spaceAfter },
  });
}

// Quebra de página explícita.
function pageBreak() {
  return new Paragraph({
    children: [new TextRun({ text: '', font: FONT, size: SIZE_BODY, break: 1 })],
    pageBreakBefore: true,
  });
}

// Bloco de assinatura — várias advogadas em sequência.
// adv = [{ nome, oab }, ...]
function assinatura(adv, opts = {}) {
  const out = [];
  if (opts.localData) {
    out.push(p(opts.localData, { alignment: AlignmentType.RIGHT, spaceAfter: 360 }));
  }
  adv.forEach((a, i) => {
    const lastBlock = i === adv.length - 1;
    out.push(pMixed([{ text: a.nome, bold: true }], { alignment: AlignmentType.CENTER, spaceAfter: 0 }));
    out.push(pMixed([{ text: a.oab }], { alignment: AlignmentType.CENTER, spaceAfter: lastBlock ? 240 : 240 }));
  });
  return out;
}

// ─── Header e Footer institucionais (banner + logo + paginação) ──────────────

function buildHeader(bannerPath = DEFAULT_BANNER) {
  return new Header({
    children: [
      new Paragraph({
        alignment: AlignmentType.CENTER,
        children: [
          new ImageRun({
            data: fs.readFileSync(bannerPath),
            transformation: BANNER_PX,
            type: 'png',
          }),
        ],
      }),
    ],
  });
}

function buildFooter(logoPath = DEFAULT_LOGO) {
  return new Footer({
    children: [
      // Linha 1: logo à direita
      new Paragraph({
        alignment: AlignmentType.RIGHT,
        spacing: { after: 60 },
        children: [
          new ImageRun({
            data: fs.readFileSync(logoPath),
            transformation: LOGO_PX,
            type: 'png',
          }),
        ],
      }),
      // Linha 2: paginação centralizada "X de Y"
      new Paragraph({
        alignment: AlignmentType.CENTER,
        children: [
          new TextRun({ text: 'Página ', font: FONT, size: SIZE_FOOTER }),
          new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: SIZE_FOOTER }),
          new TextRun({ text: ' de ', font: FONT, size: SIZE_FOOTER }),
          new TextRun({ children: [PageNumber.TOTAL_PAGES], font: FONT, size: SIZE_FOOTER }),
        ],
      }),
    ],
  });
}

// ─── Builder principal ───────────────────────────────────────────────────────
// opts:
//   titulo: string (metadado do .docx)
//   processo: string (vai em "description")
//   conteudo: Paragraph[] (corpo da peça)
//   outPath: string (caminho do arquivo de saída)
//   creator: string (default: "PMA Advocacia")
//   bannerPath / logoPath: caminhos personalizados (default: assets/ da skill)
async function buildDoc(opts) {
  const {
    titulo: docTitle, processo, conteudo, outPath,
    creator = 'PMA Advocacia',
    bannerPath = DEFAULT_BANNER,
    logoPath = DEFAULT_LOGO,
  } = opts;

  if (!conteudo || !Array.isArray(conteudo)) {
    throw new Error('buildDoc: opts.conteudo deve ser um array de Paragraph');
  }
  if (!outPath) throw new Error('buildDoc: opts.outPath é obrigatório');

  const doc = new Document({
    creator,
    title: docTitle || '',
    description: processo ? `Processo ${processo}` : '',
    styles: { default: { document: { run: { font: FONT, size: SIZE_BODY } } } },
    sections: [
      {
        properties: {
          page: {
            size: { width: 11906, height: 16838 }, // A4 em twips
            margin: {
              top: MARGIN_3CM, right: MARGIN_3CM, bottom: MARGIN_3CM, left: MARGIN_3CM,
              header: HEADER_DIST, footer: FOOTER_DIST,
            },
          },
        },
        headers: { default: buildHeader(bannerPath) },
        footers: { default: buildFooter(logoPath) },
        children: conteudo,
      },
    ],
  });

  const buffer = await Packer.toBuffer(doc);
  fs.writeFileSync(outPath, buffer);
  return outPath;
}

// ─── Export ──────────────────────────────────────────────────────────────────
module.exports = {
  // helpers de parágrafo
  p, pMixed, pQuote, pCentered,
  titulo, subtitulo, endereco, quebra, pageBreak, assinatura,
  // builder
  buildDoc, buildHeader, buildFooter,
  // constantes (úteis para casos especiais)
  FONT, SIZE_BODY, SIZE_QUOTE, SIZE_FOOTER, LINE, SPACE_AFTER, MARGIN_3CM,
  // re-exports do docx (caso o script precise de algo customizado)
  docx,
};
