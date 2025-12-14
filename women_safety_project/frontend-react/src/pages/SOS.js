import { useState } from "react";
import axios from "axios";

function SOS() {
  const [phone, setPhone] = useState("");

  const sendSOS = async () => {
    try {
      await axios.post("http://127.0.0.1:5000/sos", {
        name: "User",
        emergency_phone: phone,
        latitude: 13.05,
        longitude: 80.27
      });
      alert("SOS Alert Sent!");
    } catch (error) {
      alert("Failed to send SOS");
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>SOS Emergency Alert</h2>

      <input
        type="text"
        placeholder="Enter Emergency Phone Number"
        value={phone}
        onChange={(e) => setPhone(e.target.value)}
      />

      <button onClick={sendSOS} style={{ marginLeft: 10 }}>
        Send SOS
      </button>
    </div>
  );
}

export default SOS;
