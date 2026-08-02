#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
reparar-ligaduras.py — higiene da conversao pdfmd antes do deposito.

Duas operacoes, ambas deterministas, sobre o Markdown que saiu do pdfmd:

  1. REUNIR PALAVRA PARTIDA POR LIGADURA (fi/fl/ff) — sempre.
  2. REMOVER O OCR DE IMAGEM (--remover-ocr-de-imagem) — sob demanda.

A segunda existe por um achado de 2026-08-02 no deposito do RISTJ, e e mais
perigosa que a primeira: quando a pagina do PDF traz o texto TAMBEM como
imagem, o `--ocr-images` do pdfmd emite a transcricao dessa imagem num
blockquote ANTES do texto nativo. O arquivo passa a ter cada artigo DUAS
vezes: a versao boa e a versao com erro de OCR.

    > **OCR da imagem; confianca media 91.1%:**
    > ... Art.255.0 recurso especial ... S$ 1º ... óabeas corpus ...

    **Art. 255. ** O recurso especial ... § 1º ... habeas corpus ...

Como o `recortar-artigo.py` recorta a PRIMEIRA ocorrencia, o recorte saía da
versao degradada — e um recorte e o que a peca transcreve. No RISTJ eram 429
blocos assim. Paginas cujo texto so existe por OCR (`method=tesseract`) nao
sao tocadas: ali o OCR e o corpo da pagina, nao um blockquote duplicado.

--------------------------------------------------------------------------
Sobre as ligaduras.

PRD 2026-08-02, F3.1. O PDF do RISTJ usa as ligaduras fi/fl/ff. A extracao as
devolve como as duas letras SEGUIDAS DE UM ESPACO ESPURIO, e a palavra racha:

    "confi rmando-a"   "fi xada"   "ofi cial"   "qualifi cados"   "confl ito"

Isso nao atrapalha a leitura humana, mas derrota o `lint-citacoes`, que confere
transcricao por n-gramas contiguos de palavras: a palavra partida quebra a
sequencia e a citacao correta e acusada de divergente.

O reparo e DETERMINISTICO — nao ha modelo decidindo nada. E porque nenhuma
palavra do portugues termina em "fi", "fl" ou "ff" seguida de continuacao em
minuscula, o padrao so ocorre onde a ligadura quebrou.

Guarda dura: `fl.` e `fls.` sao a abreviatura de folha/folhas, usadas o tempo
todo em texto juridico ("fl. 25", "fls. 25-27"). A regra so junta quando o que
vem depois do espaco comeca por LETRA minuscula, entao "fl. 25" nunca e tocado.

Gera, ao lado do arquivo reparado, um `<arquivo>.ligaduras.diff` com todas as
substituicoes agrupadas e contadas — que e o material da conferencia. Sem o
diff nao ha como conferir, e sem conferencia o deposito nao entra no acervo
(regra do catalogo em direito/pecas/raw/index.md).

Uso (stdlib apenas):
    python reparar-ligaduras.py <arquivo.md>            # grava .reparado.md + .diff
    python reparar-ligaduras.py <arquivo.md> --resumo   # so relata, nao grava
    python reparar-ligaduras.py <arquivo.md> --no-lugar # sobrescreve o arquivo

Exit: 0 = ok | 1 = arquivo ausente
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

# As ligaduras que o extrator quebra. "ffi" e "ffl" antes de "ff" para que a
# alternancia case o prefixo mais longo primeiro.
LIGADURAS = ("ffi", "ffl", "fi", "fl", "ff")

# (inicio da palavra)(ligadura) (continuacao em minuscula)
#
# `\w*` cobre "con|fi rmando" e "" cobre "fi xada". A continuacao exige ao menos
# uma letra minuscula: barra numero ("fl. 25"), maiuscula (inicio de frase) e
# pontuacao. `(?![.,;:)])` impede juntar quando ha pontuacao logo apos a
# ligadura, que e onde mora a abreviatura de folha.
RX = re.compile(
    r"(?<![\w-])((?:\w*)(?:" + "|".join(LIGADURAS) + r"))[  ]+([a-zà-öø-ÿ][\wà-öø-ÿ-]*)",
    re.UNICODE,
)

# Palavras que legitimamente terminam nas letras da ligadura e podem ser
# seguidas de minuscula. Sao poucas e todas estrangeirismos ou siglas; sem esta
# lista, "wi fi caiu" viraria "wifi caiu" (certo) mas "sci fi de" nao. Mantida
# explicita para que a conferencia veja o que foi poupado.
EXCECOES = {"wifi", "sci", "hi", "lo", "off", "staff", "buff"}


# Bloco de transcricao de imagem: um blockquote aberto por "> **OCR da imagem"
# e todas as linhas "> " que o seguem, ate a primeira linha que nao e citacao.
RX_BLOCO_OCR = re.compile(
    r"(?m)^>[ \t]*\*\*OCR da imagem[^\n]*\n(?:^>[^\n]*\n)*",
)


def remover_ocr_de_imagem(texto: str) -> tuple[str, int, int]:
    blocos = RX_BLOCO_OCR.findall(texto)
    chars = sum(len(b) for b in blocos)
    return RX_BLOCO_OCR.sub("", texto), len(blocos), chars


def reparar(texto: str) -> tuple[str, Counter]:
    trocas: Counter = Counter()

    def sub(m: re.Match) -> str:
        cabeca, cauda = m.group(1), m.group(2)
        if cabeca.lower() in EXCECOES:
            return m.group(0)
        junto = cabeca + cauda
        trocas[f"{cabeca} {cauda}  ->  {junto}"] += 1
        return junto

    return RX.sub(sub, texto), trocas


def escrever_diff(destino: Path, origem: Path, trocas: Counter) -> None:
    linhas = [
        f"# Reparo de ligaduras — {origem.name}",
        "",
        f"{sum(trocas.values())} substituicao(oes), {len(trocas)} forma(s) distinta(s).",
        "",
        "Cada linha e uma forma distinta, com quantas vezes ocorreu. A conferencia",
        "consiste em ler esta lista: toda linha precisa ser uma palavra do portugues",
        "que estava partida. Qualquer juncao que produza palavra inexistente e defeito",
        "da regra — corrigir o script e regerar, nunca editar o texto a mao.",
        "",
    ]
    for forma, n in trocas.most_common():
        linhas.append(f"{n:>5}x  {forma}")
    destino.write_text("\n".join(linhas) + "\n", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description="Reune palavra partida por ligadura fi/fl/ff.")
    ap.add_argument("arquivo")
    ap.add_argument("--resumo", action="store_true", help="relata sem gravar nada")
    ap.add_argument("--no-lugar", action="store_true", help="sobrescreve o arquivo de entrada")
    ap.add_argument("--remover-ocr-de-imagem", action="store_true",
                    help="apaga os blockquotes de OCR de imagem, que duplicam o texto nativo com erro")
    args = ap.parse_args()

    origem = Path(args.arquivo)
    if not origem.exists():
        print(f"ERRO: {origem} nao existe.")
        return 1

    texto = origem.read_text(encoding="utf-8")

    print(f"reparar-ligaduras: {origem.name}")
    if args.remover_ocr_de_imagem:
        texto, n_blocos, n_chars = remover_ocr_de_imagem(texto)
        print(f"  {n_blocos} bloco(s) de OCR de imagem removido(s) ({n_chars} chars).")
        if n_blocos:
            print("    Eram duplicata degradada do texto nativo da mesma pagina.")

    reparado, trocas = reparar(texto)
    print(f"  {sum(trocas.values())} substituicao(oes), {len(trocas)} forma(s) distinta(s).")
    for forma, n in trocas.most_common(25):
        print(f"    {n:>4}x  {forma}")
    if len(trocas) > 25:
        print(f"    ... mais {len(trocas) - 25} forma(s) — lista completa no .diff")

    if args.resumo:
        return 0

    destino = origem if args.no_lugar else origem.with_suffix(".reparado.md")
    destino.write_text(reparado, encoding="utf-8")
    diff = origem.with_suffix(origem.suffix + ".ligaduras.diff")
    escrever_diff(diff, origem, trocas)
    print(f"  -> {destino.name}")
    print(f"  -> {diff.name}  (conferir ANTES de depositar)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
