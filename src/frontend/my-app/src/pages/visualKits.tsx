import React, {useState} from 'react';
import { useNavigate } from 'react-router-dom'; // Import useNavigate
import Navbar from '../components/navbar';
import Placeholder from '../static/placeholder.webp';
// import { useState } from 'react';

const VisuPage: React.FC = () => {
    const navigate = useNavigate(); // Initialize the navigate function
  
    // Added a 'path' property to each card object
    const cardData = [
      {
        title: 'Kit Primeiros Socorros',
        content:  ``,
        path: '/', // Destination path when this card is clicked
        medicines: ['1 - Paracetamol', 
        '2 - Ibuprofeno',
        '3 - Dipirona',
        '4 - Omeprazol',
        '5 - Ranitidina',
        '6 - Cetirizina',
        '7 - Loratadina',
        '8 - Cloridrato de Fluoxetina']
      },
      {
        title: 'Kit Emergência',
        content:  ``,
        path: '/',
        medicines: ['1 - Sertralina',
          '2 - AAS (ácido acetilsalicílico)',
          '3 - Losartana',
          '4 - Sinvastatina',
          '5 - Metformina',
          '6 - Levotiroxina',
          '7 - Ciprofloxacino',
          '8 - Amoxicilina']
      },
      {
        title: 'Kit Parada Cardíaca',
        content:  ``,
        path: '/',
        medicines: ['1 - Sinvastatina',
          '2 - Metformina',
          '3 - Levotiroxina',
          '4 - Ciprofloxacino',
          '5 - Amoxicilina',
          '6 - Azitromicina',
          '7 - Cloridrato de Ciclobenzaprina',
          '8 - Diclofenaco']
      },
      {
        title: 'Kit Ambulância',
        content:  ``,
        path: '/',
        medicines: ['1 - Lorazepam',
          '2 - Diazepam',
          '3 - Clonazepam',
          '4 - Metoclopramida',
          '5 - Piroxicam',
          '6 - Dipropionato de Betametasona',
          '7 - Fenitoína',
          '8 - Prednisona']
      },
      {
        title: 'Kit Médicos',
        content:  ``,
        path: '/',
        medicines: ['1 - Metronidazol',
          '2 - Tetraciclina',
          '3 - Hidroclorotiazida',
          '4 - Candesartana',
          '5 - Levocetirizina',
          '6 - Rosuvastatina',
          '7 - Lactulose',
          '8 - Bromazepam']
      },
      {
        title: 'Kit Anestesistas',
        content:  ``,
        path: '/',
        medicines: ['1 - Escitalopram',
          '2 - Bupropiona',
          '3 - Duloxetina',
          '4 - Hidroxizina',
          '5 - Piroxicam',
          '6 - Dipropionato de Betametasona',
          '7 - Amoxicilina',
          '8 - Azitromicina']
      },
    ];
    
  const [modalOpen, setModalOpen] = useState(false);
  const [currentCard, setCurrentCard] = useState<any>(null);

  const handleCardClick = (card: any) => {
    setCurrentCard(card);
    setModalOpen(true);
  };

  const closeModal = () => {
    setModalOpen(false);
  };

  return (
    <div className="flex flex-col h-screen overflow-y-scroll no-scrollbar">
      <div className="flex-grow bg-gray-100 pt-28">
        <Navbar />
        <div className="max-w-6xl mx-auto py-20">
          <div className="grid grid-cols-2 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {cardData.map((card, index) => (
              <div key={index} onClick={() => handleCardClick(card)} className="transition duration-700 hover:scale-105 border rounded-lg shadow-lg p-4 bg-white cursor-pointer">
                <div className="aspect-w-1 aspect-h-1 bg-gray-300 rounded-t-lg overflow-hidden">
                  <img className="w-full" src={Placeholder} alt="Logo" />
                </div>
                <h2 className="mt-2 font-bold text-lg">{card.title}</h2>
                <p>{card.content}</p>
              </div>
            ))}
          </div>
        </div>
      </div>
      {modalOpen && (
        <div className="fixed top-0 left-0 w-full h-full bg-black bg-opacity-50 flex justify-center items-center z-50">
          <div className="bg-white p-8 rounded-lg shadow-lg max-w-md">
            <h2 className="text-xl font-bold mb-4">{currentCard?.title} - Medicamentos</h2>
            <div className="grid grid-cols-2 gap-4">
              {currentCard?.medicines.map((medicine: string, index: number) => (
                <div key={index}>{medicine}</div>
              ))}
            </div>
            <div className="mt-4">
              <img src={Placeholder} alt="Medicine" className="w-full" />
            </div>
            <button className="mt-4 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600" onClick={closeModal}>Fechar</button>
          </div>
        </div>
      )}
    </div>
  );
};

export default VisuPage;