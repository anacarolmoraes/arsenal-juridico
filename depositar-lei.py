#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
depositar-lei.py — Etapa 0 para texto de lei: converte o HTML oficial do
Planalto e deposita o par .html + .md no raw/ do bundle, com proveniencia.

POR QUE UM SCRIPT, E NAO CONVERSAO NA UNHA
------------------------------------------
Duas armadilhas ja corromperam deposito neste acervo, e as duas sao
silenciosas — nao dao erro, produzem texto errado:

1. ENCODING. O HTML do Planalto e cp1252. Decodificado como UTF-8, todo
   acento vira lixo ("execu��o") sem que nada falhe.
2. TEXTO REVOGADO. O Planalto marca a redacao superada com <strike>. Achatar
   as tags apresenta REVOGADO COMO VIGENTE — na Lei 6.830/80 o art. 16, II
   aparecia em duas versoes sem indicar qual valia.

Este script trata as duas e recusa o deposito quando nao consegue decidir.

USO
    python depositar-lei.py <html> <bundle> --slug lei-8009-1990-bem-de-familia
    python depositar-lei.py consumir/L8009.html direito/execucao/defesa-executado \\
        --slug lei-8009-1990-bem-de-familia --nome "Lei 8.009/1990 — bem de familia"

Exit: 0 depositado | 1 erro
"""
from __future__ import annotations

import argparse
import html as H
import io
import re
import shutil
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
# So palavras COM acento servem de prova: uma palavra sem acento ("artigo")
# passa mesmo em texto mojibake, e o latin-1 — que decodifica qualquer byte —
# viraria vencedor silencioso de arquivo UTF-8 (foi o que corrompeu o primeiro
# deposito da Lei 15.484, vinda do DOU em UTF-8, nao do Planalto em cp1252).
ACENTUADAS = ("execução", "prescrição", "não", "disposições", "família", "publicação", "questão")


def decodificar(bruto: bytes) -> tuple[str, str]:
    """Escolhe o encoding pela presenca de palavra portuguesa acentuada."""
    for enc in ("cp1252", "latin-1", "utf-8"):
        try:
            s = bruto.decode(enc)
        except UnicodeDecodeError:
            continue
        if any(p in s.lower() for p in ACENTUADAS):
            return s, enc
    raise SystemExit("ERRO: nao foi possivel decodificar com acentuacao valida (cp1252/latin-1/utf-8).")


def marcar_revogado(raw: str) -> tuple[str, int]:
    """Preserva o texto riscado com rotulo explicito, antes de achatar as tags."""
    n = len(re.findall(r"(?i)<strike[\s>]", raw))

    def rep(m):
        dentro = re.sub(r"(?s)<[^>]+>", " ", m.group(1))
        dentro = " ".join(H.unescape(dentro).split())
        return f"\n[REVOGADO — NAO CITAR] {dentro}\n" if dentro else ""

    return re.sub(r"(?is)<strike[^>]*>(.*?)</strike>", rep, raw), n


def limpar(raw: str) -> str:
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", raw)
    t = re.sub(r"(?i)<br\s*/?>|</p\s*>|</div\s*>|</tr\s*>|</h[1-6]\s*>", "\n", t)
    t = re.sub(r"(?s)<[^>]+>", "", t)
    t = H.unescape(t).replace("\xa0", " ")
    t = re.sub(r"@media print\{[^}]*\}", "", t)            # css do salvamento
    t = re.sub(r"\[data-[a-z-]+[^\]]*\][^\n]*", "", t)      # extensao de navegador
    t = re.sub(r"[ \t]{2,}", " ", t)
    t = "\n".join(l.strip() for l in t.splitlines())
    return re.sub(r"\n{3,}", "\n\n", t).strip()


def cobertura(t: str) -> str:
    """Maior lei alteradora citada — e o que diz a validade do deposito."""
    nums = re.findall(r"Lei\s+(?:Complementar\s+)?n?[ºo°]?\s*(\d{1,2}\.\d{3})", t)
    if not nums:
        return "nao identificada"
    def chave(n):
        a, b = n.split(".")
        return (int(a), int(b))
    return max(set(nums), key=chave)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("html", help="HTML oficial do Planalto")
    ap.add_argument("bundle", help="bundle destino, relativo a raiz do acervo")
    ap.add_argument("--slug", required=True, help="nome do par depositado, sem extensao")
    ap.add_argument("--nome", default="", help="nome legivel da lei, para o cabecalho")
    ap.add_argument("--motivo", default="", help="por que este bundle recebe o deposito")
    args = ap.parse_args()

    src = Path(args.html)
    if not src.is_absolute():
        src = Path.cwd() / src
    if not src.exists() or src.stat().st_size == 0:
        print(f"ERRO: fonte ausente ou vazia: {src}", file=sys.stderr)
        return 1

    dst_dir = RAIZ / args.bundle / "raw"
    if not (RAIZ / args.bundle).exists():
        print(f"ERRO: bundle inexistente: {args.bundle}", file=sys.stderr)
        return 1
    dst_dir.mkdir(exist_ok=True)

    if src.suffix.lower() == ".pdf":
        # Norma publicada so em PDF (resolucao de conselho, por exemplo). O pdfmd
        # converte; aqui so se exige o par .md ja gerado, para nao esconder a
        # conversao dentro deste script e poder conferi-la antes.
        par = src.with_suffix(".md")
        if not par.exists():
            print(f"ERRO: converta antes com o pdfmd e deixe o par ao lado: {par.name}", file=sys.stderr)
            return 1
        texto = limpar(io.open(par, encoding="utf-8").read())
        # marcador de pagina do pdfmd nao e texto da norma
        texto = re.sub(r"<a id=\"pdf-page-\d+\"></a>\s*", "", texto)
        texto = re.sub(r"<!--\s*pdfmd:[^>]*-->\s*", "", texto)
        enc, n_strike = "pdf/pdfmd", 0
        raw = texto
    else:
        bruto = src.read_bytes()
        raw, enc = decodificar(bruto)
        raw, n_strike = marcar_revogado(raw)
        texto = limpar(raw)
    cob = cobertura(texto)
    # "Art. 1.911" tem separador de milhar: sem tratar, o contador leria artigo 1
    arts = sorted({int(m.replace(".", "")) for m in re.findall(r"\bArt\.\s*(\d{1,3}(?:\.\d{3})*)", texto)})

    aviso_strike = (
        f"ATENCAO — TEXTO REVOGADO MARCADO: o HTML usa <strike> em {n_strike} trecho(s) para a\n"
        f"redacao superada. A conversao os preserva com o rotulo [REVOGADO — NAO CITAR].\n"
        if n_strike else
        "Verificado: o HTML nao usa <strike>; nao ha redacao superada embutida no texto.\n"
    )
    cab = (
        "<!--\n"
        f"{args.nome or args.slug} — texto do Planalto. Deposito integral e IMUTAVEL.\n"
        f"Convertido de {src.name} (encoding {enc}) por depositar-lei.py.\n"
        "TEXTO DE LEI CIRCULA: nao e obra protegida (Lei 9.610/98, art. 8, IV).\n"
        f"COBERTURA: cita alteracoes ate a Lei {cob}. Nada posterior esta refletido.\n"
        f"{aviso_strike}"
        f"{('MOTIVO DO DEPOSITO NESTE BUNDLE: ' + args.motivo + chr(10)) if args.motivo else ''}"
        "NAO editar. E a fonte contra a qual o lint-citacoes confere transcricao.\n"
        "Recortes por artigo: python recortar-artigo.py <artigo> <bundle> --codigo <este .md>\n"
        "-->\n\n"
    )
    shutil.copy2(src, dst_dir / f"{args.slug}{src.suffix}")
    io.open(dst_dir / f"{args.slug}.md", "w", encoding="utf-8", newline="\n").write(cab + texto + "\n")

    residuo = [p for p in ("@media", "data-glasp", "<p", "<div", "&nbsp", "pdfmd:") if p in texto]
    # Ordinal perdido: "Art. 1" em vez de "Art. 1o". Acontece em conversao de PDF,
    # porque o indicador ordinal e sobrescrito. Nao corrompe o sentido, mas quebra
    # a conferencia literal — quem transcrever precisa declarar a normalizacao.
    sem_ordinal = re.findall(r"\bArt\.\s*([1-9])(?![0-9º°o.\-])", texto)
    print(f"ok {args.bundle}/raw/{args.slug}.md")
    print(f"   fonte={enc} | {len(texto)} chars | artigos {arts[0] if arts else '?'}-{arts[-1] if arts else '?'} ({len(arts)})")
    print(f"   cobertura=Lei {cob} | strike={n_strike} | residuo={residuo or 'nenhum'}")
    if sem_ordinal:
        print(f"   AVISO: {len(sem_ordinal)} artigo(s) de 1 a 9 sem indicador ordinal "
              f"(ex.: 'Art. {sem_ordinal[0]}' em vez de 'Art. {sem_ordinal[0]}o'). "
              f"Declarar a normalizacao na pagina derivada.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
