AI Model for Cyberbullying Tweet Classification

This project uses an AI-powered machine learning model to classify tweets as either cyberbullying or non-cyberbullying. It leverages natural language processing (NLP) techniques and a logistic regression classifier to analyze and predict harmful content in social media text.

Features

Preprocessing tweets by cleaning and vectorizing text data.

Classifying tweets into binary labels: cyberbullying or non-cyberbullying.

Saving and reusing the trained model and vectorizer for predictions.

A deployable framework for integrating AI into web applications.



Technologies Used

Python: Core programming language.

Scikit-learn: Model training and evaluation.

NLTK: For preprocessing text data.

Pandas: For managing datasets.

Flask (optional): For deployment as a web application.



---

How It Works

1. Data Preprocessing:

Tweets are cleaned by removing URLs, mentions, special characters, and stopwords.

The text is vectorized using the TF-IDF method.



2. Model Training:

A logistic regression model is trained on labeled tweet data to classify tweets.



3. Prediction:

The trained model is used to predict if a given tweet contains cyberbullying content.





---

Setup Instructions

1. Clone the Repository:

git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name


2. Install Dependencies: Install the required Python libraries:

pip install -r requirements.txt


3. Run the Prediction Script:

Prepare a sample tweet for testing:

tweet = "You are worthless and no one cares!"

Use the trained model and vectorizer for predictions:

processed_tweet = preprocess_text(tweet)
vectorized_tweet = vectorizer.transform([processed_tweet])
prediction = model.predict(vectorized_tweet)
print("Prediction:", prediction[0])  # Output: cyberbullying or non-cyberbullying

Results

Accuracy: ~80% on test data.

The model demonstrates effective detection of harmful content in social media text.

Project Structure

cyberbullying-tweet-classification/
├── models/
│   ├── model.pkl           # Trained logistic regression model
│   └── vectorizer.pkl      # TF-IDF vectorizer
├── data/
│   └── dataset.csv         # Training dataset
├── src/
│   ├── preprocess.py       # Preprocessing functions
│   ├── train_model.py      # Script for training the model
│   └── predict.py          # Prediction script
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies


Future Enhancements

Use a larger dataset for better performance.
