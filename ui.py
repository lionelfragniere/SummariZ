import streamlit as st
import requests

st.title("AI Summary Generator")
file = st.file_uploader("Upload your text file")

if file:
    res = requests.post("http://localhost:8000/summarize", files={"file": file})
    st.write(res.json()["summary"])
