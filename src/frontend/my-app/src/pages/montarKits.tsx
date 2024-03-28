import React from 'react';
import Navbar from '../components/navbar';
import SearchKit from '../components/searchkits';
import SearchRobot from '../components/searchrobot'; 

const MontarKits: React.FC = () => {
  const items = ['Item', 'Item', 'Item', 'Item', 'Item', 'Item', 'Item', 'Item'];

  const itemStyle = {
    width: '240px',
    height: '240px',
    borderColor: '#1D375E'
  };

  return (
    <div>
    <Navbar />
    <div className="flex flex-col h-screen pt-32">
      <SearchKit />
      <div className="grid grid-cols-4 gap-2 p-4 mt-4 mx-auto">
        {items.map((item, index) => (
          <div key={index} className="border-4 rounded-lg flex justify-center items-center" style={itemStyle}>
            {item}
          </div>
        ))}
      </div>
      <SearchRobot />
      <div className="bg-white p-4 flex justify-center">
        <div>
          <button
            className="bg-[#1D375E] hover:bg-blue-700 text-white font-bold py-2 px-16 rounded mr-4"
            onMouseEnter={(e) => e.currentTarget.style.backgroundColor = '#B6D1E9'}
            onMouseLeave={(e) => e.currentTarget.style.backgroundColor = '#1D375E'} >
            Confirmar
          </button>
          <button className="bg-red-600 hover:bg-red-300 text-white font-bold py-2 px-16 rounded">
            Cancelar
          </button>
        </div>
      </div>
    </div>
    </div>
  );
};

export default MontarKits;
