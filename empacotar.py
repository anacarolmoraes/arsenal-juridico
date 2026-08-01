# -*- coding: utf-8 -*-
"""Empacota o arsenal-juridico para distribuição, aplicando distribuicao.json.

Uso (Python do adv_env, com PYTHONUTF8=1 no Windows):
    python empacotar.py --verificar     # só valida: manifesto vivo + nada suspeito fora dele
    python empacotar.py                 # verifica e gera dist/arsenal-juridico-<data>-<sha>.zip

Regra de ouro: distribuir é SEMPRE exportar por aqui. Nunca tornar o repositório
público nem espelhá-lo — o histórico git contém o material excluído.
"""
import argparse
import fnmatch
import json
import subprocess
import sys
import zipfile
from datetime import datetime
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
MANIFESTO = RAIZ / "distribuicao.json"

# Marcadores que denunciam material de uso interno dentro de um arquivo
MARCADORES = (
    "não distribuir",
    "uso interno",
    "Documento anonimizado",
    "Fonte de terceiro",
)


def arquivos_rastreados():
    saida = subprocess.run(
        ["git", "ls-files"], cwd=RAIZ, capture_output=True, text=True,
        encoding="utf-8", check=True,
    )
    return [linha for linha in saida.stdout.splitlines() if linha.strip()]


def carregar_manifesto():
    with open(MANIFESTO, encoding="utf-8") as f:
        return json.load(f)


def excluido(caminho, exclusoes):
    return any(fnmatch.fnmatch(caminho, e["glob"]) for e in exclusoes)


def verificar(manifesto, rastreados):
    """Valida o manifesto. Retorna lista de erros (vazia = ok)."""
    erros = []
    exclusoes = manifesto["exclusoes"]

    # 0. Camada 1: glob de .gitignore NÃO pode ter arquivo rastreado — se tem,
    #    alguém commitou obra de terceiro ou PDF de processo alheio.
    for e in manifesto.get("camada1_gitignore", []):
        vazou = [c for c in rastreados if fnmatch.fnmatch(c, e["glob"])]
        for c in vazou:
            erros.append(f"CAMADA 1 VIOLADA — rastreado no git: {c} ({e['motivo']})")

    # 1. Todo glob da camada 2 precisa casar com algo — glob morto é manifesto podre.
    for e in exclusoes:
        n = sum(1 for c in rastreados if fnmatch.fnmatch(c, e["glob"]))
        if n == 0:
            erros.append(f"glob sem correspondência (removido? renomeado?): {e['glob']}")

    # 2. Varredura de suspeitos: nada com cara de uso-interno pode ficar fora do manifesto.
    for c in rastreados:
        if excluido(c, exclusoes):
            continue
        p = RAIZ / c
        suspeito = None
        if c.endswith(".rtf"):
            suspeito = "arquivo .rtf (fonte bruta de obra de terceiro?)"
        elif p.name == "escritorio.md":
            suspeito = "escritorio.md (dado do escritório)"
        elif "/raw/" in c and c.endswith(".md"):
            try:
                inicio = p.read_text(encoding="utf-8", errors="ignore")[:600]
            except OSError:
                inicio = ""
            for m in MARCADORES:
                if m.lower() in inicio.lower():
                    suspeito = f"marcador '{m}' no topo do arquivo"
                    break
        if suspeito:
            erros.append(f"fora do manifesto mas parece uso interno: {c} — {suspeito}")

    return erros


def empacotar(manifesto, rastreados):
    exclusoes = manifesto["exclusoes"]
    incluir = [c for c in rastreados if not excluido(c, exclusoes)]
    fora = len(rastreados) - len(incluir)

    sha = subprocess.run(
        ["git", "rev-parse", "--short", "HEAD"], cwd=RAIZ, capture_output=True,
        text=True, encoding="utf-8", check=True,
    ).stdout.strip()
    destino = RAIZ / "dist"
    destino.mkdir(exist_ok=True)
    nome = f"arsenal-juridico-{datetime.now():%Y%m%d}-{sha}.zip"
    alvo = destino / nome

    with zipfile.ZipFile(alvo, "w", zipfile.ZIP_DEFLATED) as z:
        for c in incluir:
            z.write(RAIZ / c, arcname=c)

    print(f"pacote: {alvo}")
    print(f"arquivos incluídos: {len(incluir)}  |  excluídos pelo manifesto: {fora}")
    return alvo


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--verificar", action="store_true",
                    help="só valida o manifesto, não gera pacote")
    args = ap.parse_args()

    manifesto = carregar_manifesto()
    rastreados = arquivos_rastreados()
    erros = verificar(manifesto, rastreados)
    if erros:
        print(f"MANIFESTO REPROVADO — {len(erros)} problema(s):", file=sys.stderr)
        for e in erros:
            print(f"  ERRO  {e}", file=sys.stderr)
        return 1
    print(f"manifesto ok: {len(manifesto['exclusoes'])} regra(s), "
          f"{sum(1 for c in rastreados if excluido(c, manifesto['exclusoes']))} arquivo(s) retidos.")
    if manifesto.get("pendencias"):
        for p in manifesto["pendencias"]:
            print(f"  PENDÊNCIA: {p}")

    if not args.verificar:
        empacotar(manifesto, rastreados)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
