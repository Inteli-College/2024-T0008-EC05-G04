import CardItem from "../components/cardItem";

export interface Robot {
    id: number;
    name: string;
    route: string;
}

export interface Item {
    id: number;
    name: string;
}

export interface itemKit {
    kit_id: number
    position: number
    item_id: number
    quantity: number
}

export interface Items {
    item_id: number;
    item_name: string;
    item_position: number;
    quantity: number;
}

export interface ResponseKitCreated{
    message: string
    kit: {
        id: number
        name: string
    }    
}

export interface Kit{
    id: number;
    name: string;
    itens: Items[];
}

export interface TextCard{
    name: string;
    quantity: number | null;
}