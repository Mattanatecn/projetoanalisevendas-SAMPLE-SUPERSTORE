# 📝 Devlog - Projeto Análise de Vendas Superstore

Este arquivo registra a evolução do projeto, as decisões tomadas e os aprendizados adquiridos.

## 📅 2026-05-09 - Dia 1: Pensamento Analítico e Exploração Inicial

### 🎯 Objetivos do Dia
- Compreender o contexto de negócio do dataset.
- Realizar a primeira exploração de dados via Excel.
- Identificar padrões de lucro e prejuízo.

### 🛠️ Atividades Realizadas
- **Entendimento do Dataset:** Análise de colunas e definição de KPIs (Vendas, Lucro e Ticket Médio).
- **Estruturação de Dados:** Transformação dos dados em Tabela Oficial (`Ctrl + T`) para garantir integridade e escalabilidade.
- **Análise Exploratória:**
    - Criação de Tabelas Dinâmicas para comparar Regiões e Categorias.
    - Identificação da região **West** como a mais lucrativa e a região **South** como a menos performante.
    - Comparação entre categorias: **Technology** (Alta margem) vs **Furniture** (Baixa margem/Volume alto).
- **Investigação de Causa Raiz (Root Cause Analysis):**
    - Drill-down na categoria *Furniture* para identificar a subcategoria **Tables** como a principal fonte de prejuízo.
    - Cruzamento de dados entre `Discount` e `Profit`, provando que descontos acima de 0% em Mesas resultam em lucro negativo.

### 💡 Principais Insights
- **Causa Raiz:** O prejuízo em Mesas não é necessariamente logístico, mas sim estratégico (descontos agressivos que anulam a margem de lucro).
- **Recomendação de Negócio:** Interrupção imediata de promoções agressivas em Mesas e revisão do preço de venda para cobrir custos.

### 🚧 Bloqueios e Dificuldades
- Dificuldade inicial com fórmulas de soma $\rightarrow$ Superado com o uso de Barra de Status e Tabela Dinâmica.

### 🚀 Próximos Passos
- Implementar a arquitetura de Dashboard no Excel (KPIs $\rightarrow$ Gráficos $\rightarrow$ Slicers).
- Transformar a análise de "Tabelas" em um insight visual no dashboard.


## 📅 2026-05-22 - Dia 2: Finalização do Dashboard e Storytelling de Dados

### 🎯 Objetivos do Dia
- Finalizar a camada visual do Dashboard Executivo.
- Implementar a análise de "Causa Raiz" visualmente.
- Garantir interatividade total entre filtros e KPIs.

### 🛠️ Atividades Realizadas
- **Construção de Gráficos Analíticos:**
    - Implementação do Gráfico de Rentabilidade por Categoria.
    - Criação do Gráfico de "Vilões" (Subcategorias com lucro negativo).
    - Desenvolvimento do Gráfico de Correlação (Desconto vs Lucro) especificamente para a subcategoria **Tables**, expondo que descontos $\ge$ 2% anulam a margem de lucro.
- **Interatividade Avançada:**
    - Configuração de Slicers (Região, Categoria, Segmento) com Conexões de Relatório para atualização simultânea de todos os visuais.
- **Resolução de Problemas Técnicos (KPIs Dinâmicos):**
    - Solução do problema de KPIs estáticos trocando fórmulas comuns por vínculos com Tabelas Dinâmicas.
    - Implementação da técnica de **"Célula Ponte"** e uso da função `INFODADOSTABELADINAMICA` (`GETPIVOTDATA`) para evitar que os KPIs sumissem ao filtrar a tabela (estabilização do Total Geral).

### 💡 Principais Insights
- **Storytelling:** O dashboard agora conduz o usuário do "Sinal de Alerta" (KPIs) $\rightarrow$ "Localização do Problema" (Gráfico de Vilões) $\rightarrow$ "Causa Raiz" (Gráfico de Descontos) $\rightarrow$ "Ação Recomendada" (Callout de Insight).

### 🚀 Próximos Passos
- Migrar a análise para o **VS Code**.
- Replicar a lógica de análise usando **Python e Pandas**.
- Evoluir as visualizações para bibliotecas interativas (**Plotly/Seaborn**).
- Transformar a análise em um Web App utilizando **Streamlit**.
            
## 📅 2026-05-26 — Dia 3: Configuração de Ambiente e Versionamento Profissional

### 🎯 Objetivos do Dia

- Migrar o projeto para o VS Code.
- Estabelecer uma arquitetura de pastas profissional.
- Configurar ambiente virtual Python e versionamento com Git/GitHub.

### 🛠️ Atividades Realizadas

**Arquitetura de Projeto**
Implementação de uma estrutura de pastas organizada (`dados/`, `notebooks/`, `src/`, `dashboard/`, `imagens/`) para separação de responsabilidades.

**Ambiente de Desenvolvimento**
- Criação e ativação de ambiente virtual (`.venv`) para isolamento de dependências.
- Instalação das principais bibliotecas de análise de dados:
  `pandas`, `matplotlib`, `seaborn`, `plotly` e `streamlit`.

**Versionamento Profissional**
- Configuração do arquivo `.gitignore` para evitar upload de arquivos desnecessários, como a pasta `.venv`.
- Inicialização do repositório Git e realização do primeiro commit da estrutura do projeto.
- Conexão e envio do projeto para um repositório remoto no GitHub.

**Organização de Dados**
Migração do dataset original e do arquivo de análise em Excel para a pasta `dados/bruto`.

### 🚀 Próximos Passos
- Iniciar a exploração de dados via Jupyter Notebook (`exploracao.ipynb`).
- Traduzir a lógica de análise do Excel para Pandas utilizando `groupby`, filtros e agregações.
- Replicar a análise de “Causa Raiz” das mesas utilizando código Python.

## 📅 2026-05-31 — Dia 4: Migração de Análise para Pandas e Validação de Dados

### 🎯 Objetivos do Dia
- Iniciar a exploração de dados via Jupyter Notebook.
- Replicar a lógica de KPIs globais do Excel utilizando Pandas.
- Identificar a subcategoria com maior impacto negativo no lucro.

### 🛠️ Atividades Realizadas
- **Implementação de Pipeline de Carga:**
    - Configuração de leitura de CSV utilizando `pd.read_csv`.
    - Resolução de conflitos de caminho de diretório (Windows Path) utilizando caminhos relativos (`../`).
    - Tratamento de erro de decodificação de caracteres (`UnicodeDecodeError`) implementando o encoding `latin1`.
- **Cálculo de KPIs Executivos:**
    - Implementação de somatórios para Vendas Totais e Lucro Total.
    - Criação de filtro booleano para isolar e somar apenas o Lucro Negativo.
- **Sincronização Excel $\leftrightarrow$ Pandas:**
    - Investigação de divergência de valores entre as ferramentas.
    - Identificação de erro de formatação no Excel (casas decimais ocultas), alinhando a visualização do dashboard com os dados reais do Python.
- **Análise de Segmentação (Groupby):**
    - Implementação de `groupby` por `Sub-Category` para ranqueamento de lucratividade.
    - Confirmação estatística de que a subcategoria **Tables** é o principal detrator do lucro global.

### 💡 Aprendizados Técnicos
- **Caminhos no Windows:** A importância do uso de *raw strings* (`r''`) ou caminhos relativos para evitar erros de sequências de escape (ex: `\b`).
- **Encoding:** Entendimento de que arquivos originados em ambiente Windows/Excel frequentemente exigem o encoding `latin1` em vez de `utf-8`.
- **Filtros vs. Agregações:** Diferença fundamental entre agrupar por uma coluna (etiqueta) e filtrar por um valor específico.
- **Integridade de Dados:** A importância de validar a formatação de células no Excel para evitar interpretações errôneas de valores arredondados.
- **criação branch** criação de uma nova branch para nõ mandar dados direto na main. 'feature/exploracao-pandas'.
### 🚀 Próximos Passos
- Realizar a análise de causa raiz das 'Tables' cruzando a métrica de `Discount` com `Profit`.
- Iniciar a transição da exploração para o script de limpeza (`src/limpeza.py`) para gerar o dataset tratado.

## 📅 2026-06-04 — Dia 5: Prova da Causa Raiz e Início da Limpeza de Dados

### 🎯 Objetivos do Dia
- Provar matematicamente a causa raiz do prejuízo em 'Tables' via Pandas.
- Iniciar o processo de limpeza e tratamento de dados (Data Cleaning).
- Documentar o código para transformar o notebook em um material educativo.

### 🛠️ Atividades Realizadas
- **Prova da Causa Raiz (Slicing & Filtering):**
    - Implementação de filtros compostos para isolar a subcategoria 'Tables'.
    - Criação de grupos de comparação: Vendas com Desconto $\ge$ 20% vs. Vendas com Desconto $<$ 20%.
    - Validação estatística: Lucro Total ($\approx$ -31k) para descontos altos vs. Lucro Total ($\approx$ 13k) para descontos baixos.
- **Limpeza Técnica (Data Typing):**
    - Conversão de tipos de dados: Transformação de `Order Date` e `Ship Date` de texto (`str`) para `datetime64`.
    - Garantia de integridade para futuras análises de sazonalidade e tempo de entrega.
- **Documentação Pedagógica:**
    - Revisão completa do notebook com a adição de comentários detalhados, explicando o "porquê" de cada função e a lógica de negócio aplicada.

### 💡 Principais Insights
- **Validação de Hipótese:** A correlação entre descontos agressivos e prejuízo em Mesas foi confirmada no Python, consolidando a análise feita anteriormente no Excel.
- **Importância da Tipagem:** A conversão de datas é o primeiro passo crítico para qualquer análise de séries temporais profissional.

### 🚀 Próximos Passos
- Análise de valores nulos (`.isnull().sum()`) para garantir a integridade do dataset.
- Criação de visualizações gráficas (Séborn/Matplotlib) para expor a causa raiz de forma executiva.
- Migração dos passos de limpeza para o script `src/limpeza.py`.
