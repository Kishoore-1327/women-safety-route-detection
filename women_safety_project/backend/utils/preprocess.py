import pandas as pd
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="women_safety_app")

def load_crime_data(path="data/crime_data.csv"):
    print("DEFAULT PATH USED:", path)
    print("USING FILE:", __file__)
    try:
        df = pd.read_csv(path)
        return df
    except Exception as e:
        print("Error loading crime data:", e)
        return pd.DataFrame()

def clean_crime_data(df):
    df.columns = [c.lower().strip() for c in df.columns]

    if "latitude" in df and "longitude" in df:
        df = df.dropna(subset=["latitude", "longitude"])
        df["latitude"] = pd.to_numeric(df["latitude"], errors="coerce")
        df["longitude"] = pd.to_numeric(df["longitude"], errors="coerce")
        df = df.dropna(subset=["latitude", "longitude"])

    return df

def geocode_address(address):
    """
    Converts a text address (ex: 'Chennai Central') to (lat, lng).
    Returns (None, None) if address is invalid.
    """
    try:
        location = geolocator.geocode(address)
        if location:
            return location.latitude, location.longitude
        return None, None
    except Exception as e:
        print("Geocoding error:", e)
        return None, None
