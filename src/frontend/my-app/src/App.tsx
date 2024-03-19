import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Login from './pages/login';
import Menu from './pages/menuFunc';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login/>} />
        <Route path="/menu" element={<Menu />} />
        // Add more routes as needed
      </Routes>
    </Router>
  );
}

export default App;