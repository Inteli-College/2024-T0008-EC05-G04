import * as React from 'react';
import TextField from '@mui/material/TextField';
import Stack from '@mui/material/Stack';
import Autocomplete from '@mui/material/Autocomplete';

export default function RobotSelection() {
  return (
    <div className="flex justify-center my-4">    
      <Autocomplete
        disablePortal
        id="combo-box-demo"
        options={mock_robot}
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

const mock_robot = ["Robot_1", "Robot_2", "Mock_Robot"];