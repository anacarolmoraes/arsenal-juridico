# Perfis de juízo de primeiro grau (petição inicial)

Padrões **públicos** de julgamento das varas que recebem as iniciais do escritório: como tratam a
gratuidade, a tutela em golpe bancário, o valor da causa, e quanto tempo levam até o primeiro
despacho. O Estágio 0 do `legal-orchestrator` lê o perfil quando a comarca da peça coincide; o
perfil só existe quando há observação para registrar (`n` declarado). Nunca dado pessoal de
magistrado.

Os perfis de **segundo grau** ficam no bundle temático (`bancario/emprestimo-nao-realizado/perfis/`,
`bancario/golpes/perfis/`), porque o padrão de câmara é por matéria. O de primeiro grau fica aqui
porque o que se observa (gratuidade, emenda, tutela no despacho inicial) é da peça, não do tema.

## Onde começar

Contagem na fila do DJEN em 08/09/2026 (`skills/pesquisa-djen/scripts/orgaos-frequentes.js`),
processos distintos por órgão de 1º grau:

| Processos | Órgão |
|---|---|
| 92 | TJTO / 3º Núcleo de Justiça 4.0, Apoio Cível |
| 57 | TJTO / 5º Núcleo de Justiça 4.0, Apoio ao Sistema dos Juizados Especiais |
| 21 | TJTO / Secretaria Judicial Unificada das Varas Cíveis de Palmas |
| 6 | TJTO / 2ª Vara Cível de Porto Nacional |
| 4 | TJTO / 1ª Vara Cível de Palmas |
| 2 | TJTO / 3ª Vara Cível de Gurupi |

Os Núcleos de Justiça 4.0 concentram o volume, mas são unidades de apoio: o perfil que interessa
é o do juízo que decide (a vara de origem), e é ela que se anota no perfil.

## Perfis

Nenhum escrito ainda. Modelo: [_template-perfil-vara.md](_template-perfil-vara.md). Fontes para
alimentar: `casos_decididos/` dos bundles temáticos, a fila do DJEN
(`skills/pesquisa-djen/monitor/`), e os despachos de emenda minerados
(`skills/pesquisa-djen/scripts/minerar-emendas.js`), que já mostram, por exemplo, que a **1ª Vara
Cível de Palmas** pediu comprovante de endereço em nome próprio e prova da insuficiência de
recursos em despachos de 2025.
