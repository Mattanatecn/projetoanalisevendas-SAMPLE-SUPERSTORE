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
- ** la a "Causa Raiz":** O prejuízo em Mesas não é necessariamente logístico, mas sim estratégico (descontos agressivos que anulam a margem de lucro).
- **Recomendação de Negócio:** Interrupção imediata de promoções agressivas em Mesas e revisão do preço de venda para cobrir custos.

### 🚧 Bloqueios e Dificuldades
- Dificuldade inicial com fórmulas de soma $\rightarrow$ Superado com o uso de Barra de Status e Tabela Dinâmica.

### 🚀 Próximos Passos
- Implementar a arquitetura de Dashboard no Excel (KPIs $\rightarrow$ Gráficos $\rightarrow$ Slicers).
- Transformar a análise de "Tabelas" em um insight visual no dashboard.


## 📅 2026-05-22 - Dia 3: Finalização do Dashboard e Storytelling de Dados

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
