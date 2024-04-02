import React from 'react';

interface ButtonMedioProps{
    title: string
    props:string
    onChangeValue: () => void | null; 
}

const ButtonMedio: React.FC<ButtonMedioProps>  = ({title, props,onChangeValue}) => {
    return(
        <div>
           <div>
           <button className={`${props} rounded-lg h-10 text-white`} onClick={onChangeValue}>{title}</button>
           </div>
        </div>
    );
};

export default ButtonMedio