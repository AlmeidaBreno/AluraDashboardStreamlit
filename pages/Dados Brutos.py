import pandas as pd
import requests
import streamlit as st

st.title('DADOS BRUTOS')

url = 'https://labdados.com/produtos'

response = requests.get(url)
dados = pd.DataFrame.from_dict(response.json())
dados['Data da Compra'] = pd.to_datetime(dados['Data da Compra'], format = '%d/%m/%Y')

with st.expander('Colunas'):
    colunas = st.multiselect('Selecione as colunas', list(dados.columns), list(dados.columns))

st.sidebar.title('Filtros')
with st.sidebar.expander('Nome do Produto'):
    produtos = st.multiselect('Selecione os produtos', dados['Produto'].unique(), dados['Produto'].unique())
with st.sidebar.expander('Categoria do Produto'):
    categorias = st.multiselect('Selecione as categorias', dados['Categoria do Produto'].unique(), dados['Categoria do Produto'].unique())
with st.sidebar.expander('Preço do Produto'):
    preco = st.slider('Selecione o preço', 0, 5000, (0,5000))
with st.sidebar.expander('Valor do Frete'):
    frete = st.slider('Valor do Frete', 0, 250, (0, 250))
with st.sidebar.expander('Data da compra'):
    data_compra = st.date_input('Selecione a data', (dados['Data da Compra'].min(), dados['Data da Compra'].max()))
with st.sidebar.expander('Vendedores'):
    vendedores = st.multiselect('Selecione o(s) vendedore(s)', dados['Vendedor'].unique(), dados['Vendedor'].unique())
with st.sidebar.expander('Local da compra'):
    local = st.multiselect('Selecione o local da compra', dados['Local da compra'].unique(), dados['Local da compra'].unique())
with st.sidebar.expander('Avaliação da compra'):
    avaliacao = st.slider('Selecione a Nota:', 1, 5, (1, 5))
with st.sidebar.expander('Tipo de pagamento'):
    tipo_pagamento = st.multiselect('Selecione os tipos de pagamento', dados['Tipo de pagamento'].unique(), dados['Tipo de pagamento'].unique())
with st.sidebar.expander('Quantidade de parcelas'):
    parcelas = st.slider('Selecione a Quantidade de parcelas', 1, 24, (1, 24))

st.dataframe(dados, use_container_width=True, hide_index=True)
