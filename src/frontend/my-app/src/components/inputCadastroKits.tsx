import React from 'react'
import TextField from '@mui/material/TextField';

interface InputBottomCadastroKitsProps{
    text: string
    label: string
    props: string
}

const InputBottomCadastroKits: React.FC<InputBottomCadastroKitsProps>  = ({text, label, props}) => {
    return(
        <div>
            <div className='flex items-center mb-6 ml-0'>
                <div className='text-[20px]'>
                    <p className= "font-medium text-[20px]" >{text}</p> 
                </div>
                <div className='ml-12 w-1/2'>
                    <TextField id="outlined-basic" label={label} className={`rounded-full ${props}`} />
                </div>
            </div>
        </div>
    );
};

export default InputBottomCadastroKits