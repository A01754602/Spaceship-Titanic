import streamlit as st
import numpy as np
import requests

# URL de la API Flask que has desplegado
FLASK_API_URL = "http://<tu-servidor>:8080/predictjson"

# Título de la app
st.title("Predicción de Supervivencia en Spaceship Titanic")

# Crear los sliders y entradas de datos

# Selección de Planeta de origen
home_planet = st.selectbox("Planeta de origen", ["Earth", "Europa", "Mars"])

# Selección de Criosueño
cryosleep = st.radio("¿Estaba en Criosueño?", ["Sí", "No"])

# Edad
age = st.slider("Edad", 0, 100, 30)

# Servicios del barco
room_service = st.slider("Room Service", 0, 10000, 0)
food_court = st.slider("Food Court", 0, 10000, 0)
shopping_mall = st.slider("Shopping Mall", 0, 10000, 0)
spa = st.slider("Spa", 0, 10000, 0)
vr_deck = st.slider("VRDeck", 0, 10000, 0)

# Destino
destination = st.selectbox("Destino", ["TRAPPIST-1e", "55 Cancri e", "PSO J318.5-22"])

# Cabina
deck = st.selectbox("Deck", ["A", "B", "C", "D", "E", "F", "G", "T"])
side = st.selectbox("Side", ["P", "S"])
num = st.number_input("Número de Cabina", min_value=0, max_value=2000, step=1)

# Botón para enviar los datos
if st.button("Predecir"):
    # Convertir las selecciones a los valores correctos que espera el modelo
    cryosleep_val = 1 if cryosleep == "Sí" else 0
    home_planet_val = {"Earth": 0.424, "Europa": 0.626, "Mars": 0.5586}[home_planet]
    destination_val = {"TRAPPIST-1e": 0.4711, "55 Cancri e": 0.61, "PSO J318.5-22": 0.5037}[destination]
    deck_val = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "T": 7}[deck]
    side_val = {"P": 0, "S": 1}[side]

    # Crear el JSON con los datos
    input_data = {
        "HomePlanet": home_planlet_val,
        "CryoSleep": cryosleep_val,
        "Age": age,
        "RoomService": room_service,
        "FoodCourt": food_court,
        "ShoppingMall": shopping_mall,
        "Spa": spa,
        "VRDeck": vr_deck,
        "Destination": destination_val,
        "Deck": deck_val,
        "Side": side_val,
        "Num": num
    }

    # Enviar los datos a la API Flask
    response = requests.post(FLASK_API_URL, json=input_data)

    # Obtener y mostrar la predicción
    prediction = response.json().get('Prediction')
    
    # Mostrar el resultado en la interfaz
    if prediction == "True":
        st.success('El pasajero sobrevive.')
    else:
        st.error('El pasajero no sobrevive.')