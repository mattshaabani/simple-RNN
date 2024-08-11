import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import load_model

# Load the IMDB dataset word Index
word_index = imdb.get_word_index()
reverse_word_index = {value : key for key, value in word_index.items()}

# Load the pre-trained model with ReLU activation
model = load_model('simple_RNN_imdb.keras')

# user input preprocesser
def preprocess_text(text):
  words = text.lower().split()
  encoded_review = [word_index.get(word, 2) + 3 for word in words]
  padded_review = sequence.pad_sequences([encoded_review], maxlen = 500)
  return padded_review

# reviews decoder
def decode_review(text):
    return ' '.join([reverse_word_index.get(i - 3, '?') for i in text])

# Streamlit App
import streamlit as st
st.title('IMDB Movie Review Sentiment Analysis')
st.write('Enter a movie review to classify it as positive or negative')

# User INput
user_input = st.text_area('Movie Review')

if st.button('Classify'):
   preprocessed_input = preprocess_text(user_input)

   # Make prediction
   prediction = model.predict(preprocessed_input)
   sentiment = 'Positive' if prediction[0][0] > 0.5 else 'Negative'

   # Display the result
   st.write(f'Sentiment: {sentiment}')
   st.write(f'Prediction Score: {prediction[0][0]}')
else:
   st.write('Please enter a movie review')