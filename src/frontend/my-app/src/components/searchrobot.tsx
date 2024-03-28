import * as React from 'react';
import { useState, useEffect } from 'react';
import TextField from '@mui/material/TextField';
import Stack from '@mui/material/Stack';
import Autocomplete from '@mui/material/Autocomplete';

interface Robot {
  id: number;
  name: string;
  route: string;
}

// Add a prop for the selection callback
interface RobotSelectionProps {
  onSelectRobot: (id: number | null) => void; // The callback function type
}

export default function RobotSelection({ onSelectRobot }: RobotSelectionProps) {
  const [robots, setRobots] = useState<Robot[]>([]);

  useEffect(() => {
    const fetchRobots = async () => {
      try {
        const response = await fetch('http://localhost:8000/api/kit');
        const data = await response.json();
        setRobots(data);
      } catch (error) {
        console.error('Failed to fetch robots:', error);
      }
    };

    fetchRobots();
  }, []);

  return (
    <div className="flex justify-center my-4">    
      <Autocomplete
        disablePortal
        id="combo-box-demo"
        options={robots}
        getOptionLabel={(option: Robot) => option.name}
        onChange={(event, value) => onSelectRobot(value ? value.id : null)} // Use the onChange event to call onSelectRobot
        sx={{
          width: 300, 
          "& .MuiOutlinedInput-root": {
            "& fieldset": {
              borderColor: "#1D375E", 
              borderWidth: '2px',
              borderRadius: '8px'
            },
            "&:hover fieldset": {
              borderColor: "#1D375E", 
            },
            "&.Mui-focused fieldset": {
              borderColor: "#1D375E",
            }
          }
        }}
        renderInput={(params) => (
          <TextField 
            {...params} 
            label="Selecione o robô" 
            className="bg-white text-base"
          />
        )}
      />
    </div>
  );
}
