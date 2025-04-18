import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from core.model import save_model

def train_model():
    with open("data/intents.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    texts, labels, responses_map = [], [], {}

    for intent in data["intents"]:
        tag = intent["tag"]
        responses_map[tag] = intent["responses"]
        for pattern in intent["patterns"]:
            texts.append(pattern)
            labels.append(tag)

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(texts)
    clf = MultinomialNB()
    clf.fit(X, labels)

    save_model({"model": clf, "vectorizer": vectorizer, "intents": responses_map})

if __name__ == "__main__":
    train_model()
