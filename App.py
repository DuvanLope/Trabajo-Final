import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

url = "airlines.csv"
airline = pd.read_csv(url)
imagen= "Departures airline.jpg"
imagen1= plt.imread(imagen)
plt.imshow(imagen1)
plt.axis('off') 

#Configuración del Streamlit

st.set_page_config(page_title="Airline Data Analysis", page_icon=":llegada_pasajeros", layout="wide")
st.title("Llegada de Pasajeros en Aerolíneas")
st.markdown("Este dashboard muestra la llegada de pasajeros en aerolíneas a lo largo del tiempo. Puedes explorar los datos y visualizar las tendencias utilizando los gráficos interactivos a continuación.")
st.image(imagen1, use_column_width=True)




print("Hello, World")
