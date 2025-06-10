import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title = 'Iris'
    layout = 'wide'
)
st.title("Hello World!")
st.header ("Welcome to MyGenAI App")

with st.sidebar:
	st.markdown('**Pilih Species**')
	check_setosa = st.checkbox('Iris-setosa', value=True)
	check_versicolor = st.checkbox('Iris-versicolor', value=True)
	check_virginica = st.checkbox('Iris-virginica', value=True)

	species = []
	if check_setosa:
		species.append('Iris-setosa')
	if check_versicolor:
		species.append('Iris-versicolor')
	if check_virginica:
		species.append('Iris-virginica')
	
	st.markdown('**Pilih Variabel**')
	var1 = st.radio('Variabel Utama',
			('SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm')
		)
	var2 = st.radio('Variabel Sekunder',
			('SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm')
		)

data = pd.read_csv('iris_data.csv')
data = data.query('Species in @species')

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

with col1:
	st.dataframe(data)

with col2:
	fig_pie = px.pie(data, names='Species')
	st.plotly_chart(fig_pie, use_container_width=True)

with col3:
	fig_box = px.box(data, x=var1, color='Species')
	st.plotly_chart(fig_box, use_container_width=True)

with col4:
	fig_scatter = px.scatter(data, x=var1, y=var2, color='Species')
	st.plotly_chart(fig_scatter, use_container_width=True)

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
