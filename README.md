# Análise Exploratória de Anúncios de Vendas de Carros

[![Abrir aplicativo](https://img.shields.io/badge/Abrir%20aplicativo-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://projeto-sprint-5-wmtu.onrender.com/)

Projeto de análise exploratória de dados de anúncios de venda de carros nos EUA. O aplicativo web, feito com Streamlit e Plotly, permite gerar gráficos interativos dos dados: histograma da quilometragem e gráfico de dispersão entre quilometragem e preço.

## Aplicativo online

https://projeto-sprint-5-wmtu.onrender.com/

Se o serviço estiver em repouso, o primeiro acesso pode levar alguns segundos.

## Dados

O arquivo `vehicles.csv` tem **51.525 anúncios** (de 01/05/2018 a 19/04/2019) e 13 colunas:

`price`, `model_year`, `model`, `condition`, `cylinders`, `fuel`, `odometer`, `transmission`, `type`, `paint_color`, `is_4wd`, `date_posted`, `days_listed`

As colunas `model_year`, `cylinders`, `odometer`, `paint_color` e `is_4wd` têm valores ausentes.

## Estrutura do projeto

```
Projeto_Sprint_5/
├── .streamlit/
│   └── config.toml     # configuração do servidor Streamlit
├── notebooks/
│   └── EDA.ipynb       # exploração inicial dos dados
├── app.py              # aplicativo Streamlit
├── requirements.txt    # dependências
├── vehicles.csv        # conjunto de dados
└── README.md
```

## Tecnologias

- Python 3
- Streamlit
- pandas
- Plotly Express
- Render (publicação do aplicativo)

## Como executar

1. Clone o repositório:

```powershell
   git clone https://github.com/Serg0-Proxy/Projeto_Sprint_5.git
   cd Projeto_Sprint_5
```

2. Crie e ative um ambiente virtual:

```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
```

3. Instale as dependências:

```powershell
   pip install -r requirements.txt
```

4. Execute o aplicativo:

```powershell
   streamlit run app.py
```

O aplicativo abre em `http://localhost:8501`.

Para abrir o notebook, instale também o `ipykernel` (`pip install ipykernel`) e abra `notebooks/EDA.ipynb` no VSCode.

## Como funciona

- Os dados são lidos uma única vez e mantidos em cache (`st.cache_data`), então marcar ou desmarcar opções não recarrega o arquivo.
- **Histograma:** distribuição da quilometragem (`odometer`) dos anúncios.
- **Gráfico de dispersão:** relação entre quilometragem (`odometer`) e preço (`price`).
- Os gráficos são interativos: zoom, seleção de regiões e informações ao passar o mouse.
