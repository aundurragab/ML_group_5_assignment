import streamlit as st
import pandas as pd
import joblib

# Load the model
model = joblib.load('trained_health_SVClassification_model.sav')

def healthy_habits():
    # Function to take inputs
    def user_input_features():

        gender = st.radio('Gender', ('Female', 'Male'))
        col1, col2 = st.columns(2)

        with col1:
            # One-hot encode gender
            gender_encoded = 1 if gender == 'Male' else 0
            age = st.number_input('Age', value=30)
            height_cm = st.number_input('Height in cm', value=170)
            weight_kg = st.number_input('Weight in kg', value=70)
            body_fat_percent = st.number_input('Body fat percentage', value=25)
            diastolic = st.number_input('Diastolic blood pressure', value=80)
        
        with col2:
            systolic = st.number_input('Systolic blood pressure', value=120)
            gripForce = st.number_input('Grip Force', value=30)
            sit_and_bend_forward_cm = st.number_input('Sit and bend forward in cm', value=15)
            sit_ups_counts = st.number_input('Sit-ups count', value=20)
            broad_jump_cm = st.number_input('Broad jump in cm', value=200)

        # Create input data as a dictionary with correct feature names
        data = {
            'ohe__gender_F': [1 - gender_encoded],  # Complement of gender_Male
            'ohe__gender_M': [gender_encoded],
            'scaler__age': [age],
            'scaler__height_cm': [height_cm],
            'scaler__weight_kg': [weight_kg],
            'scaler__body fat_%': [body_fat_percent],
            'scaler__diastolic': [diastolic],
            'scaler__systolic': [systolic],
            'scaler__gripForce': [gripForce],
            'scaler__sit and bend forward_cm': [sit_and_bend_forward_cm],
            'scaler__sit-ups counts': [sit_ups_counts],
            'scaler__broad jump_cm': [broad_jump_cm],
        }
        features = pd.DataFrame(data)
        return features

    st.markdown("<h1 style='text-align: center;'>Healthy Habits Classificator 🍏🏋️‍♂️🌞</h1>", unsafe_allow_html=True)
    
    # Centered image
    col1, col2, col3 = st.columns(3)  # Create three columns for layout
    with col2:  # Use the middle column for the centered image
        st.image('media/healthy.jpg', width=500, use_column_width=False)

    # Get user input
    input_df = user_input_features()

    # Prediction button
    if st.button("Predict"):
        # Predict
        prediction = model.predict(input_df)

        # Map prediction to corresponding category
        categories = {
            1: 'A: Apex Vitality (The Pinnacle Performers)',
            2: 'B: Robust Wellness (The Steady Strivers)',
            3: 'C: Moderate Health (The Health Conscious)',
            4: 'D: Developing Health (The Path to Progress)'
        }

        predicted_category = categories[prediction[0]]

        # Display prediction
        st.write("## Prediction")
        st.write(predicted_category)
        st.write("Recommended Actions:")
        if prediction == 1:
            st.write("- Maintain regular exercise routines to sustain peak performance.")
            st.write("- Focus on balanced nutrition and hydration.")
            st.write("- Encourage participation in advanced fitness activities to challenge and enhance abilities.")
        elif prediction == 2:
            st.write("- Engage in regular physical activities to maintain and improve current fitness levels.")
            st.write("- Emphasize flexibility and agility exercises to enhance overall mobility.")
            st.write("- Monitor and manage stress levels for holistic health.")
        elif prediction == 3:
            st.write("- Adopt a well-rounded exercise routine that includes both cardiovascular and strength-training exercises.")
            st.write("- Focus on improving specific areas of weakness identified by the model.")
            st.write("- Explore healthier dietary choices and portion control.")
        elif prediction == 4:
            st.write("- Consult with fitness professionals or healthcare providers to create a personalized fitness plan.")
            st.write("- Start with low-impact exercises and gradually increase intensity.")
            st.write("- Embrace a balanced diet, emphasizing fruits, vegetables, and whole grains.")

if __name__ == '__main__':
    healthy_habits()
