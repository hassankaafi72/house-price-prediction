import streamlit as st
import pandas as pd
import joblib

# Load your model
model = joblib.load('house_model.pkl')

st.title("🏠 House Price Predictor")
st.write("Enter house details to get an estimated price.")

# Inputs for your 4 features
area = st.number_input("Living Area (Sqft)", value=1500)
beds = st.slider("Bedrooms", 1, 6, 3)
baths = st.slider("Bathrooms", 1, 4, 2)
qual = st.slider("Overall Quality (1-10)", 1, 10, 5)

if st.button("Predict Price"):
    features = pd.DataFrame([[area, beds, baths, qual]], 
                            columns=['GrLivArea', 'BedroomAbvGr', 'FullBath', 'OverallQual'])
    prediction = model.predict(features)[0]
    st.success(f"Estimated Price: ${prediction:,.2f}")
