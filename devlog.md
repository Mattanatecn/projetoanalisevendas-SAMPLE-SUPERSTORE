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
- Base tratada gerada em `dados/tratado/superstore_tratado.csv`.
- Primeira versão da limpeza concluída.

### Próximos Passos
- Fazer commit da etapa de limpeza.
- Iniciar a análise final utilizando `dados/tratado/superstore_tratado.csv`.
- Revalidar os principais KPIs com a base tratada.
- Confirmar se os resultados da exploração continuam consistentes com o dataset tratado.
- Preparar a próxima etapa de visualizações em Python.

## 2026-07-09 - Dia 11: Conclusão da Limpeza v1

### Objetivos
- Finalizar a primeira versão do script de limpeza.
- Criar as colunas tratadas e enriquecidas definidas durante a exploração.
- Gerar o primeiro arquivo tratado do projeto.

### Atividades Realizadas
- Criação das colunas temporais:
  - `ano`;
  - `mes`.
- Revisão da regra de negócio para criação de `faixa_desconto`.
- Implementação da coluna `faixa_desconto`, considerando que `Discount` está em formato decimal:
  - `0` = sem desconto;
  - maior que `0` e menor que `0.2` = desconto baixo;
  - maior ou igual a `0.2` e menor ou igual a `0.4` = desconto alto;
  - maior que `0.4` = desconto agressivo.
- Validação da distribuição das faixas de desconto:
  - sem desconto: 4.798 linhas;
  - desconto alto: 4.117 linhas;
  - desconto agressivo: 933 linhas;
  - desconto baixo: 146 linhas.
- Inclusão de uma categoria de segurança `verificar` para casos futuros fora das regras previstas.
- Salvamento da base tratada em `dados/tratado/superstore_tratado.csv`.
- Validação do arquivo tratado gerado:
  - 9.994 linhas;
  - 26 colunas.

### Colunas Criadas na Base Tratada
- `dias_envio`
- `ano`
- `mes`
- `margem_lucro`
- `faixa_desconto`

### Principais Aprendizados
- Colunas tratadas devem nascer de necessidades identificadas na exploração.
- A coluna `faixa_desconto` precisava de validação antes de ser criada, pois dependia de uma regra de negócio.
- Valores percentuais no dataset estavam em formato decimal, então `0.2` representa 20% e `0.4` representa 40%.
- A base tratada deve ser a fonte das próximas análises, visualizações e dashboards.

### Status
- Limpeza v1 concluída.
- Arquivo tratado criado com sucesso.
- O projeto está pronto para avançar para análise final com dados tratados.

### Próximos Passos
- Iniciar análise final a partir da base tratada.
- Comparar os principais resultados da exploração com a base tratada.
- Começar a preparar visualizações em Python.

## 2026-07-12 - Dia 12: Início da Análise Final

### Objetivos
- Iniciar a análise final utilizando a base tratada.
- Organizar o novo notebook por etapas claras.
- Confirmar se o arquivo tratado está pronto para as análises de negócio.

### Atividades Realizadas
- Criação da branch `feature/analise-final`.
- Criação do notebook `notebooks/analise_final.ipynb`.
- Organização inicial do notebook nas seções:
  - carregamento da base tratada;
  - validação da base tratada.
- Criação da função `carregar_dados`, responsável por:
  - receber o caminho do arquivo;
  - carregar o CSV tratado;
  - converter `Order Date` e `Ship Date` para o tipo de data;
  - devolver o DataFrame carregado.
- Validação da quantidade de linhas e colunas.
- Verificação dos tipos das colunas e visualização inicial dos dados.
- Verificação de valores nulos e linhas duplicadas.
- Validação dos limites de datas, descontos e prazos de envio.
- Conferência dos anos disponíveis e das categorias de desconto.

### Resultados da Validação
- Registros: 9.994.
- Colunas: 26.
- Valores nulos: 0.
- Linhas duplicadas: 0.
- Período dos pedidos: 03/01/2014 a 30/12/2017.
- Descontos: 0% a 80%.
- Prazo de envio: 0 a 7 dias.
- Anos disponíveis: 2014, 2015, 2016 e 2017.
- Faixas encontradas:
  - sem desconto;
  - desconto baixo;
  - desconto alto;
  - desconto agressivo.
- Nenhum registro foi classificado como `verificar`.

### Principais Aprendizados
- Uma base tratada também deve ser validada antes de iniciar os cálculos de negócio.
- `min()` e `max()` ajudam a verificar os limites e a coerência de datas e valores numéricos.
- Uma variável criada dentro de uma função possui escopo local; o valor devolvido por `return` precisa ser recebido fora da função.
- Receber o caminho como parâmetro torna a função de carregamento mais reutilizável.
- `set()` encontra valores distintos.

### Status
- Carregamento e validação da base tratada concluídos.
- Base confirmada como pronta para a análise final.
- A visão geral do negócio ainda não foi iniciada.

### Próximos Passos
- Criar a seção de visão geral do negócio.
- Calcular os principais KPIs, incluindo faturamento, lucro, margem global, quantidade vendida, número de pedidos e ticket médio.
- Organizar os KPIs em uma função reutilizável para apoiar futuramente o dashboard.

## 2026-07-17 - Dia 13: Visão Geral do Negócio

### Objetivos
- Criar a visão geral do negócio a partir da base tratada.
- Calcular os principais KPIs do período analisado.
- Organizar os cálculos em uma função reutilizável.
- Interpretar os resultados em linguagem de negócio.

### Atividades Realizadas
- Criação da seção `3. Visão geral do negócio` no notebook.
- Criação da função `calcular_kpis`, que recebe um DataFrame e calcula:
  - faturamento total;
  - lucro total;
  - margem global;
  - quantidade vendida;
  - total de pedidos únicos;
  - ticket médio.
- Organização dos resultados em um dicionário chamado `kpis`.
- Separação entre o cálculo dos indicadores e a formatação usada para apresentá-los.
- Criação de uma interpretação dos KPIs em uma célula Markdown.
- Revisão do significado da margem global e do ticket médio.

### Resultados dos KPIs
- Faturamento total: US$ 2.297.200,86.
- Lucro total: US$ 286.397,02.
- Margem global: 12,47%.
- Quantidade vendida: 37.873 unidades.
- Pedidos únicos: 5.009.
- Ticket médio: US$ 458,61 por pedido.

### Interpretação de Negócio
- A empresa apresentou lucro no período analisado.
- Para cada US$ 100 faturados, aproximadamente US$ 12,47 permaneceram como lucro.
- Cada pedido gerou, em média, US$ 458,61 em faturamento.
- O resultado geral positivo não permite concluir sozinho que todas as áreas do negócio foram lucrativas.
- Ainda será necessário investigar categorias, regiões e períodos que possam esconder baixa lucratividade ou prejuízo.

### Principais Aprendizados
- A margem global deve ser calculada dividindo o lucro total pelo faturamento total, e não pela média simples da coluna `margem_lucro`.
- O total de pedidos deve usar `nunique()` em `Order ID`, pois um mesmo pedido pode aparecer em várias linhas.
- Uma função de análise deve receber o DataFrame como parâmetro para não depender de uma variável global.
- Um dicionário permite devolver vários KPIs com nomes que representam seus significados.
- Os valores devem permanecer numéricos durante os cálculos; a formatação monetária e percentual deve acontecer apenas na apresentação.
- Um resultado positivo só pode ser classificado como bom quando existe uma meta, um histórico ou outra referência para comparação.

### Status
- Visão geral do negócio concluída.
- KPIs gerais calculados e validados com a base tratada.
- Interpretação inicial registrada no notebook.
- A etapa 4, referente à análise temporal, foi adiada para a próxima sessão.

### Próximos Passos
- Criar a seção `4. Análise temporal`.
- Implementar a função reutilizável `resumir_por_grupo`.
- Gerar um resumo anual com faturamento, lucro, margem, quantidade, pedidos e ticket médio.
- Investigar se o faturamento e o lucro evoluíram de forma consistente entre 2014 e 2017.

## 2026-07-19 - Dia 14: Análise do Desempenho Anual

### Objetivos
- Iniciar a análise temporal da base tratada.
- Comparar o desempenho da empresa entre 2014 e 2017.
- Aprender a utilizar `groupby()` e `agg()` de forma gradual.
- Criar uma função reutilizável para resumos por diferentes grupos.
- Registrar as novas perguntas e descobertas na documentação analítica.

### Atividades Realizadas
- Criação da seção `4. Análise temporal` no notebook.
- Criação da subseção `4.1 Desempenho anual`.
- Estudo da diferença entre separar os anos manualmente com `for` e `if` e agrupá-los automaticamente com `groupby()`.
- Criação da função `resumir_por_grupo`, que recebe:
  - o DataFrame;
  - o nome da coluna de agrupamento.
- Uso de `agg()` para gerar, em uma única tabela:
  - faturamento total;
  - lucro total;
  - quantidade vendida;
  - total de pedidos únicos.
- Cálculo da margem global de cada grupo a partir do lucro total dividido pelo faturamento total.
- Cálculo do ticket médio de cada grupo a partir do faturamento total dividido pelo total de pedidos.
- Aplicação da função na coluna `ano` para criar `resumo_anual`.
- Interpretação dos resultados anuais em uma célula Markdown.

### Resultados do Resumo Anual
- 2014:
  - faturamento: US$ 484.247,50;
  - lucro: US$ 49.543,97;
  - quantidade vendida: 7.581 unidades;
  - pedidos: 969;
  - margem global: 10,23%;
  - ticket médio: US$ 499,74.
- 2015:
  - faturamento: US$ 470.532,51;
  - lucro: US$ 61.618,60;
  - quantidade vendida: 7.979 unidades;
  - pedidos: 1.038;
  - margem global: 13,10%;
  - ticket médio: US$ 453,31.
- 2016:
  - faturamento: US$ 609.205,60;
  - lucro: US$ 81.795,17;
  - quantidade vendida: 9.837 unidades;
  - pedidos: 1.315;
  - margem global: 13,43%;
  - ticket médio: US$ 463,27.
- 2017:
  - faturamento: US$ 733.215,26;
  - lucro: US$ 93.439,27;
  - quantidade vendida: 12.476 unidades;
  - pedidos: 1.687;
  - margem global: 12,74%;
  - ticket médio: US$ 434,63.

### Principais Insights
- O lucro aumentou em todos os anos, mas o faturamento caiu entre 2014 e 2015.
- Em 2015, a quantidade vendida e o número de pedidos aumentaram, enquanto o faturamento e o ticket médio diminuíram.
- O aumento no volume de vendas não garantiu aumento do faturamento em 2015.
- A margem de 2015 aumentou de 10,23% para 13,10%, indicando maior eficiência financeira, embora sua causa ainda não tenha sido identificada.
- O ano de 2016 apresentou a maior margem global, com 13,43%.
- O ano de 2017 apresentou o maior faturamento e o maior lucro, sustentados pelo maior volume de pedidos e unidades vendidas.
- Em 2017, o faturamento atingiu o maior valor mesmo com o menor ticket médio do período.

### Principais Aprendizados
- `groupby()` separa os dados automaticamente pelos valores distintos de uma coluna.
- `agg()` permite calcular várias métricas para os mesmos grupos sem repetir o agrupamento.
- A estrutura `nome_do_resultado=('coluna_original', 'operação')` cria nomes de negócio claros para as colunas agregadas.
- `nunique()` deve ser usado para contar pedidos sem repetir um mesmo `Order ID`.
- Faturamento, lucro, margem, quantidade, pedidos e ticket médio respondem perguntas diferentes e precisam ser interpretados em conjunto.
- Uma relação observada nos dados pode sustentar uma hipótese, mas não confirma automaticamente sua causa.

### Organização da Documentação
- O documento de perguntas e insights foi dividido por fase do projeto.
- `docs/perguntas_e_insights.md` passou a funcionar como índice.
- `docs/perguntas_e_insights/exploracao_inicial.md` passou a reunir as sete perguntas da exploração inicial.
- `docs/perguntas_e_insights/analise_final.md` passou a reunir as perguntas e conclusões obtidas com a base tratada.
- A numeração das perguntas da análise final foi reiniciada.
- A pergunta sobre a melhora da margem em 2015 foi mantida com status `Em investigação`.

### Status
- Resumo anual concluído com os principais indicadores.
- Interpretação anual registrada no notebook.
- Perguntas e insights reorganizados por fase do projeto.
- Causa da melhora de margem em 2015 ainda não confirmada.

### Próximos Passos
- Melhorar a apresentação da tabela anual, formatando valores monetários e percentuais.
- Continuar a análise temporal com a variação mensal e possível sazonalidade.
- Investigar por que a margem melhorou em 2015, comparando categorias, descontos e regiões.
- Preparar visualizações do desempenho ao longo do tempo.
