from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)
summarizer = pipeline("summarization")
classifier = pipeline("zero-shot-classification")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json['article']
    summary = summarizer(data, max_length=60, min_length=20, do_sample=False)[0]['summary_text']
    labels = ["Politics", "Sports", "Technology", "Entertainment", "Health"]
    result = classifier(data, candidate_labels=labels)
    return jsonify({
        "summary": summary,
        "category": result['labels'][0]
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)
