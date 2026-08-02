#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
migrar-espelho.py — promove a campo de frontmatter o que ja esta escrito na pagina.

PRD 2026-08-02, F4. As paginas `type: acordao` ja trazem tese, relator e orgao
julgador — mas em PROSA, no corpo:

    Rel. Min. Herman Benjamin; EDcl rejeitados em 16/03/2022
    **Tese:** "A repeticao em dobro, prevista no paragrafo unico do art. 42..."

Assim ninguem consulta "todos os acordaos da Quarta Turma" nem "relatados pelo
Min. X", e o `lint-bundle` nao tem o que conferir. O Espelho do Acordao do STJ
(Manual de Organizacao 2026, cap. 5) mantem esses dados em campos.

Esta migracao NAO INVENTA NADA: so move para o frontmatter o texto que ja
existe na pagina, e deixa em branco o que nao encontrar — o E6 continua
acusando, e o titular preenche. Campo ja presente nunca e sobrescrito.

Uso (stdlib apenas):
    python migrar-espelho.py                 # relata o que faria
    python migrar-espelho.py --aplicar       # grava
    python migrar-espelho.py --bundle direito/imobiliario --aplicar

Exit: 0 sempre que conseguir ler as paginas
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent

RX_FM = re.compile(r"\A---\n(.*?\n)---\n", re.S)

# "**Tese:**", "**Tese fixada:**", "**Tese fixada (redacao corrigida nos EDcl):**"
RX_TESE = re.compile(r"^\*\*Tese[^*\n]*:\*\*\s*(.+?)\s*$", re.M)

# "Rel. Min. Herman Benjamin" | "Relator Ministro Raul Araujo" | "Relatora Ministra X"
RX_RELATOR = re.compile(
    r"\bRel(?:\.|ator[a]?)\s+Min(?:\.|istr[oa])\s+([A-ZÀ-Ú][\wÀ-ÿ.'-]*(?:\s+(?:de|da|do|dos|das|e)?\s*[A-ZÀ-Ú][\wÀ-ÿ.'-]*){0,4})"
)

RX_ORGAO = re.compile(
    r"\b((?:Primeira|Segunda|Terceira|Quarta|Quinta|Sexta)\s+(?:Turma|Seção)|Corte Especial)\b"
)


def yaml_escalar(v: str) -> str:
    """Aspas simples com '' interno: sobrevive a dois-pontos, aspas e acento."""
    return "'" + v.replace("'", "''") + "'"


def campo_presente(fm: str, chave: str) -> bool:
    return re.search(rf"^{chave}:", fm, re.M) is not None


def extrair(texto: str, corpo: str) -> dict:
    achados: dict[str, str] = {}

    m = RX_TESE.search(corpo)
    if m:
        # A tese costuma vir entre aspas, as vezes seguida de comentario do
        # escritorio depois de travessao. Fica so o enunciado.
        t = m.group(1).strip()
        aspas = re.match(r'^["“](.+?)["”]', t)
        if aspas:
            t = aspas.group(1)
        else:
            t = re.split(r"\s+—\s+", t)[0]
        achados["tese"] = t.strip()

    # Relator e orgao sao procurados so no cabecalho da pagina (antes da primeira
    # secao "##"): mais abaixo vem a jurisprudencia citada, com OUTROS relatores.
    cabeca = corpo.split("\n## ", 1)[0]

    m = RX_RELATOR.search(cabeca)
    if m:
        nome = re.sub(r"\s+", " ", m.group(1)).strip(" .;,")
        achados["relator"] = f"Min. {nome}"

    m = RX_ORGAO.search(cabeca)
    if m:
        achados["orgao_julgador"] = m.group(1)

    return achados


def processar(p: Path, aplicar: bool) -> tuple[list[str], list[str]]:
    texto = p.read_text(encoding="utf-8")
    m = RX_FM.match(texto)
    if not m:
        return [], ["sem frontmatter"]

    fm, corpo = m.group(1), texto[m.end():]
    achados = extrair(texto, corpo)

    novos = {k: v for k, v in achados.items() if not campo_presente(fm, k)}
    faltando = [k for k in ("tese", "relator", "orgao_julgador") if k not in achados and not campo_presente(fm, k)]

    if novos and aplicar:
        linhas = [f"{k}: {yaml_escalar(v)}" for k, v in novos.items()]
        novo_fm = fm.rstrip("\n") + "\n" + "\n".join(linhas) + "\n"
        p.write_text(f"---\n{novo_fm}---\n{corpo}", encoding="utf-8")

    return [f"{k}={v[:70]}" for k, v in novos.items()], faltando


def main() -> int:
    ap = argparse.ArgumentParser(description="Promove tese/relator/orgao de prosa para frontmatter.")
    ap.add_argument("--bundle", help="restringe a um bundle")
    ap.add_argument("--aplicar", action="store_true", help="grava (default: so relata)")
    args = ap.parse_args()

    base = RAIZ if not args.bundle else (RAIZ / args.bundle)
    paginas = [
        p for p in base.rglob("*.md")
        if "raw" not in p.parts and ".git" not in p.parts
        and re.search(r"^type:\s*acordao\s*$", p.read_text(encoding="utf-8", errors="ignore")[:800], re.M)
    ]

    print(f"migrar-espelho: {len(paginas)} pagina(s) `type: acordao`"
          + ("" if args.aplicar else "  [SIMULACAO — use --aplicar para gravar]") + "\n")

    total_novos = 0
    pendentes: dict[str, int] = {}
    for p in sorted(paginas):
        novos, faltando = processar(p, args.aplicar)
        total_novos += len(novos)
        for f in faltando:
            pendentes[f] = pendentes.get(f, 0) + 1
        if novos or faltando:
            print(f"  {p.relative_to(base).as_posix()}")
            for n in novos:
                print(f"    + {n}")
            if faltando:
                print(f"    ? nao encontrado na pagina: {', '.join(faltando)}")

    print(f"\n{total_novos} campo(s) promovido(s).")
    if pendentes:
        print("Pendente de preenchimento pelo titular (o E6 segue acusando):")
        for k, n in sorted(pendentes.items(), key=lambda x: -x[1]):
            print(f"  {k}: {n} pagina(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
