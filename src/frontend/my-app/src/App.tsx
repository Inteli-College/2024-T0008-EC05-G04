import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Login from './pages/login';
import Menu from './pages/menuFunc';
import CadastroKit from './pages/cadastroKit';
import Page from './components/Pages';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login/>} />
        <Route path="/menu" element={<Menu/>} />
        <Route 
          path="/cadastroKit" 
          element={
            <Page>
              <CadastroKit/> 
            </Page>
          }
        />
      </Routes>
    </Router>
  );
}

export default App;