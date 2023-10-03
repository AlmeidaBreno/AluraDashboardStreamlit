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
    local_compra = st.multiselect('Selecione o local da compra', dados['Local da compra'].unique(), dados['Local da compra'].unique())
with st.sidebar.expander('Avaliação da compra'):
    avaliacao = st.slider('Selecione a Nota:', 1, 5, (1, 5))
with st.sidebar.expander('Tipo de pagamento'):
    tipo_pagamento = st.multiselect('Selecione os tipos de pagamento', dados['Tipo de pagamento'].unique(), dados['Tipo de pagamento'].unique())
with st.sidebar.expander('Quantidade de parcelas'):
    qtd_parcelas = st.slider('Selecione a Quantidade de parcelas', 1, 24, (1, 24))

query = '''
Produto in @produtos and \
`Categoria do Produto` in @categorias and \
@preco[0] <= Preço <= @preco[1] and \
@frete[0] <= `Frete` <= @frete[1] and \
@data_compra[0] <= `Data da Compra` <= @data_compra[1] and \
Vendedor in @vendedores and \
`Local da compra` in @local_compra and \
@avaliacao[0] <= `Avaliação da compra` <= @avaliacao[1] and \
`Tipo de pagamento` in @tipo_pagamento and \
@qtd_parcelas[0] <= `Quantidade de parcelas` <= @qtd_parcelas[1]
'''

dados_filtrados = dados.query(query)
dados_filtrados = dados_filtrados[colunas]

st.dataframe(dados_filtrados, use_container_width=True, hide_index=True)

st.markdown(f'A tabela possui :blue[{dados_filtrados.shape[0]}] linhas e :blue[{dados_filtrados.shape[1]}] colunas')
