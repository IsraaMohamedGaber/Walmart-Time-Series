import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load trained model
with open(r'E:\israa\ITI 9 Months\Time Series\Project\models\random_forest_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("Walmart Weekly Sales Forecast - Dept 6")

st.markdown("### Enter Features for the Forecast Week:")

# Input form
is_holiday = st.selectbox("Is Holiday?", [0, 1])
temperature = st.number_input("Temperature", value=70.0)
fuel_price = st.number_input("Fuel Price", value=3.0)
cpi = st.number_input("CPI", value=220.0)
unemployment = st.number_input("Unemployment", value=7.0)
week = st.slider("Week Number", 1, 52, 24)
month = st.slider("Month", 1, 12, 6)
year = st.slider("Year", 2012, 2015, 2012)
day_of_week = st.slider("Day of Week (0=Mon)", 0, 6, 5)
lag_1 = st.number_input("Lag 1", value=15000.0)
lag_2 = st.number_input("Lag 2", value=14500.0)
lag_3 = st.number_input("Lag 3", value=14000.0)
rolling_3 = st.number_input("3-Week Rolling Mean", value=14500.0)
rolling_5 = st.number_input("5-Week Rolling Mean", value=14200.0)

# Predict
if st.button("Predict Sales"):
    input_data = pd.DataFrame([[is_holiday, temperature, fuel_price, cpi, unemployment,
                                week, month, year, day_of_week, lag_1, lag_2, lag_3,
                                rolling_3, rolling_5]],
                              columns=['IsHoliday', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment',
                                       'Week', 'Month', 'Year', 'DayOfWeek', 'Lag_1', 'Lag_2', 'Lag_3',
                                       'Rolling_Mean_3', 'Rolling_Mean_5'])

    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Weekly Sales: ${prediction:,.2f}")
