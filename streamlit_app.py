import streamlit as st
import pandas as pd

st.title("🎈 Estoque disponível")
st.write(
    "Lista de estoque disponível para novas vendas. "
)

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

df