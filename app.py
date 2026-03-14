import streamlit as st
import pandas as pd
import plotly.express as px

# título da aplicação
st.header('Análise Exploratória de Dados - Anúncios de Vendas de Carros')

car_data = pd.read_csv('vehicles.csv')  # lendo os dados
build_histogram = st.checkbox('Criar um histograma')  # criar um botão

if build_histogram:  # se a caixa de seleção for selecionada
    # escrever uma mensagem
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

car_data = pd.read_csv('vehicles.csv')  # lendo os dados
build_scatter = st.checkbox('Criar um gráfico de dispersão')  # criar um botão

if build_scatter:  # se a caixa de seleção for selecionada
    # escrever uma mensagem
    st.write(
        'Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')

    # criar um gráfico de dispersão
    fig = px.scatter(car_data, x="odometer", y="price")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
