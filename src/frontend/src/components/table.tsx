import React, { useEffect, useState } from 'react';
import { Bar } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';

// Register the chart components
ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

interface Task {
  id: number;
  robot_name: string;
  status: string;
  kit_name: string;
  start_date: string;
  end_date: string;
  requested_by: number;
}

const formatDate = (dateString: string): string => {
  const date = new Date(dateString);
  return `${date.getDate()}/${date.getMonth() + 1}/${date.getFullYear()}`;
};

const TableWithChart: React.FC = () => {
  const [tasks, setTasks] = useState<Task[]>([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://localhost:8000/api/kit-order');
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const data: Task[] = await response.json();
        setTasks(data);
      } catch (error) {
        console.error('Failed to fetch data:', error);
      }
    };

    fetchData();
  }, []);



  return (
    <div className="p-4">
      <div className="overflow-x-auto mt-4">
        <table className="table-auto w-full text-left">
          <thead>
            <tr>
              <th className="px-4 py-2">Kit</th>
              <th className="px-4 py-2">Robot</th>
              <th className="px-4 py-2">Status</th>
              <th className="px-4 py-2">Date</th>
            </tr>
          </thead>
          <tbody>
            {tasks.map((task, index) => (
              <tr key={task.id} className={`${index % 2 === 0 ? 'bg-gray-100' : 'bg-white'}`}>
                <td className="border px-4 py-2">{task.kit_name}</td>
                <td className="border px-4 py-2">{task.robot_name}</td>
                <td className="border px-4 py-2">{task.status}</td>
                <td className="border px-4 py-2">{formatDate(task.start_date)}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default TableWithChart;
