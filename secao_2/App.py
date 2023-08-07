import pandas as pd
import streamlit as st
import altair as alt

df = pd.read_excel(
    io = 'faturamento.xlsx',
    engine='openpyxl',
    sheet_name='flow',
    usecols='A:B',
    nrows=15,
)

graf_area = alt.Chart(df).mark_area(
    line={'color':'black'},
    color='gray'
).encode(
    x = 'Year:T',
    y = 'Value:Q'
)

rotulo = graf_area.mark_text(
    align='center',
    baseline='middle',
    color='black',    
    size=14,
    dy=-18
).encode(text='Value')

st.subheader('VALORES ANUAIS')
st.altair_chart(graf_area+rotulo, use_container_width=True)
