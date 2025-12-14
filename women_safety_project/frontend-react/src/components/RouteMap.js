import React from "react";
import { MapContainer, TileLayer, Marker, Popup, Polyline } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import L from "leaflet";

/* Fix default marker icon issue in Leaflet */
delete L.Icon.Default.prototype._getIconUrl;
L.Icon.Default.mergeOptions({
  iconRetinaUrl:
    "https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon-2x.png",
  iconUrl:
    "https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon.png",
  shadowUrl:
    "https://unpkg.com/leaflet@1.9.4/dist/images/marker-shadow.png",
});

function RouteMap({ source, destination, hotspots = [], category }) {
  if (!source?.lat || !destination?.lat) {
    return <p>Loading map...</p>;
  }

  /* Straight line route (fallback – real roads in STEP 5) */
  const routeLine = [
    [source.lat, source.lng],
    [destination.lat, destination.lng],
  ];

  /* Route color based on safety */
  const getRouteColor = () => {
    if (category === "High Risk") return "red";
    if (category === "Moderate Risk") return "orange";
    return "green";
  };

  return (
    <div style={{ width: "100%" }}>
      {/* MAP */}
      <MapContainer
        center={[source.lat, source.lng]}
        zoom={12}
        style={{ height: "500px", width: "100%" }}
      >
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          attribution="© OpenStreetMap contributors"
        />

        {/* ROUTE LINE */}
        <Polyline
          positions={routeLine}
          color={getRouteColor()}
          weight={5}
        />

        {/* SOURCE MARKER */}
        <Marker position={[source.lat, source.lng]}>
          <Popup>
            <strong>Source</strong>
            <br />
            {source.label}
          </Popup>
        </Marker>

        {/* DESTINATION MARKER */}
        <Marker position={[destination.lat, destination.lng]}>
          <Popup>
            <strong>Destination</strong>
            <br />
            {destination.label}
          </Popup>
        </Marker>

        {/* CRIME HOTSPOTS */}
        {hotspots.map((h, idx) => (
          <Marker key={idx} position={[h.lat, h.lng]}>
            <Popup>
              ⚠ <strong>{h.crime_type}</strong>
              <br />
              Severity: {h.severity}
            </Popup>
          </Marker>
        ))}
      </MapContainer>

      {/* LEGEND (STABLE – NO FLICKER) */}
      <div
        style={{
          marginTop: "10px",
          background: "#fff",
          padding: "10px 14px",
          borderRadius: "8px",
          boxShadow: "0 0 8px rgba(0,0,0,0.3)",
          width: "fit-content",
          fontSize: "14px",
        }}
      >
        <strong>Legend</strong>
        <div>🟢 Safe Route</div>
        <div>🟠 Moderate Risk</div>
        <div>🔴 High Risk</div>
        <div>⚠ Crime Hotspot</div>
      </div>
    </div>
  );
}

export default RouteMap;
