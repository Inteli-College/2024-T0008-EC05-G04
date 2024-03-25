import * as React from 'react';
import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';

export default function KitDropdown() {
  return (
    <div className='flex justify-center my-2'>
        <Autocomplete
        disablePortal
        id="combo-box-demo"
        options={kits}
        renderInput={(params) => <TextField {...params} label="Selecione o Kit" />}
        className='size-3/4 '
        />
    </div>
  );
}

const kits = [
    "kit1",
    "kit2"
]
