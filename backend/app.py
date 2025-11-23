from flask import Flask, request, jsonify
from joblib import load
from features import extract_features   # <- the correct extractor here
import os

app = Flask(__name__)

# Load model
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")
if os.path.exists(MODEL_PATH):
    model = load(MODEL_PATH)
else:
    model = None
    print("WARNING: model.pkl not found. Using dummy logic.")


def classify_url(url: str):
    """Return label + score based on ML model or fallback rules."""
    global model

    if model is None:
        score = 0.0
        low = url.lower()
        for w in ["login", "verify", "update", "bank", "secure", "free", "win"]:
            if w in low:
                score += 0.3
        if "https://" not in low:
            score += 0.2
        score = min(score, 1.0)
    else:
        features = extract_features(url)       # <-- uses correct 12-feature extractor
        prob = model.predict_proba([features])[0][1]
        score = float(prob)

    if score < 0.3:
        label = "safe"
    elif score < 0.7:
        label = "suspicious"
    else:
        label = "malicious"

    return label, score


@app.route("/check_url", methods=["POST"])
def check_url():
    data = request.json
    url = data.get("url", "")
    if not url:
        return jsonify({"error": "No URL provided"}), 400

    label, score = classify_url(url)
    return jsonify({"label": label, "score": score})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
