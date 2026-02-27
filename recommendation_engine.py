import joblib
import pandas as pd

# Load trained style model
style_model = joblib.load("models/style_model.pkl")

# Load preprocessing objects
feature_encoders = joblib.load("models/style_feature_encoders.pkl")
target_encoder = joblib.load("models/style_target_encoder.pkl")
scaler = joblib.load("models/style_scaler.pkl")

# Load accessories dataset
accessories_df = pd.read_csv("data/accessories_dataset.csv")


def preprocess_input(input_df):

    # Encode categorical features using saved encoders
    for col, encoder in feature_encoders.items():
        if col in input_df.columns:
            input_df[col] = encoder.transform(input_df[col].astype(str))

    # Scale
    input_scaled = scaler.transform(input_df)

    return input_scaled


def predict_style_and_accessories(user_input_dict):

    input_df = pd.DataFrame([user_input_dict])

    # Preprocess
    input_processed = preprocess_input(input_df)

    # Predict encoded style
    encoded_prediction = style_model.predict(input_processed)[0]

    # Decode to original style name
    predicted_style = target_encoder.inverse_transform([encoded_prediction])[0]

    selected_gender = user_input_dict["gender"]

    # Fetch accessories
    recommendation = accessories_df[
        (accessories_df["style"] == predicted_style) &
        (accessories_df["gender"] == selected_gender)
    ]

    if recommendation.empty:
        return predicted_style, {}

    return predicted_style, recommendation.iloc[0].to_dict()