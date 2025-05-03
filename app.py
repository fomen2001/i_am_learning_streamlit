import streamlit as st
import numpy as np
import joblib

st.title("Prediction du prix de vente d'une voiture en fonction de ses caracteristiques")
st.subheader("Application realisee par FOMENA")
st.markdown("Cette application utilise un modele de machine learning pour predire le prix d'une voiture")


#chargement du modele
model = joblib.load(filename="final_model.joblib")

#definition d'une fonction
def inference(symboling, normalized_losses,  wheel_base,  lengtht, width, height, curb_weight, engine_size, bore, stroke, compression_ratio ,horsepower, peak_rpm, city_mpg, highway_mpg):
    new_data = np.array([
        symboling, normalized_losses,  wheel_base,  lengtht, width,
        height, curb_weight, engine_size, bore, stroke, compression_ratio,
        horsepower, peak_rpm, city_mpg, highway_mpg
    ])
    pred = model.predict(new_data.reshape(1, -1))
    return pred
#L'utilisateur saisie une valeur pour chaque caracteristique de la voiture
symboling = st.number_input(label='symboling:', min_value=0, value=3)
normalized_losses = st.number_input('normalized-losses', value=100)
wheel_base = st.number_input('wheel_base', value=90)
lengtht = st.number_input('length', value=150)
width = st.number_input('width', value=65)
height = st.number_input('height', value=50)
curb_weight = st.number_input('curb-weight', value=100)
engine_size = st.number_input('engine-size', value=120)
bore = st.number_input('bore', value=3.0)
stroke = st.number_input('stroke', value=3.0)
compression_ratio = st.number_input('compression_ratio', value=9.0)
horsepower = st.number_input('horsepower-ratio', value=9.0)
peak_rpm = st.number_input('peak-rpm', value=5000)
city_mpg = st.number_input('city_mpg', value=20)
highway_mpg = st.number_input('rightway_mpg', value=30)

#creation du bouton predire
if st.button("predict"):
    prediction = inference(
        symboling, normalized_losses,  wheel_base,  lengtht, width, height, 
        curb_weight, engine_size, bore, stroke, compression_ratio,
        horsepower, peak_rpm, city_mpg, highway_mpg
        )
    st.success(prediction)
    