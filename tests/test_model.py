from core.model import load_model

def test_load_model():
    modelo = load_model()
    assert "model" in modelo
    assert "vectorizer" in modelo
    assert "intents" in modelo
