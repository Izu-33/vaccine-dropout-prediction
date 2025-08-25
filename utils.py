import joblib
import pandas as pd
import numpy as np

def load_model_and_features(model_path, features_path, scaler_path):
    with open(model_path, "rb") as f:
        model = joblib.load(f)
    with open(features_path, "rb") as f:
        features = joblib.load(f)
    with open(scaler_path, "rb") as f:
        scaler = joblib.load(f)
    return model, features, scaler

def preprocess_input(user_input_df, all_feature_columns, scaler, numerical_features):
    df_encoded = pd.get_dummies(user_input_df, columns=["CountryCode", "Region"], drop_first=True, dtype=int)
    for col in all_feature_columns:
        if col not in df_encoded.columns:
            df_encoded[col] = 0
    df_encoded[numerical_features] = scaler.transform(df_encoded[numerical_features])
    df_encoded = df_encoded[all_feature_columns]
    return df_encoded