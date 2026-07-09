import streamlit as st

st.title("Calculator")

a = st.number_input("First Number")
b = st.number_input("Second Number")

if st.button("Add"):
    st.success(a + b)