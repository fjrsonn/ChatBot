import pickle
import os

def save_model(model, path="model/classifier.pkl"):
    with open(path, "wb") as f:
        pickle.dump(model, f)

def load_model(path="model/classifier.pkl"):
    if not os.path.exists(path):
        raise FileNotFoundError("Modelo não treinado encontrado.")
    with open(path, "rb") as f:
        return pickle.load(f)
