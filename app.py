"""Análise exploratória de anúncios de venda de carros (Streamlit + Plotly)."""

from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

DATA_PATH = Path(__file__).parent / "vehicles.csv"

LABELS = {
    "odometer": "Odômetro",
    "price": "Preço (US$)",
}


@st.cache_data
def load_data(path: Path) -> pd.DataFrame:
    """Lê o CSV uma única vez; nas próximas execuções usa o resultado em cache."""
    return pd.read_csv(path)


def show_histogram(df: pd.DataFrame) -> None:
    """Histograma da quilometragem (odômetro) dos anúncios."""
    fig = px.histogram(df, x="odometer", labels=LABELS)
    fig.update_layout(yaxis_title="Quantidade de anúncios")
    st.plotly_chart(fig)


def show_scatter(df: pd.DataFrame) -> None:
    """Gráfico de dispersão entre quilometragem e preço."""
    fig = px.scatter(df, x="odometer", y="price", labels=LABELS)
    st.plotly_chart(fig)


def main() -> None:
    st.set_page_config(page_title="Anúncios de Carros", page_icon="🚗")

    st.header("Análise Exploratória de Dados - Anúncios de Vendas de Carros")

    if not DATA_PATH.exists():
        st.error(f"Arquivo de dados não encontrado: {DATA_PATH.name}")
        st.stop()

    car_data = load_data(DATA_PATH)
    total = f"{len(car_data):,}".replace(",", ".")
    st.caption(f"{total} anúncios no conjunto de dados")

    if st.checkbox("Criar um histograma"):
        st.write(
            "Criando um histograma para o conjunto de dados "
            "de anúncios de vendas de carros"
        )
        show_histogram(car_data)

    if st.checkbox("Criar um gráfico de dispersão"):
        st.write(
            "Criando um gráfico de dispersão para o conjunto de dados "
            "de anúncios de vendas de carros"
        )
        show_scatter(car_data)


if __name__ == "__main__":
    main()
