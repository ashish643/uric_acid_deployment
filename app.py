
from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('uric_acid_model.pkl')

@app.route('/')
def home():
    return "Uric Acid Prediction API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    try:
        features = np.array([
            data['peak_current'],
            data['peak_voltage'],
            data['avg_current'],
            data['auc']
        ]).reshape(1, -1)
        prediction = model.predict(features)
        return jsonify({
            "predicted_uric_acid_concentration_µM": round(float(prediction[0]), 2)
        })
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
