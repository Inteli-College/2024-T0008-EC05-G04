import React from 'react';

const MainPage: React.FC = () => {
  const cardData = [
    {
      title: 'Visualizar Kits',
      content: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit...',
    },
    {
      title: 'Criar Kit',
      content: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit...',
    },
    {
      title: 'Estatísticas',
      content: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit...',
    },
  ];

  return (
    <div className="flex flex-col h-screen">
      {/* Navbar */}
      <nav className="bg-gray-800 text-white p-4">
        <div className="max-w-6xl mx-auto flex justify-between">
          <div className="font-bold text-xl">4UI</div>
          <div className="hidden md:flex space-x-4">
            {/* Navigation Links */}
            {/* Add <a> tags for navigation links as needed */}
          </div>
          <div className="md:hidden">
            {/* Hamburger menu icon */}
            {/* Implement toggle functionality to show/hide a menu */}
          </div>
        </div>
      </nav>

      {/* Main Content */}
      <div className="flex-grow bg-gray-100">
        <div className="max-w-6xl mx-auto py-8">
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {cardData.map((card, index) => (
              <div key={index} className="border rounded-lg shadow-lg p-4 bg-white">
                <div className="aspect-w-1 aspect-h-1 bg-gray-300 rounded-t-lg overflow-hidden">
                  {/* Image placeholder */}
                </div>
                <h2 className="mt-2 font-bold text-lg">{card.title}</h2>
                <p>{card.content}</p>
                {/* Add buttons or other interactive elements here */}
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default MainPage;
