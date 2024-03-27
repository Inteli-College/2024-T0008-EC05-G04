import CardItem from "../components/cardItem";
import InputCadastroKits from "../components/inputCadastroKits";
import ButtonMedio from "../components/button";

const CadastroKit: React.FC = () =>{
    return (
        <>
        <div className="flex justify-center">
            <h1 className="font-bold text-[28px] mb-0">Cadastrar Layout</h1>
        </div>
        <div className="flex flex-col items-center">
            <div className="w-full flex flex-col items-center">
                <InputCadastroKits props="w-[760px]" text="Nome do Kit" label="Digite o nome do kit"/>
                <div className="grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-4 mt-0">
                    <CardItem number= {1} />
                    <CardItem number= {2}/>
                    <CardItem number= {3}/>
                    <CardItem number= {4}/>
                    <CardItem number= {5}/>
                    <CardItem number= {6}/>
                    <CardItem number= {7}/>
                    <CardItem number= {8}/>  
                </div>
            <div className="mt-4 flex gap-24">
                <InputCadastroKits props="w-72"text="Item" label="Digite o item a ser adicionado"/>
                <InputCadastroKits props="w-72"text="Quantidade" label="Digite a quantidade desse item"/>
            </div>
            <div className="flex gap-40 mb-4">
                <ButtonMedio title="Salvar" props="bg-blue-900 w-28"/>
                <ButtonMedio title="Cancelar" props="bg-red-500 w-36"/>
            </div>
            </div>
        </div>
        </>
    );
};

export default CadastroKit;
