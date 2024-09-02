import streamlit as st
import pandas as pd
import numpy as no

# Creating a title
st.title("Streamlit Guide")

# Displaying a simple text
st.write("A simple text")

# Displaying a dataframe
df = pd.DataFrame({
    'Column 1':[1,2,3,4],
    'Column 2':[5,6,7,8],
})
st.write(df)

st.line_chart(df)
