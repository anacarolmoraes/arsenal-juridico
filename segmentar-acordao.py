#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
segmentar-acordao.py — separa as vozes de um acordao.

PRD 2026-08-02, F1. Um acordao e documento polifonico: falam o relator, o
tribunal de origem (ementa transcrita no relatorio) e outros precedentes
(ementas coladas no voto como argumento de autoridade). O lint-citacoes
comparava a citacao contra o ARQUIVO INTEIRO, de modo que um trecho de ementa
ALHEIA passava com 100% de sobreposicao atribuido ao julgado que apenas a
citou — ou que a rejeitou.

Modelo: o Espelho do Acordao do STJ (Manual de Organizacao 2026, cap. 5), que
mantem `enunciado de tese`, `referencia legislativa` e `jurisprudencia citada`
em campos SEPARADOS. Sao tres campos porque citacao nao e tese.

Gera `<arquivo>.estrutura.json` ao lado do .md, com:

  secoes          ementa | relatorio | voto | dispositivo, por faixa de caractere
  ementa_cnj      I. CASO EM EXAME ... IV. DISPOSITIVO E TESE, quando houver
  blocos_citados  faixas cuja voz e de OUTRO julgado, com o sinal que as delatou
  metadados       relator, orgao julgador, classe e numero
  nao_segmentado  true quando o documento nao expoe estrutura reconhecivel

Regra dura: sem estrutura reconhecivel o sidecar sai com `nao_segmentado: true`
e o lint-citacoes volta ao comportamento antigo. Nada degrada em silencio.

Uso (stdlib apenas, sem dependencias):
    python segmentar-acordao.py <arquivo.md> [<arquivo.md> ...]
    python segmentar-acordao.py --bundle direito/imobiliario
    python segmentar-acordao.py --todos
    python segmentar-acordao.py <arquivo.md> --resumo   # imprime, nao grava

Exit: 0 = tudo segmentado | 1 = algum arquivo ilegivel ou nao segmentado
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parent

# Um bloco citado precisa de corpo: enfase curta no meio da prosa do relator
# ("o proprio STJ ja decidiu que a *causa decidida* e requisito") e enfase, nao
# transcricao. 200 caracteres e o piso de uma ementa real.
MIN_BLOCO = 200

# Sem parentetico de atribuicao a vista, exige-se mais corpo antes de declarar
# transcricao. O erro barato e marcar como citado o que era enfase (o lint pede
# conferencia); o erro caro e deixar passar como voz propria o que era ementa
# alheia (a peca cita como ratio o que o julgado apenas transcreveu).
MIN_BLOCO_SEM_ATRIBUICAO = 300

# A conversao pdfmd estilhaca uma unica ementa em dezenas de trechos em italico
# separados por pedacos curtos de texto plano (numero de lei, "fls.", espaco).
# Sem costurar essas lacunas, uma ementa vira 40 blocos de 30 caracteres.
LACUNA_ITALICO = 90

# ------------------------------------------------------------------ utilidades


def sem_acento(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


def chave(s: str) -> str:
    """Titulo de secao em ASCII maiusculo, sem enfase markdown."""
    s = re.sub(r"[*_`#]", " ", s)
    return re.sub(r"\s+", " ", sem_acento(s).upper()).strip()


def offsets_de_linha(texto: str) -> list[int]:
    inicios = [0]
    for i, c in enumerate(texto):
        if c == "\n":
            inicios.append(i + 1)
    return inicios


def linha_de(offset: int, inicios: list[int]) -> int:
    lo, hi = 0, len(inicios) - 1
    while lo < hi:
        meio = (lo + hi + 1) // 2
        if inicios[meio] <= offset:
            lo = meio
        else:
            hi = meio - 1
    return lo + 1


def fundir(faixas: list[tuple[int, int]], folga: int = 0) -> list[tuple[int, int]]:
    if not faixas:
        return []
    faixas = sorted(faixas)
    saida = [list(faixas[0])]
    for ini, fim in faixas[1:]:
        if ini <= saida[-1][1] + folga:
            saida[-1][1] = max(saida[-1][1], fim)
        else:
            saida.append([ini, fim])
    return [(a, b) for a, b in saida]


# --------------------------------------------------------------------- secoes

SECOES = [
    ("voto_vista", re.compile(r"^VOTO[ -]*VISTA\b")),
    ("voto_vencido", re.compile(r"^VOTO\s+VENCIDO\b")),
    ("voto", re.compile(r"^VOTO\b")),
    ("ementa", re.compile(r"^EMENTA\b")),
    ("relatorio", re.compile(r"^RELATORIO\b")),
    ("relator", re.compile(r"^RELATOR[A]?\b")),
    ("acordao", re.compile(r"^ACORDAO\b")),
    ("certidao", re.compile(r"^CERTIDAO\b")),
    ("decisao", re.compile(r"^DECISAO\b")),
]

RX_HEADING = re.compile(r"^#{1,6}[ \t]+(.+?)[ \t]*$", re.M)

# Fecho do voto no STJ. A regex do radar (buscar.js) so conhecia conectivo de
# abertura de dispositivo; no STJ o voto costuma fechar por aqui.
RX_DISPOSITIVO = re.compile(
    r"\b(ante o exposto|diante do exposto|isto posto|posto isto|posto isso|"
    r"pelo exposto|ex positis|face ao exposto|em face do exposto|do exposto|"
    r"por tais razoes|forte em tais razoes)\b"
)
RX_FECHO_VOTO = re.compile(r"\b(e como voto|e o meu voto|e o voto)\b")

RX_RUIDO = re.compile(
    r"^\s*(<a id=|<!--|!\[|\*Imagem incorporada|\*\*\(e-STJ|\(e-STJ|"
    r"Documento eletronico|Certificado por|Assinado eletronicamente|"
    r"Superior Tribunal de Justica\s*$|\d+\s*$)"
)


def achar_secoes(texto: str) -> list[dict]:
    marcos: list[tuple[int, str, str]] = []
    for m in RX_HEADING.finditer(texto):
        titulo = chave(m.group(1))
        for nome, rx in SECOES:
            if rx.match(titulo):
                marcos.append((m.start(), nome, m.group(1).strip()))
                break

    secoes = []
    for i, (ini, nome, titulo) in enumerate(marcos):
        fim = marcos[i + 1][0] if i + 1 < len(marcos) else len(texto)
        secoes.append({"nome": nome, "titulo": titulo, "inicio": ini, "fim": fim})

    # Tudo antes da primeira secao reconhecida e capa/autuacao: partes, advogados,
    # numero do processo. Nao e voz de ninguem, mas guarda os metadados.
    if secoes and secoes[0]["inicio"] > 0:
        secoes.insert(0, {"nome": "capa", "titulo": "(cabecalho)", "inicio": 0, "fim": secoes[0]["inicio"]})
    return secoes


def achar_dispositivo(texto: str, secoes: list[dict]) -> dict | None:
    """O dispositivo e o fim do voto condutor: do conectivo ate o fecho."""
    for s in secoes:
        if s["nome"] != "voto":
            continue
        trecho = sem_acento(texto[s["inicio"]: s["fim"]]).lower()
        fecho = RX_FECHO_VOTO.search(trecho)
        limite = fecho.end() if fecho else len(trecho)
        # ultimo conectivo antes do fecho: o voto pode usar "do exposto" no meio
        # da narrativa e so decidir no fim.
        ultimo = None
        for m in RX_DISPOSITIVO.finditer(trecho[:limite]):
            ultimo = m
        if ultimo:
            return {
                "nome": "dispositivo",
                "titulo": ultimo.group(1),
                "inicio": s["inicio"] + ultimo.start(),
                "fim": s["inicio"] + limite,
                "dentro_de": "voto",
            }
    return None


# ---------------------------------------------------------------- ementa CNJ

CNJ_CAMPOS = [
    ("caso_em_exame", r"\bI\s*[.\-)]\s*CASO EM EXAME"),
    ("questao_em_discussao", r"\bII\s*[.\-)]\s*QUEST[AO]{1,2}O?E?S? EM DISCUSS[AO]{1,2}O"),
    ("razoes_de_decidir", r"\bIII\s*[.\-)]\s*RAZ[OA]{1,2}ES DE DECIDIR"),
    ("dispositivo_e_tese", r"\bIV\s*[.\-)]\s*DISPOSITIVO E TESE"),
    ("tese_de_julgamento", r"\bTESE DE JULGAMENTO"),
    ("dispositivos_citados", r"\bDISPOSITIVOS RELEVANTES CITADOS"),
    ("jurisprudencia_citada", r"\bJURISPRUDENCIA RELEVANTE CITADA"),
]


def achar_ementa_cnj(texto: str) -> dict:
    """Ementa no padrao CNJ ja vem com a tese isolada — e so ler o campo."""
    plano = chave(texto)
    achados = {}
    for nome, padrao in CNJ_CAMPOS:
        m = re.search(padrao, plano)
        if m:
            achados[nome] = m.start()
    return achados


# ------------------------------------------------------- deteccao de voz citada

RX_BOLD = re.compile(r"\*\*[^*]+?\*\*", re.S)
RX_ITALICO = re.compile(r"\*[^*\n]{3,}?\*")
RX_ASPAS = re.compile(r"[\"“][^\"”\n]{80,}[\"”]")

CLASSES = (
    r"REsp|AREsp|AgInt|AgRg|EAREsp|EREsp|EDcl|RMS|RHC|HC|MS|CC|IAC|Pet|SLS|"
    r"RE|ARE|ADI|ADPF|ADC|RCL|Rcl"
)
RX_PRECEDENTE = re.compile(rf"\b({CLASSES})\b[^\d\n]{{0,40}}?(\d[\d.]{{3,}})", re.I)
RX_ATRIBUICAO = re.compile(r"\(([^()]{10,500})\)", re.S)
RX_SINAL_ATRIB = re.compile(
    rf"\b(relator[a]?|rel\.|julgado em|DJe|DJEN|TURMA|SECAO|CORTE ESPECIAL|{CLASSES})\b", re.I
)

# Frases com que o relator abre uma transcricao. Sao o unico sinal disponivel
# quando a conversao nao preservou italico nem aspas.
RX_INTRO = re.compile(
    r"\b(assim ementad[oa]|nestes termos ementad[oa]|assim decidiu|no mesmo sentido|"
    r"nesse sentido|in verbis|verbis|confira-se|confiram-se|transcreve-se|"
    r"nos seguintes termos|assim redigid[oa]|com a seguinte ementa|"
    r"a seguir transcrit[oa]|assim resumid[oa])\b"
)


def spans_italico(texto: str) -> list[tuple[int, int]]:
    limpo = RX_BOLD.sub(lambda m: " " * len(m.group(0)), texto)
    return [(m.start(), m.end()) for m in RX_ITALICO.finditer(limpo)]


def spans_blockquote(texto: str, inicios: list[int]) -> list[tuple[int, int]]:
    faixas = []
    atual = None
    for i, ini in enumerate(inicios):
        fim = inicios[i + 1] if i + 1 < len(inicios) else len(texto)
        linha = texto[ini:fim]
        if linha.lstrip().startswith(">"):
            atual = (atual[0], fim) if atual else (ini, fim)
        elif atual and linha.strip() == "":
            continue
        elif atual:
            faixas.append(atual)
            atual = None
    if atual:
        faixas.append(atual)
    return faixas


def spans_caixa_alta(texto: str, inicios: list[int]) -> list[tuple[int, int]]:
    """Ementa transcrita sem italico costuma vir integralmente em caixa alta."""
    faixas = []
    for i, ini in enumerate(inicios):
        fim = inicios[i + 1] if i + 1 < len(inicios) else len(texto)
        linha = texto[ini:fim]
        letras = [c for c in linha if c.isalpha()]
        if len(letras) < 120:
            continue
        if sum(1 for c in letras if c.isupper()) / len(letras) > 0.85:
            faixas.append((ini, fim))
    return faixas


def contexto_anterior(texto: str, offset: int, janela: int = 900) -> str:
    """
    Texto util imediatamente antes de um bloco, ja sem o entulho da conversao.

    A frase que abre a transcricao ("nos seguintes termos:") costuma ficar longe
    do bloco em numero de caracteres, mas colada em leitura humana: entre as duas
    a conversao despeja carimbo de assinatura, rodape e-STJ e cabecalho de pagina.
    """
    bruto = texto[max(0, offset - janela): offset]
    uteis = [ln for ln in bruto.split("\n") if ln.strip() and not RX_RUIDO.match(ln)]
    return sem_acento(" ".join(uteis)).lower()


def atribuicoes_em(trecho: str) -> list[str]:
    """
    Parenteticos que sao ATRIBUICAO, nao citacao interna.

    Distincao que importa: a ementa transcrita cita, ela propria, outros
    precedentes no corpo ("No julgamento do REsp n. 1.798.374/DF, a Corte
    Especial firmou..."). Esses nao sao a autoria do bloco. So conta o
    parentetico que reune precedente + marca de julgamento (relator, orgao,
    data, DJe) — que e a forma como o STJ fecha uma transcricao.
    """
    achadas = []
    for m in RX_ATRIBUICAO.finditer(trecho):
        interno = m.group(1)
        if not RX_PRECEDENTE.search(interno):
            continue
        if not re.search(r"\b(relator|relatora|rel\.|julgado em|DJe|DJEN)\b", interno, re.I):
            continue
        p = None
        for p in RX_PRECEDENTE.finditer(interno):
            pass
        if p:
            achadas.append(f"{p.group(1)} {p.group(2)}")
    return achadas


def autoria_do_bloco(texto: str, ini: int, fim: int, limite_gap: int) -> dict:
    """
    Devolve a autoria do bloco sem chutar.

    Rotulo errado e pior que rotulo ausente: quem le "-> REsp X" confia. Se a
    atribuicao nao esta a vista, o campo sai nulo e o aviso pede conferencia.
    """
    janela = texto[ini: min(len(texto), fim + limite_gap)]
    atribs = atribuicoes_em(janela)

    if len(atribs) == 1:
        return {"precedente": atribs[0], "precedentes": atribs, "origem": "precedente"}
    if len(atribs) > 1:
        # Bloco que carrega mais de uma ementa transcrita: nao ha um dono unico.
        return {"precedente": None, "precedentes": atribs, "origem": "precedente-multiplo"}

    # Sem parentetico de fechamento: a ementa do acordao recorrido e apresentada
    # pelo relator na narrativa, nao por atribuicao formal. A janela e curta de
    # proposito — "o acordao recorrido limitou-se a fixar a tese" e frase que
    # aparece DENTRO das ementas transcritas, e com janela larga contaminava a
    # atribuicao do bloco seguinte.
    antes = contexto_anterior(texto, ini)[-250:]
    if re.search(r"\b(assim ementad[oa]|com a seguinte ementa|nestes termos ementad[oa]|"
                 r"acordao recorrido, (?:assim|nos)|ementa do acordao recorrido|"
                 r"(?:corte|tribunal) de origem[^.]{0,80}(?:assim|nos seguintes termos|ementad))\b",
                 antes):
        return {"precedente": None, "precedentes": [], "origem": "acordao-recorrido"}

    # Ha numeros de precedente no bloco, mas nenhum em posicao de atribuicao:
    # sao citacoes DENTRO da citacao. Registrar como pista, nunca como autoria.
    pistas = [f"{m.group(1)} {m.group(2)}" for m in RX_PRECEDENTE.finditer(janela)]
    return {"precedente": None, "precedentes": [], "origem": "indeterminada",
            "pistas": sorted(set(pistas))[:5]}


def achar_blocos_citados(texto: str, inicios: list[int], secoes: list[dict]) -> list[dict]:
    # A capa e a autuacao: nome das partes e dos advogados, em caixa alta. Nao e
    # voz de ninguem, e sem excluir vira falso bloco citado em todo acordao.
    metadados_ate = max(
        [s["fim"] for s in secoes if s["nome"] in ("capa", "relator")] or [0]
    )

    candidatos: list[tuple[int, int, str]] = []

    for ini, fim in fundir(spans_italico(texto), LACUNA_ITALICO):
        candidatos.append((ini, fim, "italico"))
    for ini, fim in spans_blockquote(texto, inicios):
        candidatos.append((ini, fim, "blockquote"))
    for ini, fim in fundir(spans_caixa_alta(texto, inicios), 200):
        candidatos.append((ini, fim, "caixa-alta"))
    for m in RX_ASPAS.finditer(texto):
        candidatos.append((m.start(), m.end(), "aspas"))

    # Uniao dos sinais, preservando quais dispararam.
    faixas = fundir([(a, b) for a, b, _ in candidatos], 0)

    # O relator empilha ementas em sequencia ("No mesmo sentido:"), separadas
    # apenas pelo parentetico de atribuicao. Sem cortar ali, varias transcricoes
    # de donos diferentes viram um bloco so, e nenhuma tem autoria atribuivel.
    cortadas: list[tuple[int, int]] = []
    for ini, fim in faixas:
        corte = ini
        for m in RX_ATRIBUICAO.finditer(texto[ini:fim]):
            if atribuicoes_em(m.group(0)):
                cortadas.append((corte, ini + m.end()))
                corte = ini + m.end()
        cortadas.append((corte, fim))

    blocos = []
    for i, (ini, fim) in enumerate(cortadas):
        if fim - ini < MIN_BLOCO or fim <= metadados_ate:
            continue
        sinais = sorted({s for a, b, s in candidatos if a < fim and b > ini})
        # A janela de busca da atribuicao nunca invade o proximo bloco: era assim
        # que uma transcricao herdava o dono da seguinte.
        proximo = cortadas[i + 1][0] if i + 1 < len(cortadas) else len(texto)
        autoria = autoria_do_bloco(texto, ini, fim, max(0, min(400, proximo - fim)))

        if autoria["origem"] == "indeterminada" and "blockquote" not in sinais:
            if fim - ini < MIN_BLOCO_SEM_ATRIBUICAO:
                continue
            # Frase com que o relator abre uma transcricao. Nao decide nada
            # sozinha — apenas registra por que se acredita que ha citacao ali.
            if RX_INTRO.search(contexto_anterior(texto, ini)):
                sinais.append("frase-de-abertura")

        blocos.append(
            {
                "inicio": ini,
                "fim": fim,
                "linha_inicio": linha_de(ini, inicios),
                "linha_fim": linha_de(max(ini, fim - 1), inicios),
                "chars": fim - ini,
                "sinais": sinais,
                "amostra": re.sub(r"\s+", " ", texto[ini: ini + 120]).strip(),
                **autoria,
            }
        )
    return blocos


# ------------------------------------------------------------------ metadados

RX_MINISTRO = re.compile(r"\bMINISTR[OA]\s+([A-ZÀ-Ú][A-ZÀ-Ú\s'.-]{4,60}?)(?=\s{2,}|\s*\*|\s+RECORRENTE|\s+RECORRIDO|\s+AGRAVANTE|\s+IMPETRANTE|\n|$)")
RX_ORGAO = re.compile(
    r"\b(PRIMEIRA|SEGUNDA|TERCEIRA|QUARTA|QUINTA|SEXTA)\s+(TURMA|SECAO)\b|\bCORTE ESPECIAL\b"
)
RX_CLASSE_NUM = re.compile(
    r"\b(RECURSO ESPECIAL|AGRAVO EM RECURSO ESPECIAL|AGRAVO INTERNO|EMBARGOS DE DIVERGENCIA|"
    r"HABEAS CORPUS|MANDADO DE SEGURANCA|RECURSO ORDINARIO|CONFLITO DE COMPETENCIA)"
    r"\s*N?[.º°]?\s*([\d.]{4,})"
)


def metadados(texto: str, secoes: list[dict]) -> dict:
    # O relator e nomeado na capa; buscar no documento inteiro pegaria o relator
    # de cada precedente citado no voto.
    limite = next((s["fim"] for s in secoes if s["nome"] in ("capa", "relator")), 3000)
    cabeca = texto[: max(limite, 1500)]

    md: dict = {"relator": None, "orgao_julgador": None, "classe": None, "numero": None}

    m = RX_MINISTRO.search(cabeca)
    if m:
        md["relator"] = re.sub(r"\s+", " ", m.group(1)).strip(" .-'")

    # O orgao julgador so pode ser lido onde ele e DECLARADO: capa, certidao de
    # julgamento ou cabecalho do acordao. Procurar na ementa ou no voto captura
    # o orgao dos precedentes citados — foi assim que este julgado da Quarta
    # Turma saiu rotulado "CORTE ESPECIAL", que e o orgao do REsp 1.798.374/DF
    # que ele invoca. Sem declaracao a vista, o campo fica nulo.
    for s in secoes:
        if s["nome"] not in ("capa", "relator", "certidao", "acordao", "decisao"):
            continue
        m = RX_ORGAO.search(chave(texto[s["inicio"]: s["fim"]]))
        if m:
            md["orgao_julgador"] = re.sub(r"\s+", " ", m.group(0)).strip()
            break

    m = RX_CLASSE_NUM.search(chave(cabeca))
    if m:
        md["classe"] = m.group(1).strip()
        md["numero"] = m.group(2).strip()
    return md


# ------------------------------------------------------------------- pipeline


def segmentar(caminho: Path) -> dict:
    texto = caminho.read_text(encoding="utf-8")
    inicios = offsets_de_linha(texto)

    secoes = achar_secoes(texto)
    disp = achar_dispositivo(texto, secoes)
    blocos = achar_blocos_citados(texto, inicios, secoes)
    cnj = achar_ementa_cnj(texto)

    nomes = {s["nome"] for s in secoes}
    estruturado = bool(nomes & {"ementa", "relatorio", "voto"})

    avisos = []
    if not estruturado:
        # Sem saber onde comeca o voto, nao se sabe de quem e a voz: um documento
        # que e so transcricao (compilacao de sumulas, apelacao sem cabecalho)
        # sairia com tudo marcado como citado, o que nao informa nada. O contrato
        # com o lint-citacoes ja e "nao_segmentado -> comportamento antigo".
        blocos = []
        avisos.append(
            "Nenhum cabecalho de EMENTA, RELATORIO ou VOTO encontrado: o documento nao "
            "expoe a estrutura do acordao. Deteccao de voz suprimida — conferir a vista "
            "antes de citar."
        )
    if estruturado and "voto" not in nomes:
        avisos.append("Sem secao VOTO: a ratio nao pode ser localizada; so a ementa esta disponivel.")
    if estruturado and not disp and "voto" in nomes:
        avisos.append("Secao VOTO sem conectivo de dispositivo reconhecido — conferir o fecho a vista.")
    indeterminados = [b for b in blocos if b["origem"] == "indeterminada"]
    if indeterminados:
        avisos.append(
            f"{len(indeterminados)} bloco(s) citado(s) sem atribuicao rastreavel: a transcricao "
            "e visivel, a autoria nao. Conferir a quem pertencem antes de cita-los."
        )

    saida_secoes = [
        {
            "nome": s["nome"],
            "titulo": s["titulo"],
            "inicio": s["inicio"],
            "fim": s["fim"],
            "linha_inicio": linha_de(s["inicio"], inicios),
            "linha_fim": linha_de(max(s["inicio"], s["fim"] - 1), inicios),
        }
        for s in secoes
    ]
    if disp:
        saida_secoes.append(
            {
                "nome": "dispositivo",
                "titulo": disp["titulo"],
                "inicio": disp["inicio"],
                "fim": disp["fim"],
                "linha_inicio": linha_de(disp["inicio"], inicios),
                "linha_fim": linha_de(max(disp["inicio"], disp["fim"] - 1), inicios),
                "dentro_de": "voto",
            }
        )

    chars_citados = sum(b["chars"] for b in blocos)
    return {
        "schema": "estrutura-acordao/1.0",
        "arquivo": caminho.name,
        "source_sha256": hashlib.sha256(caminho.read_bytes()).hexdigest(),
        "chars": len(texto),
        "nao_segmentado": not estruturado,
        "metadados": metadados(texto, secoes),
        "secoes": saida_secoes,
        "ementa_cnj": cnj or None,
        "blocos_citados": blocos,
        "resumo": {
            "secoes": sorted(nomes),
            "blocos_citados": len(blocos),
            "chars_citados": chars_citados,
            "proporcao_citada": round(chars_citados / len(texto), 3) if texto else 0,
        },
        "avisos": avisos,
    }


def imprimir(res: dict, limite: int = 12) -> None:
    print(f"  {res['arquivo']}  ({res['chars']} chars)")
    if res["nao_segmentado"]:
        print("    NAO SEGMENTADO — sem cabecalho de secao reconhecivel.")
    else:
        print(f"    secoes: {', '.join(s['nome'] for s in res['secoes'])}")
    md = res["metadados"]
    if md.get("relator") or md.get("orgao_julgador"):
        print(f"    relator: {md.get('relator') or '?'} | orgao: {md.get('orgao_julgador') or '?'}")
    if res["ementa_cnj"]:
        print(f"    ementa CNJ: {', '.join(sorted(res['ementa_cnj']))}")
    r = res["resumo"]
    print(f"    voz citada: {r['blocos_citados']} bloco(s), {r['chars_citados']} chars "
          f"({int(r['proporcao_citada'] * 100)}% do documento)")
    # Compilacao de sumulas ou de repetitivos chega a centenas de blocos: listar
    # todos afoga o relatorio. O sidecar guarda a lista inteira.
    mostrados = res["blocos_citados"][:limite]
    for b in mostrados:
        if b["precedente"]:
            rot = b["precedente"]
        elif b["origem"] == "acordao-recorrido":
            rot = "acordao recorrido"
        elif b["origem"] == "precedente-multiplo":
            rot = " + ".join(b["precedentes"])
        else:
            rot = "AUTORIA NAO ATRIBUIDA" + (f" (pistas: {', '.join(b.get('pistas', []))})" if b.get("pistas") else "")
        print(f"      L{b['linha_inicio']}-{b['linha_fim']}  {b['chars']:>6} chars  [{'+'.join(b['sinais'])}]  -> {rot}")
    if len(res["blocos_citados"]) > limite:
        print(f"      ... mais {len(res['blocos_citados']) - limite} bloco(s) — lista completa no sidecar.")
    for a in res["avisos"]:
        print(f"    AVISO {a}")


RX_FRONTMATTER = re.compile(r"\A---\n(.*?)\n---", re.S)


def parece_acordao(caminho: Path) -> bool:
    """
    raw/ guarda tambem codigo, lei e manual — nada disso tem ementa nem voto.
    Rodar o segmentador neles produz ruido e, pior, marca cada trecho entre
    aspas de um manual como "voz citada".
    """
    try:
        cabeca = caminho.read_text(encoding="utf-8")[:6000]
    except Exception:
        return False
    if any(rx.match(chave(t)) for t in RX_HEADING.findall(cabeca) for _, rx in SECOES):
        return True
    return bool(RX_CLASSE_NUM.search(chave(cabeca)))


def paginas_de_acordao(base: Path) -> list[Path]:
    """
    Alvo canonico do F1.2: o deposito citado pelas paginas `type: acordao`.
    E o mesmo lastro que o E4 do lint-bundle exige — segmentar o que a peca
    pode citar, nao o que por acaso esta em raw/.
    """
    achados: list[Path] = []
    for p in base.rglob("*.md"):
        if "raw" in p.parts or any(x in p.parts for x in (".git", "node_modules")):
            continue
        try:
            texto = p.read_text(encoding="utf-8")
        except Exception:
            continue
        m = RX_FRONTMATTER.match(texto)
        if not m:
            continue
        fm = m.group(1)
        tipo = re.search(r"^type:\s*(.+)$", fm, re.M)
        if not tipo or tipo.group(1).strip().strip("\"'") not in ("acordao", "sumula"):
            continue
        bruto = re.search(r"^raw:\s*(.+)$", fm, re.M)
        if not bruto:
            continue
        alvo = resolver_raw(p, bruto.group(1).strip().strip("\"'`"))
        if alvo:
            achados.append(alvo)
    return sorted(set(achados))


def resolver_raw(pagina: Path, declarado: str) -> Path | None:
    """
    O campo `raw:` aponta para o deposito OFICIAL, que e o PDF, e o caminho e
    relativo ao bundle (`/raw/earesp-600663-rs.pdf`). O segmentador le a
    conversao Markdown ao lado — a representacao canonica do acervo.
    """
    rel = declarado.lstrip("/")
    candidatos = []
    for ancestral in [pagina.parent, *pagina.parents]:
        candidatos.append(ancestral / rel)
        if ancestral == RAIZ:
            break
    for c in candidatos:
        md = c.with_suffix(".md")
        if md.exists():
            return md.resolve()
    return None


def alvos(args) -> tuple[list[Path], int]:
    if args.arquivos:
        return [Path(a) for a in args.arquivos], 0

    base = RAIZ if not args.bundle else (Path(args.bundle) if Path(args.bundle).is_absolute() else RAIZ / args.bundle)

    if args.acordaos:
        return paginas_de_acordao(base), 0

    brutos = sorted(
        p for p in base.rglob("raw/*.md")
        if "node_modules" not in p.parts and not p.name.endswith(".estrutura.json")
    )
    selecionados = [p for p in brutos if parece_acordao(p)]
    return selecionados, len(brutos) - len(selecionados)


def main() -> int:
    ap = argparse.ArgumentParser(description="Segmenta acordao em secoes e separa voz propria de voz citada.")
    ap.add_argument("arquivos", nargs="*", help="arquivos .md de acordao (normalmente em raw/)")
    ap.add_argument("--bundle", help="restringe a um bundle")
    ap.add_argument("--todos", action="store_true", help="varre raw/*.md do acervo, filtrando o que parece acordao")
    ap.add_argument("--acordaos", action="store_true", help="segmenta o raw: citado por cada pagina `type: acordao`")
    ap.add_argument("--resumo", action="store_true", help="imprime sem gravar o sidecar")
    args = ap.parse_args()

    lista, ignorados = alvos(args)
    if not lista:
        ap.error("nenhum arquivo informado (use caminhos, --acordaos, --bundle ou --todos)")

    print(f"segmentar-acordao: {len(lista)} arquivo(s)"
          + (f" ({ignorados} arquivo(s) de raw/ ignorados por nao serem acordao)" if ignorados else "")
          + "\n")
    falhas = 0
    for caminho in lista:
        if not caminho.exists():
            print(f"  ERRO {caminho}: nao existe.")
            falhas += 1
            continue
        try:
            res = segmentar(caminho)
        except Exception as e:  # noqa: BLE001 — o lote nao pode parar num arquivo ruim
            print(f"  ERRO {caminho.name}: {e}")
            falhas += 1
            continue

        imprimir(res)
        if not args.resumo:
            destino = caminho.with_suffix(caminho.suffix + ".estrutura.json")
            destino.write_text(json.dumps(res, ensure_ascii=False, indent=2), encoding="utf-8")
            print(f"    -> {destino.name}")
        if res["nao_segmentado"]:
            falhas += 1
        print()

    print(f"{len(lista) - falhas} segmentado(s), {falhas} sem estrutura ou com erro.")
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
