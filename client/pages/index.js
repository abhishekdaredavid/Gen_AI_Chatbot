
import { useState } from 'react';
import axios from 'axios';

export default function Home() {
  const [prompt, setPrompt] = useState('');
  const [response, setResponse] = useState('');

  const sendPrompt = async () => {
    try {
      const res = await axios.post('http://localhost:5000/ask', { prompt });
      setResponse(res.data.response);
    } catch (error) {
      setResponse('Error fetching response from server.');
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>Gemini Chatbot</h1>
      <textarea
        rows="4"
        cols="60"
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        placeholder="Ask me anything..."
      />
      <br />
      <button onClick={sendPrompt}>Send</button>
      <h3>Response:</h3>
      <p>{response}</p>
    </div>
  );
}
