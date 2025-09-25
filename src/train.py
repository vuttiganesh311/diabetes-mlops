from sklearn.ensemble import RandomForestClassifier
import joblib
from src.preprocess import preprocess

def train_model(csv_path="data/raw/diabetes.csv", model_path="model/model.pkl"):
    X_train, X_test, y_train, y_test = preprocess(csv_path)
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)
    joblib.dump(clf, model_path)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    train_model()
