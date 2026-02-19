# ============================================
# 🌍 Air Quality Health Impact Prediction App
# Single File - Fully Corrected Version
# ============================================

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# --------------------------------------------
# Page Config
# --------------------------------------------
st.set_page_config(page_title="Air Quality Health Impact", layout="wide")

st.title("🌍 Air Quality Health Impact Prediction System")
st.markdown("Predict health risk level based on air pollution parameters")

# --------------------------------------------
# Generate Sample Dataset (Safe Version)
# --------------------------------------------
@st.cache_data
def load_data():
    np.random.seed(42)

    data = pd.DataFrame({
        "PM2.5": np.random.randint(10, 200, 500),
        "PM10": np.random.randint(20, 300, 500),
        "NO2": np.random.randint(5, 150, 500),
        "SO2": np.random.randint(1, 80, 500),
        "CO": np.random.uniform(0.1, 10, 500),
        "O3": np.random.randint(10, 180, 500)
    })

    # Safe and Professional way using pd.cut
    data["Health Impact"] = pd.cut(
        data["PM2.5"],
        bins=[0, 50, 100, 1000],
        labels=["Low", "Moderate", "High"]
    )

    return data


data = load_data()

# --------------------------------------------
# Model Training
# --------------------------------------------
X = data.drop("Health Impact", axis=1)
y = data["Health Impact"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# --------------------------------------------
# Sidebar User Input
# --------------------------------------------
st.sidebar.header("🔎 Enter Air Quality Parameters")

pm25 = st.sidebar.number_input("PM2.5", min_value=0.0, value=40.0)
pm10 = st.sidebar.number_input("PM10", min_value=0.0, value=80.0)
no2 = st.sidebar.number_input("NO2", min_value=0.0, value=30.0)
so2 = st.sidebar.number_input("SO2", min_value=0.0, value=10.0)
co = st.sidebar.number_input("CO", min_value=0.0, value=1.5)
o3 = st.sidebar.number_input("O3", min_value=0.0, value=60.0)

input_data = pd.DataFrame({
    "PM2.5": [pm25],
    "PM10": [pm10],
    "NO2": [no2],
    "SO2": [so2],
    "CO": [co],
    "O3": [o3]
})

# --------------------------------------------
# Prediction Section
# --------------------------------------------
st.subheader("🔮 Prediction Result")

if st.button("Predict Health Impact"):

    prediction = model.predict(input_data)[0]

    if prediction == "Low":
        st.success("🟢 Health Impact: LOW RISK")
        st.info("Air quality is acceptable. Minimal health concern.")

    elif prediction == "Moderate":
        st.warning("🟡 Health Impact: MODERATE RISK")
        st.info("Sensitive individuals may experience minor health effects.")

    else:
        st.error("🔴 Health Impact: HIGH RISK")
        st.info("Serious health effects possible. Avoid outdoor exposure.")

# --------------------------------------------
# Model Performance
# --------------------------------------------
st.subheader("📊 Model Performance")
st.write(f"Model Accuracy: {accuracy:.2f}")

# --------------------------------------------
# Visualization
# --------------------------------------------
st.subheader("📈 PM2.5 Distribution")

fig, ax = plt.subplots()
ax.hist(data["PM2.5"], bins=20)
ax.set_xlabel("PM2.5 Level")
ax.set_ylabel("Frequency")
st.pyplot(fig)

# --------------------------------------------
# Show Dataset
# --------------------------------------------
with st.expander("📂 View Full Dataset"):
    st.write(data)
