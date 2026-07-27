import streamlit as st
import joblib

# Load pre-trained artifacts (do NOT retrain/save inside the app)
model = joblib.load(r"C:\Users\adity\Downloads\sentiment_model.pkl")
vectorizer = joblib.load(r"C:\Users\adity\Downloads\tfidf_vectorizer.pkl")

st.title("📊 Flipkart Product Review Sentiment Analysis")

review = st.text_area("Enter Product Review")

if st.button("Predict"):
    if review.strip() == "":
        st.warning("Please enter a review first.")
    else:
        # Transform input using the same vectorizer used during training
        review_vec = vectorizer.transform([review])

        # Predict class
        prediction = model.predict(review_vec)[0]

        # Optional: get probability/confidence if the model supports it
        try:
            proba = model.predict_proba(review_vec)[0]
            confidence = max(proba) * 100
        except AttributeError:
            confidence = None

        label_map = {0: "Negative 😞", 1: "Positive 😀"}  # adjust to your actual label encoding
        result = label_map.get(prediction, str(prediction))

        st.subheader(f"Sentiment: {result}")
        if confidence is not None:
            st.write(f"Confidence: {confidence:.2f}%")