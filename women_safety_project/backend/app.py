from flask import Flask, request, jsonify
from flask_cors import CORS

# ---------------------------------------
# IMPORTS
# ---------------------------------------

# ML Model
from model import predict_route_safety

# Preprocessing + Geocoding
from utils.preprocess import geocode_address, load_crime_data

# Risk calculation
from utils.risk_score import calculate_risk

# Route safety logic
from utils.route_risk import evaluate_route_risk, generate_risk_explanation

# SMS System
from utils.sms import send_sms_alert


# ---------------------------------------
# INITIALIZE FLASK APP
# ---------------------------------------
app = Flask(__name__)
CORS(app)


# ---------------------------------------
# 1️⃣ HOME ROUTE
# ---------------------------------------
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Women Safety API Running"})


# ---------------------------------------
# 2️⃣ BASIC ML PREDICTION
# ---------------------------------------
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    result = predict_route_safety(data)

    return jsonify({
        "input": data,
        "risk_level": result["prediction"],
        "score": result["score"]
    })


# ---------------------------------------
# 3️⃣ GEOCODE ADDRESS → LAT/LNG
# ---------------------------------------
@app.route("/geocode", methods=["POST"])
def geocode_api():
    data = request.get_json()

    address = data.get("address")
    if not address:
        return jsonify({"error": "Address is required"}), 400

    lat, lng = geocode_address(address)

    return jsonify({
        "address": address,
        "latitude": lat,
        "longitude": lng
    })


# ---------------------------------------
# 4️⃣ SINGLE POINT RISK CHECK
# ---------------------------------------
@app.route("/risk", methods=["POST"])
def risk_api():
    data = request.get_json()
    lat = data.get("latitude")
    lng = data.get("longitude")

    df = load_crime_data("data/crime_data.csv")
    score = calculate_risk(lat, lng, df)

    if score < 2:
        level = "Safe"
    elif score < 4:
        level = "Moderate"
    else:
        level = "High Risk"

    return jsonify({
        "latitude": lat,
        "longitude": lng,
        "risk_score": score,
        "risk_level": level
    })


# ---------------------------------------
# 5️⃣ ROUTE SAFETY API (WITH EXPLANATION)
# ---------------------------------------
@app.route("/route_safety", methods=["POST"])
def route_safety():
    data = request.get_json()

    source = data.get("source")
    destination = data.get("destination")

    # Convert addresses → coordinates
    s_lat, s_lng = geocode_address(source)
    d_lat, d_lng = geocode_address(destination)

    if s_lat is None or s_lng is None or d_lat is None or d_lng is None:
        return jsonify({"error": "Could not geocode locations"}), 400

    # Load crime data
    df = load_crime_data("data/crime_data.csv")

    # Evaluate route risk
    avg_score, category, raw_hotspots = evaluate_route_risk(
        s_lat, s_lng, d_lat, d_lng, df
    )

    # Prepare hotspots for frontend
    hotspots = []
    for h in raw_hotspots:
        hotspots.append({
            "lat": float(h["latitude"]),
            "lng": float(h["longitude"]),
            "crime_type": h["crime_type"],
            "severity": int(h["severity"])
        })

    # 🔹 NEW: Generate explanation
    explanation = generate_risk_explanation(hotspots)

    return jsonify({
        "source": {
            "label": source,
            "lat": float(s_lat),
            "lng": float(s_lng)
        },
        "destination": {
            "label": destination,
            "lat": float(d_lat),
            "lng": float(d_lng)
        },
        "route_risk_score": float(avg_score),
        "category": category,
        "hotspots": hotspots,
        "explanation": explanation
    })


# ---------------------------------------
# 6️⃣ SOS API
# ---------------------------------------
@app.route("/sos", methods=["POST"])
def sos_alert():
    data = request.get_json()

    user_name = data.get("name", "User")
    emergency_phone = data.get("emergency_phone")
    lat = data.get("latitude")
    lng = data.get("longitude")

    if not emergency_phone:
        return jsonify({"error": "Emergency phone number is required"}), 400

    message = (
        f"⚠️ EMERGENCY ALERT!\n"
        f"{user_name} may be in danger.\n"
        f"Location: https://maps.google.com/?q={lat},{lng}\n"
        f"Please contact them immediately."
    )

    sms_response = send_sms_alert(emergency_phone, message)

    return jsonify({
        "status": "SOS Sent",
        "sent_to": emergency_phone,
        "response": sms_response
    })


# ---------------------------------------
# RUN APP
# ---------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
