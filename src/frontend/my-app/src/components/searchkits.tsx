

import * as React from 'react';
import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';
import { useState, useEffect } from 'react';

// Define the interface for a kit
interface Kit {
  id: number;
  name: string;
}

export default function KitDropdown() {
  const [kits, setKits] = useState<Kit[]>([]); // Use a state hook for the kits

  // Fetch kits from the endpoint when the component mounts
  useEffect(() => {
    const fetchKits = async () => {
      try {
        const response = await fetch('http://localhost:8000/api/kit');
        const data = await response.json();
        setKits(data); // Assuming the endpoint returns an array of kits
      } catch (error) {
        console.error('Failed to fetch kits:', error);
      }
    };

    fetchKits();
  }, []); // The empty array means this effect runs once after the initial render

  return (
    <div className='flex justify-center my-2'>
        <Autocomplete
        disablePortal
        id="combo-box-demo"
        options={kits}
        getOptionLabel={(option: Kit) => option.name} // Use the name property for the label
        sx={{
          width: 600,
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
        renderInput={(params) => <TextField {...params} label="Selecione o Kit" />}
        className='size-3/4 '
        />
    </div>
  );
}






