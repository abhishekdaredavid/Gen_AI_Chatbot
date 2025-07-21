
from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)

openai.api_key = "your-openai-api-key"

@app.route("/ask", methods=["POST"])
def ask():
    prompt = request.json.get("prompt", "")
    if not prompt:
        return jsonify({"response": "No prompt provided"}), 400

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return jsonify({"response": response['choices'][0]['message']['content']})

if __name__ == "__main__":
    app.run(debug=True)
