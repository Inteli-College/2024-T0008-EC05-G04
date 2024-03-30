import React, { useState, useEffect } from 'react';

interface Item {
    name: string;
    id: number;
}

const useGetItems = () => {
    const [items, setItems] = useState<Item[]>([]);

    useEffect(() => {
        const fetchItems = async () => {
            try {
                const response = await fetch('http://localhost:8000/api/api/item');
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                const data = await response.json();
                setItems(data); // Update state with fetched items
            } catch (error) {
                console.error('Failed to fetch data:', error);
            }
        };

        fetchItems();
    }, []);

    return items; // Return the items for rendering or further processing
};

export default useGetItems;
