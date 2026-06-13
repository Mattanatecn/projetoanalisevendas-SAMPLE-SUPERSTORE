# Devlog - Projeto de Analise de Vendas Superstore

Este arquivo registra a evolucao do projeto, as decisoes tomadas, os aprendizados tecnicos e os principais insights de negocio.

## 2026-05-09 - Dia 1: Pensamento Analitico e Exploracao Inicial

### Objetivos
- Compreender o contexto de negocio do dataset.
- Realizar a primeira exploracao de dados via Excel.
- Identificar padroes de lucro e prejuizo.

### Atividades Realizadas
- Entendimento das colunas do dataset e definicao dos primeiros KPIs: vendas, lucro e ticket medio.
- Estruturacao dos dados em Tabela Oficial no Excel (`Ctrl + T`) para garantir integridade e escalabilidade.
- Criacao de Tabelas Dinamicas para comparar regioes e categorias.
- Identificacao da regiao `West` como a mais lucrativa e da regiao `South` como a menos performante.
- Comparacao entre categorias, com destaque para `Technology` como categoria de alta margem e `Furniture` como categoria de volume alto e margem mais baixa.
- Inicio da investigacao de causa raiz na categoria `Furniture`, identificando `Tables` como principal fonte de prejuizo.
- Cruzamento entre `Discount` e `Profit`, indicando que descontos em mesas estavam associados a lucro negativo.

### Principais Insights
- O prejuizo em `Tables` nao parece estar ligado inicialmente a logistica, mas a uma estrategia comercial de descontos agressivos.
- A recomendacao preliminar foi revisar promocoes e politica de preco para mesas.

### Bloqueios e Aprendizados
- Houve dificuldade inicial com formulas de soma no Excel.
- A dificuldade foi superada com uso da Barra de Status e Tabelas Dinamicas.

### Proximos Passos
- Implementar a arquitetura do dashboard no Excel: KPIs, graficos e slicers.
- Transformar a analise de `Tables` em um insight visual no dashboard.

## 2026-05-22 - Dia 2: Finalizacao do Dashboard e Storytelling de Dados

### Objetivos
- Finalizar a camada visual do dashboard executivo.
- Implementar visualmente a analise de causa raiz.
- Garantir interatividade entre filtros, KPIs e graficos.

### Atividades Realizadas
- Criacao do grafico de rentabilidade por categoria.
- Criacao do grafico de subcategorias com lucro negativo.
- Desenvolvimento do grafico de correlacao entre desconto e lucro para `Tables`.
- Configuracao de slicers por regiao, categoria e segmento.
- Conexao dos slicers com os relatorios para atualizacao simultanea dos visuais.
- Correcao dos KPIs estaticos por meio de vinculos com Tabelas Dinamicas.
- Implementacao da tecnica de celula ponte e uso da funcao `INFODADOSTABELADINAMICA` (`GETPIVOTDATA`) para estabilizar os KPIs mesmo com filtros ativos.

### Principais Insights
- O dashboard passou a conduzir a narrativa de dados em etapas:
  - sinal de alerta por KPIs;
  - localizacao do problema por subcategoria;
  - causa raiz por desconto;
  - recomendacao de acao.

### Proximos Passos
- Migrar a analise para o VS Code.
- Replicar a logica de analise com Python e Pandas.
- Evoluir visualizacoes com bibliotecas como Seaborn, Matplotlib e Plotly.
- Transformar a analise em um web app com Streamlit.

## 2026-05-26 - Dia 3: Configuracao de Ambiente e Versionamento

### Objetivos
- Migrar o projeto para o VS Code.
- Estabelecer uma arquitetura de pastas profissional.
- Configurar ambiente virtual Python e versionamento com Git/GitHub.

### Atividades Realizadas
- Criacao da estrutura de pastas do projeto:
  - `dados/`
  - `notebooks/`
  - `src/`
  - `dashboard/`
  - `imagens/`
- Criacao e ativacao de ambiente virtual (`.venv`).
- Instalacao das principais bibliotecas de analise de dados:
  - `pandas`
  - `matplotlib`
  - `seaborn`
  - `plotly`
  - `streamlit`
- Configuracao do `.gitignore` para evitar versionamento de ambientes virtuais e arquivos temporarios.
- Inicializacao do repositorio Git.
- Primeiro commit da estrutura do projeto.
- Conexao com repositorio remoto no GitHub.
- Migracao do dataset original e da analise em Excel para `dados/bruto`.

### Proximos Passos
- Iniciar a exploracao em `notebooks/exploracao.ipynb`.
- Traduzir a logica da analise do Excel para Pandas.
- Replicar a analise de causa raiz de `Tables` usando codigo Python.

## 2026-05-31 - Dia 4: Migracao da Analise para Pandas

### Objetivos
- Iniciar a exploracao de dados no Jupyter Notebook.
- Replicar os KPIs globais do Excel em Pandas.
- Identificar a subcategoria com maior impacto negativo no lucro.

### Atividades Realizadas
- Leitura do CSV com `pd.read_csv`.
- Ajuste de caminhos relativos para funcionar a partir da pasta `notebooks`.
- Tratamento de erro de decodificacao com `encoding='latin1'`.
- Calculo de vendas totais.
- Calculo de lucro total.
- Criacao de filtro booleano para isolar vendas com prejuizo.
- Investigacao de divergencias entre Excel e Pandas.
- Identificacao de problema de formatacao no Excel por casas decimais ocultas.
- Uso de `groupby` por `Sub-Category` para ranquear lucro por subcategoria.
- Confirmacao de `Tables` como principal detrator do lucro total.
- Criacao da branch `feature/exploracao-pandas` para trabalhar sem alterar diretamente a branch principal.

### Aprendizados Tecnicos
- Caminhos no Windows podem gerar erros por sequencias de escape.
- Arquivos vindos do Excel/Windows podem exigir `latin1` em vez de `utf-8`.
- Filtros e agregacoes respondem perguntas diferentes.
- A validacao entre Excel e Pandas ajuda a identificar problemas de interpretacao e arredondamento.

### Proximos Passos
- Realizar a analise de causa raiz de `Tables` cruzando `Discount` com `Profit`.
- Iniciar a transicao da exploracao para `src/limpeza.py`.
- Gerar futuramente um dataset tratado em `dados/tratado`.

## 2026-06-04 - Dia 5: Prova da Causa Raiz e Inicio da Limpeza

### Objetivos
- Provar matematicamente a causa raiz do prejuizo em `Tables` usando Pandas.
- Iniciar o processo de limpeza e tratamento dos dados.
- Documentar o notebook como material de aprendizado.

### Atividades Realizadas
- Isolamento da subcategoria `Tables`.
- Criacao de grupos de comparacao:
  - vendas de mesas com desconto maior ou igual a 20%;
  - vendas de mesas com desconto menor que 20%.
- Validacao estatistica da hipotese:
  - descontos altos em `Tables`: aproximadamente -31 mil de lucro;
  - descontos baixos em `Tables`: aproximadamente 13 mil de lucro.
- Conversao de `Order Date` e `Ship Date` de texto para `datetime`.
- Revisao do notebook com comentarios explicativos sobre a logica tecnica e a logica de negocio.

### Principais Insights
- A relacao entre descontos agressivos e prejuizo em `Tables` foi confirmada no Python.
- A conversao de datas e um passo essencial para futuras analises temporais e de prazo de entrega.

### Proximos Passos
- Verificar valores nulos com `.isnull().sum()`.
- Criar visualizacoes para comunicar a causa raiz.
- Migrar os passos de limpeza para `src/limpeza.py`.

## 2026-06-13 - Dia 6: Analise de Prazo de Envio e Margem

### Objetivos
- Investigar se o prazo de envio possui relacao com prejuizo.
- Criar uma metrica de margem de lucro por venda.
- Comparar lucro total, margem media e volume de vendas por subcategoria.
- Identificar novas hipoteses de causa raiz alem de `Tables`.

### Atividades Realizadas
- Verificacao de valores nulos com `df.isnull().sum()`.
- Confirmacao de ausencia de valores nulos no dataset.
- Criacao da coluna `dias_envio`, calculada pela diferenca entre `Ship Date` e `Order Date`.
- Analise de lucro por prazo de envio usando `groupby('dias_envio')`.
- Criacao da coluna `margem_lucro`, calculada por `Profit / Sales`.
- Analise da margem media por subcategoria.
- Criacao de uma tabela resumo por subcategoria contendo:
  - total de vendas;
  - lucro total;
  - margem media.

### Principais Insights
- O prazo de envio nao apresentou relacao direta com prejuizo nesta primeira analise.
- Todos os grupos de `dias_envio`, de 0 a 7 dias, apresentaram lucro total e lucro medio positivos.
- `Tables` continua sendo a subcategoria mais critica em impacto financeiro, com lucro total de aproximadamente -17,7 mil.
- `Bookcases` tambem apresentou lucro total negativo e margem media negativa.
- `Binders` apresentou margem media negativa, mas lucro total positivo, indicando uma possivel combinacao de muitas vendas pequenas pouco eficientes com vendas maiores lucrativas.
- `Appliances` tambem apresentou margem media negativa, apesar de lucro total positivo.
- A analise mostrou a diferenca entre duas leituras importantes:
  - margem media mede eficiencia;
  - lucro total mede impacto financeiro.

### Hipoteses em Aberto
- `Tables` segue como prioridade pela combinacao de prejuizo total alto e descontos agressivos ja identificados.
- `Binders` sera investigada em seguida para entender se a margem media negativa vem de muitas vendas pequenas com prejuizo compensadas por vendas maiores lucrativas.

### Proximos Passos
- Investigar `Binders` separando vendas com lucro negativo e vendas com lucro positivo.
- Comparar quantidade de vendas, valor medio de venda, lucro total e margem media nos dois grupos.
- Depois da exploracao, consolidar as transformacoes estaveis em `src/limpeza.py`.
- Gerar o primeiro arquivo tratado em `dados/tratado`.
