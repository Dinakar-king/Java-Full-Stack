from transformers import pipeline


# Load the BERT sentiment analysis pipeline (do this once)
classifier = pipeline("sentiment-analysis")


def analyze_sentiment(text: str):
    text_input =[text]
    results = classifier(text_input)
    formatted = []
    for text, result in zip(text_input, results):
        print(f"text-input : {text}")
        formatted.append({
            "text": text,
            "label": result["label"],
            "score": round(result["score"], 4)
        })


    return formatted