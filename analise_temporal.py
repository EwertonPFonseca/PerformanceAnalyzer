from pathlib import Path
import streamlit as st
import pandas as pd
from utilidades import leitura_de_dados
import plotly.express as px
import plotly.graph_objects as go



def analise_temporal():
    # importando o dataframe
    leitura_de_dados()
    df_vendas = st.session_state['dados']['df_vendas']
    st.markdown('### Análise Temporal')

    df_vendas_mes = df_vendas.groupby('NumMes')['Total Venda'].sum().reset_index()
    filtro = st.sidebar.selectbox('Filtros:', ['Geral', 'Somente top 3 meses-Venda','Vendas Trimestrais','Venda x Lucro','Média de Custo Mensal'])

    if filtro == 'Geral':
        fig = px.bar(df_vendas_mes, x='NumMes', y='Total Venda',text_auto='.2s', title="R$ Vendas",
                     labels={'NumMes':'Mês'})
        st.plotly_chart(fig,use_container_width=True)

    elif filtro == 'Somente top 3 meses-Venda':
        df_vendas_top3 = df_vendas_mes.sort_values(by='Total Venda', ascending=False)
        df_vendas_top3 = df_vendas_top3.head(3)
        fig = px.bar(df_vendas_top3, x='NumMes', y='Total Venda',text_auto='.2s',title="Top 3- Meses com Maiores R$ Vendas",
                     labels={'NumMes':'Mês'})
        st.plotly_chart(fig, use_container_width=True)

    elif filtro == 'Vendas Trimestrais':
        df_vendas_trimestre = df_vendas.groupby('Trimestre')['Total Venda'].sum().reset_index()
        fig = px.bar(df_vendas_trimestre,x='Trimestre',y='Total Venda',text_auto='.2s',title ='R$ Vendas Trimestrais')
        st.plotly_chart(fig, use_container_width=True)

    elif filtro == 'Venda x Lucro':

        df_vendas_lucro = df_vendas.groupby('NumMes')[['Lucro','Total Venda']].sum().reset_index()
        fig = px.bar(df_vendas_lucro, x='NumMes', y=['Total Venda','Lucro'],text_auto='.2s', barmode='group',title='R$ Venda x Lucro',
                     labels={'NumMes':'Mês'})
        st.plotly_chart(fig, use_container_width=True)

    elif filtro == 'Média de Custo Mensal':
        #grafico accessories | filtro e groupby somente categoria accessories
        df_media_accessories = df_vendas[df_vendas['Categoria do Produto']=='Accessories'].groupby('NumMes')['Custo Total do Produto'].mean().reset_index()
        df_media_accessories = df_media_accessories.rename(columns={'Custo Total do Produto':'Custo Médio'})
        fig = px.bar(df_media_accessories,x='NumMes',y='Custo Médio',text_auto='.2s',title='R$ Custo Médio Mensal- Categoria Accessories',labels={'NumMes':'Mês'})
        st.plotly_chart(fig,use_container_width=True)

        #grafico bikes
        df_media_bikes = df_vendas[df_vendas['Categoria do Produto']=='Bikes'].groupby('NumMes')['Custo Total do Produto'].mean().reset_index()
        df_media_bikes = df_media_bikes.rename(columns={'Custo Total do Produto':'Custo Médio'})
        fig1= px.bar(df_media_bikes,x='NumMes',y='Custo Médio',text_auto='.2s', title='R$ Custo Médio Mensal - Categoria Bikes',labels={'NumMes':'Mês'})
        st.plotly_chart(fig1,use_container_width=True)

        #grafico clothing
        df_media_clothing= df_vendas[df_vendas['Categoria do Produto']=='Clothing'].groupby('NumMes')['Custo Total do Produto'].mean().reset_index()
        df_media_clothing= df_media_clothing.rename(columns={'Custo Total do Produto':'Custo Médio'})
        fig2= px.bar(df_media_clothing,x='NumMes',y='Custo Médio',text_auto='.2s',title='R$ Custo Médio Mensal- Categoria Clothing',labels={'NumMes':'Mês'})
        st.plotly_chart(fig2,use_container_width=True)

