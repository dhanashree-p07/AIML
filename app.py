import streamlit as st

st.title("My AI/ML App")

st.write("Welcome to my AI/ML project!")

st.header("About the Project")
st.write("This is my first Streamlit application.")

name = st.text_input("Enter your name:")

if name:
    st.success(f"Hello {name}! ")
