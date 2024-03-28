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

export default function RobotSelection() {

  const [robots, setRobots] = useState<Robot[]>([]); // Use a state hook for the kits

  // Fetch kits from the endpoint when the component mounts
  useEffect(() => {
    const fetchRobots = async () => {
      try {
        const response = await fetch('http://localhost:8000/api/kit');
        const data = await response.json();
        setRobots(data); // Assuming the endpoint returns an array of kits
      } catch (error) {
        console.error('Failed to fetch kits:', error);
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
        getOptionLabel={(option: Robot) => option.name} // Use the name property for the label
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

