import { useContext, useState } from "react";

interface CardItemProps{
    number: number
    onSelectItem: (item: number) => void;
}

const CardItem: React.FC<CardItemProps>  = ({number,onSelectItem}) => {
    return(
        <div>
            <div className="bg-white rounded-lg border border-black shadow w-52 h-52 flex items-center justify-center transition duration-500  hover:text-violet-600" onClick={() => onSelectItem(number)}>
                    <p className="text-[22px] black">
                        item {number}
                    </p>
            </div>
        </div>
    );
};

export default CardItem