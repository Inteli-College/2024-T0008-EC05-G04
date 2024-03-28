import CardItem from "../components/cardItem";
import InputCadastroKits from "../components/inputCadastroKits";
import ButtonMedio from "../components/button";
import Navbar from "../components/navbar";
import {useState} from 'react';
import { number } from "yargs";

const CadastroKit: React.FC = () =>{
    // Define the types that will be used
    interface itemKit {
        kit_id: number
        position: number
        item_id: number
        quantity: number
    }
    interface ResponseKitCreated{
        message: string
        kit: {
            id: number
            name: string
        }    
    }

    const [kitItems,setKitItems] = useState<itemKit[]>([])
    const [num, setNumber] = useState<number>(0)
    const [name,setName] = useState<string>("")
    const [quantity, setQuantity] = useState<number>(0)
    
    function selectionItem(item:number){
        setNumber(item)
    }       

    function addItem(event: React.MouseEvent<HTMLDivElement, MouseEvent>){    
        // Check if an item with the same index already exists
        const itemExists = kitItems.some(item => item.position === num);

        if(kitItems?.length < 8 && itemExists){
            const newItem: itemKit = {
                kit_id: 0,
                position: num,
                item_id: 1,
                quantity: quantity
            };
            setKitItems([...kitItems,newItem])
        }
        else if(kitItems?.length == 8){
            const fetchData = async () => {
                try {
                    const response = await fetch('http://localhost:8000/api/kit',{
                    method:'POST',
                    body: "Quarto-Socorros"});
                    if (!response.ok) {
                        throw new Error(`HTTP error! status: ${response.status}`);
                    }
                    const kitCreated:ResponseKitCreated  = await response.json();
                    const kitCreatedId:number = kitCreated.kit.id;
                   
                } catch (error) {
                  console.error('Failed to fetch data:', error);
                }
            }
        }
    }

    async function processKitItems(kitItems: itemKit[], kitCreatedId: number) {  
    for (const kit of kitItems){
        kit.kit_id = kitCreatedId;
        try {
            const createKit = await fetch('http://localhost:8000/api/kit-position',{
            method:'POST',
            body: JSON.stringify(kit)});
            if (!createKit.ok) {
                throw new Error(`HTTP error! Status: ${createKit.status}`);
            }
            // Handle successful response if needed
            const data = await createKit.json();
            console.log('Response:', data);
        }
        catch (error) {
            console.error('Error:', error);
        }
    })

    return (
        <div className="flex flex-col h-screen overflow-y-scroll no-scrollbar">
            <div className="flex-grow bg-gray-100 pt-32">
                <Navbar />
                <div className="flex justify-center">
                    <h1 className="font-bold text-[28px] mb-0">Cadastrar Layout</h1>
                </div>
                <div className="flex flex-col items-center">
                    <div className="w-full flex flex-col items-center">
                        <InputCadastroKits props="w-[760px]" text="Nome do Kit" label="Digite o nome do kit"/>
                        <div className="grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-4 mt-0">
                            <CardItem item= {1}  onSelectItem={selectionItem} num = {num} />
                            <CardItem item= {2}  onSelectItem={selectionItem} num = {num} />
                            <CardItem item= {3}  onSelectItem={selectionItem} num = {num} />
                            <CardItem item= {4}  onSelectItem={selectionItem} num = {num} />
                            <CardItem item= {5}  onSelectItem={selectionItem} num = {num} />
                            <CardItem item= {6}  onSelectItem={selectionItem} num = {num} />
                            <CardItem item= {7}  onSelectItem={selectionItem} num = {num} />
                            <CardItem item= {8}  onSelectItem={selectionItem} num = {num} />  
                        </div>
                    <div className="mt-4 flex gap-24">
                        <InputCadastroKits props="w-72"text="Nome do Item" label="Digite o nome item a ser adicionado" onChangeFunc={(value) => setName(value)} />
                        <InputCadastroKits props="w-60"text="Quantidade" label="Digite a quantidade do item" onChangeFunc={(value) => setQuantity(parseInt(value))}/>
                    </div>
                    <div className="flex gap-40 mb-4">
                        <div onClick={addItem}>
                            <ButtonMedio title="Salvar" props="bg-blue-900 w-28"/>
                        </div>
                            <ButtonMedio title="Cancelar" props="bg-red-500 w-36"/>
                        </div>
                    </div>
                </div>    
            </div>
        </div>
    );
};

export default CadastroKit;
