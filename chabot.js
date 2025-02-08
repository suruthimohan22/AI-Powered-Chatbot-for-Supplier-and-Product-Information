import React, { useState } from 'react';
import axios from 'axios';

const ChatBox = () => {
    const [query, setQuery] = useState('');
    const [responses, setResponses] = useState([]);

    const handleQuery = async () => {
        const res = await axios.get(`http://localhost:8000/api/products?brand=${query}`);
        setResponses([...responses, { query, response: res.data }]);
        setQuery('');
    };

    return (
        <div>
            <input
                type="text"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                placeholder="Enter your query"
            />
            <button onClick={handleQuery}>Send</button>
            <div>
                {responses.map((res, idx) => (
                    <p key={idx}>
                        <strong>Query:</strong> {res.query} <br />
                        <strong>Response:</strong> {JSON.stringify(res.response)}
                    </p>
                ))}
            </div>
        </div>
    );
};

export default ChatBox;
