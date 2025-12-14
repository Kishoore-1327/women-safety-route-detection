import joblib
import numpy as np

model = joblib.load("models/model.pkl")

def predict_route_safety(data):
    lat = data.get("latitude")
    lng = data.get("longitude")
    severity = data.get("severity", 3)  # default average severity

    features = np.array([[lat, lng, severity]])

    prediction = model.predict(features)[0]

    risk_map = {
        0: "Safe",
        1: "Moderate",
        2: "High Risk"
    }

    return {
        "prediction": risk_map.get(prediction, "Unknown"),
        "score": float(prediction)
    }
