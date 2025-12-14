import requests

def get_route_points(start_lat, start_lng, end_lat, end_lng):
    """
    Fetch route polyline from OSRM public API.
    Returns list of (lat, lng) points.
    """
    url = f"http://router.project-osrm.org/route/v1/driving/{start_lng},{start_lat};{end_lng},{end_lat}?overview=full&geometries=geojson"

    response = requests.get(url)

    if response.status_code != 200:
        print("OSRM error:", response.text)
        return []

    data = response.json()

    # Extract route geometry
    coords = data["routes"][0]["geometry"]["coordinates"]

    # Convert [lng, lat] → [lat, lng]
    route_points = [(lat, lng) for lng, lat in coords]

    return route_points
