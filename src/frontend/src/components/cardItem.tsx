import { useEffect, useState } from "react";
import { itemKit } from "../interfaces/interfaces";
interface CardItemProps{
    position: number
    onSelectItem: (item: number) => void | null;
    num: number | null
    kitItems: itemKit[] | null
    text: string
}

const CardItem: React.FC<CardItemProps>  = ({position,onSelectItem, num, kitItems, text}) => {
    const [borderStyle, setBorderStyle] = useState<string>("");
    const [backgroundStyle, setBackgroundStyle] = useState<string>("bg-white hover:text-violet-600 text text-slate-900");
    useEffect(() => {
        if (num === position) {
            // Change the border style if num equals item
            setBorderStyle("border-violet-600 border-2"); // You can set any other border style here
        } else {
            // Reset the border style
            setBorderStyle("");
        }
    }, [num])

    useEffect(() =>{
        const foundItem = kitItems?.find(item => item.position === position);
        if (foundItem) {
            setBackgroundStyle("bg-violet-600 text-white shadow");
        }
        if (!foundItem){
            setBackgroundStyle("bg-white hover:text-violet-600 text text-slate-900");
        }
    }, [kitItems])
    
    return(
        <div>
            <div className={`${backgroundStyle}  rounded-lg border ${borderStyle} shadow w-52 h-52 flex items-center justify-center transition duration-500 `} onClick={() => onSelectItem(position)}>
                    <p className="text-[22px] black">
                        {text}
                    </p>
            </div>
        </div>
    );
};

export default CardItem