import { useState, useEffect } from 'react';

// Define the useFetch hook as a generic function
const useFetch = <T>(url: string): T | null => {
    const [data, setData] = useState<T | null>(null);

    useEffect(() => {
        const fetchData = () => {
            const xhr = new XMLHttpRequest();
            xhr.open('GET', url, false); // Synchronous request
            xhr.setRequestHeader('Content-Type', 'application/json');

            xhr.onreadystatechange = () => {
                if (xhr.readyState === XMLHttpRequest.DONE) {
                    if (xhr.status === 200) {
                        const jsonData: T = JSON.parse(xhr.responseText);
                        setData(jsonData);
                    } else {
                        console.error(`HTTP error! status: ${xhr.status}`);
                    }
                }
            };

            xhr.send();
        };

        fetchData();
    }, [url]);

    return data;
};

export default useFetch;
