import { useEffect, useState } from "react";

interface CardItemProps{
    item: number
    onSelectItem: (item: number) => void;
    num: number
}

const CardItem: React.FC<CardItemProps>  = ({item,onSelectItem, num}) => {
    const [borderStyle, setBorderStyle] = useState<string>("border-black");
    useEffect(() => {
        if (num === item) {
            // Change the border style if num equals item
            setBorderStyle("border-violet-600 border-2"); // You can set any other border style here
        } else {
            // Reset the border style
            setBorderStyle("");
        }
    }, [num])
    return(
        <div>
            <div className={`bg-white rounded-lg border ${borderStyle} shadow w-52 h-52 flex items-center justify-center transition duration-500  hover:text-violet-600`} onClick={() => onSelectItem(item)}>
                    <p className="text-[22px] black">
                        Posição {item}
                    </p>
            </div>
        </div>
    );
};

export default CardItem