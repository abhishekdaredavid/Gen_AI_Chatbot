
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

GEMINI_API_KEY = "AIzaSyA_ZjeqD4TnRjAOudYn6TofWAi2KGIhCnA"

@app.route('/ask', methods=['POST'])
def ask():
    prompt = request.json.get('prompt')
    if not prompt:
        return jsonify({'response': 'Prompt is required'}), 400

    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GEMINI_API_KEY}"
        headers = {"Content-Type": "application/json"}
        body = {
            "contents": [{"parts": [{"text": prompt}]}]
        }
        response = requests.post(url, headers=headers, json=body)
        reply = response.json()
        text = reply['candidates'][0]['content']['parts'][0]['text']
        return jsonify({'response': text})
    except Exception as e:
        return jsonify({'response': 'Error: ' + str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
