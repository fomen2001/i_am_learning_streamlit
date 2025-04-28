import streamlit as st 
import pandas as pd 
import numpy as np 

st.title("Initialisation a la Data Viz avec streamlit")
st.subheader("Auteur: FOMENA")
st.markdown("***Cette application affiche differents types de graphiques***")

#Trace lineaire
random_data = np.random.normal(size=1000)
st.line_chart(random_data) 

#Diagramme en bar
bar_data = pd.DataFrame(
    [100, 19, 88, 54],
    ["A","B", "C", "D"]
    )
st.bar_chart(bar_data)

#Carte
df = pd.read_csv("new_york.csv")
st.write(df.head(10))
st.map(df[['longitude', 'latitude']])