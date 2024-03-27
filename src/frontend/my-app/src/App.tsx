import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Login from './pages/login';
import Menu from './pages/menuFunc';
import VisuKits from './pages/visualKits'
import Dashboards from './pages/dashboards';
import Tables from './pages/tables'

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login/>} />
        <Route path="/menu" element={<Menu />} />
        <Route path="/visuKits" element={<VisuKits />} />
        <Route path="/dashboards" element={<Dashboards />} />
        <Route path="/tables" element={<Tables />} />
      </Routes>
    </Router>
  );
}

export default App;