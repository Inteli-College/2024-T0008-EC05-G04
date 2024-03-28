import CardItem from "../components/cardItem";
import InputCadastroKits from "../components/inputCadastroKits";
import ButtonMedio from "../components/button";
import {useState} from 'react';

const CadastroKit: React.FC = () =>{
    // Define a type for the chart data state
    interface itemKit {
        name: string
        index: number
        quantity: string;
    }
    const [kitItems,setKitItems] = useState<itemKit[]>()
    const [num, setNumber] = useState<number>(0)
    function selectionItem(item:number){
        setNumber(item)
    }       
    function addItem(event: React.MouseEvent<HTMLDivElement, MouseEvent>){    
        console.log(num);
    }
    return (
        <>
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
                <InputCadastroKits props="w-72"text="Nome do Item" label="Digite o nome item a ser adicionado"/>
                <InputCadastroKits props="w-60"text="Quantidade" label="Digite a quantidade do item"/>
            </div>
            <div className="flex gap-40 mb-4">
                <div onClick={addItem}>
                    <ButtonMedio title="Salvar" props="bg-blue-900 w-28"/>
                </div>
                <ButtonMedio title="Cancelar" props="bg-red-500 w-36"/>
            </div>
            </div>
        </div>
        </>
    );
};

export default CadastroKit;
