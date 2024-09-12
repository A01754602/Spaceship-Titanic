from flask import Flask, request, jsonify
import numpy as np
import joblib

# Cargar el modelo de votación entrenado
model = joblib.load('voting_model.joblib')  # Guarda tu modelo de votación como archivo joblib

# Crear la aplicación Flask
app = Flask(__name__)

# Definir la ruta de predicción
@app.route('/predictjson', methods=['POST'])
def predictjson():
    data = request.json  # Recibir los datos en formato JSON

    # Convertir los datos a un array numpy en el formato que el modelo espera
    input_data = np.array([
        data['HomePlanet'],
        data['CryoSleep'],
        data['Age'],
        data['RoomService'],
        data['FoodCourt'],
        data['ShoppingMall'],
        data['Spa'],
        data['VRDeck'],
        data['Destination'],
        data['Deck'],
        data['Side'],
        data['Num']
    ])

    # Realizar la predicción utilizando el modelo cargado
    prediction = model.predict(input_data.reshape(1, -1))

    # Devolver la predicción como JSON
    return jsonify({'Prediction': bool(prediction[0])})

# Iniciar el servidor Flask
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)