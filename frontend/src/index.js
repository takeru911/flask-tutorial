import React, {useState, useEffect} from 'react';
import ReactDOM from 'react-dom';
import './index.css';

const API_ENDPOINT = process.env.REACT_APP_API_ENDPOINT


const MyComponent = () => {
    const [value, setValue] = useState(null);

    useEffect( () => {
        async function fetchData() {
            try {
                const response = await fetch(`${API_ENDPOINT}/hello`);
                const responseJson = await response.json();
                setValue(responseJson.value);
            } catch (error) {
                console.log(error);
            }
        }
        fetchData();
    }, [value]);

    return (
        <div>
            value:
            {!value ? "is Loading": value}
        </div>
    )
}

ReactDOM.render(
    <React.StrictMode>
        <MyComponent />
    </React.StrictMode>,
    document.getElementById('root')
);
