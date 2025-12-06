# train_model.py
# Train a simple TF-IDF + LogisticRegression classifier and save model + vectorizer.

import os
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

TRAIN_FILE = "training_data.txt"
MODEL_PATH = "model.pkl"
VECT_PATH = "vectorizer.pkl"

def load_training_file(path):
    texts = []
    labels = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            # expect format: sentence,label
            try:
                sentence, label = line.rsplit(",", 1)
            except ValueError:
                # skip bad lines
                continue
            texts.append(sentence)
            labels.append(label)
    return texts, labels

def train_and_save():
    if not os.path.exists(TRAIN_FILE):
        print(f"Training file '{TRAIN_FILE}' not found. Add training examples first.")
        return

    texts, labels = load_training_file(TRAIN_FILE)
    if len(texts) < 6:
        print("Warning: very small training set. Add more examples for better results.")

    # split for evaluation
    X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)

    # vectorize
    vect = TfidfVectorizer(ngram_range=(1,2), max_features=2000)
    X_train_tfidf = vect.fit_transform(X_train)
    X_test_tfidf = vect.transform(X_test)

    # classifier
    clf = LogisticRegression(max_iter=1000)
    clf.fit(X_train_tfidf, y_train)

    # evaluate
    y_pred = clf.predict(X_test_tfidf)
    acc = accuracy_score(y_test, y_pred)
    print("Validation accuracy:", acc)
    print(classification_report(y_test, y_pred))

    # save
    joblib.dump(clf, MODEL_PATH)
    joblib.dump(vect, VECT_PATH)
    print(f"Saved model to {MODEL_PATH} and vectorizer to {VECT_PATH}")

if __name__ == "__main__":
    train_and_save()
