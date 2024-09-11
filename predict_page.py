import numpy as np
import pandas as pd
import pickle
import streamlit as st

def load_model():
    with open('gold_price_prediction_model.pkl','rb') as file:
        data = pickle.load(file)
        return data
    
data = load_model()
model = data['model']   # Random forest classsifier
    
    # [SPX, USO, SLV, EUR/USD]

def show_predicted_page():

    st.write("""### need some details for prediction """)

    SPX, USO, SLV, EUR_USD =st.columns(4)

    x1 = SPX.text_input("SPX Rate :")
    x2 = USO.text_input("USO:")
    x3 = SLV.text_input("SLV:")
    x4 = EUR_USD.text_input("EUR_USD Price:")

    ok = st.button("Predict")

    if ok:
        x1 = float(x1)
        x2 = float(x2)
        x3 = float(x3)
        x4 = float(x4)
        X = np.asarray([[x1,x2,x3,x4]])
        x_reshaped = X.reshape(1,-1)

        prediction = model.predict(x_reshaped)
        
        st.success(f"The Price of Gold in EUR/USD is {prediction[0]}")
        