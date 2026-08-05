# Perguntas e Insights da Análise Final

Este documento registra as perguntas de negócio, os métodos utilizados e as conclusões obtidas a partir da base tratada.

O notebook mostra os cálculos detalhados; este arquivo apresenta a linha de pensamento e os resultados relevantes para o negócio.

## 1. Qual foi o desempenho geral do negócio?

### Pergunta de Negócio
Qual foi o resultado geral da empresa no período analisado em termos de faturamento, lucro, margem, volume de vendas e pedidos?

### Método de Investigação
- Criação da função `calcular_kpis`.
- Cálculo de:
  - faturamento total;
  - lucro total;
  - margem global;
  - quantidade vendida;
  - pedidos únicos;
  - ticket médio.

### Resultado
- Faturamento total: aproximadamente US$ 2,30 milhões.
- Lucro total: aproximadamente US$ 286,40 mil.
- Margem global: 12,47%.
- Quantidade vendida: 37.873 unidades.
- Pedidos únicos: 5.009.
- Ticket médio: US$ 458,61 por pedido.

### Insight
A empresa apresentou lucro no resultado acumulado. Para cada US$ 100 faturados, aproximadamente US$ 12,47 permaneceram como lucro.

O resultado geral positivo não significa que todas as categorias, regiões ou vendas individuais foram lucrativas. Os indicadores gerais precisam ser detalhados para revelar problemas internos.

### Status
Confirmado.

## 2. Como faturamento, lucro e margem evoluíram ao longo dos anos?

### Pergunta de Negócio
O desempenho financeiro da empresa evoluiu de forma consistente entre 2014 e 2017?

### Método de Investigação
- Agrupamento dos dados pela coluna `ano`.
- Soma de `Sales`, `Profit` e `Quantity` em cada ano.
- Contagem de pedidos únicos com `Order ID`.
- Cálculo da margem global e do ticket médio de cada ano.
- Cálculo das variações anuais de faturamento e lucro com `pct_change()`.

### Resultado
- 2014:
  - faturamento de aproximadamente US$ 484,25 mil;
  - lucro de aproximadamente US$ 49,54 mil;
  - margem global de 10,23%.
- 2015:
  - faturamento de aproximadamente US$ 470,53 mil;
  - lucro de aproximadamente US$ 61,62 mil;
  - margem global de 13,10%.
- 2016:
  - faturamento de aproximadamente US$ 609,21 mil;
  - lucro de aproximadamente US$ 81,80 mil;
  - margem global de 13,43%.
- 2017:
  - faturamento de aproximadamente US$ 733,22 mil;
  - lucro de aproximadamente US$ 93,44 mil;
  - margem global de 12,74%.
- Variação de 2014 para 2015:
  - faturamento: -2,83%;
  - lucro: +24,37%.
- Variação de 2015 para 2016:
  - faturamento: +29,47%;
  - lucro: +32,74%.
- Variação de 2016 para 2017:
  - faturamento: +20,36%;
  - lucro: +14,24%.

### Insight
O lucro aumentou em todos os anos, mas o faturamento não: em 2015, o faturamento ficou abaixo de 2014 enquanto o lucro e a margem aumentaram.

O ano de 2016 apresentou a maior margem global. O ano de 2017 teve o maior faturamento e o maior lucro, mas sua margem ficou abaixo das margens de 2015 e 2016. Isso mostra que maior resultado financeiro absoluto não significa necessariamente maior eficiência.

Em 2015 e 2016, o lucro cresceu mais rapidamente que o faturamento, contribuindo para o aumento da margem. Em 2017, o lucro cresceu mais lentamente que o faturamento, o que ajuda a explicar a redução da margem global.

### Status
Confirmado.

## 3. O crescimento do faturamento acompanhou o aumento do volume de vendas?

### Pergunta de Negócio
O aumento da quantidade vendida e do número de pedidos resultou sempre em maior faturamento?

### Método de Investigação
- Comparação anual entre:
  - faturamento total;
  - quantidade vendida;
  - pedidos únicos;
  - ticket médio.

### Resultado
- A quantidade vendida e o número de pedidos aumentaram em todos os anos.
- Em 2015, a quantidade passou de 7.581 para 7.979 unidades e os pedidos passaram de 969 para 1.038, mas o faturamento diminuiu.
- O ticket médio caiu de US$ 499,74 em 2014 para US$ 453,31 em 2015.
- Em 2017, o ticket médio atingiu o menor valor do período, US$ 434,63, enquanto o faturamento atingiu o maior valor.

### Insight
Vender mais unidades ou receber mais pedidos não garante, sozinho, maior faturamento. Em 2015, o aumento do volume foi acompanhado por uma queda no valor médio dos pedidos.

Em 2017, o crescimento expressivo do número de pedidos e da quantidade vendida foi suficiente para gerar o maior faturamento do período, mesmo com o menor ticket médio.

### Status
Confirmado.

## 4. Por que a margem melhorou em 2015 mesmo com menor faturamento?

### Pergunta de Negócio
Quais fatores fizeram o lucro e a margem aumentarem em 2015, apesar da redução do faturamento e do ticket médio?

### Método de Investigação
- Comparação de 2014 e 2015 por categoria.
- Identificação da categoria com maior aumento de lucro e margem global.
- Filtro das vendas de `Technology`.
- Comparação das subcategorias de `Technology` entre 2014 e 2015.
- Agrupamento das vendas de `Technology` por `ano` e `faixa_desconto`.
- Cálculo das diferenças de faturamento, lucro, margem global e pedidos entre 2014 e 2015.

### Resultado
- O faturamento diminuiu de aproximadamente US$ 484,25 mil para US$ 470,53 mil.
- O lucro aumentou de aproximadamente US$ 49,54 mil para US$ 61,62 mil.
- A margem global aumentou de 10,23% para 13,10%.
- O ticket médio diminuiu de US$ 499,74 para US$ 453,31.
- Em relação a 2014, o faturamento caiu 2,83% e o lucro cresceu 24,37%.
- `Technology` foi a categoria com o maior aumento de lucro e a maior melhora de margem:
  - o faturamento caiu de aproximadamente US$ 175,28 mil para US$ 162,78 mil;
  - o lucro aumentou de aproximadamente US$ 21,49 mil para US$ 33,50 mil;
  - a margem global aumentou de 12,26% para 20,58%, uma melhora de 8,32 pontos percentuais.
- Entre as subcategorias de `Technology`, `Copiers` apresentou o maior aumento de lucro, com aproximadamente US$ 7,02 mil adicionais.
- Na comparação por faixa de desconto:
  - as vendas sem desconto aumentaram o faturamento em aproximadamente US$ 20,29 mil e o lucro em US$ 7,49 mil;
  - as vendas com desconto alto tiveram redução de aproximadamente US$ 8,71 mil no faturamento, mas aumentaram o lucro em US$ 4,71 mil e a margem em 6,96 pontos percentuais;
  - as vendas com desconto agressivo tiveram redução de aproximadamente US$ 24,08 mil no faturamento, piora de US$ 190,31 no lucro e queda de 93,01 pontos percentuais na margem.

### Insight
A melhora da margem global em 2015 esteve associada principalmente ao desempenho de `Technology`, especialmente de `Copiers`.

Dentro de `Technology`, o maior aumento de lucro veio das vendas sem desconto. As vendas com desconto alto também contribuíram, pois aumentaram o lucro e a margem mesmo com menor faturamento.

Os descontos agressivos continuaram prejudiciais e não explicam a melhora da categoria. Mesmo com menor volume financeiro, essa faixa permaneceu com lucro e margem negativos.

### Status
Confirmado dentro do recorte de categorias, subcategorias e faixas de desconto.

## 5. Quais meses apresentaram o pior desempenho?

### Pergunta de Negócio
Quais meses tiveram prejuízo e por que o ticket médio, sozinho, não é suficiente para avaliar o desempenho mensal?

### Método de Investigação
- Agrupamento dos dados pelas colunas `ano` e `mes`.
- Cálculo mensal de:
  - faturamento total;
  - lucro total;
  - quantidade vendida;
  - pedidos únicos;
  - margem global;
  - ticket médio.
- Cálculo da variação do faturamento com `pct_change()`.
- Cálculo da diferença absoluta do lucro com `diff()`.
- Filtragem dos meses com `lucro_total < 0`.
- Criação de rankings de lucro e margem global com `sort_values()`.

### Resultado
- Julho de 2014:
  - faturamento de aproximadamente US$ 33,95 mil;
  - prejuízo de aproximadamente US$ 841,48;
  - margem global de -2,48%;
  - 550 unidades vendidas;
  - 65 pedidos;
  - ticket médio de US$ 522,25.
- Janeiro de 2015:
  - faturamento de aproximadamente US$ 18,17 mil;
  - prejuízo de aproximadamente US$ 3,28 mil;
  - margem global de -18,05%;
  - 236 unidades vendidas;
  - 29 pedidos;
  - ticket médio de US$ 626,69.
- Fevereiro de 2014 apresentou lucro total baixo, mas margem global positiva de 19,08%.
- Novembro de 2016 apresentou faturamento elevado, mas margem global de apenas 5,05%.

### Insight
Janeiro de 2015 foi o mês mais crítico, pois apresentou simultaneamente o maior prejuízo e a pior margem global.

Seu ticket médio foi superior ao de julho de 2014, mas isso não representou melhor desempenho. Um pedido pode ter valor médio elevado e ainda gerar prejuízo.

Lucro e margem também precisam ser interpretados em conjunto. Um lucro total baixo pode ser explicado por pouco volume, enquanto uma margem baixa indica que pouco lucro foi gerado em relação ao faturamento.

### Status
Confirmado.

## 6. Qual categoria apresentou a menor eficiência financeira?

### Pergunta de Negócio
Qual categoria apresentou a relação mais fraca entre faturamento e lucro, e quais subcategorias podem estar reduzindo seu desempenho?

### Método de Investigação
- Aplicação da função `resumir_por_grupo` na coluna `Category`.
- Comparação entre:
  - faturamento total;
  - lucro total;
  - quantidade vendida;
  - pedidos únicos;
  - margem global;
  - ticket médio.
- Aplicação da função `resumir_por_grupo` na coluna `Sub-Category`.
- Identificação das subcategorias lucrativas e deficitárias de `Furniture`.

### Resultado
- Technology:
  - faturamento de aproximadamente US$ 836,15 mil;
  - lucro de aproximadamente US$ 145,45 mil;
  - margem global de 17,40%.
- Office Supplies:
  - faturamento de aproximadamente US$ 719,05 mil;
  - lucro de aproximadamente US$ 122,49 mil;
  - margem global de 17,04%.
- Furniture:
  - faturamento de aproximadamente US$ 742,00 mil;
  - lucro de aproximadamente US$ 18,45 mil;
  - margem global de 2,49%.
- Dentro de `Furniture`:
  - `Tables` apresentou prejuízo de aproximadamente US$ 17,73 mil e margem global de -8,56%;
  - `Bookcases` apresentou prejuízo de aproximadamente US$ 3,47 mil e margem global de -3,02%;
  - `Chairs` e `Furnishings` apresentaram lucro positivo e compensaram parte das perdas.

### Insight
Technology apresentou o maior faturamento, o maior lucro e a melhor margem global.

Furniture faturou mais que Office Supplies, mas gerou um lucro consideravelmente menor. Sua margem de 2,49%, comparada a 17,04% de Office Supplies, evidencia baixa eficiência financeira.

`Tables` é a principal causa da baixa eficiência financeira de `Furniture`, com contribuição negativa adicional de `Bookcases`. As subcategorias lucrativas evitam que a categoria termine com prejuízo, mas não são suficientes para produzir uma margem alta.

### Status
Confirmado.

## 7. Qual região apresentou o melhor desempenho e qual teve a menor eficiência?

### Pergunta de Negócio
Como faturamento, lucro e margem se distribuíram entre as regiões, e existe alguma região com faturamento relevante, mas baixa eficiência financeira?

### Método de Investigação
- Aplicação da função `resumir_por_grupo` na coluna `Region`.
- Comparação entre:
  - faturamento total;
  - lucro total;
  - quantidade vendida;
  - pedidos únicos;
  - margem global;
  - ticket médio.

### Resultado
- West:
  - faturamento de aproximadamente US$ 725,46 mil;
  - lucro de aproximadamente US$ 108,42 mil;
  - margem global de 14,94%.
- East:
  - faturamento de aproximadamente US$ 678,78 mil;
  - lucro de aproximadamente US$ 91,52 mil;
  - margem global de 13,48%.
- Central:
  - faturamento de aproximadamente US$ 501,24 mil;
  - lucro de aproximadamente US$ 39,71 mil;
  - margem global de 7,92%.
- South:
  - faturamento de aproximadamente US$ 391,72 mil;
  - lucro de aproximadamente US$ 46,75 mil;
  - margem global de 11,93%.

### Insight
West apresentou o melhor desempenho regional, reunindo o maior faturamento, o maior lucro e a melhor margem global.

Central faturou mais que South, mas gerou menos lucro e apresentou a menor margem entre as regiões. Isso indica que seu volume financeiro não foi convertido em lucro com a mesma eficiência observada nas demais regiões.

### Status
Confirmado.

## 8. Qual segmento apresentou maior resultado e qual foi o mais eficiente?

### Pergunta de Negócio
O segmento com maior faturamento e lucro também apresentou a melhor margem e o maior ticket médio?

### Método de Investigação
- Aplicação da função `resumir_por_grupo` na coluna `Segment`.
- Comparação entre:
  - faturamento total;
  - lucro total;
  - quantidade vendida;
  - pedidos únicos;
  - margem global;
  - ticket médio.

### Resultado
- Consumer:
  - faturamento de aproximadamente US$ 1,16 milhão;
  - lucro de aproximadamente US$ 134,12 mil;
  - margem global de 11,55%;
  - ticket médio de US$ 449,11.
- Corporate:
  - faturamento de aproximadamente US$ 706,15 mil;
  - lucro de aproximadamente US$ 91,98 mil;
  - margem global de 13,03%;
  - ticket médio de US$ 466,41.
- Home Office:
  - faturamento de aproximadamente US$ 429,65 mil;
  - lucro de aproximadamente US$ 60,30 mil;
  - margem global de 14,03%;
  - ticket médio de US$ 472,67.

### Insight
Consumer concentrou o maior faturamento, lucro e volume de vendas, mas apresentou a menor margem global entre os segmentos.

Home Office teve o menor faturamento e lucro total, porém apresentou a melhor margem e o maior ticket médio. Portanto, o segmento com maior resultado absoluto não foi o mais eficiente proporcionalmente.

### Status
Confirmado.
