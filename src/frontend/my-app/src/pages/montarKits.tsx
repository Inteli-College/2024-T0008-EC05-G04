import React, { useState } from 'react';
import Navbar from '../components/navbar';
import SearchKit from '../components/searchkits';
import SearchRobot from '../components/searchrobot';

const MontarKits: React.FC = () => {
  const items = ['Item', 'Item', 'Item', 'Item', 'Item', 'Item', 'Item', 'Item'];
  
  const [kitId, setKitId] = useState<number | null>(null);
  const [robotId, setRobotId] = useState<number | null>(null);  

  const itemStyle = {
    width: '240px',
    height: '240px',
    borderColor: '#1D375E'
  };

  // Assuming 'endpoint' is your target URL
  const postEndpoint = 'http://localhost:8000/api/kit-order';

  const handleConfirm = async () => {
    if (!robotId || !kitId) {
      alert('Please select both a robot and a kit.');
      return;
    }

    try {
      const response = await fetch(postEndpoint, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ robot_id: robotId, kit_id: kitId }),
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data = await response.json();
      console.log(data); // Process your response here
      alert('Success!');
    } catch (error) {
      console.error('Error:', error);
      alert('An error occurred, please try again.');
    }
  };

  return (
    <div>
      <Navbar />
      <div className="flex flex-col h-screen pt-32">
        {/* Pass setKitId and setRobotId as props to be called with the selected IDs */}
        <SearchKit onSelectKit={setKitId} />
        <div className="grid grid-cols-4 gap-2 p-4 mt-4 mx-auto">
          {items.map((item, index) => (
            <div key={index} className="border-4 rounded-lg flex justify-center items-center" style={itemStyle}>
              {item}
            </div>
          ))}
        </div>
        <SearchRobot onSelectRobot={setRobotId} />
        <div className="bg-white p-4 flex justify-center">
          <div>
            <button
              className="bg-[#1D375E] hover:bg-blue-700 text-white font-bold py-2 px-16 rounded mr-4"
              onMouseEnter={(e) => e.currentTarget.style.backgroundColor = '#B6D1E9'}
              onMouseLeave={(e) => e.currentTarget.style.backgroundColor = '#1D375E'}
              onClick={handleConfirm}>
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
