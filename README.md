# Uric Acid Concentration Predictor

This is a machine learning-based web app to predict uric acid concentration from electrochemical CV data features. Deployed using Gradio + Hugging Face.

### Inputs:
- Peak Current
- Peak Voltage
- Average Current
- Area Under Curve (AUC)

### Output:
- Predicted uric acid concentration (in µM)

### Model:
Gradient Boosting Regressor trained on handcrafted features from cyclic voltammetry data.
