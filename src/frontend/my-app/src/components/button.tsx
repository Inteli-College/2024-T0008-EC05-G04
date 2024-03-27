import React from 'react';


interface ButtonMedioProps{
    title: string
    props:string
}

const ButtonMedio: React.FC<ButtonMedioProps>  = ({title, props}) => {
    return(
        <div>
           <div>
           <button className={`${props} rounded-lg h-10 text-white`}>{title}</button>
           </div>
        </div>
    );
};

export default ButtonMedio