from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
from data_preprocessing import preprocess_style_data

def train_style_model():

    X, y = preprocess_style_data("data/fashion_dataset.csv")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.15, random_state=42
    )

    model = RandomForestClassifier(
        n_estimators=500,
        max_depth=25,
        random_state=42
    )

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    print(f"\n🔥 Style Model Accuracy: {acc*100:.2f}%")

    joblib.dump(model, "models/style_model.pkl")

if __name__ == "__main__":
    train_style_model()