import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image as keras_image
from PIL import Image

def pneumonia():

    # Load model
    model = load_model('pneumonia_model.h5')

    st.markdown("<h1 style='text-align: center;'>Pneumonia Prediction App </h1>", unsafe_allow_html=True)


# Centered image
    col1, col2, col3 = st.columns(3)  # Create three columns for layout
    with col2:  # Use the middle column for the centered image
        st.image('media/lung-logo.jpg', width=500, use_column_width=False)

    
    with st.expander("ℹ️ - About this app", expanded=True):
        st.write("""
        Welcome to the Pneumonia Prediction App! This application utilizes a deep learning model to analyze chest X-ray images 
        and predict the likelihood of pneumonia. Our goal is to provide a quick and preliminary analysis to aid healthcare professionals.
        - **How to use:** Upload a chest X-ray image in JPEG format, and the model will analyze the image and provide a prediction.
        - **Note:** This app should not be used as a sole diagnostic tool. Consult a healthcare professional for an accurate diagnosis.
        """)

    # Upload image through streamlit
    uploaded_file = st.file_uploader("Please upload an X-ray image of your chest", type="jpeg")

    # Functionality of the app
    if uploaded_file is not None:
        img = Image.open(uploaded_file).convert('L')  # Convert image to grayscale
        st.image(img, caption='Uploaded X-ray image.', use_column_width=True)

        # Preprocess the image to match model input
        img = img.resize((128, 128))
        img_array = keras_image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.

        # Create a placeholder for the "Classifying..." message
        message_placeholder = st.empty()
        message_placeholder.text("Classifying...")

        # Make prediction
        prediction = model.predict(img_array)
        prediction_value = prediction[0][0] * 100  # Convert to percentage
        message_placeholder.empty()  # Clear the "Classifying..." message
        st.write('Result:')

        if prediction_value < 50:
            st.success(f"Good news! The X-ray image is classified as Normal. The model is {100 - prediction_value:.2f}% confident.")
            st.image('media/lung-success.jpg', width=500)
        else:
            st.error(f"Bad news. The X-ray image is classified as Pneumonia. The model is {prediction_value:.2f}% confident and we strongly suggest you consult a healthcare professional.")
            st.image('media/lung-checkup.jpg', width=500)

    pass

