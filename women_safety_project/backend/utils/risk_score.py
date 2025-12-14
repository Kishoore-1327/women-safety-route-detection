import pandas as pd
from utils.distance import haversine

def calculate_risk(lat, lng, crime_df, radius_km=1.0):
    """
    Finds crimes within given radius and computes a weighted risk score.
    """
    nearby_crimes = []

    for _, row in crime_df.iterrows():
        dist = haversine(lat, lng, row["latitude"], row["longitude"])
        if dist <= radius_km:
            nearby_crimes.append(row)

    if not nearby_crimes:
        return 0  # No crimes nearby → Safe
    
    crime_df = pd.DataFrame(nearby_crimes)

    # Weighted risk (higher severity → higher weight)
    severity_score = crime_df["severity"].mean()

    # Density weight
    crime_density = len(crime_df)

    # Final risk score (tuneable)
    risk_score = (severity_score * 0.6) + (crime_density * 0.4)

    return round(risk_score, 2)
