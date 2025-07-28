import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
from preprocess import clean_text

# Step 1: Load dataset
data = pd.read_csv("data/cyberbullying_tweets.csv")

# Step 2: Clean text
data["clean_text"] = data["tweet_text"].apply(clean_text)

# Step 3: TF-IDF Vectorizer
tfidf = TfidfVectorizer(stop_words="english")
X = tfidf.fit_transform(data["clean_text"])
y = data["cyberbullying_type"]

# Step 4: Train model
model = LogisticRegression()
model.fit(X, y)

# Step 5: Save model and vectorizer
with open("models/model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("models/vectorizer.pkl", "wb") as f:
    pickle.dump(tfidf, f)

print("✅ Model and vectorizer saved!")
