from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        mensaje = data["mensaje"]

        print("Mensaje recibido:", mensaje)

        r = requests.post(
            "http://127.0.0.1:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": mensaje,
                "stream": False
            }
        )

        respuesta = r.json()["response"]

        print("Respuesta IA:", respuesta)

        return jsonify({"respuesta": respuesta})

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"respuesta": "Error 😢"})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
    