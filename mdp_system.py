# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 23:21:15 2022

@author: Vallarasu
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved models
diabetes_model = pickle.load(open('diabetes_model.sav' , 'rb'))

heartdisease_model = pickle.load(open('heartdisease_model.sav' , 'rb'))

parkinsonsdisease_model = pickle.load(open('parkinsonsdisease_model.sav' , 'rb'))

kidneydisease_model = pickle.load(open('kidneydisease_model.sav' , 'rb'))

#sidebar for navigation

with st.sidebar:
    
    selected = option_menu('Muliple Disease Prediction System',
                           ['Diabetes Prediction','Heart Disease Prediction',
                            'Parkinsons Disease Prediction',
                            'Kidney Disease Prediction'],
                           
                           icons = ['activity','heart','person','egg'],
                           
                           default_index = 0)
    

# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age')
        
    with col2:
        sex = st.number_input('Sex')
        
    with col3:
        cp = st.number_input('Chest Pain types')
        
    with col1:
        chol = st.number_input('Serum Cholestoral in mg/dl')
        
    with col2:
        restecg = st.number_input('Resting Electrocardiographic results')
        
    with col3:
        thalach = st.number_input('Maximum Heart Rate achieved')
        
    with col1:
        oldpeak = st.number_input('ST depression induced by exercise')
        
    with col2:
        ca = st.number_input('Major vessels colored by flourosopy')
        
    with col3:
        thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heartdisease_model.predict([[age, sex, cp, chol, restecg, thalach, oldpeak, ca, thal]])                          
        
        if (heart_prediction[0] == 0):
            heart_diagnosis = 'The person is not having heart disease'
        else:
            heart_diagnosis = 'The person have heart disease'
        
    st.success(heart_diagnosis)
        
    
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Disease Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3 = st.columns(3)  
    
    with col1:
        fo = st.text_input('MDVP.Fo(Hz)')
        
    with col2:
        PPQ = st.text_input('MDVP.PPQ')
        
    with col3:
        DDP = st.text_input('Jitter.DDP')
              
    with col1:
        APQ = st.text_input('MDVP.APQ')
        
    with col2:
        DDA = st.text_input('Shimmer.DDA')
        
    with col3:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col1:
        spread1 = st.text_input('spread1')
        
    with col2:
        spread2 = st.text_input('spread2')
           
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsonsdisease_model.predict([[fo,PPQ,DDP,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2]])                          
        
        if (parkinsons_prediction[0] == 1):
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)
    
    
# Kidney Prediction Page
if (selected == 'Kidney Disease Prediction'):
    
    # page title
    st.title('Kidney Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Bp = st.number_input('Blood Pressure Value')
        
    with col2:
        Sg = st.number_input('Specific Gravity Value')
    
    with col3:
        Al = st.number_input('Albumin Value')
    
    with col1:
        Su = st.number_input('Sugar Level')
    
    with col2:
        Bu = st.number_input('Blood Urea Value')
    
    with col3:
        Sc= st.number_input('Serum Creatinine Value')
    
    with col1:
        Sod = st.number_input('Sodium Value')
    with col2:
        Pot = st.number_input('Pottasium Value')
    
    with col3:
        Hemo = st.number_input('Heamoglobin Level')
    
    with col1:
        Wbcc = st.number_input('White Blood Cells Count Value')
    
    with col2:
        Rbcc = st.number_input('Red Blood Cells Count Value')
    
    with col3:
        Htn = st.number_input('Hypertension Value')
    
    
    # code for Prediction
    kidney_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Kidney Test Result'):
        kidney_prediction = kidneydisease_model.predict([[Bp,Sg,Al,Su,Bu,Sc,Sod,Pot,Hemo,Wbcc,Rbcc,Htn]])
        
        if (kidney_prediction[0] == 1):
            kidney_diagnosis = 'The person has a Kidney disease'
        else:
            kidney_diagnosis = 'The person does not have a Kidney disease'
        
    st.success(kidney_diagnosis)