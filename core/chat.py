from core.model import load_model
from core.utils import clean_text

model_data = load_model()
model = model_data["model"]
vectorizer = model_data["vectorizer"]
intents = model_data["intents"]

def get_response(message):
    cleaned = clean_text(message)
    X = vectorizer.transform([cleaned])
    intent = model.predict(X)[0]
    responses = intents[intent]
    import random
    return random.choice(responses)
