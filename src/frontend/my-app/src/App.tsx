import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Login from './pages/login';
import Menu from './pages/menuFunc';
import VisuKits from './pages/visualKits'
import MontarKit from './pages/montarKits';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login/>} />
        <Route path="/menu" element={<Menu />} />
        <Route path="/visuKits" element={<VisuKits />} />
        <Route path="/montarKits/*" element={<MontarKit />} />
        // Add more routes as needed
      </Routes>
    </Router>
  );
}

export default App;