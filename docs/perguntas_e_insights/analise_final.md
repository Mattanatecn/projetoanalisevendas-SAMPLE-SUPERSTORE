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

### Método de Investigação Planejado
- Comparar 2014 e 2015 por:
  - categorias e subcategorias vendidas;
  - faixas de desconto;
  - regiões;
  - lucro e margem global.
- Verificar se houve mudança na combinação de produtos vendidos ou redução de vendas com prejuízo.

### Resultado Parcial
- O faturamento diminuiu de aproximadamente US$ 484,25 mil para US$ 470,53 mil.
- O lucro aumentou de aproximadamente US$ 49,54 mil para US$ 61,62 mil.
- A margem global aumentou de 10,23% para 13,10%.
- O ticket médio diminuiu de US$ 499,74 para US$ 453,31.
- Em relação a 2014, o faturamento caiu 2,83% e o lucro cresceu 24,37%.

### Insight Parcial
Os dados confirmam uma melhora de eficiência em 2015, mas ainda não explicam sua causa. Descontos, combinação de produtos e desempenho regional permanecem como hipóteses de investigação.

### Status
Em investigação.
