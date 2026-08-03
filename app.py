import streamlit as st
st.title("my first streamlit app")


name=st.text_input("Enter your name")
if st.button("submit"):
   st.write(f"Hello,{name}")
