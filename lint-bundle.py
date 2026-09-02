#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lint-bundle.py — verificacao estrutural dos bundles OKF.

PRD F2.1. Substitui o lint-links.py (que fazia so E2, e morava no
KnowledgeOperatingSystem, fora do que fiscalizava).

Checagens:
  E1  toda pagina de conteudo tem frontmatter com `type` e `status`
  E2  toda referencia a arquivo resolve (link do corpo E campo de frontmatter)
  E3  toda pagina aparece em algum index.md
  E4  toda pagina `status: vigente` de jurisprudencia/teses tem fonte oficial em raw/
  E5  toda tese aponta para acordao, sumula ou legislacao do bundle
  E6  acordao cumpre o schema do Espelho do Acordao (0.5)
  W1  paginas orfas (nenhuma outra pagina de conteudo as referencia)
  W2  `status` fora do vocabulario (vigente | em_teste | superada | rascunho)
  W3  `type: legislacao` vigente sem transcricao oficial em raw/

E4 e o que importa: `status` sem fonte depositada e etiqueta, nao garantia.
Sem essa checagem, uma pagina "vigente" pode nunca ter sido conferida.

O GRAFO tem tres formas de aresta, e o lint le as tres (2026-08-29):
  1. link markdown no corpo          [texto](/jurisprudencia/x.md)
  2. campo de frontmatter            fundamentos: / raw: / playbook: / casos_origem:
  3. caminho absoluto nu no corpo    - **Workflow:** /workflows/x.md
Ler so a forma 1, como era ate aqui, produzia painel majoritariamente falso: 17 de 17
E5 e 307 de 336 W1 eram falso positivo. Portao que grita errado nao e obedecido — e
desligado. Ver `refs_frontmatter`, `RX_CAMINHO_NU` e a nota do W1 sobre raw/.

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

# O grafo do acervo NAO mora so no corpo. Campos de frontmatter como `fundamentos:`,
# `casos_origem:`, `raw:` e `playbook:` sao arestas de verdade — e eram invisiveis para
# o lint, que so lia RX_LINK. Consequencia medida em 2026-08-29: 17 de 17 E5 e 268 de
# 317 W1 eram FALSO POSITIVO. Painel majoritariamente falso nao vira portao: e abandonado.
#
# A deteccao e por RESOLUCAO, nao por lista de campos: um valor so vira aresta se apontar
# para arquivo existente. Assim campo novo entra no grafo sozinho, sem manutencao aqui, e
# `title:` ou `description:` que por acaso contenham ".md" nao criam aresta falsa.
RX_FM_ESCALAR = re.compile(r"^([a-z_]+):[ \t]*(\S.*)$", re.M)
RX_FM_LISTA = re.compile(r"^([a-z_]+):[ \t]*\n((?:[ \t]*-[ \t]*.+\n?)+)", re.M)
RX_FM_ITEM = re.compile(r"-[ \t]*(.+)")

# Terceira forma de aresta, mesma familia: caminho ABSOLUTO nu no corpo, fora de link
# markdown. E a convencao do `atividades.md` ("- **Workflow:** /workflows/x.md") e de
# varios index.md — 317 arestas reais que o lint nao via.
#
# Caminho nu SO ACRESCENTA aresta quando resolve; nunca vira E2. A assimetria e
# deliberada: prosa que menciona pagina ainda nao escrita e plano, nao link quebrado.
RX_CAMINHO_NU = re.compile(r"(?<!\()(?<!\[)(/[A-Za-z0-9._\-/]+\.md)\b")

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


def refs_frontmatter(fm: str) -> list[tuple[str, str]]:
    """Pares (campo, valor) do frontmatter que parecem apontar para arquivo do bundle.

    Cobre as duas formas em uso no acervo:
        raw: /raw/resp-2106548-sp.md          (escalar)
        fundamentos:                          (lista)
          - /jurisprudencia/sumula-543-stj.md
    """
    out: list[tuple[str, str]] = []
    for m in RX_FM_ESCALAR.finditer(fm):
        out.append((m.group(1), m.group(2)))
    for m in RX_FM_LISTA.finditer(fm):
        for item in RX_FM_ITEM.findall(m.group(2)):
            out.append((m.group(1), item))

    limpos = []
    for chave, bruto in out:
        v = bruto.strip().strip("\"'")
        if not v or v.startswith(("http://", "https://", "mailto:")):
            continue
        # Um caminho aqui e sempre absoluto-ao-bundle ou traz extensao de arquivo.
        if v.startswith("/") or v.endswith((".md", ".pdf", ".html", ".json")):
            limpos.append((chave, v))
    return limpos


def resolver_ref(bundle: Path, pagina: Path, valor: str) -> Path | None:
    """Resolve referencia a arquivo, na mesma convencao dos links do corpo.

    `/` significa raiz do bundle; qualquer outra coisa e relativa a pagina. Uma
    referencia a `.pdf` tambem aceita o `.md` irmao: o par PDF+transcricao e a
    convencao de deposito de `raw/`, e quem cita costuma apontar para o PDF.
    """
    rel = valor.split("#", 1)[0].strip()
    if not rel:
        return None
    base = bundle if rel.startswith("/") else pagina.parent
    alvo = (base / rel.lstrip("/")).resolve()
    if alvo.exists():
        return alvo
    irmao = alvo.with_suffix(".md")
    return irmao if irmao.exists() else None


# Dominio dos campos do Espelho do Acordao (schema 0.5). Modelo: o Manual de
# Organizacao do STJ 2026, cap. 5 — a base de Espelhos mantem tese, referencia
# legislativa e jurisprudencia citada em campos SEPARADOS, porque citacao nao e
# tese. `natureza` vem da Secao de Triagem: so o acordao PRINCIPAL recebe leitura
# de inteiro teor; o similar aponta para ele.
NATUREZA_VALIDA = {"principal", "similar"}
FONTE_TESE_VALIDA = {"ementa", "voto", "dispositivo"}


def conferir_deposito(bundle: Path, pagina: Path, fm: str, stems_raw: set[str]) -> tuple[bool, str]:
    """
    O E4 exigia apenas que a substring "raw/" aparecesse em algum lugar do texto
    — um comentario, um link quebrado ou uma frase em prosa satisfaziam o portao
    mais importante do acervo. Agora o deposito precisa EXISTIR.

    Ordem: o `raw:` declarado no frontmatter manda; na falta dele, aceita-se
    deposito de mesmo nome em raw/, que e a convencao das paginas antigas.
    """
    declarado = campo(fm, "raw")
    if declarado:
        rel = declarado.strip().lstrip("/")
        alvos = [bundle / rel, pagina.parent / rel]
        achado = next((a for a in alvos if a.exists()), None)
        if not achado:
            # Muitas paginas apontam para o PDF oficial e a conversao .md fica ao lado.
            achado = next((a.with_suffix(".md") for a in alvos if a.with_suffix(".md").exists()), None)
        if not achado:
            return False, f"`raw: {declarado}` nao resolve para arquivo existente."

        # O schema 7.1 manda ler o veredito do sidecar antes do conteudo. Deposito
        # reprovado na Etapa 0 nao serve de lastro para nada.
        quality = achado.with_suffix(achado.suffix + ".quality.json")
        if not quality.exists():
            quality = achado.with_suffix(".quality.json")
        if quality.exists():
            try:
                import json
                veredito = str(json.loads(quality.read_text(encoding="utf-8")).get("veredito", "")).lower()
            except Exception:
                veredito = ""
            if veredito == "reprovado":
                return False, f"deposito `{declarado}` existe, mas o `.quality.json` o marca REPROVADO."
        return True, ""

    if pagina.stem.lower() in stems_raw:
        return True, ""
    return False, "sem campo `raw:` no frontmatter e sem arquivo de mesmo nome em raw/."


def conferir_espelho(fm: str, texto: str) -> list[str]:
    """Campos que o acordao precisa declarar para ser consultavel, nao so legivel."""
    erros = []

    nat = campo(fm, "natureza")
    if nat and nat not in NATUREZA_VALIDA:
        erros.append(f"`natureza: {nat}` fora do vocabulario {sorted(NATUREZA_VALIDA)}.")

    ft = campo(fm, "fonte_da_tese")
    if ft and ft not in FONTE_TESE_VALIDA:
        erros.append(f"`fonte_da_tese: {ft}` fora do vocabulario {sorted(FONTE_TESE_VALIDA)}.")

    # A tese e o campo que torna a pagina consultavel. Enquanto morar em negrito
    # no corpo ("**Tese:**"), nao e indexavel nem lintavel.
    if campo(fm, "status") == "vigente" and not campo(fm, "tese"):
        erros.append("`status: vigente` sem campo `tese:` — o enunciado precisa estar no frontmatter, "
                     "nao apenas em negrito no corpo, para ser consultavel e conferivel.")

    # `jurisprudencia_citada` guarda o que o acordao CITA. Se listar o proprio
    # processo, a separacao entre tese e citacao se perdeu — que e exatamente o
    # defeito que o Espelho existe para evitar.
    proprio = campo(fm, "title") or ""
    citada = campo(fm, "jurisprudencia_citada") or ""
    for num in re.findall(r"\d[\d.]{4,}", proprio):
        if num in citada:
            erros.append(f"`jurisprudencia_citada` inclui o proprio julgado ({num}): "
                         "citacao e tese sao campos distintos.")
            break
    return erros


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

    # indice invertido de links (quem aponta para quem) e o direto (quem cada pagina cita)
    entrada: dict[Path, set[Path]] = {}
    saida: dict[Path, set[Path]] = {}
    alvos_de_indices: set[Path] = set()

    def registrar_aresta(origem: Path, destino: Path) -> None:
        """Uma aresta so conta como 'alguem me cita' se nao vier de index.md.

        O W1 existe para achar pagina que so o indice alcanca — contar o indice
        como citacao apagaria justamente o que ele mede.
        """
        if destino.suffix != ".md":
            return
        saida.setdefault(origem.resolve(), set()).add(destino)
        if origem.name == "index.md":
            alvos_de_indices.add(destino)
        else:
            entrada.setdefault(destino, set()).add(origem)

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
            registrar_aresta(p, destino)

        # Caminho absoluto nu no corpo (convencao do atividades.md e dos index.md).
        for nu in ([] if em_raw else RX_CAMINHO_NU.findall(limpar_codigo(texto))):
            destino = (bundle / nu.lstrip("/")).resolve()
            if destino.exists():
                registrar_aresta(p, destino)

        # Arestas do FRONTMATTER — `fundamentos:`, `casos_origem:`, `raw:`, `playbook:`
        # e o que mais vier. Sem isto o grafo do acervo fica pela metade e o W1/E5
        # acusam pagina bem fundamentada de orfa (ver nota em RX_FM_ESCALAR).
        fm_grafo = None if em_raw else frontmatter(texto)
        for chave, valor in (refs_frontmatter(fm_grafo) if fm_grafo else []):
            destino = resolver_ref(bundle, p, valor)
            if destino is None:
                add("error", "E2-link-quebrado", str(p.relative_to(bundle)),
                    f"Frontmatter `{chave}: {valor}` nao resolve para arquivo existente.")
                continue
            registrar_aresta(p, destino)

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

        tem_raw, motivo = conferir_deposito(bundle, p, fm, stems_raw)

        if tipo in ("acordao", "sumula") and not tem_raw:
            # Ementa e texto longo, especifico e facil de fabricar de forma plausivel.
            # Sem o inteiro teor depositado nao ha como o lint-citacoes conferir a
            # transcricao — e e justamente ai que mora o dano irreversivel.
            add("error", "E4-sem-inteiro-teor", str(p.relative_to(bundle)),
                f"`type: {tipo}` marcado `vigente` sem inteiro teor conferivel em raw/: {motivo}")
        elif tipo == "legislacao" and not tem_raw:
            # Texto de lei e curto, estavel e conferivel em fonte publica: o risco de
            # fabricacao nao verificavel e baixo. Aviso, nao erro.
            add("warning", "W3-lei-sem-deposito", str(p.relative_to(bundle)),
                f"`type: legislacao` marcado `vigente` sem transcricao oficial em raw/: {motivo}")

        # E6 — campos do Espelho do Acordao (schema 0.5)
        if tipo == "acordao":
            for erro in conferir_espelho(fm, texto):
                add("error", "E6-espelho-invalido", str(p.relative_to(bundle)), erro)

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
        # Consulta o grafo ja montado — corpo E frontmatter. Antes daqui so se liam os
        # links do corpo, e a tese que declarava `fundamentos:` no frontmatter (a
        # convencao do acervo) era acusada de nao ter fundamento nenhum.
        aponta = False
        for alvo in saida.get(p.resolve(), ()):
            try:
                fm_alvo = frontmatter(alvo.read_text(encoding="utf-8")) or ""
            except Exception:
                continue
            if (campo(fm_alvo, "type") or "") in ("acordao", "sumula", "legislacao"):
                aponta = True
                break
        if not aponta:
            add("error", "E5-tese-sem-fundamento", str(p.relative_to(bundle)),
                "Tese nao aponta para nenhum acordao, sumula ou legislacao do bundle — sintese sem fundamento rastreavel.")

    # W1 — orfas. raw/ fica FORA, pela mesma razao que ja o exclui do E1, E2 e E3:
    # e camada de deposito, nao de conhecimento. Um PDF transcrito e citado por uma
    # pagina curada, ou por nenhuma enquanto nao for derivado — chamar isso de "orfa"
    # e erro de categoria, e era o que produzia 260 dos 289 avisos.
    for p in conteudo:
        if "raw" in p.relative_to(bundle).parts:
            continue
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
