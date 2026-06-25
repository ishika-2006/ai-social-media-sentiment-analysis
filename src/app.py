from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get('text', '')

    sentiment = "Positive" if "love" in text.lower() else "Negative"

    return jsonify({
        "text": text,
        "sentiment": sentiment
    })

@app.route('/api/history', methods=['GET'])
def history():
    return jsonify([
        {
            "text": "I love this product",
            "sentiment": "Positive"
        }
    ])

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({
        "status": "Healthy"
    })

if __name__ == '__main__':
    app.run(debug=True)
