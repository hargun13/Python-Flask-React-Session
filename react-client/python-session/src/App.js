import React, { useState, useEffect } from 'react';
import './App.css'

const App = () => {
    const [getValueOutput, setGetValueOutput] = useState('');
    const [insertDataOutput, setInsertDataOutput] = useState('');

    const getValue = () => {
        fetch('http://127.0.0.1:5000/get_value')
            .then(response => response.json())
            .then(data => {
                setGetValueOutput(JSON.stringify(data));
            })
            .catch(error => console.error('Error:', error));
    };

    const insertData = () => {
        fetch('http://127.0.0.1:5000/insert_data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
        })
        .then(response => response.json())
        .then(data => {
            setInsertDataOutput(JSON.stringify(data));
        })
        .catch(error => console.error('Error:', error));
    };

    useEffect(() => {
        // You can perform any initial data fetching or setup here
    }, []);

    return (
        <div>
            <h1>Flask MySQL Example</h1>

            <h2>Get Value</h2>
            <button onClick={getValue}>Get Value</button>
            <div id="getValueOutput">{getValueOutput}</div>

            <h2>Insert Data</h2>
            <button onClick={insertData}>Insert Data</button>
            <div id="insertDataOutput">{insertDataOutput}</div>
        </div>
    );
};

export default App;
