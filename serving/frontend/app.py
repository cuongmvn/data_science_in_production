import joblib
import pandas as pd
import streamlit as st
from PIL import Image

from inference import load_model, predict_dataframe

st.title('My 1st ML app')

model = load_model()

# Upload display image
uploaded_file = st.file_uploader('Choose an image')
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

# Multipe CSV file
csv_file = st.file_uploader('Choose a CSV file')
if csv_file:
    st.write('filename : ', csv_file.name)
    dataframe = pd.read_csv(csv_file)
    st.write(dataframe)

# Model prediction
if st.button('Predict diabetes progression') and csv_file:
    model_input_data = dataframe#.read_csv(csv_file)
    predictions = predict_dataframe(model, model_input_data)
    print("here3")
    st.success(f'Predictions : {predictions}')


# One line text
user_input = st.text_input('label goes here', 'one liner')
print(user_input)

# Multi line text
user_input = st.text_area('Your feedback on the model predictions?', 'Empty feedback')
print(user_input)