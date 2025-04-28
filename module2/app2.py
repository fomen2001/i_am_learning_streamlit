import streamlit as st 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
import plotly.express as px

##################################Plotly###########
st.subheader("Plotly")
#dataframe des temperatures hebdommadaire

temps = pd.DataFrame(
    {'day': ['Monday','Tuesday','Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
     'temps' : [28,27, 25, 31, 32, 35, 36]}
)
st.write(temps)
#diagramme inter actif
fig = px.bar(
    data_frame=temps,
    x="day",
    y="temps", title="Temperature moyennes journalieres"
)
st.plotly_chart(fig)

#nuage de points inter actif
cars = pd.read_csv("Automobile_data.csv")
st.dataframe(cars)

numeric_cols = cars.select_dtypes(exclude="object").columns.to_list()
var_x =st.selectbox("choisis la variable en abscisse", numeric_cols)
var_y =st.selectbox("choisis la variable en ordonnee", numeric_cols)
categorical_cols = cars.select_dtypes(include="object").columns.to_list()
var_col = st.selectbox("couleur", categorical_cols)


fig2 = px.scatter(
    data_frame=cars,
    x=var_x,
    y=var_y,
    color=var_col, 
    title=str(var_y) + " Vs " + str(var_x)
)
st.plotly_chart(fig2)
