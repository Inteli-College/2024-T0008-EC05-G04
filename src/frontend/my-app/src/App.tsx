import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Login from './pages/login';
import Menu from './pages/menuFunc';
import VisuKits from './pages/visualKits';
import MontarKits from './pages/montarKits';
import Dashboards from './pages/dashboards';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login/>} />
        <Route path="/menu" element={<Menu />} />
        <Route path="/visuKits" element={<VisuKits />} />
        <Route path="/montarKits/*" element={<MontarKits />} />
        <Route path="/dashboards" element={<Dashboards />} />
        // Add more routes as needed
      </Routes>
    </Router>
  );
}

export default App;