import streamlit as st
def init_session():
    if "model" not in st.session_state:
        st.session_state.model = None
    if "encoder" not in st.session_state:
        st.session_state.encoder = None