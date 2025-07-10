from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Server werkt!"

@app.route("/upload", methods=["POST"])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "Geen bestand ontvangen."}), 400

    file = request.files['file']
    save_path = os.path.join("/tmp", file.filename)
    file.save(save_path)

    # Hier komt later de fingerprinting (nu nog niet)
    print(f"Bestand opgeslagen op: {save_path}")

    return jsonify({"status": f"Bestand ontvangen: {file.filename}"}), 200

if __name__ == "__main__":
    # Gebruik de poort die Render doorgeeft, anders standaard 10000
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
