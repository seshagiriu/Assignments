import streamlit as st
from sklearn.linear_model import LogisticRegression
@st.cache_resource
def train_model(X, y):
    model = LogisticRegression()
    model.fit(X, y)
    return model