import altair as alt
import pandas as pd
import streamlit as st

fonte = pd.DataFrame({
    'a' : ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
    'b' : [28, 55, 43, 91, 81, 53, 19, 87, 52]
})

fonte


graf_barras = alt.Chart(fonte).mark_bar().encode(
    x='a',
    y='b',
    color='a',
    tooltip=['a', 'b']
)

rotulo_barra = graf_barras.mark_text(
    dy=-6,
    size=17
).encode(
    text='b'
)
st.subheader('Plot gráfico de barras')
st.altair_chart(graf_barras + rotulo_barra, use_container_width=True)

graf_area = alt.Chart(fonte).mark_area(
    color='lightblue',
    interpolate='step-after',
    line=True
).encode(
    x='a',
    y='b',
    tooltip=['a', 'b']
)
rotulo_area = graf_area.mark_text(
    dy=-6,
    dx=30,
    size=17
).encode(
    text='b'
)


st.subheader('Plot gráfico de área')
st.altair_chart(graf_area + rotulo_area, use_container_width=True)

graf_pizza = alt.Chart(fonte).mark_arc().encode(
    theta=alt.Theta(field='b', type='quantitative'),
    color=alt.Color(field='a', type='nominal')
)

st.subheader('Plot gráfico de pizza')
st.altair_chart(graf_pizza)

# GRÁFICO DE BARRAS
df = pd.DataFrame({
    'a' : ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
    'b' : [28, 55, 43, 91, 81, 53, 19, 87, 52]
})

graf_barras = alt.Chart(df).mark_bar().encode(
    x='a',
    y='b',
    color='a',
    tooltip=['a', 'b']
)

rotulo_barra = graf_barras.mark_text(
    dy=-6,
    size=17
).encode(
    text='b'
)
st.subheader('Plot gráfico de barras')
st.altair_chart(graf_barras + rotulo_barra, use_container_width=True)

graf_barras_novo = alt.Chart(df).mark_bar(
        cornerRadiusTopLeft=10,
        cornerRadiusTopRight=10
    ).encode(
    x=alt.X('a', sort='y'),
    y='b',
    color=alt.condition(
        alt.datum.b > 43,
        alt.value('steelblue'),
        alt.value('black')
    )
)

rotulo = graf_barras_novo.mark_text(
    align='center',
    baseline='middle',
    size=14,
    dy=-10
).encode(
    text='b'
)

linha_media = alt.Chart(df).mark_rule(color='red').encode(
    y='mean(b)'
)

st.altair_chart(graf_barras_novo + rotulo + linha_media, use_container_width=True)

Vendas = pd.DataFrame({
    'Month': ['01-Jan', '02-Feb', '03-Mar', '04-Apr', '05-May', '06-Jun',
     '07-Jul','08-Ago', '09-Set', '10-Oct', '11-Nov', '12-Dec'],
    'product_A': [28, 55, 43, 91, 81, 53, 19, 87, 52, 85, 101, 77],
    'product_B': [ 93, 68, 79, 84, 81, 97, 109, 99, 125, 115, 120, 88]

})

st.subheader('GRÁFICO DE LINHAS: PRODUTO A & B')

graf_linha_A = alt.Chart(Vendas).mark_line(
    point=alt.OverlayMarkDef(color='red',size=100, filled=False, fill='white'),
    color='red'
).encode(
    x = alt.X('Month'),
    y = alt.Y('product_A',
    axis=alt.Axis(grid=False),
    scale=alt.Scale(domain=(0,160))),
    tooltip = ['Month', 'product_A', 'product_B']
).properties(
    width=600,
    height=600,
    title = 'VENDAS MENSAIS DOS PRODUTOS A & B'
)

graf_linha_B = alt.Chart(Vendas).mark_line(
    point=alt.OverlayMarkDef(color='green',size=100, filled=False, fill='white'),
    color='green'
).encode(
    x = alt.X('Month'),
    y = alt.Y('product_B'),
    tooltip = ['Month', 'product_A', 'product_B']
)

rotulo_A = graf_linha_A.mark_text(
    dy = -15,
    size=14
).encode(
    text = 'product_A'
)
rotulo_B = graf_linha_B.mark_text(
    dy = -15,
    size=14
).encode(
    text = 'product_B'
)

st.altair_chart(graf_linha_A+graf_linha_B+rotulo_A+rotulo_B)