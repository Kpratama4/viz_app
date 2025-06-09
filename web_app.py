import streamlit as st
st.title("Hello World!")
st.header ("Welcome to MyGenAI App")

check_on = st.checkbox("Check me!")
if check_on:
    st.write("checkbox is checked!")

name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello {name}!")

import pandas as pd
data = pd.read_csv('iris_data.csv')

import plotly.express as px
fig = px.scatter(data, x="SepalLengthCm", y="SepalWidthCm", color="Species")
st.plotly_chart(fig, use_container_width=True)
