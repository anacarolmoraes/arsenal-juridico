# Ligaduras — tese Buril (2026-08-29)

O `reparar-ligaduras.py` propos 3 formas, 4 substituicoes. Adotadas DUAS:

    fi eld     -> field
    fi nances  -> finances

REJEITADA a terceira, por ser FALSO POSITIVO:

    plaintiff presented -> plaintiffpresented   (2 ocorrencias)

"plaintiff" e "presented" sao duas palavras inglesas legitimas, em citacao de
doutrina estadunidense; a heuristica do script leu o par como palavra partida
por ligadura. Aplicar o reparo automatico teria corrompido o texto. Por isso o
arquivo .reparado.md foi descartado e as duas correcoes validas foram aplicadas
a mao ao .md canonico.

Segunda passagem, mesma sessao: o script so enxerga a forma ASCII ("fi eld").
O PDF trazia tambem o CARACTERE de ligadura tipografica U+FB01 ("fieeld"), que
passou incolume — 6 ocorrencias, todas em citacao em ingles de Seidman: duas
partidas por espaco ("fi eld", "fi nances") e quatro integras ("specific",
"find", "field", "find"). Normalizadas a mao para os digrafos ASCII, para que
busca por "field" ou "find" encontre o trecho. Verificado que nao havia
U+FB02/FB00/FB03/FB04 remanescentes.

Licao: neste documento a extracao nativa e limpa (4 substituicoes em 2,3 milhoes
de caracteres, contra 192 formas no RISTJ consolidado) — quando o volume de
propostas e baixo, a chance de o que sobra ser falso positivo e alta. Conferir
sempre, nunca adotar em bloco.
