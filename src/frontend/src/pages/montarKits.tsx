import React, { useState, useEffect } from 'react';
import Navbar from '../components/navbar';
import SearchBar from '../components/searchBar';
import CardItem from '../components/cardItem';
import { TextCard, Kit, Robot } from '../interfaces/interfaces';
import useFetch from '../hooks/useFetch';
import { useNavigate } from 'react-router-dom';

const MontarKits: React.FC = () => {
  const navigate = useNavigate();
  const kit = useFetch<Kit[]>('http://localhost:8000/api/kit/');
  const robots = useFetch<Robot[]>('http://localhost:8000/api/robot/');
  const [selectedKit, setSelectedKit] = useState<Kit | null>(null);
  const [selectedKitOrdered, setSelectedKitOrdered] = useState<Kit | null>(null);
  const [selectedRobot, setSelectedRobot] = useState<number | null>(null);
  const [itensArray, setItensArray] = useState<TextCard[]>([]); // This should be an array of items, not a function

  // Assuming 'endpoint' is your target URL
  const postEndpoint = 'http://localhost:8000/api/kit-order/';

  function getSelectedKit(value: number) {
    if (value) {
      kit?.map((kit) => {
        if (kit.id === value) {
          setSelectedKit(kit);
        }
      })
    }
    else { setSelectedKit(null) }
  }

  const handleConfirm = async () => {
    if (!selectedRobot || !selectedKit) {
      alert('Selecione um kit e um robô!.');
      return;
    }

    alert('Enviado!')

    try {
      const response = await fetch(postEndpoint, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ robot_id: selectedRobot, kit_id: selectedKit.id, requested_by: 1 }),
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

  useEffect(() => {
    if (selectedKit) {
      const sortedItems = [...selectedKit.itens].sort((a, b) => a.item_position - b.item_position);
      setItensArray(selectedKit.itens?.map((item) => ({ name: item.item_name, quantity: item.quantity })));
      // Process the sorted items here
      setSelectedKitOrdered({ ...selectedKit, itens: sortedItems });
    }

  }, [selectedKit]);

  return (
    <div>
      <Navbar />
      <div className="flex flex-col justify-center items-center h-screen pt-28 bg-gray-100 ">
        <div className='flex'>
          <SearchBar items={kit} text={"Kit a ser montado:"} label={"Selecione o kit"} size={300} onChangeValue={(value) => getSelectedKit(value)} />
          <SearchBar items={robots} text={"Robô:"} label={"Selecione o robô"} size={300} onChangeValue={(value) => setSelectedRobot(value)} />
        </div>
        <div className="grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-4 mt-0 mb-0">
          <CardItem text={itensArray[0]?.name} position={1} onSelectItem={() => { }} num={null} quantity={itensArray[0]?.quantity} kitItems={[]} />
          <CardItem text={itensArray[1]?.name} position={2} onSelectItem={() => { }} num={null} quantity={itensArray[1]?.quantity} kitItems={[]} />
          <CardItem text={itensArray[2]?.name} position={3} onSelectItem={() => { }} num={null} quantity={itensArray[2]?.quantity} kitItems={[]} />
          <CardItem text={itensArray[3]?.name} position={4} onSelectItem={() => { }} num={null} quantity={itensArray[3]?.quantity} kitItems={[]} />
          <CardItem text={itensArray[4]?.name} position={5} onSelectItem={() => { }} num={null} quantity={itensArray[4]?.quantity} kitItems={[]} />
          <CardItem text={itensArray[5]?.name} position={6} onSelectItem={() => { }} num={null} quantity={itensArray[5]?.quantity} kitItems={[]} />
          <CardItem text={itensArray[6]?.name} position={7} onSelectItem={() => { }} num={null} quantity={itensArray[6]?.quantity} kitItems={[]} />
          <CardItem text={itensArray[7]?.name} position={8} onSelectItem={() => { }} num={null} quantity={itensArray[7]?.quantity} kitItems={[]} />
        </div>
        <div className="m-4 flex justify-center bg-gray-100">
          <div>
            <button
              className="bg-[#1D375E] hover:bg-blue-700 text-white py-2 px-16 rounded mr-4"
              onMouseEnter={(e) => e.currentTarget.style.backgroundColor = '#B6D1E9'}
              onMouseLeave={(e) => e.currentTarget.style.backgroundColor = '#1D375E'}
              onClick={handleConfirm}>
              Confirmar
            </button>
            <button className="bg-red-600 hover:bg-red-300 text-white py-2 px-16 rounded" onClick={() => { navigate('/menu') }} >
              Cancelar
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default MontarKits;
