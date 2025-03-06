# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 20:52:12 2024

@author: Zain Ali
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


#Loading the saved models

diabetes_model=pickle.load(open('https://github.com/ZainAli879/Multidisease-Prediction-System/blob/main/Saved%20Models/diabetes_model.sav','rb'))

heart_disease_model=pickle.load(open('https://github.com/ZainAli879/Multidisease-Prediction-System/blob/main/Saved%20Models/heart_disease_model.sav','rb'))

parkinsons_model=pickle.load(open('https://github.com/ZainAli879/Multidisease-Prediction-System/blob/main/Saved%20Models/parkinsons_model.sav','rb'))

#sidebar for navigation

with st.sidebar:
    selected=option_menu('Multiple Disease Prediction System',
                         ['Diabetes Prediction','Heart Disease Prediction','Parkinsons Prediction'],icons=['activity','heart','person'],default_index=0)
    
if selected == 'Diabetes Prediction':
    st.title("Diabetes Prediction Using ML")

    # Getting the input data from user
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")
    with col2:
        Glucose = st.text_input("Glucose Level", key="glucose_input")
    with col3:
        BloodPressure = st.text_input("Blood Pressure value", key="blood_pressure_input")
    with col1:
        SkinThickness = st.text_input("SkinThickness value", key="skin_thickness_input")
    with col2:
        Insulin = st.text_input("Insulin value", key="insulin_input")
    with col3:
        BMI = st.text_input("BMI value", key="bmi_value")
    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function Value", key="diabetes_pedigree_value")
    with col2:
        Age = st.text_input("Age of Person", key="age_value")

    # Code for prediction
    diab_diagnosis = ''

    # Creating a button for prediction
    if st.button("Diabetes Test Result"):
        try:
            # Convert inputs to float
            input_data = [float(Pregnancies), float(Glucose), float(BloodPressure), float(SkinThickness), 
                          float(Insulin), float(BMI), float(DiabetesPedigreeFunction), float(Age)]
            
            diab_prediction = diabetes_model.predict([input_data])
            
            if diab_prediction[0] == 1:
                diab_diagnosis = "Person is Diabetic"
            else:
                diab_diagnosis = "Person is not Diabetic"
        except ValueError as e:
            st.error(f"Input conversion error: {e}")

    st.success(diab_diagnosis)

    
    
    
if(selected=='Heart Disease Prediction'):
    st.title("Heart Disease Prediction Using Ml")
    col1,col2,col3=st.columns(3)
    
    with col1:
         age=st.text_input("Age",key="age_input")   
    with col2:
         sex=st.text_input("Sex",key="sex_input")
    with col3:
         cp=st.text_input("Chest pain type(cp)", key="cp_input")
    with col1:
         trestbps=st.text_input("Resting blood pressure value(trestbps)",key="trestbps_input") 
    with col2:
         chol=st.text_input("cholesterol value(chol)",key="chol_input")       
    with col3:
         fbs=st.text_input("Fasting blood sugar value(fbs)",key="fbs_input")
    with col1:
         restcg=st.text_input("Resting electrocardiographic value(restcg)",key="restcg_input")
    with col2:
         thalach=st.text_input("Maximum heart rate value(thalach)", key="thalach_value")
    with col3:
         exang=st.text_input(" exercise-induced angina value(exang)",key="exang_value")
    with col1:
         oldpeak =st.text_input("oldpeak value(oldpeak)",key="oldpeak_value")
    with col2:
         slope=st.text_input("solpe value(slope)", key="slope_value")
    with col3:
         ca=st.text_input(" Coronary artery disease value(ca)",key="ca_value")
    with col1:
         thal =st.text_input("Thalassemia value(thal)",key="thal_value")
         
    #code for prediction
  
    heart_diagnosis= ''
   
    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

       user_input = [age, sex, cp, trestbps, chol, fbs, restcg, thalach, exang, oldpeak, slope, ca, thal]

       user_input = [float(x) for x in user_input]

       heart_prediction = heart_disease_model.predict([user_input])

       if heart_prediction[0] == 1:
           heart_diagnosis = 'The person is having heart disease'
       else:
           heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)
    
    
    
    
# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
