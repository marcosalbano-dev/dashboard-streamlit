import pandas as pd
import streamlit as st
import numpy as np
import altair as alt

# AULA 4
# Exemplo 1
st.write('Write and *Magic*')

#Exemplo 2
st.write(pd.DataFrame({
    'Coluna A': [1, 2,3,4,5],
    'Coluna B': ["Cachorro", "Gato", "Cavalo","Vaca","Zebra"],
}))

st.write(pd.DataFrame({
    'Coluna A': [1,2,3,4,5],
    'Coluna B': ["Dog", "Cat", "Horse","Cow","Zebra"],
}))

# #Exemplo 3
array = [1, 2, "abc", "Martin", True]
st.write(array)

# #Exemplo 4
array = [1,2, 'abc', 'Martin', True]
st.write('aqui teremos uma array:', array)


#Exemplo 5
df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c']
)

c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c']
)

st.write(df)
st.write(c)



# AULA 3
# df = pd.DataFrame({'col1': [1, 2, 3]})
# df

# '''
# Com o magic você pode escrever diretamente no texto!
# '''

# x = 'Hello World!'
# x


