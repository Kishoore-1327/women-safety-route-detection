from utils.route import get_route_points
from utils.risk_score import calculate_risk

def evaluate_route_risk(start_lat, start_lng, end_lat, end_lng, crime_df):
    """
    Computes risk score along full route.
    Returns (average risk score, category, hotspot list)
    """

    points = get_route_points(start_lat, start_lng, end_lat, end_lng)

    if not points:
        return None, None, []

    risk_scores = []
    hotspots = []

    for (lat, lng) in points[::10]:  # Check every 10th point to reduce load
        score = calculate_risk(lat, lng, crime_df)

        if score > 4:
            hotspots.append({"lat": lat, "lng": lng, "score": score})

        risk_scores.append(score)

    # Average score
    if len(risk_scores) == 0:
        avg_score = 0
    else:
        avg_score = sum(risk_scores) / len(risk_scores)

    # Categorize route
    if avg_score < 2:
        category = "Safe Route"
    elif avg_score < 4:
        category = "Moderate Risk Route"
    else:
        category = "High Risk Route"

    return round(avg_score, 2), category, hotspots

def generate_risk_explanation(hotspots):
    if not hotspots:
        return {
            "reason": "No reported crimes near this route",
            "most_frequent_crime": None,
            "count": 0
        }

    crime_counts = {}
    for h in hotspots:
        crime = h["crime_type"]
        crime_counts[crime] = crime_counts.get(crime, 0) + 1

    most_common = max(crime_counts, key=crime_counts.get)

    return {
        "reason": f"{len(hotspots)} crime incidents found near the route",
        "most_frequent_crime": most_common,
        "count": len(hotspots)
    }
