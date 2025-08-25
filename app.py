import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load model and encoder
model_path = r"model.pkl"
encoder_path = r"encoder.pkl"

with open(model_path, "rb") as f:
    model = pickle.load(f)

with open(encoder_path, "rb") as f:
    encoder = pickle.load(f)

# App title and description
st.title("🧠 Mental Health Treatment Prediction App")
st.markdown("Predict whether someone is likely to seek mental health treatment based on their responses.")

# User Input
age = st.slider("Age", 18, 60, 25)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
self_employed = st.selectbox("Self-employed", ["Yes", "No"])
family_history = st.selectbox("Family History of Mental Illness?", ["Yes", "No"])
work_interfere = st.selectbox("Mental Health Affects Work?", ['Never', 'Rarely', 'Sometimes', 'Often', 'N/A'])
no_employees = st.selectbox("Number of Employees", ['1-5', '6-25', '26-100', '100-500', '500-1000', 'More than 1000'])
remote_work = st.selectbox("Do You Work Remotely?", ['Yes', 'No'])
tech_company = st.selectbox("Is it a Tech Company?", ['Yes', 'No'])
benefits = st.selectbox("Company Offers Mental Health Benefits?", ['Yes', 'No', "Don't know"])
care_options = st.selectbox("Care Options Available?", ['Yes', 'No', "Not sure"])
wellness_program = st.selectbox("Has Wellness Program?", ['Yes', 'No', "Don't know"])
seek_help = st.selectbox("Encouraged to Seek Help?", ['Yes', 'No', "Don't know"])
anonymity = st.selectbox("Anonymity Maintained?", ['Yes', 'No', "Don't know"])
leave = st.selectbox("Ease of Taking Leave?", ['Very easy', 'Somewhat easy', 'Don’t know', 'Somewhat difficult', 'Very difficult'])
mental_health_consequence = st.selectbox("Mental Health Consequence at Work?", ['Yes', 'No', 'Maybe'])
phys_health_consequence = st.selectbox("Physical Health Consequence at Work?", ['Yes', 'No', 'Maybe'])
coworkers = st.selectbox("Comfortable Talking to Coworkers?", ['Yes', 'No', 'Some of them'])
supervisor = st.selectbox("Comfortable Talking to Supervisor?", ['Yes', 'No', 'Some of them'])
mental_health_interview = st.selectbox("Discuss Mental Health in Interview?", ['Yes', 'No', 'Maybe'])
phys_health_interview = st.selectbox("Discuss Physical Health in Interview?", ['Yes', 'No', 'Maybe'])
mental_vs_physical = st.selectbox("Mental vs Physical Importance?", ['Yes', 'No', 'Don’t know'])
obs_consequence = st.selectbox("Observed Consequences?", ['Yes', 'No'])

# Prepare input as dictionary with correct column names
input_data = {
    "Gender": gender,
    "self_employed": self_employed,
    "family_history": family_history,
    "work_interfere": work_interfere,
    "no_employees": no_employees,
    "remote_work": remote_work,
    "tech_company": tech_company,
    "benefits": benefits,
    "care_options": care_options,
    "wellness_program": wellness_program,
    "seek_help": seek_help,
    "anonymity": anonymity,
    "leave": leave,
    "mental_health_consequence": mental_health_consequence,
    "phys_health_consequence": phys_health_consequence,
    "coworkers": coworkers,
    "supervisor": supervisor,
    "mental_health_interview": mental_health_interview,
    "phys_health_interview": phys_health_interview,
    "mental_vs_physical": mental_vs_physical,
    "obs_consequence": obs_consequence,
    "Age": age
}

# Convert to DataFrame
input_df = pd.DataFrame([input_data])

# Transform input using encoder
transformed_input = encoder.transform(input_df)

# Predict
if st.button("🔍 Predict"):
    prediction = model.predict(transformed_input)
    if prediction[0] == 1:
        st.error("⚠️ This person is likely to require mental health treatment.")
    else:
        st.success("✅ This person is unlikely to require mental health treatment.")
