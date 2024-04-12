import { useEffect, useState } from "react";
import { itemKit } from "../interfaces/interfaces";
interface CardItemProps {
    position: number
    onSelectItem: (item: number) => void | null;
    num: number | null
    kitItems: itemKit[] | null
    text: string | undefined
    quantity: number | null
}

const CardItem: React.FC<CardItemProps> = ({ position, onSelectItem, num, kitItems, text, quantity }) => {
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

    useEffect(() => {
        const foundItem = kitItems?.find(item => item.position === position);
        if (foundItem) {
            setBackgroundStyle("bg-violet-600 text-white shadow");
        }
        if (!foundItem) {
            setBackgroundStyle("bg-white hover:text-violet-600 text text-slate-900");
        }
    }, [kitItems])

    return (
        <div>
            <div className={`${backgroundStyle} rounded-lg border ${borderStyle} flex flex-col justify-center shadow w-52  h-52 items-center `} onClick={() => onSelectItem(position)}>
                {text && (
                        <p className="text-xl text-center black">
                            {text}
                        </p>
                )}
                {quantity && (
                    <p className="text-xl text-center black">
                        {String(quantity)}
                    </p>
                )}
            </div>
        </div>
    );
};

export default CardItem