import { useState, useEffect } from 'react';

// Define the useFetch hook as a generic function
const useFetch = <T>(url: string): T | null => {
    const [data, setData] = useState<T | null>(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch(url);
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                const jsonData: T = await response.json();
                setData(jsonData);
            } catch (error) {
                console.error('Failed to fetch data:', error);
            }
        };

        fetchData();
    }, [url]);

    return data;
};

export default useFetch;
