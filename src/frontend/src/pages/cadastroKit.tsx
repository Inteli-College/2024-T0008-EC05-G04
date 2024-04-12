import CardItem from "../components/cardItem";
import SearchBar from '../components/searchBar';
import InputCadastroKits from "../components/inputCadastroKits";
import ButtonMedio from "../components/button";
import Navbar from "../components/navbar";
import useFetch from '../hooks/useFetch'
import { useState, useEffect } from 'react';
import { Item, itemKit } from "../interfaces/interfaces";
import { useNavigate } from 'react-router-dom';

const CadastroKit: React.FC = () => {
    const navigate = useNavigate();

    // Define the types that will be used
    const item = useFetch<Item[]>('http://localhost:8000/api/item/');

    const [kitItems, setKitItems] = useState<itemKit[]>([])

    const [num, setNumber] = useState<number>(0)

    const [itemSelected, setItemSelected] = useState<number>(0)

    const [quantity, setQuantity] = useState<number>(0)

    const [name, setName] = useState<string>("")

    function selectionPosition(item: number) {
        setNumber(item)
        const searchBarElement = document.getElementById('combo-box-demo');
        if (searchBarElement) {
            searchBarElement.focus();
        }
    }

    function selectionItem(id: number | null) {
        if (id !== null) {
            setItemSelected(id);
        }
    }

    useEffect(() => {
        if (kitItems?.length == 8) {
            createKit();
        }
    }, [kitItems])

    function addItem() {
        // Check if an item with the same index already exists
        const itemExists = kitItems.some(item => item.position === num);
        try {
            if (kitItems?.length < 8 && !itemExists && quantity > 0) {
                const newItem: itemKit = {
                    kit_id: 0,
                    position: num,
                    item_id: itemSelected,
                    quantity: quantity
                };
                setKitItems([...kitItems, newItem])
            }
            else if (quantity <= 0 || Number.isNaN(quantity)){
                alert("Insira um número no campo quantidade!")
            }
            console.log(quantity);
        }
        catch (error) {
            console.error("Error adding item:", error);
            }
    }


    async function createKit() {
        try {
            const response = await fetch('http://localhost:8000/api/kit/', {
                method: 'POST',
                body: JSON.stringify({ name }),
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const kitCreated = await response.json();
            const kitCreatedId = kitCreated.kit.id;
            createKitPositions(kitCreatedId);
            alert('Kit cadastrado com sucesso!');// Await if createKitPositions is asynchronous
        } catch (error) {
            console.error("Error creating kit:", error);
            alert("Algo deu errado!")
        }
    }

    async function createKitPositions(kitCreatedId: number) {
        for (const kit of kitItems) {
            kit.kit_id = kitCreatedId;
            try {
                const createKit = await fetch('http://localhost:8000/api/kit-position/', {
                    method: 'POST',
                    body: JSON.stringify(kit),
                    headers: {
                        'Content-Type': 'application/json'
                    }
                });
                if (!createKit.ok) {
                    throw new Error(`HTTP error! Status: ${createKit.status}`);
                }
                // Handle successful response if needed
                const data = await createKit.json();
                console.log('Response:', data);
                setKitItems([])
            }
            catch (error) {
                console.error('Error:', error);
            }
        }
    }

    return (
        <div className="flex flex-col h-screen overflow-y-scroll no-scrollbar">
            <div className="flex-grow bg-gray-100 pt-32">
                <Navbar />
                <div className="flex justify-center">
                    <h1 className="font-bold text-[28px] mb-0">Cadastrar Layout</h1>
                </div>
                <div className="flex flex-col items-center">
                    <div className="w-full flex flex-col items-center">
                        <InputCadastroKits props="w-[760px]" text="Nome do Kit" label="Digite o nome do kit" onChangeFunc={(value) => setName(value)} />
                        <div className="grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-4 mt-0">
                            <CardItem quantity={null} text={"Posição 1"} position={1} onSelectItem={selectionPosition} num={num} kitItems={kitItems} />
                            <CardItem quantity={null} text={"Posição 2"} position={2} onSelectItem={selectionPosition} num={num} kitItems={kitItems} />
                            <CardItem quantity={null} text={"Posição 3"} position={3} onSelectItem={selectionPosition} num={num} kitItems={kitItems} />
                            <CardItem quantity={null} text={"Posição 4"} position={4} onSelectItem={selectionPosition} num={num} kitItems={kitItems} />
                            <CardItem quantity={null} text={"Posição 5"} position={5} onSelectItem={selectionPosition} num={num} kitItems={kitItems} />
                            <CardItem quantity={null} text={"Posição 6"} position={6} onSelectItem={selectionPosition} num={num} kitItems={kitItems} />
                            <CardItem quantity={null} text={"Posição 7"} position={7} onSelectItem={selectionPosition} num={num} kitItems={kitItems} />
                            <CardItem quantity={null} text={"Posição 8"} position={8} onSelectItem={selectionPosition} num={num} kitItems={kitItems} />
                        </div>
                        <div className="mt-4 flex gap-24">
                            <SearchBar
                                items={item}
                                text={"Item:"}
                                label={"Selecione o item"}
                                size={300}
                                onChangeValue={(value) => selectionItem(value)} />
                            <InputCadastroKits props="w-60" text="Quantidade" label="Digite a quantidade do item" onChangeFunc={(value) => setQuantity(parseInt(value))} />
                        </div>
                        <div className="flex gap-40 mb-4">
                            <div >
                                {kitItems.length < 7 && (<ButtonMedio title="Adicionar Item" props="bg-blue-900 w-36" onChangeValue={(addItem)} />)}
                                {kitItems.length == 7 && (<ButtonMedio title="Salvar" props="bg-blue-900 w-36" onChangeValue={(addItem)} />)}
                            </div>
                            <ButtonMedio title="Cancelar" props="bg-red-500 w-36" onChangeValue={() => {
                                if (kitItems.length == 0) { navigate("/menu") }
                                else { kitItems?.pop(); }
                            }} />
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default CadastroKit;
