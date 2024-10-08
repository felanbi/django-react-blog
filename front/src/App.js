import { Route, Routes } from "react-router-dom";
import Cookies from "js-cookie";

import Articles from "./pages/Articles";
import Events from "./pages/Events";

import "./App.css";

function App() {
  const jwtToken = Cookies.get('access');

  return (
    <Routes>
      <Route path="/articles" element={<Articles jwtToken={jwtToken} />} />
      <Route path="/events" element={<Events jwtToken={jwtToken} />} />
    </Routes>
  );
}

export default App;
