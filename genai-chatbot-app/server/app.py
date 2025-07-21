
from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)

openai.api_key = "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"

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
