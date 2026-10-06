##data set-https://www.kaggle.com/datasets/milobele/sentiment140-dataset-1600000-tweets/data
##In this project we are going to perform sentiment analysis using twitter data set
# Twitter Sentiment Analysis

A Python machine learning project that performs sentiment analysis on Twitter data and classifies tweets as Negative, Neutral, or Positive.

## What the Program Does

- Loads and preprocesses Twitter data
- Removes mentions, URLs, unwanted characters, and stopwords
- Applies lemmatization to the text
- Converts text into numerical features using TF-IDF
- Splits the data into training and testing sets
- Trains a Logistic Regression model
- Evaluates the model using accuracy and classification metrics
- Tracks the experiment using MLflow
- Saves the trained model and TF-IDF vectorizer

## Technologies Used

Python, Pandas, NLTK, Scikit-learn, TF-IDF, Logistic Regression, MLflow, and Joblib.

## Main Files

- `main.py` - runs the complete pipeline
- `scripts/preprocess.py` - cleans and preprocesses the tweets
- `scripts/train.py` - trains the sentiment classification model
- `scripts/evaluate.py` - evaluates the trained model

## Dataset

Sentiment140 Twitter Dataset:
https://www.kaggle.com/datasets/milobele/sentiment140-dataset-1600000-tweets/data
