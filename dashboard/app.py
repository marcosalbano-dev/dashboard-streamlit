import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image
from conexao import conn
from dataset import df_listagem_cadastrados, df_listagem_titulados

cursor = conn.cursor()

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title='DASHBOARD DE VENDAS',
    page_icon='💲',
    layout='wide',
    initial_sidebar_state='expanded',
    menu_items={
        'Get Help': 'http://www.meusite.com.br',
        'Report a bug': "http://www.meuoutrosite.com.br",
        'About': "Esse app foi desenvolvido no nosso Curso."
    }
)

# -- Criar o sidebar
with st.sidebar:
    logo_teste = Image.open('./Midia/logo vizion.png')
    st.image(logo_teste, width=300)
    st.subheader('MENU - DASHBOARD IDACE')
    fMunicipio = st.selectbox(
        "Selecione o Município:",
        options=df_listagem_cadastrados['MUNICÍPIO'].sort_values().unique()
    )
    
    tab1_total_por_municipio = df_listagem_cadastrados.loc[(
        df_listagem_cadastrados['MUNICÍPIO'] == fMunicipio)
    ]
    
    fTerritorio = st.selectbox(
        "Selecione o Território:",
        options=df_listagem_cadastrados['TERRITÓRIO'].sort_values().unique()
    )
    
    tab2_total_por_territorio = df_listagem_cadastrados.loc[(
        df_listagem_cadastrados['TERRITÓRIO'] == fTerritorio)
    ]
    
st.subheader('CADASTRADOS POR MUNICÍPIO')    
tab1_total_por_municipio
st.subheader('CADASTRADOS POR TERRITÓRIO')
tab2_total_por_territorio