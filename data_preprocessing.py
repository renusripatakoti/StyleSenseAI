import pandas as pd
import joblib
import os
from sklearn.preprocessing import LabelEncoder, StandardScaler

def preprocess_style_data(file_path):

    df = pd.read_csv(file_path)

    # Fill missing
    df = df.fillna(method="ffill")

    X = df.drop("target_style", axis=1)
    y = df["target_style"]

    categorical_cols = X.select_dtypes(include=["object"]).columns

    encoders = {}
    for col in categorical_cols:
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col].astype(str))
        encoders[col] = le

    target_encoder = LabelEncoder()
    y = target_encoder.fit_transform(y.astype(str))

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    os.makedirs("models", exist_ok=True)

    joblib.dump(encoders, "models/style_feature_encoders.pkl")
    joblib.dump(target_encoder, "models/style_target_encoder.pkl")
    joblib.dump(scaler, "models/style_scaler.pkl")

    return X_scaled, y