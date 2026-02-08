import streamlit as st
from state.session import init_session
from pages.train import train_page
from pages.predict import predict_page
st.set_page_config(page_title="Churn Prediction App")
init_session()
page = st.sidebar.selectbox("Navigation", ["Train Model", "Predict"])
if page == "Train Model":
    train_page()
else:
    predict_page()