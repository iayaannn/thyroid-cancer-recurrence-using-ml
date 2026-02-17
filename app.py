import streamlit as st
import joblib
import pandas as pd

model = joblib.load("model.pkl")

st.title("Thyroid Cancer Recurrence Predictor")

age = st.number_input("Age", 1, 120)
gender = st.selectbox("Gender", ["M", "F"])
radiotherapy = st.selectbox("Hx Radiothreapy", ["Yes", "No"])
adenopathy = st.selectbox("Adenopathy", ["No","Right","Left","Bilateral","Extensive","Posterior"])
pathology = st.selectbox("Pathology", ["Micropapillary","Papillary","Follicular","Hurthel cell"])
focality = st.selectbox("Focality", ["Uni-Focal","Multi-Focal"])
risk = st.selectbox("Risk", ["Low","Intermediate","High"])
T = st.selectbox("T", ["T1a","T1b","T2","T3a","T3b","T4a","T4b"])
N = st.selectbox("N", ["N0","N1a","N1b"])
M = st.selectbox("M", ["M0","M1"])
stage = st.selectbox("Stage", ["I","II","III","IVA","IVB"])
response = st.selectbox("Response", [
    "Excellent","Indeterminate",
    "Biochemical Incomplete","Structural Incomplete"
])

if st.button("Predict"):
    input_df = pd.DataFrame([{
        "Age": age,
        "Gender": gender,
        "Hx Radiothreapy": radiotherapy,
        "Adenopathy": adenopathy,
        "Pathology": pathology,
        "Focality": focality,
        "Risk": risk,
        "T": T,
        "N": N,
        "M": M,
        "Stage": stage,
        "Response": response
    }])

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    if prediction == "Yes" or prediction == 1:
        st.error(f"⚠️ High Recurrence Risk ({probability*100:.2f}%)")
    else:
        st.success(f"✅ Low Recurrence Risk ({probability*100:.2f}%)")
