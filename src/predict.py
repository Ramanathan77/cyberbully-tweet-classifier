import pickle
from preprocess import clean_text

def load_model():
    with open("models/model.pkl", "rb") as f:
        model = pickle.load(f)
    with open("models/vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)
    return model, vectorizer

def predict_text(text):
    model, vectorizer = load_model()
    cleaned = clean_text(text)
    vector = vectorizer.transform([cleaned])
    prediction = model.predict(vector)[0]
    return prediction

# Test it
if __name__ == "__main__":
    tweet = input("Enter a tweet: ")
    result = predict_text(tweet)
    print("🔍 Prediction:", result)
