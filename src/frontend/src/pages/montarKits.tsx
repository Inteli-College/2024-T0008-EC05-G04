import React, { useState, useEffect } from 'react';
import Navbar from '../components/navbar';
import SearchBar from '../components/searchBar';
import CardItem from '../components/cardItem';
import { Kit } from '../interfaces/interfaces';
import useFetch from '../hooks/useFetch';

const MontarKits: React.FC = () => {
  const items = ['Item', 'Item', 'Item', 'Item', 'Item', 'Item', 'Item', 'Item'];
  const [kit, setKit] = useState<Kit | null>(null);
  const [kitId, setKitId] = useState<number | null>(null);
  const [robotId, setRobotId] = useState<number | null>(null);  

  useEffect(() => {
    const fetchKit = useFetch<Kit>('http://localhost:8000/api/item');
  }, []);

  // Assuming 'endpoint' is your target URL
  const postEndpoint = 'http://localhost:8000/api/kit-order';

  const handleConfirm = async () => {
    if (!robotId || !kit) {
      alert('Please select both a robot and a kit.');
      return;
    }

    try {
      // const response = await fetch(postEndpoint, {
      //   method: 'POST',
      //   headers: {
      //     'Content-Type': 'application/json',
      //   },
      //   body: JSON.stringify({ robot_id: robotId, kit_id: kitId }),
      // });

      // if (!response.ok) {
      //   throw new Error('Network response was not ok');
      // }

      // const data = await response.json();
      // console.log(data); // Process your response here
      // alert('Success!');
    } catch (error) {
      console.error('Error:', error);
      alert('An error occurred, please try again.');
    }
  };

  return (
    <div>
      <Navbar />
      <div className="flex flex-col items-center h-screen pt-32 bg-gray-100">
        {/* Pass setKitId and setRobotId as props to be called with the selected IDs */}
        <SearchBar items = {kit} text = {"Kit a ser montado:"} label = {"Selecione o kit"} size={300}  onChangeValue ={(value) => setKitId(value)} />
        <div className="grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-4 mt-0">
            <CardItem text={String(kit?.items[0].item_name)} position= {1} onSelectItem={()=>{}} num = {null} kitItems = {[]}/>
            <CardItem text={String(kit?.items[1].item_name)} position= {2} onSelectItem={()=>{}} num = {null} kitItems = {[]} />
            <CardItem text={String(kit?.items[2].item_name)} position= {3} onSelectItem={()=>{}} num = {null} kitItems = {[]} />
            <CardItem text={String(kit?.items[3].item_name)} position= {4} onSelectItem={()=>{}} num = {null} kitItems = {[]} />
            <CardItem text={String(kit?.items[4].item_name)} position= {5} onSelectItem={()=>{}} num = {null} kitItems = {[]} />
            <CardItem text={String(kit?.items[5].item_name)} position= {6} onSelectItem={()=>{}} num = {null} kitItems = {[]} />
            <CardItem text={String(kit?.items[6].item_name)} position= {7} onSelectItem={()=>{}} num = {null} kitItems = {[]} />
            <CardItem text={String(kit?.items[7].item_name)} position= {8} onSelectItem={()=>{}} num = {null} kitItems = {[]} />  
        </div>
      
        <div className=" p-4 flex justify-center bg-gray-100">
          <div>
            <button
              className="bg-[#1D375E] hover:bg-blue-700 text-white py-2 px-16 rounded mr-4"
              onMouseEnter={(e) => e.currentTarget.style.backgroundColor = '#B6D1E9'}
              onMouseLeave={(e) => e.currentTarget.style.backgroundColor = '#1D375E'}
              onClick={handleConfirm}>
              Confirmar
            </button>
            <button className="bg-red-600 hover:bg-red-300 text-white py-2 px-16 rounded">
              Cancelar
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default MontarKits;
