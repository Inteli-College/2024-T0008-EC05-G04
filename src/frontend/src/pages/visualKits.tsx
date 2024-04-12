import React, {useState} from 'react';
import { useNavigate } from 'react-router-dom'; // Import useNavigate
import Navbar from '../components/navbar';
import ButtonMedio from "../components/button";
import Placeholder from '../static/logoS.svg';
import useFetch from '../hooks/useFetch';
import { Kit } from '../interfaces/interfaces';
import CardItem from '../components/cardItem';

// import { useState } from 'react';

const VisuPage: React.FC = () => {
    const navigate = useNavigate(); // Initialize the navigate function
  
    const kits = useFetch<Kit[]>('http://localhost:8000/api/kit');
    // Added a 'path' property to each card object
    
  const [modalOpen, setModalOpen] = useState(false);
  const [currentCard, setCurrentCard] = useState<Kit>();

  const handleCardClick = (kitSelected: Kit) => {
    const sortedItems = [...kitSelected.itens].sort((a, b) => a.item_position - b.item_position);
    setCurrentCard({ ...kitSelected, itens: sortedItems });
    setModalOpen(true);
  };

  const closeModal = () => {
    setModalOpen(false);
  };

  function navigateLayout(){
    navigate('/cadastroKit')
  };

  return (
    <div className="flex flex-col h-screen overflow-y-scroll no-scrollbar">
      <div className="flex-grow bg-gray-100 pt-20">
        <Navbar />
        <div className="max-w-6xl mx-auto py-20">
            <div className="flex justify-end">
                <ButtonMedio title="Adicionar layout" props="transition duration-700 hover:scale-105 bg-blue-900 font-semibold w-40 mb-8" onChangeValue={navigateLayout} />
            </div>
          <div className="grid grid-cols-2 md:grid-cols-2 lg:grid-cols-3 gap-10">
            {kits?.map((kit, index) => (
              <div key={index} onClick={() => handleCardClick(kit)} className="transition duration-700 hover:scale-105 border rounded-lg shadow-lg p-12 flex flex-col items-center bg-white cursor-pointer">
                <h2 className="mt-2 font-bold text-lg">{kit.name}</h2>
                <p className='text-base'>Kit id: {kit.id}</p>
              </div>
            ))}
          </div>
        </div>
      </div>
      {modalOpen && (
        <div className="fixed top-0 left-0 w-full h-full bg-black bg-opacity-50 flex justify-center items-center z-50">
          <div className="bg-white p-8 rounded-lg shadow-lg max-w-5xl">
            <h2 className="text-xl font-bold mb-4">{currentCard?.name} </h2>
            <div className="grid grid-cols-4 gap-4">
              {currentCard?.itens.map((item, index: number) => (
                <CardItem text={item?.item_name} position={index} onSelectItem={() => { }} num={null} quantity={item?.quantity} kitItems={[]} />
              ))}
            </div>
            <button className="mt-4 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600" onClick={closeModal}>Fechar</button>
          </div>
        </div>
      )}
    </div>
  );
};

export default VisuPage;