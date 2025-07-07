import os
from dotenv import load_dotenv
import requests
import json
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

print("OPENROUTER_API_KEY:", OPENROUTER_API_KEY)

@app.route("/", methods=["GET"])
def index():
    return send_from_directory('.', 'index.html')

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    payload = {
        "model": "deepseek/deepseek-r1-0528:free",
        "messages": [
            {"role": "user", "content": user_message}
        ]
    }
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        
    }
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        data=json.dumps(payload)
    )
    try:
        data = response.json()
        if "choices" in data and data["choices"]:
            reply = data["choices"][0]["message"]["content"]
        elif isinstance(data, dict):
            reply = json.dumps(data)
        else:
            reply = str(data)
    except Exception:
        reply = "Sorry, there was an error processing your request."
    return jsonify({"reply": str(reply)})

if __name__ == "__main__":
    # Use threaded mode for better concurrency and remove debug mode for production
    app.run(host="0.0.0.0", port=5000, threaded=True)