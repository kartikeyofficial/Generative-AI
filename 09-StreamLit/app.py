import streamlit as st
import pandas as pd
import numpy as np
st.title("Hello Streamlit")


## Display the simple text
st.write("this is a simple Text")

## Create a simple dataframe
df = pd.DataFrame({
  'first column':[1,2,3,4],
  'second column': [10,20,30,40]
})
st.write(df)

## Diaplay the Dataframe

st.write("Here is the Dataframe")


## Create the Line Chart

chart_data = pd.DataFrame(
  np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)