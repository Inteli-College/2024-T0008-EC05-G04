import React from 'react';
import Logo from '../static/logoNav.svg';

const Navbar: React.FC = () => {
  return (
    <div className="fixed top-0 w-full z-50">
      {/* Navbar */}
      <nav className="bg-navblue text-white p-4">
        <div className="mx-auto flex justify-between items-center">
          <img className="transition duration-700 hover:scale-105 object-center ml-10 w-1/14" src={Logo} alt="Logo" />
          <div className="flex">
            <a href="/" className="transition duration-500 text-white hover:scale-110 text-xl block p-4 mr-5">Layouts</a>
            <a href="/" className="transition duration-500 text-white hover:text-violet-600 text-xl block p-4 mr-5">Montar Kit</a>
            <a href="/" className="transition duration-500 text-white hover:text-violet-600 text-xl block p-4 mr-5">Estatísticas</a>
          </div>
        </div>
      </nav>
    </div>
  );
};

export default Navbar;
