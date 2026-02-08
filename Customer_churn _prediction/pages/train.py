import streamlit as st
import pandas as pd
from ml.preprocess import preprocess_data
from ml.model import train_model
def train_page():
    st.header("📊 Train Model")
    df = pd.read_csv("data/churn.csv")
    st.write("Training Data", df)
    if st.button("Train Model"):
        X, y, encoder = preprocess_data(df)
        model = train_model(X, y)
        st.session_state.model = model
        st.session_state.encoder = encoder
        st.success("Model trained successfully")