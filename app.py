# app.py

import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load(r'C:\Users\vijay\OneDrive\Desktop\MICP\Notebooks\insurance_model.pkl')

# Title
st.title("🧾 Insurance Cost Predictor")
st.write("Enter your details below to estimate your insurance cost.")

# User Inputs
age = st.number_input("Age", min_value=0, max_value=120, value=30)
sex = st.selectbox("Sex", options=['male', 'female'])
bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0)
children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
smoker = st.selectbox("Smoker", options=['yes', 'no'])
region = st.selectbox("Region", options=['northeast', 'northwest', 'southeast', 'southwest'])

# Prediction
if st.button("Predict"):
    input_df = pd.DataFrame({
        'age': [age],
        'sex': [sex],
        'bmi': [bmi],
        'children': [children],
        'smoker': [smoker],
        'region': [region]
    })

    prediction = model.predict(input_df)
    st.success(f"💰 Estimated Insurance Cost: ${round(prediction[0], 2)}")
