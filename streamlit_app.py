import streamlit as st
import numpy as np
import joblib

# Load the model
model = joblib.load("model.pkl")

# Origin and destination lists
origin_stations = ['Abdullah Hukum', 'Bangi', 'Bank Negara', 'Batu Tiga', 'Bandar Tasek Selatan',
    'Jalan Templer', 'Kajang', 'Kampung Batu', 'KL Sentral', 'Klang', 'Kuala Lumpur', 'Nilai',
    'Midvalley', 'Petaling', 'Pulau Sebang (Tampin)', 'Rawang', 'Serdang', 'Setia Jaya',
    'Subang Jaya', 'Sungai Buloh', 'Tanjong Malim', 'Batu Caves', 'Seremban', 'Shah Alam', 'UKM',
    'Sentul', 'Padang Jawa', 'Pelabuhan Klang Selatan', 'Sungai Gadut', 'Telok Gadong',
    'Telok Pulai', 'Tiroi', 'Unknown', 'Batang Benar', 'Batang Kali', 'Bukit Badak', 'Jalan Kastam',
    'Kajang 2', 'Kepong', 'Kepong Sentral', 'Kampung Dato Harun', 'Kampung Raja Uda',
    'Kuala Kubu Bharu', 'Kuang', 'Labu', 'Pantai Dalam', 'Putra', 'Rasa', 'Rembau', 'Salak Selatan',
    'Segambut', 'Senawang', 'Seputeh', 'Serendah', 'Seri Setia', 'Taman Wahyu', 'Angkasapuri',
    'Batu Kentonmen']

destination_stations = origin_stations  # assume same options

# Streamlit UI
st.title("🚉 Komuter Ridership Predictor")

hour = st.selectbox("Hour (0-23)", list(range(24)))
day_of_week = st.selectbox("Day of Week", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
is_weekend = st.radio("Is it Weekend?", ["No", "Yes"])
origin = st.selectbox("Origin Station", origin_stations)
destination = st.selectbox("Destination Station", destination_stations)

# Convert inputs
day_index = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].index(day_of_week)
is_weekend_binary = 1 if is_weekend == "Yes" else 0
origin_encoded = origin_stations.index(origin)
destination_encoded = destination_stations.index(destination)

# Predict
if st.button("Predict Ridership"):
    features = np.array([[hour, day_index, is_weekend_binary, origin_encoded, destination_encoded]])
    prediction = round(model.predict(features)[0])
    st.success(f"Estimated Ridership: **{prediction}** passengers")
