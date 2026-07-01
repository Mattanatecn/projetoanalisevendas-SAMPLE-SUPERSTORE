# Devlog - Projeto de Análise de Vendas Superstore

Este arquivo registra a evolução do projeto, as decisões tomadas, os aprendizados técnicos e os principais insights de negócio.

## 2026-05-09 - Dia 1: Pensamento Analítico e Exploração Inicial

### Objetivos
- Compreender o contexto de negócio do dataset.
- Realizar a primeira exploração de dados via Excel.
- Identificar padrões de lucro e prejuízo.

### Atividades Realizadas
- Entendimento das colunas do dataset e definição dos primeiros KPIs: vendas, lucro e ticket médio.
- Estruturação dos dados em Tabela Oficial no Excel (`Ctrl + T`) para garantir integridade e escalabilidade.
- Criação de Tabelas Dinâmicas para comparar regiões e categorias.
- Identificação da região `West` como a mais lucrativa e da região `South` como a menos performante.
- Comparação entre categorias, com destaque para `Technology` como categoria de alta margem e `Furniture` como categoria de volume alto e margem mais baixa.
- Início da investigação de causa raiz na categoria `Furniture`, identificando `Tables` como principal fonte de prejuízo.
- Cruzamento entre `Discount` e `Profit`, indicando que descontos em mesas estavam associados a lucro negativo.

### Principais Insights
- O prejuízo em `Tables` não parece estar ligado inicialmente à logística, mas a uma estratégia comercial de descontos agressivos.
- A recomendação preliminar foi revisar promoções e política de preço para mesas.

### Bloqueios e Aprendizados
- Houve dificuldade inicial com fórmulas de soma no Excel.
- A dificuldade foi superada com uso da Barra de Status e Tabelas Dinâmicas.

### Próximos Passos
- Implementar a arquitetura do dashboard no Excel: KPIs, gráficos e slicers.
- Transformar a análise de `Tables` em um insight visual no dashboard.

## 2026-05-22 - Dia 2: Finalização do Dashboard e Storytelling de Dados

### Objetivos
- Finalizar a camada visual do dashboard executivo.
- Implementar visualmente a análise de causa raiz.
- Garantir interatividade entre filtros, KPIs e gráficos.

### Atividades Realizadas
- Criação do gráfico de rentabilidade por categoria.
- Criação do gráfico de subcategorias com lucro negativo.
- Desenvolvimento do gráfico de correlação entre desconto e lucro para `Tables`.
- Configuração de slicers por região, categoria e segmento.
- Conexão dos slicers com os relatórios para atualização simultânea dos visuais.
- Correção dos KPIs estáticos por meio de vínculos com Tabelas Dinâmicas.
- Implementação da técnica de célula ponte e uso da função `INFODADOSTABELADINAMICA` (`GETPIVOTDATA`) para estabilizar os KPIs mesmo com filtros ativos.

### Principais Insights
- O dashboard passou a conduzir a narrativa de dados em etapas:
  - sinal de alerta por KPIs;
  - localização do problema por subcategoria;
  - causa raiz por desconto;
  - recomendação de ação.

### Próximos Passos
- Migrar a análise para o VS Code.
- Replicar a lógica de análise com Python e Pandas.
- Evoluir visualizações com bibliotecas como Seaborn, Matplotlib e Plotly.
- Transformar a análise em um web app com Streamlit.

## 2026-05-26 - Dia 3: Configuração de Ambiente e Versionamento

### Objetivos
- Migrar o projeto para o VS Code.
- Estabelecer uma arquitetura de pastas profissional.
- Configurar ambiente virtual Python e versionamento com Git/GitHub.

### Atividades Realizadas
- Criação da estrutura de pastas do projeto:
  - `dados/`
  - `notebooks/`
  - `src/`
  - `dashboard/`
  - `imagens/`
- Criação e ativação de ambiente virtual (`.venv`).
- Instalação das principais bibliotecas de análise de dados:
  - `pandas`
  - `matplotlib`
  - `seaborn`
  - `plotly`
  - `streamlit`
- Configuração do `.gitignore` para evitar versionamento de ambientes virtuais e arquivos temporários.
- Inicialização do repositório Git.
- Primeiro commit da estrutura do projeto.
- Conexão com repositório remoto no GitHub.
- Migração do dataset original e da análise em Excel para `dados/bruto`.

### Próximos Passos
- Iniciar a exploração em `notebooks/exploracao.ipynb`.
- Traduzir a lógica da análise do Excel para Pandas.
- Replicar a análise de causa raiz de `Tables` usando código Python.

## 2026-05-31 - Dia 4: Migração da Análise para Pandas

### Objetivos
- Iniciar a exploração de dados no Jupyter Notebook.
- Replicar os KPIs globais do Excel em Pandas.
- Identificar a subcategoria com maior impacto negativo no lucro.

### Atividades Realizadas
- Leitura do CSV com `pd.read_csv`.
- Ajuste de caminhos relativos para funcionar a partir da pasta `notebooks`.
- Tratamento de erro de decodificação com `encoding='latin1'`.
- Cálculo de vendas totais.
- Cálculo de lucro total.
- Criação de filtro booleano para isolar vendas com prejuízo.
- Investigação de divergências entre Excel e Pandas.
- Identificação de problema de formatação no Excel por casas decimais ocultas.
- Uso de `groupby` por `Sub-Category` para ranquear lucro por subcategoria.
- Confirmação de `Tables` como principal detrator do lucro total.
- Criação da branch `feature/exploracao-pandas` para trabalhar sem alterar diretamente a branch principal.

### Aprendizados Técnicos
- Caminhos no Windows podem gerar erros por sequências de escape.
- Arquivos vindos do Excel/Windows podem exigir `latin1` em vez de `utf-8`.
- Filtros e agregações respondem perguntas diferentes.
- A validação entre Excel e Pandas ajuda a identificar problemas de interpretação e arredondamento.

### Próximos Passos
- Realizar a análise de causa raiz de `Tables` cruzando `Discount` com `Profit`.
- Iniciar a transição da exploração para `src/limpeza.py`.
- Gerar futuramente um dataset tratado em `dados/tratado`.

## 2026-06-04 - Dia 5: Prova da Causa Raiz e Início da Limpeza

### Objetivos
- Provar matematicamente a causa raiz do prejuízo em `Tables` usando Pandas.
- Iniciar o processo de limpeza e tratamento dos dados.
- Documentar o notebook como material de aprendizado.

### Atividades Realizadas
- Isolamento da subcategoria `Tables`.
- Criação de grupos de comparação:
  - vendas de mesas com desconto maior ou igual a 20%;
  - vendas de mesas com desconto menor que 20%.
- Validação estatística da hipótese:
  - descontos altos em `Tables`: aproximadamente -31 mil de lucro;
  - descontos baixos em `Tables`: aproximadamente 13 mil de lucro.
- Conversão de `Order Date` e `Ship Date` de texto para `datetime`.
- Revisão do notebook com comentários explicativos sobre a lógica técnica e a lógica de negócio.

### Principais Insights
- A relação entre descontos agressivos e prejuízo em `Tables` foi confirmada no Python.
- A conversão de datas é um passo essencial para futuras análises temporais e de prazo de entrega.

### Próximos Passos
- Verificar valores nulos com `.isnull().sum()`.
- Criar visualizações para comunicar a causa raiz.
- Migrar os passos de limpeza para `src/limpeza.py`.

## 2026-06-13 - Dia 6: Análise de Prazo de Envio e Margem

### Objetivos
- Investigar se o prazo de envio possui relação com prejuízo.
- Criar uma métrica de margem de lucro por venda.
- Comparar lucro total, margem média e volume de vendas por subcategoria.
- Identificar novas hipóteses de causa raiz além de `Tables`.

### Atividades Realizadas
- Verificação de valores nulos com `df.isnull().sum()`.
- Confirmação de ausência de valores nulos no dataset.
- Criação da coluna `dias_envio`, calculada pela diferença entre `Ship Date` e `Order Date`.
- Análise de lucro por prazo de envio usando `groupby('dias_envio')`.
- Criação da coluna `margem_lucro`, calculada por `Profit / Sales`.
- Análise da margem média por subcategoria.
- Criação de uma tabela resumo por subcategoria contendo:
  - total de vendas;
  - lucro total;
  - margem média.

### Principais Insights
- O prazo de envio não apresentou relação direta com prejuízo nesta primeira análise.
- Todos os grupos de `dias_envio`, de 0 a 7 dias, apresentaram lucro total e lucro médio positivos.
- `Tables` continua sendo a subcategoria mais crítica em impacto financeiro, com lucro total de aproximadamente -17,7 mil.
- `Bookcases` também apresentou lucro total negativo e margem média negativa.
- `Binders` apresentou margem média negativa, mas lucro total positivo, indicando uma possível combinação de muitas vendas pequenas pouco eficientes com vendas maiores lucrativas.
- `Appliances` também apresentou margem média negativa, apesar de lucro total positivo.
- A análise mostrou a diferença entre duas leituras importantes:
  - margem média mede eficiência;
  - lucro total mede impacto financeiro.

### Hipóteses em Aberto
- `Tables` segue como prioridade pela combinação de prejuízo total alto e descontos agressivos já identificados.
- `Binders` será investigada em seguida para entender se a margem média negativa vem de muitas vendas pequenas com prejuízo compensadas por vendas maiores lucrativas.

### Próximos Passos
- Investigar `Binders` separando vendas com lucro negativo e vendas com lucro positivo.
- Comparar quantidade de vendas, valor médio de venda, lucro total e margem média nos dois grupos.
- Depois da exploração, consolidar as transformações estáveis em `src/limpeza.py`.
- Gerar o primeiro arquivo tratado em `dados/tratado`.

## 2026-06-15 - Dia 7: Estruturação da Comparação de Binders

### Objetivos
- Iniciar a investigação da subcategoria `Binders`.
- Separar as vendas de `Binders` entre vendas com lucro e vendas com prejuízo.
- Organizar os indicadores em uma pequena tabela para facilitar a comparação visual.

### Atividades Realizadas
- Criação do filtro para manter apenas registros da subcategoria `Binders`.
- Separação dos dados em dois grupos:
  - vendas com `Profit >= 0`;
  - vendas com `Profit < 0`.
- Definição dos indicadores que serão comparados:
  - quantidade de vendas;
  - vendas totais;
  - venda média;
  - lucro total;
  - margem média;
  - desconto médio.
- Planejamento de uma tabela `comparacao_binders` usando `pd.DataFrame` para visualizar os dois grupos lado a lado.

### Aprendizados Técnicos
- A comparação fica mais clara quando a análise é dividida em etapas simples: filtrar, separar, calcular e visualizar.
- Criar uma tabela resumo ajuda a sair de vários `print()` soltos e aproxima o notebook de uma análise mais profissional.
- Separar grupos por condição, como lucro positivo e lucro negativo, permite investigar hipóteses de negócio com mais clareza.

### Status
- Estrutura da comparação definida.
- Análise e interpretação dos resultados ficaram para a próxima etapa.

### Próximos Passos
- Executar a tabela `comparacao_binders` no notebook.
- Interpretar se o prejuízo em `Binders` está mais relacionado a volume, ticket médio, margem ou desconto.
- Registrar a conclusão em `docs/perguntas_e_insights.md`.

## 2026-06-18 - Dia 8: Revisão da Exploração e Comparação entre Binders e Tables

### Objetivos
- Revisar a organização da exploração no notebook.
- Confirmar quais análises já foram feitas para `Binders` e `Tables`.
- Melhorar o registro das perguntas e insights do projeto.
- Preparar a comparação de `Tables` com a mesma lógica usada em `Binders`.

### Atividades Realizadas
- Revisão da sequência atual do notebook `notebooks/exploracao.ipynb`.
- Confirmação de que a análise de `Tables` por desconto já havia sido feita anteriormente:
  - vendas com desconto maior ou igual a 20%;
  - vendas com desconto menor que 20%;
  - comparação do lucro total entre os dois grupos.
- Confirmação de que a análise de `Binders` por lucro e prejuízo foi estruturada com os indicadores:
  - quantidade de vendas;
  - vendas totais;
  - venda média;
  - lucro total;
  - margem média;
  - desconto médio.
- Construção da tabela `comparacao_binders` usando `pd.DataFrame`.
- Investigação adicional de `Binders` por faixa de desconto:
  - `binders_high_discount`;
  - `binders_low_discount`;
  - comparação de lucro total e margem média entre desconto alto e desconto baixo.
- Início da preparação da mesma lógica de comparação para `Tables`, separando:
  - `tables_prejuizo`;
  - `tables_lucro`.
- Correção dos principais pontos da comparação de `Tables`:
  - uso de `Profit >= 0` para o grupo com lucro;
  - correção do nome da variável `vendas_media_lucro_tables`;
  - uso correto da coluna `margem_lucro`.
- Revisão e melhoria do arquivo `docs/perguntas_e_insights.md`.
- Correção da acentuação do arquivo de perguntas e insights para deixar o texto mais natural em português.

### Principais Insights
- A análise de `Binders` mostrou que o grupo com prejuízo apresentou lucro total negativo e margem média negativa.
- Também foi observado que o grupo de `Binders` com prejuízo apresentou desconto médio maior.
- Isso indica uma possível relação entre descontos mais agressivos e perda de margem em parte das vendas de `Binders`.
- Ainda é necessário comparar diretamente as faixas de desconto para fortalecer ou confirmar essa hipótese.
- A análise de `Tables` já existe no notebook, mas ainda precisa ser padronizada em uma tabela resumo semelhante à de `Binders`.

### Aprendizados Técnicos
- Tabelas resumo com `pd.DataFrame` deixam a comparação mais clara do que vários `print()` separados.
- É importante manter o mesmo critério entre análises parecidas, como usar `Profit < 0` para prejuízo e `Profit >= 0` para lucro.
- Prints de DataFrames inteiros poluem o notebook; tabelas agregadas são mais adequadas para análise e comunicação.
- O notebook deve contar uma história analítica: visão geral, identificação do problema, investigação da causa e conclusão parcial.

### Status
- Comparação de `Binders` estruturada.
- Texto de perguntas e insights revisado e acentuado.
- Comparação de `Tables` iniciada e corrigida, mas ainda sem a tabela final `comparacao_tables`.

### Próximos Passos
- Criar a tabela `comparacao_tables` com os mesmos indicadores usados em `comparacao_binders`.
- Comparar os grupos `Tables com prejuízo` e `Tables com lucro`.
- Depois, avaliar se vale criar uma tabela final comparando os grupos problemáticos de `Tables` e `Binders`.
- Atualizar `docs/perguntas_e_insights.md` com a conclusão da comparação de `Tables`.
- Em seguida, iniciar a transição para `src/limpeza.py` e geração dos dados tratados.

## 2026-06-22 - Dia 9: Conclusão da Comparação entre Tables e Binders

### Objetivos
- Finalizar a comparação entre `Tables` e `Binders`.
- Entender se o maior problema estava em `Tables` ou em `Binders`.
- Criar uma tabela de apoio para interpretar os dados sem misturar conclusão e evidência.

### Atividades Realizadas
- Finalização da tabela `comparacao_tables`, comparando:
  - `Tables com prejuízo`;
  - `Tables com lucro`.
- Junção das tabelas `comparacao_tables` e `comparacao_binders` usando `pd.concat`.
- Ordenação da tabela comparativa por `lucro_total`, para visualizar os grupos com maior prejuízo.
- Revisão da interpretação da comparação entre grupos com prejuízo e resultado total por subcategoria.
- Identificação de uma diferença importante:
  - `Binders` possui um grupo de vendas com prejuízo mais negativo;
  - porém `Binders` fecha com lucro total positivo;
  - `Tables` fecha com lucro total negativo, pois o lucro das vendas positivas não compensa as perdas.

### Principais Insights
- `Binders` apresenta perdas relevantes em parte das vendas, mas a subcategoria ainda é lucrativa no resultado acumulado.
- `Tables` é o problema financeiro principal, porque a subcategoria fecha com lucro total negativo.
- A comparação mostrou a diferença entre olhar apenas grupos negativos e olhar o resultado final da subcategoria.
- O real problema financeiro identificado na exploração continua sendo `Tables`.

### Aprendizados Técnicos
- A tabela final deve servir como apoio para interpretação, não necessariamente conter textos longos de conclusão.
- Tabelas com textos grandes ficam difíceis de ler no notebook.
- Para comparar melhor, é importante separar:
  - prejuízo interno de um grupo;
  - lucro compensatório;
  - resultado final da subcategoria.
- Reaproveitar tabelas já criadas, como `comparacao_tables` e `comparacao_binders`, é melhor do que repetir todos os cálculos.

### Status
- Comparação entre `Tables` e `Binders` concluída no notebook.
- Conclusão principal definida: `Tables` é o real problema financeiro.
- Registro em `docs/perguntas_e_insights.md` ficará para a próxima etapa.

### Próximos Passos
- Adicionar a conclusão final da comparação em `docs/perguntas_e_insights.md`.
- Revisar o notebook para reduzir prints grandes e manter apenas tabelas úteis.
- Depois disso, iniciar a transição para `src/limpeza.py`.
- Gerar futuramente o primeiro dataset tratado em `dados/tratado`.

## 2026-07-01 - Dia 10: Início da Limpeza dos Dados

### Objetivos
- Iniciar a transição da exploração para um script de limpeza em `src/limpeza.py`.
- Transformar as etapas já validadas no notebook em um processo repetível.
- Preparar a base para futuramente gerar o primeiro arquivo tratado em `dados/tratado`.

### Atividades Realizadas
- Criação do arquivo `src/limpeza.py`.
- Leitura do arquivo bruto `dados/bruto/Sample - Superstore.csv` com `pd.read_csv` e `encoding='latin1'`.
- Definição dos caminhos:
  - `caminho_entrada`;
  - `caminho_saida`.
- Conversão das colunas de data:
  - `Order Date`;
  - `Ship Date`.
- Uso de `format='%m/%d/%Y'` para deixar explícito o padrão de data do dataset.
- Uso de `errors='coerce'` para permitir identificar datas inválidas.
- Verificação de datas inválidas após a conversão.
- Verificação de datas incoerentes, ou seja, casos em que `Ship Date` seria anterior a `Order Date`.
- Criação da coluna `dias_envio`, calculada pela diferença entre `Ship Date` e `Order Date`.
- Criação da coluna `margem_lucro`, calculada por `Profit / Sales`.
- Verificação de valores nulos com `df.isnull().sum()`.
- Verificação de linhas duplicadas com `df.duplicated().sum()`.

### Resultados da Validação
- Datas inválidas: 0.
- Datas incoerentes: 0.
- Valores nulos após as transformações: 0.
- Linhas duplicadas: 0.
- As colunas `dias_envio` e `margem_lucro` foram criadas corretamente.

### Aprendizados Técnicos
- A limpeza deve transformar descobertas da exploração em um processo organizado e repetível.
- A verificação de datas precisa considerar dois tipos de problema:
  - datas inválidas tecnicamente, que não conseguem ser convertidas;
  - datas incoerentes para o negócio, como envio antes do pedido.
- `errors='coerce'` é útil porque transforma datas problemáticas em `NaT`, permitindo investigar o problema em vez de esconder o erro.
- Nem toda coluna pensada na exploração deve entrar automaticamente na base tratada; algumas precisam de validação de regra de negócio antes.

### Decisão de Projeto
- As colunas `dias_envio` e `margem_lucro` entram como transformações já validadas.
- As colunas `ano` e `mes` podem ser criadas depois para apoiar análises temporais e filtros em dashboard.
- A coluna `faixa_desconto` não será criada ainda.
- Antes de criar `faixa_desconto`, será necessário revisar a análise exploratória de descontos e validar se as faixas fazem sentido para o negócio.

### Regra para `faixa_desconto`
- A regra proposta só será implementada depois de revisão:
  - 0% = sem desconto;
  - maior que 0% e menor que 20% = desconto baixo;
  - 20% a 40% = desconto alto;
  - acima de 40% = desconto agressivo.
- Essa regra precisa ser confirmada com base no comportamento observado na exploração, principalmente nas análises de `Tables` e `Binders`.

### Status
- Script de limpeza iniciado.
- Validações principais de datas, nulos e duplicados implementadas.
- Base tratada ainda não foi salva.
- Regras adicionais de enriquecimento, como `ano`, `mes` e `faixa_desconto`, ficaram para etapa posterior.

### Próximos Passos
- Salvar o arquivo tratado em `dados/tratado/superstore_tratado.csv`.
- Depois, avaliar a criação das colunas `ano` e `mes`.
- Revisar a exploração de descontos antes de criar `faixa_desconto`.
- Só implementar `faixa_desconto` quando a regra de negócio estiver validada.
