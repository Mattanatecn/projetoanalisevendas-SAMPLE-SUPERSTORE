# Perguntas e Insights da Exploração Inicial

Este documento registra as principais perguntas de negócio, hipóteses investigadas, métodos utilizados e conclusões da exploração inicial.

O objetivo é preservar o raciocínio desenvolvido antes da base tratada. O notebook mostra os cálculos; este arquivo mostra a linha de pensamento da exploração.

## 1. Qual subcategoria mais prejudica o lucro total?

### Pergunta de Negócio
Qual subcategoria possui o maior impacto negativo no lucro da empresa?

### Método de Investigação
- Agrupamento dos dados por `Sub-Category`.
- Soma da coluna `Profit` para cada subcategoria.
- Ordenação do resultado do menor lucro para o maior lucro.

### Resultado
`Tables` apresentou o pior lucro total entre as subcategorias, com aproximadamente -17,7 mil.

### Insight
`Tables` é a principal subcategoria detratora de lucro no resultado acumulado.

### Status
Confirmado.

## 2. O desconto explica o prejuízo em Tables?

### Pergunta de Negócio
Os descontos aplicados em `Tables` estão relacionados ao prejuízo da subcategoria?

### Método de Investigação
- Filtro da base para manter apenas vendas da subcategoria `Tables`.
- Separação das vendas em dois grupos:
  - desconto maior ou igual a 20%;
  - desconto menor que 20%.
- Comparação do lucro total entre os dois grupos.

### Resultado
- Vendas de `Tables` com desconto maior ou igual a 20% tiveram aproximadamente -31 mil de lucro.
- Vendas de `Tables` com desconto menor que 20% tiveram aproximadamente 13 mil de lucro.

### Insight
Os descontos agressivos são um forte indício da causa raiz do prejuízo em `Tables`.

### Status
Confirmado.

## 3. O prazo de envio está relacionado ao prejuízo?

### Pergunta de Negócio
Pedidos com maior prazo de envio geram mais prejuízo?

### Método de Investigação
- Conversão das colunas `Order Date` e `Ship Date` para formato de data.
- Criação da coluna `dias_envio`, calculada pela diferença entre `Ship Date` e `Order Date`.
- Agrupamento por `dias_envio`.
- Cálculo de quantidade de vendas, lucro total e lucro médio por prazo de envio.

### Resultado
Todos os prazos de envio, de 0 a 7 dias, apresentaram lucro total e lucro médio positivos.

### Insight
Nesta primeira análise, o prazo de envio não parece explicar o prejuízo.

### Status
Hipótese descartada por enquanto.

## 4. Quais subcategorias possuem pior margem média?

### Pergunta de Negócio
Quais subcategorias vendem com pior eficiência média de lucro?

### Método de Investigação
- Criação da coluna `margem_lucro`, calculada por `Profit / Sales`.
- Agrupamento por `Sub-Category`.
- Cálculo da média de `margem_lucro`.
- Ordenação das subcategorias da pior margem média para a melhor margem média.

### Resultado
As piores margens médias identificadas foram:
- `Binders`
- `Appliances`
- `Tables`
- `Bookcases`
- `Machines`

### Insight
`Tables` continua sendo crítica pelo impacto financeiro total, mas `Binders` chamou atenção por apresentar margem média negativa mesmo com lucro total positivo.

### Status
Confirmado como sinal de investigação.

## 5. Como comparar impacto financeiro e eficiência?

### Pergunta de Negócio
Uma subcategoria com margem média ruim sempre é a maior fonte de prejuízo?

### Método de Investigação
- Criação de uma tabela resumo por `Sub-Category`.
- Cálculo de:
  - total de vendas;
  - lucro total;
  - margem média.
- Ordenação pelo lucro total.

### Resultado
- `Tables` apresentou o pior lucro total e margem média negativa.
- `Binders` apresentou margem média negativa, mas lucro total positivo.
- `Appliances` apresentou margem média negativa, mas lucro total positivo.
- `Bookcases` apresentou lucro total negativo e margem média negativa.

### Insight
Margem média e lucro total respondem perguntas diferentes:
- margem média mede eficiência;
- lucro total mede impacto financeiro.

### Status
Confirmado.

## 6. Binders tem muitas vendas pequenas com prejuízo?

### Pergunta de Negócio
A margem média negativa de `Binders` vem de muitas vendas pequenas com prejuízo compensadas por vendas maiores lucrativas?

### Método de Investigação Planejado
- Filtrar apenas vendas de `Binders`.
- Separar vendas com `Profit < 0` e vendas com `Profit >= 0`.
- Comparar:
  - quantidade de vendas;
  - vendas totais;
  - valor médio de venda;
  - lucro total;
  - margem média;
  - desconto médio.

### Resultado Parcial
- `Binders` com prejuízo:
  - 613 vendas;
  - aproximadamente 36,1 mil em vendas totais;
  - aproximadamente -38,5 mil de lucro;
  - margem média negativa;
  - desconto médio alto.
- `Binders` com lucro:
  - 910 vendas;
  - aproximadamente 167,3 mil em vendas totais;
  - aproximadamente 68,7 mil de lucro;
  - margem média positiva;
  - desconto médio menor.

### Insight
`Binders` possui um grupo relevante de vendas com prejuízo, mas as vendas lucrativas são maiores em volume financeiro e compensam as perdas.

O problema não está necessariamente na subcategoria inteira, mas em uma parte das vendas de `Binders`, especialmente nas vendas com prejuízo, menor ticket médio e desconto médio mais alto.

### Status
Confirmado como padrão interno da subcategoria.

## 7. Por que Tables fica negativa e Binders fica positiva?

### Pergunta de Negócio
Por que `Tables` fecha com lucro total negativo enquanto `Binders` fecha com lucro total positivo, mesmo que `Binders` também tenha um prejuízo acumulado alto nas vendas ruins?

### Método de Investigação
- Separação das vendas de cada subcategoria em dois grupos:
  - vendas com `Profit < 0`;
  - vendas com `Profit >= 0`.
- Comparação entre:
  - quantidade de vendas com lucro e com prejuízo;
  - lucro acumulado das vendas negativas;
  - lucro acumulado das vendas positivas;
  - lucro total final da subcategoria.

### Resultado
Em `Tables`:
- 203 vendas tiveram prejuízo;
- o prejuízo acumulado foi de aproximadamente -32,4 mil;
- 116 vendas tiveram lucro;
- o lucro acumulado positivo foi de aproximadamente 14,7 mil;
- o lucro total final ficou em aproximadamente -17,7 mil.

Em `Binders`:
- 613 vendas tiveram prejuízo;
- o prejuízo acumulado foi de aproximadamente -38,5 mil;
- 910 vendas tiveram lucro;
- o lucro acumulado positivo foi de aproximadamente 68,7 mil;
- o lucro total final ficou em aproximadamente 30,2 mil.

### Insight
`Tables` fica negativa porque o lucro das vendas boas não é suficiente para compensar o prejuízo das vendas ruins.

`Binders`, por outro lado, tem um prejuízo acumulado até maior que `Tables` nas vendas negativas, mas o lucro das vendas positivas supera esse prejuízo e mantém a subcategoria lucrativa no total.

### Conclusão Analítica
`Tables` é o problema mais crítico no resultado final, porque suas vendas lucrativas não compensam as perdas.

`Binders` exige atenção, mas por outro motivo: a subcategoria é lucrativa no total, porém possui um grupo interno de vendas ruins que reduz a eficiência e poderia estar diminuindo um lucro que seria ainda maior.

### Status
Confirmado.
