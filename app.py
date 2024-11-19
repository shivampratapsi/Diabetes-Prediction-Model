import streamlit as st
import joblib
import numpy as np
import pickle

model = joblib.load("myDiabitData .pkl")


st.title("Diabetes Prediction App")

st.header("Now please move your mouse to know your state😇 :")

age = st.slider("Age", 1, 120, 15)
gender = st.selectbox("Gender", ("Male", "Female"))
smoking_history = st.selectbox(
    "Smoking History",
    ("No Info","current","former", "ever", "not current","never")
)
heart_disease = st.selectbox("Heart Disease", ("No", "Yes"))
hypertension = st.selectbox("Hypertension", ("No", "Yes"))
bmi = st.slider("BMI", 10.0, 30.0, 18.0)
hba1c_level = st.slider("HbA1c Level", 3.0, 15.0, 3.5)
blood_Glucose_Level = st.slider("Blood Glucose Level", 50, 300, 100)

gender = 1 if gender == "Male" else 0
hypertension = 1 if hypertension == "Yes" else 0
heart_disease = 1 if heart_disease == "Yes" else 0

smokhistory_dictionary = {
    "ever": 0,
    "current": 1,
    "former": 2,
    "not current": 3,
    "never": 4,
    "No Info": 5
}
smoking_history = smokhistory_dictionary[smoking_history]

input_data = np.array([[ age,gender,smoking_history ,heart_disease, hypertension,bmi, hba1c_level, blood_Glucose_Level]])
prediction = model.predict(input_data)[0]

st.write("Please click below predict button ->")

if st.button("Predict"):
    if prediction == 1:
        st.write("Oww😨 ! You are a **diabetic person**.")
        st.write("**Gonna low your sugar intake 🥣🥣**.")
    else:
        st.write("Good👍 **you don't have diabetes**.")
        st.write("**Are 👁️you👁️ satisfied !**.")



        
with open('gender_classification_model.pkl', 'wb') as file:
    pickle.dump(model,file)