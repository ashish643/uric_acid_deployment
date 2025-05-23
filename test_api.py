import requests

url = "https://uric-acid-deployment.onrender.com/predict"
data = {
    "peak_current": -0.25,
    "peak_voltage": 0.35,
    "avg_current": -0.12,
    "auc": 0.45
}

response = requests.post(url, json=data)

print("Status:", response.status_code)
print("Prediction:", response.json())
