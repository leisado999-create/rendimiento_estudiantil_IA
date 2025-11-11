from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("modelo.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    X_new = np.array([[data['horas_estudio'], data['asistencia'], data['participacion']]])
    prediction = model.predict(X_new)
    return jsonify({"promedio_predicho": round(prediction[0], 2)})

if __name__ == '__main__':
    app.run(port=5000)
