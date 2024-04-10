import React from 'react'
import TextField from '@mui/material/TextField';


interface InputBottomCadastroKitsProps{
    text: string
    label: string
    props: string
    onChangeFunc?: (value: string) => void; 
}

const InputBottomCadastroKits: React.FC<InputBottomCadastroKitsProps>  = ({text, label, props, onChangeFunc}) => {
    return(
        <div>
            <div className='flex items-center mb-4 ml-0'>
                <div className=''>
                    <p className= "font-medium text-xl" >{text}</p> 
                </div>
                <div className='ml-12 w-1/2'>
                    <TextField id="outlined-basic" label={label} className={`${props}`} onChange={(event)=>  onChangeFunc && onChangeFunc(event.target.value)}/>
                </div>
            </div>
        </div>
    );
};

export default InputBottomCadastroKits