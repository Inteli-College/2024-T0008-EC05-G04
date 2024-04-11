import React, { useEffect, useState } from 'react';
import { Pie } from 'react-chartjs-2';
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';

ChartJS.register(ArcElement, Tooltip, Legend);

interface Dataset {
  robot_name: string;
  kit_name: string;
}

interface ChartDataType {
  labels: string[];
  datasets: {
    data: number[];
    backgroundColor: string[];
    borderColor: string;
    borderWidth: number;
  }[];
}

const PieGraph: React.FC = () => {
  const [chartData, setChartData] = useState<ChartDataType>({
    labels: [],
    datasets: [
      {
        data: [],
        backgroundColor: [],
        borderColor: 'white',
        borderWidth: 1,
      },
    ],
  });

  const options = {
    plugins: {
      title: {
        display: true,
        text: 'Quantidade de Kits por tipo',
        font: {
          size: 20
        },
      }
    },
    // Additional options can go here
  }; 

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://localhost:8000/api/kit-order');
        const data: Dataset[] = await response.json();

        const processData = (data: Dataset[]) => {
          const nameCount = data.reduce((acc, item) => {
            acc[item.kit_name] = (acc[item.kit_name] || 0) + 1;
            return acc;
          }, {} as Record<string, number>);

          const chartData: ChartDataType = {
            labels: Object.keys(nameCount),
            datasets: [
              {
                data: Object.values(nameCount),
                backgroundColor: [
                  '#ff6384',
                  '#36a2eb',
                  '#cc65fe',
                  '#ffce56',
                  '#fd6b19', // Add more colors as needed
                ],
                borderColor: 'white',
                borderWidth: 2,
              },
            ],
          };

          setChartData(chartData);
        };

        processData(data);
      } catch (error) {
        console.error('Failed to fetch data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <Pie data={chartData} options={options}/>
    </div>
  );
}

export default PieGraph;

  
