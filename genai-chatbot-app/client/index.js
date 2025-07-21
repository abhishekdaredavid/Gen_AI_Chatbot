
import { useState } from 'react';
import axios from 'axios';

export default function Home() {
  const [prompt, setPrompt] = useState('');
  const [response, setResponse] = useState('');

  const handleSubmit = async () => {
    const res = await axios.post('http://localhost:5000/ask', { prompt });
    setResponse(res.data.response);
  };

  return (
    <div style={{ padding: '2rem' }}>
      <h1>GenAI Chatbot</h1>
      <textarea value={prompt} onChange={(e) => setPrompt(e.target.value)} />
      <br />
      <button onClick={handleSubmit}>Send</button>
      <p>Response: {response}</p>
    </div>
  );
}
