import { useEffect, useState } from "react";


interface itemKit {
    kit_id: number
    position: number
    item_id: number
    quantity: number
}
interface CardItemProps{
    item: number
    onSelectItem: (item: number) => void;
    num: number
    kitItems: itemKit[]
}

const CardItem: React.FC<CardItemProps>  = ({item,onSelectItem, num, kitItems}) => {
    const [borderStyle, setBorderStyle] = useState<string>("");
    const [backgroundStyle, setBackgroundStyle] = useState<string>("bg-white");
    useEffect(() => {
        if (num === item) {
            // Change the border style if num equals item
            setBorderStyle("border-violet-600 border-2"); // You can set any other border style here
        } else {
            // Reset the border style
            setBorderStyle("");
        }
    }, [num])

    useEffect(() =>{
        kitItems.map(item => {
            if (item.item_id == num){
                setBackgroundStyle("bg-violet-600")
            }
        })
    })
    
    return(
        <div>
            <div className={`${backgroundStyle}  rounded-lg border ${borderStyle} shadow w-52 h-52 flex items-center justify-center transition duration-500  hover:text-violet-600`} onClick={() => onSelectItem(item)}>
                    <p className="text-[22px] black">
                        Posição {item}
                    </p>
            </div>
        </div>
    );
};

export default CardItem