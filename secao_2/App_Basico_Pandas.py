import pandas as pd
import streamlit as st
import numpy as np
import altair as alt

# AULA 8

st.json({
     'foo': 'bar',
     'baz': 'boz',
     'stuff': [
         'stuff 1',
         'stuff 2',
         'stuff 3',
         'stuff 5',
     ],
 })

meuObjeto = {
    'banana': 'amarela',
    'limão': 'verde',
    'laranja': 'laranja'
 }

st.json(meuObjeto)

# AULA 6

# st.header('DATAFRAME')
# "Gerando um dataframe aleatório 5x5"
# df = pd.DataFrame(
#     np.random.randn(5, 5),
#     columns=('col %d' % i for i in range(5)))

# st.subheader("Exemplo 1 - imprimindo o Dataframe")
# st.dataframe(df)

# st.subheader("Exemplo 2 - Alterando as dimensões")
# st.dataframe(df, 300, 200)

# st.subheader("Exemplo 3 - Dando um destaque nos maiores valores")
# st.dataframe(df.style.highlight_max(axis=0))

# st.header('TABLE - Similar ao Dataframe, mas o conteúdo de TABLE é estático')
# st.subheader("Exemplo 4 - Imprimindo os dados com Table")
# st.table(df)

# st.header('METRIC - Similar ao Dataframe, mas o conteúdo de TABLE é estático')
# st.subheader('Exemplo 5 - Temperatura')
# st.metric(label="Temperatura", value="22 °C", delta="1 °C")

# st.subheader('Exemplo 6 - Exemplo com 3 colunas')
# col1, col2, col3 = st.columns(3)
# col1.metric("Temperatura", "25 °C", "2 °C")
# col2.metric("Vento", "10 Km/h", "-8%")
# col3.metric("Humidade", "86%", "4%")

# st.subheader('Exemplo 7 - alterando cor do delta')
# st.metric(label="Gas price", value=4, delta=-0.5,
#      delta_color="inverse")

# st.metric(label="Active developers", value=123, delta=123,
#      delta_color="off")

# AULA 5

# title
# st.title('Texto com maior destaque - Título')

# # header
# st.header('Texto com pouco destaque - Cabeçalho')

# # subheader
# st.subheader("Texto com pouco destaque - subcabeçalho")

# # markdown
# "Texto sem nenhuma função"
# st.write('Este é um *write*')
# st.markdown('Este é um *markdown*')

# # caption
# st.caption('Texto com fonte pequena usado para descrições e outros detalhamentos')

# # code
# code = '''if(hungry > 0):
#     return "go to refrigerator"
# else:
#     return "study Streamlit"'''
# st.code(code, language='python')

# # text
# st.text('Texto usando st.text')

# # Latex https://katex.org/docs/supported.html
# st.latex('\int x²+y²+32ab \isin x²+y²+z²')

# AULA 4
# Exemplo 1
# st.write('Write and *Magic*')

# #Exemplo 2
# st.write(pd.DataFrame({
#     'Coluna A': [1, 2,3,4,5],
#     'Coluna B': ["Cachorro", "Gato", "Cavalo","Vaca","Zebra"],
# }))

# st.write(pd.DataFrame({
#     'Coluna A': [1,2,3,4,5],
#     'Coluna B': ["Dog", "Cat", "Horse","Cow","Zebra"],
# }))

# # #Exemplo 3
# array = [1, 2, "abc", "Martin", True]
# st.write(array)

# # #Exemplo 4
# array = [1,2, 'abc', 'Martin', True]
# st.write('aqui teremos uma array:', array)


# #Exemplo 5
# df = pd.DataFrame(
#     np.random.randn(200, 3),
#     columns=['a', 'b', 'c']
# )

# c = alt.Chart(df).mark_circle().encode(
#     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c']
# )

# st.write(df)
# st.write(c)

# AULA 3
# df = pd.DataFrame({'col1': [1, 2, 3]})
# df

# '''
# Com o magic você pode escrever diretamente no texto!
# '''

# x = 'Hello World!'
# x


