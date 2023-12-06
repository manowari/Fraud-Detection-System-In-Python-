# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load your dataset (assuming it has 'text' and 'label' columns)
# For fraud detection, you might have text data related to transactions or user activities.
# Example data loading:
# data = pd.read_csv("your_fraud_dataset.csv")

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data['text'], data['label'], test_size=0.2, random_state=42)

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Sentiment Analysis Model (Logistic Regression)
sentiment_model = LogisticRegression()
sentiment_model.fit(X_train_tfidf, y_train)
sentiment_predictions = sentiment_model.predict(X_test_tfidf)

# Evaluate the model
print("Sentiment Analysis Model Evaluation:")
print(f"Accuracy: {accuracy_score(y_test, sentiment_predictions)}")
print("Classification Report:\n", classification_report(y_test, sentiment_predictions))
