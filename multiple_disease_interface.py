# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 20:52:12 2024

@author: Zain Ali
"""

import pickle
import streamlit as st
import requests
import os
from streamlit_option_menu import option_menu

# Function to download model from GitHub
def download_model(url, filename):
    if not os.path.exists(filename):  # Download only if not already downloaded
        response = requests.get(url)
        if response.status_code == 200:
            with open(filename, "wb") as f:
                f.write(response.content)
        else:
            st.error(f"Failed to download {filename}. Check the URL.")

# GitHub RAW URLs (Ensure these are correct)
diabetes_model_url = "https://raw.githubusercontent.com/ZainAli879/Multidisease-Prediction-System/main/Saved%20Models/diabetes_model.sav"
heart_model_url = "https://raw.githubusercontent.com/ZainAli879/Multidisease-Prediction-System/main/Saved%20Models/heart_disease_model.sav"
parkinsons_model_url = "https://raw.githubusercontent.com/ZainAli879/Multidisease-Prediction-System/main/Saved%20Models/parkinsons_model.sav"

# Local filenames
diabetes_model_file = "diabetes_model.sav"
heart_model_file = "heart_disease_model.sav"
parkinsons_model_file = "parkinsons_model.sav"

# Download models
download_model(diabetes_model_url, diabetes_model_file)
download_model(heart_model_url, heart_model_file)
download_model(parkinsons_model_url, parkinsons_model_file)

# Load models safely
try:
    with open(diabetes_model_file, "rb") as f:
        diabetes_model = pickle.load(f)

    with open(heart_model_file, "rb") as f:
        heart_disease_model = pickle.load(f)

    with open(parkinsons_model_file, "rb") as f:
        parkinsons_model = pickle.load(f)

    st.success("Models loaded successfully!")

except Exception as e:
    st.error(f"Error loading models: {e}")

# Sidebar for navigation
with st.sidebar:
    selected = option_menu(
        'Multiple Disease Prediction System',
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
        icons=['activity', 'heart', 'person'],
        default_index=0
    )

if selected == 'Diabetes Prediction':
    st.title("Diabetes Prediction Using ML")

    # Getting the input data from user
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")
    with col2:
        Glucose = st.text_input("Glucose Level")
    with col3:
        BloodPressure = st.text_input("Blood Pressure value")
    with col1:
        SkinThickness = st.text_input("SkinThickness value")
    with col2:
        Insulin = st.text_input("Insulin value")
    with col3:
        BMI = st.text_input("BMI value")
    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function Value")
    with col2:
        Age = st.text_input("Age of Person")

    diab_diagnosis = ''

    if st.button("Diabetes Test Result"):
        try:
            input_data = list(map(float, [Pregnancies, Glucose, BloodPressure, SkinThickness,
                                          Insulin, BMI, DiabetesPedigreeFunction, Age]))
            
            diab_prediction = diabetes_model.predict([input_data])

            diab_diagnosis = "Person is Diabetic" if diab_prediction[0] == 1 else "Person is not Diabetic"

        except ValueError as e:
            st.error(f"Input conversion error: {e}")

    st.success(diab_diagnosis)

if selected == 'Heart Disease Prediction':
    st.title("Heart Disease Prediction Using ML")

    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input("Age")
    with col2:
        sex = st.text_input("Sex")
    with col3:
        cp = st.text_input("Chest pain type (cp)")
    with col1:
        trestbps = st.text_input("Resting blood pressure (trestbps)")
    with col2:
        chol = st.text_input("Cholesterol level (chol)")
    with col3:
        fbs = st.text_input("Fasting blood sugar (fbs)")
    with col1:
        restcg = st.text_input("Resting electrocardiographic results (restcg)")
    with col2:
        thalach = st.text_input("Maximum heart rate (thalach)")
    with col3:
        exang = st.text_input("Exercise-induced angina (exang)")
    with col1:
        oldpeak = st.text_input("Oldpeak")
    with col2:
        slope = st.text_input("Slope")
    with col3:
        ca = st.text_input("Number of major vessels (ca)")
    with col1:
        thal = st.text_input("Thalassemia (thal)")

    heart_diagnosis = ''

    if st.button('Heart Disease Test Result'):
        try:
            user_input = list(map(float, [age, sex, cp, trestbps, chol, fbs, restcg,
                                          thalach, exang, oldpeak, slope, ca, thal]))

            heart_prediction = heart_disease_model.predict([user_input])

            heart_diagnosis = "Person has heart disease" if heart_prediction[0] == 1 else "Person does not have heart disease"

        except ValueError as e:
            st.error(f"Input conversion error: {e}")

    st.success(heart_diagnosis)

if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction using ML")

    inputs = []
    labels = ['MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)', 'MDVP:Jitter(Abs)',
              'MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP', 'MDVP:Shimmer', 'MDVP:Shimmer(dB)',
              'Shimmer:APQ3', 'Shimmer:APQ5', 'MDVP:APQ', 'Shimmer:DDA', 'NHR', 'HNR',
              'RPDE', 'DFA', 'spread1', 'spread2', 'D2', 'PPE']

    col1, col2 = st.columns(2)
    for i, label in enumerate(labels):
        with col1 if i % 2 == 0 else col2:
            inputs.append(st.text_input(label))

    parkinsons_diagnosis = ''

    if st.button("Parkinson's Test Result"):
        try:
            user_input = list(map(float, inputs))

            parkinsons_prediction = parkinsons_model.predict([user_input])

            parkinsons_diagnosis = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"

        except ValueError as e:
            st.error(f"Input conversion error: {e}")

    st.success(parkinsons_diagnosis)
