
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
