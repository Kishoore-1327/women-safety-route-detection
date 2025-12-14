import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import RouteSafety from "./pages/RouteSafety";
import SOS from "./pages/SOS";

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/route-safety" element={<RouteSafety />} />
        <Route path="/sos" element={<SOS />} />
      </Routes>
    </Router>
  );
}

export default App;
