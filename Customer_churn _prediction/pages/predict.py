import streamlit as st
import pandas as pd
def predict_page():
    st.header("🔮 Predict Churn")
    if st.session_state.model is None:
        st.warning("Please train the model first")
        return
    tenure = st.slider("Tenure (months)", 0, 72, 12)
    charges = st.slider("Monthly Charges", 20, 120, 70)
    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    internet = st.selectbox("Internet Service", ["DSL", "Fiber"])
    input_df = pd.DataFrame([{
        "tenure": tenure,
        "MonthlyCharges": charges,
        "Contract": contract,
        "InternetService": internet
    }])
    encoder = st.session_state.encoder
    model = st.session_state.model
    X_cat = encoder.transform(input_df[["Contract", "InternetService"]])
    X_num = input_df[["tenure", "MonthlyCharges"]].values
    X_input = pd.concat(
    [
    pd.DataFrame(X_cat, columns=encoder.get_feature_names_out()),
    pd.DataFrame(X_num, columns=["tenure", "MonthlyCharges"])
    ],
    axis=1
    )
    if st.button("Predict"):
        prob = model.predict_proba(X_input)[0][1]
        st.metric("Churn Probability", f"{prob:.2%}")
        if prob > 0.5:
            st.error("⚠️ High risk of churn")
        else:
            st.success("✅ Low risk of churn")