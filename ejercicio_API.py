import streamlit as st
import requests

url = "https://dummyjson.com/products/1"
data = requests.get(url).json()

st.title(data["title"])
st.write(data)
st.image(data["thumbnail"])