import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Login from './pages/login';
import Menu from './pages/menuFunc';
import CadastroKit from './pages/cadastroKit';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login/>} />
        <Route path="/menu" element={<Menu/>} />
        <Route path="/cadastroKit" element={<CadastroKit/>} />
      </Routes>
    </Router>
  );
}

export default App;