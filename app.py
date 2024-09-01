import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px

datos = pd.read_csv('./sbux.csv')

#print(datos.info())

fig = px.histogram(datos,'Close')
fig.show()

st.plotly_chart(fig)

