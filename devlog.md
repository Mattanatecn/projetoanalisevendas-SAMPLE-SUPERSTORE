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

## 2026-07-22 - Dia 15: Conclusão do Resumo Anual

### Objetivos
- Quantificar a variação do faturamento e do lucro entre anos consecutivos.
- Melhorar a organização das funções da análise.
- Formatar a tabela anual para facilitar sua leitura no notebook.
- Concluir a parte numérica e textual do desempenho anual antes de iniciar a análise mensal.

### Atividades Realizadas
- Estudo da fórmula de variação percentual entre um valor atual e o valor anterior.
- Simulação da comparação anual de forma manual e com laço `for`.
- Uso de `pct_change()` para calcular automaticamente:
  - variação anual do faturamento;
  - variação anual do lucro.
- Interpretação conjunta do crescimento do faturamento, do lucro e da margem global.
- Separação das responsabilidades em duas funções:
  - `resumir_por_grupo`, responsável pelos indicadores gerais de qualquer agrupamento;
  - `variacoes_temporais`, responsável pelas comparações entre períodos ordenados.
- Uso de `.copy()` para preservar o resumo original antes de adicionar as variações temporais.
- Criação de um dicionário com regras de formatação para cada coluna.
- Uso de `style.format()` para apresentar:
  - valores monetários;
  - quantidades com separador de milhares;
  - margens e variações em porcentagem;
  - ausência de comparação em 2014 representada por `-`.
- Decisão de deixar os gráficos finais para a etapa de visualização, depois da conclusão das análises.

### Resultados das Variações Anuais
- De 2014 para 2015:
  - faturamento: -2,83%;
  - lucro: +24,37%.
- De 2015 para 2016:
  - faturamento: +29,47%;
  - lucro: +32,74%.
- De 2016 para 2017:
  - faturamento: +20,36%;
  - lucro: +14,24%.

### Principais Insights
- Em 2015, o faturamento diminuiu, mas o lucro cresceu 24,37%, reforçando a evidência de melhora na eficiência financeira.
- Em 2016, o lucro cresceu mais rapidamente que o faturamento e a margem global aumentou.
- Em 2017, o faturamento cresceu mais rapidamente que o lucro e a margem global diminuiu.
- O crescimento do lucro precisa ser analisado em relação ao crescimento do faturamento para compreender a evolução da margem.

### Principais Aprendizados
- A variação percentual compara o valor atual com o período imediatamente anterior.
- `pct_change()` automatiza a mesma lógica que poderia ser implementada manualmente ou com um laço `for`.
- O primeiro período apresenta `NaN` porque não existe um período anterior para comparação.
- Funções genéricas não devem incluir cálculos que só fazem sentido para dados temporais.
- Uma função sem `return` devolve `None`, o que impede operações posteriores sobre o resultado.
- Ao trabalhar com uma cópia, as alterações e o `return` devem utilizar a mesma variável.
- `style.format()` muda apenas a apresentação; os valores do DataFrame continuam numéricos.

### Erros Investigados
- Correção do nome `pct_chenge()` para `pct_change()`.
- Correção da ausência de `return` na primeira tentativa da função temporal.
- Correção do uso alternado entre o resumo original e sua cópia, que fazia a variação do faturamento desaparecer do resultado final.
- Correção do dicionário utilizado na formatação das variações.

### Status
- Resumo anual concluído com indicadores, variações, interpretação e formatação.
- Funções reorganizadas por responsabilidade.
- Documento de perguntas e insights atualizado com as taxas anuais.
- Análise mensal ainda não iniciada.
- Investigação da causa da melhora de margem em 2015 continua pendente.

### Próximos Passos
- Analisar a evolução cronológica usando o agrupamento por ano e mês.
- Analisar sazonalidade agrupando os mesmos meses dos diferentes anos.
- Investigar a melhora da margem em 2015 por categorias, descontos e regiões.
- Iniciar as visualizações apenas depois da conclusão das etapas analíticas.

## 2026-07-23 - Dia 16: Desempenho Mensal e Análise por Categoria

### Objetivos
- Analisar o desempenho mensal da empresa ao longo dos quatro anos da base.
- Identificar meses com prejuízo e os períodos com pior lucro e margem.
- Entender por que lucro, margem e ticket médio precisam ser avaliados em conjunto.
- Iniciar a análise de categorias utilizando a função reutilizável criada anteriormente.

### Atividades Realizadas
- Aplicação da função `resumir_por_grupo` com agrupamento pelas colunas `ano` e `mes`.
- Criação de um resumo cronológico com os 48 meses existentes entre 2014 e 2017.
- Uso de `.copy()` para preservar o resumo mensal original antes da inclusão de novas colunas.
- Cálculo da variação mensal do faturamento com `pct_change()`.
- Substituição da variação percentual do lucro pela diferença absoluta com `diff()`, pois a presença de valores negativos poderia gerar percentuais de difícil interpretação.
- Criação de uma formatação específica para a tabela mensal, incluindo valores monetários, percentuais, quantidades e diferenças de lucro.
- Filtragem dos meses com lucro negativo por meio da condição `lucro_total < 0`.
- Criação de rankings mensais com `sort_values()` para localizar:
  - os menores lucros totais;
  - as menores margens globais.
- Interpretação das diferenças entre lucro total, margem global, faturamento, ticket médio e volume de pedidos.
- Início da seção `5. Categorias e subcategorias`.
- Reutilização da função `resumir_por_grupo` para gerar o resumo por `Category`.
- Comparação do desempenho de Technology, Furniture e Office Supplies.

### Resultados da Análise Mensal
- Julho de 2014 e janeiro de 2015 foram os meses que apresentaram prejuízo.
- Janeiro de 2015 foi o período mais crítico:
  - lucro aproximado de US$ 3.281,01 negativos;
  - margem global de -18,05%;
  - menor número de pedidos e menor quantidade vendida em comparação com julho de 2014.
- O ticket médio de janeiro de 2015 foi superior ao de julho de 2014, mas isso não impediu que o mês apresentasse um prejuízo maior.
- Fevereiro de 2014 apresentou lucro total baixo principalmente pelo baixo volume de vendas, enquanto sua margem de 19,08% indicou boa eficiência.
- Novembro de 2016 apresentou faturamento elevado, mas margem global de apenas 5,05%.

### Resultados da Análise por Categoria
- Technology apresentou o maior faturamento, o maior lucro e a melhor margem global.
- Furniture faturou mais que Office Supplies, mas gerou um lucro consideravelmente menor.
- A margem global de Furniture foi de 2,49%, enquanto Office Supplies apresentou margem de 17,04%.
- O resultado indica que Furniture possui baixa eficiência financeira e provavelmente contém subcategorias que reduzem seu desempenho.

### Principais Insights
- Um ticket médio alto não garante lucro, pois o valor médio dos pedidos não mostra quanto permanece como resultado financeiro.
- O lucro total mostra o valor financeiro gerado, enquanto a margem mostra a eficiência desse resultado em relação ao faturamento.
- Um mês com pouco lucro não é necessariamente ruim quando também possui baixo volume e uma margem saudável.
- Faturamento elevado também não garante bom desempenho quando a margem permanece baixa.
- A comparação entre Furniture e Office Supplies reforça que faturamento e lucro devem ser analisados em conjunto.
- A análise mensal já respondeu às perguntas principais desta etapa, portanto não foi necessário aprofundá-la além do foco definido para o projeto.

### Principais Aprendizados
- O agrupamento por `['ano', 'mes']` mantém os meses separados dentro de cada ano e produz os 48 períodos da base.
- `pct_change()` calcula uma variação relativa ao período anterior.
- `diff()` calcula uma diferença absoluta e pode ser mais clara quando a métrica possui valores negativos.
- Um filtro localiza os registros que atendem a uma condição, enquanto um ranking permite comparar os melhores ou piores resultados.
- Lucro e margem respondem perguntas diferentes e não devem ser interpretados isoladamente.
- Uma função genérica pode ser reutilizada em análises anuais, mensais e por categoria sem repetir os mesmos cálculos.

### Ajustes Realizados
- Correção do agrupamento mensal para considerar simultaneamente o ano e o mês.
- Ajuste da análise para exibir e considerar os 48 meses, e não apenas um único ano.
- Retirada da variação percentual do lucro mensal e adoção da diferença absoluta.
- Criação de um dicionário de formatação próprio para o resumo mensal.

### Status
- Análise do desempenho mensal concluída no nível necessário para o projeto.
- Meses com prejuízo identificados e interpretados.
- Rankings de lucro e margem mensal concluídos.
- Análise por categoria iniciada e interpretação geral registrada no notebook.
- Visualizações continuam reservadas para uma etapa posterior.
- Investigação específica da melhora da margem em 2015 continua pendente.

### Próximos Passos
- Aplicar `resumir_por_grupo` na coluna `Sub-Category`.
- Identificar quais subcategorias explicam a baixa margem de Furniture.
- Comparar faturamento, lucro e margem das principais subcategorias.

## 2026-07-27 - Dia 17: Subcategorias e Investigação da Margem de 2015

### Objetivos
- Concluir a análise das categorias e subcategorias.
- Identificar quais subcategorias explicam a baixa margem de Furniture.
- Avançar na investigação da melhora da margem global em 2015.
- Descobrir qual categoria e quais subcategorias mais contribuíram para essa melhora.

### Atividades Realizadas
- Aplicação da função `resumir_por_grupo` na coluna `Sub-Category`.
- Comparação do faturamento, lucro, margem, quantidade vendida, pedidos e ticket médio das subcategorias.
- Identificação das subcategorias lucrativas e deficitárias de Furniture.
- Agrupamento simultâneo pelas colunas `ano` e `Category`.
- Comparação das três categorias entre 2014 e 2015.
- Identificação de Technology como principal categoria associada à melhora da margem em 2015.
- Criação de um filtro para manter somente as vendas da categoria Technology.
- Agrupamento dos dados filtrados pelas colunas `ano` e `Sub-Category`.
- Comparação de Accessories, Copiers, Machines e Phones entre 2014 e 2015.
- Registro das interpretações em células Markdown no notebook.

### Resultados de Furniture
- Bookcases apresentou prejuízo de aproximadamente US$ 3,47 mil e margem global de -3,02%.
- Tables apresentou prejuízo de aproximadamente US$ 17,73 mil e margem global de -8,56%.
- Tables foi a principal causa da baixa eficiência financeira de Furniture.
- Chairs e Furnishings foram lucrativas e compensaram os prejuízos das outras duas subcategorias.
- Apesar dessa compensação, Furniture terminou com margem global de apenas 2,49%.

### Comparação entre 2014 e 2015
- Furniture apresentou redução de lucro e margem em 2015.
- Office Supplies apresentou aumento de lucro e margem.
- Technology apresentou o maior aumento de lucro e a maior melhora de margem entre as categorias.
- Em Technology:
  - o faturamento diminuiu de aproximadamente US$ 175,28 mil para US$ 162,78 mil;
  - o lucro aumentou de aproximadamente US$ 21,49 mil para US$ 33,50 mil;
  - a margem aumentou de 12,26% para 20,58%;
  - o aumento da margem foi de 8,32 pontos percentuais.

### Resultados das Subcategorias de Technology
- Copiers apresentou o maior aumento de lucro, com aproximadamente US$ 7,02 mil adicionais.
- A margem de Copiers aumentou de 26,85% para 37,93%, uma melhora de 11,08 pontos percentuais.
- Machines também apresentou melhora relevante de lucro e margem.
- Accessories aumentou o lucro principalmente pelo crescimento do faturamento, embora sua margem tenha diminuído levemente.
- Phones apresentou redução de lucro e não contribuiu para a melhora da categoria.

### Principais Insights
- Tables e Bookcases reduzem o desempenho de Furniture, mas Tables possui o maior impacto negativo.
- Uma categoria pode terminar com lucro positivo e ainda apresentar baixa eficiência quando parte relevante de seu resultado é consumida por subcategorias deficitárias.
- Technology foi a principal categoria associada à melhora da margem global em 2015.
- A melhora de Technology foi impulsionada principalmente por Copiers, com contribuição adicional de Machines e Accessories.
- A análise por categoria mostra onde ocorreu a melhora, enquanto a análise por subcategoria aproxima a investigação de sua causa.
- Os resultados ainda precisam ser comparados com os descontos antes de considerar encerrada a investigação de 2015.

### Principais Aprendizados
- O agrupamento por `['ano', 'Category']` permite comparar cada categoria dentro de cada ano.
- Filtrar uma categoria antes do agrupamento reduz a tabela ao recorte necessário para responder uma pergunta específica.
- A diferença entre duas margens deve ser apresentada em pontos percentuais.
- Aumento de lucro e aumento de margem não significam necessariamente a mesma coisa.
- Encontrar a dimensão em que uma mudança aconteceu não comprova sozinho sua causa.

### Status
- Análise geral de categorias e subcategorias concluída.
- Causa da baixa margem de Furniture identificada nas subcategorias Tables e Bookcases.
- Evidências necessárias para confirmar a pergunta sobre a eficiência de Furniture obtidas.
- Principal contribuição para a melhora de 2015 localizada em Technology, especialmente em Copiers.
- Investigação da melhora da margem de 2015 permanece aberta até a análise dos descontos.
- Análises regional e por segmento ainda não iniciadas.

### Próximos Passos
- Comparar as faixas de desconto de 2014 e 2015.
- Verificar se a mudança nos descontos ajuda a explicar a melhora de Technology.

## 2026-08-03 - Dia 18: Conclusão da Análise de Descontos em Technology

### Objetivos
- Verificar se as faixas de desconto ajudam a explicar a melhora do lucro e da margem de `Technology` em 2015.
- Comparar o desempenho de vendas sem desconto, com desconto alto e com desconto agressivo entre 2014 e 2015.
- Encerrar a investigação iniciada após a análise anual.

### Atividades Realizadas
- Agrupamento das vendas de `Technology` pelas colunas `ano` e `faixa_desconto` com a função `resumir_por_grupo`.
- Comparação de faturamento, lucro, margem global, quantidade vendida, pedidos e ticket médio por faixa.
- Separação dos resumos de 2014 e 2015.
- Criação da tabela `diferencas_desconto` contendo:
  - diferença de faturamento;
  - diferença de lucro;
  - variação da margem em pontos percentuais;
  - diferença no número de pedidos.
- Registro da interpretação em células Markdown no notebook.
- Atualização de `docs/perguntas_e_insights/analise_final.md` com as conclusões de categorias, subcategorias e descontos.

### Resultados
- Vendas sem desconto:
  - aumento de aproximadamente US$ 20,29 mil no faturamento;
  - aumento de aproximadamente US$ 7,49 mil no lucro;
  - melhora de 1,12 ponto percentual na margem;
  - aumento de 21 pedidos.
- Desconto alto:
  - redução de aproximadamente US$ 8,71 mil no faturamento;
  - aumento de aproximadamente US$ 4,71 mil no lucro;
  - melhora de 6,96 pontos percentuais na margem;
  - aumento de 22 pedidos.
- Desconto agressivo:
  - redução de aproximadamente US$ 24,08 mil no faturamento;
  - piora de aproximadamente US$ 190,31 no lucro;
  - queda de 93,01 pontos percentuais na margem;
  - redução de um pedido.

### Principais Insights
- O maior aumento de lucro de `Technology` veio das vendas sem desconto.
- As vendas com desconto alto também contribuíram para a melhora, pois aumentaram o lucro e a margem mesmo com menor faturamento.
- Nem todo desconto foi prejudicial: a faixa de desconto alto apresentou resultado positivo e maior eficiência em 2015.
- Os descontos agressivos continuaram gerando lucro e margem negativos e não contribuíram para a melhora de `Technology`.
- A melhora de `Technology` em 2015 esteve associada ao crescimento das vendas sem desconto e à maior eficiência das vendas com desconto alto.

### Principais Aprendizados
- Diferenças absolutas de lucro são mais claras que variações percentuais quando existem valores negativos.
- A diferença entre margens deve ser comunicada em pontos percentuais.
- Menor faturamento não significa necessariamente pior desempenho quando lucro e margem aumentam.
- Uma faixa com poucas vendas pode continuar causando impacto financeiro relevante.
- Comparar faixas de desconto ajuda a distinguir descontos sustentáveis de descontos que destroem margem.

### Status
- Investigação da melhora da margem em 2015 concluída no recorte de categorias, subcategorias e descontos.
- `Technology` confirmada como principal categoria associada à melhora.
- `Copiers` identificada como principal subcategoria contribuidora.
- Vendas sem desconto e descontos altos identificados como os principais componentes positivos.
- Descontos agressivos confirmados como grupo financeiramente prejudicial.
- Análises regional e por segmento ainda não iniciadas.

### Próximos Passos
- Analisar faturamento, lucro e margem por região.
- Analisar faturamento, lucro e margem por segmento de clientes.
- Consolidar os principais insights em uma conclusão executiva.

## 2026-08-05 - Dia 19: Encerramento da Análise Final

### Objetivos
- Concluir as análises regional e por segmento de clientes.
- Consolidar os resultados obtidos com a base tratada.
- Registrar as perguntas e insights que ainda estavam pendentes.
- Revisar e padronizar a apresentação das tabelas do notebook.
- Encerrar formalmente a etapa de análise final antes das visualizações.

### Atividades Realizadas
- Aplicação da função `resumir_por_grupo` na coluna `Region`.
- Comparação de faturamento, lucro, quantidade vendida, pedidos, margem global e ticket médio entre as regiões.
- Aplicação da função `resumir_por_grupo` na coluna `Segment`.
- Comparação dos mesmos indicadores entre Consumer, Corporate e Home Office.
- Interpretação dos resultados regionais e por segmento em células Markdown.
- Criação da seção `8. Conclusão executiva` no notebook.
- Consolidação dos principais resultados e recomendações de negócio.
- Inclusão das perguntas sobre região e segmento em `docs/perguntas_e_insights/analise_final.md`.
- Criação do dicionário reutilizável `formatacao_grupos`.
- Formatação das tabelas de categoria, subcategoria, região, segmento, descontos e comparações temporais.
- Limitação das tabelas comparativas aos anos de 2014 e 2015, mantendo os resumos completos disponíveis para cálculo.
- Criação de uma formatação específica para diferenças de faturamento, lucro, margem em pontos percentuais e pedidos.
- Remoção da saída intermediária e extensa do filtro de Technology.
- Padronização dos títulos e subtítulos do notebook.

### Resultados da Análise Regional
- West apresentou o maior faturamento, o maior lucro e a melhor margem global, de 14,94%.
- Central apresentou a menor margem regional, de 7,92%.
- Central faturou mais que South, mas gerou menos lucro, indicando menor eficiência financeira.
- East apresentou o segundo maior faturamento e lucro entre as regiões.

### Resultados da Análise por Segmento
- Consumer concentrou o maior faturamento, lucro, quantidade vendida e número de pedidos.
- Apesar do maior resultado absoluto, Consumer apresentou a menor margem entre os segmentos, com 11,55%.
- Home Office apresentou o menor faturamento e lucro total, mas alcançou a melhor margem global, de 14,03%.
- Home Office também apresentou o maior ticket médio, de US$ 472,67.
- Corporate ocupou uma posição intermediária em volume e eficiência.

### Conclusões Consolidadas
- A empresa apresentou resultado geral positivo, com aproximadamente US$ 2,30 milhões em faturamento, US$ 286,40 mil em lucro e margem global de 12,47%.
- O lucro cresceu em todos os anos, mas faturamento, volume e margem não evoluíram sempre na mesma direção.
- A melhora de 2015 esteve associada principalmente a Technology, especialmente Copiers, às vendas sem desconto e à maior eficiência das vendas com desconto alto.
- Descontos agressivos permaneceram com lucro e margem negativos.
- Furniture apresentou baixa eficiência principalmente por causa de Tables e Bookcases.
- Janeiro de 2015 foi o mês mais crítico, mostrando que ticket médio elevado não garante lucro.
- West apresentou o melhor desempenho regional, enquanto Central apresentou a menor eficiência.
- Consumer liderou em resultado absoluto, enquanto Home Office se destacou pela eficiência.

### Recomendações de Negócio
- Revisar a política de descontos agressivos.
- Investigar preços, custos e descontos de Tables e Bookcases.
- Avaliar os fatores que reduzem a eficiência da região Central.
- Preservar e estudar as práticas associadas ao desempenho de Technology e Copiers.
- Monitorar faturamento, lucro e margem em conjunto nas próximas etapas do projeto.

### Principais Aprendizados
- Uma dimensão com maior faturamento ou lucro não é necessariamente a mais eficiente.
- Margem global permite comparar a eficiência de grupos com volumes diferentes.
- A função `resumir_por_grupo` pôde ser reutilizada nas análises anual, mensal, por categoria, subcategoria, região e segmento.
- O refinamento progressivo de uma pergunta, do resultado geral até categorias, subcategorias e descontos, ajuda a localizar explicações sustentadas pelos dados.
- Uma conclusão executiva deve sintetizar resultados, riscos e possíveis ações sem repetir todos os cálculos do notebook.

### Status
- Análise final da base tratada concluída.
- Perguntas principais respondidas e documentadas.
- Conclusão executiva registrada no notebook.
- Tabelas revisadas e formatadas sem alterar os valores numéricos originais.
- Estrutura de títulos revisada e padronizada.
- Etapa de cálculos encerrada sem necessidade de novas investigações obrigatórias.
- Visualizações e dashboard permanecem como próxima fase do projeto.

### Próximos Passos
- Planejar os gráficos que representam os principais insights.
- Iniciar a etapa de visualização de dados.
- Organizar os commits da conclusão da análise final.
- Criar o README após a criação das visualizações e do dashboard.

## 2026-08-10 - Dia 20: Início da Visualização de Dados

### Objetivos
- Iniciar a etapa de visualização dos resultados da análise final.
- Praticar a escolha e a construção de gráficos com Seaborn e Matplotlib.
- Transformar os principais insights em representações visuais claras.

### Atividades Realizadas
- Criação do notebook `notebooks/visualizacoes.ipynb`.
- Carregamento da base tratada com a função `carregar_dados`.
- Agrupamento e soma do lucro por ano.
- Criação do gráfico de linha da evolução do lucro anual entre 2014 e 2017.
- Formatação dos anos no eixo X e dos valores do lucro em milhares no eixo Y.
- Agrupamento e soma do lucro por categoria.
- Criação da estrutura inicial do gráfico de barras de lucro total por categoria.
- Identificação de que a formatação de anos não deve ser reutilizada em um eixo categórico.

### Principais Aprendizados
- Gráficos de linha são adequados para acompanhar uma métrica ao longo do tempo.
- Gráficos de barras facilitam a comparação de resultados entre categorias.
- O `reset_index()` transforma o agrupamento em um DataFrame apropriado para o Seaborn.
- A formatação dos eixos deve respeitar o tipo de dado apresentado: anos são numéricos e categorias são textuais.

### Status
- Primeiro gráfico de visualização concluído.
- Gráfico de lucro por categoria iniciado e com a causa do problema de eixo identificada.
- Personalização visual detalhada deixada para uma etapa posterior.

### Próximos Passos
- Criar visualizações para os demais insights prioritários da análise final.
- Definir uma identidade visual comum depois que as estruturas dos gráficos estiverem prontas.

## 2026-09-07 - Dia 21: Conclusão das Visualizações Principais

### Objetivos
- Concluir as visualizações prioritárias da análise final.
- Representar visualmente resultado absoluto, eficiência e prejuízo.
- Iniciar a padronização visual do notebook.

### Atividades Realizadas
- Conclusão do gráfico de lucro total por categoria.
- Criação do gráfico de lucro das subcategorias de Furniture, com destaque para Tables e Bookcases.
- Criação do gráfico de lucro por faixa de desconto.
- Criação dos gráficos de lucro total e margem global por região.
- Criação do gráfico de evolução do lucro nos 48 meses analisados.
- Destaque visual dos meses com prejuízo no gráfico mensal.
- Criação do gráfico de margem global por segmento.
- Configuração de um tema global com `sns.set_theme`.
- Definição de uma paleta reutilizável para dados principais, destaques, prejuízos e linhas de referência.
- Aplicação de cores condicionais para diferenciar resultados positivos, prejuízos e pontos de atenção.
- Validação da execução das células do notebook sem erros.

### Insights Representados
- O lucro anual cresceu entre 2014 e 2017.
- Technology apresentou o maior lucro entre as categorias.
- Tables e Bookcases reduziram o resultado de Furniture.
- Algumas faixas de desconto apresentaram resultado negativo.
- West liderou o lucro e a margem regional, enquanto Central apresentou a menor margem.
- Julho de 2014 e janeiro de 2015 foram os meses com prejuízo.
- Home Office apresentou a maior margem global entre os segmentos.

### Principais Aprendizados
- Cores devem comunicar significado e não servir apenas como decoração.
- O vermelho foi reservado para prejuízos, enquanto a cor de destaque identifica pontos relevantes sem resultado negativo.
- `ax.patches` e `zip()` permitem relacionar cada barra ao valor que ela representa.
- Linhas de referência ajudam a separar visualmente lucro e prejuízo.
- Uma identidade visual definida no início reduz repetição e mantém consistência entre gráficos.

### Status
- O notebook possui oito visualizações principais.
- As estruturas dos gráficos e a padronização de cores foram concluídas.
- Os principais resultados da análise final estão representados visualmente.
- A revisão final de espaçamento e legibilidade ficou pendente.

### Próximos Passos
- Ajustar o espaçamento global e revisar a legibilidade dos títulos, eixos e legendas.
- Executar e revisar visualmente o notebook completo.
- Encerrar a branch de visualização depois da revisão final.
- Iniciar o desenvolvimento do dashboard em uma branch própria.
