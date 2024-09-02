import streamlit as st

st.title('Text Input')

name = st.text_input('Enter your name:')
age = st.slider("Select your age",0,100)

options = ['Male','Female','Choose not to say']
choice = st.selectbox('Choose your favourite language:',options)

if name:
    st.write(f'Hello, {name}')

if age:
    st.write(f'Your age is {age}')

if choice:
    st.write(f'You are a {choice}')

'''
Extras

Below are decorators to implement caching mechanism
@st-cache_data => used to cache computations that return data
@st-cache_resource=> used cache global resources like ML models or database connections – unserializable objects that you don't want to load multiple times. 

'''