# app.py - Site interativo do Brasil nos Jogos Olímpicos

# Importando Bibliotecas
import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da Página
st.set_page_config(
    page_title="Brasil nas Olimpíadas",
    page_icon="🇧🇷",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Título do Site
st.title("🇧🇷 A Ascensão do Brasil nos Jogos Olímpicos de Verão")
st.markdown("""
Explore a evolução histórica do Brasil nos Jogos Olímpicos de Verão. 
Com gráficos interativos, analise as medalhas por ano, tipo e esporte! 🎖️
""")

# Carregando os Dados
@st.cache
def load_data():
    return pd.read_csv("olympics_medals.csv")

dados = load_data()

# Filtrar Jogos de Verão e Dados do Brasil
dados_verao = dados[dados["Season"] == "Summer"]
dados_brasil = dados_verao[dados_verao["NOC"] == "BRA"]

# 🔷 Gráfico 1: Evolução Temporal de Medalhas
st.header("📈 Evolução Temporal de Medalhas")
medalhas_temporais = (
    dados_brasil.groupby(["Year", "Medal"])["Medal"]  # Contar medalhas por ano e tipo
    .count()
    .unstack(fill_value=0)
)

fig1 = px.line(
    medalhas_temporais,
    x=medalhas_temporais.index,
    y=["Gold", "Silver", "Bronze"],
    title="Evolução de Medalhas do Brasil ao Longo dos Anos",
    labels={"value": "Número de Medalhas", "variable": "Tipo de Medalha"},
    markers=True,
)
fig1.update_traces(line=dict(width=3))
st.plotly_chart(fig1, use_container_width=True)

# 🔷 Gráfico 2: Distribuição por Esportes
st.header("🎯 Medalhas por Modalidade")
dados_por_esportes = (
    dados_brasil.groupby("Sport")["Medal"]
    .count()
    .sort_values(ascending=False)
)

fig2 = px.bar(
    dados_por_esportes,
    x=dados_por_esportes.values,
    y=dados_por_esportes.index,
    orientation="h",
    title="Esportes com Maior Contribuição de Medalhas",
    labels={"x": "Quantidade de Medalhas", "y": "Esporte"}
)
fig2.update_layout(yaxis=dict(categoryorder="total ascending"))
st.plotly_chart(fig2, use_container_width=True)

# 🔷 Conclusão e Reflexão
st.header("📜 Conclusão")
st.markdown("""
O Brasil conquistou destaque nas últimas edições dos Jogos Olímpicos. 
Com mais recursos e treinamentos, espera-se que continue crescendo como potência esportiva!
""")
