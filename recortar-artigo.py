#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
recortar-artigo.py — extrai o texto literal de um artigo do codigo depositado
em direito/pecas/raw/ e grava um recorte no raw/ do bundle que vai cita-lo.

POR QUE ISSO EXISTE
-------------------
O CPC inteiro e fonte transversal: serve a quase todos os bundles. Depositar
o codigo completo em cada raw/ duplicaria megabytes e violaria a regra de nao
repetir fonte canonica. Mas o lint-citacoes confere a transcricao contra um
arquivo do PROPRIO bundle, e o E4 do lint-bundle exige deposito para promover
pagina a `vigente`.

A solucao e a que este script implementa: o codigo integral mora uma vez em
direito/pecas/raw/; cada bundle recebe o RECORTE do artigo que cita, com
cabecalho de proveniencia apontando para o integral.

USO
    python recortar-artigo.py 921 direito/execucao/defesa-executado
    python recortar-artigo.py 381-383 direito/execucao/credor
    python recortar-artigo.py 921 direito/execucao/defesa-executado --codigo cpc-...md

Gera: <bundle>/raw/cpc-art-921.md  (ou cpc-arts-381-383.md)

Exit: 0 recorte gravado | 1 erro (fonte ausente, artigo nao localizado)
"""
from __future__ import annotations

import argparse
import io
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
CODIGO_PADRAO = RAIZ / "direito" / "pecas" / "raw" / "cpc-l13105-compilada.md"

# Cabecalho de artigo: "Art. 921." com A MAIUSCULO e ponto depois do numero.
# O maiusculo + ponto e o que distingue o artigo em si das remissoes internas,
# que a lei escreve em minusculo ("nos termos do art. 921", "arts. 313 e 315").
# Nao ancorar em inicio de linha: a conversao as vezes cola o cabecalho do
# capitulo na mesma linha do artigo ("CAPITULO I ... Art. 921. Suspende-se...").
def rx_artigo(n: str) -> re.Pattern:
    num = re.escape(n)
    return re.compile(rf"\bArt\.\s*{num}(-[A-Z])?\.")


def achar_inicio(texto: str, n: str) -> int:
    m = rx_artigo(n).search(texto)
    if not m:
        return -1
    return m.start()


def achar_fim(texto: str, inicio: int, ultimo: str) -> int:
    """Fim = inicio do proximo artigo depois de `ultimo` (921 -> 922, 923...)."""
    base = int(re.match(r"\d+", ultimo).group())
    for prox in range(base + 1, base + 12):  # tolera lacunas por revogacao
        m = rx_artigo(str(prox)).search(texto, inicio + 1)
        if m:
            return m.start()
    return len(texto)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("artigo", help="numero do artigo, ou faixa: 921 | 381-383")
    ap.add_argument("bundle", help="caminho do bundle destino, relativo a raiz do acervo")
    ap.add_argument("--codigo", default=str(CODIGO_PADRAO), help="markdown do codigo integral")
    ap.add_argument("--rotulo", default="CPC", help="sigla do codigo (default: CPC)")
    args = ap.parse_args()

    fonte = Path(args.codigo)
    if not fonte.is_absolute():
        fonte = RAIZ / fonte
    if not fonte.exists():
        print(f"ERRO: codigo integral nao encontrado em {fonte}", file=sys.stderr)
        print("      Deposite o PDF oficial e converta com pdfmd antes de recortar.", file=sys.stderr)
        return 1

    destino_dir = (RAIZ / args.bundle / "raw")
    if not destino_dir.parent.exists():
        print(f"ERRO: bundle inexistente: {args.bundle}", file=sys.stderr)
        return 1
    destino_dir.mkdir(exist_ok=True)

    texto = io.open(fonte, encoding="utf-8").read()

    if "-" in args.artigo:
        primeiro, ultimo = args.artigo.split("-", 1)
        nome = f"{args.rotulo.lower()}-arts-{primeiro}-{ultimo}.md"
        titulo = f"{args.rotulo}, arts. {primeiro} a {ultimo}"
    else:
        primeiro = ultimo = args.artigo
        nome = f"{args.rotulo.lower()}-art-{primeiro}.md"
        titulo = f"{args.rotulo}, art. {primeiro}"

    ini = achar_inicio(texto, primeiro)
    if ini < 0:
        print(f"ERRO: art. {primeiro} nao localizado em {fonte.name}.", file=sys.stderr)
        print("      Conferir a qualidade da conversao antes de insistir.", file=sys.stderr)
        return 1
    fim = achar_fim(texto, ini, ultimo)
    recorte = texto[ini:fim].rstrip()

    try:
        origem = fonte.relative_to(RAIZ).as_posix()
    except ValueError:  # fonte fora do acervo (teste, deposito temporario)
        origem = fonte.as_posix()

    cabecalho = (
        f"<!--\n"
        f"RECORTE AUTOMATICO — nao editar a mao.\n"
        f"Gerado por recortar-artigo.py a partir de {origem},\n"
        f"que e o deposito integral e imutavel do codigo. Este arquivo existe para que o\n"
        f"lint-citacoes confira a transcricao dentro deste bundle sem duplicar o codigo.\n"
        f"Para atualizar apos nova versao do codigo: regerar, nunca corrigir aqui.\n"
        f"-->\n\n"
        f"# {titulo}\n\n"
    )
    saida = destino_dir / nome
    io.open(saida, "w", encoding="utf-8", newline="\n").write(cabecalho + recorte + "\n")
    linhas = recorte.count("\n") + 1
    print(f"ok: {saida.relative_to(RAIZ).as_posix()} ({len(recorte)} chars, {linhas} linhas)")
    print("--- primeiras linhas do recorte, confira antes de citar:")
    for l in recorte.splitlines()[:6]:
        print("   ", l[:110])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
