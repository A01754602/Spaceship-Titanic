# Librerías de Python
from flask import Flask, request, jsonify
import numpy as np
import joblib

# Cargar el modelo entrenado (clasificador de votación en este caso)
model = joblib.load('voting_model.joblib')  # Guarda tu modelo de votación como archivo joblib

# Crear la aplicación Flask
app = Flask(__name__)

# Definir la ruta de predicción
@app.route('/predictjson', methods=['POST'])
def predictjson():
    # Procesar los datos de entrada
    data = request.json
    
    # Extraer las características del pasajero
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

    # Realizar la predicción con el modelo cargado
    result = model.predict(input_data.reshape(1, -1))

    # Enviar la respuesta como un JSON
    return jsonify({'Prediction': bool(result[0])})

# Iniciar el servidor Flask
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)