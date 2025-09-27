import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split

def preprocess(csv_path):
    df = pd.read_csv(csv_path)

    # Replace zeros in specific columns with np.nan (except for target column)
    columns_with_zero = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
    
    # Convert all pd.NA to np.nan (this is the fix)
    df = df.replace({pd.NA: np.nan})

    # Replace 0s with np.nan in the relevant columns
    df[columns_with_zero] = df[columns_with_zero].replace(0, np.nan)

    # Impute missing values using mean strategy
    imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
    df[columns_with_zero] = imputer.fit_transform(df[columns_with_zero])

    # Split features and target
    X = df.drop('Outcome', axis=1)
    y = df['Outcome']

    # Train-test split
    return train_test_split(X, y, test_size=0.2, random_state=42)
