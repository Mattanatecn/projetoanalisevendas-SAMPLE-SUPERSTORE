# Perguntas e Insights

Este documento registra as principais perguntas de negocio, hipoteses investigadas, metodos utilizados e conclusoes do projeto.

O objetivo e separar o raciocinio analitico dos codigos exploratorios. O notebook mostra os calculos; este arquivo mostra a linha de pensamento da analise.

## 1. Qual subcategoria mais prejudica o lucro total?

### Pergunta de Negocio
Qual subcategoria possui o maior impacto negativo no lucro da empresa?

### Metodo de Investigacao
- Agrupamento dos dados por `Sub-Category`.
- Soma da coluna `Profit` para cada subcategoria.
- Ordenacao do resultado do menor lucro para o maior lucro.

### Resultado
`Tables` apresentou o pior lucro total entre as subcategorias, com aproximadamente -17,7 mil.

### Insight
`Tables` e a principal subcategoria detratora de lucro no resultado acumulado.

### Status
Confirmado.

## 2. O desconto explica o prejuizo em Tables?

### Pergunta de Negocio
Os descontos aplicados em `Tables` estao relacionados ao prejuizo da subcategoria?

### Metodo de Investigacao
- Filtro da base para manter apenas vendas da subcategoria `Tables`.
- Separacao das vendas em dois grupos:
  - desconto maior ou igual a 20%;
  - desconto menor que 20%.
- Comparacao do lucro total entre os dois grupos.

### Resultado
- Vendas de `Tables` com desconto maior ou igual a 20% tiveram aproximadamente -31 mil de lucro.
- Vendas de `Tables` com desconto menor que 20% tiveram aproximadamente 13 mil de lucro.

### Insight
Os descontos agressivos sao um forte indicio da causa raiz do prejuizo em `Tables`.

### Status
Confirmado.

## 3. O prazo de envio esta relacionado ao prejuizo?

### Pergunta de Negocio
Pedidos com maior prazo de envio geram mais prejuizo?

### Metodo de Investigacao
- Conversao das colunas `Order Date` e `Ship Date` para formato de data.
- Criacao da coluna `dias_envio`, calculada pela diferenca entre `Ship Date` e `Order Date`.
- Agrupamento por `dias_envio`.
- Calculo de quantidade de vendas, lucro total e lucro medio por prazo de envio.

### Resultado
Todos os prazos de envio, de 0 a 7 dias, apresentaram lucro total e lucro medio positivos.

### Insight
Nesta primeira analise, o prazo de envio nao parece explicar o prejuizo.

### Status
Hipotese descartada por enquanto.

## 4. Quais subcategorias possuem pior margem media?

### Pergunta de Negocio
Quais subcategorias vendem com pior eficiencia media de lucro?

### Metodo de Investigacao
- Criacao da coluna `margem_lucro`, calculada por `Profit / Sales`.
- Agrupamento por `Sub-Category`.
- Calculo da media de `margem_lucro`.
- Ordenacao das subcategorias da pior margem media para a melhor margem media.

### Resultado
As piores margens medias identificadas foram:
- `Binders`
- `Appliances`
- `Tables`
- `Bookcases`
- `Machines`

### Insight
`Tables` continua sendo critica pelo impacto financeiro total, mas `Binders` chamou atencao por apresentar margem media negativa mesmo com lucro total positivo.

### Status
Confirmado como sinal de investigacao.

## 5. Como comparar impacto financeiro e eficiencia?

### Pergunta de Negocio
Uma subcategoria com margem media ruim sempre e a maior fonte de prejuizo?

### Metodo de Investigacao
- Criacao de uma tabela resumo por `Sub-Category`.
- Calculo de:
  - total de vendas;
  - lucro total;
  - margem media.
- Ordenacao pelo lucro total.

### Resultado
- `Tables` apresentou o pior lucro total e margem media negativa.
- `Binders` apresentou margem media negativa, mas lucro total positivo.
- `Appliances` apresentou margem media negativa, mas lucro total positivo.
- `Bookcases` apresentou lucro total negativo e margem media negativa.

### Insight
Margem media e lucro total respondem perguntas diferentes:
- margem media mede eficiencia;
- lucro total mede impacto financeiro.

### Status
Confirmado.

## 6. Binders tem muitas vendas pequenas com prejuizo?

### Pergunta de Negocio
A margem media negativa de `Binders` vem de muitas vendas pequenas com prejuizo compensadas por vendas maiores lucrativas?

### Metodo de Investigacao Planejado
- Filtrar apenas vendas de `Binders`.
- Separar vendas com `Profit < 0` e vendas com `Profit >= 0`.
- Comparar:
  - quantidade de vendas;
  - vendas totais;
  - valor medio de venda;
  - lucro total;
  - margem media.

### Resultado
Ainda nao investigado.

### Insight
Pendente.

### Status
Proxima hipotese a investigar.
