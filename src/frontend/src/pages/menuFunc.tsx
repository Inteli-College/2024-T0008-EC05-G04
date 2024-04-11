import React from 'react';
import { useNavigate } from 'react-router-dom'; // Import useNavigate
import Navbar from '../components/navbar';
import Placeholder from '../static/logoS.svg';

const MainPage: React.FC = () => {
  const navigate = useNavigate(); // Initialize the navigate function

  // Added a 'path' property to each card object
  const cardData = [
    {
      title: 'Visualizar Kits',
      content: 'Permite visualizar os kits existentes, assim como criar novos kits.',
      path: '/visuKits', // Destination path when this card is clicked
    },
    {
      title: 'Montar Kit',
      content: 'Funcionalidade para montar kits hospitalares.',
      path: '/montarKits',
    },
    {
      title: 'Estatísticas',
      content: 'Funcionalidade para visualizar estatísticas de kits montados.',
      path: '/dashboards',
    },
  ];

  // Function to navigate to the card's path
  const handleCardClick = (path: string) => {
    navigate(path);
  };

  return (
      <div className="flex flex-col h-screen">
        <div className="flex-grow bg-gray-100 pt-56">
        <Navbar />
          <div className="max-w-6xl mx-auto py-20">
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-24">
              {cardData.map((card, index) => (
                // Added onClick event to each card that calls handleCardClick with the card's path
                <div key={index} onClick={() => handleCardClick(card.path)} className="transition duration-500 scale-[1.20] hover:scale-[1.30] border rounded-lg shadow-lg p-16 flex flex-col items-center bg-white cursor-pointer">
                  <b><h2 className="mt-2 text-xl text pt-2">{card.title}</h2></b>

                  <p className='text-center'>{card.content}</p>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
  );
};

export default MainPage;
