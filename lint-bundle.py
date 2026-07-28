#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lint-bundle.py — verificacao estrutural dos bundles OKF.

PRD F2.1. Substitui o lint-links.py (que fazia so E2, e morava no
KnowledgeOperatingSystem, fora do que fiscalizava).

Checagens:
  E1  toda pagina de conteudo tem frontmatter com `type` e `status`
  E2  todo link relativo resolve
  E3  toda pagina aparece em algum index.md
  E4  toda pagina `status: vigente` de jurisprudencia/teses tem fonte oficial em raw/
  W1  paginas orfas (nenhuma outra pagina de conteudo as referencia)
  W2  `status` fora do vocabulario (vigente | em_teste | superada)

E4 e o que importa: `status` sem fonte depositada e etiqueta, nao garantia.
Sem essa checagem, uma pagina "vigente" pode nunca ter sido conferida.

Uso (stdlib apenas, sem dependencias):
    python lint-bundle.py                      # todos os bundles sob a raiz
    python lint-bundle.py direito/imobiliario  # um bundle
    python lint-bundle.py --quiet              # so erros e avisos
    python lint-bundle.py --errors-only

Exit: 0 = sem erros | 1 = ha erro
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent

RESERVADOS = {"index.md", "log.md", "README.md", "atividades.md", "escritorio.md", "roadmap.md"}
IGNORAR_DIR = {".git", "node_modules", "__pycache__", ".claude", "skills"}

# Pastas cujo conteudo e citavel numa peca e portanto exige fonte oficial em raw/.
PASTAS_CITAVEIS = {"jurisprudencia", "jurisprudencia_stj", "teses"}
STATUS_VALIDOS = {"vigente", "em_teste", "superada", "rascunho"}

RX_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
RX_FENCE = re.compile(r"```.*?```", re.DOTALL)
RX_INLINE = re.compile(r"`[^`]*`")

achados: list[tuple[str, str, str, str]] = []  # (sev, check, arquivo, detalhe)


def add(sev, check, arq, detalhe):
    achados.append((sev, check, arq, detalhe))


def limpar_codigo(t: str) -> str:
    """Remove blocos e trechos de codigo: link de exemplo em doc nao e link real."""
    return RX_INLINE.sub("", RX_FENCE.sub("", t))


def frontmatter(t: str) -> str | None:
    if not t.startswith("---"):
        return None
    fim = t.find("\n---", 3)
    return t[3:fim] if fim != -1 else None


def campo(fm: str, chave: str) -> str | None:
    m = re.search(rf"^{chave}:\s*(.+)$", fm, re.M)
    return m.group(1).strip().strip("\"'") if m else None


def bundles_sob(raiz: Path) -> list[Path]:
    """Um bundle e um diretorio com index.md e ao menos uma pasta de conteudo."""
    encontrados = []
    for idx in raiz.rglob("index.md"):
        if any(p in IGNORAR_DIR for p in idx.parts):
            continue
        d = idx.parent
        if any((d / p).is_dir() for p in PASTAS_CITAVEIS | {"heuristicas", "playbooks", "casos_decididos"}):
            encontrados.append(d)
    # remove aninhados (mantem o mais externo que ja cobre o interno)
    return [b for b in encontrados if not any(b != o and o in b.parents for o in encontrados)]


def paginas(bundle: Path) -> list[Path]:
    out = []
    for p in bundle.rglob("*.md"):
        if any(x in IGNORAR_DIR for x in p.relative_to(bundle).parts):
            continue
        out.append(p)
    return out


def verificar(bundle: Path) -> None:
    rotulo = bundle.relative_to(RAIZ) if RAIZ in bundle.parents or bundle == RAIZ else bundle
    todas = paginas(bundle)
    conteudo = [p for p in todas if p.name not in RESERVADOS]

    # indice invertido de links
    entrada: dict[Path, set[Path]] = {}
    alvos_de_indices: set[Path] = set()

    for p in todas:
        try:
            texto = p.read_text(encoding="utf-8")
        except Exception as e:
            add("error", "ilegivel", str(p.relative_to(bundle)), f"Nao foi possivel ler: {e}")
            continue

        # raw/ e camada de DEPOSITO, nao de conhecimento: e o alvo do E4, nao seu sujeito.
        # Exigir frontmatter e indexacao ali seria ruido — o valor de raw/ e ser
        # transcricao imutavel da fonte oficial. Vale para raw/ em qualquer nivel
        # (ha bundles com raw por sub-tema, ex.: pecas/recurso-especial/raw/).
        em_raw = "raw" in p.relative_to(bundle).parts

        # E1 — frontmatter
        if p.name not in RESERVADOS and not em_raw:
            fm = frontmatter(texto)
            if fm is None:
                add("error", "E1-sem-frontmatter", str(p.relative_to(bundle)), "Sem frontmatter YAML.")
            else:
                if not campo(fm, "type"):
                    add("error", "E1-sem-type", str(p.relative_to(bundle)), "Frontmatter sem `type`.")
                st = campo(fm, "status")
                if not st:
                    add("error", "E1-sem-status", str(p.relative_to(bundle)), "Frontmatter sem `status` — a pagina nao declara se foi conferida.")
                elif st not in STATUS_VALIDOS:
                    add("warning", "W2-status-invalido", str(p.relative_to(bundle)), f"`status: {st}` fora do vocabulario {sorted(STATUS_VALIDOS)}.")

        # E2 — links. Nao se lintam links dentro de raw/: sao transcricoes de PDF por
        # OCR, onde colchetes e parenteses do texto original viram falso link.
        for bruto in ([] if em_raw else RX_LINK.findall(limpar_codigo(texto))):
            link = bruto.split()[0].split("#", 1)[0]
            if not link or link.startswith(("http://", "https://", "mailto:")):
                continue
            base = bundle if link.startswith("/") else p.parent
            destino = (base / link.lstrip("/")).resolve()
            if not destino.exists():
                add("error", "E2-link-quebrado", str(p.relative_to(bundle)), f"Link `{link}` nao resolve.")
                continue
            if destino.suffix == ".md":
                if p.name == "index.md":
                    alvos_de_indices.add(destino)
                else:
                    entrada.setdefault(destino, set()).add(p)

    # E3 — cobertura de indice
    for p in conteudo:
        if "raw" in p.relative_to(bundle).parts:
            continue
        if p.resolve() not in alvos_de_indices:
            add("error", "E3-fora-do-indice", str(p.relative_to(bundle)), "Nao aparece em nenhum index.md — existe no disco e nao existe para o agente.")

    # E4 — lastro documental, com severidade proporcional ao risco de fabricacao
    raw = bundle / "raw"
    stems_raw = set()
    if raw.is_dir():
        stems_raw = {f.stem.lower() for f in raw.iterdir() if f.is_file()}

    for p in conteudo:
        partes = p.relative_to(bundle).parts
        if not partes or partes[0] not in PASTAS_CITAVEIS:
            continue
        try:
            texto = p.read_text(encoding="utf-8")
        except Exception:
            continue
        fm = frontmatter(texto) or ""
        tipo = campo(fm, "type") or ""
        if campo(fm, "status") != "vigente":
            continue

        tem_raw = p.stem.lower() in stems_raw or "raw/" in texto or "(raw)" in texto

        if tipo in ("acordao", "sumula") and not tem_raw:
            # Ementa e texto longo, especifico e facil de fabricar de forma plausivel.
            # Sem o inteiro teor depositado nao ha como o lint-citacoes conferir a
            # transcricao — e e justamente ai que mora o dano irreversivel.
            add("error", "E4-sem-inteiro-teor", str(p.relative_to(bundle)),
                f"`type: {tipo}` marcado `vigente` sem inteiro teor em raw/. Sem deposito, nenhuma transcricao dele pode ser verificada.")
        elif tipo == "legislacao" and not tem_raw:
            # Texto de lei e curto, estavel e conferivel em fonte publica: o risco de
            # fabricacao nao verificavel e baixo. Aviso, nao erro.
            add("warning", "W3-lei-sem-deposito", str(p.relative_to(bundle)),
                "`type: legislacao` marcado `vigente` sem transcricao oficial depositada em raw/ (conferir contra o Planalto).")

    # E5 — tese sem fundamento: sintese do escritorio precisa apontar para a fonte
    for p in conteudo:
        partes = p.relative_to(bundle).parts
        if not partes or partes[0] != "teses":
            continue
        try:
            texto = p.read_text(encoding="utf-8")
        except Exception:
            continue
        if (campo(frontmatter(texto) or "", "type") or "") != "tese":
            continue
        aponta = False
        for bruto in RX_LINK.findall(limpar_codigo(texto)):
            link = bruto.split()[0].split("#", 1)[0]
            if link.startswith(("http", "mailto")):
                continue
            base = bundle if link.startswith("/") else p.parent
            alvo = (base / link.lstrip("/")).resolve()
            if alvo.exists() and alvo.suffix == ".md":
                fm_alvo = frontmatter(alvo.read_text(encoding="utf-8")) or ""
                if (campo(fm_alvo, "type") or "") in ("acordao", "sumula", "legislacao"):
                    aponta = True
                    break
        if not aponta:
            add("error", "E5-tese-sem-fundamento", str(p.relative_to(bundle)),
                "Tese nao aponta para nenhum acordao, sumula ou legislacao do bundle — sintese sem fundamento rastreavel.")

    # W1 — orfas
    for p in conteudo:
        if not entrada.get(p.resolve()):
            add("warning", "W1-orfa", str(p.relative_to(bundle)), "Nenhuma pagina de conteudo aponta para ela (so o indice, no maximo).")

    print(f"  {rotulo}: {len(todas)} arquivos ({len(conteudo)} de conteudo)")


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    quiet = "--quiet" in sys.argv
    errors_only = "--errors-only" in sys.argv

    alvos = [Path(a).resolve() for a in args] if args else bundles_sob(RAIZ)
    if not alvos:
        print("Nenhum bundle encontrado.")
        return 0

    print(f"lint-bundle: {len(alvos)} bundle(s)\n")
    for b in alvos:
        verificar(b)
    print()

    erros = [a for a in achados if a[0] == "error"]
    avisos = [a for a in achados if a[0] == "warning"]
    mostrar = erros if errors_only else (erros + avisos if quiet else achados)

    rotulo = {"error": "ERRO ", "warning": "AVISO", "suggestion": "SUGER"}
    for sev in ("error", "warning", "suggestion"):
        grupo = [a for a in mostrar if a[0] == sev]
        for _, check, arq, det in grupo:
            print(f"  {rotulo[sev]} [{check}] {arq}")
            print(f"        {det}")
        if grupo:
            print()

    print(f"{len(erros)} erro(s), {len(avisos)} aviso(s).")
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(main())
