import streamlit as st
import random

st.header("Hola Streamlit")
st.write("Si ves esto, la estructura esta funcionando")

st.header("Moneda")

if st.button("Lanzar"):
    st.write(random.choice(["Cara", "Cruz"]))