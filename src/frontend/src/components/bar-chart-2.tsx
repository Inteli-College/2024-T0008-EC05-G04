import React, { useEffect, useState } from 'react';
import { Bar } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from 'chart.js';

// Register Chart.js components
ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

interface Kit {
  robot_name: string;
}

// Define a type for the chart data state
interface ChartDataState {
  labels: string[];
  datasets: [{
    label: string;
    data: number[];
    backgroundColor: string;
    borderColor: string;
    borderWidth: number;
  }];
}

const BarGraph: React.FC = () => {
  const [chartData, setChartData] = useState<ChartDataState>({
    labels: [],
    datasets: [
      {
        label: 'Quantidade',
        data: [],
        backgroundColor: 'rgba(153, 102, 255, 0.5)',
        borderColor: 'rgba(153, 102, 255, 1)',
        borderWidth: 1,
      },
    ],
  });

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://localhost:8000/api/kit-order');
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const kits: Kit[] = await response.json();

        // Count occurrences of each name
        const nameCounts = kits.reduce((acc, { robot_name }) => {
          acc[robot_name] = (acc[robot_name] || 0) + 1;
          return acc;
        }, {} as Record<string, number>);

        const labels = Object.keys(nameCounts);
        const data = Object.values(nameCounts);

        // Directly use the structured data in setState
        setChartData({
          labels,
          datasets: [
            { ...chartData.datasets[0], data },
          ],
        });
      } catch (error) {
        console.error('Failed to fetch data:', error);
      }
    };

    fetchData();
  }, []);

  const options = {
    scales: {
      y: {
        beginAtZero: true,
      },
    },
    plugins: {
      title: {
        display: true,
        text: 'Ocorrências de cada Robô',
        font: {
          size: 20
        },
        color: '#333'
      }
    },
  };

  return (
    <div>
      <Bar data={chartData} options={options} />
    </div>
  );
};

export default BarGraph;