# Log

## 2026-09-13

**Lei 13.709/2018 depositada** (transversal `direito/pecas/raw/lgpd-l13709-2018-compilada.{html,md}`, `depositar-lei.py`, cobertura até a Lei 15.352, 64 artigos, sem riscado; 1 artigo de 1 a 9 sem indicador ordinal no HTML). Vinda de `consumir/` do workspace. Fecha a pendência que travava o bundle; nenhuma página derivada ainda, porque nenhum caso puxou artigo. `index.md` e `raw/index.md` atualizados com o comando de recorte.

## 2026-08-29

**Criação do bundle (v0.1.0).** Semente a partir de `consumir/LGPD/`, parado desde 01/08/2026. O
roteador já previa `direito/lgpd/` como planejado e vazio, desde que o acervo `direito_digital` migrou
para `digital/plataformas` em 02/08/2026.

**Nasce fraco, e o index declara isso na abertura.** A Lei 13.709/2018 **não está depositada** — sem o
literal, nenhuma página pode transcrever artigo nem subir a `vigente` pelo portão E4. A matéria jurídica
central (bases legais, hipóteses de tratamento, incidentes, sanções) **não está coberta**. Preferi
registrar a lacuna a preencher o bundle com paráfrase de lei não depositada, que é exatamente o erro que
a regra da granularidade existe para impedir.

**Duas fontes depositadas, com regimes opostos.** A **cartilha de segurança da informação** (maio/2021)
é obra autoral da titular — circula na equipe, excluída de pacote externo (camada 2). O **infográfico
sobre LGPD em cartórios** é coluna assinada por terceiro (Joelson Sell): fora do git (camada 1). A
conversão deste último saiu por OCR e o texto em duas colunas ficou **entrelaçado em vários pontos** —
legível, mas fora de ordem; anotado no catálogo que não se cita sem conferir o PDF. Sem página derivada:
serventia extrajudicial é tangencial à prática do escritório, e as referências que ele traz (art. 23,
§ 4º, da LGPD; Provimentos CNJ 74/2018 e 50/2015) não foram conferidas em fonte oficial.

**Uma página derivada, e ela vale por si:**
[`heuristicas/engenharia-social-as-alavancas`](heuristicas/engenharia-social-as-alavancas.md). A cartilha
cataloga **dez** alavancas psicológicas (confiança, ignorância, medo, ambição, dever legal, curiosidade,
urgência, pânico, raiva e vistas pessoais) e a premissa de que o elo mais fraco da segurança são as
pessoas. O achado é o uso forense: em ação de golpe bancário, o contra-ataque padrão do banco é culpa
exclusiva da vítima, e nomear a alavanca acionada **reclassifica o fato** — de consumidor descuidado
para consumidor induzido por técnica catalogada e conhecida do setor. A página amarra isso ao eixo que
já vence em [`bancario/golpes/`](../bancario/golpes/index.md), o defeito do serviço por operação fora do
perfil de consumo (REsp 2.222.059/SP), e adverte contra o erro de parar na alavanca: ela neutraliza a
culpa exclusiva, não substitui o fundamento. Nasce `em_teste` — a fonte é material de formação interna,
não fonte jurídica.

**Pendências:** depositar a Lei 13.709/2018 (destrava o resto); conferir os Provimentos CNJ 74/2018 e
50/2015 em fonte oficial; a cartilha é de 2021 e traz marcos vencidos.
