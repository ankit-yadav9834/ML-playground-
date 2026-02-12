import streamlit as st
import pandas as pd 
import numpy as np 

st.title("Streamlit text input ")

name = st.text_input("Enter your name: ")

# Creating a slidder 
age = st.slider("Select your age :", 0,100,25 )
st.write(f"Your age :{age}")

# Creating options box 

options = ["Python", "c++", "#C", "Java"]
choice = st.selectbox("Choose your favourite language ", options)
st.write(f"You selected {choice}")

if name:
    st.write(f"Hello {name} and your age is {age} ")



data =pd.DataFrame({
    'First column ': [1,2,3,4,5,6],
    'Second column ': [10,20,30,40,50,60]
})

st.write(data)
st.line_chart(data)
data.to_csv("sampledataforStreamlit")

# to upload file 

uploaded_file = st.file_uploader("Chosse a CSV file ", type = "csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(data)