
from pathlib import Path
import streamlit as st
import pandas as pd
from utilidades import leitura_de_dados
from indicators import indicators
from analise_categoria import analise_categoria
from analise_temporal import analise_temporal
import plotly.express as px


st.set_page_config(page_title='Performance Analyzer', layout ='wide')

#### CSS ##################################
# Defina a cor desejada em formato CSS
estilos_h1 = 'color: gold; font-size: 24px;'
estilos_h2 = 'color: black; font-size: 20px;'
estilos_p = 'color: black; font-size: 18px;'

###########################################

st.markdown("# Bem-vindo ao Performance Analyzer")

st.divider()

st.sidebar.markdown(f'<p style="{estilos_h1}"> EW ANALYTICS</p>',unsafe_allow_html=True)
st.sidebar.markdown(f'<p style="{estilos_h2}"> Selecione uma Análise</p>',unsafe_allow_html=True)
opcao = st.sidebar.selectbox("Opções", ['Indicadores','Análise Temporal', 'Análise por Categoria'])

#importando o dataframe
leitura_de_dados()
df_vendas = st.session_state['dados']['df_vendas']

if opcao =='Indicadores':
    indicators()

elif opcao == 'Análise Temporal':
    analise_temporal()

elif opcao ==  'Análise por Categoria':
    analise_categoria()

