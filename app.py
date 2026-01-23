from flask import Flask, request, jsonify
from deep_translator import GoogleTranslator
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows frontend JS to call the backend

@app.route("/translate", methods=["POST"])
def translate_text():
    data = request.json
    source = data.get("source_language")
    target = data.get("target_language")
    text = data.get("text")

    try:
        translated = GoogleTranslator(source=source, target=target).translate(text)
        return jsonify({"translated_text": translated})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
