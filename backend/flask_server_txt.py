from flask import Flask, request, jsonify
from flask_cors import CORS
import hashlib
import joblib
import numpy as np
import model_test
from collections import Counter
app = Flask(__name__)
CORS(app)

cache = {}

def make_key(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.get_json()
        text = data.get("text", "")
        key = make_key(text)
        if key in cache:
            print("cache yes")
            return jsonify({
                "ai_score": cache[key],
                "cached": True
            })
        print("no chache")
        if len(text)<50:
            return jsonify({
            "ai_score": 0.0,
            "cached": False
        })
        score = model_test.predict(text)
        cache[key] = score
        return jsonify({
            "ai_score": score,
            "cached": False
        })

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)
