import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(
    page_title="Health App Hub",
    page_icon=":hospital:",
    layout="wide"
)

# Custom names for the apps
app_names = {
    "Main": "home",
    "Heart Attack Prediction": "heart_attack",
    "Pneumonia Prediction": "pneumonia",
    "Smoking Detection": "smoking03",
    "Healthy Habits Classificator": "healthy_habits",
    "Feedback": "feedback"
}

# Sidebar navigation
selected_app = st.sidebar.radio("### Menu:", list(app_names.keys()))

# Function to get the file name corresponding to the selected app name
def get_app_filename(app_name):
    return app_names.get(app_name)

# Render selected app
if selected_app != "Main":
    selected_app_filename = get_app_filename(selected_app)
    if selected_app_filename in app_names.values():
        selected_app_function = getattr(__import__(selected_app_filename), selected_app_filename)
        selected_app_function()
    else:
        st.title("App Not Found")
        st.write(f"The app '{selected_app}' is not available.")
else:
    st.title("Welcome to Health App Hub! 🏥")
    st.write("Explore and try our health prediction apps. Choose wisely, stay healthy!")

    # Images with descriptions, increased size, and layout changes
    col1, col2, col3, col4 = st.columns(4)
    # Add buttons for each app with the corresponding display name
    with col1:
        image = Image.open("media/heart.jpg")
        st.image(image, width=200, use_column_width=True)
        st.markdown("<h3 style='text-align: center; color: #3cb371;'>Heart Attack Prediction</h3>", unsafe_allow_html=True)
        st.write("The **Heart Attack Prediction App** assesses the likelihood of a heart attack based on factors like age, blood pressure, cholesterol levels, and lifestyle choices. Users input their health parameters to **receive a risk estimation**, empowering them to make informed decisions about their cardiovascular health")

    with col2:
        image = Image.open("media/neumonia.jpg")
        st.image(image, width=200, use_column_width=True)
        st.markdown("<h3 style='text-align: center; color: #3cb371;'>Pneumonia Prediction</h3>", unsafe_allow_html=True)
        st.write("The **Pneumonia Prediction App** analyzes chest X-ray images to determine the **likelihood of pneumonia**. By processing these images, the app provides a **quick and accurate assessment**, aiding in timely medical intervention and treatment decisions")

    with col3:
        image = Image.open("media/smoking.jpg")
        st.image(image, width=200, use_column_width=True)
        st.markdown("<h3 style='text-align: center; color: #3cb371;'>Smoking Habits Detection</h3>", unsafe_allow_html=True)
        st.write("The **Smoking Habits Detection App** identifies smoking behaviors and evaluates related health risks. By analyzing user inputs, it **provides insights into the impact of smoking on overall health**, aiding individuals in understanding the risks associated with tobacco use and encouraging smoking cessation for improved well-being")

    with col4:
        image = Image.open("media/health.jpg")
        st.image(image, width=200, use_column_width=True)
        st.markdown("<h3 style='text-align: center; color: #3cb371;'>Healthy Habits Classification</h3>", unsafe_allow_html=True)
        st.write("The **Healthy Habits Classification App** categorizes individuals' health levels by considering physical performance metrics and personal details. It offers **personalized insights, guiding users to make informed decisions about their well-being** and encouraging healthier lifestyle choices")

st.subheader("Disclaimer:")
st.write("These apps provide general predictions based on the input data. Consult healthcare professionals for accurate diagnoses.")
