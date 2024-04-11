import * as React from 'react';
import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';
import { Label } from '@mui/icons-material';
import { Item, Robot, Kit } from '../interfaces/interfaces';

interface Props {
  items: Item[] | Robot[] | Kit | null;
  text: string;
  label: string;
  size: number;
  onChangeValue: (id: number) => void; 
}

const autocomplete: React.FC<Props> = ({ items, text, label ,size,onChangeValue }) => {
    let combinedOptions: (Item | Robot | Kit)[] = [];
    if (items) {
      if ((items as Item[]).length > 0) {
        combinedOptions = items as Item[];
      } else if ((items as Robot[]).length > 0) {
        combinedOptions = items as Robot[];
      }  else if ((items as Robot[]).length > 0) {
        combinedOptions = items as Robot[];
      }
    }
    return (
      <div className='flex items-center mb-4 ml-6 mr-6'>
        <div className='mr-12'>
            <p className= "font-medium text-xl" >{text}</p> 
        </div> 
        <Autocomplete
          disablePortal
          id="combo-box-demo"
          options={combinedOptions|| []}
          getOptionLabel={(option: Item | Robot | Kit) => option.name}
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
              label= {label}
              className=" text-base"
            />
          )}
        />
    </div>
  );
}
export default autocomplete