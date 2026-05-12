import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Dataset
data = {
    "hours": [1,2,3,4,5,6,7,8,9,10],
    "attendance": [50,55,60,65,70,75,80,85,90,95],
    "marks": [30,35,40,45,50,60,65,70,75,85]
}

df = pd.DataFrame(data)

# Train model
X = df[["hours", "attendance"]]
y = df["marks"]

model = LinearRegression()
model.fit(X, y)

# Streamlit UI
st.title("🎓 Student Performance Predictor")

st.write("Enter student details")

hours = st.slider("Study Hours", 0, 12, 5)
attendance = st.slider("Attendance Percentage", 0, 100, 75)

if st.button("Predict"):
    prediction = model.predict([[hours, attendance]])

    st.success(f"Predicted Marks: {prediction[0]:.2f}")

    if prediction[0] >= 75:
        st.info("Grade: A")
    elif prediction[0] >= 50:
        st.info("Grade: B")
    else:
        st.warning("Grade: C")
