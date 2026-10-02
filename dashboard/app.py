from pathlib import Path

import pandas as pd
import plotly.graph_objects as go
import streamlit as st


CAMINHO_DADOS = (Path(__file__).resolve().parents[1] / "dados" / "tratado" / "superstore_tratado.csv")

COR_PRINCIPAL = "#287271"
COR_DESTAQUE = "#E9C46A"
COR_NEGATIVA = "#C94C4C"
COR_REFERENCIA = "#5F6B6D"

ORDEM_DESCONTO = [
    "sem desconto",
    "desconto baixo",
    "desconto alto",
    "desconto agressivo",
]

CONFIG_GRAFICO = {
    "displayModeBar": False,
    "scrollZoom": False,
    "responsive": True,
}


st.set_page_config(page_title="Sample Superstore | Dashboard", layout="wide",)


@st.cache_data(show_spinner=False)
def carregar_dados(caminho):
    return pd.read_csv(caminho, encoding="utf-8", parse_dates=["Order Date", "Ship Date"],)


def filtrar_dados(dados, anos, regioes, categorias, segmentos):
    filtro = (
        dados["ano"].isin(anos)
        & dados["Region"].isin(regioes)
        & dados["Category"].isin(categorias)
        & dados["Segment"].isin(segmentos)
    )
    return dados.loc[filtro].copy()


def calcular_kpis(dados):
    faturamento = dados["Sales"].sum()
    lucro = dados["Profit"].sum()
    pedidos = dados["Order ID"].nunique()

    return {
        "faturamento": faturamento,
        "lucro": lucro,
        "margem": lucro / faturamento if faturamento else 0,
        "quantidade": dados["Quantity"].sum(),
        "pedidos": pedidos,
        "ticket_medio": faturamento / pedidos if pedidos else 0,
    }


def resumir_por_grupo(dados, coluna):
    resumo = (
        dados.groupby(coluna, as_index=False)
        .agg(
            faturamento_total=("Sales", "sum"),
            lucro_total=("Profit", "sum"),
        )
    )
    resumo["margem_global"] = (resumo["lucro_total"] / resumo["faturamento_total"])
    return resumo


def formatar_moeda(valor):
    valor_absoluto = abs(valor)
    if valor_absoluto >= 1_000_000:
        return f"US$ {valor / 1_000_000:.2f} mi"
    if valor_absoluto >= 1_000:
        return f"US$ {valor / 1_000:.1f} mil"
    return f"US$ {valor:,.2f}"


def formatar_inteiro(valor):
    return f"{valor:,.0f}".replace(",", ".")


def estilizar_grafico(figura, titulo, altura=360):
    figura.update_layout(
        title={"text": titulo, "x": 0, "xanchor": "left"},
        height=altura,
        margin={"l": 16, "r": 16, "t": 58, "b": 24},
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font={"size": 13},
        showlegend=False,
    )
    figura.update_xaxes(showgrid=False, zeroline=False)
    figura.update_yaxes(gridcolor="rgba(127,127,127,0.18)", zeroline=False)
    return figura


def criar_grafico_mensal(dados):
    mensal = (
        dados.assign(periodo=dados["Order Date"].dt.to_period("M").dt.to_timestamp())
        .groupby("periodo", as_index=False)
        .agg(
            faturamento_total=("Sales", "sum"),
            lucro_total=("Profit", "sum"),
        )
    )
    cores = [
        COR_NEGATIVA if lucro < 0 else COR_PRINCIPAL
        for lucro in mensal["lucro_total"]
    ]

    figura = go.Figure(
        go.Scatter(
            x=mensal["periodo"],
            y=mensal["lucro_total"],
            customdata=mensal[["faturamento_total"]],
            mode="lines+markers",
            line={"color": COR_PRINCIPAL, "width": 3},
            marker={"color": cores, "size": 8},
            hovertemplate=(
                "%{x|%m/%Y}<br>"
                "Lucro: US$ %{y:,.2f}<br>"
                "Faturamento: US$ %{customdata[0]:,.2f}"
                "<extra></extra>"
            ),
        )
    )
    figura.add_hline(y=0, line_color=COR_REFERENCIA, line_width=1)
    figura.update_yaxes(tickprefix="US$ ", tickformat="~s")
    figura.update_xaxes(tickformat="%Y")
    return estilizar_grafico(figura, "Evolução mensal do lucro", altura=390)


def criar_grafico_lucro(dados, coluna, titulo, altura=360, ordem=None):
    resumo = resumir_por_grupo(dados, coluna)
    if ordem:
        resumo[coluna] = pd.Categorical(
            resumo[coluna],
            categories=ordem,
            ordered=True,
        )
        resumo = resumo.sort_values(coluna, ascending=False)
    else:
        resumo = resumo.sort_values("lucro_total")

    cores = [
        COR_NEGATIVA if lucro < 0 else COR_PRINCIPAL
        for lucro in resumo["lucro_total"]
    ]
    figura = go.Figure(
        go.Bar(
            x=resumo["lucro_total"],
            y=resumo[coluna],
            customdata=resumo[["faturamento_total", "margem_global"]],
            orientation="h",
            marker_color=cores,
            hovertemplate=(
                "%{y}<br>"
                "Lucro: US$ %{x:,.2f}<br>"
                "Faturamento: US$ %{customdata[0]:,.2f}<br>"
                "Margem: %{customdata[1]:.1%}"
                "<extra></extra>"
            ),
        )
    )
    figura.add_vline(x=0, line_color=COR_REFERENCIA, line_width=1)
    figura.update_xaxes(tickprefix="US$ ", tickformat="~s")
    figura.update_yaxes(gridcolor="rgba(0,0,0,0)")
    return estilizar_grafico(figura, titulo, altura=altura)


def criar_grafico_margem(dados, coluna, titulo):
    resumo = resumir_por_grupo(dados, coluna).sort_values("margem_global")
    menor_margem = resumo["margem_global"].min()
    cores = [
        COR_NEGATIVA
        if margem < 0
        else COR_DESTAQUE
        if margem == menor_margem
        else COR_PRINCIPAL
        for margem in resumo["margem_global"]
    ]

    figura = go.Figure(
        go.Bar(
            x=resumo[coluna],
            y=resumo["margem_global"],
            customdata=resumo[["faturamento_total", "lucro_total"]],
            marker_color=cores,
            hovertemplate=(
                "%{x}<br>"
                "Margem: %{y:.1%}<br>"
                "Faturamento: US$ %{customdata[0]:,.2f}<br>"
                "Lucro: US$ %{customdata[1]:,.2f}"
                "<extra></extra>"
            ),
        )
    )
    figura.update_yaxes(tickformat=".0%")
    return estilizar_grafico(figura, titulo)


df = carregar_dados(CAMINHO_DADOS)

anos_disponiveis = sorted(df["ano"].unique().tolist())
regioes_disponiveis = sorted(df["Region"].unique().tolist())
categorias_disponiveis = sorted(df["Category"].unique().tolist())
segmentos_disponiveis = sorted(df["Segment"].unique().tolist())

with st.sidebar:
    st.header("Filtros")
    anos = st.multiselect(
        "Ano",
        anos_disponiveis,
        default=anos_disponiveis,
    )
    regioes = st.multiselect(
        "Região",
        regioes_disponiveis,
        default=regioes_disponiveis,
    )
    categorias = st.multiselect(
        "Categoria",
        categorias_disponiveis,
        default=categorias_disponiveis,
    )
    segmentos = st.multiselect(
        "Segmento",
        segmentos_disponiveis,
        default=segmentos_disponiveis,
    )
    st.divider()
    st.caption(
        f"Base: {df['Order Date'].min():%d/%m/%Y} a "
        f"{df['Order Date'].max():%d/%m/%Y}"
    )

df_filtrado = filtrar_dados(df, anos, regioes, categorias, segmentos)

st.title("Sample Superstore")
st.caption("Desempenho comercial e rentabilidade")

if df_filtrado.empty:
    st.warning("Nenhum dado encontrado para a combinação de filtros selecionada.")
    st.stop()

periodo_inicial = df_filtrado["Order Date"].min()
periodo_final = df_filtrado["Order Date"].max()
st.caption(
    f"Período selecionado: {periodo_inicial:%d/%m/%Y} a "
    f"{periodo_final:%d/%m/%Y} | {formatar_inteiro(len(df_filtrado))} registros"
)

kpis = calcular_kpis(df_filtrado)
colunas_kpi = st.columns(6)
metricas = [
    ("Faturamento", formatar_moeda(kpis["faturamento"])),
    ("Lucro", formatar_moeda(kpis["lucro"])),
    ("Margem global", f"{kpis['margem']:.1%}"),
    ("Pedidos", formatar_inteiro(kpis["pedidos"])),
    ("Quantidade vendida", formatar_inteiro(kpis["quantidade"])),
    ("Ticket médio", formatar_moeda(kpis["ticket_medio"])),
]

for coluna, (rotulo, valor) in zip(colunas_kpi, metricas):
    coluna.metric(rotulo, valor, border=True)

st.subheader("Evolução")
st.plotly_chart(
    criar_grafico_mensal(df_filtrado),
    use_container_width=True,
    config=CONFIG_GRAFICO,
    key="lucro_mensal",
)

st.subheader("Rentabilidade")
coluna_categoria, coluna_regiao = st.columns(2)
with coluna_categoria:
    st.plotly_chart(
        criar_grafico_lucro(
            df_filtrado,
            "Category",
            "Lucro por categoria",
        ),
        use_container_width=True,
        config=CONFIG_GRAFICO,
        key="lucro_categoria",
    )

with coluna_regiao:
    st.plotly_chart(
        criar_grafico_margem(
            df_filtrado,
            "Region",
            "Margem global por região",
        ),
        use_container_width=True,
        config=CONFIG_GRAFICO,
        key="margem_regiao",
    )

coluna_desconto, coluna_segmento = st.columns(2)
with coluna_desconto:
    st.plotly_chart(
        criar_grafico_lucro(
            df_filtrado,
            "faixa_desconto",
            "Lucro por faixa de desconto",
            ordem=ORDEM_DESCONTO,
        ),
        use_container_width=True,
        config=CONFIG_GRAFICO,
        key="lucro_desconto",
    )

with coluna_segmento:
    st.plotly_chart(
        criar_grafico_margem(
            df_filtrado,
            "Segment",
            "Margem global por segmento",
        ),
        use_container_width=True,
        config=CONFIG_GRAFICO,
        key="margem_segmento",
    )

st.plotly_chart(
    criar_grafico_lucro(
        df_filtrado,
        "Sub-Category",
        "Lucro por subcategoria",
        altura=560,
    ),
    use_container_width=True,
    config=CONFIG_GRAFICO,
    key="lucro_subcategoria",
)

with st.expander("Dados detalhados"):
    colunas_tabela = [
        "Order Date",
        "Order ID",
        "Customer Name",
        "Region",
        "Segment",
        "Category",
        "Sub-Category",
        "Sales",
        "Profit",
        "Discount",
        "Quantity",
    ]
    tabela = df_filtrado[colunas_tabela].rename(
        columns={
            "Order Date": "Data do pedido",
            "Order ID": "Pedido",
            "Customer Name": "Cliente",
            "Region": "Região",
            "Segment": "Segmento",
            "Category": "Categoria",
            "Sub-Category": "Subcategoria",
            "Sales": "Faturamento",
            "Profit": "Lucro",
            "Discount": "Desconto",
            "Quantity": "Quantidade",
        }
    )
    st.dataframe(
        tabela,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Data do pedido": st.column_config.DateColumn(format="DD/MM/YYYY"),
            "Faturamento": st.column_config.NumberColumn(format="US$ %.2f"),
            "Lucro": st.column_config.NumberColumn(format="US$ %.2f"),
            "Desconto": st.column_config.NumberColumn(format="percent"),
        },
    )
    st.download_button(
        "Baixar dados filtrados",
        data=df_filtrado.to_csv(index=False).encode("utf-8"),
        file_name="superstore_filtrado.csv",
        mime="text/csv",
    )
