from pathlib import Path
import streamlit as st
import pandas as pd
from utilidades import leitura_de_dados
import plotly.graph_objects as go

def indicators():
    # importando o dataframe
    leitura_de_dados()
    df_vendas = st.session_state['dados']['df_vendas']

    st.markdown('### KPIs')

    valor_venda = df_vendas['Total Venda'].sum()

    col1,col2,col3= st.columns(3)

    # KPI faturamento
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        delta={'reference': 20000000},  # o delta mostra a diferença entre a meta e o valor atual
        value=valor_venda,
        title={'text': "R$ Total Vendas (meta-20M)"}
    ))
    fig.update_layout(
        height=300,  # Altura em pixels
        width=500  # Largura em pixels
    )

    col1.plotly_chart(fig)

    #KPI MARKUP
    custo_total = df_vendas['Custo Total do Produto'].sum()
    lucro = valor_venda - custo_total
    markup = lucro / custo_total

    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        delta={'reference': 0.65},  # o delta mostra a diferença entre a meta e o valor atual
        value=markup,
        title={'text': "%Markup (meta-0.65)"}


    ))
    fig.update_layout(
        height=300,  # Altura em pixels
        width=500  # Largura em pixels
    )

    col2.plotly_chart(fig)

    #KPI Redução número de vendas no cartão de crédito

    vendas_credito = df_vendas[df_vendas['Forma Pagamento']=='Cartão Crédito']['Forma Pagamento'].count()
    credito_lastyear=3900
    meta_reducao= 0.40
    reducao_atual= ((credito_lastyear-vendas_credito)/credito_lastyear)


    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        delta={'reference': meta_reducao},  # o delta mostra a diferença entre a meta e o valor atual
        value=reducao_atual,
        title={'text': "% Redução nas Vendas- Crédito (meta-0.40)"}

    ))
    fig.update_layout(
        height=300,  # Altura em pixels
        width=500  # Largura em pixels
    )

    col3.plotly_chart(fig)









