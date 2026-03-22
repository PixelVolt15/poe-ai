from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "PoE AI funcionando 🚀"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        mensaje = data["mensaje"]

        respuesta = f"Dijiste: {mensaje}"

        return jsonify({"respuesta": respuesta})

    except:
        return jsonify({"respuesta": "Error 😢"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    