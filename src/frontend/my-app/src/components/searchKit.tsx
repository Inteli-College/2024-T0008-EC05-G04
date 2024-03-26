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
          width: 600, // Defina a largura de acordo com o seu design do Figma
          "& .MuiOutlinedInput-root": {
            "& fieldset": {
              borderColor: "#1D375E", // Cor da borda conforme seu Figma
              borderWidth: '4px', // Grossura da borda
              borderRadius: '8px' // Curvatura do input
            },
            "&:hover fieldset": {
              borderColor: "#1D375E", // Cor da borda em hover
            },
            "&.Mui-focused fieldset": {
              borderColor: "#1D375E", // Cor da borda quando focado
            }
          }
        }}
        renderInput={(params) => (
          <TextField 
            {...params} 
            label="Digite o kit a ser feito" 
            className="bg-white text-base"
          />
        )}
      />
    </div>
  );
}

const mock_robot = ["Robot_1", "Robot_2", "Mock_Robot"];