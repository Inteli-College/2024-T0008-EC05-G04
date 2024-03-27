import React from 'react';

interface CardItemProps{
    title: string
}

const CardItem: React.FC<CardItemProps>  = ({title}) => {
    return(
        <div>
            <div className="bg-white rounded-lg border border-black shadow w-52 h-52 flex items-center justify-center">
                <p className="text-[22px] black">
                    {title}
                </p>
            </div>
        </div>
    );
};

export default CardItem