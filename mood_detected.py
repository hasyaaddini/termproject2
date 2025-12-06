# mood_detector.py
# Load trained model + vectorizer and expose predict_mood(text).
# If model files are missing, fall back to a simple keyword-based classifier.

import os
import joblib

MODEL_PATH = "model.pkl"
VECT_PATH = "vectorizer.pkl"

# Simple keyword fallback (kept small and similar to what you already had)
keyword_mood = {
    "happy": ["happy", "wonderful", "amazing", "excited", "glad", "joyful"],
    "sad": ["sad", "depressed", "down", "unhappy", "sorrowful"],
    "angry": ["angry", "furious", "pissed", "annoyed", "irritated"]
}

model = None
vectorizer = None
use_ml = False

def try_load_model():
    global model, vectorizer, use_ml
    if os.path.exists(MODEL_PATH) and os.path.exists(VECT_PATH):
        try:
            model = joblib.load(MODEL_PATH)
            vectorizer = joblib.load(VECT_PATH)
            use_ml = True
            # print("Loaded ML model.")
        except Exception:
            model = None
            vectorizer = None
            use_ml = False

# call on import
try_load_model()

def simple_keyword_predict(text):
    text = text.lower()
    counts = {m:0 for m in keyword_mood}
    for m, words in keyword_mood.items():
        for w in words:
            if w in text:
                counts[m] += 1
    best = max(counts, key=lambda k: counts[k])
    if counts[best] == 0:
        return "neutral"
    return best

def predict_mood(text):
    text = text.strip()
    if not text:
        return "neutral"
    if use_ml and model is not None and vectorizer is not None:
        try:
            X = vectorizer.transform([text])
            pred = model.predict(X)[0]
            return pred
        except Exception:
            # fallback to keyword
            return simple_keyword_predict(text)
    else:
        return simple_keyword_predict(text)
