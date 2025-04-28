import streamlit as st 
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt


st.title("Application de distribution normale")
st.subheader("Auteur: FOMENA")
st.write(
    ("cette application permet d'afficher l'histogramme d'une distribution normale."
     " L'utilisateur a la possibilite de varier le nombre de bins "
     "et de donner un titre au graphique")
)




data = np.random.normal(size=1000)
data = pd.DataFrame(data, columns=["Dist_norm"])
#st.write(data.head()) 
st.dataframe(data.head())

fig, ax = plt.subplots()
n_bins = st.number_input(
    label="choisis un nombre de bins",
    min_value=10,
    value=20
)
ax.hist(data.Dist_norm, bins=n_bins)
title = st.text_input(
    label ="ecrire le titre du graphique"
)
plt.title(title)
st.pyplot(fig)