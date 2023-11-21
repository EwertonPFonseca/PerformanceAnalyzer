from pathlib import Path
import streamlit as st
import pandas as pd
import plotly.express as px
from utilidades import leitura_de_dados

def analise_categoria():
    # importando o dataframe
    leitura_de_dados()
    df_vendas = st.session_state['dados']['df_vendas']

    st.markdown('### Análise Categoria')
    filtro = st.sidebar.selectbox('Filtros:',['Vendas','Número de Pedidos','Número Clientes Distintos'])

    if filtro =='Vendas':
        col1,col2,col3 = st.columns(3)

        #metric Bike
        df_faturamento_bike = df_vendas[df_vendas['Categoria do Produto'] =='Bikes'].groupby('Categoria do Produto')['Total Venda'].sum().reset_index()
        total_bikes = f"R$ {df_faturamento_bike['Total Venda'].sum():_.2f}"
        total_bikes = total_bikes.replace('.', ',').replace('_', '.')
        col1.metric(' R$ Vendas Bikes', total_bikes)

        # metric Accessories
        df_faturamento_accessories = df_vendas[df_vendas['Categoria do Produto'] == 'Accessories'].groupby('Categoria do Produto')['Total Venda'].sum().reset_index()
        total_accessories = f"R$ {df_faturamento_accessories['Total Venda'].sum():_.2f}"
        total_accessories = total_accessories.replace('.', ',').replace('_', '.')
        col2.metric(' R$ Vendas Accessories', total_accessories)

        # metric Clothing
        df_faturamento_clothing = df_vendas[df_vendas['Categoria do Produto'] == 'Clothing'].groupby('Categoria do Produto')['Total Venda'].sum().reset_index()
        total_clothing= f"R$ {df_faturamento_clothing['Total Venda'].sum():_.2f}"
        total_clothing = total_clothing.replace('.', ',').replace('_', '.')
        col3.metric(' R$ Vendas Clothing', total_clothing)

        #gráfico de pizza
        df_pie_chart = df_vendas.groupby('Categoria do Produto')['Total Venda'].sum().reset_index()
        fig = px.pie(df_pie_chart,values='Total Venda',names='Categoria do Produto')
        st.plotly_chart(fig,use_container_width=True)



    elif filtro =='Número de Pedidos':
        df_pedidos = df_vendas.groupby('Categoria do Produto')['Ordem de Venda'].count().reset_index()
        fig= px.bar(df_pedidos,x='Categoria do Produto',y='Ordem de Venda',text_auto='.2s',title='Número de Pedidos por Categoria')
        st.plotly_chart(fig,use_container_width=True)

    elif filtro =='Número Clientes Distintos':
        count_distinct = df_vendas.groupby('Categoria do Produto')['Nome Cliente'].nunique().reset_index()
        count_distinct = count_distinct.sort_values(by='Nome Cliente')
        fig = px.bar(count_distinct,x='Nome Cliente',y='Categoria do Produto',text_auto='.2s',
                     labels={'Categoria do Produto':'Categoria do Produto','Nome Cliente':'Clientes'},
                     orientation='h',title='Número Clientes Distintos')
        st.plotly_chart(fig,use_container_width=True)

