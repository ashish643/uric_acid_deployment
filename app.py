import cloudpickle
import numpy as np
from flask import Flask, request, jsonify

# Load the trained model
with open("uric_acid_model.pkl", "rb") as f:
    model = cloudpickle.load(f)

app = Flask(__name__)

@app.route("/")
def home():
    return "Uric Acid Concentration Prediction API is running."

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    input_data = np.array(data["features"]).reshape(1, -1)
    prediction = model.predict(input_data)
    return jsonify({"predicted_concentration": prediction[0]})

if __name__ == "__main__":
    app.run(debug=True)
