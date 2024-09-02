import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px

import helper

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
    print(helper.suma(1, 2))
    




