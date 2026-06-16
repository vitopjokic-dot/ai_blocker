from datasets import load_dataset
import numpy as np
import re
import joblib
from collections import Counter
from sklearn.linear_model import LogisticRegression

ds = load_dataset("Hello-SimpleAI/HC3", "all")

X = []
y = []

def clean(text):
    return text.replace("\n", " ").strip()


def features(text):
    words = text.lower().split()
    if not words:
        return [0, 0, 0]

    freq = Counter(words)
    repetition = sum(v for v in freq.values() if v > 1) / len(words)
    lexical_diversity = len(set(words)) / len(words)
    avg_word_len = sum(len(w) for w in words) / len(words)

    return [repetition, lexical_diversity, avg_word_len]


for item in ds["train"]:
    for h in item["human_answers"]:
        X.append(clean(h))
        y.append(0)

    for a in item["chatgpt_answers"]:
        X.append(clean(a))
        y.append(1)

X_feat = np.array([features(t) for t in X])


model = LogisticRegression(max_iter=300)
model.fit(X_feat, y)

print("find")


joblib.dump(model, "ai_detector_model.pkl")
joblib.dump(features, "feature_fn.pkl")

print("saved")
