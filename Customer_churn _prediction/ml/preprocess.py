import pandas as pd
from sklearn.preprocessing import OneHotEncoder
def preprocess_data(df):
    X = df.drop("Churn", axis=1)
    y = df["Churn"].map({"Yes": 1, "No": 0})
    cat_cols = ["Contract", "InternetService"]
    num_cols = ["tenure", "MonthlyCharges"]
    encoder = OneHotEncoder(handle_unknown="ignore", sparse_output=False)
    X_cat = encoder.fit_transform(X[cat_cols])
    X_num = X[num_cols].values
    X_processed = pd.DataFrame(
    X_cat,
    columns=encoder.get_feature_names_out(cat_cols)
)
    X_processed[num_cols] = X_num
    return X_processed, y, encoder