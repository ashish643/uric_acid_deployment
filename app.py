import gradio as gr
import joblib
import numpy as np

# Load the trained model
model = joblib.load("uric_acid_model.pkl")

def predict_uric_acid(peak_current, peak_voltage, avg_current, auc):
    features = np.array([[peak_current, peak_voltage, avg_current, auc]])
    prediction = model.predict(features)[0]
    return round(prediction, 2)

iface = gr.Interface(
    fn=predict_uric_acid,
    inputs=[
        gr.Number(label="Peak Current"),
        gr.Number(label="Peak Voltage"),
        gr.Number(label="Average Current"),
        gr.Number(label="Area Under Curve (AUC)")
    ],
    outputs="number",
    title="Uric Acid Concentration Predictor",
    description="Enter electrochemical feature values to predict uric acid concentration (in µM)."
)

iface.launch()
