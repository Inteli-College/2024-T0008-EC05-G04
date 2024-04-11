import React from 'react';
import { useNavigate } from 'react-router-dom'; // Import useNavigate
import Navbar from '../components/navbar';
import BarChart from '../components/bar-chart-2'
import PieChart from '../components/pie-chart';
import BarChart2 from '../components/bar-chart-kits';



interface ContentBlockProps {
  children: React.ReactNode;
}

const ContentBlock: React.FC<ContentBlockProps> = ({ children }) => {
  return (
    <div className="flex justify-center items-center p-6 bg-gray-200 rounded shadow min-h-full">
      <div className="w-full">
        {children}
      </div>
    </div>
  );
};

const Dashboards: React.FC = () => {
  const navigate = useNavigate(); // Initialize the navigate function
  return (
    
    <div className="flex flex-col h-screen overflow-y-scroll no-scrollbar">
      <div className="flex-grow bg-gray-100 pt-28">
        <Navbar />
        <div className="flex-grow container mx-auto px-4 flex flex-col justify-center">
          <div className="text-center my-6">
            <h1 className="text-3xl my-6">Estatísticas</h1>
            <div className="flex justify-center gap-44 my-20">
              <button onClick={() => navigate('/tables')} className=" transition duration-500 hover:bg-buttongrey text-black text-2xl text-opacity-50 py-2 px-4 rounded-3xl">
                Tabelas
              </button>
              <button className="transition duration-500 hover:bg-buttongrey text-black text-2xl py-2 px-4 rounded-3xl">
                Dashboards
              </button>
            </div>
          </div>
          <div className="grid grid-flow-row-dense grid-cols-2 md:grid-cols-2 gap-10 mb-20">
            <div className='col-span-1 row-span-1'>
              <ContentBlock>
                {<BarChart2 />}
              </ContentBlock>
            </div>
            <div className='col-span-1 row-span-2'>
              <ContentBlock>
                {<PieChart />}
              </ContentBlock>
            </div>
            <div className='col-span-1 row-span-1'>
              <ContentBlock>
                {<BarChart />}
              </ContentBlock>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboards;