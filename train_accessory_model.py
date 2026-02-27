import pandas as pd
import joblib
import os
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train_accessory_model():

    df = pd.read_csv("data/accessories_dataset.csv")
    df = df.fillna(method="ffill")

    # INPUT FEATURES
    X = df[["gender", "style"]]

    y_cols = [
        "topwear","bottomwear","outerwear","shoes",
        "jewellery","bag","watch","hairstyle",
        "makeup","fragrance","fabric_type","layering_advice"
    ]

    y = df[y_cols]

    # encode inputs
    input_encoders = {}
    for col in X.columns:
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col].astype(str))
        input_encoders[col] = le

    # encode outputs
    target_encoders = {}
    for col in y_cols:
        le = LabelEncoder()
        y[col] = le.fit_transform(y[col].astype(str))
        target_encoders[col] = le

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.15, random_state=42
    )

    model = MultiOutputClassifier(
        RandomForestClassifier(n_estimators=400, max_depth=25, random_state=42)
    )

    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    acc_list = []
    for i in range(len(y_cols)):
        acc = accuracy_score(y_test.iloc[:, i], preds[:, i])
        acc_list.append(acc)

    final_acc = sum(acc_list) / len(acc_list)
    print(f"\n🔥 Accessory Model Accuracy: {final_acc*100:.2f}%")

    os.makedirs("models", exist_ok=True)

    joblib.dump(model, "models/accessory_model.pkl")
    joblib.dump(target_encoders, "models/accessory_target_encoders.pkl")
    joblib.dump(input_encoders, "models/accessory_input_encoders.pkl")

if __name__ == "__main__":
    train_accessory_model()