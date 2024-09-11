from predict_page import show_predicted_page
from show_page import show_explore_page
import streamlit as st

st.title("Gold Price Prediction")
page = st.selectbox("Explore Analysis Or Predict", ("Predict", "Explore"))

if page == "Predict":
    show_predicted_page()
else:
    show_explore_page()