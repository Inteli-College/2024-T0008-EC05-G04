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

export interface ResponseKitCreated{
    message: string
    kit: {
        id: number
        name: string
    }    
}