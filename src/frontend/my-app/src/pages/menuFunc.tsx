import React from 'react';
import { useNavigate } from 'react-router-dom'; // Import useNavigate
import Navbar from '../components/navbar';
import Placeholder from '../static/placeholder.webp';

const MainPage: React.FC = () => {
  const navigate = useNavigate(); // Initialize the navigate function

  // Added a 'path' property to each card object
  const cardData = [
    {
      title: 'Visualizar Kits',
      content: '',
      path: '/visuKits', // Destination path when this card is clicked
    },
    {
      title: 'Criar Kit',
      content: '',
      path: '/',
    },
    {
      title: 'Estatísticas',
      content: '',
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
                <div key={index} onClick={() => handleCardClick(card.path)} className="transition duration-500 scale-[1.20] hover:scale-[1.30] border rounded-lg shadow-lg p-4 bg-white cursor-pointer">
                  <div className="aspect-w-1 aspect-h-1 scale-[1.03] bg-gray-300 rounded-t-lg overflow-hidden">
                    <img className="w-full" src={Placeholder} alt="Logo" />
                  </div>
                  <h2 className="mt-2 text-lg pt-2">{card.title}</h2>
                  <p>{card.content}</p>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
  );
};

export default MainPage;
