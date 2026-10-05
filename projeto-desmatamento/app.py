import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(page_title="Dashboard Ambiental Brasil", layout="wide")


st.title("🌲 Desmatamento e Preservação Ambiental no Brasil")

@st.cache_data
def load_data():
    return pd.read_csv("dados/simulacao_desmatamento_brasil.csv")

df = load_data()

st.sidebar.header("Filtros de Análise")
ano_filtro = st.sidebar.multiselect("Ano", df['ano'].unique(), default=df['ano'].unique())
regiao_filtro = st.sidebar.multiselect("Região", df['regiao'].unique(), default=df['regiao'].unique())
bioma_filtro = st.sidebar.multiselect("Bioma", df['bioma'].unique(), default=df['bioma'].unique())

df_filtrado = df[
    (df['ano'].isin(ano_filtro)) &
    (df['regiao'].isin(regiao_filtro)) &
    (df['bioma'].isin(bioma_filtro))
]

st.sidebar.markdown("---")
st.sidebar.header("Navegação")
pagina = st.sidebar.radio("Ir para:", ["Visão Geral", "Análise Estatística Avançada"])

if pagina == "Visão Geral":
    st.subheader("Visão Geral dos Indicadores")
    

    col1, col2, col3 = st.columns(3)
    col1.metric("Área Desmatada (km²)", f"{df_filtrado['area_desmatada_km2'].sum():,.0f}")
    col2.metric("Total de Queimadas", f"{df_filtrado['focos_queimada'].sum():,.0f}")
    col3.metric("Emissão CO₂ (ton)", f"{df_filtrado['emissoes_co2'].sum():,.0f}")

    colA, colB = st.columns(2)
    with colA:
        df_tempo = df_filtrado.groupby('ano')['area_desmatada_km2'].sum().reset_index()
        fig1 = px.line(df_tempo, x='ano', y='area_desmatada_km2', title="Desmatamento por Ano", markers=True)
        st.plotly_chart(fig1, use_container_width=True)
        
    with colB:
        df_bioma = df_filtrado.groupby('bioma')['area_desmatada_km2'].sum().reset_index()
        fig2 = px.bar(df_bioma, x='bioma', y='area_desmatada_km2', title="Desmatamento por Bioma", color='bioma')
        st.plotly_chart(fig2, use_container_width=True)

        st.subheader("Tabela Detalhada de Dados")
    st.dataframe(df_filtrado[['data', 'uf', 'bioma', 'area_desmatada_km2', 'focos_queimada', 'nivel_risco']].head(100))
    
    st.subheader("Conclusão Executiva")
    st.markdown("""
    A análise visual e os KPIs demonstram padrões claros de sazonalidade e concentração de desmatamento em biomas e estados específicos. 
    Conclui-se que as políticas de preservação devem ser intensificadas nos meses de pico de queimadas e focadas nas regiões de maior risco para mitigar as emissões de CO₂.
    """)

elif pagina == "Análise Estatística Avançada":
    st.subheader("Análise Estatística de Correlação")
    st.markdown("Nesta página, aplicamos métodos estatísticos avançados para entender o comportamento dos dados.")
    
    correlacao = df_filtrado['area_desmatada_km2'].corr(df_filtrado['focos_queimada'])
    
    col_corr, col_vazia = st.columns([1, 2])
    col_corr.metric("Coeficiente de Correlação (Pearson)", f"{correlacao:.4f}")
    st.info("💡 **Interpretação:** Um valor próximo de 1 indica uma correlação positiva muito forte. Isso prova estatisticamente que o aumento da área desmatada está diretamente ligado ao aumento dos focos de queimada.")
    
    colC, colD = st.columns(2)
    with colC:
        fig3 = px.scatter(df_filtrado, x='area_desmatada_km2', y='focos_queimada', color='bioma', 
                          title="Dispersão: Desmatamento x Queimadas")
        st.plotly_chart(fig3, use_container_width=True)
        
    with colD:
        df_heatmap = df_filtrado.groupby(['mes', 'ano'])['focos_queimada'].sum().reset_index()
        fig4 = px.density_heatmap(df_heatmap, x='ano', y='mes', z='focos_queimada', 
                                  title="Concentração de Focos (Heatmap)", color_continuous_scale="YlOrRd")
        st.plotly_chart(fig4, use_container_width=True)