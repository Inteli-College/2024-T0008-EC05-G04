import React from 'react';

interface CardItemProps{
    number: number
}

const CardItem: React.FC<CardItemProps>  = ({number}) => {
    
    function clickItem(){
        

    }
    return(
        <div>
            <div className="bg-white rounded-lg border border-black shadow w-52 h-52 flex items-center justify-center transition duration-500  hover:text-violet-600" onClick={clickItem}>
                    <p className="text-[22px] black">
                        item {number}
                    </p>
            </div>
        </div>
    );
};

export default CardItem