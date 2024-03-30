import * as React from 'react';
import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';

interface Robot {
    id: number;
    name: string;
    route: string;
  }


interface Item {
id: number;
name: string;
}

interface Props {
  items: Item[] | null | Robot[];
  text: string;
  size: number;
  onChangeValue: (id: number) => void; 
}

const autocomplete: React.FC<Props> = ({ items, text, size,onChangeValue }) => {
    const combinedOptions: (Item | Robot)[] = items ? [...(items as Item[]), ...(items as Robot[])] : [];
    return (
    <div className="flex justify-center my-4">    
      <Autocomplete
        disablePortal
        id="combo-box-demo"
        options={combinedOptions|| []}
        getOptionLabel={(option: Item | Robot) => option.name}
        onChange={(event, value) => onChangeValue(value ? value.id : 0)} // Use the onChange event to call onSelectRobot
        sx={{
          width: size, 
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
            label= {text}
            className="bg-white text-base"
          />
        )}
      />
    </div>
  );
}
export default autocomplete