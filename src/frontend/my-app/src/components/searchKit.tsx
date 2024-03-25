import * as React from 'react';
import TextField from '@mui/material/TextField';
import Stack from '@mui/material/Stack';
import Autocomplete from '@mui/material/Autocomplete';

export default function RobotSelection() {
  return (
    <div className='flex justify-center my-2'>    
      <Autocomplete
        disablePortal
        id="combo-box-demo"
        options={mock_robot}
        renderInput={(params) => <TextField {...params} label="Selecione o robô" />}
        className='size-1/4'
      />
    </div>

  );
}
const mock_robot = ["Robot_1","Robot_2","Mock_Robot"]