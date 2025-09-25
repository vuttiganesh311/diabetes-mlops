import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

def preprocess(csv_path):
    df = pd.read_csv(csv_path)

    # Replace zeroes with NaN in specific columns
    columns_with_zero = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]
    df[columns_with_zero] = df[columns_with_zero].replace(0, pd.NA)

    imputer = SimpleImputer(strategy="mean")
    df[columns_with_zero] = imputer.fit_transform(df[columns_with_zero])

    X = df.drop("Outcome", axis=1)
    y = df["Outcome"]
    return train_test_split(X, y, test_size=0.2, random_state=42)
