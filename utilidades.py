from pathlib import Path
import streamlit as st
import pandas as pd


def leitura_de_dados():

    if not 'dados' in st.session_state:
        pasta_datasets = Path(__file__).parents[0]/'base_oficial.xlsx'
        df_vendas = pd.read_excel(pasta_datasets)
        df_vendas.sort_values('NumMes',ascending= True)
        df_vendas['Trimestre'] = df_vendas['Data do Pedido'].dt.to_period('Q').astype(str)


        dados = {'df_vendas':df_vendas}

        st.session_state['caminho_dataset'] = pasta_datasets
        st.session_state['dados'] = dados


