# 📊 Flipkart Product Review Sentiment Analysis using NLP
https://nlp-sentiment-analysis-flipkart-reviews-qmwdp2ptqrvdk5zkcijqrh.streamlit.app/

An end-to-end Natural Language Processing (NLP) project that classifies Flipkart product reviews into **Positive**, **Neutral**, and **Negative** sentiments using Machine Learning.

The project demonstrates the complete NLP workflow, including text preprocessing, feature engineering, model training, evaluation, and prediction on unseen customer reviews.

---

## 📌 Project Overview

Customer reviews contain valuable insights that help businesses understand user satisfaction and improve their products. This project builds a sentiment analysis model using over **20,000 Flipkart product reviews**.

The workflow includes:

- Data Cleaning
- Text Preprocessing
- Feature Engineering using TF-IDF
- Model Training
- Model Evaluation
- Sentiment Prediction

---

## 🚀 Features

- Cleaned and preprocessed 100K+ product reviews
- Removed HTML tags, emojis, punctuation, numbers, and extra spaces
- Converted text to lowercase
- Tokenization
- Stopword Removal
- Lemmatization
- TF-IDF Feature Extraction
- Trained multiple Machine Learning models
- Compared model performance
- Predict sentiment for custom user reviews

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- NLTK
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib

---

## 📂 Project Structure

```
flipkart-product-review-sentiment-analysis/
│
├── data/
│   └── flipkart_reviews.csv
│
├── notebook/
│   └── Flipkart_Sentiment_Analysis.ipynb
│
├── model/
│   ├── sentiment_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── images/
│
├── README.md
├── requirements.txt
└── app.py
```

---

## ⚙️ NLP Pipeline

```
Raw Dataset
      │
      ▼
Data Cleaning
      │
      ▼
HTML Removal
      │
      ▼
Emoji Removal
      │
      ▼
Lowercase Conversion
      │
      ▼
Punctuation & Number Removal
      │
      ▼
Tokenization
      │
      ▼
Stopword Removal
      │
      ▼
Lemmatization
      │
      ▼
TF-IDF Vectorization
      │
      ▼
Model Training
      │
      ▼
Model Evaluation
      │
      ▼
Sentiment Prediction
```

---

## 🤖 Machine Learning Models

The following classification models were implemented and compared:

- Logistic Regression
- Multinomial Naive Bayes

Evaluation metrics include:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

---

## 💬 Sample Prediction

**Input Review**

```
Amazing camera quality and excellent battery life.
```

**Predicted Sentiment**

```
Positive 😊
```

---

## 📈 Libraries Used

```python
pandas
numpy
nltk
scikit-learn
matplotlib
seaborn
joblib
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/flipkart-product-review-sentiment-analysis.git
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Open the notebook

```
notebook/Flipkart_Sentiment_Analysis.ipynb
```

or run the Streamlit application (if included):

```bash
streamlit run app.py
```

---

## 📌 Future Improvements

- Deploy using Streamlit
- Compare with Linear SVM
- Fine-tune using BERT
- Deploy on Hugging Face Spaces
- Dockerize the application
- Add REST API using FastAPI

---

## 📚 Skills Demonstrated

- Natural Language Processing (NLP)
- Text Cleaning
- Feature Engineering
- TF-IDF
- Machine Learning
- Text Classification
- Data Preprocessing
- Model Evaluation
- Python
- Scikit-learn

---

## 👨‍💻 Author

**Aditya Singh**

M.Sc. Data Science | IIIT Lucknow

If you found this project useful, consider giving it a ⭐ on GitHub.
