#!/usr/bin/env python3
"""
ingest-prep.py — Etapa 0 da ingestão (SCHEMA_BUNDLE_PILOTO, seção 7.1).

Varre raw/, converte PDFs sem par .md usando pdfmd (escalonando os modos de OCR),
pontua a qualidade do markdown de forma DETERMINÍSTICA (zero tokens de LLM) e
grava um sidecar <arquivo>.quality.json com o veredito.

Regra para o agente de ingestão: leia o sidecar antes do .md.
  - aprovado  -> prossiga normalmente
  - marginal  -> leia sinalizando incoerências na página derivada
  - reprovado -> NÃO leia o .md; registre pendência no log para revisão humana

Uso (com o Python do ambiente do pdfmd):
  D:/WORK/advocacia/pdfmd/pdfmd_env/Scripts/python.exe ingest-prep.py [--force] [--raw raw]
"""

import argparse
import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

PDFMD = r"D:\WORK\advocacia\pdfmd\pdfmd_env\Scripts\pdfmd.exe"
# Escalonamento: cada modo só roda se o anterior não atingir "aprovado".
OCR_MODES = ["auto", "tesseract", "ocrmypdf"]
OCR_LANG = "por"

# Âncoras típicas de documento jurídico brasileiro — ausência só gera aviso.
ANCHORS = ["EMENTA", "ACÓRDÃO", "ACORDAO", "RELATOR", "SENTENÇA", "SENTENCA",
           "Art.", "artigo", "Súmula", "Sumula"]

RX_GARBAGE_RUN = re.compile(r"[A-Za-z0-9+/=]{30,}")          # runs tipo base64 (assinaturas PJe)
RX_SIG_ARTIFACT = re.compile(r"\$\$[^\n]{0,80}@")            # artefatos "$$ ...@" de validação
RX_TOKEN = re.compile(r"[A-Za-zÀ-ÿ]{3,}")
RX_VOWEL = re.compile(r"[aeiouáéíóúâêôãõàAEIOUÁÉÍÓÚÂÊÔÃÕÀ]")

APROVADO, MARGINAL = 75, 55  # limiares calibráveis (registrar mudanças no log)


def page_count(pdf: Path) -> int:
    import fitz  # pymupdf, presente no ambiente do pdfmd
    with fitz.open(pdf) as doc:
        return doc.page_count


def score_markdown(md_text: str, pages: int) -> dict:
    metrics, penalties = {}, []
    text = md_text.strip()
    n = max(len(text), 1)

    # 1. Cobertura de extração (páginas escaneadas sem OCR rendem quase nada)
    coverage = len(text) / max(pages, 1)
    metrics["chars_por_pagina"] = round(coverage)
    if coverage < 200:
        penalties.append(("cobertura_baixa", 45))
    elif coverage < 600:
        penalties.append(("cobertura_mediana", 15))

    # 2. Proporção de letras (texto real é majoritariamente alfabético)
    letters = sum(c.isalpha() or c.isspace() for c in text)
    metrics["proporcao_letras"] = round(letters / n, 3)
    if metrics["proporcao_letras"] < 0.70:
        penalties.append(("proporcao_letras_baixa", 30))
    elif metrics["proporcao_letras"] < 0.80:
        penalties.append(("proporcao_letras_mediana", 10))

    # 3. Tokens pronunciáveis (lixo como 'C5424525510=4830' não tem vogal)
    tokens = RX_TOKEN.findall(text)
    if tokens:
        vowel_ratio = sum(bool(RX_VOWEL.search(t)) for t in tokens) / len(tokens)
    else:
        vowel_ratio = 0.0
    metrics["tokens_com_vogal"] = round(vowel_ratio, 3)
    if vowel_ratio < 0.90:
        penalties.append(("tokens_impronunciaveis", 25))

    # 4. Artefatos conhecidos (assinatura digital PJe/STJ, caractere de substituição)
    garbage = len(RX_GARBAGE_RUN.findall(text)) + len(RX_SIG_ARTIFACT.findall(text))
    garbage += text.count("�")
    metrics["artefatos"] = garbage
    if garbage > 20:
        penalties.append(("muitos_artefatos", 25))
    elif garbage > 5:
        penalties.append(("alguns_artefatos", 10))

    # 5. Tabelas quebradas (células vazias em excesso nas linhas com pipe)
    pipe_lines = [l for l in text.splitlines() if l.count("|") >= 2]
    if pipe_lines:
        cells = [c.strip() for l in pipe_lines for c in l.split("|")[1:-1]]
        empty = sum(1 for c in cells if not c) / max(len(cells), 1)
        metrics["celulas_vazias_tabelas"] = round(empty, 3)
        if empty > 0.40:
            penalties.append(("tabelas_quebradas", 15))

    # 6. Âncoras jurídicas (só aviso — nem todo documento as tem)
    metrics["ancoras_encontradas"] = [a for a in ANCHORS if a in text]
    if not metrics["ancoras_encontradas"]:
        metrics["aviso"] = "nenhuma âncora jurídica encontrada — confira se o documento é do tipo esperado"

    score = max(0, 100 - sum(p for _, p in penalties))
    verdict = "aprovado" if score >= APROVADO else "marginal" if score >= MARGINAL else "reprovado"
    return {"score": score, "verdict": verdict, "metrics": metrics,
            "penalidades": [name for name, _ in penalties]}


def convert(pdf: Path, out_md: Path, mode: str) -> bool:
    # --page-breaks insere marcadores '---' por página: permite citar a página
    # do PDF oficial em todo trecho literal (exigência do relatório de fontes)
    cmd = [PDFMD, str(pdf), "-o", str(out_md), "--ocr", mode, "--lang", OCR_LANG,
           "--page-breaks", "-q", "--no-progress", "--no-color"]
    try:
        r = subprocess.run(cmd, capture_output=True, timeout=1800)
        return r.returncode == 0 and out_md.exists()
    except (subprocess.TimeoutExpired, OSError):
        return False


def process(pdf: Path, force: bool) -> dict:
    md = pdf.with_suffix(".md")
    sidecar = pdf.with_suffix(".quality.json")
    if md.exists() and sidecar.exists() and not force:
        return json.loads(sidecar.read_text(encoding="utf-8")) | {"pulado": True}

    pages = page_count(pdf)
    best = None
    for mode in OCR_MODES:
        tmp = pdf.with_suffix(f".{mode}.tmp.md")
        if not convert(pdf, tmp, mode):
            continue
        result = score_markdown(tmp.read_text(encoding="utf-8", errors="replace"), pages)
        result["modo_ocr"] = mode
        if best is None or result["score"] > best[0]["score"]:
            best = (result, tmp)
        if result["verdict"] == "aprovado":
            break

    # limpa temporários, promove o melhor
    if best:
        result, winner = best
        winner.replace(md)
    for mode in OCR_MODES:
        tmp = pdf.with_suffix(f".{mode}.tmp.md")
        tmp.unlink(missing_ok=True)
    if not best:
        result = {"score": 0, "verdict": "reprovado", "metrics": {},
                  "penalidades": ["conversao_falhou_em_todos_os_modos"]}

    result |= {"arquivo": pdf.name, "paginas": pages, "gerado_em": date.today().isoformat(),
               "ferramenta": "pdfmd"}
    sidecar.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    return result


def main():
    ap = argparse.ArgumentParser(description="Portão de qualidade da ingestão (Etapa 0)")
    ap.add_argument("--raw", default="raw", help="pasta com os PDFs (default: raw/)")
    ap.add_argument("--force", action="store_true", help="reconverte mesmo com par .md existente")
    args = ap.parse_args()

    raw = Path(__file__).parent / args.raw
    pdfs = sorted(raw.glob("*.pdf"))
    if not pdfs:
        print(f"nenhum PDF em {raw}")
        return 0

    worst = "aprovado"
    order = {"aprovado": 0, "marginal": 1, "reprovado": 2}
    for pdf in pdfs:
        r = process(pdf, args.force)
        tag = "(já convertido)" if r.get("pulado") else f"[modo {r.get('modo_ocr', '-')}]"
        print(f"{r['verdict'].upper():9} score={r['score']:3} {tag} {pdf.name}"
              + (f"  penalidades: {', '.join(r['penalidades'])}" if r.get("penalidades") else ""))
        if order[r["verdict"]] > order[worst]:
            worst = r["verdict"]

    print(f"\nresultado geral: {worst}. Sidecars .quality.json gravados em {raw}/")
    return 0 if worst != "reprovado" else 1


if __name__ == "__main__":
    sys.exit(main())
