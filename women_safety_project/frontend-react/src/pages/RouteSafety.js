import React, { useState } from "react";
import axios from "axios";
import RouteMap from "../components/RouteMap";

function RouteSafety() {
  const [source, setSource] = useState("");
  const [destination, setDestination] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleCheckSafety = async () => {
    if (!source || !destination) {
      alert("Please enter both Source and Destination");
      return;
    }

    setLoading(true);

    try {
      const response = await axios.post(
        "http://127.0.0.1:5000/route_safety",
        {
          source,
          destination,
        }
      );

      setResult(response.data);
    } catch (error) {
      console.error("API Error:", error);
      alert("Failed to fetch route safety!");
    }

    setLoading(false);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>Check Route Safety</h2>

      {/* INPUTS */}
      <div style={{ marginBottom: "10px" }}>
        <label>Source Address:</label>
        <br />
        <input
          type="text"
          value={source}
          onChange={(e) => setSource(e.target.value)}
          style={{ width: "300px", padding: "8px" }}
        />
      </div>

      <div style={{ marginBottom: "10px" }}>
        <label>Destination Address:</label>
        <br />
        <input
          type="text"
          value={destination}
          onChange={(e) => setDestination(e.target.value)}
          style={{ width: "300px", padding: "8px" }}
        />
      </div>

      {/* BUTTON */}
      <button
        onClick={handleCheckSafety}
        style={{
          padding: "10px 20px",
          background: "black",
          color: "white",
          border: "none",
          cursor: "pointer",
        }}
      >
        {loading ? "Checking..." : "Check Safety"}
      </button>

      {/* RESULT */}
      {result && (
        <div
          style={{
            marginTop: "20px",
            padding: "15px",
            border: "1px solid #ccc",
            borderRadius: "8px",
          }}
        >
          <h3>Route Safety Result</h3>

          <p>
            <strong>Source:</strong> {result.source.label}
          </p>
          <p>
            <strong>Destination:</strong> {result.destination.label}
          </p>
          <p>
            <strong>Risk Score:</strong> {result.route_risk_score}
          </p>
          <p>
            <strong>Category:</strong> {result.category}
          </p>

          <h4>Crime Hotspots on Route:</h4>
          {result.hotspots.length === 0 ? (
            <p>No hotspots detected 👍</p>
          ) : (
            <ul>
              {result.hotspots.map((h, index) => (
                <li key={index}>
                  {h.crime_type} | Severity {h.severity}
                </li>
              ))}
            </ul>
          )}

          {/* MAP */}
          <div style={{ marginTop: "20px" }}>
            <RouteMap
              source={result.source}
              destination={result.destination}
              hotspots={result.hotspots}
              category={result.category}
            />
          </div>
        </div>
      )}
    </div>
  );
}

export default RouteSafety;
