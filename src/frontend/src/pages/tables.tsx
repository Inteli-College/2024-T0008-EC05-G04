import React from 'react';
import { useNavigate } from 'react-router-dom'; // Import useNavigate
import Table from '../components/table';
import Navbar from '../components/navbar';

const Tables: React.FC = () => {
    const navigate = useNavigate(); // Initialize the navigate function
    return (
        <div className="flex flex-col h-screen">
            <div className="flex-grow bg-gray-100 pt-28">
                <Navbar />
                <div className="flex-grow container mx-auto px-4 flex flex-col justify-center">
                    <div className="text-center my-6">
                        <h1 className="text-3xl my-6">Estatísticas</h1>
                        <div className="flex justify-center gap-44 my-20">
                        <button className=" transition duration-500 hover:bg-buttongrey text-black text-2xl py-2 px-4 rounded-3xl">
                            Tabelas
                        </button>
                        <button onClick={() => navigate('/dashboards')} className="transition duration-500 hover:bg-buttongrey text-black text-2xl text-opacity-50 py-2 px-4 rounded-3xl">
                            Dashboards
                        </button>
                        </div>
                        <Table />
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Tables