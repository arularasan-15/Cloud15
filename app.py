import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.set_page_config(page_title="Student Predictor", layout="centered")

st.title(" Student Performance Predictor")

st.write("Enter student details to predict marks")

# Inputs
hours = st.slider("Study Hours per Day", 0, 12, 5)
attendance = st.slider("Attendance (%)", 0, 100, 75)

# Predict
if st.button("Predict Marks"):
    prediction = model.predict([[hours, attendance]])
    marks = round(prediction[0], 2)

    st.success(f" Predicted Marks: {marks}")

    # Grade logic
    if marks >= 75:
        st.info("Grade: A 🟢 Excellent")
    elif marks >= 50:
        st.info("Grade: B 🟡 Good")
    else:
        st.warning("Grade: C  Needs Improvement")

    # Simple chart
    chart_data = pd.DataFrame({
        "Category": ["Study Hours", "Attendance", "Marks"],
        "Value": [hours, attendance, marks]
    })
    st.bar_chart(chart_data.set_index("Category"))
