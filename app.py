import streamlit as st
st.title("checking the the person eligiable for vote or not")

age=st.number_input("Enter your age:")
if st.button("submit"):
   if age>=18:
      st.success("you are eligiable to vote...")
   else:
      st.write("not eligiable to vote..")
