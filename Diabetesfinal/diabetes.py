import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

st.title("Análisis de Riesgo de Diabetes")
#-------

st.write("""Este proyecto analiza un dataset de factores de riesgo de diabetes
como edad, IMC, presión arterial y glucosa para identificar patrones
asociados al riesgo de desarrollar la enfermedad.
""")
#-------

st.header("Objetivos")
#-------

st.write("""- Analizar factores de riesgo asociados a la diabetes.
- Identificar patrones en variables como edad, glucosa y BMI.
- Visualizar tendencias y distribución de los datos.
""")
#-------

st.header("Filtros")
df = pd.read_csv("diabetes_risk_dataset.csv")
st.sidebar.header("Filtros")
edad = st.sidebar.slider("Edad",int(df["age"].min()),int(df["age"].max()),(20,60))
df = df[(df["age"] >= edad[0]) & (df["age"] <= edad[1])]

BMI
nivel de glucosa
resultado diabetes (0 / 1)
#-------



