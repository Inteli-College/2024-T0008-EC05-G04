import React from 'react';
import Navbar from '../components/navbar'; // Assuming Navbar is in the same directory

const PageContent: React.FC = () => {
  const items = ['Item', 'Item', 'Item', 'Item', 'Item', 'Item', 'Item', 'Item'];

  const itemStyle = {
    width: '240px',
    height: '240px',
    borderColor: '#1D375E'
  };

  return (
    <div className="flex flex-col h-screen">
      <Navbar />
      <div className="grid grid-cols-4 gap-2 p-4 mt-10 mx-auto">
        {items.map((item, index) => (
          <div key={index} className="border-4 rounded-lg flex justify-center items-center" style={itemStyle}>
            {item}
          </div>
        ))}
      </div>
      <div className="mt-auto bg-white p-8 flex justify-center">
        <div>
          <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-16 rounded mr-4">
            Confirmar
          </button>
          <button className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-16 rounded">
            Cancelar
          </button>
        </div>
      </div>
    </div>
  );
};

export default PageContent;
