import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px

import my_project.data_wrangling as data_wrangling

def main():

    datos = pd.read_csv('./sbux.csv')
    #print(datos.info())

    boton_histograma = st.button('Clik aqui para generar el histograma')

    if boton_histograma:
        fig = px.histogram(datos,'Close')
        fig.show()
        st.plotly_chart(fig)

if __name__ == '__main__':
    print(__name__)
    print(data_wrangling.suma(1, 2))
    




