import React, { useState } from 'react';
import Logo from '../static/logoNav.svg';
import MenuIcon from '@mui/icons-material/Menu';

import { Hamburger } from './navbarMenu';

const Navbar = () => {
  /// State to control the visibility of the mobile menu
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const handleHamburgerClick = () => {
      // Toggle the state that controls the mobile menu visibility
      setIsMenuOpen(prevState => !prevState);
  };

  return (
    <div className="fixed top-0 w-full z-50">
      {/* Navbar */}
      <nav className="bg-navblue text-white p-4">
        <div className="mx-auto flex justify-between items-center">
          <a href='/menu'><img className="transition duration-700 hover:scale-105 object-center ms-10 1/14" src={Logo} alt="Logo" /></a>
          <div className="flex">
            <a href="/visuKits" className="transition duration-500 text-bold text-white hover:text-blue-600 text-xl block p-4 me-5">Layouts</a>
            <a href="/" className="transition duration-500 text-white hover:text-blue-600 text-xl block p-4 me-5">Montar Kit</a>
            <a href="/dashboards" className="transition duration-500 text-white hover:text-blue-600 text-xl block p-4 me-5">Estatísticas</a>
          </div>
          
        </div>
      </nav>
      
    </div>
  );
};

export default Navbar;
