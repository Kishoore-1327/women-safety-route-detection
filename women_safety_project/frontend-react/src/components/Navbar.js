import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav style={{
      padding: "15px",
      background: "#1a1a1a",
      color: "white",
      display: "flex",
      gap: "20px"
    }}>
      <Link to="/" style={{ color: "white", textDecoration: "none" }}>Home</Link>
      <Link to="/route-safety" style={{ color: "white", textDecoration: "none" }}>Route Safety</Link>
      <Link to="/sos" style={{ color: "white", textDecoration: "none" }}>SOS Alert</Link>
    </nav>
  );
}

export default Navbar;
