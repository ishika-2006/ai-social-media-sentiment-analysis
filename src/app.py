from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# -----------------------------
# Sentiment Analysis API
# -----------------------------
@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.get_json()

    text = data.get("text", "").lower()

    # Simple rule-based sentiment logic
    positive_words = ["good", "great", "excellent", "love", "happy", "amazing", "nice", "best"]
    negative_words = ["bad", "worst", "hate", "sad", "angry", "terrible", "poor", "awful"]

    if any(word in text for word in positive_words):
        sentiment = "Positive"
    elif any(word in text for word in negative_words):
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return jsonify({
        "input_text": data.get("text"),
        "sentiment": sentiment
    })


# -----------------------------
# History API (sample data)
# -----------------------------
@app.route('/api/history', methods=['GET'])
def history():
    return jsonify([
        {"text": "I love this product", "sentiment": "Positive"},
        {"text": "This is very bad service", "sentiment": "Negative"},
        {"text": "It is okay overall", "sentiment": "Neutral"}
    ])


# -----------------------------
# User API (demo)
# -----------------------------
@app.route('/api/users', methods=['GET'])
def users():
    return jsonify([
        {"user_id": 1, "username": "user_one"},
        {"user_id": 2, "username": "user_two"}
    ])


# -----------------------------
# Feedback API
# -----------------------------
@app.route('/api/feedback', methods=['POST'])
def feedback():
    data = request.get_json()

    return jsonify({
        "status": "Feedback stored successfully",
        "rating": data.get("rating"),
        "comments": data.get("comments")
    })


# -----------------------------
# Health Check API
# -----------------------------
@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"status": "Healthy", "service": "Sentiment Analysis API"})


if __name__ == '__main__':
    app.run(debug=True)
