import CardItem from "../components/cardItem";
import InputCadastroKits from "../components/inputCadastroKits";
import ButtonMedio from "../components/button";

const CadastroKit: React.FC = () =>{
    return (
        <>
        <div className="flex justify-center">
            <h1 className="font-bold text-[36px] mb-5">Cadastrar Layout</h1>
        </div>
        <div className="flex flex-col items-center">
            <div className="w-full flex flex-col items-center">
                <InputCadastroKits props="w-[760px]" text="Nome do Kit" label="Digite o nome do kit"/>
                <div className="grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-4 mt-5">
                    <CardItem title="Item 1"/>
                    <CardItem title="Item 2"/>
                    <CardItem title="Item 3"/>
                    <CardItem title="Item 4"/>
                    <CardItem title="Item 5"/>
                    <CardItem title="Item 6"/>
                    <CardItem title="Item 7"/>
                    <CardItem title="Item 8"/>  
                </div>
            <div className="mt-8 flex gap-24">
                <InputCadastroKits props="w-72"text="Item" label="Digite o item a ser adicionado"/>
                <InputCadastroKits props="w-72"text="Quantidade" label="Digite a quantidade desse item"/>
            </div>
            <div className="flex gap-40 mb-6">
                <ButtonMedio title="Salvar" props="bg-blue-900 w-28"/>
                <ButtonMedio title="Cancelar" props="bg-red-500 w-36"/>
            </div>
            </div>
        </div>
        </>
    );
};

export default CadastroKit;
