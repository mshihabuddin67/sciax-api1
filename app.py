from flask import Flask, request, jsonify
from services.analyzer import analyze

app = Flask(__name__)

@app.route("/")
def home():
    return "S-CIAX v2 Running"

@app.route("/analyze", methods=["POST"])
def analyze_route():
    data = request.json
    prompt = data.get("prompt", "")

    result = analyze(prompt)

    return jsonify({
        "status": "ok",
        "result": result
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
